# Chapter 01: Clause 4-10 Alignment & Annex A.2-A.3 Governance Crosswalk

## 1. Statutory Baseline & Technical Control Matrix

### 1.1 Management System Harmonization (Clause 4 - 10)
Both ISO/IEC 42001:2023 (Artificial Intelligence Management System, AIMS) and ISO/IEC 27001:2022 (Information Security Management System, ISMS) are structured upon the ISO Harmonized Structure. Because the management clauses (Clause 4 through Clause 10) share a standardized taxonomy and sequential progression, organizations can directly augment existing ISMS governance frameworks without constructing redundant administrative silos.

ISO/IEC 42001 expands enterprise risk governance beyond conventional Information Security Confidentiality, Integrity, and Availability (CIA) metrics to encompass algorithmic fairness, transparency, accountability, societal impact, and autonomous decision trustworthiness.

| Management Clause | ISO/IEC 27001:2022 (ISMS Baseline) | ISO/IEC 42001:2023 (AIMS Augmentation) | Dual-System Harmonization Guidance |
| :--- | :--- | :--- | :--- |
| **Clause 4: Context of the Organization** | Identifies organizational information assets, internal/external issues, and interested party security requirements (4.1, 4.2). Establishes ISMS scope (4.3). | Mandates explicit classification of organizational AI roles (AI Developer, AI Provider, AI Deployer, AI Subject). Assesses downstream impacts on society, individuals, and external ecosystems. | Merge context analysis into a unified Enterprise Risk & Technology Landscape Register. Incorporate algorithmic bias, intellectual property, and regulatory compliance (e.g., EU AI Act) into context definitions. |
| **Clause 5: Leadership** | Top management establishes Information Security Policy, assigns CISO / Information Security Officer roles, and allocates cybersecurity resources (5.1, 5.2, 5.3). | Establishes Responsible AI Policy. Mandates cross-functional AI Governance oversight combining data engineering, legal/compliance, security, and algorithmic ethics (5.1, 5.2, 5.3). | Form an AI Governance Committee as an executive sub-council under the existing Information Security Steering Committee. Designate dedicated AI Ethicists and ML Compliance Officers. |
| **Clause 6: Planning** | Executes asset-based CIA risk assessments (6.1.2), formulates Risk Treatment Plans (6.1.3), and issues ISMS Statement of Applicability (SoA). Sets security objectives (6.2). | Mandates specialized AI risk assessments (6.1.2) and integrates the mandatory **AI System Impact Assessment (6.1.4)**. Establishes AIMS SoA and AI-specific measurable objectives (6.2). | Construct a Dual-Track Risk Matrix. Feed AI System Impact Assessment findings directly into the consolidated Enterprise Risk Treatment Plan. Maintain cross-referenced Dual SoAs. |
| **Clause 7: Support** | Allocates IT compute/storage resources, runs general security awareness training, and manages documented information (7.1 - 7.5). | Tracks dedicated compute infrastructure (GPUs/TPUs), training/validation datasets, prompt engineering security, AI literacy, and adversarial defense competencies (7.1 - 7.5). | Expand asset registers with hardware accelerators, feature stores, and trained model weights. Embed prompt injection, data poisoning, and model evasion into mandatory technical awareness curricula. |
| **Clause 8: Operation** | Executes Secure Software Development Lifecycle (SSDLC) controls, configuration baselines, and third-party supplier risk management (8.1). | Governs AI system lifecycle processes (8.1), performs continuous operational AI risk assessments (8.2, 8.3), and executes operational **AI System Impact Assessments (8.4)**. | Embed MLOps gates into existing CI/CD deployment pipelines. Enforce automated drift detection, model validation gates, and pre-deployment fairness sign-offs prior to production release. |
| **Clause 9: Performance Evaluation** | Conducts internal ISMS audits, measures security metrics (incident count, patch latency), and convenes management reviews (9.1, 9.2, 9.3). | Continuously monitors model drift, accuracy degradation, explainability scores, disparate impact indices, and stakeholder feedback loops (9.1, 9.2, 9.3). | Integrate algorithmic fairness, inference telemetry, and Model Card verification into annual management review meeting agendas and internal audit scope. |
| **Clause 10: Improvement** | Investigates information security incidents, identifies root causes, and executes corrective actions for nonconformities (10.1, 10.2). | Remediates algorithmic failures, hallucination spikes, unintended demographic discrimination, and concept drift incidents. Maintains model rollback protocols (10.1, 10.2). | Establish rapid model rollback, graceful degradation switches, and automated human-in-the-loop (HITL) intervention playbooks for anomalous AI decisions. |

