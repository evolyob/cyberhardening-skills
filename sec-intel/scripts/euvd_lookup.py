#!/usr/bin/env python3
"""
Resilient Vulnerability Intelligence Client (v2.1)
Dual-Engine Fallback: ENISA EUVD (EPSS & CVSS) + Google OSV.dev + CISA SSVC.
"""

import argparse
import json
import re
from urllib import parse, request
from typing import Any, Dict, List, Optional

EUVD_API_BASE = "https://euvdservices.enisa.europa.eu/api"
OSV_API_BASE = "https://api.osv.dev/v1/vulns"
CVE_ORG_API_BASE = "https://cveawg.mitre.org/api/cve"


def _fetch_json(url: str, timeout: int = 5) -> Optional[Dict[str, Any]]:
    """Fetch JSON payload from URL with standard headers; return None on error."""
    req = request.Request(
        url, headers={"User-Agent": "SecIntel-Resilient/2.1", "Accept": "application/json"}
    )
    try:
        with request.urlopen(req, timeout=timeout) as resp:
            if resp.status != 200:
                return None
            return json.loads(resp.read().decode("utf-8", errors="replace"))
    except Exception:
        return None


def _sla_tier(exposed: bool, kev: bool, auto: bool, total: bool) -> Optional[str]:
    """Return 'urgent' (3d), 'careful' (14d), or None via minimal MODA 115/11/06 rule."""
    if (exposed + kev + auto + total) >= 3:
        return "urgent"
    if kev or (exposed and (auto or total)):
        return "careful"
    return None


def _extract_cve_id(item: Dict[str, Any]) -> Optional[str]:
    """Extract first CVE-YYYY-NNNN identifier from item id or aliases."""
    for text in (str(item.get("id") or ""), str(item.get("aliases") or "")):
        m = re.search(r"CVE-\d{4}-\d+", text, re.I)
        if m:
            return m.group(0).upper()
    return None


def fetch_cisa_ssvc(cve_id: str, timeout: int = 4) -> Optional[Dict[str, str]]:
    """Fetch CISA Vulnrichment SSVC metrics from CVE.org."""
    data = _fetch_json(f"{CVE_ORG_API_BASE}/{parse.quote(cve_id.upper())}", timeout=timeout)
    if not data:
        return None
    metrics = [
        m.get("other", {})
        for adp in data.get("containers", {}).get("adp", [])
        for m in adp.get("metrics", [])
        if m.get("other", {}).get("type") == "ssvc"
    ]
    if not metrics:
        return None
    opts = {
        k: str(v)
        for opt in metrics[0].get("content", {}).get("options", [])
        if isinstance(opt, dict)
        for k, v in opt.items()
    }
    return opts or None


def _enrich_ssvc(item: Dict[str, Any], timeout: int = 4) -> None:
    """Attach CISA SSVC metrics and urgent/careful SLA tags to item in-place."""
    if not item.get("ssvc"):
        cve_id = _extract_cve_id(item)
        if not cve_id:
            return
        ssvc = fetch_cisa_ssvc(cve_id, timeout=timeout)
        if not ssvc:
            return
        item["ssvc"] = ssvc
    ssvc = item["ssvc"]
    if "Automatable" not in ssvc or "Technical Impact" not in ssvc:
        return
    kev = ssvc.get("Exploitation", "").lower() == "active" or bool(item.get("exploitedSince"))
    auto = ssvc.get("Automatable", "").lower() == "yes"
    total = ssvc.get("Technical Impact", "").lower() == "total"
    sla = {
        k: v
        for k, v in (("exposed", _sla_tier(True, kev, auto, total)), ("internal", _sla_tier(False, kev, auto, total)))
        if v
    }
    if sla:
        item["sla"] = sla


