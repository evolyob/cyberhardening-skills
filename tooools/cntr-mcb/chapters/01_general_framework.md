# Chapter 01: General Framework, Detection as Code & Telemetry Taxonomy

## 1. Statutory Baseline & Control Matrix

### 1.1 Executive Mandate & Statutory Alignment (CSMA Compliance)

The Financial Container Security Monitoring & Configuration Baseline establishes the binding technical architecture for financial institutions operating containerized systems across private, hybrid, and multi-cloud environments. Modern microservice deployments alter traditional perimeter defenses through short-lived workload lifecycles, shared host OS kernels, declarative orchestration APIs, and abstracted overlay networks. Traditional quarterly vulnerability assessments and network firewalls fail to inspect runtime namespace escapes, in-memory credential harvesting, and rapid configuration drift within container clusters.

Financial institutions maintain strict statutory accountability under the Cyber Security Management Act (CSMA, Ministry of Digital Affairs Pcode: A0030297, amended 2025-09-24). The statutory framework defines non-negotiable obligations for entities classified as Specific Non-Government Agencies and Critical Infrastructure Providers:

- Information and Communication Systems (Article 3, Item 1): Encompasses all container worker nodes, master control planes, overlay network plugins, and cluster storage arrays handling financial transaction data.
- Information and Communication Services (Article 3, Item 2): Governs deployment pipelines, service meshes, container registries, and API gateways supporting core banking and payment processing services.
- Cyber Security (Article 3, Item 3): Mandates technical safeguards to prevent unauthorized access to, control over, disclosure of, damage to, alteration of, or destruction of containerized financial assets, protecting confidentiality, integrity, and availability.
- Cyber Security Incident (Article 3, Item 4): Classifies any cluster security policy violation, control plane degradation, container escape, or credential leakage as a formal reportable event.
- Specific Non-Government Agency (Article 3, Item 6) & Critical Infrastructure Provider (Article 3, Item 8): Categorizes commercial banks, securities exchanges, clearinghouses, and payment switches as core critical infrastructure requiring stringent technical baselines.
- Products Harmful to National Cyber Security (Article 3, Item 11): Strictly prohibits deployment of untrusted base images, third-party container management plugins, or open-source packages from unverified foreign entities posing supply chain or sovereignty risks.

Under CSMA Article 16, financial institutions must draft, implement, and maintain a Cyber Security Maintenance Plan governed by designated Responsibility Levels (Level A, Level B, and Level C). Tier-1 financial institutions operating payment gateways or deposit ledgers fall under Level A, requiring continuous automated security monitoring, real-time threat feeds, and certified security engineering oversight. The technical controls of the Cyber Security Maintenance Plan map directly to the four baseline tiers of this specification:

- P0 Foundational Telemetry & Traceability: Mandatory retention of raw Kubernetes API server audit events, runtime system calls, and host access logs for a minimum statutory duration of one year.
- P1 Threat Defense & Hardening: Real-time blocking of container privilege escalation (`privileged: true`, `CAP_SYS_ADMIN`), unauthorized hostPath mounts, and interactive shell execution in production pods.
- P2 Environmental Adaptive Defense: Enforcement of immutable root filesystems, behavioral baselines for network sockets, and admission controls verifying cryptographic container image signatures.
- P3 Operational Observability & Collaboration: Multi-cloud telemetry aggregation, automated cross-cluster correlation, and continuous posture evaluation against published benchmarks.

CSMA Article 17 empowers competent authorities to conduct formal audits of container security posture, evaluating Cloud Security Posture Management (CSPM) adherence, Cloud Workload Protection Platform (CWPP) runtime coverage, and immutable log retention configurations. Under CSMA Article 18, discovery of a severe container security incident mandates formal notification to the supervisory authority within one hour, immediate containment of running workloads, and preservation of digital forensic telemetry.

To satisfy these legal and technical mandates, the baseline establishes a dual-track compliance framework combining static configuration hardening with dynamic behavioral detection:

1. Preventative Configuration Baselines (CIS Benchmarks): Enforce deterministic guardrails across container runtimes, node operating systems, orchestration control planes, and cloud compute environments before container workloads transition to production.
2. Behavioral Runtime Detection (MITRE ATT&CK for Containers v19): Deploy continuous telemetry monitoring to intercept, analyze, and quarantine adversary tactics, techniques, and procedures across active clusters.

```
+---------------------------------------------------------------------------------------------------+
|                         FINANCIAL CONTAINER DEFENSE IN DEPTH (CSMA & DeTT&CT)                     |
+---------------------------------------------------------------------------------------------------+
|  PREVENTATIVE CONTROLS (CIS Benchmarks)           |  DETECTIVE & FORENSIC CONTROLS (MITRE ATT&CK) |
|  - CSMA Art. 16: Immutable Node OS Hardening      |  - CSMA Art. 16: K8s API Audit Stream (1+ Yr) |
|  - CSMA Art. 16: Pod Security Admission Rules     |  - CSMA Art. 17: eBPF System Call Tracing     |
|  - CSMA Art. 3(11): Cryptographic Image Signing   |  - CSMA Art. 18: Real-Time Incident Isolation |
|  - P0-P3 Configuration Baselines across Clusters  |  - Detection as Code (DaC) Sigma Pipeline     |
+---------------------------------------------------------------------------------------------------+
```