---

### 1.2 Annex A.2 & A.3 Governance Crosswalk vs ISO/IEC 27002:2022
ISO/IEC 42001:2023 Annex A establishes normative reference controls. Annex A.2 focuses on Policies Related to AI, and Annex A.3 focuses on Internal Organization. Below is the comprehensive crosswalk mapping these controls and foundational governance touchpoints against the 93 controls of ISO/IEC 27002:2022 (covering clauses 5.1, 5.2, 5.3, 5.7, 5.9, 5.37, 6.1, 6.3, 6.8, 7.1, 8.1, 8.6, 8.8, 8.10, 8.12, 8.25, and 8.33).

| ISO 42001 Control | Control Title & Scope | ISO 27002:2022 Mapping | Integration Type | Technical Implementation & Telemetry Controls | Target Metrics (KPI / KRI / KCI) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A.2.1** | **Policies for AI (Objective)** | **5.1** Policies for information security | **Governance Baseline** | Define overarching top-level mandates directing responsible, safe, and ethical development and deployment of AI across the entire organization. | **KPI**: Executive approval and publication of AIMS policy within annual review window (100%). |
| **A.2.2** | **AI Policy** | **5.1** Policies for information security | **Existing Extension** | Augment the primary Information Security Policy with an enterprise Responsible AI Charter. Codify acceptable use of Generative AI, ban unauthorized public LLMs, and enforce intellectual property protection rules. | **KPI**: Employee AI acceptable use policy acknowledgment rate = 100%.<br>**KRI**: Zero unauthorized public GenAI usage incidents on corporate networks. |
| **A.2.3** | **Alignment with Other Organizational Policies** | **5.1** Policies for information security | **Cross-System Harmonization** | Reconcile AI policies with Privacy Policies (GDPR/ISO 27701), Data Classification (ISO 27002 5.12), Data Protection (8.12), and IP/Copyright compliance. Eliminate policy conflicts regarding automated data ingest. | **KCI**: Quarterly inter-policy consistency review identifies 0 conflicting operational directives. |
| **A.2.4** | **Review of the AI Policy** | **5.1** Policies for information security | **Existing Extension** | Establish periodic and event-triggered policy reviews driven by major regulatory changes (such as EU AI Act enforcement), critical security incidents, or adoption of disruptive foundation models. | **KPI**: Policy review completed within 30 days of major regulatory or technological shifts. |
| **A.3.1** | **Internal Organization (Objective)** | **5.2** Information security roles and responsibilities<br>**5.3** Segregation of duties | **Governance Baseline** | Establish organizational infrastructure and governance bodies responsible for assigning, executing, and validating AI accountability. | **KPI**: Charter established for cross-functional AI Ethics and Safety Board. |
| **A.3.2** | **AI Roles and Responsibilities** | **5.2** Roles and responsibilities<br>**5.3** Segregation of duties<br>**6.1** Screening | **Existing Extension** | Delineate roles among AI System Owner, Lead Data Scientist, MLOps Engineer, Model Auditor, and Business Consumer. Enforce strict separation between algorithmic development access and production deployment rights. | **KRI**: Separation of duties violations between model training environments and production inference pipelines = 0.<br>**KCI**: 100% of ML staff background checks verified. |
| **A.3.3** | **Reporting Concerns** | **6.8** Information security event reporting | **Existing Extension** | Expand existing incident response whistleblowing and helpdesk channels to enable all staff and external users to report model hallucinations, biased decisions, toxic outputs, or data leakage concerns. | **KPI**: Mean Time to Initial Assessment (MTTA) for reported AI anomalies < 4 hours.<br>**KRI**: Unaddressed AI ethical or safety escalations = 0. |
| **Foundational Mapping** | **Threat Intelligence in AI Context** | **5.7** Threat intelligence | **Cross-System Harmonization** | Ingest AI-specific threat feeds (e.g., MITRE ATLAS, OWASP Top 10 for LLMs) to anticipate prompt injection, model inversion, and data poisoning attack vectors. | **KPI**: Monthly ingestion and threat modeling against MITRE ATLAS techniques completed. |
| **Foundational Mapping** | **Inventory of AI Assets** | **5.9** Inventory of information and other associated assets | **Existing Extension** | Expand asset registers to document training datasets, fine-tuning scripts, model weights, checkpoints, hyperparameters, and feature stores with cryptographic hashes. | **KPI**: AI Asset Inventory coverage across active production pipelines = 100%. |
| **Foundational Mapping** | **Documented Operating Procedures** | **5.37** Documented operating procedures | **Existing Extension** | Maintain documented MLOps operational procedures: automated retraining triggers, model drift remediation steps, and manual override procedures. | **KCI**: 100% of MLOps pipelines possess peer-reviewed Standard Operating Procedures (SOPs). |
| **Foundational Mapping** | **AI Security Training & Awareness** | **6.3** Information security awareness, education and training | **Existing Extension** | Deliver specialized security training covering adversarial inputs, prompt injection defenses, privacy-preserving machine learning (differential privacy), and bias mitigation techniques. | **KPI**: Annual AI security training completion rate for ML engineering teams >= 95%. |
| **Foundational Mapping** | **Physical & Perimeter Protection for Compute** | **7.1** Physical security perimeters | **Existing Extension** | Enforce physical access controls around on-premises high-density GPU/TPU training clusters and HSM appliances storing model signing keys. | **KCI**: Physical access audit nonconformities for compute datacenters = 0. |
| **Foundational Mapping** | **User Endpoint Devices & Notebooks** | **8.1** User endpoint devices | **Existing Extension** | Restrict local caching of raw training data on data scientists' workstations; enforce containerized Jupyter/VS Code environments hosted in zero-trust enclaves. | **KRI**: Unencrypted training data discovered on developer local endpoints = 0. |
| **Foundational Mapping** | **Capacity Management for AI Training** | **8.6** Capacity management | **Existing Extension** | Monitor GPU VRAM, distributed training interconnect bandwidth, and storage I/O to avoid compute starvation and denial-of-service during peak inference/training runs. | **KPI**: Maintain GPU cluster compute load between 70% and 85%. |
| **Foundational Mapping** | **Vulnerability Management in ML Stacks** | **8.8** Management of technical vulnerabilities | **Existing Extension** | Continuously scan deep learning framework dependencies (PyTorch, TensorFlow, HuggingFace transformers, ONNX Runtime) and base container images for CVEs. | **KRI**: Unpatched critical/high vulnerabilities in production ML containers older than 14 days = 0. |
| **Foundational Mapping** | **Information Deletion & Machine Unlearning** | **8.10** Information deletion | **AI-Specific Deepening** | Establish verifiable mechanisms to purge protected data from training pools upon withdrawal of consent; execute machine unlearning or retraining where legally mandated. | **KPI**: Right-to-be-forgotten deletion execution in data lakes and retraining queues completed within statutory timelines (100%). |
| **Foundational Mapping** | **Data Leakage Prevention in AI Inferences** | **8.12** Data leakage prevention | **AI-Specific Deepening** | Implement outbound egress filters, semantic DLP scanners, and prompt firewalls to block extraction of proprietary source code or PII via model responses. | **KRI**: Confirmed PII leakage events via production inference endpoints = 0. |
| **Foundational Mapping** | **Secure Development Lifecycle for AI** | **8.25** Secure development life cycle | **AI-Specific Deepening** | Embed automated model cards, bias testing gates, code static analysis (SAST), and dependency scanning (SCA) into standard MLOps continuous delivery pipelines. | **KCI**: 100% of models promoted to production satisfy automated secure development gates. |
| **Foundational Mapping** | **Protection of Test Data** | **8.33** Test information | **Existing Extension** | Prevent production PII leakage into model testing/validation datasets; use synthetic data or masked tokenized corpora for pre-release validation. | **KPI**: Compliance rate of synthetic/masked data usage across pre-production test environments = 100%. |

