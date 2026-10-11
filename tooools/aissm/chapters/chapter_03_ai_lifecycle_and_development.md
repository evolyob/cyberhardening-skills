# Chapter 03: Annex A.6 (AI System Lifecycle & MLOps Development) Controls

## 1. Statutory Baseline & Technical Control Matrix

### 1.1 Annex A.6 Management & Development Controls vs ISO/IEC 27002:2022 Technical Mapping
ISO/IEC 42001:2023 Annex A.6 establishes comprehensive controls governing the artificial intelligence lifecycle from conceptualization, specification, and architectural design through development, verification, deployment, operational monitoring, and decommissioning. Traditional software engineering covered under ISO/IEC 27002:2022 focuses on deterministic code defects and static application vulnerabilities; Annex A.6 expands this discipline into probabilistic MLOps workflows, tracking non-deterministic model behaviors, distribution shifts, and adversarial data perturbations.

| ISO 42001 Control | Control Title & Scope | ISO 27002:2022 Mapping | Integration Type | Technical Implementation & Telemetry Controls | Target Metrics (KPI / KRI / KCI) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **A.6.1.1** | **Management Guidance for AI Systems (Objective)** | **8.25** Secure development life cycle | **Governance Baseline** | Establish organizational governance policies and engineering guidelines ensuring responsible and trustworthy AI design throughout all lifecycle phases. | **KPI**: Adoption rate of responsible AI development guidelines across internal engineering units = 100%. |
| **A.6.1.2** | **Objectives for Responsible AI System Development** | **8.26** Application security requirements | **AI-Specific Deepening** | Formulate operational objectives for fairness, transparency, explainability, safety, privacy, and accountability during project inception; document anticipated benefits and misuse threat models. | **KPI**: System specification documents containing defined responsible AI metric thresholds = 100%. |
| **A.6.1.3** | **Processes for Responsible AI Design and Development** | **8.25** Secure development life cycle<br>**8.27** Secure system architecture | **AI-Specific Deepening** | Embed trust criteria (fault tolerance, defensive distillation, model interpretability frameworks, human-in-the-loop overrides) into corporate software engineering baselines. | **KCI**: MLOps continuous delivery gate compliance audit pass rate = 100%. |
| **A.6.2.1** | **AI System Development Lifecycle (Objective)** | **8.25** Secure development life cycle | **Governance Baseline** | Ensure every development stage (specification, data engineering, model design, verification, deployment, operation, decommissioning) follows formal verification gates. | **KPI**: Documented lifecycle stage gate approvals completed for 100% of production-promoted models. |
| **A.6.2.2** | **AI System Requirements and Specification** | **8.26** Application security requirements | **AI-Specific Deepening** | Specify technical requirements for accuracy, inference latency, explainability (SHAP/LIME), bias tolerances (DIR 0.80 - 1.25), data drift thresholds (PSI < 0.10), and differential privacy budgets. | **KPI**: System requirements documentation coverage for non-functional AI metrics = 100%. |
| **A.6.2.3** | **AI System Design and Development Documentation** | **8.28** Secure coding<br>**8.30** Outsourced development | **AI-Specific Deepening** | Maintain end-to-end provenance linking training scripts, dataset digests, hyperparameters, and resulting model weight checkpoints. Require Cosign digital signatures on container images and weights. | **KPI**: Verification rate of cryptographic digital signatures on registered model artifacts = 100%. |
| **A.6.2.4** | **AI System Verification and Validation (V&V)** | **8.29** Security testing<br>**8.31** Separation of development, test and production | **Existing Extension** | Execute dual-track evaluation: Verification (conformance to algorithmic specifications) and Validation (fitness for intended purpose). Execute adversarial red-teaming, evasion testing, and out-of-distribution stress testing. | **KPI**: Pre-release adversarial red-team test pass rate >= 90%.<br>**KCI**: Test execution conducted exclusively in isolated staging sandboxes (100%). |
| **A.6.2.5** | **AI System Deployment** | **8.25** Secure development life cycle<br>**8.32** Change management | **Existing Extension** | Enforce canary releases, shadow mode deployments, and blue-green traffic splits with automated rollback switches triggered when live error or drift thresholds breach tolerances. | **KPI**: Rollback automation drill executed successfully within < 5 minutes.<br>**KCI**: Minimum shadow mode evaluation duration >= 14 consecutive days prior to live traffic cutover. |
| **A.6.2.6** | **AI System Operation and Monitoring** | **8.8** Technical vulnerability management<br>**8.16** Monitoring activities | **AI-Specific Deepening** | Implement continuous telemetry measuring data drift (Wasserstein Distance, PSI), concept drift, prediction confidence decay, and anomalous query payloads. Trigger automated alerts and retraining workflows. | **KRI**: Unresolved critical drift alerts exceeding 2-hour response SLA = 0.<br>**KPI**: Real-time inference monitoring telemetry coverage across active endpoints = 100%. |
| **A.6.2.7** | **Technical Documentation of AI Systems** | **5.37** Documented operating procedures<br>**8.27** Secure system architecture | **AI-Specific Deepening** | Author standardized Model Cards, Data Sheets, operating manuals, graceful degradation guidelines, manual override SOPs, and dependency bills of materials (SBOM). | **KPI**: Model Card and technical documentation audit completeness = 100%. |
| **A.6.2.8** | **AI System Event Logging** | **8.12** Data leakage prevention<br>**8.15** Logging | **Existing Extension** | Record inference input tokens/features, predicted probabilities, operator override interventions, and runtime exceptions. Store logs in tamper-evident, append-only repositories while masking PII. | **KPI**: Cryptographically protected inference decision audit log retention rate = 100%. |

