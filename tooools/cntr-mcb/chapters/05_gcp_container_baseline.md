# Chapter 5: Google Cloud Container Security Monitoring & Configuration Baseline

## 1. Statutory Baseline & Technical Control Matrix

Financial institutions deploying containerized workloads on Google Cloud Platform must satisfy multi-jurisdictional regulatory frameworks. Key standards include the Financial Supervisory Commission (FSC) Regulations Governing Internal Control Systems, Financial Cloud Outsourcing Guidelines, ISO/IEC 27001 Annex A.12, NIST SP 800-190 (Application Container Security Guide), and the Center for Internet Security (CIS) Google Kubernetes Engine (GKE) Benchmark v2.0.1. Under the cloud shared responsibility model, Google manages the physical data centers, host hardware, hypervisors, and Kubernetes control plane infrastructure. Financial institutions retain full operational accountability for container images, pod configurations, identity and access management (IAM) bindings, network segmentation, runtime behavioral telemetry, and long-term audit trail retention.

```
+---------------------------------------------------------------------------------------------------+
|                               SHARED RESPONSIBILITY IN GOOGLE CLOUD                               |
+---------------------------------------------------------------------------------------------------+
| Customer Responsibility:                                                                          |
| - Pod Security Context, ServiceAccount Bindings, NetworkPolicies, Policy Controller Constraints   |
| - Container Image Integrity, Vulnerability Remediation, Binary Authorization Attestations        |
| - Cloud Audit Logs Export, Security Command Center (SCC) Triage, Chronicle SIEM Correlation       |
+---------------------------------------------------------------------------------------------------+
| Google Cloud Responsibility:                                                                      |
| - Kubernetes Control Plane (etcd, kube-apiserver, kube-scheduler, kube-controller-manager)        |
| - Worker Node Infrastructure (Autopilot Mode OS, Kernel Patching, Hypervisor Isolation)           |
| - Physical Facilities, Hardware Security Modules (Cloud KMS), Global VPC Backbone                 |
+---------------------------------------------------------------------------------------------------+
```

### 1.1 GKE Architecture & Foundational Security Controls

Google Kubernetes Engine provides two operational models: GKE Standard and GKE Autopilot. In GKE Standard, the tenant configures, scales, and maintains the underlying Compute Engine worker nodes, requiring explicit OS patch management, node pool maintenance, and agent installations. In GKE Autopilot, Google provisions, hardens, and operates the worker node infrastructure according to strict security baselines. Autopilot blocks privileged pods, restricts dangerous hostPath mounts, automates node operating system upgrades, and secures worker node surfaces by default, reducing cluster attack vectors.

Regardless of the operational model, financial container baselines mandate four foundational architecture components:

1. Workload Identity Federation: Eliminates static, long-lived service account JSON keys inside containers. Workload Identity maps Kubernetes ServiceAccounts (KSAs) directly to Google Cloud IAM ServiceAccounts (GSAs). The GKE metadata server intercepts container requests to `169.254.169.254` and exchanges projected Kubernetes service account tokens for short-lived Google Cloud OAuth2 access tokens via Google Cloud Security Token Service (STS). This mechanism enforces least-privilege API access without storing credentials in pod filesystems or environment variables.

2. GKE Sandbox (gVisor Runtime): Provides user-space kernel virtualization using the `gvisor` runtime class (`runsc`). GKE Sandbox intercepts container system calls, executing them in an unprivileged user-space kernel rather than allowing direct execution against the host Linux kernel. This architectural boundary neutralizes container breakout attacks (MITRE ATT&CK T1611) and kernel privilege escalation attempts (T1068) in multi-tenant environments.

3. Shielded GKE Nodes: Enforces cryptographic hardware-rooted integrity for all worker nodes using Unified Extensible Firmware Interface (UEFI) Secure Boot, virtual Trusted Platform Modules (vTPM), and kernel integrity monitoring. Shielded Nodes prevent malicious bootloaders, kernel-level rootkits, and unauthorized driver injection from compromising the node operating system.

4. Private GKE Clusters & Authorized Networks: Disables public IPv4 endpoints on cluster control plane masters. API server communication requires private VPC peering or Cloud Interconnect routing, restricted through Master Authorized Networks to designated bastion jump hosts and approved internal CIDR blocks. Node pools reside exclusively in private subnets with private IP addresses, routing external traffic through Cloud NAT gateways.

### 1.2 Security Command Center (SCC) Premium CWPP & CSPM Engine

Security Command Center Premium serves as the core Cloud Workload Protection Platform (CWPP) and Cloud Security Posture Management (CSPM) solution for Google Cloud container estates. SCC integrates four specialized detection engines:

