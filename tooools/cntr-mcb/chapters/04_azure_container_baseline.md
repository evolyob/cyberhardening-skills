# Chapter 4: Microsoft Azure Container Security Monitoring & Configuration Baseline

## 1. Statutory Baseline & Technical Control Matrix

### 1.1 Architecture & Control Plane Security Boundaries

Azure Kubernetes Service (AKS) operates on a shared responsibility model where Microsoft manages control plane infrastructure (API Server, etcd, controller manager, scheduler), while tenant organizations govern worker node pools, workloads, identities, network policies, and runtime monitoring. Securing financial workloads on AKS requires an integrated defensive architecture combining Cloud Workload Protection Platforms (CWPP), Cloud Security Posture Management (CSPM), admission control, and central Security Information and Event Management (SIEM) telemetry correlation.

Microsoft Defender for Containers serves as the core CWPP engine for Azure container environments. The solution deploys an eBPF DaemonSet runtime sensor (`mdfc-operator` and `defender-agent`) on Linux worker nodes, runs agentless snapshot vulnerability assessments of container images in Azure Container Registry (ACR), and audits worker node operating system configurations. Microsoft Defender CSPM evaluates AKS infrastructure against the Microsoft Cloud Security Benchmark (MCSB) and the CIS AKS Benchmark, delivering Cloud Infrastructure Entitlement Management (CIEM) to identify excessive identity permissions across cluster components.

Admission control operates through the Azure Policy add-on for Kubernetes, built on Open Policy Agent (OPA) Gatekeeper. This engine intercepts resource creation requests at the Kubernetes API Server, enforcing Pod Security Standards (PSS) Baseline and Restricted profiles before workloads execute. Identity governance mandates Microsoft Entra ID integration with Azure Role-Based Access Control (Azure RBAC), requiring administrators to disable local cluster accounts (`--disable-local-accounts`) and transition application credentials to Microsoft Entra Workload ID with short-lived OpenID Connect (OIDC) federated tokens.

Telemetry aggregation channels diagnostic logs from the AKS managed control plane, worker node system logs, and Defender security alerts into a central Log Analytics Workspace. From this repository, Microsoft Sentinel correlates runtime signals with enterprise identity events to detect anomalous behaviors across the container lifecycle.

### 1.2 Statutory & Regulatory Framework Alignment

Financial container workloads on Azure must satisfy statutory security requirements. The following matrix correlates standards with native Azure controls and verification procedures.

| Regulatory Standard | Clause / Control ID | Technical Requirement | Azure Implementation Mechanism | Audit Verification Method |
| :--- | :--- | :--- | :--- | :--- |
| **NIST CSF v2.0** | PR.PS-01, PR.PS-02 | Workload runtime protection and configuration integrity | Defender for Containers eBPF sensor; Azure Policy add-on for Kubernetes | Audit Defender daemonset health; verify Gatekeeper constraint enforcement in Log Analytics |
| **NIST CSF v2.0** | DE.CM-01, DE.CM-03 | Continuous telemetry collection and anomaly detection | AKS Diagnostic Settings (`kube-audit`, `kube-apiserver`) to Log Analytics | Verify `KubeAudit` table ingestion latency (< 5 minutes) in Sentinel |
| **NIST SP 800-53 R5.1.1** | AC-2, AC-3, AC-6 | Least privilege access control and identity governance | Microsoft Entra ID integration with AKS Azure RBAC; local accounts disabled | Run `az aks show --query "aadProfile.enableAzureRbac"` and verify `disableLocalAccounts: true` |
| **NIST SP 800-53 R5.1.1** | AU-2, AU-6, AU-12 | Audit log generation, reduction, and immutable storage | Log Analytics Workspace Data Retention; Immutable Blob Storage | Review Log Analytics data retention policies and workspace access controls |
| **NIST SP 800-53 R5.1.1** | CM-2, CM-6, CM-7 | Baseline configuration auditing and least functionality | Defender CSPM automated posture assessments against CIS AKS Benchmark | Inspect Defender CSPM compliance score and outstanding recommendations |
| **NIST SP 800-53 R5.1.1** | SI-3, SI-4 | Malicious code detection and system monitoring | Defender for Containers runtime alerts; ACR automated image vulnerability scanning | Verify image vulnerability scan reports in Defender for Cloud before deployment |
| **PCI DSS v4.0.1** | Req 1.3, 2.2 | Network segmentation and secure system configuration | Azure CNI with Azure Network Policy or Calico; CIS AKS hardened node images | Audit NetworkPolicy resources blocking namespace cross-talk and metadata IP access |
| **PCI DSS v4.0.1** | Req 6.4, 7.2 | Vulnerability management and restricted privileges | Defender Vulnerability Management; Azure Policy blocking privileged containers | Verify Gatekeeper constraint `K8sAzurePrivilegedContainer` denies root container creation |
| **PCI DSS v4.0.1** | Req 10.2, 10.3 | Capture audit trails for administrative access | Control plane audit logging (`kube-audit-admin`) forwarded to Microsoft Sentinel | Query `KubeAuditAdmin` table for privileged role assignments and exec sessions |
| **CIS AKS Benchmark** | 5.1.1 to 5.4.5 | Pod Security Standards and admission control baseline | Azure Policy built-in initiative for Kubernetes Pod Security Restricted profile | Check Azure Policy compliance dashboard for cluster resource compliance percentage |
| **MCSB v1** | IM-1, LT-1, PA-1 | Central identity, logging, and posture assessment | Microsoft Entra Workload ID; Log Analytics central workspace; Defender CSPM | Verify absence of static Kubernetes Secret tokens in application pod manifests |

