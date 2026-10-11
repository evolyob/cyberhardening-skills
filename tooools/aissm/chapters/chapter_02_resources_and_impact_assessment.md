# Chapter 02: Annex A.4 (Resources) & Annex A.5 (AI Impact Assessment) Crosswalk

## 1. Statutory Baseline & Technical Control Matrix

### 1.1 Annex A.4 Resources for AI Systems vs ISO/IEC 27002:2022 Technical Mapping
ISO/IEC 42001:2023 Annex A.4 establishes normative controls for provisioning, tracking, and securing the resources required across the AI system lifecycle. AI resource governance spans training datasets, algorithmic tooling, computational clusters (GPUs/TPUs), and specialized human competencies. Traditional ISO/IEC 27002:2022 asset controls prioritize stationary IT infrastructure and confidential records; Annex A.4 expands this boundary to capture dynamic data lineages, specialized ML toolchains, and mathematical model weights.

| ISO 42001 Control | Control Title & Scope | ISO 27002:2022 Mapping | Integration Type | Technical Implementation & Telemetry Controls | Target Metrics (KPI / KRI / KCI) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A.4.1** | **Resources for AI Systems (Objective)** | **7.1** Physical security perimeters<br>**8.1** User endpoint devices | **Governance Baseline** | Establish organizational processes to define, procure, track, and manage data, tooling, compute infrastructure, and skilled personnel across all AI lifecycle stages. | **KPI**: AI resource baseline allocation approved by governance board prior to project initiation (100%). |
| **A.4.2** | **Documentation of Resources** | **5.9** Inventory of assets<br>**5.37** Documented operating procedures | **Existing Extension** | Maintain a dedicated AI Asset Inventory tracking training datasets, feature repositories, model weight checkpoints, training scripts, hyperparameter configurations, and software dependency manifests (SBOM). | **KPI**: AI Asset Inventory coverage across active production pipelines = 100%.<br>**KCI**: Quarterly asset reconciliation audit achieves 100% concordance between physical records and repository states. |
| **A.4.3** | **Data Resources** | **8.10** Information deletion<br>**8.12** Data leakage prevention<br>**8.33** Test information | **AI-Specific Deepening** | Verify training and validation data provenance, licensing scope, and labeling integrity. Enforce spectral anomaly filtering to prevent data poisoning. Mask PII in test and training splits. Compute SHA-256 digests for dataset integrity. | **KRI**: Zero instances of unvetted or unlicensed datasets integrated into production pipelines.<br>**KCI**: Cryptographic hash verification compliance for all ingestion batches = 100%. |
| **A.4.4** | **Tooling Resources** | **8.25** Secure development life cycle<br>**8.30** Outsoourced development | **AI-Specific Deepening** | Control access and configuration baselines for MLOps toolchains (e.g., MLflow, Kubeflow, feature stores, data labeling platforms). Audit third-party labeling vendors for security posture and data transit security. | **KRI**: Unpatched high/critical vulnerabilities in MLOps platform dependencies older than 14 days = 0.<br>**KPI**: Retention rate of labeling audit trail logs = 100%. |
| **A.4.5** | **System and Computing Resources** | **7.1** Physical security perimeters<br>**8.1** User endpoint devices<br>**8.6** Capacity management | **Existing Extension** | Telemetry monitoring for GPU/TPU clusters, high-bandwidth memory, and distributed training interconnects. Implement strict network isolation between training sandboxes and production inference enclaves. | **KPI**: Maintain compute cluster operational load between 65% and 85%.<br>**KRI**: Zero unauthorized compute instances or unallocated resource spikes detected. |
| **A.4.6** | **Human Resources** | **6.1** Screening<br>**6.3** Information security awareness | **Existing Extension** | Conduct technical and background screening for data labelers and ML engineers. Deliver semi-annual training on prompt injection mitigation, algorithmic bias identification, and data protection compliance. | **KPI**: Training completion rate for machine learning personnel >= 95%.<br>**KCI**: Simulated prompt injection and data poisoning defense drill pass rate >= 90%. |