1. Container Threat Detection (CTD): Operates an eBPF-based guest telemetry engine embedded directly into GKE node kernels. CTD monitors container namespaces in real time, capturing system calls, dynamic process executions, and network socket transitions without requiring modifications to container source code or base images. CTD generates high-fidelity findings when observing abnormal execution, including `execution: modified malicious binary executed` (T1036.005), `reverse shell` (T1190), `unexpected child shell` (T1609, T1552.007), `privilege escalation: sudo potential privilege escalation` (T1068), and `execution: container escape` (T1611).

2. Event Threat Detection (ETD): Consumes the continuous Cloud Audit Logs event stream, evaluating identity behaviors and administrative actions across the Google Cloud organization. ETD detects control plane compromises, including abnormal IAM privilege grants, credential access from suspicious IP ranges (T1078.001), administrative evasion through log sink modifications (T1070), and anomalous Kubernetes RBAC cluster-admin role bindings.

3. Virtual Machine Threat Detection (VMTD): Delivers hypervisor-level agentless memory inspection for Compute Engine worker nodes. Operating from the Google Cloud hypervisor layer below the virtual machine operating system, VMTD scans node memory for hidden kernel rootkits, memory injection techniques, and unauthorized cryptocurrency mining threads without placing agent software inside the guest OS or degrading pod execution performance.

4. Security Health Analytics (SHA): Provides continuous, automated CSPM posture assessment against CIS GKE Benchmark v2.0.1 and regulatory compliance frameworks. SHA scans cluster configuration definitions, reporting non-compliant assets such as legacy node metadata endpoints enabled, default service accounts bound to cluster nodes, missing network policies, and publicly exposed dashboard services.

In addition to SCC, financial clusters deploy Policy Controller, an admission control engine based on Open Policy Agent (OPA) Gatekeeper. Policy Controller intercepts Kubernetes API admission requests, evaluating pod specifications against declarative constraint templates before committing objects to etcd. Policy Controller strictly rejects privileged containers (`securityContext.privileged: true`), hostPath volume mounts to sensitive directories (`/`, `/proc`, `/etc`, `/var/run/docker.sock`), host network sharing (`hostNetwork: true`), and root user execution (`runAsNonRoot: true`).

```
+---------------------------------------------------------------------------------------------------+
|                        SECURITY COMMAND CENTER (SCC) DETECTION TAXONOMY                           |
+--------------------------+-----------------------+------------------------------------------------+
| Detection Engine         | Telemetry Source      | Key Threat Detections (MITRE ATT&CK)           |
+--------------------------+-----------------------+------------------------------------------------+
| Container Threat         | eBPF Kernel Probes in | - execution: modified malicious binary (T1036) |
| Detection (CTD)          | Container Namespaces  | - execution: container escape (T1611)          |
|                          |                       | - reverse shell / unexpected child shell       |
|                          |                       | - credential access: access sensitive files    |
+--------------------------+-----------------------+------------------------------------------------+
| Event Threat             | Cloud Audit Logs      | - anomalous RBAC role grants (T1078, T1098)   |
| Detection (ETD)          | (Admin Activity,      | - audit logging sink tampering (T1070)         |
|                          | Data Access)          | - API calls from suspicious/anomalous IPs      |
+--------------------------+-----------------------+------------------------------------------------+
| Virtual Machine Threat   | Hypervisor Memory     | - kernel rootkits & memory injection (T1068)   |
| Detection (VMTD)         | Inspection (Compute   | - unauthorized cryptomining processes (T1496)  |
|                          | Engine Nodes)         | - zero guest agent footprint or latency        |
+--------------------------+-----------------------+------------------------------------------------+
| Security Health          | Resource Metadata &   | - CIS GKE Benchmark v2.0.1 compliance checks  |
| Analytics (SHA)          | GKE API Configuration | - open dashboard / public master endpoint      |
|                          |                       | - overprivileged node service accounts         |
+--------------------------+-----------------------+------------------------------------------------+
```

### 1.3 GKE Advanced Vulnerability Insights & Supply Chain Controls

Securing the container lifecycle requires shifting defense into the build and admission phases:

1. GKE Advanced Vulnerability Insights: Delivers continuous, automated container workload vulnerability scanning. Unlike basic scanning limited to OS package manifests, Advanced Vulnerability Insights inspects running workloads for known Common Vulnerabilities and Exposures (CVEs) across operating system distributions (Debian, Ubuntu, Alpine, Red Hat) as well as language-level runtime dependency packages (Go, Java, Node.js, Python).

2. Artifact Registry Integrated Scanning: Automates vulnerability analysis upon container image ingestion into Google Cloud Artifact Registry. Artifact Registry tags images with vulnerability summaries, tracking Common Vulnerability Scoring System (CVSS) scores and exploit availability.