### 1.3 Telemetry Logging Architecture & Data Component (DC) Mapping

To maintain diagnostic sovereignty and complete audit trails, financial institutions must capture all ten canonical Data Component (DC) tags defined by the Financial Container Security Monitoring Baseline (MCB).

| Data Component Tag | Raw Log Category / Telemetry Class | Azure Native Collection Mechanism | Storage Destination | SIEM Retention Standard |
| :--- | :--- | :--- | :--- | :--- |
| **kubernetes:audit** | Kubernetes Audit Log (`kube-audit`, `kube-audit-admin`) | AKS Diagnostic Settings to Log Analytics Workspace | Log Analytics `KubeAudit` and `KubeAuditAdmin` tables | Hot: 90 days; Cold Archive: 365 days |
| **kubernetes:events** | Kubernetes Cluster Events | Container Insights monitoring agent DaemonSet | Log Analytics `KubeEvents` table | Hot: 90 days; Cold Archive: 365 days |
| **kubernetes:apiserver** | API Server Operational Logs | AKS Diagnostic Settings (`kube-apiserver`) | Log Analytics `KubeApiServer` table | Hot: 90 days; Cold Archive: 365 days |
| **kubernetes:orchestrator** | Controller Manager and Scheduler Logs | AKS Diagnostic Settings (`kube-controllermanager`, `kube-scheduler`) | Log Analytics Workspace diagnostic tables | Hot: 90 days; Cold Archive: 180 days |
| **containerd:events** | Container Runtime Lifecycle Events | Microsoft Defender for Containers eBPF Runtime Sensor | Defender SecurityAlerts table / Sentinel incident queue | Hot: 180 days; Cold Archive: 365 days |
| **containerd:runtime** | Container Workload Stdout / Stderr Logs | Container Insights (`ContainerLogV2` schema) | Log Analytics `ContainerLogV2` table | Hot: 30 days; Cold Archive: 90 days |
| **container:api** | Container Engine API Requests | N/A (Managed AKS isolates direct containerd socket API access) | Cloud platform isolation boundary | Managed by Microsoft infrastructure SLA |
| **container:registry** | Container Registry Pull, Push, and Auth Activity | Azure Container Registry (ACR) Diagnostic Logs | Log Analytics `ContainerRegistryRepositoryEvents` table | Hot: 90 days; Cold Archive: 365 days |
| **ebpf:syscalls** | Kernel System Call Telemetry (execve, openat, ptrace) | Defender for Containers eBPF kernel hooks | Microsoft Defender for Cloud telemetry pipeline | Hot: 90 days; Cold Archive: 365 days |
| **container:stats** | Container CPU, Memory, Disk, and Network Metrics | Container Insights / Azure Managed Prometheus | Azure Monitor Metrics / Managed Prometheus Workspace | Hot: 30 days; Cold Archive: 90 days |

### 1.4 Quantitative Key Risk & Control Indicators (KPI / KRI / KCI)

Financial institutions must track quantitative metrics to verify container controls operate within prescribed risk tolerances.

| Category | Indicator Name | Metric Threshold | Measurement Method / Calculation Formula | Enforcing Service |
| :--- | :--- | :--- | :--- | :--- |
| **KCI** | Local Account Deprecation Ratio | 100% compliant | `(Clusters with Local Accounts Disabled / Total AKS Clusters) * 100` = 100% | Azure Policy / Defender CSPM |
| **KCI** | Entra Workload ID Adoption | 100% compliant | `(Workloads with Federated Tokens / Total Production Pods) * 100` = 100% | Defender CSPM CIEM |
| **KRI** | Critical Runtime Alert Volume | 0 uncontained alerts | Count of unresolved High/Critical Defender alerts > 15 minutes | Microsoft Sentinel Incident Queue |
| **KRI** | Vulnerable Image Deployment Rate | 0% allowed | `(Deployed Images with CVSS >= 8.0 / Total Deployed Images) * 100` = 0% | ACR Image Scanning / Azure Policy |
| **KPI** | Mean Time to Detect (MTTD) | <= 3 minutes | Elapsed time from initial malicious syscall to Sentinel Incident creation | Defender for Containers + Sentinel |
| **KPI** | Mean Time to Contain (MTTC) | <= 15 minutes | Elapsed time from Sentinel incident alert to automated pod isolation | Sentinel Automation Rule / Logic App |
| **KCI** | Gatekeeper Constraint Enforcement | 100% active | `(Namespaces Enforcing Pod Security Restricted / Total Namespaces) * 100` = 100% | Azure Policy add-on for Kubernetes |
| **KRI** | Privileged Container Workload Count | 0 in non-system namespaces | Count of running pods where `securityContext.privileged == true` | Azure Policy / Defender CSPM |

### 1.5 Threat Detection Coverage Matrix: MITRE ATT&CK for Containers (36 TTPs)

Evaluation of native Azure security services against the 36 MITRE ATT&CK for Containers techniques confirms that 25 techniques generate native runtime alerts through Microsoft Defender for Containers (Category 2). The remaining 11 techniques represent conditional architectural exclusions (Category 4), where managed platform boundaries or preventive controls address the threat, supplemented by Azure compensating controls.

