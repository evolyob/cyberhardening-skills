# Chapter 01: General Framework, Detection as Code & Telemetry Taxonomy

## 1. Statutory Baseline & Technical Control Matrix

### 1.1 Executive Mandate & Regulatory Foundation

The Financial Container Security Monitoring & Configuration Baseline (MCB for Containers) establishes the technical specification for financial institutions operating containerized architectures across private, hybrid, and multi-cloud environments. Modern microservice deployments alter traditional perimeter security models by introducing ephemeral workload lifecycles, high-density multi-tenancy, declarative orchestration APIs, and abstracted virtual networks. Traditional annual static checklists and host-based perimeter defenses fail to capture runtime anomalies, in-memory process injections, and rapid configuration drift occurring within container clusters.

To satisfy statutory requirements imposed by financial supervisory authorities (mandating continuous auditability, non-repudiation of administrative actions, digital forensics readiness, and strict change control), financial institutions must implement an integrated defense-in-depth model synthesizing two complementary paradigms:

1. **Preventative Configuration Baselines (CIS Benchmarks)**: Enforce defensive guardrails across container runtimes, node operating systems, orchestration control planes, and cloud compute environments before workloads transition to production.
2. **Behavioral Runtime Detection (MITRE ATT&CK for Containers v19)**: Deploy telemetry monitoring and anomaly detection to identify, intercept, and trace adversary tactics, techniques, and procedures (TTPs) targeting running containers and control plane components.

```
+---------------------------------------------------------------------------------------------------+
|                         FINANCIAL CONTAINER DEFENSE IN DEPTH (DeTT&CT ALIGNED)                    |
+---------------------------------------------------------------------------------------------------+
|  PREVENTATIVE CONTROLS (CIS Benchmarks)           |  DETECTIVE & FORENSIC CONTROLS (MITRE ATT&CK) |
|  - Immutable Host & Node Hardening                |  - Control Plane API Auditing                 |
|  - Pod Security Admission Constraints             |  - High-Fidelity eBPF System Call Tracing     |
|  - Principle of Least Privilege (RBAC / IAM)      |  - Runtime Anomaly & Behavioral Detection     |
|  - Encrypted Secrets & Transport Security         |  - Detection as Code (DaC) Sigma Pipeline     |
+---------------------------------------------------------------------------------------------------+
```

Financial institutions must apply the **DeTT&CT (Detect Tactics, Techniques & Combat Threats)** framework to systematically measure defense posture. By mapping enterprise defensive capabilities (CWPP platforms, admission controllers, and SIEM correlation rules) against the 36 core container TTP leaf nodes, security teams calculate empirical coverage metrics, eliminate visibility blindspots, and engineer redundant compensating controls.

---

### 1.2 Shared Responsibility & Sovereign Detection Boundary Matrix

Container security operational responsibilities shift dynamically based on whether the architecture is deployed on-premises (self-built bare metal or virtualized Kubernetes) or hosted through managed cloud service providers (AWS EKS/ECS, Azure AKS, Google Cloud GKE, IBM Cloud IKS/ROKS, Red Hat OpenShift OCP).

In managed environments, cloud service providers manage the physical hardware, hypervisor, and underlying control plane infrastructure. However, financial institutions maintain strict statutory accountability for **Monitoring Governance** and **Evidentiary Integrity**. While managed providers expose high-level workload alerts, regulatory compliance mandates that financial institutions collect, ingest, and retain raw control plane audit trails, container runtime telemetry, and host access logs in centralized, immutable storage for a minimum statutory retention period of one year.

The concept of the **Sovereign Detection Brain** dictates that financial institutions must retain complete ownership and interpretive authority over their threat detection logic. Relying exclusively on proprietary vendor detection algorithms creates vendor lock-in and leaves organizations unable to defend the provenance, precision, and evidentiary basis of security findings during judicial or regulatory inquiries.

The following matrix delineates operational and evidentiary boundaries across deployment models:

| Architectural Domain | Self-Built Environment (On-Premises / IaaS) | Managed Cloud Environment (EKS, AKS, GKE, IKS, OCP) | Regulatory Compliance & Evidentiary Standard |
| :--- | :--- | :--- | :--- |
| **Physical & Hypervisor** | Institution assumes 100% operational, hardware, and physical security control. | Cloud Service Provider (CSP) manages physical facilities, hypervisors, and data centers. | SOC 1 / SOC 2 Type II, ISO/IEC 27001 third-party audit attestations required. |
| **Control Plane (API, etcd)** | Institution deploys, patches, hardens, and monitors master nodes, etcd clusters, and schedulers. | CSP manages control plane uptime, patching, and availability. Institution manages API flags and log export toggles. | Mandatory export of raw API server and controller audit logs to central immutable SIEM. |
| **Worker Node OS & Kernel** | Institution maintains OS lifecycle, CIS kernel hardening, security patching, and eBPF instrumentation. | CSP provides hardened Node OS images; Institution configures automated node group updates and host agents. | Kernel parameter enforcement (`sysctl` hardening, disabled user namespaces, CIS compliance). |
| **Container Runtime (CRI)** | Institution configures containerd/CRI-O, enforces secure storage drivers, and collects runtime socket logs. | CSP manages runtime engine; Institution validates runtime configuration via cluster profiles and startup scripts. | Audit logging of container lifecycle events (`create`, `start`, `kill`, `exec`, `attach`). |
| **Network & Ingress/Egress** | Institution engineers CNI plugins (Calico, Cilium), hardware load balancers, and perimeter firewalls. | Institution configures VPC subnets, cloud security groups, CNI network policies, and Cloud WAF endpoints. | Default-deny NetworkPolicies per namespace; VPC Flow Logs enabled across all container subnets. |
| **Workload Admission & RBAC** | Institution implements custom admission webhooks (OPA Gatekeeper, Kyverno) and role-based access controls. | Institution implements admission policies, validates cluster role bindings, and maps cloud IAM to ServiceAccounts. | Zero cluster-admin privilege delegation; denial of root containers and host volume mounts. |
| **Detection Logic & DaC** | Institution authors, versions, tests, and deploys Sigma rules against raw local telemetry streams. | Institution ingests vendor CWPP alerts while deploying vendor-neutral Sigma rules against exported audit streams. | **Detection Sovereignty**: Detection logic version-controlled in Git; zero blackbox dependencies for core banking audits. |
| **Forensic Traceability** | Institution maintains direct forensic access to node memory dumps, raw filesystem snapshots, and local logs. | Institution captures cloud disk snapshots, container volume exports, and centralized raw telemetry feeds. | Chain of custody preservation; cryptographic hashing of forensic log exports. |

---

### 1.3 Detection Engineering Decoupling Model (MITRE Framework)

Traditional financial Security Operations Centers (SOCs) encounter operational bottlenecks when monitoring containerized workloads due to proprietary rule lock-in, alert ambiguity, and fragile query syntax tied directly to specific SIEM implementations. When detection rules are authored exclusively in proprietary dialects (such as Splunk SPL, Microsoft Sentinel KQL, or IBM QRadar AQL), migrating monitoring infrastructure or integrating hybrid cloud platforms causes loss of intellectual capital and breaks defense coverage.

To overcome these structural limitations, this baseline implements the **MITRE Detection Engineering Decoupling Architecture**. This model establishes four distinct abstraction tiers, severing the dependency between tactical detection intent and backend query execution:

```
+-----------------------------------------------------------------------------------------------+
|                        MITRE DECOUPLED DETECTION ENGINEERING ARCHITECTURE                     |
+-----------------------------------------------------------------------------------------------+
|  TIER 1: DETECTION STRATEGY (DS)                                                             |
|  High-level defensive intent mapped to MITRE ATT&CK leaf techniques (e.g. DS0017 Container)   |
+-----------------------------------------------------------------------------------------------+
                                                |
                                                v
+-----------------------------------------------------------------------------------------------+
|  TIER 2: ANALYTIC (AN)                                                                        |
|  Abstract, vendor-neutral detection logic (Sigma YAML) capturing behavioral invariant state    |
+-----------------------------------------------------------------------------------------------+
                                                |
                                                v
+-----------------------------------------------------------------------------------------------+
|  TIER 3: DATA COMPONENT (DC)                                                                  |
|  Standardized telemetry field mappings (e.g. process_creation, container_network_connection)    |
+-----------------------------------------------------------------------------------------------+
                                                |
                                                v
+-----------------------------------------------------------------------------------------------+
|  TIER 4: LOG SOURCE (LS)                                                                      |
|  Physical raw logs (K8s API Audit, eBPF tracepoints, GuardDuty Finding, Defender Event)        |
+-----------------------------------------------------------------------------------------------+
```

---

### 1.4 Detection as Code (DaC) Principles & Six Detection Source Categories

Financial institutions must manage detection logic using **Detection as Code (DaC)** disciplines identical to modern software development lifecycles (GitOps, CI/CD validation, automated linting, regression testing, and declarative deployment).

The baseline classifies all container monitoring sources into **Six Canonical Detection Categories**:

| Category ID | Category Name | Scope & Technical Implementation | Primary Deployment Target |
| :--- | :--- | :--- | :--- |
| **Category 1** | **Native Log Custom Rules (Sigma)** | Vendor-neutral Sigma rules executed against raw K8s API audit logs, container runtime logs, and Linux system telemetry. | Self-built clusters, high-risk banking cores, regulatory forensic pipelines. |
| **Category 2** | **CWPP Native Workload Alerts** | Real-time behavioral findings generated by cloud-native security agents (GuardDuty, Defender, SCC, RHACS). | Managed EKS, AKS, GKE, ROKS, OCP clusters. |
| **Category 3** | **Managed Log Analysis Logic** | Custom queries (KQL, SPL, YARA-L) executed against cloud provider telemetry exports (CloudTrail, Log Analytics). | Hybrid and multi-cloud SIEM aggregation sinks. |
| **Category 4** | **Infrastructure Environmental Mitigations** | Security boundaries provided inherently by managed cloud infrastructure (Fargate isolation, managed IMDSv2). | Serverless containers, managed worker node pools. |
| **Category 5** | **Native Adjustable Security Policies** | Declarative admission controller constraints (OPA Gatekeeper, Kyverno, RHACS Security Policies). | Automated deployment pipelines, CI/CD gates. |
| **Category 6** | **SIEM Unique Rules & Default Monitoring** | Pre-built vendor correlation rules and threat intelligence feeds native to centralized SIEM platforms. | Central enterprise SOC, cross-cluster correlation engines. |

---

### 1.5 Multi-Tier Telemetry Taxonomy Matrix

Telemetry collection in container environments spans four architectural layers:

```
+---------------------------------------------------------------------------------------------------+
|                            MULTI-TIER CONTAINER TELEMETRY TAXONOMY                                |
+---------------------------------------------------------------------------------------------------+
|  1. ORCHESTRATION LAYER (K8s API Audit, Admission Webhooks, Controller Logs, etcd Events)        |
|  2. ENGINE & RUNTIME LAYER (containerd / CRI-O Sockets, CNI Events, Image Pull/Push Logs)         |
|  3. HOST & SYSTEM BEHAVIORAL LAYER (eBPF Kernel Syscalls, SSH, PAM, Linux Auditd, Process Trees) |
|  4. NETWORK & CNI TELEMETRY LAYER (VPC Flow Logs, DNS Query Logs, Cilium eBPF Network Metrics)    |
+---------------------------------------------------------------------------------------------------+
```

