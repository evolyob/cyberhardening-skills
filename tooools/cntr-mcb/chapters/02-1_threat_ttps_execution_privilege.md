# Chapter 02-1: Threat TTPs Part 1: Initial Access, Execution, Persistence, Privilege Escalation & Container Escape

## 1. Statutory Baseline & Technical Control Matrix

### 1.1 Architecture & Governance Alignment

Financial container platforms operate under regulatory mandates demanding defense-in-depth, immutable telemetry trails, and continuous behavioral inspection. Regulatory baselines including the Financial Supervisory Commission (FSC) Cloud and Container Security Framework, ISO/IEC 27001:2022 Controls A.8.20 (Network Security), A.8.24 (Use of Cryptography), and A.8.28 (Secure Coding), NIST SP 800-190 (Application Container Security Guide), and CIS Kubernetes and Docker Benchmarks mandate that containerized workloads enforce kernel-isolated boundaries, verified image provenance, and real-time behavioral tracing.

Container runtime environments introduce distinct operational failure modes absent in traditional virtual machines. Shared host kernels, dynamic overlay networks, ephemeral container lifecycles, and declarative orchestrator APIs broaden the attack surface. Threat actors target exposed control planes, excessive Linux capabilities, unsegmented service accounts, and host volume mounts to execute lateral movement and host breakouts. To mitigate these risks deterministically, financial engineering baselines define four quantitative telemetry verification metrics:

1. Mean Time to Detect (MTTD): Target <= 5 minutes for Critical (T0) and High (T1) threat tiers across orchestration and runtime planes.
2. Mean Time to Remediate (MTTR): Target <= 15 minutes for automated container isolation, process termination, and credential revocation.
3. False Positive Ratio (FPR): Target <= 3.0% across all production Cloud Workload Protection Platform (CWPP) and SIEM detection rules.
4. Telemetry Ingestion Lag: Target <= 30 seconds from kernel system call execution to centralized SIEM event ingestion.

### 1.2 Master Matrix: Initial Access, Execution, Persistence, Privilege Escalation & Escape

The table below documents 20 leaf-node TTPs across Initial Access, Execution, Persistence, Privilege Escalation, and Container Breakout:

| TTP ID | Threat Tier | Technique Name | Tactic | Data Components | CWPP & Cloud Signature | Baseline Exception & Whitelist Policy |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| T1036.005 | T2 (Medium) | Masquerading: Match Legitimate Name | Defense Evasion | DC0028, DC0034 | Defender: Executable detected; Google: modified binary | Exclude verified system controllers deployed via GitOps. |
| T1036.010 | T2 (Medium) | Masquerading: Masquerade Account | Defense Evasion | DC0014, DC0028 | GuardDuty: UnauthorizedAccess:IAM; RHACS: Account Anomaly | Exclude authorized IAM directory synchronization accounts. |
| T1046 | T3 (Low) | Network Service Discovery | Discovery | DC0032, DC0082 | GuardDuty: Recon:EC2/Portscan; Google: port_scan | Exclude approved network vulnerability scanners and mesh probes. |
| T1053.007 | T1 (High) | Container Cronjob | Execution, Persistence | DC0001, DC0072 | GuardDuty: AnomalousBehavior; Defender: CronJob anomaly | Exclude scheduled batch processing jobs managed by central CI/CD. |
| T1059.013 | T2 (Medium) | Container Admin Tool | Execution | DC0077, DC0072 | GuardDuty: SuspiciousTool; Defender: Tool in container | Exclude designated administrative bastion pods and build runners. |
| T1068 | T0 (Critical) | Exploitation for Privilege Escalation | Privilege Escalation | DC0091, DC0032 | GuardDuty: RuncContainerEscape; RHACS: PrivEsc Attempt | Zero production workload exemptions permitted. |
| T1078.001 | T2 (Medium) | Default Accounts | Initial Access, Persistence | DC0002, DC0028 | GuardDuty: AnonymousAccess; Defender: Anonymous user | Exclude unauthenticated readiness probes (/healthz, /livez). |
| T1078.003 | T2 (Medium) | Local Accounts | Initial Access, Persistence | DC0002, DC0064 | Defender: Local account logon; GuardDuty: UnauthorizedAccess | Exclude bootstrap automation during declared maintenance windows. |
| T1098.006 | T1 (High) | Additional Cluster Roles | Persistence, PrivEsc | DC0010, DC0028 | GuardDuty: RoleBindingCreated; Defender: Elevated RBAC | Exclude automated deployments executed by authorized CI/CD agents. |
| T1110.001 | T2 (Medium) | Password Guessing | Credential Access | DC0002, DC0064 | GuardDuty: SSHBruteForce; Defender: Brute force attack | Exclude synthetic external connectivity monitoring probes. |
| T1110.003 | T2 (Medium) | Password Spraying | Credential Access | DC0002, DC0028 | Defender: Password spray; GuardDuty: CredentialAccess | Exclude centralized password rotation verification workflows. |
| T1110.004 | T2 (Medium) | Credential Stuffing | Credential Access | DC0002, DC0088 | Defender: High volume login failure; Google: cred_stuffing | Exclude corporate vulnerability scanners during test windows. |
| T1133 | T1 (High) | External Remote Services | Initial Access, Persistence | DC0088, DC0082 | GuardDuty: ExposedDashboard; Defender: Exposed API | Exclude edge ingress controllers restricted by IP allowlists. |
| T1136.001 | T2 (Medium) | Local Account Creation | Persistence | DC0064, DC0040 | GuardDuty: SensitiveFileModified; RHACS: Local Account | Exclude base container image build pipelines in CI runners. |
| T1190 | T2 (Medium) | Exploit Public Application | Initial Access | DC0032, DC0028 | GuardDuty: AnomalousProcess; Defender: Web command injection | Exclude authorized penetration testing exercises. |
| T1204.003 | T2 (Medium) | Malicious Image Execution | Execution | DC0072, DC0015 | GuardDuty: MaliciousFile; Defender: Malicious image | Exclude local developer test sandboxes isolated from core banking. |
| T1543.005 | T1 (High) | Create Systemd Service on Host | Persistence | DC0040, DC0064 | GuardDuty: SystemdServiceCreated; RHACS: Service Modified | Exclude automated host configuration daemons (Ansible, Puppet). |
| T1609 | T1 (High) | Container Administration Command | Execution | DC0072, DC0064 | GuardDuty: ExecInContainer; Defender: Exec into pod | Exclude authorized break-glass sessions with signed tickets. |
| T1610 | T1 (High) | Deploy Container Workload | Execution, Persistence | DC0028, DC0072 | GuardDuty: RogueWorkloadCreated; Defender: Pod without GitOps | Exclude automated CI/CD deployment pipelines. |
| T1611 | T0 (Critical) | Escape to Host (Container Breakout) | Privilege Escalation | DC0034, DC0064 | GuardDuty: ContainerEscape; Defender: Breakout detected | Zero production workload exemptions permitted. |

### 1.3 Tactical Deep Dive & Detection as Code Specifications

#### 1.3.1 Initial Access & External Ingress

##### T1190: Exploit Public-Facing Application
- Threat Tier: T2 (Medium) | Data Components: DC0032 (network flow), DC0028 (K8s API)
- CWPP Runtime Detection Logic: Correlates ingress web exploit signatures with unexpected child process execution (e.g., Java runtime or Nginx spawning `/bin/sh`, `/bin/bash`, or `python3`).
- Cloud Alert Signatures: AWS (GuardDuty: Execution:Runtime/AnomalousProcess), Azure (Defender: Web application command injection), GCP (CTD: web_rce_detected), Red Hat (ACS: Web Shell Process Execution), IBM (SCC: Ingress Exploit Alert).
- Whitelist Exception Criteria: Exclude authorized penetration testing exercises with pre-registered change requests.