#### Part A: Native CWPP Alerts (25 Techniques Covered)

The table below details the native detection alerts provided by Microsoft Defender for Containers and their corresponding MITRE ATT&CK mappings.

| MITRE Technique ID | Technique Name | CWPP Alert Display Name | Severity | Native Detection Mechanism |
| :--- | :--- | :--- | :--- | :--- |
| **T1036.005** | Masquerading: Match Legitimate Name or Location | Possible executable detected in a command line, encoded in Base64 | Informational | eBPF sensor inspects command-line arguments of processes executed inside containers. |
| **T1036.010** | Masquerading: Masquerade Task or Service | Potential base64 encoded shell script execution | Informational | Runtime sensor flags script interpreters running base64 strings to evade lexical matching. |
| **T1046** | Network Service Discovery | Network Scanning Tool Detected | Informational / Medium | eBPF process monitor detects execution of network scanning tools (nmap, masscan, zmap). |
| **T1053.007** | Scheduled Task/Job: Container Lifecycle Hooks | Suspicious Cron operations in command line detected | Low | Host and container process monitoring detects crontab file modifications or enumeration. |
| **T1059.013** | Command & Scripting Interpreter: Cloud API | Cmd & Scripting Interpreter: Cloud API; Suspicious command executed in container | Medium | Kube-audit analysis identifies abnormal kubectl exec sessions invoking administrative tools. |
| **T1069** | Permission Groups Discovery | Permission Groups Discovery | Informational / N/A | Audited via Defender CSPM CIEM and Log Analytics kube-audit queries to limit false positives. |
| **T1070** | Indicator Removal on Host | Kubernetes events deleted; Possible Log Tampering Activity; Suspicious usage of shred command | Informational / Low / Medium | Detects deletion of Kubernetes events, log file truncation, chattr file changes, and shred execution. |
| **T1078.001** | Valid Accounts: Default Accounts | Abnormal / Suspicious Kubernetes service account operation detected | Low / Medium | Machine learning baseline detects anomalous API calls executed by default service accounts. |
| **T1078.003** | Valid Accounts: Local Accounts | Abnormal / Suspicious Kubernetes service account operation detected | Low / Medium | Flags anomalous administrative actions triggered via local service account tokens. |
| **T1098.006** | Account Manipulation: Additional Cloud Roles | Account added to sudo group; New high privileges role detected; Role binding to cluster-admin | Informational | Flags addition of users to sudoers, new privileged ClusterRole, or cluster-admin RoleBinding. |
| **T1133** | External Remote Services | Kubernetes API requests from suspicious IP address; SSH server running inside container | Informational / Medium | Threat intelligence flags connections from botnet IPs; sensor flags running SSH daemons in pods. |
| **T1190** | Exploit Public-Facing Application | Exposed Kubernetes / Kubeflow dashboard; Exposed Redis / Postgres; Path traversal; React2Shell | Low / Medium / High | Identifies exposed administrative dashboards, vulnerable services, and active command injections. |
| **T1204.003** | User Execution: Malicious Image | Container with a miner image detected | High | eBPF and audit log analytics cross-reference running image hashes against threat intelligence. |
| **T1485** | Data Destruction | Suspicious usage of shred command on hidden files detected | Low | eBPF process telemetry detects shred execution targeting hidden configuration directories. |
| **T1496.001** | Resource Hijacking: Compute Hijacking | Digital currency mining behavior; CPU optimization; Cryptominer process kills | High | eBPF sensor detects known mining binaries, process nice priority abuse, and peer miner terminations. |
| **T1496.002** | Resource Hijacking: Bandwidth Hijacking | Suspicious Proxyware or Traffic monetizers detected in command line; Crypto pool DNS access | High | Flags execution of proxyware (Honeygain, PacketStream) and DNS queries resolving to mining pools. |
| **T1528** | Steal Application Access Token | Access to cloud metadata service detected; Suspicious access to workload identity token | Informational / Low / Medium | Detects container processes making HTTP requests to IMDS (169.254.169.254) or accessing token files. |
| **T1543.005** | Create or Modify System Process: Container Process | CoreDNS modification detected; Creation of admission webhook configuration | Informational / High | Detects unauthorized CoreDNS ConfigMap edits, admission webhook deployments, or /proc tampering. |
| **T1552.001** | Unsecured Credentials: Credentials in Files | Access to kubelet kubeconfig; TeamPCP supply chain attack; Secret Reconnaissance Detected | Informational / Medium / High | Flags access to node kubeconfig, known supply chain package exploits (Trivy backdoor), and secret scraping. |
| **T1609** | Container Administration Command | Suspicious command executed in container (K8S_MaliciousContainerExec) | Medium | Kube-audit analysis flags interactive exec sessions executing suspicious shells or reconnaissance tools. |
| **T1610** | Deploy Container | New container in the kube-system namespace detected | Informational | Kube-audit monitoring detects deployment of unauthorized pods into the critical kube-system namespace. |
| **T1611** | Escape to Host | Attempt to create new Linux namespace; Sensitive volume mount; Privileged container detected | Informational / Medium | Flags container attempts to create user namespaces (CVE-2022-0185), hostPath mounts, and privileged mode. |
| **T1612** | Build Image on Host | Docker build operation detected on a Kubernetes node | Informational | eBPF monitor flags invocation of docker build, buildah, or kaniko on production worker nodes. |
| **T1613** | Container and Resource Discovery | Kubernetes penetration testing tool detected; Suspicious request to Kubernetes API | Low / Informational | Flags known offensive tools (peirates, kube-hunter) and burst API reconnaissance requests. |
| **T1685** | Disable or Modify Tools | Disable or Modify Tools (Attempt to terminate Defender agent, configuration tampering) | Low / Medium | Flags kill signals directed at `mdfc-operator` pods, stopping security daemons, or tampering with audit rules. |