| Telemetry Tier | Core Telemetry Events | Mandatory Capture Attributes | Regulatory & Forensic Value |
| :--- | :--- | :--- | :--- |
| **Orchestration** | `Pod`, `ServiceAccount`, `ClusterRoleBinding`, `Secret` requests | Request URI, Verb, Client IP, User Agent, RBAC Identity, HTTP Status | Detecting privilege escalation, anonymous access, and cluster-wide resource enumeration. |
| **Engine & Runtime** | `ContainerCreate`, `ContainerStart`, `Exec`, `Kill` | Container ID, Image SHA256, Namespaces, Volume Mounts, CapAdd list | Proving provenance of running binaries and detecting unauthorized interactive shells. |
| **Host & System** | `execve`, `ptrace`, `setns`, `socket`, `openat` | PID, PPID, UID, GID, Binary Path, Command Arguments, Exit Code | Identifying kernel exploits, in-memory execution, and container breakout attempts. |
| **Network & CNI** | Ingress/Egress packet flows, DNS queries, service mesh traces | Source IP/Port, Dest IP/Port, Protocol, DNS Query Domain, Packet Bytes | Catching C2 callbacks, data exfiltration, and cryptomining pool traffic. |

---

### 1.6 Continuous Posture Management (CSPM) & Metrics Framework

Static periodic audits fail to capture configuration drift in rapid deployment environments. Automated Cloud Security Posture Management (CSPM) converts CIS Kubernetes Benchmark specifications into continuous automated checks, emitting real-time Compliance Scores and drift alerts.

Financial institutions measure and report container security operations using 8 standardized quantitative metrics:

| Metric Category | Metric Identifier | Metric Name & Definition | Target Threshold | Monitoring Cadence |
| :--- | :--- | :--- | :--- | :--- |
| **KPI** | **KPI-SEC-01** | **Container Audit Log Ingestion Reliability**: Percentage of cluster nodes actively streaming uninterrupted audit and runtime telemetry to central SIEM. | **$\ge$ 99.95%** | Continuous / Real-Time |
| **KPI** | **KPI-SEC-02** | **Mean Time to Remediate High/Critical CVEs**: Average hours elapsed between image vulnerability identification and production pod rollout. | **$\le$ 24 Hours** | Weekly Average |
| **KPI** | **KPI-SEC-03** | **Admission Control Enforcement Coverage**: Ratio of production namespaces enforcing strict Pod Security Standard constraints. | **100%** | Continuous Audit |
| **KPI** | **KPI-SEC-04** | **Detection Rule Automated Validation Pass Rate**: Percentage of DaC Sigma rules verified through synthetic behavior reproduction tests. | **100%** | Per CI/CD Commit |
| **KRI** | **KRI-SEC-01** | **Unauthenticated / Anonymous API Invocations**: Number of control plane requests originating from `system:anonymous` or unmapped identities. | **0 (Absolute Zero)** | Real-Time Alerting |
| **KRI** | **KRI-SEC-02** | **Privileged Container Launch Attempts**: Count of pod creation requests requesting `privileged: true` or `CAP_SYS_ADMIN` in production. | **0 (Zero Tolerance)** | Immediate Incident |
| **KRI** | **KRI-SEC-03** | **HostPath Sensitive Volume Mount Violations**: Pod manifests attempting to mount `/`, `/etc`, `/proc`, or container engine sockets. | **0** | Immediate Incident |
| **KCI** | **KCI-SEC-01** | **CIS Kubernetes Benchmark Compliance Score**: Automated CSPM evaluation score against official CIS benchmark recommendations. | **$\ge$ 95.0%** | Daily Audit Score |

---

## 2. Production Incident & Remediation Architecture

### 2.1 Incident Walkthrough: High-Frequency Trading Core Breakout

In a tier-1 financial institution, an automated trading gateway container running in an on-premises Kubernetes cluster was compromised by an external threat actor.

```
+---------------------------------------------------------------------------------------------------+
|                               ATTACK SEQUENCE & LATERAL MOVEMENT PATH                            |
+---------------------------------------------------------------------------------------------------+
|  1. Initial Ingress: CVE-2024-38472 exploitation in trading API container (T1190)                 |
|  2. Execution: Interactive shell spawned via /bin/sh; cron persistence installed (T1059.004)       |
|  3. Discovery: Kubelet API queried for serviceaccount token & pod secrets (T1552.007, T1613)      |
|  4. Breakout: Container escape to worker node host via mounted docker.sock socket (T1611)         |
|  5. Impact: High-frequency transaction packet sniffer deployed on host interface (T1040)          |
+---------------------------------------------------------------------------------------------------+
```

