# Chapter 2: Container Threat Behaviors & MITRE ATT&CK Mapping

## 1. Statutory Baseline & Technical Control Matrix

### 1.1 Architecture & Governance Alignment

Financial container platforms operate under regulatory mandates demanding defense-in-depth, immutable telemetry trails, and continuous behavioral inspection. Regulatory baselines including the Financial Supervisory Commission (FSC) Cloud & Container Security Framework, ISO/IEC 27001:2022 Controls A.8.20 (Network Security), A.8.24 (Use of Cryptography), and A.8.28 (Secure Coding), NIST SP 800-190 (Application Container Security Guide), and Center for Internet Security (CIS) Benchmarks for Docker and Kubernetes mandate that containerized workloads enforce hardware-isolated boundaries, verified provenance, and real-time behavioral tracing.

Container runtime environments introduce distinct architectural failure modes absent in traditional virtual machines. Shared host kernels, dynamic overlay networks, short container lifecycles, and automated orchestration APIs broaden the attack surface. Threat actors exploit misconfigurations, excessive Linux capabilities, and leaked service account tokens to execute lateral movement and host breakouts. To mitigate these risks deterministically, financial engineering standards require quantitative telemetry verification across four core metrics:

1. Mean Time to Detect (MTTD): Target <= 5 minutes for Critical (T0) and High (T1) threat tiers across orchestration and runtime planes.
2. Mean Time to Remediate (MTTR): Target <= 15 minutes for automated container isolation, process termination, and credential revocation.
3. False Positive Ratio (FPR): Target <= 3.0% across all production Cloud Workload Protection Platform (CWPP) and Security Information and Event Management (SIEM) detection rules.
4. Telemetry Ingestion Lag: Target <= 30 seconds from container runtime event generation to centralized SIEM index ingestion.

The operational baseline categorizes all container threats into four severity tiers: Tier T0 (Critical, involving host breakout, cluster control plane compromise, or irreversible data destruction), Tier T1 (High, involving credential theft, privilege escalation, and unauthorized container deployment), Tier T2 (Medium, involving defense evasion, internal network probing, and brute force attempts), and Tier T3 (Low, involving local resource discovery and compute overhead anomalies).

### 1.2 Telemetry Taxonomy & Detection Category Distribution

Comprehensive threat detection across containerized environments relies on a six-category defense taxonomy combining preventative admission controls, managed cloud audit trails, host kernel hooks, and centralized analytical correlation:

- Category 1 (Native Log Custom Detection Rules): Custom detection signatures derived from native Linux system logs, Docker daemon events, containerd telemetry, and Kubernetes API audit logs, formatted into portable Sigma and YARA-L rules.
- Category 2 (CWPP Native Behavioral Detections): Out-of-the-box runtime detection engines powered by kernel probes and extended Berkeley Packet Filter (eBPF) tracing, supplied by cloud-native tools such as AWS GuardDuty Runtime Monitoring, Microsoft Defender for Containers, Google Cloud Security Command Center (SCC) Container Threat Detection (CTD), IBM Cloud Security and Compliance Center (SCC), and Red Hat Advanced Cluster Security (RHACS).
- Category 3 (Managed Cloud Control Plane Audit Logic): Analytical detection logic operating on cloud control plane telemetry including AWS CloudTrail, Azure Activity Logs, and Google Cloud Audit Logs to identify identity abuse and resource tampering.
- Category 4 (Infrastructure & Architectural Mitigations): Protective constraints established through platform architecture. This category subdivides into Absolute Exclusions (where managed control plane nodes eliminate direct host attack vectors) and Conditional Exclusions (where perimeter firewalls, cloud security groups, and web application firewalls intercept ingress vectors).
- Category 5 (Native Tunable Security Policies): Dynamic admission control policies and declarative runtime constraints enforced via Kubernetes Admission Webhooks, Pod Security Standards (PSS), Open Policy Agent (OPA) Gatekeeper, Kyverno, and Red Hat ACS policy rules.
- Category 6 (Enterprise SIEM Correlated Rules): Cross-source correlation rules deployed in centralized platforms including Microsoft Sentinel, Splunk ES, IBM QRadar, Google SecOps, and Micro Focus ArcSight to detect multi-stage attack chains.

The baseline maps 36 Leaf-Node Tactics, Techniques, and Procedures (TTPs) defined in the MITRE ATT&CK for Containers matrix across these six categories. The table below outlines the distribution of detection capabilities across supported enterprise platforms:

| Container Platform / Vendor | Cat 1: Custom Native Logs | Cat 2: CWPP Native Alerts | Cat 3: Managed Log Logic | Cat 4: Absolute Architecture Exclusions | Cat 4: Conditional Architecture Exclusions | Cat 5: Native Tunable Policies | Total TTPs Covered |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Docker / Kubernetes (Self-Hosted) | 36 | 0 | 0 | 0 | 0 | 0 | 36 |
| Red Hat OpenShift (RHACS) | 0 | 15 | 0 | 0 | 0 | 21 | 36 |
| Amazon Web Services (EKS / ECS) | 0 | 23 | 5 | 1 | 7 | 0 | 36 |
| Microsoft Azure (AKS) | 0 | 25 | 0 | 0 | 11 | 0 | 36 |
| Google Cloud (GKE) | 0 | 33 | 0 | 1 | 2 | 0 | 36 |
| IBM Cloud (IKS / ROKS) | 0 | 35 | 0 | 1 | 0 | 0 | 36 |