#### Part B: Compensating Architecture Controls (11 Architectural Exclusions)

Eleven techniques are categorized as Category 4 (Conditional Architectural Exclusion with Compensating Security Controls) because single-sensor CWPP runtime detection is insufficient or superseded by managed platform boundaries.

1. **T1068 (Exploitation for Privilege Escalation)**: Runtime behavioral rules cannot reliably detect zero-day kernel exploits without generating excessive false positives. Compensating controls: Enable Defender for Containers Agentless Scanning for worker nodes, activate Defender CSPM Agentless Container Posture, and configure AKS Node Image Auto-Upgrade (`--node-os-upgrade-channel SecurityPatch`) to apply kernel patches automatically.
2. **T1110.001 (Brute Force: Password Guessing)**: Managed AKS isolates password authentication when configured per financial baselines. Compensating controls: Enforce Microsoft Entra ID integration, execute `az aks update --disable-local-accounts`, activate Microsoft Entra ID Identity Protection, and deploy Application Gateway WAF rate-limiting.
3. **T1110.003 (Brute Force: Password Spraying)**: Password spraying targets corporate identity providers rather than container runtimes. Compensating controls: Deploy Entra ID Conditional Access policies requiring MFA, enforce Smart Lockout, and monitor sign-in risk telemetry in Microsoft Sentinel.
4. **T1110.004 (Brute Force: Credential Stuffing)**: Credential stuffing occurs at the public application ingress layer. Compensating controls: Deploy Azure Front Door or Application Gateway WAF with the Bot Protection rule set and IP reputation filtering.
5. **T1136.001 (Create Account: Local Account)**: Creating a local Linux user account inside a container provides negligible cluster persistence unless bound to Kubernetes RBAC roles, which Defender flags under T1098.006. Compensating controls: Ingest `kube-audit` into Log Analytics to audit ServiceAccount creation, collect `CloudProcessEvents` for `useradd`, and enforce read-only root filesystems via Azure Policy.
6. **T1490 (Inhibit System Recovery)**: AKS manages and isolates the etcd datastore, preventing direct tenant manipulation. Compensating controls: Protect persistent volumes via Azure Backup Vault Enhanced Soft-Delete (14 to 180 days retention with AlwaysON lock), store snapshots in Immutable Azure Blob Storage (WORM mode), and enable Defender for Resource Manager.
7. **T1498 (Network Denial of Service)**: L3/L4 volumetric network flooding cannot be mitigated at the container pod runtime layer. Compensating controls: Enable Azure DDoS Protection on the AKS Virtual Network, deploy Azure Firewall Premium with IDPS, and monitor Azure Monitor metrics `UnderDDoSAttack` and `DDoSTriggerSYNPackets`.
8. **T1499 (Endpoint Denial of Service)**: Application exhaustion attacks require ingress rate regulation and resource quotas. Compensating controls: Deploy Application Gateway WAF with managed OWASP rules, configure Kubernetes `ResourceQuota` and `LimitRange` objects in every namespace, and implement Horizontal Pod Autoscaler (HPA) and PodDisruptionBudgets.
9. **T1525 (Implant Internal Image)**: Image tampering occurs in the registry control plane, outside worker node runtime sensors. Compensating controls: Enforce ACR artifact signing using Notation CLI, configure ACR tag immutability, apply AKS Image Integrity Policy (Ratify Gatekeeper plugin) to deny unsigned image deployments, and monitor Defender for Resource Manager alerts.
10. **T1550.001 (Use Alternate Authentication Material: Application Access Token)**: Replaying stolen bearer tokens requires correlation across authentication logs, source IP addresses, and identity providers. Compensating controls: Deploy Microsoft Entra Workload ID with short-lived federated OIDC tokens, disable legacy ServiceAccount token auto-mounting, and correlate `KubeAudit` with `CloudAuditEvents` in Microsoft Sentinel.
11. **T1552.007 (Unsecured Credentials: Container API)**: AKS isolates the Kubernetes API Server behind managed endpoints. Compensating controls: Configure AKS as a Private Cluster (`--enable-private-cluster`) or restrict API Server authorized IP ranges, disable local accounts, set `kubeletConfig.readOnlyPort = 0`, and enforce the Azure Policy Restricted profile.

### 1.6 Detection as Code: Production Microsoft Sentinel KQL Rules

To operationalize threat detection, security operations teams must deploy production-grade Kusto Query Language (KQL) analytics rules into Microsoft Sentinel. The following rules map to the enterprise SIEM requirements (SIEM-001 through SIEM-005).

#### SIEM-001: Anonymous User Request to Kubernetes API (T1078.004 / P0)