---

### 1.2 Annex A.5 Assessing Impacts of AI Systems vs ISO/IEC 27002:2022 Risk Governance Matrix
ISO/IEC 42001:2023 Annex A.5 introduces the statutory mandate for AI System Impact Assessments (AIA). Unlike traditional ISO 27005 risk assessments, which evaluate harm to the organization's information assets, an AIA focuses outward: assessing potential negative impacts on individuals (privacy, autonomy, civil liberties), protected demographic groups (discrimination, exclusion), and broader society (critical infrastructure, democratic processes, environmental footprint).

| ISO 42001 Control | Control Title & Scope | ISO 27002:2022 Mapping | Integration Type | Technical Implementation & Telemetry Controls | Target Metrics (KPI / KRI / KCI) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A.5.1** | **Assessing Impacts of AI Systems (Objective)** | **5.7** Threat intelligence<br>**8.25** Secure development life cycle | **Governance Baseline** | Ensure the organization establishes and executes systematic assessment procedures to evaluate potential consequences of AI systems on individuals, groups, and society. | **KCI**: AI System Impact Assessment operational coverage across all production AI initiatives = 100%. |
| **A.5.2** | **AI System Impact Assessment Process** | **5.7** Threat intelligence<br>**8.8** Technical vulnerability management | **AIMS Unique** | Define dynamic event-triggered assessment triggers: trigger re-assessments upon new model scope, ingestion of new data classes, algorithm architectural shifts, or expanded deployment contexts. | **KPI**: Impact assessment completed and approved prior to production model promotion (100%).<br>**KRI**: Zero unmitigated high-impact risks identified during pre-deployment audits. |
| **A.5.3** | **Documentation of AI System Impact Assessments** | **5.37** Documented operating procedures | **AIMS Unique** | Produce formal AI System Impact Assessment (AIA) Reports documenting stakeholder registries, harm severity rankings, likelihood scores, residual risk treatments, and sign-offs. | **KPI**: Version completeness and audit traceability of AIA documentation = 100%. |
| **A.5.4** | **Assessing Impact on Individuals or Groups** | **5.34** Privacy and protection of PII<br>*(Extended to ISO/IEC 27701)* | **AIMS Unique** | Quantify algorithmic bias and disparity across demographic groups using Disparate Impact Ratio (DIR) and Equalized Odds difference metrics. Evaluate impacts on consumer rights, physical safety, and personal autonomy. | **KCI**: Model Disparate Impact Ratio maintained within the statutory range of 0.80 to 1.25 across all protected attributes.<br>**KRI**: Zero substantiated algorithmic discrimination claims. |
| **A.5.5** | **Assessing Societal Impacts of AI Systems** | **5.5** Contact with authorities<br>**5.30** ICT readiness for business continuity | **AIMS Unique** | Analyze broad macroeconomic consequences, labor displacement, systemic public infrastructure dependencies, and carbon footprint from compute cycles. Enforce fallback protocols to prevent societal disruption. | **KPI**: Energy consumption and carbon accounting tracked for 100% of large-scale model training runs.<br>**KCI**: Redundant human-takeover failover drills verified successfully annually (100%). |

---

## 2. Production Incident & Remediation Architecture

### 2.1 Incident Context: Clean-Label Backdoor Poisoning and Demographic Disparity in a Clinical Diagnostic Model
A regional healthcare alliance deployed an automated deep learning computer-aided detection (CADe/CADx) system across emergency radiology departments to identify acute pneumonia and early-stage pulmonary nodules from digital chest radiographs.