---

### 1.2 Secure MLOps Pipeline Quality Gates & Security Baselines
To embed ISO/IEC 42001 Annex A.6 controls into practical engineering execution, organizations map lifecycle requirements to six automated continuous delivery gates integrated with ISO/IEC 27002:2022 security controls.

| Gate ID & Name | Lifecycle Phase | Input Artifacts | Verification Criteria (ISO 42001 / ISO 27002) | Tooling & Automated Enforcement | Exit Gate Acceptance Criteria |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **G1: Concept & Scope** | A.6.1.2 / A.6.2.2 | Business requirements document, initial architecture spec | **8.26**: Verification of non-functional metrics (accuracy, latency, explainability).<br>**A.5.2**: Initial AI System Impact Assessment completed. | Policy-as-code linting, requirements validation templates. | Formal sign-off on System Requirements Specification and initial AIA Report. |
| **G2: Secure Engineering** | A.6.2.3 | Algorithmic source code, feature extraction scripts, dependencies | **8.28**: Static Application Security Testing (SAST).<br>**8.30**: Software Composition Analysis (SCA) for third-party libraries and licenses. | SonarQube, Snyk, Bandit, Trivy. | Zero high or critical unpatched CVEs in ML dependencies; zero proprietary license conflicts. |
| **G3: Verification & Validation** | A.6.2.4 | Candidate model weights, golden test datasets | **8.29**: Adversarial perturbation robustness (FGSM, PGD).<br>**8.31**: Out-of-distribution (OOD) stress testing in isolated enclaves. | Deepchecks, CleverHans, Foolbox, Fairlearn. | Accuracy and F1-score exceed baseline thresholds; adversarial robustness pass rate >= 90%; DIR between 0.80 and 1.25. |
| **G4: Controlled Release** | A.6.2.5 | Container images, inference service manifests | **8.32**: Formal change management approval.<br>**A.6.2.3**: Digital signing of model weights and container digest via Cosign. | MLflow Model Registry, Cosign, Tekton / GitHub Actions. | Cryptographic signature verified; automated canary traffic deployment configured with rollback triggers. |
| **G5: Production Telemetry** | A.6.2.6 / A.6.2.8 | Live inference query streams, prediction outputs | **8.16**: Continuous drift telemetry.<br>**8.8**: Concept drift and data drift alerting.<br>**8.15**: Append-only tamper-evident logging. | Evidently AI, Prometheus, Grafana, OpenSearch. | Population Stability Index (PSI) < 0.10; alerts fire if PSI >= 0.25; 100% of decisions logged with PII masked. |
| **G6: Decommissioning** | Lifecycle Termination | Decommissioning plan, model archive manifests | **8.10**: Safe deletion of temporary training artifacts and cached endpoints.<br>**8.14**: Long-term archiving of model cards and audit trails. | Cloud lifecycle policies, immutable WORM storage. | Inference endpoints terminated, API keys revoked, historical artifacts archived for statutory retention periods. |

