# PDPA Enforcement Rules Art 12: 11 Technical & Organizational Measures (`references/security_measures.md`)

## 1. Statutory Context & Proportionality Principle
Taiwan PDPA Article 27 mandates that non-government agencies maintain appropriate technical and organizational measures (TOMs). Enforcement Rules Article 12 specifies 11 mandatory control areas evaluated under the principle of proportionality (cost, risk level, data sensitivity, and technical state of the art).

---

## 2. 11 Mandatory Measures & Engineering Implementation Standards

| Item | Statutory Mandate | Privacy & Risk Engineering Framework | Core Technical Controls & Verification |
| :--- | :--- | :--- | :--- |
| **Item 1** | Allocation of management personnel and adequate resources | Risk Governance Domain 1 / Privacy Engineering Ch 1 | Three Lines of Defence, RACI matrix (Single Accountable Owner), Board-approved privacy budget. |
| **Item 2** | Defining scope and retention periods of personal data | Risk Governance Domain 4 / Privacy Engineering Ch 8 | Data classification matrix, automated TTL retention policies, Crypto-shredding key deletion. |
| **Item 3** | Risk assessment and management mechanisms | Risk Governance Domain 2 / Privacy Engineering Ch 3 | 3-stage risk assessment (Identify/Analyze/Evaluate), LINDDUN privacy threat modeling, DPIA thresholds. |
| **Item 4** | Incident prevention, reporting, and response mechanisms | Risk Governance Incident Mgmt / Privacy Engineering Ch 2 | Containment-first incident response lifecycle, dual-track 72h regulatory reporting, forensic readiness. |
| **Item 5** | Internal procedures for collection, processing, and use | Risk Governance SDLC / Privacy Engineering Ch 5 | Privacy by Design (PbD) 7 principles, synthetic test data generation, Post Implementation Review (PIR). |
| **Item 6** | Data security management and personnel access controls | Risk Governance IAM & Crypto / Privacy Engineering Ch 6 | Zero Trust IAM, phishing-resistant MFA, PAM Just-In-Time (JIT), Segregation of Duties (SoD). |
| **Item 7** | Personal data protection education and training | Risk Governance Awareness / Privacy Engineering Ch 2 | Role-based privacy training, simulated phishing campaigns evaluated via Key Control Indicators (KCIs). |
| **Item 8** | Security management of equipment and facilities | Risk Governance Cloud & Infra / Privacy Engineering Ch 4 | Cloud multitenancy isolation (RLS), Cloud HSM / BYOK root key management, TIA cross-border reviews. |
| **Item 9** | Third-party processor supervision and contract auditing | Risk Governance Vendor Mgmt / Privacy Engineering Ch 1 | Binding DPAs/SCCs, strict vendor access boundaries, ongoing security auditing rights. |
| **Item 10** | Safety audit mechanisms and retention of access trace logs | Risk Governance Audit Trails / Privacy Engineering Ch 6 | WORM immutable storage, cryptographic hash chaining, mandatory 5-year log retention SLA. |
| **Item 11** | Continuous improvement mechanisms | Risk Governance Continuous Audit / Privacy Engineering Ch 1 | KRI/KCI metric telemetry dashboards, annual independent audits, automated remediation tracking. |