Financial institutions apply the DeTT&CT (Detect Tactics, Techniques & Combat Threats) framework to systematically evaluate defense posture. By mapping enterprise defensive capabilities (CWPP platforms, admission controllers, and SIEM correlation rules) against the 36 core container TTP leaf nodes, security teams calculate empirical coverage metrics, eliminate visibility blindspots, and deploy redundant compensating controls.

---

### 1.2 Shared Responsibility & Sovereign Detection Boundary Matrix

Container infrastructure introduces distinct operational divisions between self-built environments (bare metal and private OpenShift) and managed cloud platforms (Amazon EKS, Azure AKS, Google Cloud GKE, IBM Cloud IKS/ROKS). Managed cloud platforms delegate physical facilities, hypervisors, and managed control plane nodes to the Cloud Service Provider (CSP). However, supervisory authorities hold financial institutions fully accountable for Monitoring Governance, Workload Integrity, and Evidentiary Proof.

The Sovereign Detection Brain principle dictates that financial institutions must retain intellectual ownership and runtime control over their threat detection logic. Relying exclusively on opaque proprietary cloud alerts creates strategic vendor dependency, impedes independent verification, and fails evidentiary standards during judicial audits. Detection logic must exist as auditable, version-controlled code independent of specific cloud vendor implementations.

The following matrix defines the technical and statutory division of responsibilities across eight architectural domains:

| Architectural Domain | Self-Built Environment (On-Premises / IaaS) | Managed Cloud Environment (EKS, AKS, GKE, IKS, ROKS) | Statutory & Evidentiary Requirement |
| :--- | :--- | :--- | :--- |
| **Physical & Hypervisor** | Institution assumes full hardware lifecycle, physical access control, and hypervisor maintenance. | CSP operates data centers, hardware isolation, and hypervisor patches. | Annual SOC 1 / SOC 2 Type II and ISO/IEC 27001 audit attestations required. |
| **Control Plane (API, etcd)** | Institution installs, patches, hardens, and monitors master API nodes, etcd clusters, and controllers. | CSP manages control plane availability and patching. Institution activates audit log exports. | CSMA Art. 16: Mandatory export of API audit trails to immutable enterprise SIEM. |
| **Worker Node OS & Kernel** | Institution maintains host OS patching, kernel sysctl parameters, and eBPF instrumentation. | CSP provides hardened machine images. Institution manages automated node updates and agents. | Enforcement of CIS Node Benchmarks; unprivileged user namespaces disabled. |
| **Container Runtime (CRI)** | Institution configures containerd/CRI-O sockets, storage drivers, and daemon audit logging. | CSP manages runtime engine binary. Institution audits runtime parameters via node profiles. | P0-02: Mandatory logging of container lifecycle hooks (`create`, `start`, `kill`, `exec`). |
| **Network & CNI** | Institution configures CNI plugins (Cilium, Calico), network firewalls, and load balancers. | Institution configures VPC subnets, security groups, CNI network policies, and Cloud WAF. | Default-deny NetworkPolicies per namespace; VPC Flow Logs enabled on subnets. |
| **Workload Admission & RBAC** | Institution deploys admission webhooks (OPA Gatekeeper, Kyverno) and role-based permissions. | Institution configures admission policies, cluster role bindings, and cloud IAM mappings. | Least privilege RBAC; zero cluster-admin bindings to microservice accounts. |
| **Detection Logic & DaC** | Institution authors, versions, tests, and deploys Sigma rules against local telemetry streams. | Institution compiles vendor-neutral Sigma rules to native cloud analytics engines. | Sovereign Detection Brain: Rules versioned in Git; zero blackbox dependencies. |
| **Forensic Traceability** | Institution executes memory dumps, disk image acquisitions, and local audit exports. | Institution captures cloud disk snapshots, container volume exports, and SIEM event streams. | CSMA Art. 18: SHA-256 evidence chain of custody; 1-year immutable retention. |

---

### 1.3 Detection Engineering Decoupling Model (DeTT&CT Framework)

Financial Security Operations Centers encounter operational friction when detection rules are hardcoded into proprietary query dialects like Splunk SPL, Microsoft Sentinel KQL, or IBM QRadar AQL. Direct dialect authoring locks institutions into specific monitoring vendors, impairs cross-cloud visibility, and obscures the relationship between detection rules and underlying threat techniques.

To resolve these limitations, this baseline enforces the DeTT&CT (Detect Tactics, Techniques & Combat Threats) Decoupled Detection Engineering Model. This architecture separates high-level defensive objectives from physical query execution across four formal abstraction tiers:

```
+---------------------------------------------------------------------------------------------------+
|                        DeTT&CT DECOUPLED DETECTION ENGINEERING HIERARCHY                          |
+---------------------------------------------------------------------------------------------------+
|  TIER 1: DETECTION STRATEGY (DS) -> High-level defensive intent mapped to MITRE ATT&CK techniques |
|  TIER 2: ANALYTIC (AN)           -> Vendor-neutral detection logic (Sigma YAML) of state invariants|
|  TIER 3: DATA COMPONENT (DC)     -> Standardized telemetry schema mappings (e.g. DC0028, DC0032)  |
|  TIER 4: LOG SOURCE (LS)         -> Concrete physical log feeds (K8s Audit Events, CRI, Syslog)    |
+---------------------------------------------------------------------------------------------------+
```

The functional definitions of the four tiers are structured as follows:

1. Detection Strategy (DS): Defines the defensive objective addressing a specific threat vector. Each Strategy maps to one or more MITRE ATT&CK leaf techniques (such as T1611 Escape to Host or T1552.001 Credentials in Files), specifying theoretical detection boundaries without referencing physical fields.
2. Analytic (AN): Formulates behavioral detection logic using declarative Sigma YAML specifications. The Analytic defines exact matching criteria, condition operators, and statistical thresholds independent of target SIEM syntax, enabling one-to-many compilation across multi-cloud targets.
3. Data Component (DC): Defines standardized telemetry semantics required by the Analytic, bridging abstract detection logic with physical schema fields (`DC0028: Kubernetes API Request`, `DC0032: Process Execution Syscall`, `DC0082: Network Socket Flow`).
4. Log Source (LS): Represents the physical telemetry stream, including Linux kernel tracepoints, Kubernetes API server audit logs, containerd CRI logs, AWS CloudTrail records, and Azure Activity Logs. CI/CD pipelines map generic Data Component fields to concrete Log Source columns during deployment.

The table below demonstrates the complete four-tier mapping pipeline for critical container threat techniques across multi-cloud environments:

| MITRE TTP ID | Threat Technique Name | Detection Strategy (DS) | Analytic (AN) ID | Required Data Component (DC) | Target Log Source (LS) Across Platforms |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **T1611** | Escape to Host | DS0017: Container Runtime Isolation | AN0612: Privileged Mount Detection | DC0028: K8s API Request<br>DC0032: eBPF Syscall | EKS / AKS / GKE Audit, Falco Kernel Events |
| **T1059.004** | Interactive Shell in Pod | DS0028: Workload Process Monitoring | AN0177: Unauthorized Exec Invocations | DC0028: K8s API Subresource<br>DC0072: CRI Event | K8s API Audit, containerd CRI, CloudWatch, Sentinel |
| **T1552.001** | Credentials in Files | DS0034: Workload Credential Guard | AN0859: Token Path Read Access | DC0032: File Access Syscall (`openat`) | eBPF Traces, GuardDuty, Defender, RHACS |
| **T1078.001** | Default Service Account Abuse | DS0019: Orchestrator Identity Guard | AN1279: Anonymous API Request | DC0028: K8s User Context | K8s Audit Sink, CloudTrail, GCP Cloud Logging |
| **T1496.001** | Compute Mining Hijacking | DS0022: Workload Resource Anomaly | AN1492: Stratum Protocol Connection | DC0082: Network Flow Data<br>DC0085: Cgroup CPU Metrics | VPC Flow Logs, Cilium Metrics, GuardDuty, Azure Flow |

---

### 1.4 Detection as Code (DaC) Principles & Sigma Rules Hierarchy

Detection as Code (DaC) applies software engineering disciplines to threat detection logic. Rather than manually configuring alerts inside graphical SIEM consoles, detection engineers manage detection rules as structured code artifacts within Git repositories. DaC enforces five mandatory engineering stages:

1. Version Control & Immutability: Every detection rule is stored in a centralized Git repository. Changes require peer review, linear history, and cryptographic commit signing, satisfying CSMA Article 16 requirements for verified change records.
2. Automated Syntax & Schema Linting: CI/CD validation pipelines run `sigma-cli` and `pySigma` linters to verify YAML syntax, mandatory metadata fields, and standardized data component definitions prior to merge.
3. Synthetic Adversary Testing: Automated pipelines deploy ephemeral test containers and inject synthetic attack techniques, verifying that rules trigger expected alerts without generating unintended false positives.
4. Multi-Dialect Continuous Compilation: Automated compiler jobs translate approved Sigma rules into native backend queries for target monitoring platforms (Microsoft Sentinel KQL, Splunk SPL, IBM QRadar AQL, and Google Chronicle YARA-L).
5. Automated Deployment & Drift Prevention: Deployment runners synchronize compiled rules to target SIEM and CWPP platforms via REST APIs. Out-of-band manual rule modifications are overwritten automatically during the next pipeline execution.

The Sigma specification hierarchy enforces a strict structure for container detection rules:

```yaml
title: Kubernetes Anonymous User Request Execution
id: 7a8b9c0d-1e2f-4a5b-8c9d-0e1f2a3b4c5d
status: stable
description: Detects API requests initiated with system:anonymous identity performing resource modifications.
author: Financial Cyber Defense Engineering Team
date: 2026-10-05
references:
  - https://attack.mitre.org/techniques/T1078/001/
  - CSMA-Article-16-Control-P0-01
tags:
  - attack.initial_access
  - attack.t1078.001
  - financial.csma.level_a
  - financial.mcb.p0
logsource:
  category: kubernetes
  product: kubernetes_audit
  service: audit_log
detection:
  selection:
    user.username: 'system:anonymous'
    verb:
      - 'create'
      - 'update'
      - 'patch'
      - 'delete'
  filter_probes:
    requestURI|startswith:
      - '/healthz'
      - '/livez'
      - '/readyz'
  condition: selection and not filter_probes
falsepositives:
  - Public readiness endpoints explicitly configured without authentication
level: high
```

The hierarchical blocks serve specific architectural functions:

- Metadata Block: Defines unambiguous identification attributes including canonical Title, persistent UUIDv4 ID, maturity Status (experimental, test, stable), and reference documentation.
- Taxonomy & Tagging Block: Anchors the rule to the MITRE ATT&CK taxonomy, CSMA Responsibility Level, and Financial MCB baseline tier (P0-P3).
- Log Source Block: Categorizes the required telemetry schema according to abstract Category, Product, and Service identifiers.
- Detection Logic Block: Specifies exact matching values and logical evaluation operators using boolean expressions (`selection and not filter`).
- Operational Governance Block: Documents verified false positive conditions and assigns an operational Severity Level (Low, Medium, High, Critical).

---

### 1.5 Six Detection Source Categories

Comprehensive container monitoring requires multiple telemetry sources across the application lifecycle. The Financial MCB classifies all detection mechanisms into six canonical categories:

- Category 1 (Native Log Custom Rules - Sigma): Custom vendor-neutral rules compiled to native query syntax, executing directly on raw Kubernetes API audit logs, container runtime events, and host syslog. Provides maximum transparency and sovereignty for on-premises clusters and core banking environments.
- Category 2 (CWPP Native Workload Alerts): Behavioral runtime detection engines (GuardDuty Runtime, Defender for Containers, Google SCC CTD, IBM SCC, RHACS) intercepting in-memory process execution and malicious system calls via eBPF probes.
- Category 3 (Managed Cloud Control Plane Audit Logic): Analytical queries on cloud management planes (CloudTrail, Azure Activity Logs, GCP Audit Logs) detecting cross-service IAM abuse, storage bucket modifications, and infrastructure tampering.
- Category 4 (Infrastructure Architectural Mitigations): Hardened configurations neutralizing threat vectors through architecture. Encompasses Absolute Exclusions (managed kernels eliminating host attack vectors, like AWS Fargate and GKE Autopilot) and Conditional Exclusions (perimeter controls, private API endpoints, WAF).
- Category 5 (Native Adjustable Security Policies): Declarative admission controllers and runtime policy engines (OPA Gatekeeper, Kyverno, Kubernetes PSA) inspecting manifests during API submission to reject non-compliant workloads before execution.
- Category 6 (Enterprise SIEM Unique Rules & Cross-Cluster Correlation): Centralized SOC correlation queries deployed in enterprise SIEM platforms (Microsoft Sentinel, Splunk ES, IBM QRadar) linking events across disparate clusters, network devices, and identity providers into coherent attack chains.

The table below details technical characteristics and operational parameters across the six detection categories:

| Category ID | Category Name | Underlying Telemetry Stream | Processing Engine & Location | Detection Latency | False Positive Rate | Primary Financial Use Case |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Category 1** | Native Log Custom Rules | K8s API Audit JSON, CRI, syslog | Central SIEM / Local Pipeline | 30 to 120 seconds | Low (Custom tuned) | Core ledger clusters, sovereign audit trails, regulatory forensics. |
| **Category 2** | CWPP Native Workload Alerts | eBPF kernel probes, process trees | Cloud-native agent / CSP SaaS | Real-time (< 5 seconds) | Low to Medium | Runtime breakout blocking, zero-day exploit discovery, cryptomining alerts. |
| **Category 3** | Managed Cloud Control Plane | CloudTrail, Activity Logs, Admin Logs | Cloud SIEM / Serverless processor | 1 to 5 minutes | Low | Cloud IAM role assumption, unauthorized cluster updates, bucket policy shifts. |
| **Category 4** | Infrastructure Mitigations | Virtualization hypervisors, VPC rules | Cloud infrastructure fabric | Preventative (0 seconds) | Zero (Deterministic) | Serverless workloads, network perimeter isolation, private API bastions. |
| **Category 5** | Native Adjustable Policies | Dynamic admission webhook requests | In-cluster API admission webhooks | Preventative (< 100 ms) | Zero (Deterministic) | CI/CD build gates, blocking privileged pods, enforcing non-root execution. |
| **Category 6** | Enterprise SIEM Correlation | Aggregated multi-cloud telemetry feeds | Enterprise SOC correlation engine | 2 to 10 minutes | Medium (Requires tuning) | Multi-stage lateral movement detection, cross-cluster correlation, data exfiltration. |

---

### 1.6 Multi-Tier Telemetry Taxonomy Matrix

Accurate threat detection across containerized environments requires full visibility into multiple infrastructure layers. The Financial MCB defines a four-tier telemetry taxonomy covering Orchestration, Engine and Runtime, Host and Kernel, and Network layers:

```
+---------------------------------------------------------------------------------------------------+
|                            MULTI-TIER CONTAINER TELEMETRY TAXONOMY                                |
+---------------------------------------------------------------------------------------------------+
|  1. ORCHESTRATION LAYER: K8s API Audit Events, Admission Webhooks, Controller Logs, etcd State     |
|  2. ENGINE & RUNTIME LAYER: containerd / CRI-O Sockets, Image Registry Events, Container Hooks   |
|  3. HOST & KERNEL LAYER: eBPF System Call Tracepoints, Auditd, PAM Authentication, Process Trees  |
|  4. NETWORK & CNI LAYER: CNI Flow Telemetry, VPC Flow Logs, CoreDNS Resolution Logs, Mesh Traces  |
+---------------------------------------------------------------------------------------------------+
```

The table below documents telemetry attributes, collection protocols, retention periods, and forensic applications for each tier:

| Telemetry Tier | Core Telemetry Events | Mandatory Capture Attributes | Ingestion Protocol | Statutory Retention | Regulatory & Forensic Value |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Orchestration** | `Pod`, `ServiceAccount`, `RoleBinding`, `Secret`, `ConfigMap` | Request URI, HTTP Verb, Client IP, User Agent, RBAC Subject Identity, HTTP Status Code | Webhook JSON / Syslog TLS | Minimum 1 Year (CSMA Art. 16) | Detecting unauthorized RBAC privilege escalation, anonymous access attempts, and cluster reconnaissance. |
| **2. Engine & Runtime** | `ContainerCreate`, `ContainerStart`, `ContainerKill`, `Exec` | Container ID, Pod Name, Namespace, Image Digest SHA-256, Mounted Volumes, Linux Capabilities list | CRI gRPC Socket / Fluent-Bit | Minimum 1 Year (CSMA Art. 16) | Proving container provenance, verifying image integrity, and auditing interactive shell execution. |
| **3. Host & Kernel** | `execve`, `setns`, `ptrace`, `openat`, `socket`, `clone` | Host PID, Container PID, PPID, Real UID, Effective GID, Binary Path, Command Arguments, Exit Code | eBPF Kernel Probe / Ring Buffer | Minimum 1 Year (CSMA Art. 16) | Intercepting kernel privilege escalation, container breakout attempts, and direct memory tampering. |
| **4. Network & CNI** | IP packet flows, TCP session flags, DNS lookups, TLS metadata | Source IP/Port, Destination IP/Port, Protocol, Packet/Byte Count, DNS Domain Query, TLS SNI | NetFlow / IPFIX / VPC Flow | Minimum 1 Year (CSMA Art. 16) | Uncovering command-and-control communication, unauthorized internal port scans, and data exfiltration. |

---

### 1.7 Continuous Posture Management (CSPM) & Eight Quantitative Metrics

Traditional periodic checklists fail to secure container workloads subject to frequent microservice deployments, autoscaling events, and dynamic configuration updates. Cloud Security Posture Management (CSPM) transforms static CIS Kubernetes Benchmarks into continuous automated evaluations. Rather than performing periodic audits, CSPM engines continuously poll cluster API endpoints and node configurations, detecting compliance drift in real time and triggering automated remediation workflows.

Financial institutions must track and report container security operations using eight quantitative metrics divided into Key Performance Indicators (KPI), Key Risk Indicators (KRI), and Key Control Indicators (KCI):

| Metric Category | Metric ID | Metric Name & Calculation Formula | Data Sources | Target Threshold | Monitoring Cadence | Mandatory Escalation Action |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **KPI** | **KPI-SEC-01** | **Container Audit Log Ingestion Reliability**<br>`(Active Streaming Nodes / Total Nodes) * 100` | SIEM Ingestion Monitors, Daemonset Telemetry | **>= 99.95%** | Continuous Real-Time | Dispatch SecOps PagerDuty alert; restart log daemonset within 15 minutes. |
| **KPI** | **KPI-SEC-02** | **Mean Time to Remediate High/Critical CVEs (MTTR)**<br>`Sum(Hours from Scan to Production Fix) / Total CVEs` | Scanner API, Harbor/ECR, CI/CD Pipeline | **<= 24 Hours** | Weekly Rolling Average | Block deployment pipeline for non-compliant microservices; report to CISO. |
| **KPI** | **KPI-SEC-03** | **Admission Control Enforcement Coverage**<br>`(Guarded Namespaces / Total Namespaces) * 100` | OPA Gatekeeper, Kyverno, K8s API Metrics | **100% (Absolute)** | Continuous Real-Time | Automated admission policy reinjection; alert on unmanaged namespaces. |
| **KPI** | **KPI-SEC-04** | **Detection Rule Automated Validation Pass Rate**<br>`(Passing Test Scenarios / Total Test Scenarios) * 100` | GitOps CI/CD Test Suite, Synthetic Simulators | **100% (Absolute)** | Per Git Commit / Merge | Block pull request merge; halt DaC compilation pipeline until tests succeed. |
| **KRI** | **KRI-SEC-01** | **Unauthenticated / Anonymous API Requests**<br>`Count of Requests where user.username='system:anonymous'` | K8s API Server Audit Log Sink | **0 (Zero Tolerance)** | Continuous Real-Time | Declare P1 Incident under CSMA Art. 18; isolate client source IP. |
| **KRI** | **KRI-SEC-02** | **Privileged Container Launch Attempts**<br>`Count of Pod Submissions with privileged=true or CAP_SYS_ADMIN` | K8s Admission Logs, Audit Events | **0 (Zero Tolerance)** | Immediate Per Event | Terminate pod immediately; revoke ServiceAccount credentials; notify SOC. |
| **KRI** | **KRI-SEC-03** | **Sensitive HostPath Mount Violations**<br>`Count of Manifests mounting /, /etc, /proc, or docker.sock` | K8s Admission Logs, Audit Events | **0 (Zero Tolerance)** | Immediate Per Event | Reject deployment manifest; quarantine deployment credentials; conduct audit. |
| **KCI** | **KCI-SEC-01** | **CIS Kubernetes Benchmark Compliance Score**<br>`(Passed Benchmark Rules / Total Benchmark Rules) * 100` | CSPM Engine (Security Hub, Defender, SCC, RHACS) | **>= 95.0%** | Daily Automated Scan | Submit drift remediation tickets; review gaps in weekly risk committee. |

---

## 2. Production Incident & Remediation Architecture

### 2.1 Production Incident Scenario: Payment Gateway Breakout