```kusto
// SIEM-001: Anonymous User Requests Attempting State Modification
// Severity: High | Platform: Microsoft Sentinel | Data Source: KubeAudit
KubeAudit
| where TimeGenerated >= ago(1h)
| where User.username =~ "system:anonymous" or User.groups has "system:unauthenticated"
| where Verb in ("create", "update", "delete", "patch")
| extend StatusCode = toint(ResponseStatus.code)
| where StatusCode in (200, 201, 202)
| project TimeGenerated, ClusterId, Verb, ObjectRef_resource = ObjectRef.resource,
          ObjectRef_namespace = ObjectRef.namespace, ObjectRef_name = ObjectRef.name,
          SourceIp = SourceIps[0], UserAgent = UserAgent, StatusCode
| extend AccountCustomEntity = "system:anonymous", IPCustomEntity = SourceIp
```

#### SIEM-002: Privileged Pod Creation Alert (T1611 / P1)

```kusto
// SIEM-002: Privileged Container Workload Creation
// Severity: Critical | Platform: Microsoft Sentinel | Data Source: KubeAudit
KubeAudit
| where TimeGenerated >= ago(1h)
| where Verb =~ "create" and ObjectRef.resource =~ "pods"
| extend ReqObj = parse_json(RequestObject)
| extend Containers = ReqObj.spec.containers
| mv-expand Containers
| extend IsPrivileged = tobool(Containers.securityContext.privileged)
| where IsPrivileged == true
| project TimeGenerated, ClusterId, PodName = ObjectRef.name,
          Namespace = ObjectRef.namespace, ContainerName = Containers.name,
          ContainerImage = Containers.image, CallerUser = User.username,
          SourceIp = SourceIps[0]
| extend AccountCustomEntity = CallerUser, IPCustomEntity = SourceIp
```

#### SIEM-003: Sensitive HostPath Volume Mount (T1611 / P1)

```kusto
// SIEM-003: Pod Mounted Sensitive Host Filesystem Path
// Severity: Critical | Platform: Microsoft Sentinel | Data Source: KubeAudit
let SensitivePaths = dynamic(["/", "/etc", "/root", "/var/run", "/var/run/docker.sock",
                              "/var/run/containerd/containerd.sock", "/proc", "/sys", "/dev"]);
KubeAudit
| where TimeGenerated >= ago(1h)
| where Verb in ("create", "update") and ObjectRef.resource in ("pods", "deployments", "daemonsets")
| extend ReqObj = parse_json(RequestObject)
| extend Volumes = ReqObj.spec.volumes
| mv-expand Volumes
| extend HostPath = tostring(Volumes.hostPath.path)
| where isnotempty(HostPath) and SensitivePaths has HostPath
| project TimeGenerated, ClusterId, ResourceKind = ObjectRef.resource,
          ResourceName = ObjectRef.name, Namespace = ObjectRef.namespace,
          VolumeName = Volumes.name, MountedPath = HostPath,
          CreatedBy = User.username, SourceIp = SourceIps[0]
| extend AccountCustomEntity = CreatedBy, IPCustomEntity = SourceIp
```

#### SIEM-004: Interactive Shell Execution in Workload Container (T1059.004 / P1)

```kusto
// SIEM-004: Interactive Exec Session Launched Inside Container
// Severity: Medium | Platform: Microsoft Sentinel | Data Source: KubeAudit
let ShellBinaries = dynamic(["/bin/sh", "/bin/bash", "sh", "bash", "/bin/zsh", "zsh"]);
KubeAudit
| where TimeGenerated >= ago(1h)
| where Verb =~ "create" and ObjectRef.subresource =~ "exec"
| extend ReqObj = parse_json(RequestObject)
| extend ExecCommand = tostring(ReqObj.command)
| where ExecCommand has_any (ShellBinaries)
| project TimeGenerated, ClusterId, PodName = ObjectRef.name,
          Namespace = ObjectRef.namespace, ContainerName = tostring(ReqObj.container),
          ExecCommand, Caller = User.username, SourceIp = SourceIps[0]
| extend AccountCustomEntity = Caller, IPCustomEntity = SourceIp
```

#### SIEM-005: Cryptomining Outbound Network Connection (T1496 / P2)

```kusto
// SIEM-005: Outbound Mining Pool Traffic or Mining Ports Detected
// Severity: High | Platform: Microsoft Sentinel | Data Source: AzureDiagnostics / NetworkWatcher
let MiningPorts = dynamic([3333, 4444, 5555, 7777, 9001, 14444]);
let MiningDomains = dynamic(["pool.supportxmr.com", "xmr-eu.dwarfpool.com", "minexmr.com", "nanopool.org"]);
AzureDiagnostics
| where TimeGenerated >= ago(1h)
| where Category =~ "NetworkSecurityGroupRuleCounter" or Category =~ "AzureFirewallNetworkRule"
| extend DestPort = toint(destinationPort_d), DestHost = tostring(destinationHostName_s),
         DestIp = tostring(destinationAddress_s), SourceIp = tostring(sourceAddress_s)
| where DestPort in (MiningPorts) or DestHost has_any (MiningDomains)
| project TimeGenerated, ResourceGroup, SourceIp, DestIp, DestPort, DestHost, Action = action_s
| extend IPCustomEntity = DestIp
```

---

## 2. Production Incident & Remediation Architecture

### 2.1 Incident Context & Operational Scenario