---

## 2. Production Incident & Remediation Architecture

### 2.1 Incident Context: Algorithmic Bias and Privilege Escalation in Automated Credit Decisioning
A multinational commercial bank deployed an automated credit scoring and loan origination deep learning model across its retail banking division. The underlying cloud environment had been certified under ISO/IEC 27001:2022 for five consecutive years.

Six months after full commercial release, national financial regulatory authorities initiated an inquiry following customer complaints. Forensic auditing uncovered two structural failures:
1. **Systemic Algorithmic Discrimination**: Loan application rejection rates for protected demographic minority applicants were disproportionately elevated. The calculated Disparate Impact Ratio (DIR) stood at 0.52 (substantially violating the statutory four-fifths threshold of 0.80).
2. **Backdoor Privilege Escalation**: A disgruntled senior data engineer, possessing unrestricted access to the enterprise Feature Store without segregation of duties, had implanted a backdoor feature combination (a specific combination of rare transaction zip codes and arbitrary collateral codes). When queried, this backdoor triggered an unconditional bypass of credit risk checks, approving maximum-limit credit lines without secondary human verification.

### 2.2 Root Cause Analysis (RCA)

```text
+----------------------------------------------------------------------------------------------------+
|                                    ROOT CAUSE ANALYSIS TAXONOMY                                    |
+----------------------------------------------------------------------------------------------------+
| 1. ABSENCE OF AI IMPACT ASSESSMENT (ISO 42001 Clause 6.1.4 / A.5.2 / A.5.4)                       |
|    - The project team only executed standard ISO 27005 information security risk assessments       |
|      focusing on database Confidentiality, Integrity, and Availability (CIA).                      |
|    - No AI System Impact Assessment was conducted to evaluate asymmetric socioeconomic impact,          |
|      demographic bias, or individual economic disenfranchisement.                                  |
+----------------------------------------------------------------------------------------------------+
| 2. BREAKDOWN OF SEGREGATION OF DUTIES & FEATURE INTEGRITY (ISO 42001 A.3.2 / A.4.3 / ISO 27002 5.3)|
|    - Data scientists had dual write privileges to both research experimentation repositories and    |
|      the production Feature Store.                                                                 |
|    - Training features lacked cryptographic hashing (SHA-256), digital signing, and dual-peer      |
|      authorization gates prior to training consumption.                                            |
+----------------------------------------------------------------------------------------------------+
| 3. REPORTING & GOVERNANCE DECOUPLING (ISO 42001 A.2.2 / A.3.3 / ISO 27002 6.8)                     |
|    - Retail branch managers had noticed anomalous loan approvals 90 days prior to regulatory       |
|      intervention.                                                                                 |
|    - Because the bank lacked an AI concern reporting channel (A.3.3), staff dismissed the outputs   |
|      as routine model variations rather than escalating them as critical security incidents.       |
+----------------------------------------------------------------------------------------------------+
```