During the fourth month of clinical operation, an external academic medical audit revealed two critical defects:
1. **Severe Demographic Disparity**: The model exhibited a false negative rate of 31.4% for patients aged 65 and older, compared to an average false negative rate of 4.2% for patients aged 18 to 45.
2. **Clean-Label Backdoor Poisoning**: To expand training corpora for rare thoracic lesions, data engineers had batch-downloaded 12,000 public radiographs from an unvetted open-source research archive. Forensic investigation discovered that an adversarial actor had embedded an imperceptible, high-frequency spectral watermark (a clean-label backdoor trigger) into 400 images labeled as normal. When the model encountered this trigger pattern during runtime, it systematically classified high-risk malignancies as benign.

### 2.2 Root Cause Analysis (RCA)

```text
+----------------------------------------------------------------------------------------------------+
|                                    ROOT CAUSE ANALYSIS TAXONOMY                                    |
+----------------------------------------------------------------------------------------------------+
| 1. DATA RESOURCE INTEGRITY & PROVENANCE BREAKDOWN (ISO 42001 A.4.3 / ISO 27002 8.12, 8.33)         |
|    - The engineering group ingested external datasets without verifying digital source signatures  |
|      or validating publisher licensing boundaries.                                                 |
|    - The pipeline lacked spectral frequency decomposition and data hygiene checks to detect        |
|      adversarial watermark triggers prior to model ingestion.                                       |
+----------------------------------------------------------------------------------------------------+
| 2. SUPERFICIAL IMPACT ASSESSMENT & ABSENCE OF DYNAMIC TRIGGERS (ISO 42001 A.5.2 / A.5.4)           |
|    - The baseline AIA was conducted as a static paper checklist during initial project kickoff.   |
|    - Ingesting a massive unvetted dataset constituted a major operational change, yet failed to     |
|      trigger a secondary impact assessment across protected age demographics.                       |
+----------------------------------------------------------------------------------------------------+
| 3. INADEQUATE TOOLCHAIN RBAC & WORKSPACE ISOLATION (ISO 42001 A.4.4 / A.4.5 / ISO 27002 8.25)     |
|    - The shared enterprise feature repository and GPU training clusters lacked Role-Based Access    |
|      Control (RBAC). Data scientists could push local, unverified data batches directly into        |
|      automated training pipelines without dual-person authorization.                               |
+----------------------------------------------------------------------------------------------------+
```

### 2.3 Remediation Architecture
To resolve these systemic risks, the healthcare alliance established an automated ingestion inspection and dynamic impact assessment pipeline complying with ISO/IEC 42001 Annex A.4 and Annex A.5 controls.

```mermaid
sequenceDiagram
    autonumber
    participant Ext as External Data Provider
    participant Ingest as Data Ingestion & Sanitization Gate (A.4.3 / 8.12)
    participant FeatStore as Immutable Feature Store (A.4.2 / 5.9)
    participant AIAGate as Dynamic AIA Engine (A.5.2 / A.5.4)
    participant TrainCluster as Isolated GPU Cluster (A.4.5 / 8.6)
    participant AuditLog as Evidentiary Archive (A.5.3 / 5.37)

    Ext->>Ingest: Transmit candidate image dataset + metadata
    Ingest->>Ingest: Validate cryptographic source signature & license bounds
    Ingest->>Ingest: Execute spectral analysis & clean-label backdoor scan
    alt Data signature invalid or adversarial noise detected
        Ingest-->>Ext: Reject batch; trigger Security Incident Alert (ISO 27002 6.8)
    else Data sanitization and integrity checks pass
        Ingest->>FeatStore: Register versioned features with immutable SHA-256 hash
        FeatStore->>AIAGate: Trigger event-driven A.5.2 Impact Assessment
        AIAGate->>AIAGate: Evaluate demographic parity & DIR across age brackets
        alt Disparate Impact Ratio < 0.80 (Fairness Threshold Failed)
            AIAGate-->>FeatStore: Block training entitlement; generate AIA Defect Report
        else AIA validation benchmarks satisfied
            AIAGate->>AuditLog: Archive signed AI System Impact Assessment Report (A.5.3)
            AIAGate->>TrainCluster: Issue cryptographically signed Training Ticket
            TrainCluster->>TrainCluster: Execute distributed training while monitoring compute load
        end
    end
```