```yaml
title: Web Application Process Spawn in Container Workload
logsource:
  category: process_creation
  product: linux
detection:
  selection_parent:
    ParentImage|endswith: ['/java', '/nginx', '/httpd', '/node', '/php-fpm']
  selection_child:
    Image|endswith: ['/sh', '/bash', '/dash', '/zsh', '/python', '/python3', '/perl']
  condition: selection_parent and selection_child
falsepositives:
  - Container entrypoint initialization scripts
level: high
tags: [attack.initial_access, attack.t1190]
```

##### T1133: External Remote Services
- Threat Tier: T1 (High) | Data Components: DC0088 (K8s audit), DC0082 (network flow)
- CWPP Runtime Detection Logic: Identifies exposure of Kubernetes API server (`6443`), Kubelet port (`10250`), or cluster dashboard directly to public 0.0.0.0/0 IP ranges without mutual TLS or IP restriction.
- Cloud Alert Signatures: AWS (GuardDuty: Policy:Kubernetes/ExposedDashboard), Azure (Defender: Publicly exposed Kubernetes API), GCP (SCC: open_k8s_api_server), Red Hat (ACS: Exposed Control Plane), IBM (SCC: Public NodePort Exposure).
- Whitelist Exception Criteria: Exclude edge ingress controllers protected by WAF and explicit corporate CIDR restrictions.

```yaml
title: Public Exposure of Kubernetes Control Plane Services
logsource:
  category: network_connection
  product: kubernetes
detection:
  selection_service:
    dest_port: [6443, 8443, 10250, 10255, 2379]
  selection_ingress:
    src_ip|cidr: ['0.0.0.0/0']
  filter_internal:
    src_ip|cidr: ['10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16']
  condition: selection_service and selection_ingress and not filter_internal
falsepositives:
  - Authorized managed cloud public API endpoints with IAM certificate authentication
level: high
tags: [attack.initial_access, attack.persistence, attack.t1133]
```

#### 1.3.2 Execution & Interactive Commands

##### T1609: Container Administration Command
- Threat Tier: T1 (High) | Data Components: DC0072 (K8s API), DC0064 (eBPF syscalls)
- CWPP Runtime Detection Logic: Catches `kubectl exec`, `crictl exec`, or `docker exec` operations initiated against production pods. Flags interactive bash sessions spawned in critical banking namespaces.
- Cloud Alert Signatures: AWS (GuardDuty: Execution:Kubernetes/ExecInContainer), Azure (Defender: Exec into pod detected), GCP (SCC: k8s_exec_into_pod), Red Hat (ACS: Pod Interactive Shell Session), IBM (SCC: Container Exec Anomaly).
- Whitelist Exception Criteria: Exclude verified emergency break-glass sessions with approved change management tickets.

```yaml
title: Interactive Command Execution in Container Workload
logsource:
  category: kubernetes_audit
  product: kubernetes
detection:
  selection_exec:
    verb: 'create'
    objectRef.subresource: 'exec'
  selection_commands:
    requestObject.command: ['/bin/sh', '/bin/bash', 'sh', 'bash', 'dash']
  filter_system:
    objectRef.namespace: ['kube-system', 'monitoring']
  condition: selection_exec and selection_commands and not filter_system
falsepositives:
  - Liveness and readiness exec probes configured in workload manifests
level: high
tags: [attack.execution, attack.t1609]
```

##### T1059.013: Command and Scripting: Container Admin Tool
- Threat Tier: T2 (Medium) | Data Components: DC0077 (docker events), DC0072 (K8s API)
- CWPP Runtime Detection Logic: Hooks process execution inside containers to flag invocations of container runtime and cluster management binaries (`kubectl`, `crictl`, `docker`, `podman`, `nerdctl`).
- Cloud Alert Signatures: AWS (GuardDuty: Execution:Runtime/SuspiciousTool), Azure (Defender: Management tool launched inside container), GCP (CTD: container_management_binary_executed), Red Hat (ACS: CLI Tool Inside Pod).
- Whitelist Exception Criteria: Exclude designated CI/CD build runner pods isolated in build namespaces.