In a production deployment supporting Open Banking payment APIs, a financial institution operated an Azure Kubernetes Service cluster across three availability zones in the `eastus2` region. The application processed payment requests via a Node.js microservice connected to transaction engines via private endpoints. The cluster was provisioned with default administrative settings: local administrator accounts remained enabled, the Azure Policy add-on was running in audit-only mode, and worker nodes communicated across an Azure CNI network without egress restrictions toward the Azure Instance Metadata Service.

At 03:14 UTC, an external threat actor initiated a multi-stage attack aimed at breaching cluster boundaries, harvesting cloud identity tokens, and establishing persistence for financial fraud and compute hijacking.

### 2.2 Attack Progression & Kill-Chain Breakdown

The intrusion unfolded across four operational phases:

1. **Ingress Exploitation**: The attacker identified an unpatched web dependency in the payment gateway pod, executing a React2Shell remote command injection. This exploit spawned a reverse shell connecting back to an external listener.
2. **Credential Access via IMDS**: Lacking Microsoft Entra Workload ID federation, the compromised pod retained default access to the underlying worker node network interface. The attacker issued HTTP requests to `http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/`. The IMDS endpoint returned a valid JSON Web Token (JWT) representing the AKS worker node managed identity.
3. **Host Escape via Sensitive Volume Mount**: Using the stolen credentials and service account privileges that lacked admission enforcement, the attacker submitted a pod specification configuring `securityContext.privileged: true` and mounting the host socket `/var/run/containerd/containerd.sock` via `hostPath`. Using a portable container client, the adversary instructed the container engine to launch a debugging container attached to the host root namespace, escaping container boundaries.
4. **Defense Evasion**: Once on the node, the intruder attempted to cover tracks by executing `kubectl delete events --all -n payment`, truncating local log files, and modifying file attributes with `chattr +i` on an installed rootkit. The attacker then executed an XMRig cryptomining binary configured to run at low CPU priority.

### 2.3 Detection & Alert Triangulation

Within two minutes of the breakout, Microsoft Defender for Containers triggered four high-severity alerts in the security operations queue:
- `Container with a sensitive volume mount detected` (Alert ID: `MDFC-K8S-057`, Severity: High, Target: payment namespace)
- `Attempt to create a new Linux namespace from a container detected` (Alert ID: `MDFC-K8S-055`, Severity: Medium, Node: `aks-agentpool-3104-vmss000002`)
- `Access to cloud metadata service detected` (Alert ID: `MDFC-K8S-038`, Severity: Medium, Pod: `payment-gw-78b9c4-k9x11`)
- `Digital currency mining related behavior detected` (Alert ID: `MDFC-K8S-031`, Severity: High, Node Host OS)

Microsoft Sentinel correlated these alerts into a single High Incident (`INC-89412`), triggering an automated incident response workflow.

### 2.4 Root-Cause Defect Analysis

Forensic analysis conducted by the incident response team isolated four structural security defects in the cluster configuration:

1. **Defect 1: Audit-Only Admission Governance**: The Azure Policy add-on for Kubernetes operated with the default evaluation setting (`Audit`) rather than active enforcement (`Deny`). Consequently, the API Server accepted the malicious pod manifest containing `privileged: true` and the sensitive hostPath mount without interception.
2. **Defect 2: Active Local Administrative Accounts**: The cluster retained local administrator account functionality (`--enable-local-accounts`), allowing long-lived static tokens to authenticate without traversing Microsoft Entra Conditional Access policies or MFA verification gates.
3. **Defect 3: Unrestricted IMDS Egress Access**: The worker node network did not isolate the link-local metadata address (`169.254.169.254`). Workload pods communicated directly with the node metadata service, exposing cloud identity tokens.
4. **Defect 4: Missing Automated Node Patching**: The node pool OS image upgrade channel was set to `None`, leaving unpatched Linux kernel components vulnerable to local namespace privilege escalation.

### 2.5 Architecture Remediation Blueprint

To eliminate these vulnerabilities, the engineering team executed an infrastructure hardening blueprint across four technical layers.

#### Step 1: AKS Cluster Identity & Control Plane Hardening

Execute the Azure CLI commands below to disable local static accounts, enforce Microsoft Entra ID authentication with Azure RBAC, activate Microsoft Entra Workload ID, and enable automated security patching on worker node operating systems.

```bash
# Disable local administrator accounts and enforce Microsoft Entra ID
az aks update \
  --resource-group rg-prod-banking-eastus2 \
  --name aks-prod-core-01 \
  --disable-local-accounts

# Enable OIDC Issuer and Microsoft Entra Workload Identity
az aks update \
  --resource-group rg-prod-banking-eastus2 \
  --name aks-prod-core-01 \
  --enable-oidc-issuer \
  --enable-workload-identity

# Configure automated node OS image patching
az aks update \
  --resource-group rg-prod-banking-eastus2 \
  --name aks-prod-core-01 \
  --node-os-upgrade-channel SecurityPatch

# Enforce Private Cluster authorized IP ranges
az aks update \
  --resource-group rg-prod-banking-eastus2 \
  --name aks-prod-core-01 \
  --api-server-authorized-ip-ranges 10.240.0.0/16
```

#### Step 2: Gatekeeper OPA Admission Constraints (Azure Policy)

Deploy Gatekeeper constraint definitions to block privileged containers and restrict hostPath filesystem mounts across all non-system namespaces.