3. Binary Authorization: Implements cryptographic signature gates at GKE admission controllers. Binary Authorization requires deployable container images to carry digital attestations generated by trusted CI/CD pipelines (such as Cloud Build) and signed using asymmetric Cloud KMS keys. If an image lacks a valid cryptographic signature or contains unaddressed Critical CVEs, Binary Authorization blocks deployment, preventing image tampering (MITRE ATT&CK T1525) and unauthorized container deployment (T1610).

```
+---------------------------------------------------------------------------------------------------+
|                        SUPPLY CHAIN SECURITY & ADMISSION CONTROL PIPELINE                         |
+---------------------------------------------------------------------------------------------------+
| [Source Repository] --> [Cloud Build Pipeline] --> [Artifact Registry Vulnerability Scan]        |
|                                                                 |                                 |
|                                                                 v                                 |
| [Admission Denied] <-- [Binary Authorization Check] <-- [Cloud KMS Cryptographic Attestation]     |
|         |                               |                                                         |
|         v                               v                                                         |
|   (Block Deploy)                 (Signed & Clean)                                                 |
|                                         |                                                         |
|                                         v                                                         |
|                         [GKE Admission Controller] --> [Pod Deployed in GKE Sandbox]              |
+---------------------------------------------------------------------------------------------------+
```

### 1.4 Telemetry Taxonomy & Chronicle SIEM Export Pipeline

Financial compliance mandates complete traceability across all Kubernetes control plane operations and container runtime activities. Cloud Logging collects events across distributed clusters, while Cloud Audit Logs records administrative and data access interactions.

To establish observability, native Google Cloud services map directly to standardized Data Component (DC) tags:

| Data Component Tag | Native Log Source Category | Google Cloud Native Service Implementation |
|---|---|---|
| `kubernetes:audit` | Kubernetes Audit Log | Cloud Audit Logs (Admin Activity & Data Access) |
| `kubernetes:events` | Kubernetes Cluster Events | Cloud Logging / GKE Cluster Event Stream |
| `kubernetes:apiserver` | Kubernetes API Server Logs | Cloud Logging (GKE Control Plane Logs) |
| `kubernetes:orchestrator` | K8s Controller Manager / Scheduler Logs | Cloud Logging (GKE Control Plane Logs) |
| `docker:events` / `containerd:events` | Containerd Lifecycle Events | Cloud Logging (Node Logs / systemd journald) |
| `docker:daemon` / `containerd:runtime` | Container Runtime Logs | Cloud Logging (Node Logs - containerd service) |
| `docker:api` | Node Container Runtime API Calls | SCC CTD Agent / Security Telemetry Agent (Note: Cloud Audit Logs records Google Cloud and K8s APIs, not node-local socket calls) |
| `docker:registry` | Container Registry Operations | Cloud Audit Logs (Artifact Registry audit events) |
| `ebpf:syscalls` | Kernel System Call Telemetry | Security Command Center CTD Agent (eBPF telemetry) |
| `docker:stats` | Container Resource Metrics | Cloud Monitoring & Cloud Logging (Container Metrics) |

For enterprise security operations, clusters route audit records using Cloud Logging Log Sinks. Log Sinks forward normalized JSON telemetry to Cloud Pub/Sub topics. Google Chronicle SIEM (Google SecOps) ingests the Pub/Sub stream, indexing Kubernetes events into unified security telemetry schemas (UDM) for petabyte-scale behavioral analysis, threat intelligence correlation, and automated security orchestration. Concurrently, a secondary Log Sink routes telemetry to Google BigQuery, satisfying 365-day immutable financial compliance storage requirements.

```
+---------------------------------------------------------------------------------------------------+
|                           ENTERPRISE LOG EXPORT & SIEM ARCHITECTURE                               |
+---------------------------------------------------------------------------------------------------+
| [GKE Cluster: Control Plane & Nodes]                                                              |
|        |                                                                                          |
|        +--> Cloud Audit Logs (Admin Activity, Data Access)                                         |
|        +--> GKE stdout/stderr & Node journald Logs                                                |
|        +--> SCC CTD / ETD / VMTD Finding Stream                                                   |
|                    |                                                                              |
|                    v                                                                              |
|           [Cloud Logging Router]                                                                  |
|                    |                                                                              |
|         +----------+----------+                                                                   |
|         |                     |                                                                   |
|         v                     v                                                                   |
|   [Log Sink: Pub/Sub]   [Log Sink: BigQuery]                                                      |
|         |                     |                                                                   |
|         v                     v                                                                   |
|  [Google Chronicle]    [Long-Term Audit Archive]                                                  |
|  - UDM Normalization   - Immutable Storage (365 Days)                                             |
|  - YARA-L Rules Engine - Statutory Compliance Reports                                             |
|  - SOAR Workflows                                                                                 |
+---------------------------------------------------------------------------------------------------+
```

