# Statement of Applicability (SoA) Generation Rules & Templates

## 1. Unified SoA Generation Decision Engine

The interactive wizard (`scripts/wizard.py`) maps organizational profiles to control declarations using this deterministic decision tree:

```
[Organizational Profile Evaluation]
       │
       ├─ Q1: Does organization train or fine-tune models in-house?
       │     ├─ YES ──> Mark A.6.2.3 (AI Dev Docs), A.6.2.4 (V&V), A.7.2 (Training Data) as APPLICABLE
       │     └─ NO  ──> Mark A.6.1.2, A.6.1.3, A.6.2.2-A.6.2.4, A.7.2, A.7.6 as EXCLUDED with "API-Only Consumption" justification
       │
       ├─ Q2: Are AI outputs exposed directly to external citizens/users?
       │     ├─ YES ──> Mark A.8.2 (User Specs), A.8.3 (Understandability), A.5.2 (Impact Assessment) as APPLICABLE
       │     └─ NO  ──> Mark A.8.2-A.8.5 as EXCLUDED with "Internal Batch ETL Processing" justification
       │
       └─ Q3: Are third-party commercial APIs (e.g., OpenAI, Claude) integrated?
             ├─ YES ──> Mark A.10.1 (Supplier Relationships), A.10.2 (Allocation of Responsibilities) as MANDATORY APPLICABLE
             └─ NO  ──> Exclude A.10.1-A.10.4 with "Air-Gapped On-Premises Architecture" justification
```

---

## 2. Standard Markdown SoA Table Format

```markdown
| Unified Control ID | CNS/ISO Ref | ISO 27002 Ref | Status | Justification & Policy Reference | Implementation Artifact |
| :--- | :--- | :--- | :---: | :--- | :--- |
| `SOA-A.2.2` | **A.2.2** AI Policy | **5.1** InfoSec Policy | `Applicable` | Executive Yuan Guidelines Art. 3 & ISO A.2.2 compliance | `[AI Policy & Governance Scope Document / 人工智慧政策與治理範疇書]` |
| `SOA-A.5.2` | **A.5.2** AI Impact | **5.8** Project Security| `Applicable` | Mandatory for public administrative decision assistance | `[AI Impact Assessment Report / AI 衝擊與風險評估報告]` |
| `SOA-A.6.2.3` | **A.6.2.3** AI Dev Docs | **8.28** Secure Coding | `Applicable` | Enforces prompt sanitization, model architecture docs, and guardrails | `[AI System Architecture & Model Specification / 系統架構與模型規格書]` |
| `SOA-A.10.1` | **A.10.1** Third-Party | **5.19** Vendor Sec | `Applicable` | Zero-data-retention terms with foundation model vendors | `[Third-Party AI Supplier Agreement / 外部 AI 供應商評估與協議]` |
```

---

## 3. Interactive Generation Command

To run the interactive assessment and produce a validated SoA document:

```bash
# Run interactive wizard to generate SoA
python3 scripts/wizard.py -o ~/agy/download/cns42001_dual_soa.md
```