### 2.3 Remediation Architecture
To permanently eliminate these vulnerabilities, the bank implemented an integrated AIMS/ISMS governance architecture. The technical remediation pipeline enforces cryptographic feature provenance, automated impact assessment gates, and real-time production inference circuit breakers.

```mermaid
sequenceDiagram
    autonumber
    participant Dev as ML Engineering / Data Science
    participant Store as Managed Feature Store (A.4.3 / 8.12)
    participant AIA as AI Impact Assessment Engine (6.1.4 / A.5.2)
    participant SecGate as Staging Release Gate (A.6.2.5 / 8.25)
    participant Prod as Production Inference Cluster (8.1)
    participant Telemetry as Telemetry & Drift Monitor (A.6.2.6 / 8.16)
    participant EthicBoard as AI Governance Council (A.3.2 / 5.2)

    Dev->>Store: Submit new training feature set + metadata
    Note over Dev,Store: Enforce Dual-Authorization (2-Person Rule)
    Store->>Store: Compute SHA-256 hash & verify data lineage
    Store->>AIA: Dispatch dataset to AI Impact Assessment Engine
    AIA->>AIA: Calculate Disparate Impact Ratio (DIR) across protected classes
    alt DIR < 0.80 or DIR > 1.25 (Fairness Gate Failed)
        AIA-->>Dev: Reject dataset; trigger Nonconformity Report (Clause 10.2)
        AIA->>EthicBoard: Log fairness failure & bias report
    else DIR within 0.80 - 1.25 (Fairness Gate Passed)
        AIA->>SecGate: Issue cryptographically signed AIA Clearance Certificate
        SecGate->>SecGate: Verify Cosign digital signature & run SAST/SCA scans
        SecGate->>Prod: Canary deploy model with strict RBAC & mTLS
        Prod->>Telemetry: Stream real-time inference inputs and outputs
        Telemetry->>Telemetry: Monitor Population Stability Index (PSI) & demographic parity
        alt Anomaly or Backdoor Trigger Detected
            Telemetry->>Prod: Trip Circuit Breaker: fallback to deterministic rule engine
            Telemetry->>EthicBoard: Escalate high-priority AI Security Incident (A.3.3 / 6.8)
        end
    end
```