```yaml
title: Container Management CLI Execution in Microservice Pod
logsource:
  category: process_creation
  product: linux
detection:
  selection_cli:
    Image|endswith: ['/kubectl', '/crictl', '/docker', '/podman', '/nerdctl', '/buildah']
  filter_runners:
    container.namespace: ['ci-runners', 'build-system']
  condition: selection_cli and not filter_runners
falsepositives:
  - Dedicated deployment orchestrator pods
level: medium
tags: [attack.execution, attack.t1059.013]
```

#### 1.3.3 Persistence & Account Manipulation

##### T1098.006: Account Manipulation: Additional Cluster Roles
- Threat Tier: T1 (High) | Data Components: DC0010 (K8s audit), DC0028 (K8s API)
- CWPP Runtime Detection Logic: Inspects Kubernetes audit trails for creation or modification of `ClusterRoleBinding` and `RoleBinding` resources delegating `cluster-admin` privileges or wildcard (`*`) permissions to service accounts.
- Cloud Alert Signatures: AWS (GuardDuty: PrivilegeEscalation:Kubernetes/RoleBindingCreated), Azure (Defender: Elevated RBAC binding created), GCP (SCC: cluster_admin_role_assigned), Red Hat (ACS: High Privilege Role Assigned).
- Whitelist Exception Criteria: Exclude GitOps continuous delivery service accounts updating versioned declarative manifests.

```yaml
title: Cluster Administrator Role Delegation to Workload ServiceAccount
logsource:
  category: kubernetes_audit
  product: kubernetes
detection:
  selection_verb:
    verb: ['create', 'patch', 'update']
    objectRef.resource: ['clusterrolebindings', 'rolebindings']
  selection_role:
    requestObject.roleRef.name: ['cluster-admin', 'admin']
  filter_gitops:
    user.username: ['system:serviceaccount:gitops:argo-cd', 'system:serviceaccount:flux:flux-admin']
  condition: selection_verb and selection_role and not filter_gitops
falsepositives:
  - Infrastructure bootstrap automation
level: critical
tags: [attack.persistence, attack.privilege_escalation, attack.t1098.006]
```

##### T1610: Deploy Container Workload
- Threat Tier: T1 (High) | Data Components: DC0028 (K8s API), DC0072 (K8s events)
- CWPP Runtime Detection Logic: Detects direct pod, DaemonSet, or deployment creation initiated outside authorized CI/CD GitOps controllers. Identifies deployment of images with unverified registries.
- Cloud Alert Signatures: AWS (GuardDuty: Persistence:Kubernetes/RogueWorkloadCreated), Azure (Defender: Pod created without GitOps), GCP (SCC: rogue_workload_deployed), Red Hat (ACS: Untrusted Workload Deployment).
- Whitelist Exception Criteria: Exclude certified CI/CD pipeline automation identities.

```yaml
title: Direct Workload Deployment Bypassing GitOps Controller
logsource:
  category: kubernetes_audit
  product: kubernetes
detection:
  selection_create:
    verb: 'create'
    objectRef.resource: ['pods', 'daemonsets', 'deployments']
  filter_controllers:
    user.username|startswith: ['system:serviceaccount:kube-system:', 'system:serviceaccount:argocd:']
  condition: selection_create and not filter_controllers
falsepositives:
  - Developer sandbox cluster provisioning
level: high
tags: [attack.persistence, attack.execution, attack.t1610]
```

#### 1.3.4 Privilege Escalation & Container Breakout

