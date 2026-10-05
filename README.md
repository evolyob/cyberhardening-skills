# Cyber Hardening Skills

A collection of production-ready cybersecurity, system hardening, threat intelligence, statutory privacy compliance, and dynamic incident response configurations for Google Antigravity (AGY).

---

## 1. Skills Catalog & Capabilities Matrix

The following skills are available in this repository:

| Skill | Category | Primary Mission & Scope | Core Tools & Technologies |
| :--- | :--- | :--- | :--- |
| **[`asset-risk`](asset-risk/)** | Security & Risk Assessment | Categorize information assets, assign canonical threat-vulnerability pairs, and generate 8-step DR drill plans. | Python Stdlib, Anti-Monotony Round-Robin |
| **[`container-mcb`](container-mcb/)** | Container & Cloud Security | Financial container security monitoring and configuration baselines across 6 platforms (AWS, Azure, GCP, IBM, Red Hat, VMware), MITRE ATT&CK for Containers, and P0-P3 checklists. | Python Stdlib, Detection as Code, Sigma Rules |
| **[`audit-skill`](audit-skill/)** | Governance & Quality | 23-Gate automated AST static code, skill, and frontend web asset auditor (<20ms). Enforces 3-step workflow, dynamic line budgets, and security guardrails. | Python AST, DOMPurify XSS, Static Analysis |
| **[`env-audit`](env-audit/)** | Host Hardening & OS Audit | Multi-platform (Linux/macOS) binary, package EOL, and CVE audit engine with automated upstream target synchronization. | Python Stdlib, EndOfLife API, Regex |
| **[`sec-intel`](sec-intel/)** | Security & Threat Intel | Authoritative, evidence-based intelligence lookup for IPs, ASNs, Domains, and CVEs via ICANN RDAP, real DNS resolution, and dual-engine EUVD/OSV. | ICANN RDAP, `dnspython`, EUVD, OSV |
| **[`dair-ir`](tooools/dair-ir/)** | Incident Response | Guide dynamic cybersecurity incident response across 8 operational stages and specialized playbooks (ransomware, cloud exfiltration, OT/ICS). | Structured Playbook DAG, Incident Protocols |
| **[`pii-tw`](tooools/pii-tw/)** | Statutory Privacy & Compliance | Taiwan Personal Data Protection Act (PDPA) compliance and privacy engineering framework (Art 12 TOMs, DPIA, 8-Domain technical controls). | Statutory Mapping, PDPA Technical Checklist |

---

## 2. Infrastructure Security & Reference Notes (`tooools/`)

| Directory | Scope & Description |
| :--- | :--- |
| **[`tooools/`](tooools/)** | Infra secure configuration benchmarks, security headers, SSL/TLS analyzers, and offensive/defensive cybersecurity reference notes. |

---

## 3. Reference Architectures & Examples (`examples/`)

The [`examples/`](examples/) directory provides reference implementations and foundational infrastructure templates:

| Component | Path | Description |
| :--- | :--- | :--- |
| **Prompt Template** | [`examples/gemini_template.md`](examples/gemini_template.md) | Standard system prompt template with structured workflow, writing style, persistent memory, and security guardrails. |
| **Modular Plugin Suite** | [`examples/plugins/core-guardrails/`](examples/plugins/core-guardrails/) | Production-grade consolidated plugin bundling:<ul><li>`rules/AGENTS.md`: Always-on security, portability, budgets, and Anti-AI writing constraints.</li><li>`hooks.json`: Lifecycle hook configurations (`PreToolUse`, `PostToolUse`).</li><li>`hooks/noai_gate.py`: Pre-tool Anti-AI cliché filter and mainland term detector.</li><li>`hooks/secret_leak_guard.py`: Guardrail preventing accidental exposure of sensitive keys.</li><li>`hooks/anti_blind_mutation.py`: Prevents unaligned, unvalidated code edits.</li><li>`hooks/view_file_safety.py`: Pre-tool safety filter restricting unauthorized credential and secret file inspection.</li><li>`hooks/post_tool_quality_guard.py`: Post-tool execution verification and quality filter.</li></ul> |
| **Persistent Memory Framework** | [`examples/memory/`](examples/memory/) | Structured 3-tier long-term memory system (Load -> Save -> Recall):<ul><li>`core.md`: Master index and routing table for persistent memory (< 35 lines).</li><li>`topics/`: Machine verification SOP and task architecture (`system_governance.md`, `agent_skill_architecture.md`).</li><li>`templates/`: Specification contracts, coding laws, and skill data specifications.</li></ul> |