---

## 3. Exam Question Bank & Distractor Forensics

### Question 1 (FIRST Action Scenario)
A tier-1 manufacturing corporation with a mature ISO/IEC 27001:2022 certified Information Security Management System plans to implement an autonomous computer-vision quality control robotics system on its assembly lines. The executive committee resolves to adopt ISO/IEC 42001:2023 to certify their artificial intelligence operations. During the initial project kickoff, before procuring vendor hardware or ingesting edge camera feeds, what is the **FIRST** action the cross-functional project committee must execute in accordance with ISO/IEC 42001 Clause 6.1 and Annex A.5?

- A. `(Recommended)` Conduct an AI System Impact Assessment (A.5.2 / Clause 6.1.4) to systematically identify potential adverse impacts on worker physical safety, assembly line continuity, and operational decision risks.
- B. Deploy the commercial off-the-shelf vision model directly into an isolated staging VPC to execute automated technical vulnerability scanning (ISO/IEC 27002 8.8).
- C. Author an entirely decoupled, independent Tier-1 AIMS Quality Manual that completely supersedes and replaces the existing ISO/IEC 27001 documentation suite.
- D. Procure high-density GPU acceleration server clusters and finalize hardware capacity allocation plans (ISO/IEC 42001 A.4.5).

#### Distractor Forensics
* **Option A Analysis (Correct)**: Pursuant to ISO/IEC 42001 Clause 6.1.2 and Clause 6.1.4, an organization must conduct an AI System Impact Assessment prior to system development, procurement, or operational deployment. The findings from this assessment serve as the prerequisite input for defining risk acceptance criteria, determining risk treatment plans (Clause 6.1.3), and selecting applicable Annex A controls.
* **Option B Analysis (Incorrect)**: Performing technical vulnerability scans (ISO 27002 8.8) is an operational engineering control that occurs later in the verification and validation phase. Initiating scanning before establishing system boundaries, operational context, and impact parameters represents an out-of-order execution.
* **Option C Analysis (Incorrect)**: Violates ISO Harmonized Structure principles and Annex D harmonization guidelines. ISO/IEC 42001 is designed to integrate cleanly with ISO/IEC 27001. Replacing the existing ISMS creates duplicative administrative overhead and destroys operational continuity.
* **Option D Analysis (Incorrect)**: Hardware procurement and capacity planning (A.4.5 / ISO 27002 8.6) must be dictated by defined system requirements, model specifications, and impact risk profiles, rather than preceding them.