##### T1611: Escape to Host (Container Breakout)
- Threat Tier: T0 (Critical) | Data Components: DC0034 (containerd runtime), DC0064 (eBPF syscalls)
- CWPP Runtime Detection Logic: Detects runtime container escape mechanisms including sensitive hostPath volume mounts (`/`, `/etc`, `/var/run/docker.sock`), execution of `nsenter` targeting host PID 1, abuse of `CAP_SYS_ADMIN` or `CAP_SYS_PTRACE`, and overwriting host `/sys` or `/proc` filesystems.
- Cloud Alert Signatures: AWS (GuardDuty: PrivilegeEscalation:Runtime/ContainerEscape), Azure (Defender: Container breakout detected), GCP (CTD: container_escape_attempt), Red Hat (ACS: Container Breakout Detected), IBM (SCC: Host Isolation Breach).
- Whitelist Exception Criteria: Zero production workload exemptions permitted.

```yaml
title: Privileged Container Host Escape Attempt via Sensitive Mount
logsource:
  category: process_creation
  product: linux
detection:
  selection_escape:
    Image|endswith: ['/nsenter', '/chroot']
    CommandLine|contains: ['--target 1', '-t 1', '/host', '/proc/1/ns']
  selection_sock:
    CommandLine|contains: ['docker.sock', 'containerd.sock']
  condition: selection_escape or selection_sock
falsepositives:
  - None (Zero production workload exemption)
level: critical
tags: [attack.privilege_escalation, attack.t1611]
```

##### T1068: Exploitation for Privilege Escalation
- Threat Tier: T0 (Critical) | Data Components: DC0091 (containerd), DC0032 (eBPF syscalls)
- CWPP Runtime Detection Logic: Intercepts kernel privilege escalation exploits including dirty COW, unshare user namespace invocations, and cgroup `release_agent` abuse executed inside container boundaries.
- Cloud Alert Signatures: AWS (GuardDuty: PrivilegeEscalation:Runtime/RuncContainerEscape), Azure (Defender: Kernel exploit attempt in pod), GCP (CTD: kernel_privilege_escalation), Red Hat (ACS: Privilege Escalation Attempt).
- Whitelist Exception Criteria: Zero production workload exemptions permitted.

```yaml
title: Kernel Privilege Escalation via User Namespace and Release Agent Abuse
logsource:
  category: process_creation
  product: linux
detection:
  selection_cgroup:
    CommandLine|contains: ['release_agent', 'notify_on_release', 'devices.allow']
  selection_unshare:
    Image|endswith: ['/unshare']
    CommandLine|contains: ['-U', '-r', '--user']
  condition: selection_cgroup or selection_unshare
falsepositives:
  - None
level: critical
tags: [attack.privilege_escalation, attack.t1068]
```

---

## 2. Production Incident & Remediation Architecture

### 2.1 Attack Chain Topology: Payment Gateway Microservice Breakout

The incident below details an attack chain executing remote code execution, token harvesting, privilege escalation, and host breakout on an unhardened financial cluster:

```
+---------------------------------------------------------------------------------+
| 1. Ingress Exploit & Initial Access                                             |
|    HTTP Request with Spring4Shell Exploit -> Web Shell Injected (T1190)         |
|                                      |                                          |
| 2. Credential Access & Reconnaissance                                           |
|    Workload Reads Auto-Mounted ServiceAccount Token (T1078.001)                 |
|    Probes API Server & RBAC Permissions (T1046, T1069)                          |
|                                      |                                          |
| 3. RBAC Privilege Escalation & Persistence                                      |
|    Creates ClusterRoleBinding Delegating cluster-admin (T1098.006)              |
|    Deploys Rogue Privileged DaemonSet "telemetry-agent" (T1610)                 |
|                                      |                                          |
| 4. Host Breakout & Node Control                                                 |
|    Mounts Host /var/run/docker.sock and hostPath / (T1611)                      |
|    Spawns Root Shell on Host Node via nsenter (T1609, T1611)                    |
+---------------------------------------------------------------------------------+
```