In a production core banking environment, an external attacker targeted an internet-facing payment processing gateway deployed within a multi-tenant Kubernetes cluster. The incident unfolded through five distinct tactical attack stages:

```
+---------------------------------------------------------------------------------------------------+
|                                PRODUCTION INTRUSION TIMELINE & KILL CHAIN                         |
+---------------------------------------------------------------------------------------------------+
|  1. Initial Access: Exploitation of unpatched CVE-2024-38472 in payment gateway pod (T1190)       |
|  2. Execution: Interactive shell spawned (/bin/sh); malicious cron persistence created (T1059)   |
|  3. Credential Harvesting: Extraction of ServiceAccount token and Kubelet API discovery (T1552)  |
|  4. Container Breakout: Host filesystem escape via mounted /var/run/docker.sock socket (T1611)    |
|  5. Impact & Lateral Movement: Host network packet sniffer installed; external C2 beacon (T1040) |
+---------------------------------------------------------------------------------------------------+
```

Chronological Execution Breakdown:

1. Initial Access (T1190 Exploit Public-Facing Application): The attacker targeted an unpatched payment gateway container running Apache HTTP Server vulnerable to remote command execution (CVE-2024-38472). Transmitting a crafted HTTP request with encoded newline characters bypassed the front-end WAF and executed arbitrary commands in the container.
2. Execution & Persistence (T1059.004 Unix Shell & T1053.007 Container Cronjob): The exploit executed `/bin/sh`, spawning a reverse TCP shell to external attacker infrastructure. To maintain persistence, the attacker added an entry to `/etc/cron.d/sync-check` to re-execute the reverse connection every five minutes.
3. Credential Harvesting & Discovery (T1552.001 Credentials in Files & T1613 Container Discovery): The attacker accessed the default token at `/var/run/secrets/kubernetes.io/serviceaccount/token`. Using `curl`, the attacker queried the internal API server (`https://kubernetes.default.svc`), discovering that the token possessed cluster-wide `pods:list` and `secrets:get` permissions.
4. Container Breakout (T1611 Escape to Host): The manifest mounted `/var/run/docker.sock`. The attacker downloaded a static `docker` binary, communicating directly with the host daemon to launch a privileged container mounting the host root filesystem at `/host`. Executing `chroot /host` granted root control over the worker node.
5. Impact & Network Egress (T1040 Network Sniffing & T1133 External Remote Services): Operating as host root, the attacker installed `tcpdump` to capture inter-service traffic between adjacent banking pods, batching and transmitting captured data to an external C2 server over HTTPS.

Root Cause Architecture Failures:

- Failure 1: Permissive Workload Admission. Admission webhooks permitted deployment manifests mounting host socket `/var/run/docker.sock` and running with root user UID 0.
- Failure 2: Missing System Call Filtering. Worker nodes ran without Seccomp or AppArmor profiles, allowing arbitrary `execve` and `chroot` system calls.
- Failure 3: Default ServiceAccount Privilege Sprawl. The pod mounted the default ServiceAccount token without operational need, and the token held administrative RBAC bindings.
- Failure 4: Telemetry Pipeline Lag. Node-level audit logs buffered locally rather than streaming continuously over mTLS, delaying detection by four hours and breaching the CSMA Article 18 window.

---

### 2.2 Hardened Defense-in-Depth Remediation Architecture

To remediate the vulnerabilities and prevent recurrence, the financial institution deployed an end-to-end hardened production architecture incorporating five defensive layers:

```
+---------------------------------------------------------------------------------------------------+
|                        HARDENED FINANCIAL PRODUCTION REMEDIATION ARCHITECTURE                     |
+---------------------------------------------------------------------------------------------------+
|  [ LAYER 1: CI/CD BUILD GATE ]      -> Trivy CVE Scan + Cosign Signature + SBOM Attestation       |
|  [ LAYER 2: ADMISSION CONTROL ]     -> OPA Gatekeeper: Enforce Non-Root + Deny HostPath / Sockets  |
|  [ LAYER 3: RUNTIME CWPP & eBPF ]   -> Falco Kernel Probe: Intercept execve / Block Shell Spawns   |
|  [ LAYER 4: TELEMETRY & AUDIT SINK] -> Fluent-Bit mTLS Forwarder -> 1-Year WORM Storage Bucket    |
|  [ LAYER 5: AUTOMATED SOAR DAG ]    -> Real-Time Pod Quarantine + Node Cordon + Token Revocation   |
+---------------------------------------------------------------------------------------------------+
```

The five hardened layers enforce technical protections across the workload lifecycle:

1. Layer 1 (CI/CD Supply Chain Security): All container images undergo static vulnerability scanning during build. Builds containing Critical or High CVEs fail automatically. Images receive cryptographic Cosign signatures backed by hardware security modules, creating verifiable Software Bill of Materials (SBOM) attestations.
2. Layer 2 (Preventative Admission Control): OPA Gatekeeper admission webhooks enforce the Pod Security Standards Restricted profile across production namespaces. Workload submissions mounting `/var/run/docker.sock`, requesting `privileged: true`, or running as UID 0 are rejected at the API server boundary.
3. Layer 3 (Runtime eBPF Behavioral Shielding): Falco and cloud CWPP daemonsets monitor Linux kernel system calls. Kernel probes intercept `execve()` invocations spawning `/bin/sh` or `/bin/bash` inside microservice containers, terminating offending processes immediately.
4. Layer 4 (Continuous Telemetry Ingestion): Fluent-Bit forwarders stream Kubernetes audit logs, runtime events, and network flow records over mutual TLS to an immutable Write-Once-Read-Many (WORM) cloud storage bucket and central SIEM, meeting CSMA Article 16 log retention mandates.
5. Layer 5 (Automated Incident Response Orchestration): SOAR playbooks execute automated containment upon receiving confirmed breakout alerts: applying zero-trust quarantine NetworkPolicies, cordoning the affected worker node, and invalidating compromised ServiceAccount tokens within 60 seconds.