---

## 3. Exam Question Bank & Distractor Forensics

### Question 1 (FIRST Action Scenario)
A multinational financial institution holding active ISO/IEC 27001:2022 certification plans to train a deep learning fraud detection system by pooling customer financial transaction histories across several regional subsidiaries. The enterprise is implementing ISO/IEC 42001:2023. During the initial design phase, before data engineers extract transaction streams into a centralized feature repository, what is the **FIRST** action the project governance team must execute pursuant to Annex A.4.3 (Data resources) and Annex A.5.2 (AI system impact assessment process)?

- A. `(Recommended)` Determine the lawful basis, licensing constraints, and cross-border regulatory boundaries of the pooled data, and conduct an initial AI System Impact Assessment to evaluate potential adverse consequences on account holders.
- B. Purchase and configure distributed GPU server racks in the primary datacenter and execute performance benchmarking on raw ingestion bandwidth (ISO/IEC 42001 A.4.5).
- C. Build production REST API endpoints for real-time model scoring and expose them to regional networks for operational latency profiling.
- D. Strip primary user names from account records and immediately transfer the raw transactions to a third-party commercial labeling platform for pattern annotation.

#### Distractor Forensics
* **Option A Analysis (Correct)**: Under ISO/IEC 42001 A.4.3 and A.5.2, an organization must establish data provenance, regulatory constraints, and potential harm profiles before data consolidation and model engineering commence. Completing the initial AI System Impact Assessment defines operational boundaries and informs subsequent risk treatment plans.
* **Option B Analysis (Incorrect)**: Hardware procurement and capacity configuration (A.4.5) are downstream implementation tasks. Procuring compute before establishing legal authority, data boundaries, and impact risk profiles risks deploying invalid infrastructure.
* **Option C Analysis (Incorrect)**: Building and exposing production API endpoints prior to data verification and impact assessment violates secure development baselines (ISO/IEC 27002 8.25) and basic project lifecycle sequence.
* **Option D Analysis (Incorrect)**: Handing over unvetted data to an external vendor without contractual controls or formal impact assessments violates third-party governance (ISO/IEC 27002 8.30 / ISO 42001 A.10.1) and risks severe data leakage.

---

### Question 2 (BEST/MOST Implementation Choice)
When integrating ISO/IEC 42001 A.4.3 (Data resources), A.4.2 (Documentation of resources), and ISO/IEC 27002 8.12 (Data leakage prevention), which technical architecture represents the **BEST** practice for guaranteeing dataset integrity and mitigating clean-label data poisoning when preparing millions of unstructured text records to fine-tune an internal Large Language Model?

- A. `(Recommended)` Establish an immutable data lake repository enforcing cryptographic checksums (SHA-256), tracking data lineage manifests, executing automated semantic anomaly screening, and requiring dual-custody approval before dataset registration.
- B. Store text corpora on individual data science laptops equipped with full-disk encryption (BitLocker) to avoid enterprise network exposure.
- C. Run a basic string deduplication script across text files and review five randomly selected output samples manually following model completion.
- D. Compress the raw text files into password-protected zip archives and upload them to an unmonitored external cloud storage bucket.

#### Distractor Forensics
* **Option A Analysis (Correct)**: Combines immutable versioning and lineage tracking (A.4.2), cryptographic hash verification for integrity (ISO 27002 8.24), anomaly scanning for poisoning defense (A.4.3), and segregation of duties via dual custody (ISO 27002 5.3).
* **Option B Analysis (Incorrect)**: Storing training corpora across developer laptops violates centralized asset management (ISO 27002 5.9 / A.4.2), impairs auditability, eliminates data lineage tracking, and creates endpoint security risks.
* **Option C Analysis (Incorrect)**: Simple deduplication does not detect semantic or spectral data poisoning. Inspecting five generated samples after training provides statistically negligible verification and violates rigorous testing controls.
* **Option D Analysis (Incorrect)**: Uploading corporate data to unmanaged external repositories violates basic data protection principles (ISO/IEC 27002 5.9, 8.12) and introduces immediate exposure risks.

