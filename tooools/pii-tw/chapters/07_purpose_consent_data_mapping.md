# Chapter 07: Specific Purpose, Consent Architecture & Data Flow Mapping (DFD)

## 1. Statutory Baseline & Control Architecture
- **PDPA Statutory Articles 8 & 9**: Mandatory statutory notification obligations prior to collecting personal data directly or indirectly.
- **PDPA Statutory Articles 19 & 20**: Specific purpose requirements and strict conditions for out-of-scope data processing and use.
- **PDPA Statutory Articles 3 & 13**: Data Subject Rights (DSR) and mandatory response SLAs (15 days for access/copy, 30 days for correction/deletion).
- **ISACA CRISC / CDPSE Mapping**: Data Life Cycle Management, Data Flow Mapping & Consent Architecture.

### 1.1 Data Life Cycle Management Pipeline
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│ 1. Collection│ ──> │2. Processing │ ──> │3. Store/Trans│ ──> │4. Use/Share  │ ──> │ 5. Disposal  │
│(Consent/Notice     │(Normalization│     │(Encryption/  │     │(PBAC Gate /  │     │(Crypto-Shred/│
│ & Minimization)    │ & Tagging)   │     │ WORM Storage)│     │ Third-Party) │     │ NIST Purge)  │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
```

### 1.2 Data Flow Mapping (DFD) Levels & Standards
- **DFD Level 0 (Context Diagram)**: High-level boundary representation mapping external data subjects, third-party payment gateways, and enterprise boundaries.
- **DFD Level 1 (System Level)**: Maps data ingress endpoints, internal microservices, messaging topics (Kafka), database instances, and backup vaults.
- **DFD Level 2 (Sub-Process Level)**: Details data schemas, field-level encryption boundaries, purpose tokens, and API call interfaces.

### 1.3 Purpose-Based Access Control (PBAC) & Consent Management (CMP)
| Architecture Component | Technical Implementation | Control Standard |
| :--- | :--- | :--- |
| **Purpose Tagging** | Metadata schema tags attaching MOJ Specific Purpose Codes (e.g. Code 040 Marketing, Code 082 Financial Services). | Every read/write query must carry an authenticated Purpose Token in HTTP headers. |
| **Policy Enforcement Point (PEP)** | API Gateway / Service Mesh proxy validating Purpose Claims against user consent records in CMP. | Block unapproved purpose requests with HTTP 403 Forbidden; emit audit event. |
| **Consent Management Platform (CMP)** | Centralized preference center providing dynamic opt-in consent and real-time revocation Webhooks. | Revocation events broadcast to Kafka topics, triggering downstream subscriber invalidation. |

---

## 2. Production Scenario: Cross-Channel Ad Retargeting Violation
- **Incident Overview**: An e-commerce app shared loan applicant financial records with external ad-networks for retargeting campaigns without obtaining separate individual consent.
- **Root-Cause Analysis**:
  1. Loan processing (Purpose Code 082) was merged with commercial advertising (Purpose Code 040) without individual opt-in checkboxes.
  2. The organization lacked DFD lineage documentation, leaving engineering unaware that third-party analytics SDKs accessed raw financial tables.
- **Remediation Architecture**:
  1. Built an automated DFD data lineage map tracking all PII fields and downstream API consumers.
  2. Integrated a centralized CMP enforcing granular opt-in consent checkboxes for secondary marketing purposes.
  3. Deployed PBAC middlewares at API gateways to validate purpose claims before forwarding payloads to external SDKs.

---

## 3. CRISC / CDPSE Exam Question Bank & Distractor Forensics

### Q1 `[CRISC/CDPSE - NEXT]`
When a data subject revokes consent for direct marketing via the self-service preference center, what is the NEXT action the technical architecture must execute?
- A. Permanently erase all core transaction histories and primary user accounts
- B. Emit a revocation event across the message bus to notify downstream marketing tools and block marketing API requests
- C. Retain active marketing feeds until the annual contract expiration date
- D. Require the user to submit a notarized physical written affidavit

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: Consent withdrawal requires immediate propagation (NEXT action) across message pipelines to halt downstream marketing processing.
> - **Why A is Incorrect**: Core transaction records must be retained for legal contract fulfillment and tax compliance.
> - **Why C is Incorrect**: Continuing marketing use after revocation violates statutory purpose limitation rules.
> - **Why D is Incorrect**: Imposing onerous physical barriers violates statutory rules ensuring consent can be withdrawn as easily as given.

### Q2 `[CRISC/CDPSE - PRIMARY]`
In enterprise privacy and risk governance, what is the PRIMARY objective of maintaining Data Flow Diagrams (DFDs) and data inventories?
- A. Reduce the total lines of source code across application repositories
- B. Establish complete visibility of personal data flows, processing nodes, and storage repositories to serve as a risk baseline
- C. Replace perimeter network firewall configurations
- D. Minimize server memory consumption

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: DFDs provide baseline operational visibility into data lineages, enabling risk assessors to identify single points of failure and exposure surfaces.
> - **Why A and D are Incorrect**: Code reduction and memory consumption are software optimization goals unrelated to privacy mapping.
> - **Why C is Incorrect**: DFDs are architectural mapping documents, not network filtering controls.

### Q3 `[CRISC/CDPSE - FIRST]`
A customer submits a formal Data Subject Access Request (DSAR) under PDPA Article 10. What is the compliance team's FIRST action before fulfilling the request?
- A. Transmit unencrypted database dumps directly to the email address provided in the request
- B. Authenticate and verify the identity of the requesting individual
- C. Delete all customer records to avoid fulfilling the request
- D. Invoice the customer a penalty fee for submitting the inquiry

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: Strong identity verification is the mandatory first step (FIRST) to prevent disclosing personal data to unauthorized impersonators.
> - **Why A is Incorrect**: Sending unauthenticated PII creates an immediate data breach.
> - **Why C is Incorrect**: Deleting data upon receiving a DSAR violates statutory rights.
> - **Why D is Incorrect**: Charging punitive fees is prohibited under statutory access rights provisions.

### Q4 `[CRISC/CDPSE - EXCEPT]`
Under Purpose-Based Access Control (PBAC) standards, which criterion is INSUFFICIENT or invalid on its own to authorize access to sensitive personal data?
- A. The caller presents a cryptographically signed token certifying a valid processing purpose
- B. The requested data element is strictly necessary for fulfilling the specified purpose
- C. The user is a senior manager requesting data for arbitrary personal curiosity
- D. The data subject has granted active, unrevoked consent for that specific purpose

> **[Correct Answer] C**
> **[Distractor Forensics]**
> - **Why C is Correct**: Organizational seniority without legitimate business need or lawful purpose cannot authorize access (EXCEPT valid criterion).
> - **Why A, B, D are Incorrect**: Cryptographic purpose claims, data necessity, and active consent are standard pillars of PBAC authorization.