def fetch_from_osv(cve_or_id: str, timeout: int = 5) -> Optional[Dict[str, Any]]:
    """Fallback Engine: Google OSV.dev Anycast CDN API."""
    target = cve_or_id.strip().upper()
    data = _fetch_json(f"{OSV_API_BASE}/{parse.quote(target)}", timeout=timeout)
    if not data or not data.get("id"):
        return None

    cvss_score, cvss_ver = "參見細節", "N/A"
    for sev in data.get("severity", []):
        if sev.get("type") in ("CVSS_V3", "CVSS_V4", "CVSS_V2"):
            cvss_ver = sev["type"].replace("CVSS_", "")
            m = re.search(r"CVSS:[0-9.]+/.*?/([0-9.]+)", sev.get("score", ""))
            cvss_score = m.group(1) if m else sev.get("score", "")

    products = [
        aff.get("package", {}).get("name") or aff.get("database_specific", {}).get("cpe", [""])[0]
        for aff in data.get("affected", [])
    ]
    return {
        "source": "Google OSV.dev (Fallback CDN)",
        "id": data.get("id", target),
        "aliases": "\n".join(data.get("aliases", [])),
        "description": data.get("details") or data.get("summary") or "",
        "datePublished": data.get("published"),
        "dateUpdated": data.get("modified"),
        "baseScore": cvss_score,
        "baseScoreVersion": cvss_ver,
        "baseScoreVector": "-",
        "epss": None,
        "assigner": data.get("database_specific", {}).get("cna_assigner", "OSV.dev"),
        "products": [p for p in products if p][:3],
    }


def query_euvd_by_id(cve_or_euvd_id: str, timeout: int = 5) -> Dict[str, Any]:
    """Query vulnerability by CVE or EUVD ID with automatic Google OSV.dev fallback."""
    target = cve_or_euvd_id.strip().upper()
    data = _fetch_json(f"{EUVD_API_BASE}/enisaid?id={parse.quote(target)}", timeout=timeout)
    if data and not data.get("error"):
        data["source"] = "ENISA EUVD (Primary)"
        _enrich_ssvc(data, timeout=timeout)
        return data
    osv_data = fetch_from_osv(target, timeout=timeout)
    if osv_data:
        _enrich_ssvc(osv_data, timeout=timeout)
        return osv_data
    return {"error": f"雙引擎查詢皆無此漏洞紀錄 (ENISA EUVD & Google OSV.dev): '{target}'"}


def query_euvd_search(
    text: str, size: int = 5, page: int = 0,
    from_score: Optional[float] = None, from_epss: Optional[float] = None, timeout: int = 6
) -> Dict[str, Any]:
    """Search EUVD vulnerability records with fallback to direct OSV lookup if query is a CVE ID."""
    clean_text = text.strip()
    if re.fullmatch(r"(?:CVE|EUVD)-\d{4}-\d+", clean_text, re.I):
        single = query_euvd_by_id(clean_text, timeout=timeout)
        return single if "error" in single else {"items": [single], "total": 1, "source": single.get("source")}

    params = {"text": clean_text, "size": str(size), "page": str(page)}
    if from_score is not None:
        params["fromScore"] = str(from_score)
    if from_epss is not None:
        params["fromEpss"] = str(from_epss)

    data = _fetch_json(f"{EUVD_API_BASE}/search?{parse.urlencode(params)}", timeout=timeout)
    if not data:
        return {"error": "ENISA EUVD 查詢連線異常"}
    data["source"] = "ENISA EUVD (Primary)"
    for item in data.get("items", []):
        _enrich_ssvc(item, timeout=min(timeout, 4))
    return data


def is_urgent_sla(item: Dict[str, Any]) -> bool:
    """Return True if item triggers 3-day (urgent) or 14-day (careful) SLA."""
    return bool(item.get("sla"))


def _extract_products(item: Dict[str, Any]) -> List[str]:
    if item.get("products"):
        return item["products"][:3]
    out: List[str] = []
    for p in item.get("enisaIdProduct", []):
        name = p.get("product", {}).get("name", "")
        if not name:
            continue
        vendor = p.get("product", {}).get("vendor", {}).get("name", "")
        ver = p.get("product_version", "")
        lbl = f"{vendor} {name}".strip()
        out.append(f"{lbl} ({ver})" if ver else lbl)
    return out[:3]