```yaml
# Enforce denial of privileged container workloads
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sAzurePrivilegedContainer
metadata:
  name: pss-restricted-block-privileged
spec:
  enforcementAction: deny
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
    namespaces:
      - payment
      - banking-api
      - core-transact
  parameters:
    exemptImages: []
---
# Block sensitive hostPath mounts across workloads
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sAzureBlockHostPath
metadata:
  name: pss-restricted-block-hostpath
spec:
  enforcementAction: deny
  match:
    kinds:
      - apiGroups: [""]
        kinds: ["Pod"]
    namespaces:
      - payment
      - banking-api
      - core-transact
  parameters:
    allowedHostPaths: []
```

#### Step 3: Zero-Trust Network Policy Blocking IMDS Egress

Deploy a Kubernetes NetworkPolicy to cut off workload access to the link-local metadata address `169.254.169.254`, preventing pods from extracting node credentials.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-metadata-service-egress
  namespace: payment
spec:
  podSelector: {}
  policyTypes:
    - Egress
  egress:
    # Permit intra-cluster DNS resolution
    - to:
        - namespaceSelector: {}
          podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - protocol: UDP
          port: 53
        - protocol: TCP
          port: 53
    # Permit egress to internal financial microservices
    - to:
        - ipBlock:
            cidr: 10.240.0.0/16
            except:
              - 169.254.169.254/32
    # Deny all link-local cloud metadata endpoints explicitly
    - to:
        - ipBlock:
            cidr: 0.0.0.0/0
            except:
              - 169.254.169.254/32
