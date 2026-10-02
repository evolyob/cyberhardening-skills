# Taiwan Personal Data Protection Act (PDPA) Overview (`references/law_overview.md`)

## 1. Statutory Architecture & Hierarchy
The Taiwan Personal Data Protection Act (PDPA) governs public and private entities across Taiwan jurisdiction.

```
                    ┌────────────────────────────────────────┐
                    │   PDPA Statutory Law (Primary Act)     │
                    └───────────────────┬────────────────────┘
                                        │
         ┌──────────────────────────────┴──────────────────────────────┐
         ▼                                                             ▼
┌─────────────────────────────────┐                   ┌─────────────────────────────────┐
│  PDPA Enforcement Rules         │                   │  Competent Authority Industry   │
│  - Art 12: 11 Mandatory TOMs    │                   │  Security Maintenance Plans     │
└─────────────────────────────────┘                   └─────────────────────────────────┘
```

---

## 2. Data Subject Rights (DSR / DSAR) (Articles 3, 10, 11 & 13)
Data Subject Rights cannot be waived or contractually restricted:

| Right | Statutory Article | Statutory SLA | Engineering & Technical Implementation |
| :--- | :--- | :--- | :--- |
| **Right to Inquiry & Access** | Art 3 Item 1, Art 10 | 15 days (+15 day extension) | Self-service portal, automated DSR export endpoints |
| **Right to Request Copies** | Art 3 Item 2, Art 10 | 15 days (+15 day extension) | Export structured, machine-readable formats (JSON/CSV) |
| **Right to Supplement / Rectify** | Art 3 Item 3, Art 11 Para 1 | 30 days (+30 day extension) | Mutation APIs with immutable audit logging and validation |
| **Right to Cease Processing / Use** | Art 3 Item 4, Art 11 Para 2-4 | 30 days (+30 day extension) | Purpose tagging and PBAC policy enforcement points |
| **Right to Erasure** | Art 3 Item 5, Art 11 Para 3 | 30 days (+30 day extension) | Distributed purge orchestrator, Crypto-shredding |

---

## 3. Lawful Bases for Collection, Processing and Use

### 3.1 General Personal Data (Articles 15 & 19)
- **Public Entities**: Within necessary scope of statutory duties; or with data subject consent.
- **Private Entities**:
  1. Expressly provided by statutory law.
  2. Contractual or quasi-contractual relationship, with adequate security measures in place.
  3. Manifestly made public by the data subject or lawfully publicized.
  4. Academic research institutions for public interest with complete de-identification.
  5. Individual, informed, affirmative consent.
  6. Necessary for advancing public interest.
  7. Obtained from generally accessible public sources.
  8. Causes no harm to data subject rights and interests.

### 3.2 Special Categories / Sensitive Personal Data (Article 6)
Encompasses 6 sensitive classes: **Medical Records, Healthcare, Genetics, Sex Life, Physical Examination, Criminal Records**.
Collection is prohibited by default, with strict statutory exceptions (Art 6 Para 1).

---

## 4. Breach Notification Mandate & Penalty Matrix (2023 Amendments)

### 4.1 Breach Notification Obligation (Article 12)
- Upon discovery of theft, leakage, alteration, or compromise, entities must notify affected data subjects via verifiable channels (SMS, email, registered mail) after containment.
- Sectoral security plans mandate notifying competent supervisory authorities within **72 hours**.

### 4.2 Administrative Fines (Articles 47 & 48)
- **Failure to implement adequate technical security measures (Art 48 Para 2)**: NTD 20,000 to NTD 2,000,000; non-compliance within ordered timeline triggers recurring fines of NTD 150,000 to NTD 15,000,000 per violation.
- **Severe violations (Art 48 Para 3)**: Direct fine of NTD 150,000 to NTD 15,000,000 with mandatory corrective orders.
- **Representative liability (Art 50)**: Corporate representatives face identical fine amounts unless they prove adequate prevention diligence.
- **Civil & Criminal Liability (Arts 28, 29, 41, 42)**: Statutory damages of NTD 500 to NTD 20,000 per person per incident (aggregate cap up to NTD 200 million); commercial profit violations trigger criminal imprisonment up to 5 years.