#### Root-Cause Technical Failures:
1. **Permissive Admission Policy**: The deployment manifest mounted `/var/run/docker.sock` to enable local build tooling, granting root daemon control.
2. **Missing Runtime Syscall Filtering**: The container ran without a Seccomp or AppArmor profile, allowing arbitrary `execve` and `setns` system calls.
3. **Over-Privileged ServiceAccount**: The default ServiceAccount possessed cluster-wide `secrets:get` and `pods:list` RBAC permissions.
4. **Audit Log Ingestion Failure**: K8s API audit logs were buffered on node disk rather than forwarded in real-time, delaying detection by 4 hours.

---

### 2.2 End-to-End Hardened Architecture & Automated Containment

To remediate the vulnerability and prevent recurrence, the institution implemented a 5-tier defense-in-depth architecture:

```
+---------------------------------------------------------------------------------------------------+
|                        HARDENED FINANCIAL CONTAINER PRODUCTION ARCHITECTURE                       |
+---------------------------------------------------------------------------------------------------+
|  [ CI/CD Stage ]      -> Image Scan (Trivy) + Sign (Cosign) -> Immutable Registry (ECR/Harbor)     |
|  [ Admission Stage ]  -> OPA Gatekeeper: Enforce Non-Root + Block HostPath + Block Privileged     |
|  [ Runtime Stage ]    -> eBPF Kernel Probe (Cilium/Falco) -> Real-Time Syscall Behavioral Engine   |
|  [ Telemetry Stage ]  -> Fluent-Bit mTLS Stream -> Immutable SIEM Sink (WORM Storage)              |
|  [ Response Stage ]   -> SOAR DAG: Automated Pod Quarantine + Node Cordon + Token Invalidation   |
+---------------------------------------------------------------------------------------------------+
```

#### Declarative Production Policy Enforcements:

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
    namespaces: ["trading-production", "core-banking"]
  parameters:
    runAsNonRoot: true
    allowPrivilegeEscalation: false
    readOnlyRootFilesystem: true
    disallowedHostPaths:
      - pathPrefix: "/var/run"
      - pathPrefix: "/etc"
      - pathPrefix: "/proc"
      - pathPrefix: "/"