---

### Question 3 (NEXT Procedural Step Scenario)
An insurtech company develops an automated machine learning model to evaluate property insurance claims. The team completes initial model training and drafts the baseline impact assessment. During the execution of A.5.4 (Assessing impact on individuals or groups), fairness analysis reveals that claim approval rates for properties in lower-income postal codes are significantly depressed, resulting in a Disparate Impact Ratio (DIR) of 0.65 (falling below the acceptable regulatory threshold of 0.80). In accordance with ISO/IEC 42001 A.5.2 and A.5.3, what is the **NEXT** procedural step the project team must execute?

- A. `(Recommended)` Document the observed disparity and its severity in the formal AI System Impact Assessment Report, formulate algorithmic remediation strategies (such as re-weighting or balanced resamplng), and submit the findings to the AI Governance Committee for determination.
- B. Omit the disparity metrics from the final documentation and manually edit the validation dataset labels to simulate demographic balance.
- C. Deploy the model into live production immediately to assess whether actual policyholders file formal administrative complaints.
- D. Terminate all artificial intelligence initiatives enterprise-wide and disband the data science engineering organization.

#### Distractor Forensics
* **Option A Analysis (Correct)**: Pursuant to ISO/IEC 42001 A.5.2 and A.5.3, any significant adverse impact identified during evaluation must be documented transparently in the AIA Report, coupled with concrete mitigation proposals and escalated to designated governance authorities for risk decisions.
* **Option B Analysis (Incorrect)**: Falsifying evaluation metrics and concealing unfavorable findings directly violates documentation requirements (A.5.3), standard ethics, and statutory compliance.
* **Option C Analysis (Incorrect)**: Deploying a system with known adverse impacts prior to executing risk treatments violates core risk management mandates (Clause 6.1.3, Clause 8.3) and exposes the firm to severe legal liability.
* **Option D Analysis (Incorrect)**: Disbanding the entire team is a disproportionate reaction that ignores standard risk treatment cycles. Technical interventions such as data re-balancing, fair representation learning, or algorithmic constraints routinely remediate these defects.

---

### Question 4 (PRIMARY Focus / EXCEPT Scenario)
When integrating ISO/IEC 42001 A.4.5 (System and computing resources) with ISO/IEC 27002 8.6 (Capacity management) to support enterprise high-performance AI training and inference infrastructure, all of the following technical controls are required **EXCEPT**:

- A. Implementing automated telemetry to track GPU memory consumption, job scheduling queues, and inference latency against pre-defined alert thresholds.
- B. Configuring elastic auto-scaling policies within cloud environments to prevent resource exhaustion and denial-of-service conditions during high demand.
- C. `(Recommended)` Permitting all internal machine learning contractors to share a single root administrative SSH credential to simplify compute node cluster management and reduce software license expenses.
- D. Tracking energy draw and carbon emissions associated with large-scale model training clusters as part of organizational societal impact monitoring.

#### Distractor Forensics
* **Option C Analysis (Correct Choice - Represents the Prohibited/Excepted Anti-Pattern)**: Sharing root administrative credentials across contractors directly violates identity management (ISO/IEC 27002 5.16), access control (ISO/IEC 27002 5.15), and accountability requirements. Compute resources governed under A.4.5 must maintain individual attribution and least-privilege access.
* **Option A Analysis (Compliant Implementation)**: Aligning with ISO/IEC 27002 8.6, continuous monitoring of hardware resources ensures system availability and identifies operational bottlenecks.
* **Option B Analysis (Compliant Implementation)**: Dynamic scaling safeguards availability and protects inference endpoints from resource exhaustion under burst loads.
* **Option D Analysis (Compliant Implementation)**: Conforms to ISO/IEC 42001 A.4.5 and A.5.5 guidance concerning environmental impact accounting and sustainable resource stewardship.