#### Attack Phase Decomposition:
- Phase 1 (Initial Access): The threat actor identifies an unpatched payment microservice vulnerable to Spring4Shell (CVE-2022-22965), delivering a serialized payload to spawn a remote web shell.
- Phase 2 (Credential Access): Inside the container, the attacker accesses the default ServiceAccount token at `/var/run/secrets/kubernetes.io/serviceaccount/token`. The namespace retained default token automounting.
- Phase 3 (Privilege Escalation): The attacker discovers overly broad RBAC permissions and creates a `ClusterRoleBinding` granting `cluster-admin` to the compromised identity.
- Phase 4 (Persistence & Breakout): The attacker deploys a rogue privileged DaemonSet with `hostPath: /` and `privileged: true`, using `nsenter` to break out into host PID 1.

### 2.2 Root-Cause Defect Decomposition

1. Absence of Admission Control: Admission webhooks did not enforce Pod Security Standards (PSS), permitting workloads with `privileged: true` and sensitive `hostPath` mounts.
2. Unsegmented Service Account Tokens: Default namespaces automatically mounted ServiceAccount tokens, allowing microservices to authenticate to the Kubernetes API.
3. RBAC Privilege Drift: ServiceAccounts held permissions across cluster roles, violating least-privilege boundaries.
4. Telemetry Gap: Absence of eBPF kernel tracing allowed web shell execution and container escape attempts to proceed undetected.

### 2.3 Defense-in-Depth Hardening Architecture

```
Layer 1: CI/CD Build Gate (Static Analysis, CVE Block, Image Signing via Cosign)
   │
Layer 2: Admission Controller (OPA Gatekeeper Enforces Restricted Pod Security)
   │
Layer 3: Runtime Inspection (eBPF Sensor Hooks Syscalls, Detects nsenter & Breakouts)
   │
Layer 4: Network Microsegmentation (CNI NetworkPolicies Restrict API & IMDS Ingress)
```

Declarative OPA Gatekeeper Policy preventing privileged containers and sensitive volume mounts:

```yaml
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sPSPContainerSecurity
metadata:
  name: enforce-pod-hardening
spec:
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
    namespaces: ["production", "payment", "banking"]
  parameters:
    privileged: false
    allowPrivilegeEscalation: false
    allowedHostPaths: []
    readOnlyRootFilesystem: true
```

---

## 3. Exam Question Bank & Distractor Forensics

### Question 1: Operational Sequence (FIRST Action)
During runtime telemetry inspection of a financial transaction cluster, a Security Operations Center (SOC) analyst observes an alert indicating that a microservice in the `payment-prod` namespace executed `kubectl exec` to spawn an interactive `/bin/sh` shell (T1609), followed by reading `/var/run/secrets/kubernetes.io/serviceaccount/token` (T1078.001). Under the statutory incident response framework, which action must the SOC analyst execute FIRST?

- A. Manually delete the affected node from the cluster to force workload eviction.
- B. Quarantine the compromised pod via NetworkPolicy isolation and revoke the associated ServiceAccount token.
- C. Initiate a multi-region disaster recovery failover of all transaction databases.
- D. Modify the cluster-wide OPA Gatekeeper constraint to block all container creation requests.

#### Distractor Forensics:
- Option B is the CORRECT answer. Immediate network quarantine of the pod combined with ServiceAccount token revocation halts active command-and-control channels and prevents lateral movement while preserving container memory for forensics.
- Option A is incorrect. Deleting the node forces Kubernetes to reschedule the compromised pod onto another healthy node, spreading the infection and destroying memory evidence.
- Option C is incorrect. Multi-region database failover causes massive banking downtime and does not address the active container compromise.
- Option D is incorrect. Changing Gatekeeper admission policies affects future deployments but does not terminate or isolate the currently running rogue container.

---