```

---

## 3. Exam Question Bank & Distractor Forensics

### Question 1 (FIRST Action)
During a routine night-shift security review, a financial SOC analyst receives a Category 1 Sigma rule alert indicating an unauthorized `kubectl exec` session initiated with `/bin/bash` into a payment processing container running in a production namespace. According to financial container incident response procedures, what is the **FIRST** operational step the analyst must execute?

- **A.** Terminate the worker node virtual machine immediately using the cloud infrastructure console.
- **B.** Isolate the affected pod using a zero-trust NetworkPolicy and export runtime forensic memory and audit logs before terminating the container workload.
- **C.** Modify the deployment manifest in Git and trigger a full Jenkins CI/CD redeployment pipeline.
- **D.** Submit a standard change management ticket requesting a software update during the next scheduled maintenance window.

> **Correct Answer: B**
> **Distractor Forensics:**
> - **Option A is Flawed**: Shutting down the entire worker node destroys in-memory forensic evidence and causes collateral service disruption to uninvolved tenant pods sharing the node.
> - **Option B is Correct**: Isolating the pod via NetworkPolicy blocks active C2 network communication while preserving ephemeral process memory and local disk artifacts for statutory digital forensics investigation.
> - **Option C is Flawed**: CI/CD redeployment does not contain the active adversary session currently running in the live pod.
> - **Option D is Flawed**: Critical interactive breakout attempts require immediate containment, not deferred routine change ticketing.

---

### Question 2 (BEST/MOST Strategy)
A financial institution operating in a hybrid cloud configuration deploys AWS EKS for customer-facing web services and on-premises OpenShift for core ledger transactions. The organization must ensure consistent detection engineering across both environments without maintaining duplicate, proprietary rule repositories for each vendor. Which architecture represents the **BEST** technical implementation?

- **A.** Author all detection logic exclusively in Splunk SPL and require all cloud providers to forward raw, unparsed syslog streams.
- **B.** Implement Detection as Code (DaC) using Sigma rules mapped to standardized Data Components (DCs), compiling vendor-neutral rules into native KQL/SPL formats via automated CI/CD pipelines.
- **C.** Rely entirely on AWS GuardDuty and disable all on-premises Kubernetes audit log collection to reduce operational storage overhead.
- **D.** Re-architect all core banking workloads into single monolithic virtual machines to eliminate container telemetry complexity.

> **Correct Answer: B**
> **Distractor Forensics:**
> - **Option A is Flawed**: Directly authoring rules in proprietary SPL creates tool lock-in and fails to establish an abstract detection taxonomy.
> - **Option B is Correct**: Implementing Detection as Code with Sigma and Data Components provides true detection sovereignty, enabling identical behavioral detection logic to compile across multi-cloud SIEM targets automatically.
> - **Option C is Flawed**: GuardDuty only monitors AWS workloads and cannot cover on-premises OpenShift clusters; disabling audit logs violates statutory retention mandates.
> - **Option D is Flawed**: Monolithic regression abandons microservice scalability and fails to address modern infrastructure requirements.

---

### Question 3 (NEXT Step)
An automated CSPM compliance scanner generates an alert showing that three namespaces in a production EKS cluster possess a CIS Benchmark Compliance Score of 68%, caused by pods executing with `allowPrivilegeEscalation: true` and missing network isolation policies. The security engineering team has already updated the base deployment Helm charts in Git. What is the **NEXT** technical step required to enforce compliance?

- **A.** Wait for the annual external regulatory audit to document the exception.
- **B.** Deploy an admission controller (OPA Gatekeeper or Kyverno) in `enforce` mode to block non-compliant pod creation at the API server gate and trigger a rolling restart of non-compliant workloads.
- **C.** Grant developers temporary cluster-admin permissions to manually patch live pods.
- **D.** Disable the CSPM scanner alert notifications to eliminate alert fatigue.

> **Correct Answer: B**
> **Distractor Forensics:**
> - **Option A is Flawed**: Compliance drift requires active remediation; deferring to annual audits violates continuous security standards.
> - **Option B is Correct**: Deploying declarative admission controller policies enforces immediate preventative gating at the API layer, while rolling restarts force workloads to adopt the corrected Helm chart configurations.
> - **Option C is Flawed**: Granting developers live cluster-admin access violates least privilege and introduces severe operational risk.
> - **Option D is Flawed**: Disabling scanner notifications blinds the organization to critical vulnerabilities.

---

### Question 4 (PRIMARY/EXCEPT Concept)
Under the Financial Container Security Monitoring Baseline (MCB), financial institutions deploying container workloads onto managed cloud environments (such as Google Cloud GKE Autopilot or AWS Fargate) maintain responsibility for all of the following governance and technical controls, **EXCEPT**:

- **A.** Retaining and forwarding raw Kubernetes control plane API audit logs to a centralized immutable SIEM for a minimum of one year.
- **B.** Applying kernel-level operating system patches directly to the cloud service provider's underlying physical hypervisor hosts.
- **C.** Defining and enforcing application-level RBAC role bindings, ServiceAccount token controls, and admission policies.
- **D.** Monitoring and investigating workload-centric CWPP security findings and runtime behavioral anomalies.

> **Correct Answer: B**
> **Distractor Forensics:**
> - **Option A is a Mandatory Responsibility**: Financial institutions are legally required to maintain digital audit trails regardless of hosting model.
> - **Option B is the EXCEPTION (Correct Answer)**: In managed serverless/cloud container environments, physical hypervisor and host kernel maintenance is the exclusive operational responsibility of the Cloud Service Provider (CSP).
> - **Option C is a Mandatory Responsibility**: Tenant-level RBAC, ServiceAccounts, and workload admission are 100% managed by the institution.
> - **Option D is a Mandatory Responsibility**: Investigating workload-level runtime anomalies remains a core monitoring governance duty.