```

#### Step 4: Microsoft Sentinel Automated Response Playbook

Configure an automated Sentinel Playbook (Azure Logic App) triggered by High-severity Defender for Containers alerts:
1. Calls the Kubernetes API to apply an immediate isolation taint (`node.kubernetes.io/quarantined=true:NoExecute`) to the affected worker node.
2. Directs Azure CNI to apply an emergency Network Security Group rule blocking all egress from the node private IP address.
3. Revokes all active OAuth2 tokens associated with the worker node managed identity in Microsoft Entra ID.
4. Generates an encrypted incident case package containing captured memory artifacts and Log Analytics query records for forensic analysis.

---

## 3. Exam Question Bank & Distractor Forensics

### Question 1: Operational Triage & Isolation (FIRST Action)

A financial institution's Security Operations Center (SOC) receives a Critical alert from Microsoft Defender for Containers: `Container with a sensitive volume mount detected` (T1611). Investigation confirms that a workload pod running in the `payments-prod` namespace on Azure Kubernetes Service (AKS) has mounted `/var/run/containerd/containerd.sock` from the host node. What is the FIRST action the lead incident responder should take?

- **A.** Execute `kubectl delete pod` with the `--force --grace-period=0` flag to eliminate the unauthorized container instance immediately.
- **B.** Cordon and taint the affected worker node, apply an isolating network policy to the suspicious pod, and capture volatile runtime memory before terminating the workload.
- **C.** Modify the Azure Policy definition in the Azure portal from `Audit` to `Deny` to enforce admission control cluster-wide.
- **D.** Drain all workloads from the affected worker node using `kubectl drain --ignore-daemonsets` to initiate automated node reimaging.

#### Correct Answer: B

#### Complete 4-Option Distractor Forensics

- **Option A is incorrect**: Executing `kubectl delete pod --force` immediately destroys volatile container memory, process tables, temporary filesystem changes, and in-flight network connection state. In a financial security incident, premature destruction of digital evidence prevents forensic investigators from establishing the root cause, determining whether host breakout occurred, or identifying lateral movement. Triage must isolate before terminating.
- **Option B is correct**: Cordoning and tainting the host node prevents the scheduler from placing new workloads on the compromised host. Applying an isolating network policy cuts off network command-and-control communication, and acquiring volatile runtime memory preserves digital evidence necessary to assess whether the container socket was exploited to compromise the host kernel.
- **Option C is incorrect**: Updating the Azure Policy definition to `Deny` is an essential post-incident remediation control, but it is preventive rather than reactive. Modifying the policy affects future API requests; it does not contain or isolate the actively running malicious container currently mounted to the host filesystem.
- **Option D is incorrect**: Issuing `kubectl drain` evicts running pods from the node and causes the Kubernetes scheduler to reschedule them onto healthy worker nodes across the cluster. If the attacker has established persistence or infected other containers on that node, draining propagates the compromised workloads across the remaining production fleet.

---

### Question 2: Cloud Identity Hardening (BEST / MOST Action)

An enterprise architect must design an identity security architecture for a regulated payment application deployed on Azure Kubernetes Service (AKS). The regulatory requirement mandates that no static credentials or persistent service account tokens may exist inside workload containers, and identity tokens must be cryptographically constrained to short lifespans with strict role delegation. Which architectural design BEST fulfills these statutory mandates?

- **A.** Provision an Azure Key Vault instance, store static Entra service principal client secrets inside it, and mount them into containers via the Secrets Store CSI Driver.
- **B.** Configure AKS with Microsoft Entra Workload ID, enable the cluster OIDC Issuer, annotate application ServiceAccounts with federated Entra Managed Identities, and configure applications to retrieve short-lived tokens via the Azure Identity SDK.
- **C.** Grant the AKS worker node pool system-assigned Managed Identity Contributor access on the subscription, allowing pods to authenticate via the local Instance Metadata Service (IMDS).
- **D.** Implement a Kubernetes CronJob that executes hourly to cycle and update default ServiceAccount Secret tokens across all application namespaces.

#### Correct Answer: B

#### Complete 4-Option Distractor Forensics

- **Option A is incorrect**: The Secrets Store CSI Driver successfully syncs secrets into pods as mounted volume files, but this mechanism still relies on static, long-lived client secrets stored in Azure Key Vault. If an attacker breaches the container and reads the mounted filesystem, the static client secret can be exfiltrated and replayed until manual rotation occurs.
- **Option B is correct**: Microsoft Entra Workload ID establishes OpenID Connect (OIDC) federation between the AKS cluster API Server and Microsoft Entra ID. Application pods exchange short-lived, projected service account tokens for short-lived Entra ID access tokens without any static secrets existing in cluster storage or container filesystems.
- **Option C is incorrect**: Relying on the node pool Managed Identity via IMDS violates the principle of least privilege. Every pod sharing that worker node can query `169.254.169.254` and assume the broad privileges assigned to the node, creating an identity blast radius where a compromise of one pod compromises the entire node identity.
- **Option D is incorrect**: Cycling default ServiceAccount secrets via an hourly CronJob introduces operational complexity and timing gaps without solving the core vulnerability. Standard Kubernetes service account tokens remain static bearer tokens during their valid window and do not provide identity federation with enterprise Entra ID governance.

---

### Question 3: Runtime Threat Remediation (NEXT Action)

Microsoft Defender for Containers alerts on `Attempt to create a new Linux namespace from a container detected` (T1611) originating from a worker node in an AKS cluster. The SOC has successfully isolated the offending pod using network security controls and preserved the container state for forensics. What is the NEXT operational action the platform engineering team must execute?

- **A.** Re-enable local cluster administrator accounts via `az aks update --enable-local-accounts` to establish out-of-band debugging access.
- **B.** Reboot the physical Azure virtual machine host supporting the worker node pool directly from the Azure portal.
- **C.** Inspect the worker node kernel logs and audit daemon events via Log Analytics, revoke compromised identity tokens, and replace the worker node by triggering an image re-baseline or node pool reimaging.
- **D.** Increase the CPU and memory limits on the pod's Deployment manifest to alleviate potential resource starvation false positives.

#### Correct Answer: C

#### Complete 4-Option Distractor Forensics

- **Option A is incorrect**: Re-enabling local administrator accounts directly violates financial compliance baselines (CIS AKS Benchmark 5.1.3 and NIST SP 800-53 AC-2). Local accounts bypass Microsoft Entra ID Conditional Access, eliminate individual user attribution, and introduce long-lived credential risks during an active security incident.
- **Option B is incorrect**: Power-cycling the VMSS instance without forensic log inspection clears operating system RAM and volatile kernel traces, preventing analysts from identifying whether kernel rootkits, modified binaries, or secondary backdoor mechanisms were deposited on the host disk.
- **Option C is correct**: After isolating the workload, the engineering team must examine host kernel and system audit records (`KubeAudit`, Syslog) to determine if the namespace breakout succeeded in modifying host files. Once verified, revoking active identity tokens and replacing the potentially compromised node via node reimaging guarantees that no resident kernel compromises persist.
- **Option D is incorrect**: Namespace creation attempts (such as invoking `unshare` or `clone` syscalls associated with CVE-2022-0185) are explicit privilege escalation and container breakout techniques. They are unrelated to compute resource limits, and increasing resource quotas does not remediate an exploit attempt.

---

### Question 4: Architectural Exclusion Evaluation (PRIMARY / EXCEPT Action)

During an annual regulatory audit, a financial institution reviews its container security monitoring coverage across the 36 MITRE ATT&CK for Containers techniques. All of the following techniques are classified as Category 4 Architectural Exclusions requiring external Azure compensating controls (such as Microsoft Entra ID, Azure WAF, or Azure Backup) EXCEPT:

- **A.** T1068 (Exploitation for Privilege Escalation)
- **B.** T1490 (Inhibit System Recovery)
- **C.** T1525 (Implant Internal Image)
- **D.** T1610 (Deploy Container: Unauthorized Pod Deployment in kube-system)

#### Correct Answer: D

#### Complete 4-Option Distractor Forensics

- **Option A is an architectural exclusion**: T1068 involves kernel and container runtime CVE exploits. Because generic runtime sensors cannot identify zero-day exploits without high false alarm rates, Defender for Containers treats this as an architectural exclusion compensated by agentless vulnerability scanning and automated node OS image patching.
- **Option B is an architectural exclusion**: T1490 targets datastore destruction and backup inhibition. In AKS, the etcd control plane datastore is managed and isolated by Azure, and persistent volume protection is compensated through Azure Backup Enhanced Soft-Delete and Immutable Blob Storage.
- **Option C is an architectural exclusion**: T1525 represents supply-chain tampering inside container registries, which occurs outside the visibility of node runtime sensors. It is compensated through ACR artifact signing with Notation and admission verification via Ratify.
- **Option D is the exception (Correct Answer)**: T1610 (Deploy Container) is directly alerted by Microsoft Defender for Containers as a native Category 2 CWPP alert (`New container in the kube-system namespace detected`). When an unauthorized pod is scheduled in `kube-system`, Defender's control plane audit analysis generates a native runtime alert without requiring external compensating services.
