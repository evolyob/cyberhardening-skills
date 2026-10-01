# Chapter 05: Internal Management Procedures, Privacy by Design (PbD) & SDLC Controls

## 1. Statutory Baseline & Control Engineering
- **PDPA Enforcement Rules Art 12 Para 2 Item 5**: Mandatory internal management procedures governing personal data collection, processing, and use.
- **Privacy & Risk Engineering Framework**: SDLC Privacy Integration, Segregation of Duties (SoD), Synthetic Data Engineering & Post Implementation Review (PIR).

### 1.1 Privacy by Design (PbD) 7 Foundational Principles Matrix
| Principle | Engineering Standard & Implementation | Technical Gate in SDLC |
| :--- | :--- | :--- |
| **1. Proactive not Reactive** | Anticipate privacy risks before architectural commit; mandate pre-development DPIA screening. | Requirements Stage (DPIA Gate) |
| **2. Privacy as the Default** | Default system configurations enforce maximum privacy (opt-in only, no pre-checked consent). | Architecture & Design Stage |
| **3. Privacy Embedded into Design** | Embed cryptographic tokenization, PBAC, and field encryption directly into microservices. | Development Stage (Code Review) |
| **4. Full Functionality (Positive-Sum)** | Avoid zero-sum trade-offs; maintain business functionality while preserving mathematical privacy. | Design & Architecture Stage |
| **5. End-to-End Security** | Protect data across the complete lifecycle (In-Transit, At-Rest, In-Use, and Crypto-Shredding). | Deployment & Operations Stage |
| **6. Visibility and Transparency** | Provide verifiable audit logging, open privacy notices, and verifiable Data Subject Rights portals. | Operations & Audit Stage |
| **7. Respect for User Privacy** | Prioritize user control via self-service consent centers and automated data portability APIs. | User Experience & Design Stage |

### 1.2 SDLC Privacy Control Gates
```
┌─────────────────┐     ┌─────────────────────┐     ┌────────────────────────┐
│ 1. Requirements │ ──> │     2. Design       │ ──> │     3. Development     │
│ (DPIA Screening)│     │(DFD/LINDDUN Threat) │     │ (SAST/SCA/Code Review) │
└─────────────────┘     └─────────────────────┘     └───────────┬────────────┘
                                                                │
┌─────────────────┐     ┌─────────────────────┐                 │
│ 5. Release & PIR│ <── │ 4. QA & Testing     │ <───────────────┘
│ (Post Review)   │     │ (Synthetic Data/DAST│
└─────────────────┘     └─────────────────────┘
```

### 1.3 Test Data Governance & Segregation of Duties (SoD)
- **Prohibition of Production PII Mirrors**: Prohibit copying unmasked production customer databases into test, development, or staging environments.
- **Synthetic Data Generation**: Apply machine learning models (e.g. CTGAN) or rule-based generators to output fictive datasets matching statistical distributions and foreign key constraints.
- **Segregation of Duties (SoD)**: Developers and QA engineers must possess zero access to production decryption keys and database credentials.

---

## 2. Production Scenario: Development Environment Data Exposure
- **Incident Overview**: Developers attempting to troubleshoot a production transaction failure mirrored a full production database snapshot containing 3,000,000 customer records to an unauthenticated staging server.
- **Control Defects**: Violation of Segregation of Duties (SoD); failure of test data sanitization controls; absence of automated CI/CD privacy gating.
- **Remediation Architecture**:
  1. Revoked all developer access to production database backups.
  2. Implemented automated synthetic data generators within CI/CD pipelines to dynamically provision dummy test datasets.
  3. Conducted a Post Implementation Review (PIR) verifying credential isolation and automated pipeline compliance.

---

## 3. Scenario Practice & Decision Forensics (Q&A) & Distractor Forensics

### Q1 `[Privacy Engineering - BEST]`
During the software testing phase, what is the BEST engineering practice to prevent unauthorized disclosure of personal data?
- A. Require all QA engineers and testers to sign non-disclosure agreements
- B. Populate non-production test environments exclusively with synthetically generated data
- C. Disable all audit logging in test databases to maximize performance
- D. Restrict test environment network access to non-business weekend hours

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: In privacy engineering, the gold standard is eliminating real personal data from test environments by generating synthetic datasets with identical schema properties.
> - **Why A is Incorrect**: NDAs are administrative controls that fail to prevent accidental technical data leaks.
> - **Why C is Incorrect**: Disabling logs destroys traceability and security monitoring.
> - **Why D is Incorrect**: Restricting hours does not address the underlying data exposure.

### Q2 `[Privacy Engineering - PRIMARY]`
Following the release of a new customer-facing system, what is the PRIMARY objective of conducting a Post Implementation Review (PIR)?
- A. Assign disciplinary responsibility for project timeline overruns
- B. Verify whether implemented privacy and security controls operate effectively as designed without introducing secondary vulnerabilities
- C. Rewrite technical end-user documentation and user training manuals
- D. Justify additional maintenance budget allocations to senior leadership

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: In Industry Standards Risk Governance control lifecycle governance, a PIR evaluates whether deployed controls achieve their intended risk reduction and checks for unintended side effects in production.
> - **Why A is Incorrect**: PIR is a control assurance activity, not a punitive personnel management tool.
> - **Why C is Incorrect**: Documentation updates are standard operational tasks, not the primary objective of control verification.
> - **Why D is Incorrect**: Budget justifications do not constitute the primary objective of a technical control review.

### Q3 `[Privacy Engineering - FIRST]`
When integrating Privacy by Design (PbD) into an agile software development lifecycle (SDLC), what is the engineering team's FIRST action during sprint planning?
- A. Execute automated Dynamic Application Security Testing (DAST) on release candidate builds
- B. Identify personal data elements and establish privacy requirements and lawful processing constraints
- C. Conduct physical security reviews of server room biometric locks
- D. Configure production database replication failover clusters

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: In SDLC planning, teams must first identify PII data flows and define privacy requirements (FIRST) before committing to architecture and code.
> - **Why A is Incorrect**: DAST occurs during the testing and staging phase, late in the SDLC.
> - **Why C and D are Incorrect**: Physical security and database clustering are infrastructure operational tasks unrelated to sprint feature requirements definition.

### Q4 `[Privacy Engineering - EXCEPT]`
Which practice represents a direct violation of the Privacy by Default principle in application design?
- A. Setting user cookie tracking preferences to opt-in by default
- B. Pre-checking marketing consent checkboxes during user registration
- C. Limiting application profile visibility to private by default
- D. Masking credit card numbers on user interface screens by default

> **[Correct Answer] B**
> **[Distractor Forensics]**
> - **Why B is Correct**: Pre-checking consent boxes forces data sharing by default, directly violating Privacy by Default (EXCEPT valid practice).
> - **Why A, C, D are Incorrect**: Opt-in cookies, private default profiles, and automated field masking are exemplary implementations of Privacy by Default.