Declarative Production Policy Specifications:

```yaml
# OPA Gatekeeper Constraint: Enforce Secure Container Baseline
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sPSPContainerSecurity
metadata:
  name: financial-production-containment
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
    namespaces: ["payment-production", "core-banking"]
  parameters:
    runAsNonRoot: true
    allowPrivilegeEscalation: false
    readOnlyRootFilesystem: true
    disallowedHostPaths:
      - pathPrefix: "/var/run"
      - pathPrefix: "/etc"
      - pathPrefix: "/proc"
      - pathPrefix: "/sys"
      - pathPrefix: "/"
```

```yaml
# Falco Runtime Behavioral Rule: Intercept Interactive Shell Spawns in Microservices
- rule: Unauthorized Shell Spawned in Financial Workload
  desc: Detects interactive shell execution inside production payment containers
  condition: >
    spawned_process and
    container and
    container.name in (payment-gateway, transaction-engine) and
    proc.name in (bash, sh, zsh, ksh, csh)
  output: >
    CRITICAL: Shell spawn detected inside container
    (user=%user.name pod=%k8s.pod.name ns=%k8s.ns.name binary=%proc.name cmdline=%proc.cmdline host_pid=%proc.pid)
  priority: CRITICAL
  tags: [financial_mcb, runtime_threat, mitre_t1059_004, csma_art_18]
```

---

## 3. Exam Question Bank & Distractor Forensics

### Question 1: Operational Sequence (FIRST Action)
During a midnight monitoring shift, a financial SOC analyst receives a Category 1 Sigma alert indicating an unauthorized `kubectl exec` session initiated with `/bin/bash` into a payment processing container running inside a production namespace (T1059.004). Telemetry shows the session accessed `/var/run/secrets/kubernetes.io/serviceaccount/token`. In accordance with CSMA Article 18 containment protocols, what is the FIRST operational action the analyst must execute?

- A. Power off the physical worker node host server immediately using out-of-band management.
- B. Apply a quarantine NetworkPolicy restricting all pod ingress and egress traffic, cordon the worker node, and preserve in-memory forensic state before terminating the container.
- C. Update the Helm chart deployment repository in Git and trigger a production redeployment pipeline.
- D. Submit an emergency change request ticket to schedule a maintenance window review during the next business morning.

#### Distractor Forensics:
- Option A is Flawed: Powering off the host destroys volatile RAM memory artifacts, wipes active network socket connections, prevents root cause analysis, and causes severe service disruption to benign workloads sharing the node.
- Option B is the Correct Answer: The initial priority under CSMA Article 18 is immediate network containment. Isolating the compromised pod via a default-deny NetworkPolicy terminates active C2 channels and halts lateral movement while preserving ephemeral container memory and filesystem artifacts required for forensic analysis. Cordoning the node prevents the orchestrator from scheduling new workloads onto the suspect host.
- Option C is Flawed: Triggering a CI/CD redeployment does not terminate the active interactive shell session running inside the live container, allowing the attacker to continue extracting banking credentials during the rollout.
- Option D is Flawed: Deferring active intrusion containment to a morning change review ticket violates statutory incident response timelines and breaches the CSMA Article 18 one-hour reporting requirement for severe security events.

---

### Question 2: Architectural Strategy (BEST/MOST Implementation)
A tier-1 commercial bank operates a hybrid multi-cloud architecture comprising AWS EKS for customer banking, Azure AKS for risk analytics, and on-premises Red Hat OpenShift for ledger settlement. The bank must establish a unified threat detection engineering framework ensuring consistent behavioral coverage across all platforms without maintaining separate, proprietary query rulebases for each target SIEM. Which architecture represents the BEST and MOST effective technical implementation?

- A. Write all detection rules exclusively in Splunk SPL and require all cloud providers to forward unparsed syslog streams to a single on-premises indexer cluster.
- B. Deploy Detection as Code (DaC) using vendor-neutral Sigma rules mapped to standardized Data Components (DCs), compiling detection logic to native SIEM formats via automated GitOps CI/CD pipelines.
- C. Rely exclusively on AWS GuardDuty Runtime Monitoring and disable audit logging on OpenShift and AKS to minimize telemetry storage expenditures.
- D. Migrate all microservice container applications back to monolithic mainframe virtual machines to avoid distributed container telemetry complexity.

#### Distractor Forensics:
- Option A is Flawed: Directly authoring detection logic in proprietary SPL causes vendor lock-in, increases maintenance overhead across heterogeneous cloud platforms, and breaks the abstract separation between detection strategy and underlying log schema.
- Option B is the Correct Answer: Implementing Detection as Code with Sigma rules and the DeTT&CT decoupling model establishes detection sovereignty. The bank defines vendor-neutral detection logic once and compiles it automatically to Microsoft Sentinel KQL, Splunk SPL, or OpenShift analytics engines via CI/CD pipelines, ensuring standardized coverage and GitOps auditability across hybrid clouds.
- Option C is Flawed: AWS GuardDuty cannot inspect Azure AKS or on-premises OpenShift clusters. Disabling audit log collection on those platforms directly violates CSMA Article 16 and P0 foundational telemetry retention mandates.
- Option D is Flawed: Regressing modern financial applications to monolithic virtual machines abandons microservice agility and fails to solve fundamental threat monitoring requirements.