---

### Question 2 (BEST/MOST Implementation Choice)
An enterprise fintech firm is harmonizing its ISO/IEC 27001:2022 ISMS with ISO/IEC 42001:2023. The organization intends to fine-tune an open-source Large Language Model (LLM) on historical customer support transcripts to automate financial dispute resolution. When integrating ISO/IEC 42001 A.4.3 (Data resources) with ISO/IEC 27002 8.12 (Data leakage prevention) and 8.33 (Test information), which technical architecture represents the **BEST** implementation choice to safeguard data integrity and prevent unauthorized data poisoning?

- A. `(Recommended)` Establish an immutable data ingestion pipeline that logs cryptographic provenance (SHA-256 hashes), enforces automated PII tokenization/masking, conducts spectral anomaly detection for backdoor markers, and requires dual-custody approval before registering feature sets.
- B. Store raw customer transcripts in an encrypted AWS S3 bucket with server-side SSE-S3 encryption and grant unrestricted read permissions to all data science staff via a single shared service role.
- C. Ingest the entire unscrubbed transcript corpus directly into fine-tuning scripts, and rely solely on output semantic filtering (prompt firewalls) to block PII leakage during live customer inference.
- D. Restrict data access by downloading transcript files directly onto local encrypted NVMe drives of developer workstations, completely isolating data from enterprise network interfaces.

#### Distractor Forensics
* **Option A Analysis (Correct)**: Integrates cryptographic verification (ISO 27002 8.24), data leakage prevention and privacy masking (ISO 27002 8.12, 8.33), data resource quality and poisoning defense (ISO 42001 A.4.3), and segregation of duties (ISO 42001 A.3.2 / ISO 27002 5.3) into a single verifiable architectural control gate.
* **Option B Analysis (Incorrect)**: While server-side encryption protects data at rest (ISO 27002 8.24), granting unrestricted access via a shared IAM role violates segregation of duties (ISO 27002 5.3 / A.3.2) and least privilege (ISO 27002 5.15), leaving the pipeline vulnerable to insider data tampering.
* **Option C Analysis (Incorrect)**: Training on raw, unmasked PII severely violates data protection principles and ISO 27002 8.33. Relying entirely on post-generation output guardrails fails to address model memorization, training data extraction attacks, or systemic model poisoning.
* **Option D Analysis (Incorrect)**: Storing training datasets locally on developer laptops violates centralized asset inventory management (ISO 27002 5.9 / A.4.2), destroys auditability and data lineage tracking, and creates high-risk endpoints vulnerable to device theft or exfiltration.

---

### Question 3 (NEXT Procedural Step Scenario)
An insurance carrier acts strictly as an **AI Deployer**, licensing a commercial third-party machine learning system to triage auto insurance claims. The carrier does not develop models, fine-tune neural weights, or write ML training code. During the drafting of their ISO/IEC 42001 Statement of Applicability (SoA) under Clause 6.1.3, the project team determines that Annex A.6 (AI system lifecycle and development) controls related to internal algorithm training are not directly performed by the carrier. What is the **NEXT** procedural step the organization must execute to remain fully compliant with ISO/IEC 42001?