### 1.5 MITRE ATT&CK for Containers Coverage & Architecture Boundary Exclusions

The baseline evaluates 36 container threat techniques (TTPs) defined by MITRE ATT&CK for Containers:

1. Direct Native CWPP Coverage: 33 TTPs receive out-of-the-box behavioral detection via SCC CTD, ETD, and VMTD finding categories. These cover unauthorized binary execution, privilege escalation, credential file access, shell spawning, and container breakouts.

2. Conditional Architectural Exclusions (Compensating Controls):
- T1498 (Network Denial of Service): SCC CTD does not inspect raw network packet flood volume. The compensating control mandates Cloud Armor (WAF) distributed denial-of-service mitigation and Cloud Next Generation Firewall (Cloud NGFW) intrusion inspection.
- T1525 (Implant Internal Image): SCC CTD focuses on post-deployment container runtime behavior. The compensating control mandates Binary Authorization admission gates paired with Artifact Registry automated vulnerability scanning to block tainted images before admission.

3. Absolute Architectural Exclusion:
- T1059.013 (Container CLI/API direct abuse): In GKE (particularly Autopilot), Google manages the master control plane infrastructure, network endpoints, and kubelet runtime isolation. Direct, unauthenticated access to the underlying container engine socket or runtime CLI is blocked by Google infrastructure architecture. All management traffic must authenticate through Google Cloud IAM and the Kubernetes API server. Compensating governance uses Cloud Audit Logs and SCC ETD to track all authorized administrative interactions.

```
+---------------------------------------------------------------------------------------------------+
|                        MITRE ATT&CK FOR CONTAINERS EVALUATION BREAKDOWN                           |
+----------------------------------+-------+--------------------------------------------------------+
| Classification                   | Count | Primary Mechanism & Compensating Architecture          |
+----------------------------------+-------+--------------------------------------------------------+
| Direct Native CWPP Findings      | 33    | SCC CTD (eBPF), SCC ETD (Audit Logs), SCC VMTD (Memory)|
| Conditional Exclusion (Mitigated)| 2     | T1498 (Cloud Armor/NGFW), T1525 (Binary Authorization) |
| Absolute Architectural Exclusion | 1     | T1059.013 (GKE Managed Control Plane & IAM Isolation)  |
+----------------------------------+-------+--------------------------------------------------------+
| Total Evaluated Techniques       | 36    | Effective Detection & Compensating Control Rate: 100%  |
+----------------------------------+-------+--------------------------------------------------------+
```

### 1.6 Quantitative Telemetry & Key Control Indicators Matrix

Financial institutions must monitor operational metrics to verify that container security controls function within defined thresholds:

| Metric ID | Indicator Type | Metric Name | Target Threshold | Telemetry Source & Validation Method | Responsible Team |
|---|---|---|---|---|---|
| KCI-GCP-01 | Key Control Indicator | GKE Control Plane Audit Log Ingestion Completeness | 100% Admin & Data Access captured; Log Sink drop rate < 0.001% | Cloud Monitoring metric `logging.googleapis.com/log_entry_count` compared against API server request volume | Cloud Platform Operations / SecOps |
| KCI-GCP-02 | Key Control Indicator | Workload Identity Adoption Ratio | 100% pods accessing Google Cloud APIs use Workload Identity; 0 static JSON keys | Security Health Analytics finding `NON_COMPLIANT_SERVICE_ACCOUNT_KEY` and Policy Controller audit | Cloud Architecture / IAM Team |
| KCI-GCP-03 | Key Control Indicator | Binary Authorization Attestation Enforcement | 100% production pods verified via Cloud KMS signature; 0 unverified images | Binary Authorization admission audit logs (`dryrun: false`) in Cloud Audit Logs | DevSecOps / Release Engineering |
| KRI-GCP-01 | Key Risk Indicator | Container Runtime Threat Detection Latency | Mean Time to Detect (MTTD) < 60 seconds from exploit to SCC finding | Security Command Center CTD alert timestamp delta against node syscall event timestamp | Security Operations Center (SOC) |
| KRI-GCP-02 | Key Risk Indicator | Critical Workload CVE Exposure Duration | Mean Time to Remediate (MTTR) < 48 hours for CVSS >= 9.0 vulnerabilities | GKE Advanced Vulnerability Insights continuous workload reports | Application Security / SRE |
| KRI-GCP-03 | Key Risk Indicator | Overprivileged Workload Cluster-Admin Bindings | 0 unauthorized ClusterRoleBindings in non-system namespaces | Cloud Audit Logs API queries filtered by `verb=create AND resource=clusterrolebindings` | Cloud Governance / Compliance |
| KPI-GCP-01 | Key Performance Indicator | CIS GKE Benchmark Compliance Posture Score | >= 98% compliance score maintained across all production clusters | Security Command Center Security Health Analytics compliance dashboard | Cloud Security Architecture |
| KPI-GCP-02 | Key Performance Indicator | Policy Controller Constraint Pass Rate | >= 99.9% admission requests comply with security constraints without rejection | Policy Controller Prometheus metrics `gatekeeper_violations` and admission review counts | Kubernetes Platform Team |