### Question 2: Architectural Optimization (BEST/MOST Effective Control)
A banking institution is migrating its core ledger microservices to a managed Kubernetes cluster. To prevent threat actors from exploiting container breakouts (`T1611`) and escalating privileges via host namespace abuse (`T1068`), which architectural control combination provides the MOST effective defense?

- A. Increasing CloudWatch log retention to 365 days and deploying static anti-virus agents on worker nodes.
- B. Enforcing OPA Gatekeeper Restricted Pod Security Standards, disabling hostPath mounts, and deploying eBPF runtime sensors.
- C. Running containers with root user privileges while implementing perimeter firewall rules.
- D. Storing ServiceAccount credentials in plain text ConfigMaps to avoid token mount overhead.

#### Distractor Forensics:
- Option B is the CORRECT answer. Combining declarative admission gating (Restricted PSS, blocking privileged containers and hostPath mounts) with eBPF runtime sensors provides preventative guardrails and real-time behavioral containment against container breakouts.
- Option A is incorrect. Static host anti-virus tools fail to inspect container namespaces and eBPF syscalls, while log retention provides historical analysis rather than active prevention.
- Option C is incorrect. Running containers as root directly enables privilege escalation and host escape vulnerabilities.
- Option D is incorrect. Storing credentials in plain text ConfigMaps violates basic secret management standards and exposes credentials to unauthorized read operations.

---

### Question 3: Incident Response Pipeline (NEXT Step)
Following the successful containment of a rogue DaemonSet deployment (`T1610`) in a payment processing cluster, the security engineering team confirmed that the rogue workload attempted to mount `/var/run/docker.sock` to escape to the host (`T1611`). Which engineering remediation step should the team execute NEXT?

- A. Grant cluster-admin privileges to the application namespace to simplify debugging.
- B. Audit all ClusterRoleBindings, remove unneeded wildcard permissions, and mandate GitOps pull-request enforcement for workload manifests.
- C. Disable all audit logging on the cluster to improve node CPU throughput.
- D. Deploy an unauthenticated public ingress controller to monitor incoming traffic.

#### Distractor Forensics:
- Option B is the CORRECT answer. Reviewing RBAC assignments, removing excessive permissions, and enforcing GitOps deployment gates remediates the root vulnerabilities that allowed unauthorized DaemonSet creation.
- Option A is incorrect. Granting cluster-admin permissions exacerbates privilege escalation risks and directly violates least-privilege standards.
- Option C is incorrect. Disabling audit logging eliminates regulatory auditability and forensic traceability, violating statutory requirements.
- Option D is incorrect. Exposing an unauthenticated ingress controller creates an ingress attack vector (T1133).

---

### Question 4: Architectural Boundary (PRIMARY/EXCEPT Analysis)
When implementing a container security baseline across financial production workloads, all of the following engineering practices represent valid, standard-compliant hardening controls EXCEPT:

- A. Granting the `CAP_SYS_ADMIN` capability and setting `privileged: true` on production microservice containers to enable internal debugging.
- B. Disabling automatic ServiceAccount token mounting (`automountServiceAccountToken: false`) on pods that do not require API interaction.
- C. Restricting egress traffic from container worker nodes to the cloud Instance Metadata Service (IMDS) via network policies.
- D. Enforcing cryptographic image signature verification at the admission controller stage using Cosign.

#### Distractor Forensics:
- Option A is the CORRECT answer (the invalid practice to identify). Granting `CAP_SYS_ADMIN` and `privileged: true` disables kernel isolation barriers, giving the workload root access to host hardware and enabling container escape (`T1611`).
- Option B is incorrect (valid control). Disabling token automounting enforces least privilege and mitigates token theft (`T1078.001`).
- Option C is incorrect (valid control). Blocking IMDS egress prevents compromised workloads from stealing cloud IAM credentials.
- Option D is incorrect (valid control). Cryptographic signature verification guarantees container image provenance (`T1204.003`).