---

### Question 3: Remediation Workflow (NEXT Step)
An automated CSPM compliance assessment reports that five production namespaces in an EKS cluster exhibit a CIS Kubernetes Benchmark Compliance Score of 62%, caused by running containers with `allowPrivilegeEscalation: true` and missing network microsegmentation policies. The security engineering team has merged the corrected configurations into the application Helm charts in Git. What is the NEXT technical step the engineering team must execute to enforce compliance?

- A. Postpone remediation actions until the annual external supervisory audit documentation cycle.
- B. Deploy an admission controller (OPA Gatekeeper or Kyverno) in enforce mode to block non-compliant pod creation at the API server gate and initiate a rolling restart of target workloads.
- C. Grant temporary cluster-admin permissions to microservice developers to manually edit running pod manifests using kubectl patch.
- D. Suppress the CSPM scanner alert notifications to eliminate ticket volume.

#### Distractor Forensics:
- Option A is Flawed: Deferring configuration remediation to annual audits permits active vulnerabilities to persist indefinitely in production clusters, violating continuous compliance requirements.
- Option B is the Correct Answer: Merging Helm charts fixes future repository manifests, but running workloads remain vulnerable until recreated. Enforcing admission controller policies establishes preventative gating at the API boundary, while executing a rolling restart applies the compliant configurations to live pods without service downtime.
- Option C is Flawed: Granting cluster-admin access to application developers violates the principle of least privilege, introduces severe operational risk, and fails to fix the root cause configuration in GitOps repositories.
- Option D is Flawed: Disabling scanner notifications conceals compliance failures without remediating underlying security risks, creating non-compliance liability under CSMA Article 17.

---

### Question 4: Governance & Responsibility (PRIMARY/EXCEPT Concept)
Under the Financial Container Security Monitoring Baseline and the CSMA, financial institutions hosting containerized banking applications on managed cloud container services (such as AWS EKS, Azure AKS, or Google Cloud GKE) retain statutory accountability for all of the following monitoring and technical controls, EXCEPT:

- A. Collecting and streaming raw Kubernetes control plane API audit logs to an enterprise immutable SIEM sink for at least one year.
- B. Applying operating system security patches directly to the physical hardware hypervisors operated by the cloud service provider.
- C. Defining, versioning, and deploying workload admission control constraints and namespace role-based access control policies.
- D. Investigating CWPP runtime workload behavioral detections and anomaly alerts affecting production pods.

#### Distractor Forensics:
- Option A is a Statutory Requirement: CSMA Article 16 and the P0 baseline mandate that financial institutions retain raw control plane audit trails in immutable storage for digital forensic readiness regardless of cloud deployment model.
- Option B is the EXCEPTION (Correct Answer): In managed cloud architectures, physical data center facilities, server hardware, and virtualization hypervisors reside exclusively within the Cloud Service Provider operational domain under the shared responsibility model. Financial institutions possess neither physical access nor legal authorization to patch CSP hypervisors.
- Option C is a Statutory Requirement: Institutions maintain full ownership of tenant-level access control, RBAC bindings, and admission policies governing application workloads.
- Option D is a Statutory Requirement: Monitoring and responding to runtime workload anomalies within application containers remains an essential operational responsibility of the financial institution.

---

### Question 5: Telemetry & Forensics (EVALUATION / COMPLIANCE)
During an annual CSMA Article 17 supervisory audit, authorities discover that a financial institution's Kubernetes cluster experienced an audit log forwarder daemonset failure. For forty-five consecutive days, the cluster generated zero API server audit events and zero eBPF syscall records in the central immutable SIEM. Which quantitative metric failed during this incident, and what statutory compliance violation occurred?

- A. KPI-SEC-01 (Container Audit Log Ingestion Reliability) dropped below 99.95%, violating the CSMA Article 16 mandatory one-year audit trail retention requirement.
- B. KCI-SEC-01 (CIS Benchmark Compliance Score) dropped below 50.0%, violating local zoning laws.
- C. KPI-SEC-02 (MTTR for CVEs) exceeded 24 hours, violating container image licensing agreements.
- D. KRI-SEC-03 (HostPath Volume Violations) reached zero, violating physical perimeter access standards.

#### Distractor Forensics:
- Option A is the Correct Answer: KPI-SEC-01 measures the percentage of cluster nodes actively streaming uninterrupted telemetry to the central SIEM (target threshold >= 99.95%). A 45-day complete loss of log streaming represents a critical ingestion failure that creates an evidentiary void and directly breaches CSMA Article 16 obligations requiring unbroken, immutable log retention for forensic traceability.
- Option B is Flawed: KCI-SEC-01 measures CIS benchmark configuration posture, not log streaming reliability; zoning laws do not govern container cybersecurity.
- Option C is Flawed: KPI-SEC-02 measures image vulnerability remediation times, which does not relate to runtime audit log ingestion failures.
- Option D is Flawed: KRI-SEC-03 measures prohibited hostPath mounts where a score of zero is the desired compliant outcome, not a failure condition.