---

## 2. Production Incident & Remediation Architecture

### 2.1 Incident Context: Concept Drift and Unauthorized Edge Hot-Patching in an Autonomous Guided Vehicle Fleet
An automated logistics enterprise deployed a fleet of 150 Autonomous Guided Vehicles (AGVs) within an industrial intermodal cargo hub. The vehicles ran deep convolutional neural networks (CNNs) for real-time obstacle identification and path collision avoidance.

During an intense seasonal storm involving persistent heavy rainfall and dense fog, the visual perception stack experienced severe degradation:
1. **Unmonitored Concept Drift**: Low-contrast camera feeds skewed the input distribution away from normal training parameters. The calculated Population Stability Index (PSI) jumped from a baseline of 0.05 to 0.38. The vehicle obstacle miss rate escalated from 0.15% to 16.3%, causing several minor collisions with physical barricades.
2. **Unauthorized Production Hot-Patching**: Confronted with rising delivery backlogs, on-call support engineers bypassed formal change management gates (ISO 27002 8.32) and code review workflows. They compiled an unvetted image-filtering script on a personal laptop, embedded hardcoded administrative tokens, and pushed updated neural weights directly to edge vehicle controllers via an unsecured maintenance SSH channel.
3. **Cascading Day-Time Optical Failure**: The hot-patched filtering weights introduced extreme color oversaturation during normal daylight conditions the following morning. The perception system registered phantom obstacles across clear routes, causing a fleet-wide emergency braking deadlock that paralyzed cargo hub operations for 8.5 hours.

### 2.2 Root Cause Analysis (RCA)

```text
+----------------------------------------------------------------------------------------------------+
|                                    ROOT CAUSE ANALYSIS TAXONOMY                                    |
+----------------------------------------------------------------------------------------------------+
| 1. FAILURE OF OPERATIONAL MONITORING & FAILSFE CIRCUIT BREAKERS (ISO 42001 A.6.2.6 / ISO 27002 8.16)|
|    - The edge perception pipeline monitored CPU/GPU thermal load but lacked real-time statistical  |
|      drift telemetry (Wasserstein distance or PSI) for sensor feeds.                                |
|    - The system had no automated fallback logic (such as switching to secondary LiDAR safety       |
|      scanners and speed restrictions) when visual confidence scores decayed.                       |
+----------------------------------------------------------------------------------------------------+
| 2. TOTAL COLLAPSE OF CHANGE MANAGEMENT & RELEASE CONTROLS (ISO 42001 A.6.2.3 / A.6.2.5 / 8.32)     |
|    - The edge runtime accepted binary updates without validating cryptographic signatures          |
|      against an enterprise Model Registry.                                                         |
|    - Engineers bypassed segregation of duties, using administrative backdoors to push unapproved    |
|      weights directly to production hardware.                                                      |
+----------------------------------------------------------------------------------------------------+
| 3. INSUFFICIENT V&V ACROSS OUT-OF-DISTRIBUTION CONDITIONS (ISO 42001 A.6.2.4 / ISO 27002 8.29)      |
|    - Pre-deployment validation datasets exclusively represented clear-weather daytime runs.         |
|    - The validation suite omitted stress testing against adverse meteorological conditions,        |
|      leaving out-of-distribution blind spots undiscovered prior to live operational release.        |
+----------------------------------------------------------------------------------------------------+
```

### 2.3 Remediation Architecture
To permanently prevent unauthorized modifications and handle distributional shift safely, the logistics enterprise engineered an end-to-end MLOps pipeline compliant with ISO/IEC 42001 Annex A.6 and ISO/IEC 27002:2022.

