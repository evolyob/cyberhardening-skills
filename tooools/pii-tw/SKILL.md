---
name: pii-tw
description: Taiwan Personal Data Protection Act (PDPA) statutory compliance and Industry Standards Privacy Engineering privacy engineering framework. Provides statutory mapping, Enforcement Rules Art 12 technical controls, PIA/DPIA checklists, and 8-domain engineering guides.
dependencies: []
---

# Taiwan PDPA & Privacy Engineering Privacy Engineering Framework (`pii-tw`)

## Objective
Single Source of Truth for Taiwan Personal Data Protection Act (PDPA) statutory compliance and Industry Standards Privacy Engineering privacy risk engineering. Directly maps statutory obligations to concrete technical controls, security measures, and verification checklists.

---

## Routing & Core Commands

| Scenario / Goal | CLI Command | Output Artifact |
| :--- | :--- | :--- |
| **1. Statutory Control** | `python3 <skill_dir>/scripts/query.py --article <No>` | Statutory summary, Privacy Engineering domain, technical controls & verification criteria. |
| **2. Security Measure** | `python3 <skill_dir>/scripts/query.py --measure <1-11>` | Enforcement Rules Art 12 mandatory measures & technical implementation guide. |
| **3. Privacy Engineering Domain**| `python3 <skill_dir>/scripts/query.py --domain <Domain>` | 8-Domain engineering standards mapped to Taiwan PDPA statutory provisions. |
| **4. Cross Keyword** | `python3 <skill_dir>/scripts/query.py --check "<Keyword>"` | 4-way cross-indexing across articles, measures, glossary terms, and chapters. |
| **5. Full Overview** | `python3 <skill_dir>/scripts/query.py --list` | Structured overview of all 8 chapters and 11 mandatory security measures. |

---

## Execution Workflow

1. **Identify Requirement**: Determine whether query targets statutory articles, security measures, or engineering domains.
2. **Execute Query**: Run `scripts/query.py` with appropriate flags (`--article`, `--measure`, `--domain`, `--check`).
3. **Inspect Chapter Guides**: Consult corresponding chapter file in `chapters/` (Ch01~Ch08) for in-depth engineering specifications.
4. **Format Deliverables**: Emit structured compliance matrices, technical audit findings, or remediation action plans.

---

## Data Assets & File Specifications

- `data/compliance_matrix.json`: Complete mapping of PDPA statutory articles, Enforcement Rules Art 12, and Privacy Engineering controls.
- `data/data_categories.json`: Complete statutory PII category codes (C001~C134) and specific purpose codes (001~182).
- `data/glossary.json`: Bilingual glossary of Taiwan PDPA statutory terms and Privacy Engineering privacy engineering concepts.
- `references/law_overview.md`: Taiwan PDPA statutory architecture, lawful bases, data subject rights, and penalty matrix.
- `references/security_measures.md`: Enforcement Rules Art 12: 11 Technical and Organizational Measures (TOMs).
- `references/domain_mapping.md`: Industry Standards Privacy & Risk Engineering 8-domain engineering mapping and question stem taxonomy.