### 1.3 Master MITRE ATT&CK for Containers TTP Matrix

The following matrix documents the complete inventory of 36 container TTPs, defining tactical alignment, threat tiering, telemetry data components, MITRE detection strategies, CWPP runtime inspection logic, native cloud alerting signatures, and baseline exception rules:

| TTP ID | Threat Tier | Technique Name | Primary Tactic | Data Components | Detection Strategy & Rule | CWPP Runtime Detection Logic | Cloud CWPP Rule Signature | Exception & Whitelist Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| T1036.005 | T2 (Medium) | Masquerading: Match Legitimate Resource Name | Defense Evasion | DC0028 (K8s API), DC0034 (containerd) | DET0347, AN0986 | Compares resource metadata names against namespaces; alerts when system prefixes appear outside system namespaces. | Defender: Executable detected in cmdline; Google: modified malicious binary | Exclude verified system controllers deployed via GitOps in core namespaces. |
| T1036.010 | T2 (Medium) | Masquerading: Masquerade Account Name | Defense Evasion | DC0014 (docker daemon), DC0028 (K8s API) | DET0383, AN1080 | Identifies creation of user accounts or service accounts mimicking internal system account nomenclature. | GuardDuty: UnauthorizedAccess:IAMUser; RHACS: User Account Anomaly | Exclude authorized IAM directory synchronization service accounts. |
| T1046 | T3 (Low) | Network Service Discovery | Discovery | DC0032 (eBPF syscalls), DC0082 (network flow) | DET0376, AN1060 | Hooks connect() and socket() syscalls to catch rapid sequential SYN probes across RFC 1918 internal subnets. | GuardDuty: Recon:EC2/Portscan; Google CTD: port_scan_detected | Exclude approved network discovery scanners and service mesh health probes. |
| T1053.007 | T1 (High) | Scheduled Task/Job: Container Cronjob | Execution, Persistence | DC0001 (K8s API), DC0072 (K8s events) | DET0206, AN0582 | Monitors Kubernetes CronJob creations executing inline shell scripts, curl commands, or network downloads. | GuardDuty: Execution:Kubernetes/AnomalousBehavior; Defender: Kubernetes CronJob anomaly | Exclude scheduled batch processing jobs managed by central CI/CD. |
| T1059.013 | T2 (Medium) | Command and Scripting: Container Admin Tool | Execution | DC0077 (docker events), DC0072 (K8s API) | DET0083, AN0233 | Intercepts execution of docker, podman, crictl, or kubectl CLI binaries from inside container workloads. | GuardDuty: Execution:Runtime/SuspiciousTool; Defender: Tool launched inside container | Exclude designated administrative bastion pods and build runner workers. |
| T1068 | T0 (Critical) | Exploitation for Privilege Escalation | Privilege Escalation | DC0091 (containerd runtime), DC0032 (eBPF) | DET0514, AN1422 | Catches kernel exploitation including dirty COW, unshare user namespace, and cgroup release_agent overwrites. | GuardDuty: PrivilegeEscalation:Runtime/RuncContainerEscape; RHACS: Privilege Escalation Attempt | Zero production workload exemptions permitted. |
| T1069 | T3 (Low) | Permission Groups Discovery | Discovery | DC0064 (K8s audit), DC0028 (K8s API) | DET0179, AN0491 | Flags rapid API enumeration of ClusterRoles, ClusterRoleBindings, and RoleBindings by non-admin identities. | Defender: Kubernetes RBAC enumeration; Google: discovery_api_query | Exclude continuous compliance audit operators (Gatekeeper, Falco exporters). |
| T1070 | T0 (Critical) | Indicator Removal | Defense Evasion | DC0040 (docker daemon), DC0059 (eBPF) | DET0184, AN0523 | Alerts on modification or truncation of /var/log, shell history zeroing, or stopping auditing daemons. | GuardDuty: DefenseEvasion:Runtime/SuspiciousCommand; RHACS: Log Tampering Detected | Exclude automated log rotation daemons (logrotate, fluentbit cleanup). |
| T1078.001 | T2 (Medium) | Valid Accounts: Default Accounts | Initial Access, Persistence | DC0002 (K8s audit), DC0028 (K8s API) | DET0465, AN1279 | Alerts on requests initiated using default service accounts or system:anonymous credentials against API server. | GuardDuty: Policy:Kubernetes/AnonymousAccessGranted; Defender: Anonymous user request | Exclude public unauthenticated readiness probe endpoints (/healthz, /livez). |
| T1078.003 | T2 (Medium) | Valid Accounts: Local Accounts | Initial Access, Persistence | DC0002 (K8s audit), DC0064 (host auth) | DET0407, AN1120 | Detects authentication using local node accounts instead of central federated enterprise identity providers. | Defender: Local account logon to cluster node; GuardDuty: UnauthorizedAccess:EC2 | Exclude initial bootstrap automation during declared maintenance windows. |
| T1098.006 | T1 (High) | Account Manipulation: Additional Cluster Roles | Persistence, Privilege Escalation | DC0010 (K8s audit), DC0028 (K8s API) | DET0572, AN1579 | Tracks RBAC mutations granting cluster-admin or wildcard verbs to workloads outside kube-system. | GuardDuty: PrivilegeEscalation:Kubernetes/RoleBindingCreated | Exclude automated deployments executed by authorized CI/CD release agents. |
| T1110.001 | T2 (Medium) | Brute Force: Password Guessing | Credential Access | DC0002 (host auth), DC0064 (K8s audit) | DET0551, AN1498 | Tracks repeated failed authentication attempts against SSH node ports or container management interfaces. | GuardDuty: UnauthorizedAccess:EC2/SSHBruteForce; Defender: Brute force attack on node | Exclude synthetic external connectivity monitoring probes. |
| T1110.003 | T2 (Medium) | Brute Force: Password Spraying | Credential Access | DC0002 (K8s audit), DC0028 (K8s API) | DET0487, AN1341 | Identifies single password validation attempts distributed across multiple service accounts within short intervals. | Defender: Password spray detected; GuardDuty: CredentialAccess:IAMUser | Exclude centralized password rotation verification automated workflows. |
| T1110.004 | T2 (Medium) | Brute Force: Credential Stuffing | Credential Access | DC0002 (K8s API), DC0088 (ingress log) | DET0460, AN1268 | Correlates high-volume failed authentication attempts originating from known malicious threat proxy networks. | Defender: High volume login failure from suspicious IP; Google: credential_stuffing_attempt | Exclude corporate vulnerability scanners during announced test windows. |
| T1133 | T1 (High) | External Remote Services | Initial Access, Persistence | DC0088 (K8s audit), DC0082 (network flow) | DET0354, AN0998 | Identifies exposure of Kubernetes API server, kubelet port, or cluster dashboards directly to public Internet subnets. | GuardDuty: Policy:Kubernetes/ExposedDashboard; Defender: Publicly exposed Kubernetes API | Exclude explicitly authorized edge ingress controllers restricted by IP allowlists. |
| T1136.001 | T2 (Medium) | Create Account: Local Account | Persistence | DC0064 (eBPF syscalls), DC0040 (host logs) | DET0447, AN1239 | Hooks useradd, adduser, and chpasswd executions inside active running container filesystems. | GuardDuty: Persistence:Runtime/SensitiveFileModified; RHACS: Local Account Created in Pod | Exclude base container image build pipelines executed within ephemeral CI runners. |
| T1190 | T2 (Medium) | Exploit Public-Facing Application | Initial Access | DC0032 (network flow), DC0028 (K8s API) | DET0080, AN0222 | Correlates ingress web exploit attempts with subsequent child process generation (e.g., java spawning sh). | GuardDuty: Execution:Runtime/AnomalousProcess; Defender: Web application command injection | Exclude authorized penetration testing exercises with formal notification. |
| T1204.003 | T2 (Medium) | User Execution: Malicious Image | Execution | DC0072 (K8s API), DC0015 (containerd) | DET0248, AN0691 | Alerts on pods launching container images from public unvetted registries or with critical CVE vulnerabilities. | GuardDuty: Execution:Kubernetes/MaliciousFile; Defender: Malicious image detected | Exclude approved local developer test sandboxes isolated from banking data. |
| T1485 | T0 (Critical) | Data Destruction | Impact | DC0064 (docker events), DC0059 (eBPF) | DET0146, AN0416 | Catches mass file deletion, shredding commands (rm -rf /*, shred), or volume formatting inside workloads. | GuardDuty: Impact:Runtime/DataDestruction; RHACS: Mass File System Deletion Detected | Exclude automated ephemeral storage scratch directory cleanup operations. |
| T1490 | T0 (Critical) | Inhibit System Recovery | Impact | DC0064 (K8s audit), DC0028 (K8s API) | DET0329, AN0912 | Detects deletion of VolumeSnapshots, PersistentVolumeClaims, and automated backup controllers (e.g., Velero). | GuardDuty: Impact:Kubernetes/BackupDeleted; Defender: Cluster backup resource tampering | Exclude scheduled backup retention lifecycle pruning jobs executed by Velero. |
| T1496.001 | T3 (Low) | Resource Hijacking: Compute Hijacking | Impact | DC0072 (containerd), DC0085 (cgroups) | DET0540, AN1492 | Flags sustained 100% CPU thread consumption combined with Stratum cryptocurrency protocol DNS requests. | GuardDuty: CryptoCurrency:Runtime/BitcoinTool.B; Google CTD: cryptomining_detected | Exclude scheduled stress testing and mathematical risk simulations. |
| T1496.002 | T3 (Low) | Resource Hijacking: Bandwidth Hijacking | Impact | DC0085 (network metrics), DC0082 (flow logs) | DET0028, AN0083 | Identifies abnormal egress network traffic volumes towards external peer-to-peer or anonymized proxy endpoints. | GuardDuty: Behavior:EC2/TrafficVolumeUnusual; Defender: Large outbound data transfer | Exclude bulk cross-region database replication and snapshot archive backups. |
| T1498 | T2 (Medium) | Network Denial of Service | Impact | DC0032 (network metrics), DC0082 (flow logs) | DET0518, AN1430 | Detects rapid volumetric outbound UDP/TCP packet bursts generated from compromised pods targeting external hosts. | GuardDuty: Backdoor:EC2/DenialOfService.Udp; Defender: Outbound DDoS activity | Exclude load testing traffic generated from isolated load testing node pools. |
| T1499 | T2 (Medium) | Endpoint Denial of Service | Impact | DC0018 (K8s events), DC0038 (docker events) | DET0208, AN0588 | Catches fork bomb processes, memory exhaustion, or pod crashes degrading node-level kubelet stability. | Defender: High memory consumption exhausting host; Google CTD: container_exhaustion | Exclude JVM heap size warmup routines within configured cgroup limits. |
| T1525 | T0 (Critical) | Implant Internal Image | Persistence | DC0015 (docker daemon), DC0036 (registry) | DET0334, AN0946 | Detects unauthorized image pushes, tag overwrites, or tampering with base images in enterprise registries. | GuardDuty: Persistence:Kubernetes/SuspiciousImageUpdate; Defender: Image tampered in ACR | Exclude verified automated continuous deployment build pipeline accounts. |
| T1528 | T1 (High) | Steal Application Access Token | Credential Access | DC0055 (K8s audit), DC0028 (K8s API) | DET0515, AN1423 | Tracks access to Kubernetes Secret objects and subsequent API usage originating from external unauthorized IPs. | GuardDuty: CredentialAccess:Kubernetes/SecretsAccessed | Exclude authorized secret synchronizers (External Secrets Operator). |
| T1543.005 | T1 (High) | Create or Modify System Process: Container | Persistence, Privilege Escalation | DC0019 (K8s audit), DC0060 (containerd) | DET0473, AN1304 | Flags modification of static pod manifests (/etc/kubernetes/manifests) or installation of systemd container units. | GuardDuty: Persistence:Runtime/SuspiciousCommand; RHACS: Static Pod Manifest Created | Exclude standard Kubernetes cluster version upgrade automation procedures. |
| T1550.001 | T1 (High) | Alternate Auth Material: App Access Token | Credential Access, Lateral Movement | DC0007 (K8s API), DC0028 (K8s audit) | DET0185, AN0530 | Identifies API token reuse across discordant source subnets or anomalous user-agent signature mismatches. | Defender: Anomalous token replay detected; Google: anomalous_token_use | Exclude multi-region automated CI/CD runners using distributed workers. |
| T1552.001 | T1 (High) | Unsecured Credentials: Credentials In Files | Credential Access | DC0055 (eBPF syscalls), DC0064 (K8s audit) | DET0307, AN0859 | Intercepts unauthorized process access to /var/run/secrets/kubernetes.io/serviceaccount/token and .env files. | GuardDuty: CredentialAccess:Runtime/SensitiveFileRead; RHACS: Service Account Token Read | Exclude official application runtime initialization scripts accessing secrets. |
| T1552.007 | T1 (High) | Unsecured Credentials: Container API | Credential Access | DC0002 (K8s API), DC0032 (kubelet logs) | DET0198, AN0571 | Alerts on direct unauthenticated HTTP requests targeting kubelet read-only port 10255 or Docker daemon TCP sockets. | GuardDuty: CredentialAccess:Kubernetes/KubeletAPIQueried; Defender: Kubelet API abuse | Exclude cluster monitoring agents (cAdvisor, Prometheus node-exporter). |
| T1609 | T1 (High) | Container Administration Command | Execution | DC0032 (K8s API), DC0064 (docker daemon) | DET0112, AN0177 | Audits all kubectl exec, kubectl attach, and docker exec commands initiated into production running containers. | GuardDuty: Execution:Kubernetes/ExecIntoPod; Defender: Container interactive session started | Exclude pre-approved break-glass emergency troubleshooting sessions. |
| T1610 | T1 (High) | Deploy Container | Execution, Defense Evasion | DC0038 (K8s API), DC0085 (docker events) | DET0249, AN0693 | Detects ad-hoc container creation bypassing Kubernetes admission controllers or GitOps deployment pipelines. | GuardDuty: Execution:Kubernetes/WorkloadDeployed; RHACS: Unmanaged Pod Deployed | Exclude emergency operator deployments initiated by cluster administrator credentials. |
| T1611 | T0 (Critical) | Escape to Host | Privilege Escalation | DC0092 (K8s API), DC0072 (containerd) | DET0219, AN0612 | Detects breakout attempts via nsenter, privileged securityContext, Docker socket mount, or hostPath /. | GuardDuty: PrivilegeEscalation:Runtime/RuncContainerEscape; Google CTD: container_escape | Zero production workload exemptions permitted. |
| T1612 | T2 (Medium) | Build Image on Host | Persistence | DC0015 (docker daemon), DC0034 (containerd) | DET0459, AN1261 | Alerts on invocations of docker build, nerdctl build, or buildah executed inside Kubernetes worker node shells. | Defender: Image build command executed on host node; RHACS: Node Image Build Detected | Exclude dedicated container build worker nodes isolated in private build subnets. |
| T1613 | T3 (Low) | Container and Resource Discovery | Discovery | DC0037 (K8s API), DC0091 (docker daemon) | DET0388, AN1352 | Tracks extensive API querying of namespaces, pods, nodes, and configmaps by workload service accounts. | Defender: Discovery commands executed in container; Google CTD: resource_discovery | Exclude core cluster components (CoreDNS, kube-proxy, Ingress controllers). |
| T1685 | T1 (High) | Disable or Modify Tools | Defense Evasion | DC0041 (K8s audit), DC0064 (eBPF) | DET0497, AN1373 | Flags termination of security agent processes (Falco, GuardDuty agent, Defender daemonset) or eBPF unhooking. | GuardDuty: DefenseEvasion:Runtime/SecurityAgentTerminated; RHACS: Agent Disconnected | Zero production workload exemptions permitted. |

### 1.4 Deep CWPP Detection Logic by Tactical Domain

#### 1.4.1 Execution TTPs
Execution techniques within container workloads center on executing unauthorized code via orchestrator APIs, lifecycle hooks, or compromised images. For T1609 (Container Administration Command), the attack vector abuses the Kubernetes API server subresource `pods/exec` to spawn interactive shells within production workloads. CWPP detection logic intercepts this at two architectural planes: first, by auditing Kubernetes API Server audit logs for `verb=create` targeting `subresource=exec`, and second, by hooking kernel `execve()` calls via eBPF to detect unexpected binary executions (such as `/bin/sh` or `/bin/bash`) originating under container cgroup hierarchies whose entrypoint is a web server or database engine.

For T1053.007 (Container Cronjob) and T1059.013 (Container Administration Tool), attackers establish automated execution chains or execute internal container commands. CWPP monitoring inspects pod specification submissions, alerting on CronJobs embedding shell scripts or invoking administrative CLI tools (`kubectl`, `crictl`, `docker`). Whitelist controls isolate automated CI/CD runners and administrative maintenance pods, ensuring standard microservices cannot execute management utilities.

#### 1.4.2 Persistence TTPs
Adversaries establish persistence across container environments by implanting backdoored images, scheduling unauthorized workloads, or creating rogue accounts. T1525 (Implant Internal Image) involves pushing compromised layers to private container registries or poisoning base image repositories. CWPP and registry scanners detect this via cryptographic image digest verification, vulnerability scanning upon push, and admission webhooks blocking image deployments whose signatures fail Cosign or Notary verification.

T1612 (Build Image on Host) bypasses centralized image scanning by compiling container images directly on underlying worker nodes using `docker build` or `nerdctl build`. CWPP host agents identify this by tracing process execution trees on Kubernetes worker nodes, alerting whenever container compilation utilities execute outside isolated build pools. T1136.001 (Local Account) and T1543.005 (Create or Modify System Process) are detected through eBPF monitoring of filesystem write operations to `/etc/passwd`, `/etc/shadow`, and `/etc/kubernetes/manifests/`, immediately blocking static pod injections.

#### 1.4.3 Privilege Escalation TTPs
Privilege escalation within containerized architectures represents an immediate systemic risk. T1611 (Escape to Host) and T1068 (Exploitation for Privilege Escalation) allow adversaries to break container namespace and cgroup boundaries to achieve root privileges on the underlying node. CWPP detection monitors kernel exploitation signatures including unauthorized namespace transitions (`setns()`, `unshare()`), direct access to host devices (`/dev/mem`, `/dev/kmem`), modification of cgroup release agent scripts, and access to `/var/run/docker.sock` or `containerd.sock`.

T1098.006 (Additional Cluster Roles) targets the orchestration control plane by binding unprivileged service accounts to high-privilege ClusterRoles (such as `cluster-admin`). CWPP engines and SIEM rules parse Kubernetes audit logs for `verb=create` or `verb=patch` on `RoleBinding` and `ClusterRoleBinding` resources, raising critical alerts whenever non-admin identities perform RBAC assignments outside established deployment manifests.

#### 1.4.4 Discovery TTPs
Post-compromise discovery operations allow attackers to map cluster topology, internal subnets, and RBAC permissions. T1046 (Network Service Discovery) involves internal port scanning executed from compromised containers. CWPP eBPF network probes monitor socket creation and connection states, flagging rapid outbound TCP SYN packets directed at RFC 1918 private IP ranges or sequential internal cluster service endpoints.

T1613 (Container and Resource Discovery) and T1069 (Permission Groups Discovery) exploit default service account tokens to query the Kubernetes API server for running pods, namespaces, endpoints, and secrets. CWPP systems baseline normal API query frequencies for each microservice identity, triggering alerts upon abnormal spikes in `GET` and `LIST` API queries directed toward cluster metadata endpoints.

#### 1.4.5 Credential Access TTPs
Credential access represents the primary catalyst for multi-tenant container compromise. T1552.001 (Credentials In Files) involves reading auto-mounted service account tokens located at `/var/run/secrets/kubernetes.io/serviceaccount/token` or extracting credentials embedded in container configuration files. CWPP runtime agents monitor file open calls (`openat()`), intercepting processes other than designated client SDKs attempting to read the token file.

T1552.007 (Container API) and T1528 (Steal Application Access Token) focus on extracting tokens via unauthenticated Kubelet ports (port 10255) or querying cloud Instance Metadata Services (IMDS at `169.254.169.254`). CWPP agents enforce host-level firewall rules and eBPF network filters blocking workload pods from accessing the cloud metadata endpoint unless explicitly authorized through workload identity mappings.

---

## 2. Production Incident & Remediation Architecture

### 2.1 Incident Operational Context

A critical production security incident occurred within a Tier-1 core financial banking cluster handling retail transaction processing. The targeted infrastructure comprised an Amazon EKS cluster deployed across multiple availability zones, running on Amazon Linux 2 worker nodes with Calico CNI for network policy enforcement.

The attack chain progressed through five distinct operational phases:

```
+---------------------------------------------------------------------------------+
|                           ATTACK PROGRESSION SEQUENCE                           |
+---------------------------------------------------------------------------------+
| 1. Initial Access & Ingress Exploitation                                        |
|    Attacker -> Exploits Spring4Shell (CVE-2022-22965) in Payment Gateway (T1190)|
|                                      |                                          |
| 2. Local Reconnaissance & Credential Theft                                      |
|    Interactive Shell -> Enumerates Pod Environment & Mounts (T1613)             |
|    Dumps ServiceAccount Token at /var/run/secrets/kubernetes.io (T1552.001)     |
|                                      |                                          |
| 3. Privilege Escalation & RBAC Tampering                                        |
|    Queries API Server -> Exploits Over-Permissive RBAC Configuration            |
|    Creates ClusterRoleBinding Granting cluster-admin Privileges (T1098.006)     |
|                                      |                                          |
| 4. Persistent Workload Deployment                                               |
|    Deploys Rogue DaemonSet ("aws-telemetry-sync") Bypassing GitOps (T1610)      |
|    Configures Privileged Flag (privileged: true) & hostPath: / (T1611)          |
|                                      |                                          |
| 5. Host Breakout & Impact Execution                                             |
|    Executes nsenter into Host PID 1 -> Drops XMRig Cryptominer (T1496.001)      |
|    Attempts Log Truncation -> Initiates Stratum C2 Traffic (T1070, T1496.002)   |
+---------------------------------------------------------------------------------+
```

Phase 1 (Initial Access): The threat actor identified an unpatched payment gateway microservice vulnerable to Remote Code Execution via CVE-2022-22965 (Spring4Shell). By submitting a crafted HTTP request with serialized class loader parameters, the attacker achieved remote command execution inside the container.

Phase 2 (Credential Access): Operating within the compromised container, the attacker spawned an internal shell and accessed the default service account token mounted automatically at `/var/run/secrets/kubernetes.io/serviceaccount/token`. The pod belonged to an unsegmented namespace where default token automounting remained active.

Phase 3 (Privilege Escalation): The attacker used `curl` to query the internal Kubernetes API server (`https://kubernetes.default.svc`). Due to historical operational drift, the `default` service account within that namespace had previously been granted administrative privileges via an overly broad `ClusterRoleBinding`. Exploiting this misconfiguration, the attacker verified full cluster control.

Phase 4 (Persistence & Evasion): To establish persistent access across the cluster, the attacker submitted a rogue DaemonSet named `aws-telemetry-sync`, masquerading as an official AWS monitoring component. The DaemonSet specification requested `privileged: true` and mounted the host filesystem root (`hostPath: /`).

Phase 5 (Host Breakout & Impact): Once the rogue DaemonSet scheduled pods across worker nodes, the attacker executed `nsenter --target 1 --mount --uts --ipc --net --pid` to break out of the container isolation. From the host root shell, the attacker dropped a compiled XMRig mining binary, disabled host audit logging, and initiated outbound Stratum protocol connections to external mining pools.

### 2.2 Root-Cause Defect Forensic Decomposition

Forensic analysis conducted following cluster isolation revealed five foundational architectural and configuration defects:

1. Automatic Service Account Token Mounting (T1552.001): Workload pod specifications failed to set `automountServiceAccountToken: false`. Microservices with zero business requirement to communicate with the Kubernetes API server were granted valid JSON Web Tokens (JWT) by default.
2. Excessive RBAC Cluster Permissions (T1098.006): Administrative roles were bound to the namespace `default` service account rather than dedicated, cryptographically authenticated identities. This violated the principle of least privilege and allowed single-pod compromises to escalate into cluster takeover.
3. Absence of Preventative Admission Controls (T1610, T1611): The cluster lacked an active admission controller (such as OPA Gatekeeper or Kyverno) to enforce Kubernetes Pod Security Standards. Pods requesting `privileged: true`, host namespaces (`hostPID`, `hostNetwork`), and root directory `hostPath` volume mounts were scheduled without policy validation.
4. Mutable Root Filesystem & Missing Runtime Isolation (T1190, T1496.001): Containers executed with mutable root filesystems and root UID (UID 0). This permitted the adversary to write downloaded binaries directly to disk, execute compilers, and invoke interactive shells.
5. Unrestricted Egress Networking (T1046, T1496.002): The payment gateway namespace lacked Calico network policies restricting outbound network traffic. Workloads could establish unrestricted egress connections to arbitrary public Internet IP addresses and ports, enabling payload staging and cryptomining C2 communication.

### 2.3 Comprehensive Defense-in-Depth Architectural Remediation

To eliminate the systemic vulnerabilities identified during forensics, the engineering team executed a defense-in-depth remediation architecture across four functional layers:

```
+---------------------------------------------------------------------------------+
|               FOUR-LAYER DEFENSE-IN-DEPTH REMEDIATION ARCHITECTURE              |
+---------------------------------------------------------------------------------+
| LAYER 1: PREVENTATIVE ADMISSION CONTROLS                                        |
| - Kyverno / Gatekeeper: Enforce Pod Security Standards "Restricted" profile.    |
| - Block privileged: true, hostPID: true, hostNetwork: true, & hostPath mounts.  |
| - Enforce automountServiceAccountToken: false on all workload specifications.   |
| - Validate container image cryptographic signatures using Sigstore Cosign.      |
+---------------------------------------------------------------------------------+
| LAYER 2: RUNTIME BEHAVIORAL PROFILING & eBPF ENFORCEMENT                        |
| - Deploy CWPP runtime daemonsets (Falco & AWS GuardDuty Runtime Monitoring).    |
| - Hook kernel execve(), openat(), and setns() syscalls to profile process trees.|
| - Enforce readOnlyRootFilesystem: true and drop all default Linux capabilities. |
| - Automatically kill containers executing unexpected shells or token dumps.     |
+---------------------------------------------------------------------------------+
| LAYER 3: NETWORK MICROSEGMENTATION & IDENTITY HARDENING                         |
| - Calico / Cilium CNI: Enforce default-deny egress policies across namespaces.  |
| - Restrict outbound egress strictly to declared internal microservices and APIs.|
| - Deploy IMDSv2 with hop limit = 1 to block container access to node metadata.  |
| - Migrate workload identities to AWS IAM Roles for Service Accounts (IRSA).     |
+---------------------------------------------------------------------------------+
| LAYER 4: SIEM TELEMETRY CORRELATION & AUTOMATED INCIDENT RESPONSE               |
| - Stream Kubernetes audit logs and CWPP alerts to Microsoft Sentinel.           |
| - Deploy real-time correlation rules linking RBAC mutations with alerts.        |
| - Automated SOAR playbook: Automatically cordon and drain nodes in 60 seconds.  |
| - Immediate automated revocation of tainted ServiceAccount tokens and sessions. |
+---------------------------------------------------------------------------------+
```

Layer 1 (Preventative Admission Control): Deployed Kyverno admission controllers configured with the Pod Security Standards "Restricted" profile. Admission webhooks inspect every incoming manifest, rejecting any workload requesting `privileged: true`, host namespaces, or writable root filesystems. Furthermore, an admission mutation rule injects `automountServiceAccountToken: false` onto all service accounts and pod templates unless explicitly exempted via signed exception metadata. Image verification webhooks reject any container image whose cryptographic signature does not validate against the internal enterprise private key.

Layer 2 (Runtime Behavioral Profiling & eBPF Enforcement): Configured CWPP runtime agents on all worker nodes. Agents employ eBPF probes to intercept process creation, filesystem writes, and network socket operations. Containers run with `readOnlyRootFilesystem: true` and non-root users (`runAsNonRoot: true`), with temporary data restricted to ephemeral memory-backed volumes (`emptyDir: medium: Memory`). The CWPP engine terminates any workload process attempting to spawn `/bin/sh`, execute `nsenter`, or read service account tokens outside approved client libraries.

Layer 3 (Network Microsegmentation & Identity Hardening): Implemented strict default-deny network policies using Calico CNI. Ingress and egress traffic are restricted to explicitly declared service ports. Workload communication with the cloud metadata service (`169.254.169.254`) is blocked by configuring the EC2 metadata parameter `HttpPutResponseHopLimit=1`, preventing container network packets from traversing the host network namespace. All application credentials migrate to AWS IAM Roles for Service Accounts (IRSA), eliminating long-lived credentials.

Layer 4 (SIEM Telemetry Correlation & Automated Response): Connected Amazon EKS audit log streams, VPC Flow Logs, and GuardDuty CWPP findings directly into Microsoft Sentinel via Amazon Kinesis Firehose. Deployed real-time correlation rules that link unusual RBAC modifications with subsequent container deployments. Configured automated Security Orchestration, Automation, and Response (SOAR) playbooks: upon receiving a confirmed T0/T1 alert, the platform automatically cordons and drains the affected worker node, isolates the network namespace, and invalidates all associated IAM session tokens within 60 seconds.

---

## 3. Exam Question Bank & Distractor Forensics

### Question 1: Operational Sequence (FIRST Action)
During a routine trading session, the Security Operations Center (SOC) receives a high-severity alert from the runtime CWPP engine indicating that a container running inside a customer-facing banking namespace has executed `openat()` on `/var/run/secrets/kubernetes.io/serviceaccount/token` followed by a network socket connection to the internal Kubernetes API Server (`T1552.001`). Within 45 seconds, a second alert indicates an attempt to deploy a privileged pod with `hostPath: /` mounted (`T1611`). Which operational action must the incident response engineer execute FIRST?

- A. Revoke all administrative IAM credentials across the cloud platform root account.
- B. Quarantine and isolate the compromised pod by applying a network policy restricting all ingress and egress, and cordon the underlying worker node.
- C. Connect via `kubectl exec` into the alerting container to inspect memory artifacts and dump process history.
- D. Delete the entire Kubernetes namespace hosting the banking workload to purge all compromised resources.

#### Distractor Forensics:
- Option A is incorrect. Revoking cloud platform root IAM credentials represents an over-scoped, disruptive action that fails to contain the immediate workload threat inside the container runtime, and causes unnecessary enterprise operational downtime.
- Option B is the CORRECT answer. In container incident response, the primary immediate priority is containing active lateral movement and host breakout attempts. Isolating the compromised pod via network microsegmentation and cordoning the underlying worker node halts the attacker from reaching the Kubernetes API server or scheduling further rogue workloads, while preserving volatile container state for forensic analysis.
- Option C is incorrect. Executing `kubectl exec` into an actively compromised pod introduces foreign processes, alters filesystem access timestamps, contaminates forensic evidence, and alerts the adversary to SOC intervention.
- Option D is incorrect. Deleting the entire namespace destroys critical forensic evidence (container layers, ephemeral logs, process artifacts) and induces an uncoordinated operational outage for benign services sharing the namespace.

### Question 2: Architectural Optimization (BEST/MOST Effective Control)
A financial institution designs a multi-tenant Kubernetes platform hosting both core banking transaction processors and third-party partner integrations. Security architects must establish preventative controls to eliminate the risk of container breakout and host compromise (`T1611` / `T1068`). Which combination of architectural controls provides the BEST and MOST effective protection against container escape vulnerabilities?

- A. Increasing worker node CPU and memory capacity to reduce resource contention across namespaces.
- B. Enforcing the Kubernetes Pod Security Standards "Restricted" profile via admission controllers, running containers with non-root UID and read-only root filesystems, and executing untrusted workloads within lightweight virtualization runtimes (such as Kata Containers or gVisor).
- C. Deploying antivirus software inside each container image during continuous integration build pipelines.
- D. Configuring external network firewalls to inspect all ingress HTTP traffic directed toward edge load balancers.

#### Distractor Forensics:
- Option A is incorrect. Hardware resource allocation provides compute scaling but provides zero security boundary protection against kernel exploitation or container escape techniques.
- Option B is the CORRECT answer. Defense-in-depth against host breakout requires layered isolation: admission controllers enforce the "Restricted" profile (prohibiting `privileged: true`, host namespaces, and dangerous capabilities), immutable read-only filesystems prevent dropped exploit execution, and sandbox runtimes (Kata Containers or gVisor) replace shared kernel access with dedicated virtualization or intercepted syscall layers, completely neutralizing kernel exploit escape paths.
- Option C is incorrect. Traditional antivirus scanners embedded within container images increase attack surface, expand image size, fail to prevent zero-day kernel exploits, and cannot intercept runtime syscall-level escape behaviors.
- Option D is incorrect. Edge network firewalls inspect north-south traffic but cannot detect or restrict east-west lateral movement, internal kernel exploits, or container runtime breakouts occurring within cluster worker nodes.

### Question 3: Incident Response Pipeline (NEXT Step)
A financial cluster administrator successfully terminates an unauthorized pod running an illicit XMRig cryptomining process (`T1496.001`) that was deployed via an exposed Docker daemon API. The cluster is stabilized and active mining network traffic has ceased. According to financial container incident response procedures, what is the NEXT operational step the response team must execute?

- A. Close the security incident ticket and return the cluster to normal monitoring status.
- B. Conduct a comprehensive forensic audit of Docker daemon access logs, identify the initial network ingress path, verify integrity of all container images residing on the host, and enforce mutual TLS (mTLS) authentication on the Docker socket.
- C. Rebuild the entire corporate cloud data center from tape backup storage.
- D. Purchase additional cloud compute capacity to absorb future resource hijacking spikes.

#### Distractor Forensics:
- Option A is incorrect. Closing the ticket immediately after killing the process fails to address the root-cause entry point (the exposed daemon API), leaving the infrastructure vulnerable to immediate re-infection.
- Option B is the CORRECT answer. After immediate containment, the next mandatory phase of incident response is eradication and root-cause analysis: auditing access logs to identify the intrusion vector, scanning images for planted backdoors (`T1525`), and remediating the architectural defect by closing the exposed port or enforcing mutual TLS certificate authentication on the daemon interface.
- Option C is incorrect. Full data center reconstruction from tape represents a disproportionate disaster recovery action for an isolated container daemon breach that has already been contained.
- Option D is incorrect. Purchasing additional compute capacity validates the threat actor's resource theft, increases operating expenditures, and fails to mitigate security exposure.

### Question 4: Architectural Boundary (PRIMARY/EXCEPT Analysis)
When implementing a defense-in-depth container security baseline across financial production workloads, all of the following engineering practices represent valid, standard-compliant hardening controls EXCEPT:

- A. Granting the `CAP_SYS_ADMIN` capability and setting `privileged: true` on production microservice containers to enable internal debugging and diagnostics.
- B. Disabling automatic ServiceAccount token mounting (`automountServiceAccountToken: false`) on all pods that do not require programmatic interaction with the Kubernetes API.
- C. Restricting egress traffic from container worker nodes to the cloud Instance Metadata Service (IMDS) using packet filters or hop limit configurations.
- D. Enforcing cryptographic image signature verification at the admission controller stage to reject unsigned container images.

#### Distractor Forensics:
- Option A is the CORRECT answer (the invalid practice to identify). Granting `CAP_SYS_ADMIN` and setting `privileged: true` disables all container namespace and cgroup isolation barriers, giving the workload root-level access to host hardware and kernel structures. This directly enables container escape (`T1611`) and violates CIS Kubernetes Benchmark Controls 5.2.1 and 5.2.5.
- Option B is incorrect (valid control). Disabling automatic token automounting is an essential least-privilege practice that directly prevents token theft and unauthorized API access (`T1552.001`).
- Option C is incorrect (valid control). Restricting access to IMDS endpoints prevents compromised containers from stealing node-level IAM credentials and escalating cloud account privileges (`T1526`, `T1552`).
- Option D is incorrect (valid control). Image signature verification via admission controllers guarantees provenance and prevents the deployment of untrusted or tampered container images (`T1204.003`, `T1525`).