---

## 2. Production Incident & Remediation Architecture

### 2.1 Incident Context & Attack Execution

A financial services firm operated a critical core banking transaction gateway on a production GKE Standard cluster. The application environment processed retail transaction requests, interacting with a private Cloud SQL PostgreSQL database through Google Cloud Workload Identity. The cluster resided within a dedicated Virtual Private Cloud (VPC) with outbound connectivity managed via Cloud NAT.

```
+---------------------------------------------------------------------------------------------------+
|                                PRODUCTION INCIDENT ATTACK SEQUENCE                               |
+---------------------------------------------------------------------------------------------------+
| 1. Ingress Exploit: Attacker sends serialized payload to public transaction service (T1190)       |
|    |                                                                                              |
|    v                                                                                              |
| 2. Runtime Execution: Java workload spawns /bin/sh; attacker overwrites /usr/bin/ps (T1036.005)   |
|    |                                                                                              |
|    v                                                                                              |
| 3. Host Escape Attempt: Attacker queries mounted /var/run/docker.sock to access host node (T1611) |
|    |                                                                                              |
|    v                                                                                              |
| 4. Metadata Harvesting: Attacker queries 169.254.169.254 to harvest node service account token    |
|    |                                                                                              |
|    v                                                                                              |
| [BLOCKED & DETECTED]: SCC CTD fires Critical Alert; Chronicle SIEM triggers automated SOAR pod kill|
+---------------------------------------------------------------------------------------------------+
```

The attack progressed through four sequential stages:

1. Initial Compromise via Ingress Webhook (MITRE ATT&CK T1190): An external threat actor identified an unpatched remote code execution vulnerability in an internet-facing transaction processing service. The container ran an outdated Java runtime with vulnerable third-party dependencies. The attacker delivered a specially crafted HTTP request containing an exploitation payload, achieving remote code execution inside the container.

2. Shell Execution & Binary Masquerading (MITRE ATT&CK T1059.004 & T1036.005): Upon gaining code execution, the attacker invoked `/bin/sh` to launch an interactive reverse shell back to a remote command-and-control server. To evade basic process monitoring tools executed by operational engineers, the attacker replaced the native `/usr/bin/ps` binary with a modified script designed to filter out malicious process names. Security Command Center Container Threat Detection intercepted the underlying `execve` and `unlink` system calls via eBPF probes, immediately generating the finding: `execution: modified malicious binary executed` (Finding Category: `execution: modified malicious binary executed`, Severity: `Critical`).

3. Container Breakout Attempt via Socket Mount (MITRE ATT&CK T1611): Seeking host-level persistence, the attacker examined the container filesystem. Due to a legacy configuration error in the pod deployment specification, the application mounted the host path `/var/run/docker.sock` to support legacy container metrics tooling. The attacker attempted to use the mounted socket to spin up an unauthorized sibling container with host root privileges (`securityContext.privileged: true`).

4. Node Metadata Credential Access Attempt (MITRE ATT&CK T1552.001 & T1078.001): Concurrently, the attacker issued an HTTP GET request to `http://169.254.169.254/computeMetadata/v1/instance/service-accounts/default/token` with the required `Metadata-Flavor: Google` header. The attacker intended to extract OAuth2 access tokens associated with the underlying Compute Engine node pool to move laterally into Google Cloud Storage buckets and BigQuery datasets.

### 2.2 Root-Cause Defect Analysis

The forensic post-mortem revealed four fundamental architectural defects:

1. Absence of Admission Policy Enforcement: The cluster lacked Policy Controller constraint templates. Deployments could mount sensitive host paths (`/var/run/docker.sock`) and configure privileged security contexts without encountering admission rejections.

2. Unhardened Node Metadata Endpoints: While the application used Workload Identity for Cloud SQL access, the underlying GKE node pool had not enabled GKE Metadata Concealment (`node-metadata=GKE_METADATA`). Consequently, pods could fall back to querying the Compute Engine default service account attached to the virtual machine node, exposing node-level IAM permissions.

