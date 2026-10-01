# Global Skills Registry & Intent Index (`SKILLS.md`)

> Authoritative capability registry, 4-facet intent matrix, and scenario pipelines for all active skills under this directory.
> Automatically generated and synchronized via `cross-map`.

---

## 1. Skill Registry & Security Contracts

| Skill Name | Core Responsibility | Readiness | Execution Channel | Declared Flags | Security Contract |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`asset-risk`** | Categorize information assets, assign canonical threat-vulnerability pairs from parameters | `Ready` | Single-shot ephemeral CLI (< 2s) | `--batch`, `--cat`, `--drill` | [`SECURITY.md`](./asset-risk/SECURITY.md) |
| **`audit-skill`** | Audits skills, Python code, and frontend web assets against quantitative context-efficiency, security boundaries, and Lazy Senior engineering standards | `Ready` | Single-shot ephemeral CLI (< 50ms) | `--ast`, `--security` | [`SECURITY.md`](./audit-skill/SECURITY.md) |
| **`cross-map`** | Scans skills, extracts sub-features and CLI flags, builds 4-facet intent matrices, and manages multi-skill scenario routing pipelines | `Ready` | Single-shot ephemeral CLI (< 20ms) | `--check`, `--json`, `--sync` | [`SECURITY.md`](./cross-map/SECURITY.md) |
| **`dair-ir`** | Guide dynamic cybersecurity incident response across 8 operational stages and specialized playbooks (ransomware, cloud exfiltration, OT/ICS) | `Ready` | - Channel: Single-shot ephemeral CLI (< 20ms) | `--chapter`, `--check`, `--format` | [`SECURITY.md`](./dair-ir/SECURITY.md) |
| **`deep-grill`** | Ask challenging questions about a proposed plan, design, or idea to surface hidden assumptions, risks, and edge cases one question at a time | `Ready` | Single-shot ephemeral CLI (< 2s) | *(Module / API)* | [`SECURITY.md`](./deep-grill/SECURITY.md) |
| **`deep-mod`** | Universal interactive deep research, architecture visualization, and surgical skill extraction pipeline with Anti-AI enforcement | `Ready` | Single-shot ephemeral CLI (< 2s) | `--check`, `--format`, `--list-only` | [`SECURITY.md`](./deep-mod/SECURITY.md) |
| **`env-audit`** | Audit OS binaries, CVEs, EOL risks, upstream versions, and generate upgrade commands | `Ready` | Single-shot ephemeral CLI (< 2s) | `--json`, `--quiet`, `--upgradable` | [`SECURITY.md`](./env-audit/SECURITY.md) |
| **`noai-note`** | Two-phase executive assistant tool for meeting notes, executive briefs, presentation outlines (PPTX), revision comparison tables, and 1-pager visual blueprints (PDF/DOCX) with Shift-Left Anti-AI filtering | `Ready` | Single-shot ephemeral CLI (< 2s) | `--check`, `--format`, `--list-only` | [`SECURITY.md`](./noai-note/SECURITY.md) |
| **`sec-intel`** | Authoritative, evidence-based intelligence lookup for IPs, ASNs, Domains, and CVEs via ICANN RDAP, Real DNS (dig), and Dual-Engine EUVD/OSV | `Ready` | Single-shot ephemeral CLI (< 2s) | `--all`, `--comprehensive`, `--dns` | [`SECURITY.md`](./sec-intel/SECURITY.md) |

---

## 2. 4-Facet Intent & Semantic Routing Matrix