```mermaid
sequenceDiagram
    autonumber
    participant Edge as Edge AGV Perception Node
    participant Telemetry as Telemetry & Drift Engine (A.6.2.6 / 8.16)
    participant Failsafe as Drift Analyzer & Circuit Breaker
    participant Retrain as Automated Retraining Pipeline (A.6.2.6 / 8.25)
    participant VVGate as V&V Adversarial Testing Gate (A.6.2.4 / 8.29)
    participant Registry as Immutable Model Registry (A.6.2.3 / 8.32)
    participant Canary as Canary Deployment Controller (A.6.2.5)

    Edge->>Telemetry: Stream inference confidence scores and feature summaries
    Telemetry->>Failsafe: Compute Population Stability Index (PSI) in 60s windows
    alt PSI >= 0.25 or Confidence < Safety Threshold
        Failsafe->>Edge: Trigger Failsafe Mode: Speed Reduction + LiDAR Secondary Interlock
        Failsafe->>Retrain: Transmit anomalous edge samples to quarantined training queue
        Retrain->>Retrain: Blend synthetic weather variations & retrain candidate model
        Retrain->>VVGate: Submit candidate model package for comprehensive verification
        VVGate->>VVGate: Execute OOD stress tests, adversarial perturbation, and latency checks
        alt Validation Benchmarks Fail
            VVGate-->>Retrain: Reject candidate model; compile automated defect telemetry
        else All Validation Benchmarks Pass
            VVGate->>Registry: Register model; CI/CD key generates Cosign digital signature
            Registry->>Canary: Dispatch signed release bundle to canary group (5% fleet)
            Canary->>Edge: Push payload via mutual TLS authenticated channel
            Edge->>Edge: Verify Cosign cryptographic signature before hot-swapping weights
        end
    end
```

---

## 3. Exam Question Bank & Distractor Forensics

### Question 1 (FIRST Action Scenario)
The operations engineering team of an enterprise e-commerce platform observes on their real-time telemetry dashboard (governed under ISO/IEC 42001 A.6.2.6 and ISO/IEC 27002 8.16) that the Population Stability Index (PSI) of an autonomous recommendation model has suddenly surged from 0.04 to 0.31 (surpassing the critical warning threshold of 0.25). Simultaneously, recommendation conversion rates and model output confidence have dropped by 35%. Pursuant to ISO/IEC 42001 A.6.2.6 (AI system operation and monitoring), what is the **FIRST** action the operations team must execute?

- A. `(Recommended)` Trigger predefined incident response procedures to evaluate the cause of the input feature anomaly, and activate operational fallback mechanisms (such as rule-based baseline recommendations or system degradation) based on risk assessment.
- B. Permanently wipe all historical inference logs and user interaction tables from production databases to reduce storage infrastructure load.
- C. Instruct database administrators to manually edit user feature tables to match the previous month's statistical averages.
- D. Ignore the telemetry alert and defer analysis until the next annual internal management review meeting.

#### Distractor Forensics
* **Option A Analysis (Correct)**: Under ISO/IEC 42001 A.6.2.6, when operational monitoring reveals acute distributional drift that impairs system performance, the immediate response is to initiate predefined incident procedures and trigger graceful degradation or fallback mechanisms. This prevents anomalous predictions from propagating business damage while root cause investigations begin.
* **Option B Analysis (Incorrect)**: Deleting inference records violates event logging mandates (ISO/IEC 42001 A.6.2.8 / ISO/IEC 27002 8.15), destroying evidentiary records and preventing forensic investigation.
* **Option C Analysis (Incorrect)**: Manually tampering with production data damages data integrity (ISO/IEC 27002 8.12 / ISO/IEC 42001 A.4.3), distorts operational records, and fails to fix the underlying model defect.
* **Option D Analysis (Incorrect)**: Ignoring critical operational alerts breaches continuous monitoring requirements and risks prolonged operational failure and financial loss.

---

### Question 2 (BEST/MOST Implementation Choice)
When establishing an automated continuous integration and verification pipeline (CI/V&V) for a high-consequence computer-vision system in compliance with ISO/IEC 42001 A.6.2.4 (Verification and validation) and ISO/IEC 27002 8.29 (Security testing), which testing methodology represents the **BEST** technical implementation?

- A. `(Recommended)` Execute automated test suites within an isolated staging environment combining adversarial perturbation simulations (e.g., FGSM, PGD attacks), out-of-distribution stress evaluations across diverse environmental conditions, and demographic fairness parity checks, validating results against predefined quality acceptance gates.
- B. Have individual developers capture three personal photographs on mobile devices and verify that the local workstation execution script finishes without syntax exceptions.
- C. Deploy untested model weights directly to public internet endpoints and evaluate reliability solely through customer support escalation volume over 30 days.
- D. Restrict validation exclusively to static Python code formatting tools (such as PEP 8 linters), omitting all performance, robustness, and output verification on trained weights.