3. Unenforced Supply Chain Attestation: The CI/CD deployment pipeline pushed container images directly into Artifact Registry without requiring cryptographic signing or Binary Authorization verification. The vulnerable container image was deployed despite harboring known Critical CVEs.

4. Incomplete Control Plane Telemetry Export: The Cloud Logging Log Sink filtered out Kubernetes API server Data Access logs to reduce log ingestion costs. Consequently, initial discovery queries against the Kubernetes API went unrecorded in the enterprise SIEM until SCC CTD triggered runtime alerts.

### 2.3 Step-by-Step Remediation Architecture

The engineering and security teams executed a four-phase remediation plan to restore operational integrity:

```
+---------------------------------------------------------------------------------------------------+
|                               PHASED REMEDIATION ARCHITECTURE                                     |
+-------------------+-------------------------------------------------------------------------------+
| Phase             | Operational Actions & Technical Controls                                      |
+-------------------+-------------------------------------------------------------------------------+
| Phase 1:          | 1. Isolate compromised worker nodes using `kubectl cordon` and `drain`.       |
| Containment       | 2. Terminate rogue pods; revoke active OAuth2 access tokens in Cloud IAM.     |
|                   | 3. Apply temporary Cloud Armor WAF rule blocking exploit request signature.   |
+-------------------+-------------------------------------------------------------------------------+
| Phase 2:          | 1. Deploy Policy Controller constraint templates blocking hostPath mounts.     |
| Admission Policy  | 2. Enforce `runAsNonRoot: true` and drop all Linux capabilities.              |
|                   | 3. Restrict `securityContext.privileged: false` across all namespaces.        |
+-------------------+-------------------------------------------------------------------------------+
| Phase 3:          | 1. Recreate node pools with `workload-metadata=GKE_METADATA` enabled.          |
| Host & Supply     | 2. Configure Binary Authorization policy requiring Cloud KMS attestations.    |
| Chain Hardening   | 3. Activate GKE Advanced Vulnerability Insights continuous scanning.          |
+-------------------+-------------------------------------------------------------------------------+
| Phase 4:          | 1. Configure Cloud Logging Log Sink exporting 100% Audit Logs to Pub/Sub.    |
| SIEM Detection &  | 2. Deploy Chronicle YARA-L rules correlating CTD findings with API activity.  |
| Automation        | 3. Implement Cloud Function SOAR workflow for automated pod quarantine.       |
+-------------------+-------------------------------------------------------------------------------+
```

#### Phase 1: Containment & Threat Neutralization
1. Isolate the affected worker node by issuing `kubectl cordon <node-name>` and `kubectl drain <node-name> --delete-emptydir-data --force --ignore-daemonsets`, preventing new pods from scheduling onto the contaminated host.
2. Delete the compromised pod workload directly via `kubectl delete pod <pod-name> -n banking-prod --grace-period=0 --force`.
3. Revoke active OAuth2 access tokens and rotate the Compute Engine default service account keys within Cloud IAM.
4. Apply an emergency Cloud Armor rate-limiting and signature-matching rule at the external HTTP(S) Load Balancer to drop exploit payloads matching the CVE vector.

#### Phase 2: Policy Controller Admission Enforcement
Deploy declarative OPA Gatekeeper constraint templates via Policy Controller to prevent recurring configuration weaknesses.

Create the constraint template denying host filesystem mounts:

```yaml
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sNoHostPath
metadata:
  name: enforce-no-hostpath
spec:
  enforcementAction: deny
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
    namespaces:
      - "banking-prod"
      - "default"
```

Create the constraint template enforcing non-privileged execution and dropping dangerous capabilities:

```yaml
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sRestrictedCapabilities
metadata:
  name: drop-all-capabilities
spec:
  enforcementAction: deny
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
  parameters:
    requiredDropCapabilities:
      - "ALL"
      - "CAP_SYS_ADMIN"
```

#### Phase 3: Node Metadata Protection & Binary Authorization Activation
1. Rebuild the GKE node pool using the Google Cloud CLI, strictly enforcing Workload Identity metadata protection and Shielded Node configurations:

```bash
gcloud container node-pools create secure-pool-01 \
    --cluster=banking-gke-prod \
    --region=asia-east1 \
    --node-version=latest \
    --workload-metadata=GKE_METADATA \
    --enable-shielded-nodes \
    --shielded-secure-boot \
    --shielded-vtpm \
    --shielded-integrity-monitoring \
    --image-type=COS_CONTAINERD \
    --metadata=disable-legacy-endpoints=true
```

2. Enforce Binary Authorization by linking GKE admission to a Cloud Build attestor key in Cloud KMS:

```yaml
apiVersion: binaryauthorization.googleapis.com/v1
kind: Policy
defaultAdmissionRule:
  evaluationMode: REQUIRE_ATTESTATION
  enforcementMode: ENFORCING_BLOCK_AND_AUDIT_LOG
  requireAttestationsBy:
    - projects/banking-security-prod/attestors/secops-ci-attestor
clusterAdmissionRules:
  asia-east1.banking-gke-prod:
    evaluationMode: REQUIRE_ATTESTATION
    enforcementMode: ENFORCING_BLOCK_AND_AUDIT_LOG
    requireAttestationsBy:
      - projects/banking-security-prod/attestors/secops-ci-attestor
```

#### Phase 4: Chronicle SIEM Detection Rule Deployment
Configure a Google Chronicle YARA-L detection rule to correlate SCC CTD runtime alerts with anomalous Kubernetes API calls:

```
rule gke_runtime_binary_modification_and_privilege_escalation {
  meta:
    author = "Financial SecOps Engineering"
    description = "Detects modified binary execution inside GKE followed by privileged escalation or container escape"
    severity = "CRITICAL"
    ttp = "T1036.005, T1611"

  events:
    // Match SCC CTD finding for modified binary execution
    $scc.metadata.event_type = "SECURITY_COMMAND_CENTER"
    $scc.security_result.category = "execution: modified malicious binary executed"
    $scc.principal.hostname = $node_name
    $scc.target.resource.name = $container_id

    // Match Kubernetes audit event for privileged pod creation or exec
    $k8s.metadata.event_type = "KUBERNETES_AUDIT"
    $k8s.target.resource.name = $container_id
    $k8s.security_result.action = "ALLOW"

  match:
    $container_id over 5m

  condition:
    $scc and $k8s
}
```

---

## 3. Exam Question Bank & Distractor Forensics

### Question 1: Incident Response Priority on Container Escape Finding
During live operations, the Security Operations Center (SOC) receives a Critical alert from Security Command Center Container Threat Detection: `finding.category = "execution: container escape"` associated with a production transaction gateway pod running in a financial GKE cluster. What is the FIRST operational action the incident response engineer should perform?

- A. Delete the GKE cluster using the Google Cloud CLI to stop the attack.
- B. Cordon and drain the affected worker node, then isolate the compromised pod while capturing forensic memory state.
- C. Update the Policy Controller constraint template to deny all incoming Kubernetes admission requests.
- D. Modify the application base image in Artifact Registry and trigger a new CI/CD pipeline build.

#### Answer & Distractor Forensics
- Correct Answer: B
- Option A is incorrect. Deleting the entire production Kubernetes cluster destroys business service availability, violating Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO), while simultaneously destroying volatile RAM evidence on worker nodes needed for forensic analysis.
- Option B is correct. In accordance with NIST SP 800-61 incident response guidelines, the FIRST priority upon verifying an active container escape is immediate containment: cordoning the node prevents newly scheduled workloads from landing on the compromised host, draining relocates uncompromised sibling pods safely, and isolating the pod while securing volatile memory ensures evidence preservation prior to node rebuilding.
- Option C is incorrect. Updating admission constraints in Policy Controller addresses preventative guardrails for future deployments, but does nothing to contain or remediate a threat that has already bypassed admission control and executed an escape into the host kernel.
- Option D is incorrect. Rebuilding container images in the CI/CD pipeline is an eradication and recovery step that occurs much later in the incident response lifecycle. Modifying images while an active adversary maintains host-level execution fails to contain ongoing lateral movement.

### Question 2: Eliminating Metadata Service Account Harvesting
A financial architecture audit identifies that container workloads running on GKE can potentially extract Compute Engine default service account tokens by querying the instance metadata IP `169.254.169.254`. Which GCP architectural pattern is the MOST effective control to completely eliminate this vulnerability without disrupting legitimate Google Cloud API access for applications?

- A. Configure custom iptables firewall rules inside every container base image to drop outgoing traffic to 169.254.169.254.
- B. Disable all external network access for the GKE cluster by deleting the default internet gateway and Cloud NAT.
- C. Enable GKE Workload Identity on the cluster and configure node pools with `workload-metadata=GKE_METADATA`.
- D. Rotate the Compute Engine default service account private JSON keys every 60 minutes via an automated Cloud Function.

