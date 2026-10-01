# ISACA CDPSE & CRISC 8-Domain Engineering Mapping (`references/cdpse_mapping.md`)

## 1. Governance & Engineering Domain Cross-Walk

| Chapter | ISACA CDPSE / CRISC Domain | Taiwan PDPA Statutory Basis | Primary Engineering Deliverables & Controls |
| :--- | :--- | :--- | :--- |
| **Ch 01** | Privacy Governance Architecture | Enforcement Rules Art 12 Items 1 & 11 | Three Lines of Defence, RACI Matrix, Risk Appetite / Tolerance thresholds, KPI/KRI/KCI telemetry. |
| **Ch 02** | Incident Response & Awareness | Statutory Art 12, Enforcement Rules Items 4 & 7 | CSIRT runbooks, Containment-first workflow, 72h regulatory notification, simulated phishing KCIs. |
| **Ch 03** | Risk Management & PIA/DPIA | Enforcement Rules Art 12 Item 3 | 3-stage risk assessment, Inherent/Residual risk calculation, LINDDUN threat modeling, 4 Treatment options. |
| **Ch 04** | Cloud Infrastructure & Cross-Border | Statutory Art 21, Enforcement Rules Item 8 | Multitenant Row-Level Security (RLS), BYOK/Cloud HSM, TEE confidential computing, TIA impact reports. |
| **Ch 05** | Applications, PbD & SDLC | Enforcement Rules Art 12 Item 5 | PbD 7 principles, synthetic test data generation, CI/CD automated SAST/DAST gating, PIR sign-offs. |
| **Ch 06** | IAM, Cryptography & Audit Logging | Enforcement Rules Art 12 Items 6 & 10 | Zero Trust IAM, PAM JIT, application-layer envelope encryption, WORM 5-year immutable logs. |
| **Ch 07** | Purpose, Consent & Data Flow (DFD) | Statutory Arts 3, 8, 9, 19, 20 | End-to-end DFD lineage, Purpose-Based Access Control (PBAC), CMP consent revocation pipelines. |
| **Ch 08** | Data Minimization, Retention & Disposal | Statutory Art 11, Enforcement Rules Item 2 | K-Anonymity ($k \ge 5$), Differential Privacy, Crypto-shredding, NIST SP 800-88 media sanitization. |

---

## 2. ISACA Question Stem Taxonomy & Decision Rules

- **`FIRST`**: Identify the foundational governance or technical action in a lifecycle (e.g., Executive sponsorship & Risk Appetite; Containment before notification; Asset identification before risk scoring).
- **`PRIMARY / MOST`**: Identify the most direct control addressing root-cause exposure (e.g., Application-layer encryption for DBA segregation; RLS for multitenancy isolation; Residual risk vs appetite for treatment decisions).
- **`NEXT`**: Identify the immediate downstream step following an event (e.g., Propagate revocation events to downstream messaging queues upon user consent withdrawal).
- **`EXCEPT / LEAST`**: Identify invalid, prohibited, or ineffective methods (e.g., Standard OS deletion without block overwrites or key destruction is invalid media sanitization).