def format_vuln_item(item: Dict[str, Any], compact: bool = False) -> str:
    aliases = [a.strip() for a in (item.get("aliases") or "").splitlines() if a.strip()]
    alias_str = f" {', '.join(aliases)}" if aliases else ""
    epss = item.get("epss")
    epss_str = f"{epss}%" if epss not in (None, "N/A") and not str(epss).startswith("N/A") else ""
    products = _extract_products(item)

    ssvc = item.get("ssvc")
    sla = item.get("sla") or {}
    sla_parts = [f"{lbl}: {sla[k]}" for lbl, k in (("Exposed", "exposed"), ("Internal", "internal")) if k in sla]
    ssvc_line = ""
    if isinstance(ssvc, dict) and ssvc.get("Automatable"):
        extra = f" | {', '.join(sla_parts)}" if sla_parts else ""
        ssvc_line = f"{ssvc['Automatable']} (Exploitation: {ssvc.get('Exploitation', '-')} | Impact: {ssvc.get('Technical Impact', '-')}{extra})"

    if compact:
        head = f"[{item.get('id', 'N/A')}]{alias_str} | CVSS: {item.get('baseScore', '-')}"
        if epss_str:
            head += f" | EPSS: {epss_str}"
        lines = [head]
        if ssvc_line:
            lines.append(f"  • SSVC Automatable : {ssvc_line}")
        if products:
            lines.append(f"  • 影響產品: {', '.join(products)}")
        return "\n".join(lines)

    desc = (item.get("description") or "").strip()
    if len(desc) > 350:
        desc = desc[:347] + "..."
    lines = [
        f"[{item.get('id', 'N/A')}]{alias_str}  (資料來源: {item.get('source', 'ENISA EUVD')})",
        f"  • CVSS 評分    : {item.get('baseScore', '-')} (v{item.get('baseScoreVersion', '3.1')}) | Vector: {item.get('baseScoreVector', '-')}",
    ]
    if epss_str:
        lines.append(f"  • EPSS 機率    : {epss_str} (利用預測指標)")
    if ssvc_line:
        lines.append(f"  • SSVC Automatable : {ssvc_line}")
    if products:
        lines.append(f"  • 受影響產品   : {', '.join(products)}")
    if item.get("datePublished"):
        lines.append(f"  • 發佈/修訂    : {item['datePublished']} (更新: {item.get('dateUpdated', '-')}) | 權責機構: {item.get('assigner', '-')}")
    if desc:
        lines.append(f"  • 漏洞描述     : {desc}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Resilient Vulnerability Client (EUVD, OSV & CISA SSVC)")
    parser.add_argument("query", help="CVE identifier, EUVD ID, or keyword")
    parser.add_argument("--size", type=int, default=3, help="Max results to display (default: 3)")
    parser.add_argument("--min-score", type=float, default=None, help="Minimum CVSS base score filter")
    parser.add_argument("--min-epss", type=float, default=None, help="Minimum EPSS score percentage filter")
    parser.add_argument("--urgent", action="store_true", help="Only show 3-day (urgent) or 14-day (careful) vulnerabilities")
    parser.add_argument("--compact", action="store_true", help="Compact output without descriptions or timestamps")
    parser.add_argument("--json", action="store_true", help="Output raw JSON response")
    parser.add_argument("--timeout", type=int, default=5, help="Timeout in seconds (default: 5)")
    args = parser.parse_args()
    query = args.query.strip()

    if re.fullmatch(r"(?:CVE|EUVD)-\d{4}-\d+", query, re.I):
        data = query_euvd_by_id(query.upper(), timeout=args.timeout)
        if args.json:
            print(json.dumps(data, indent=2, ensure_ascii=False))
        elif "error" in data:
            print(f"[Vulnerability Error] {data['error']}")
        elif args.urgent and not is_urgent_sla(data):
            print(f"[INFO] {query.upper()} 未達 3天/14天 處置門檻，已過濾。")
        else:
            print(format_vuln_item(data, compact=args.compact))
        return

    data = query_euvd_search(query, size=args.size, from_score=args.min_score, from_epss=args.min_epss, timeout=args.timeout)
    if args.json:
        return print(json.dumps(data, indent=2, ensure_ascii=False))
    if "error" in data:
        return print(f"[Vulnerability Error] {data['error']}")
    items = [it for it in data.get("items", []) if not args.urgent or is_urgent_sla(it)]
    if not items:
        return print(f"[WARNING] 無符合條件之漏洞紀錄: '{query}'")

    print(f"[Vulnerability Intelligence Report] 顯示 {len(items)} 筆紀錄:\n")
    for idx, item in enumerate(items, start=1):
        print(format_vuln_item(item, compact=args.compact))
        if idx < len(items):
            print("\n" + "─" * 60 + "\n")


if __name__ == "__main__":
    main()