#### Answer & Distractor Forensics
- Correct Answer: C
- Option A is incorrect. Configuring iptables inside application container images is unmaintainable and ineffective because unprivileged containers lack `CAP_NET_ADMIN` to modify routing tables. Furthermore, an attacker gaining root inside a container can alter local iptables rules.
- Option B is incorrect. Deleting internet egress gateways disables all external communication, breaking legitimate payment gateway integrations and third-party APIs, while failing to block access to the internal link-local metadata address `169.254.169.254`.
- Option C is correct. Enabling GKE Workload Identity with `workload-metadata=GKE_METADATA` forces the GKE metadata server to intercept all requests to `169.254.169.254`. The metadata server blocks direct access to the underlying Compute Engine instance service account, permitting only pods with explicitly bound Kubernetes ServiceAccounts to acquire short-lived, scoped OAuth2 tokens for their mapped Google Cloud ServiceAccount.
- Option D is incorrect. Rotating static JSON keys does not stop workloads from querying the instance metadata server for temporary OAuth2 tokens. Key rotation adds operational complexity without eliminating the underlying architectural flaw.

### Question 3: Remediating Posture Drifts Discovered by SCC Security Health Analytics
A routine compliance audit conducted by Security Command Center Security Health Analytics (SHA) reports multiple CIS Google Kubernetes Engine Benchmark v2.0.1 failures across three staging clusters. Specifically, developers have deployed pods with `securityContext.privileged: true` and mounted host directories to `/etc`. Following the identification of these non-compliant configurations, which implementation step should the security engineering team execute NEXT to enforce preventative compliance?

- A. Deploy Policy Controller constraint templates enforcing `K8sNoHostPath` and `K8sRestrictedCapabilities` in admission control.
- B. Enable Cloud Logging Log Sinks exporting all cluster stdout/stderr logs directly to Google Chronicle.
- C. Manually execute `kubectl exec` into every running pod to delete the mounted `/etc` directories.
- D. Purchase additional Compute Engine virtual machine quota to scale the cluster node pool.

#### Answer & Distractor Forensics
- Correct Answer: A
- Option A is correct. Once configuration posture drifts are identified by CSPM scanning (SHA), the NEXT logical architectural step is deploying preventative admission control guardrails. Policy Controller constraint templates enforce automated compliance at the API admission boundary, automatically rejecting future pod deployments that request privileged execution or hostPath volume mounts.
- Option B is incorrect. Exporting runtime application logs to Chronicle provides detection and historical audit observability, but does not prevent developers or automated pipelines from deploying non-compliant, insecure pod configurations.
- Option C is incorrect. Manually executing `kubectl exec` into running pods is an ad-hoc, error-prone action that violates change management policies and can cause service downtime without preventing newly deployed pods from repeating the identical configuration error.
- Option D is incorrect. Scaling Compute Engine quota addresses infrastructure compute capacity, which has no relationship to remediating Kubernetes configuration compliance failures.

### Question 4: Architecture Exclusion Classification in Managed GKE Estates
Under the Financial Container Security Monitoring Baseline (MCB), container threat techniques are categorized across native CWPP coverage, conditional architectural exclusions, and absolute architectural exclusions. Which of the following MITRE ATT&CK techniques is classified as an ABSOLUTE architectural exclusion in Google Kubernetes Engine (particularly Autopilot mode), and why?

- A. T1611 (Escape to Host), because GKE uses Linux kernels that cannot be breached by container breakout techniques.
- B. T1059.013 (Container CLI/API direct abuse), because Google Cloud manages control plane access and isolates container runtime sockets behind Google IAM.
- C. T1498 (Network Denial of Service), because Google Cloud VPC networks possess infinite network capacity and cannot experience denial of service.
- D. T1525 (Implant Internal Image), because Artifact Registry automatically deletes any container image uploaded with known software vulnerabilities.

#### Answer & Distractor Forensics
- Correct Answer: B
- Option A is incorrect. T1611 (Escape to Host) is not an architectural exclusion; it is actively monitored and covered by Security Command Center Container Threat Detection through native eBPF syscall probes that detect breakout behavior.
- Option B is correct. T1059.013 is classified as an absolute architectural exclusion because in managed GKE (especially Autopilot mode), Google operates and isolates the underlying container runtime daemons and control plane infrastructure. Unauthenticated access to the underlying Docker/containerd UNIX socket or administrative CLI is blocked by Google infrastructure architecture; all administrative requests must authenticate through Google Cloud IAM and the Kubernetes API server.
- Option C is incorrect. T1498 (Network Denial of Service) is a conditional architectural exclusion mitigated by Cloud Armor and Cloud NGFW, not an absolute exclusion. Public cloud networks are not infinite and can be overwhelmed without WAF and DDoS mitigation layers.
- Option D is incorrect. T1525 (Implant Internal Image) is a conditional architectural exclusion mitigated by Binary Authorization cryptographic attestations. Artifact Registry does not automatically delete images containing vulnerabilities; it scans and indexes CVE findings for policy evaluation.