| Skill | Intent | Keywords, Slots & Flags | Example Utterances |
| :--- | :--- | :--- | :--- |
| **`asset-risk`** | `default_action` | `--batch` `--cat` | • "<Asset>"<br>• "<Asset>" |
| **`audit-skill`** | `Execute Automated Auditor` | `--ast` `--security` | • "Analyze / Execute" |
|  | `Fact-Based Findings Report` | `--ast` `--security` |  |
|  | `User Gate & Remediation` | `--ast` `--security` |  |
| **`cross-map`** | `Work Shape & Explicit Skill Lock Gate` | `--check` `--json` | • "Analyze / Execute" |
|  | `Readiness Pre-flight & Token Gate` | `--check` `--json` |  |
|  | `Execute Scanner Engine` | `--check` `--json` |  |
| **`dair-ir`** | `Work Shape & Explicit Skill Lock` | `--chapter` `--check` | • "Analyze / Execute" |
|  | `Query Stage or Playbook` | `--chapter` `--check` |  |
|  | `Structured Reporting & Exit Gate Verification` | `--chapter` `--check` |  |
| **`deep-grill`** | `default_action` | `[path]` | • "wrap up" |
| **`deep-mod`** | `Execute domain-agnostic interactive research, architecture visualization, and skill distillation with Shift-Left Anti-AI enforcement.` | `--check` `--format` | • "Analyze / Execute" |
| **`env-audit`** | `Dynamic Environment Discovery & Target Inspection` | `--json` `--quiet` | • "Analyze / Execute" |
|  | `Real-Time Upstream & Vulnerability Assessment` | `--json` `--quiet` |  |
|  | `Render Structured Audit Report` | `--json` `--quiet` |  |
| **`noai-note`** | `Zero-Analysis Collection` | `--check` `--format` | • "collection"<br>• "<finalized_text>" |
|  | `Finalized Executive Output` | `--check` `--format` |  |
| **`sec-intel`** | `default_action` | `--all` `--comprehensive` | • "None" |

---

## 3. Multi-Skill Scenario Pipelines

| Composite Scenario | Work Mode | Trigger Events | Routed Pipeline | Stage Flags, Slots & Exit Gate |
| :--- | :--- | :--- | :--- | :--- |
| **Security Boundary Enforcement & Policy Audit**<br>*(security_policy_enforcement)* | `phased` | • "Audit skill security boundaries"<br>• "Establish compliant SECURITY.md policies" | **Step 1**: `audit-skill`<br>**Step 2**: `cross-map` | **Step 1**: `--security, --ast` `[target_path]`<br>*(Gate: `zero_ast_and_security_violations`)*<br>**Step 2**: `--sync` `[skills_root]`<br>*(Gate: `registry_synced`)* |
| **External Source Security Investigation**<br>*(external_source_review)* | `phased` | • "Audit external GitHub repository"<br>• "Investigate domain reputation and safety" | **Step 1**: `sec-intel`<br>**Step 2**: `audit-skill`<br>**Step 3**: `noai-note` | **Step 1**: `--domain` `[URL/Domain]`<br>*(Gate: `domain_reputation_verified`)*<br>**Step 2**: `--security, --ast` `[target_path]`<br>*(Gate: `source_code_audited`)*<br>**Step 3**: `--text` `[content]`<br>*(Gate: `notes_detoxed`)* |
| **Codebase Hardening & Subtractive Refactor**<br>*(codebase_hardening)* | `phased` | • "Perform subtractive refactoring on bloated scripts"<br>• "Audit code hygiene and eliminate nested blocks" | **Step 1**: `audit-skill`<br>**Step 2**: `env-audit` | **Step 1**: `--ast` `[target_path]`<br>*(Gate: `ast_hygiene_confirmed`)*<br>**Step 2**: `--linux` `[system]`<br>*(Gate: `os_dependencies_upgraded`)* |
| **Incident Response Drill & Playbook Execution**<br>*(incident_response_drill)* | `phased` | • "Execute ransomware incident response drill"<br>• "Perform cloud storage exfiltration containment" | **Step 1**: `dair-ir`<br>**Step 2**: `sec-intel`<br>**Step 3**: `noai-note` | **Step 1**: `--stage, --playbook` `[incident_type]`<br>*(Gate: `containment_and_blast_radius_verified`)*<br>**Step 2**: `--ip, --cve` `[target_entity]`<br>*(Gate: `threat_indicators_enriched`)*<br>**Step 3**: `--format json` `[incident_data]`<br>*(Gate: `debrief_report_assembled`)* |
| **Asset Risk Assessment & Threat Modeling**<br>*(asset_risk_threat_modeling)* | `phased` | • "Categorize critical information assets"<br>• "Map asset threats and vulnerability pairs" | **Step 1**: `asset-risk`<br>**Step 2**: `env-audit` | **Step 1**: `--batch` `[asset_list]`<br>*(Gate: `asset_threat_matrix_mapped`)*<br>**Step 2**: `--json` `[system]`<br>*(Gate: `host_vulnerabilities_identified`)* |