- A. `(Recommended)` Document the specific justification for the exclusion of internal training controls in the Statement of Applicability (SoA), while verifying that deployer controls, specifically Annex A.9 (AI system use) and Annex A.10 (Third-party relationships), are fully retained and audited.
- B. Unilaterally delete Annex A.6, A.9, and A.10 from the SoA template, certifying compliance solely against the management requirements of Clause 4 through Clause 10.
- C. Demand that the commercial software vendor transfer all proprietary model weights and training source code to the carrier to enable redundant internal model validation.
- D. Issue a formal waiver declaring that third-party ISO/IEC 27001 certification held by the vendor legally exempts the carrier from all operational AI risk management duties.

#### Distractor Forensics
* **Option A Analysis (Correct)**: ISO/IEC 42001 Clause 6.1.3 mandates that any exclusion of Annex A controls must be explicitly documented and justified within the Statement of Applicability (SoA). When acting solely as an AI Deployer, internal model development controls may be excluded, but third-party governance (Annex A.10) and responsible operational deployment (Annex A.9) become strictly mandatory.
* **Option B Analysis (Incorrect)**: Completely excising Annex A controls without structured justification violates Clause 6.1.3. An organization cannot certify against ISO/IEC 42001 while omitting applicability comparisons against normative Annex A controls.
* **Option C Analysis (Incorrect)**: Demanding vendor proprietary source code and weights is commercially unfeasible and unnecessary; third-party assurance is governed through contractual Service Level Agreements (SLAs), supplier risk assessments (A.10.1), and independent validation reports.
* **Option D Analysis (Incorrect)**: A vendor's ISO/IEC 27001 certificate only attests to the vendor's internal information security practices. It does not validate how the deployer configures, integrates, or oversees the AI system within its own operational environment.

---

### Question 4 (PRIMARY Focus / EXCEPT Scenario)
When establishing an internal organization structure for AI governance pursuant to ISO/IEC 42001 Annex A.3 and aligning it with ISO/IEC 27002:2022 organizational controls (Clause 5 and Clause 6), all of the following architectural practices are mandatory **EXCEPT**:

- A. Defining clear segregation of duties between algorithmic model builders, production release authorities, and independent model validation teams (A.3.2 / ISO 27002 5.3).
- B. Implementing an escalation channel enabling employees and external operators to report AI hallucinations, bias, and unexpected model decisions without fear of reprisal (A.3.3 / ISO 27002 6.8).
- C. `(Recommended)` Requiring that all machine learning production incident triage, ethical risk assessments, and model rollback decisions be executed exclusively by the Chief Information Security Officer (CISO) without cross-functional consultation.
- D. Establishing documented competence and awareness requirements for data labeling personnel and prompt engineers regarding prompt injection and data poisoning threats (A.4.6 / ISO 27002 6.3).

#### Distractor Forensics
* **Option C Analysis (Correct Choice - Represents the Prohibited/Excepted Anti-Pattern)**: ISO/IEC 42001 emphasizes cross-functional governance. Vesting sole, unassisted authority over AI ethics, data provenance, and algorithmic risk in the CISO violates Clause 5.1 and A.3.2 principles, which require coordinated collaboration across legal, compliance, data science, and business leadership.
* **Option A Analysis (Compliant Implementation)**: Aligning A.3.2 with ISO 27002 5.3 enforces segregation of duties between model developers and production deployers, preventing unauthorized tampering and rogue model deployments.
* **Option B Analysis (Compliant Implementation)**: Establishing an open reporting channel aligns with A.3.3 and ISO 27002 6.8, ensuring timely identification and escalation of model anomalies and ethical breaches.
* **Option D Analysis (Compliant Implementation)**: Conforms to ISO 42001 A.4.6 and ISO 27002 6.3 by ensuring that human resources engaged in the AI lifecycle possess verified competence and threat awareness.