#### Distractor Forensics
* **Option A Analysis (Correct)**: Integrates adversarial robustness evaluations, out-of-distribution stress testing, demographic fairness assessments, and formal gate criteria in an isolated staging environment, fully adhering to ISO/IEC 42001 A.6.2.4 and ISO/IEC 27002 8.29 and 8.31.
* **Option B Analysis (Incorrect)**: Testing on three non-representative personal photos without isolated staging or systematic coverage fails to provide statistically valid assurance of model performance or security.
* **Option C Analysis (Incorrect)**: Using public production traffic as an unmonitored test ground violates basic environment separation (ISO/IEC 27002 8.31) and exposes the organization to operational failure.
* **Option D Analysis (Incorrect)**: Syntax linting checks code formatting, not model accuracy, robustness, or inference reliability. It fails to fulfill verification and validation mandates.

---

### Question 3 (NEXT Procedural Step Scenario)
A specialized clinical diagnostic Large Language Model has finished training and satisfied all offline performance benchmarks within an isolated staging enclave (fulfilling A.6.2.4 Verification and validation). In accordance with ISO/IEC 42001 A.6.2.5 (AI system deployment) and ISO/IEC 27002 8.32 (Change management), what is the **NEXT** procedural step the engineering team must execute before routing live production clinical inquiries to the model?

- A. `(Recommended)` Submit a formal change request with verification evidence for authorization, record cryptographically signed model artifacts into an immutable Model Registry, and initiate a phased deployment using canary routing or shadow mode accompanied by automated rollback triggers.
- B. Rename the staging server to production immediately and disable all authentication headers on the inference gateway.
- C. Delete previous model checkpoints and training logs to free up storage space across enterprise drives.
- D. Bypass release review and email uncompiled Python model weights directly to hospital staff for local execution.

#### Distractor Forensics
* **Option A Analysis (Correct)**: Complies with change management (ISO/IEC 27002 8.32) and controlled deployment practices (ISO/IEC 42001 A.6.2.5). Cryptographic signing ensures artifact authenticity, while canary routing and shadow testing minimize clinical disruption, backed by automated rollback capabilities.
* **Option B Analysis (Incorrect)**: Bypassing change authorization and removing access authentication violates access control (ISO/IEC 27002 5.15) and environment separation (ISO/IEC 27002 8.31).
* **Option C Analysis (Incorrect)**: Deleting prior model checkpoints eliminates rollback capability and destroys historical traceability (ISO/IEC 42001 A.6.2.3 / A.6.2.7).
* **Option D Analysis (Incorrect)**: Distributing raw code directly to end users bypasses deployment controls, endpoint management, and standard software distribution governance.

---

### Question 4 (PRIMARY Focus / EXCEPT Scenario)
When an enterprise conducts the formal decommissioning and retirement of a production AI model in accordance with ISO/IEC 42001 lifecycle governance and ISO/IEC 27002 8.10 (Information deletion) and 8.14 (Redundancy/backup), all of the following technical and operational procedures are mandatory **EXCEPT**:

- A. Revoking active API credentials, closing exposed inference endpoints, and disabling routing rules associated with the retired model service.
- B. Archiving model weights, architectural specifications, training lineage metadata, and audit logs within secure, compliant storage in accordance with statutory retention policies.
- C. `(Recommended)` Directing junior staff to delete all historical model training records, checkpoints, and performance audit reports immediately without archival to avoid third-party discovery.
- D. Updating the centralized AI Asset Inventory (A.4.2 / ISO/IEC 27002 5.9) to reflect the decommissioned status of the system and notifying relevant operational stakeholders.

#### Distractor Forensics
* **Option C Analysis (Correct Choice - Represents the Prohibited/Excepted Anti-Pattern)**: Deleting historical weights, training logs, and audit reports without archival violates documentation retention mandates (ISO/IEC 27002 5.37), regulatory accountability requirements, and ISO/IEC 42001 auditability. Legal and regulatory standards require systematic archival to substantiate past decisions.
* **Option A Analysis (Compliant Implementation)**: Terminating network endpoints and revoking credentials prevents orphaned services from becoming unmonitored security liabilities.
* **Option B Analysis (Compliant Implementation)**: Archiving model artifacts and lineage manifests preserves historical context and fulfills regulatory audit obligations.
* **Option D Analysis (Compliant Implementation)**: Updating the asset inventory ensures organizational transparency and maintains accurate configuration records.
