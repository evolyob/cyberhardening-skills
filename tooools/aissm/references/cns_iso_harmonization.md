# CNS 42001 & National AI Guidelines vs ISO 42001/27002 Harmonization

## 1. High-Level Structure Crosswalk (National Standards vs ISO Core)

| Clause Domain | CNS 42001 / National Executive Guidelines | ISO/IEC 42001:2023 | ISO/IEC 27001/27002:2022 | Key Operational Implementation Action |
| :--- | :--- | :--- | :--- | :--- |
| **Governance & Accountability** | Executive Yuan GenAI Guidelines (Agency Head Final Liability) | Clause 5 (Leadership) & Annex A.2 | Clause 5.1 (Policies) & 5.2 (Roles) | Institutionalize AI Governance Board with joint oversight by Chief AI Officer and CISO. |
| **Confidentiality & Data Protection** | Executive Yuan GenAI Guidelines (Confidential Data Input Restrictions) | Annex A.7 (Data for AI) & A.5 | ISO 27002 8.10, 8.11 (Masking/Deletion) | Mandate egress network filtering and prompt guardrails to block confidential records from commercial LLMs. |
| **Procurement & Vendor SLA** | Public Sector AI Procurement Guidelines (Model Weight IP & Zero Retention) | Annex A.10 (Third-Party AI) | ISO 27002 5.19, 5.23 (Cloud Services) | Require zero-data-retention (ZDR) clauses and API vulnerability disclosure SLAs in vendor contracts. |
| **Lifecycle & MLOps Safety** | CNS 42001 Annex A.6 (Verification & Telemetry Tracking) | Annex A.6 (AI Lifecycle) | ISO 27002 8.28 (Secure Coding), 8.31 | Embed automated drift detection and hallucination validation gates into CI/CD release pipelines. |
| **Transparency & Traceability** | Executive Yuan GenAI Guidelines (Mandatory AI Disclosure) | Annex A.8 (User Transparency) | ISO 27002 5.14 (Information Transfer) | Watermark and label AI-assisted administrative documents; log full prompt/response telemetry. |

---

## 2. Two-Stage Audit Certification Readiness Checklist

### Stage 1: Document Review & Governance Baseline
- [ ] **AI Context & Scope Document**: Boundary definition of in-house models vs third-party APIs (`docs/governance/scope.md`).
- [ ] **AI Policy Charter**: Approved by executive leadership and integrated with ISMS security policies (`docs/policies/ai_policy.md`).
- [ ] **AI Impact Assessment (AIA) Procedure**: Documented trigger criteria and stakeholder harm assessment methodology.
- [ ] **Dual Statement of Applicability (SoA)**: Complete justification for all 38 Annex A controls (`reports/cns42001_soa.md`).

### Stage 2: Operational Effectiveness & Evidence Verification
- [ ] **AI Asset & Data Inventory**: Verified provenance, licensing, and SHA-256 hashes for 100% of production datasets.
- [ ] **Verification & Validation (V&V) Records**: Pre-release red-teaming, adversarial stress tests, and fairness evaluation sign-offs.
- [ ] **Operational Telemetry & Logs**: Append-only audit trails capturing prompt inputs, model versions, and human overrides.
- [ ] **Management Review & Internal Audit**: Formal review meeting minutes assessing AI telemetry alongside ISMS metrics.

---

## 3. Fast CLI Crosswalk Query

```bash
# Query Governance & National Guideline mappings
python3 scripts/query.py --filter "Governance" --format markdown

# Query Data & Confidentiality Controls
python3 scripts/query.py --filter "Data" --format markdown
```
