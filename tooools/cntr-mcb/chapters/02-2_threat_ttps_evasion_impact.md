# Chapter 02-2: Threat TTPs Part 2: Defense Evasion, Credential Access, Discovery, Impact & Cryptomining

## 1. Statutory Baseline & Technical Control Matrix

### 1.1 Architecture & Threat Landscape Overview

Financial container platforms require continuous verification across runtime execution layers to prevent silent lateral movement, credential extraction, and malicious resource consumption. Regulatory standards, including Financial Supervisory Commission (FSC) Cloud and Container Security Guidelines, ISO/IEC 27001:2022 Controls A.8.20 and A.8.28, and NIST SP 800-190, require immutable telemetry auditing and real-time behavioral tracing. Attackers targeting containerized banking workloads frequently bypass perimeter defenses, transitioning directly into post-exploitation phases: Defense Evasion, Credential Access, Discovery, and Impact.

To maintain operational compliance, financial architectures enforce four core metrics across runtime inspection tools:

1. Mean Time to Detect (MTTD): Under 5 minutes for Critical (T0) and High (T1) threat tiers across orchestration and container runtime planes.
2. Mean Time to Remediate (MTTR): Under 15 minutes for automated container isolation, process termination, and credential invalidation.
3. False Positive Ratio (FPR): Under 3.0% across all production Cloud Workload Protection Platform (CWPP) and Security Information and Event Management (SIEM) detection rules.
4. Telemetry Ingestion Lag: Under 30 seconds from kernel system call execution to centralized SIEM event ingestion.

Modern container attacks focus on evading host sensors, harvesting workload identity tokens, querying cluster control planes, and deploying compute-intensive cryptomining payloads or destructive data wipers. Defense architectures pair kernel-level extended Berkeley Packet Filter (eBPF) telemetry with orchestrator audit streams to detect attacks before persistence hardens.

### 1.2 Master Matrix: Defense Evasion, Credential Access, Discovery, Impact & Lateral Movement

The table below documents 17 leaf-node TTPs across Defense Evasion, Credential Access, Discovery, Impact, and Lateral Movement:

| TTP ID | Threat Tier | Technique Name | Primary Tactic | Data Components | CWPP & Cloud Signature | Baseline Exception & Whitelist Policy |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| T1069 | T3 (Low) | Permission Groups Discovery | Discovery | DC0064, DC0028 | Defender: RBAC enumeration; Google: discovery_api_query | Exclude compliance audit operators (Gatekeeper, Falco). |
| T1070 | T0 (Critical) | Indicator Removal | Defense Evasion | DC0040, DC0059 | GuardDuty: SuspiciousCommand; RHACS: Log Tampering | Exclude automated log rotation daemons (logrotate). |
| T1485 | T0 (Critical) | Data Destruction | Impact | DC0064, DC0059 | GuardDuty: DataDestruction; RHACS: Mass File Deletion | Exclude ephemeral storage scratch directory cleanup. |
| T1490 | T0 (Critical) | Inhibit System Recovery | Impact | DC0064, DC0028 | GuardDuty: BackupDeleted; Defender: Backup tampering | Exclude scheduled backup lifecycle pruning jobs (Velero). |
| T1496.001 | T3 (Low) | Compute Hijacking | Impact | DC0072, DC0085 | GuardDuty: BitcoinTool.B; Google CTD: cryptomining | Exclude approved stress testing and risk simulations. |
| T1496.002 | T3 (Low) | Bandwidth Hijacking | Impact | DC0085, DC0082 | GuardDuty: TrafficVolumeUnusual; Defender: Large outbound | Exclude cross-region database replication streams. |
| T1498 | T2 (Medium) | Network Denial of Service | Impact | DC0032, DC0082 | GuardDuty: DenialOfService.Udp; Defender: Outbound DDoS | Exclude load testing traffic in isolated test node pools. |
| T1499 | T2 (Medium) | Endpoint Denial of Service | Impact | DC0018, DC0038 | Defender: Memory exhaustion; Google CTD: exhaustion | Exclude JVM heap warmup within configured cgroup limits. |
| T1525 | T0 (Critical) | Implant Internal Image | Persistence | DC0015, DC0036 | GuardDuty: SuspiciousImageUpdate; Defender: ACR tampered | Exclude automated CI/CD accounts with valid Cosign signatures. |
| T1526 | T2 (Medium) | Cloud Service Discovery | Discovery | DC0032, DC0082 | GuardDuty: InstanceMetadataQueried; Defender: IMDS queried | Exclude cloud controller managers with network exceptions. |
| T1528 | T1 (High) | Steal App Access Token | Credential Access | DC0055, DC0028 | GuardDuty: SecretsAccessed; Google SCC: secrets_api_read | Exclude secret synchronizers (External Secrets Operator). |
| T1550.001 | T1 (High) | Alternate Auth Material | Lateral Movement | DC0007, DC0028 | Defender: Anomalous token replay; Google: token_use | Exclude multi-region automated CI/CD runners. |
| T1552.001 | T1 (High) | Credentials In Files | Credential Access | DC0055, DC0064 | GuardDuty: SensitiveFileRead; RHACS: Token Read | Exclude official application runtime initialization scripts. |
| T1552.007 | T1 (High) | Container API Credentials | Credential Access | DC0002, DC0032 | GuardDuty: KubeletAPIQueried; Defender: Kubelet abuse | Exclude cluster monitoring agents (cAdvisor, Prometheus). |
| T1612 | T2 (Medium) | Build Image on Host | Persistence | DC0015, DC0034 | Defender: Host image build; RHACS: Node Image Build | Exclude dedicated build worker nodes in build subnets. |
| T1613 | T3 (Low) | Resource Discovery | Discovery | DC0037, DC0091 | Defender: Discovery commands; Google CTD: discovery | Exclude core cluster components (CoreDNS, kube-proxy). |
| T1685 | T1 (High) | Disable or Modify Tools | Defense Evasion | DC0041, DC0064 | GuardDuty: SecurityAgentTerminated; RHACS: Disconnected | Zero production workload exemptions permitted. |

### 1.3 Tactical Deep Dive & Detection as Code Specifications

#### 1.3.1 Defense Evasion & Sensor Manipulation

Adversaries evade detection by modifying audit trails, compiling software directly on worker nodes, tampering with base images, or terminating security agents.

##### T1070: Indicator Removal
- Threat Tier: T0 (Critical) | Data Components: DC0040 (docker daemon), DC0059 (eBPF syscalls)
- CWPP Runtime Detection Logic: Intercepts kernel file unlinking (unlinkat), truncation (truncate, ftruncate), shell history clearing, and redirection of log outputs to /dev/null. Monitors process activity terminating auditd, rsyslog, or container log collectors.
- Cloud Alerting Signatures: AWS (GuardDuty: DefenseEvasion:Runtime/SuspiciousCommand), Azure (Defender: Suspicious deletion of log files), GCP (CTD: log_tampering_detected), Red Hat (ACS: Log Tampering Detected), IBM (SCC: Audit Log Truncation Alert).
- Whitelist Exception Criteria: Exclude official automated log rotation scripts (logrotate) operating as UID 0 during maintenance schedules.

```yaml
title: Container Runtime Indicator Removal
logsource:
  category: process_creation
  product: linux
detection:
  selection_cmds:
    Image|endswith: ['/rm', '/shred', '/truncate']
    CommandLine|contains: ['/var/log', '.bash_history', '.ash_history', '/dev/null']
  selection_daemons:
    CommandLine|contains: ['systemctl stop auditd', 'service auditd stop', 'killall rsyslogd']
  condition: selection_cmds or selection_daemons
falsepositives:
  - Legitimate logrotate daemon executions on host worker nodes
level: critical
tags: [attack.defense_evasion, attack.t1070]
```

##### T1525: Implant Internal Image
- Threat Tier: T0 (Critical) | Data Components: DC0015 (docker daemon), DC0036 (registry)
- CWPP Runtime Detection Logic: Scans container image digests during registry upload and admissions verification. Flags tag mutation, missing cryptographic signatures (Cosign/Notary), and layers containing unexpected binaries or SSH keys.
- Cloud Alerting Signatures: AWS (GuardDuty: Persistence:Kubernetes/SuspiciousImageUpdate), Azure (Defender: Image tampered in ACR), GCP (SCC: registry_image_overwritten), Red Hat (ACS: Untrusted Registry Push Detected), IBM (SCC: Image Digest Mutation Alert).
- Whitelist Exception Criteria: Exclude certified automated CI/CD service accounts pushing signed release tags.

```yaml
title: Unauthorized Container Registry Image Mutation
logsource:
  category: application
  product: container_registry
detection:
  selection_action:
    action: 'push'
    tag_mutation: true
  filter_ci:
    user_identity|endswith: 'svc-cicd-pipeline'
    signature_valid: true
  condition: selection_action and not filter_ci
falsepositives:
  - Authorized manual image promotion during emergency break-glass procedures
level: critical
tags: [attack.persistence, attack.defense_evasion, attack.t1525]
```

##### T1612: Build Image on Host
- Threat Tier: T2 (Medium) | Data Components: DC0015 (docker daemon), DC0034 (containerd)
- CWPP Runtime Detection Logic: Employs eBPF process execution hooks to catch image compilation commands (docker build, podman build, buildah, kaniko, nerdctl build) running on general worker nodes or inside microservice pods.
- Cloud Alerting Signatures: AWS (GuardDuty: Execution:Runtime/ImageBuildCommand), Azure (Defender: Image build command executed on host node), GCP (CTD: host_image_build_detected), Red Hat (ACS: Node Image Build Detected), IBM (SCC: Unauthorized Image Build on Worker).
- Whitelist Exception Criteria: Exclude dedicated build runner nodes isolated in private build subnets.

```yaml
title: Container Image Build Executed on Workload Node
logsource:
  category: process_creation
  product: linux
detection:
  selection_binaries:
    Image|endswith: ['/docker', '/podman', '/buildah', '/nerdctl', '/kaniko']
    CommandLine|contains: ['build', 'buildah bud']
  condition: selection_binaries
falsepositives:
  - Designated CI/CD runner pods running inside isolated namespace build-workers
level: medium
tags: [attack.persistence, attack.defense_evasion, attack.t1612]
```

##### T1685: Disable or Modify Tools
- Threat Tier: T1 (High) | Data Components: DC0041 (K8s audit), DC0064 (eBPF)
- CWPP Runtime Detection Logic: Traces system calls targeting security monitoring daemons. Intercepts ptrace, kill, sigkill, daemonset manifest deletion, eBPF sensor detachment, and modification of configuration files in /etc/falco/ or /etc/datadog-agent/.
- Cloud Alerting Signatures: AWS (GuardDuty: DefenseEvasion:Runtime/SecurityAgentTerminated), Azure (Defender: Security agent tampering detected), GCP (CTD: security_agent_stopped), Red Hat (ACS: Agent Disconnected), IBM (SCC: Host Monitoring Agent Tampering).
- Whitelist Exception Criteria: Zero production workload exemptions allowed. Maintenance updates must execute via verified orchestrator rollouts.

```yaml
title: Tampering with Container Security Daemon
logsource:
  category: process_creation
  product: linux
detection:
  selection_kill:
    CommandLine|contains: ['kill -9', 'pkill -9', 'systemctl stop falco', 'systemctl stop datadog-agent', 'systemctl stop amazon-guardduty']
  selection_targets:
    CommandLine|contains: ['falco', 'guardduty', 'defender', 'stackrox', 'qradar']
  condition: selection_kill and selection_targets
falsepositives:
  - None on production nodes
level: high
tags: [attack.defense_evasion, attack.t1685]
```

#### 1.3.2 Credential Access & Lateral Movement

Adversaries extract authentication material from local filesystem projections, cloud metadata endpoints, or container control APIs to escalate privileges and move across namespaces.

##### T1528: Steal Application Access Token
- Threat Tier: T1 (High) | Data Components: DC0055 (K8s audit), DC0028 (K8s API)
- CWPP Runtime Detection Logic: Evaluates Kubernetes API Server audit logs for abnormal GET or LIST operations targeting v1/secrets. Identifies bulk secret reads initiated by application service accounts rather than configuration management operators.
- Cloud Alerting Signatures: AWS (GuardDuty: CredentialAccess:Kubernetes/SecretsAccessed), Azure (Defender: Suspicious read of Kubernetes secrets), GCP (SCC: secrets_api_read), Red Hat (ACS: Workload Secret Harvest Attempt), IBM (SCC: Secret Object Access Spike).
- Whitelist Exception Criteria: Exclude certified secret managers (External Secrets Operator, HashiCorp Vault Agent, Sealed Secrets).

```yaml
title: Kubernetes API Secret Object Harvesting
logsource:
  service: kubernetes.audit
detection:
  selection_audit:
    verb: ['get', 'list']
    objectRef.resource: 'secrets'
  filter_operators:
    user.username|contains: ['system:serviceaccount:vault:vault-agent', 'system:serviceaccount:external-secrets:external-secrets-controller']
  condition: selection_audit and not filter_operators
falsepositives:
  - Initial configuration synchronization during pod scheduling
level: high
tags: [attack.credential_access, attack.t1528]
```

##### T1550.001: Alternate Authentication Material: Application Access Token
- Threat Tier: T1 (High) | Data Components: DC0007 (K8s API), DC0028 (K8s audit)
- CWPP Runtime Detection Logic: Detects token replay across discordant IP addresses. Correlates Kubernetes audit logs where a service account token allocated to an internal pod IP is presented from public IP ranges or unmapped subnets.
- Cloud Alerting Signatures: AWS (GuardDuty: UnauthorizedAccess:Kubernetes/TorIPCaller), Azure (Defender: Anomalous token replay detected), GCP (SCC: anomalous_token_use), Red Hat (ACS: Token Replay Anomaly Detected), IBM (SCC: Service Account Token Divergence).
- Whitelist Exception Criteria: Exclude multi-region automated CI/CD runners using distributed workers.

```yaml
title: Kubernetes Service Account Token Replay External Source
logsource:
  service: kubernetes.audit
detection:
  selection_token:
    user.username|startswith: 'system:serviceaccount:'
  filter_internal_cidrs:
    sourceIPs|cidr: ['10.0.0.0/8', '172.16.0.0/12', '192.168.0.0/16']
  condition: selection_token and not filter_internal_cidrs
falsepositives:
  - Developers connecting to external development clusters with static tokens
level: high
tags: [attack.credential_access, attack.lateral_movement, attack.t1550.001]
```

##### T1552.001: Unsecured Credentials: Credentials In Files
- Threat Tier: T1 (High) | Data Components: DC0055 (eBPF syscalls), DC0064 (K8s audit)
- CWPP Runtime Detection Logic: Intercepts openat, open, and read syscalls directed toward serviceaccount tokens, cloud credential files, or .env files by non-application binaries.
- Cloud Alerting Signatures: AWS (GuardDuty: CredentialAccess:Runtime/SensitiveFileRead), Azure (Defender: Service account token read by suspicious process), GCP (CTD: service_account_token_theft), Red Hat (ACS: Service Account Token Read), IBM (SCC: Workload Credential Read Anomaly).
- Whitelist Exception Criteria: Exclude legitimate application processes specified in approved binary profiles.

```yaml
title: Unauthorized Access to Container Projected Token
logsource:
  category: file_access
  product: linux
detection:
  selection_target:
    TargetFilename|contains: ['/var/run/secrets/kubernetes.io/serviceaccount/token', '/.aws/credentials', '/.azure/credentials', '/app/.env']
  selection_suspicious_binaries:
    Image|endswith: ['/cat', '/curl', '/wget', '/sh', '/bash', '/head', '/tail']
  condition: selection_target and selection_suspicious_binaries
falsepositives:
  - Container entrypoint bootstrap scripts executing before application binary starts
level: high
tags: [attack.credential_access, attack.t1552.001]
```

##### T1552.007: Unsecured Credentials: Container API
- Threat Tier: T1 (High) | Data Components: DC0002 (K8s API), DC0032 (kubelet logs)
- CWPP Runtime Detection Logic: Monitors unauthenticated HTTP traffic hitting Kubelet read-only port 10255, Kubelet authenticated port 10250, or unencrypted Docker daemon sockets (tcp 2375).
- Cloud Alerting Signatures: AWS (GuardDuty: CredentialAccess:Kubernetes/KubeletAPIQueried), Azure (Defender: Kubelet API abuse), GCP (SCC: unauthenticated_kubelet_access), Red Hat (ACS: Insecure Kubelet Port Probed), IBM (SCC: Daemon API Unauthenticated Access).
- Whitelist Exception Criteria: Exclude Prometheus node-exporter scraping approved metrics endpoints.

```yaml
title: Unauthenticated Kubelet API Probe
logsource:
  category: network_connection
  product: linux
detection:
  selection_ports:
    DestinationPort: [10250, 10255, 2375]
  filter_master:
    SourceIp: ['10.0.1.10', '10.0.1.11']
  condition: selection_ports and not filter_master
falsepositives:
  - Approved monitoring agents with verified source IPs
level: high
tags: [attack.credential_access, attack.t1552.007]
```

#### 1.3.3 Discovery & Environment Enumeration

Adversaries enumerate cluster topologies, RBAC permissions, and cloud metadata infrastructure to identify high-value targets.

##### T1069: Permission Groups Discovery
- Threat Tier: T3 (Low) | Data Components: DC0064 (K8s audit), DC0028 (K8s API)
- CWPP Runtime Detection Logic: Analyzes API audit logs for rapid requests inspecting roles, clusterroles, rolebindings, and clusterrolebindings using can-i commands or automated discovery tools.
- Cloud Alerting Signatures: AWS (GuardDuty: Discovery:Kubernetes/RoleBindingListing), Azure (Defender: Kubernetes RBAC enumeration), GCP (SCC: discovery_api_query), Red Hat (ACS: Cluster Role Enumeration Detected), IBM (SCC: API RBAC Discovery).
- Whitelist Exception Criteria: Exclude compliance controllers (OPA Gatekeeper, Kyverno, RHACS admission controllers).

```yaml
title: Kubernetes RBAC Permission Enumeration
logsource:
  service: kubernetes.audit
detection:
  selection_rbac:
    verb: ['list', 'get']
    objectRef.apiGroup: 'rbac.authorization.k8s.io'
  filter_controllers:
    user.username|contains: ['system:kube-controller-manager', 'gatekeeper-admin']
  condition: selection_rbac and not filter_controllers
falsepositives:
  - Admin users performing maintenance troubleshooting
level: low
tags: [attack.discovery, attack.t1069]
```

##### T1526: Cloud Service Discovery
- Threat Tier: T2 (Medium) | Data Components: DC0032 (network flow), DC0082 (IMDS audit)
- CWPP Runtime Detection Logic: Intercepts network packets directed toward 169.254.169.254 (cloud Instance Metadata Service). Flags processes attempting to retrieve IAM security credentials, project IDs, or service accounts from worker nodes without token headers or from unprivileged pods.
- Cloud Alerting Signatures: AWS (GuardDuty: Recon:EC2/InstanceMetadataQueried), Azure (Defender: Cloud metadata service queried from pod), GCP (SCC: metadata_server_abused), Red Hat (ACS: Node IMDS Access Detected), IBM (SCC: Cloud Identity Endpoint Discovery).
- Whitelist Exception Criteria: Exclude cloud node agents (AWS Node Agent, Azure Network Agent) running with host networking.

```yaml
title: Cloud Metadata Service IMDS Query from Container Workload
logsource:
  category: network_connection
  product: linux
detection:
  selection_imds:
    DestinationIp: '169.254.169.254'
  filter_host_processes:
    Image|endswith: ['/aws-k8s-agent', '/cloud-init']
  condition: selection_imds and not filter_host_processes
falsepositives:
  - Workload identity bootstrapping in legacy clusters lacking IAM roles for service accounts
level: medium
tags: [attack.discovery, attack.t1526]
```

##### T1613: Container and Resource Discovery
- Threat Tier: T3 (Low) | Data Components: DC0037 (K8s API), DC0091 (docker daemon)
- CWPP Runtime Detection Logic: Detects repetitive requests querying v1/pods, v1/namespaces, v1/nodes, and v1/services originating from pod service accounts. Tracks execution of discovery utilities traversing internal API endpoints.
- Cloud Alerting Signatures: AWS (GuardDuty: Discovery:Kubernetes/AnomalousAPIQuery), Azure (Defender: Discovery commands executed in container), GCP (CTD: resource_discovery), Red Hat (ACS: Kubernetes Metadata Enumeration), IBM (SCC: Discovery Scan on Cluster Resources).
- Whitelist Exception Criteria: Exclude CoreDNS, kube-proxy, Ingress controllers, and service mesh sidecars.

```yaml
title: Container and Cluster Resource Discovery
logsource:
  service: kubernetes.audit
detection:
  selection_discovery:
    verb: 'list'
    objectRef.resource: ['pods', 'nodes', 'namespaces', 'services']
  filter_system:
    user.username|startswith: 'system:node:'
  condition: selection_discovery and not filter_system
falsepositives:
  - Microservices executing client-go for cluster leader election
level: low
tags: [attack.discovery, attack.t1613]
```

#### 1.3.4 Impact, Resource Hijacking & Denial of Service

Adversaries disrupt operations, hijack computational resources, wipe databases, or destroy backups to maximize operational damage or extract financial ransom.

##### T1485: Data Destruction
- Threat Tier: T0 (Critical) | Data Components: DC0064 (docker events), DC0059 (eBPF)
- CWPP Runtime Detection Logic: Intercepts destructive commands (rm -rf /, shred, dd if=/dev/urandom, wipefs, mkfs) executed inside container namespaces. Tracks bulk block device modifications and filesystem unmounting.
- Cloud Alerting Signatures: AWS (GuardDuty: Impact:Runtime/DataDestruction), Azure (Defender: Mass file deletion in container), GCP (CTD: data_destruction_attempt), Red Hat (ACS: Mass File System Deletion Detected), IBM (SCC: Destructive Storage Command).
- Whitelist Exception Criteria: Exclude automated ephemeral storage cleanup processes operating in temporary build directories.

```yaml
title: Mass Data Destruction Command Inside Container
logsource:
  category: process_creation
  product: linux
detection:
  selection_cmds:
    CommandLine|contains: ['rm -rf --no-preserve-root', 'rm -rf /*', 'shred -u -z', 'mkfs.', 'dd of=/dev/sd', 'wipefs -a']
  condition: selection_cmds
falsepositives:
  - None for production banking workloads
level: critical
tags: [attack.impact, attack.t1485]
```

##### T1490: Inhibit System Recovery
- Threat Tier: T0 (Critical) | Data Components: DC0064 (K8s audit), DC0028 (K8s API)
- CWPP Runtime Detection Logic: Evaluates Kubernetes API audit logs for DELETE operations targeting volumesnapshots, volumesnapshotcontents, persistentvolumeclaims, or Velero backup custom resources (backups.velero.io, backupstoragelocations).
- Cloud Alerting Signatures: AWS (GuardDuty: Impact:Kubernetes/BackupDeleted), Azure (Defender: Cluster backup resource tampering), GCP (SCC: backup_resource_deletion), Red Hat (ACS: Volume Snapshot Deletion Alert), IBM (SCC: Backup Service Disruption).
- Whitelist Exception Criteria: Exclude scheduled backup retention lifecycle pruning jobs executed by authenticated Velero controllers.

```yaml
title: Deletion of Cluster Backup and Storage Snapshots
logsource:
  service: kubernetes.audit
detection:
  selection_delete:
    verb: 'delete'
    objectRef.resource: ['volumesnapshots', 'volumesnapshotcontents', 'backups', 'backupstoragelocations']
  filter_velero:
    user.username: 'system:serviceaccount:velero:velero'
  condition: selection_delete and not filter_velero
falsepositives:
  - Storage engineers manually purging decommissioned test volume snapshots
level: critical
tags: [attack.impact, attack.t1490]
```

##### T1496.001: Resource Hijacking: Compute Hijacking
- Threat Tier: T3 (Low) | Data Components: DC0072 (containerd), DC0085 (cgroups)
- CWPP Runtime Detection Logic: Correlates CPU thread consumption spikes across container cgroup accounting with execution of mining binaries (XMRig, ccminer) and network traffic over Stratum protocol ports (3333, 4444, 5555, 7777).
- Cloud Alerting Signatures: AWS (GuardDuty: CryptoCurrency:Runtime/BitcoinTool.B), Azure (Defender: Digital currency mining detected), GCP (CTD: cryptomining_detected), Red Hat (ACS: Cryptomining Process Detected), IBM (SCC: Unauthorized Mining Worker).
- Whitelist Exception Criteria: Exclude scheduled stress testing and mathematical simulations with advance approval.

```yaml
title: Cryptomining Activity in Container Workload
logsource:
  category: process_creation
  product: linux
detection:
  selection_process:
    Image|contains: ['xmrig', 'minerd', 'cryptonight', 'ethminer']
    CommandLine|contains: ['stratum+tcp://', 'stratum+ssl://', '--donate-level=']
  selection_ports:
    DestinationPort: [3333, 4444, 5555, 7777, 9001]
  condition: selection_process or selection_ports
falsepositives:
  - Approved high-performance compute workloads executing cryptographic benchmarking
level: high
tags: [attack.impact, attack.t1496.001]
```

##### T1496.002: Resource Hijacking: Bandwidth Hijacking
- Threat Tier: T3 (Low) | Data Components: DC0085 (network metrics), DC0082 (flow logs)
- CWPP Runtime Detection Logic: Evaluates VPC Flow Logs and container network metrics for anomalous egress byte counts directed toward unclassified external IPs, peer-to-peer networks, or proxy nodes.
- Cloud Alerting Signatures: AWS (GuardDuty: Behavior:EC2/TrafficVolumeUnusual), Azure (Defender: Large outbound data transfer), GCP (SCC: egress_traffic_spike), Red Hat (ACS: Egress Network Anomaly), IBM (SCC: High Volumetric Network Egress).
- Whitelist Exception Criteria: Exclude cross-region database replication and snapshot archive backups.

```yaml
title: Abnormal Outbound Egress Volumetric Spike
logsource:
  category: network_traffic
  product: linux
detection:
  selection_egress:
    bytes_out|gt: 10737418240 # 10 GB per 5-minute interval
  filter_internal:
    destination_ip|cidr: ['10.0.0.0/8', '172.16.0.0/12']
  condition: selection_egress and not filter_internal
falsepositives:
  - Automated cloud backup synchronization pipelines
level: medium
tags: [attack.impact, attack.t1496.002]
```

##### T1498: Network Denial of Service
- Threat Tier: T2 (Medium) | Data Components: DC0032 (network metrics), DC0082 (flow logs)
- CWPP Runtime Detection Logic: Detects abnormal bursts of outbound UDP datagrams, TCP SYN flood packets, or ICMP echo requests originating from container network namespaces.
- Cloud Alerting Signatures: AWS (GuardDuty: Backdoor:EC2/DenialOfService.Udp), Azure (Defender: Outbound DDoS activity), GCP (SCC: network_dos_detected), Red Hat (ACS: Network Flooding Detected), IBM (SCC: Outbound DoS Volumetric Burst).
- Whitelist Exception Criteria: Exclude load testing traffic generated from isolated load testing node pools.

```yaml
title: Outbound Network Denial of Service Flood
logsource:
  category: network_connection
  product: linux
detection:
  selection_flood:
    packet_rate_per_second|gt: 50000
    protocol: ['udp', 'tcp_syn']
  condition: selection_flood
falsepositives:
  - Approved network stress testing pods
level: high
tags: [attack.impact, attack.t1498]
```

##### T1499: Endpoint Denial of Service
- Threat Tier: T2 (Medium) | Data Components: DC0018 (K8s events), DC0038 (docker events)
- CWPP Runtime Detection Logic: Intercepts process fork loops, rapid thread creation, excessive memory allocations exhausting node cgroups, and container crash loops inducing Kubelet node pressure.
- Cloud Alerting Signatures: AWS (GuardDuty: Impact:Runtime/ResourceExhaustion), Azure (Defender: High memory consumption exhausting host), GCP (CTD: container_exhaustion), Red Hat (ACS: Container CrashLoop OOM Event), IBM (SCC: Node Instability Resource Drain).
- Whitelist Exception Criteria: Exclude JVM heap size warmup routines within configured cgroup memory limits.

```yaml
title: Container Fork Bomb and Resource Exhaustion
logsource:
  category: process_creation
  product: linux
detection:
  selection_fork:
    process_spawn_rate_per_sec|gt: 100
    parent_process: 'sh'
  selection_patterns:
    CommandLine|contains: [':(){ :|:& };:', 'while true; do']
  condition: selection_fork or selection_patterns
falsepositives:
  - Misconfigured shell scripts running loops without delay
level: medium
tags: [attack.impact, attack.t1499]
```

---

## 2. Production Incident & Remediation Architecture

### 2.1 Incident Operational Context

A high-severity security incident occurred in a multi-tenant production Kubernetes cluster powering online retail banking and loan evaluation services. The cluster operated on Amazon EKS with Amazon Linux 2 worker nodes, integrated with AWS GuardDuty Runtime Monitoring and Calico CNI.

The threat actor obtained initial execution inside a customer credit evaluation pod following an application injection defect. The attack unfolded across five operational phases:

```
+-----------------------------------------------------------------------------------+
|                            INCIDENT ATTACK CHAIN PHASES                           |
+-----------------------------------------------------------------------------------+
| Phase 1: Local Discovery & Environment Reconnaissance                             |
|   Attacker -> Executes curl against K8s API & IMDS (T1613, T1069, T1526)          |
|                                         |                                         |
| Phase 2: Credential Extraction & Harvesting                                       |
|   Pod Filesystem -> Reads Projected ServiceAccount Token (T1552.001)              |
|   Kubelet Probe  -> Queries Unauthenticated Kubelet Port 10255 (T1552.007)        |
|                                         |                                         |
| Phase 3: Lateral Movement & Evasion Tactics                                       |
|   External Proxy -> Replays Stolen ServiceAccount Token from Foreign IP (T1550.001)|
|   Container Host -> Deletes /var/log, Zeroes .bash_history (T1070)                |
|   Sensor Tamper  -> Sends SIGKILL to Falco & GuardDuty Agent Daemons (T1685)      |
|                                         |                                         |
| Phase 4: Host Compilation & Image Hijack                                          |
|   Worker Node    -> Executes nerdctl build Directly on Host (T1612)               |
|   Image Registry -> Attempts Tag Overwrite on Internal Registry (T1525)           |
|                                         |                                         |
| Phase 5: Resource Hijacking & Data Destruction Extortion                          |
|   Compute Core   -> Launches XMRig Cryptominer via Stratum (T1496.001, T1496.002) |
|   Storage Layer  -> Purges VolumeSnapshots & Velero Backups (T1490, T1485)        |
+-----------------------------------------------------------------------------------+
```

Phase 1 (Discovery): After executing a web shell payload, the attacker invoked discovery scripts querying the Kubernetes API server for namespace resources (T1613) and checking RBAC permissions (T1069). Concurrently, the attacker sent HTTP requests to http://169.254.169.254/latest/meta-data/ (T1526) attempting to discover host EC2 role credentials.

Phase 2 (Credential Access): The attacker accessed the container filesystem token at /var/run/secrets/kubernetes.io/serviceaccount/token (T1552.001) and read mounted application database secrets. The attacker probed the internal node network on port 10255 (T1552.007) to collect unauthenticated pod metadata from the Kubelet.

Phase 3 (Lateral Movement & Evasion): Using an external Tor exit node, the attacker replayed the harvested ServiceAccount token against the public EKS API endpoint (T1550.001). Moving into an administrative pod, the attacker cleared system logs and bash history via rm -rf /var/log/* and history -c (T1070). To silence alerts, the attacker executed kill -9 against running Falco and GuardDuty eBPF sensor processes (T1685).

Phase 4 (Persistence & Evasion): The attacker used an exposed container socket to invoke nerdctl build directly on the worker node (T1612), compiling a malicious image layer, and attempted to overwrite the internal staging registry tag (T1525).

Phase 5 (Impact & Data Destruction): The attacker deployed a miner pod that saturated CPU cores and initiated outbound Stratum connections on TCP port 3333 (T1496.001, T1496.002). Upon recognizing SOC intervention, the attacker executed destructive API requests deleting VolumeSnapshot objects, PersistentVolumeClaims, and Velero backup custom resources (T1490, T1485), attempting to inhibit cluster recovery.

### 2.2 Root-Cause Defect Forensic Decomposition

Forensic investigation conducted by the incident response team identified five architectural and configuration defects:

1. Automatic ServiceAccount Token Injection (T1552.001): Workload specifications lacked automountServiceAccountToken: false. Pods that required no orchestrator access received valid API tokens by default.
2. Unrestricted Node Metadata Network Access (T1526): The cluster network lacked packet filtering rules or IMDSv2 hop limits. Workload pods could communicate with 169.254.169.254 across the node network bridge.
3. Absence of Mutable Filesystem & Process Execution Restrictions (T1070, T1612, T1685): Workload containers ran with writable root filesystems and root UID. This allowed attackers to wipe system logs, execute process kill commands, and compile image layers on the node.
4. Over-Permissive RBAC & Public API Exposure (T1528, T1550.001): Workload service accounts were mapped to cluster-wide reading roles, and the EKS control plane API endpoint remained exposed to public CIDRs without IP allowlisting.
5. Missing Immutable Snapshot Locks & Backup Retention Controls (T1485, T1490): Cloud storage volumes and Velero backup repositories lacked Object Lock (WORM compliance mode) and multi-party authorization, allowing compromised cluster credentials to purge restore points.

### 2.3 Comprehensive Defense-in-Depth Architectural Remediation

To permanently remediate the systemic defects, engineering deployed an integrated defense-in-depth model across four operational layers:

```
+-----------------------------------------------------------------------------------+
|               FOUR-LAYER DEFENSE-IN-DEPTH ARCHITECTURAL REMEDIATION               |
+-----------------------------------------------------------------------------------+
| LAYER 1: PREVENTATIVE ADMISSION CONTROLS                                          |
| - OPA Gatekeeper / Kyverno: Enforce Pod Security Standards "Restricted" profile.  |
| - Block privileged: true, hostPID, hostNetwork, and writable root filesystems.    |
| - Inject automountServiceAccountToken: false across all application namespaces.   |
| - Require Cosign cryptographic signature verification before image admission.     |
+-----------------------------------------------------------------------------------+
| LAYER 2: RUNTIME BEHAVIORAL PROFILING & SENSOR PROTECTION                         |
| - GuardDuty Runtime Monitoring & Falco eBPF daemons deployed with filesystem locks|
| - Intercept execve(), openat(), and unlinkat() system calls in real time.         |
| - Automatically terminate containers executing shell invocations or log wipe.     |
| - Deploy systemd Watchdog to restart and alert if security daemons receive signal.|
+-----------------------------------------------------------------------------------+
| LAYER 3: NETWORK MICROSEGMENTATION & METADATA HARDENING                           |
| - Calico CNI: Default-deny egress policy restricting inter-pod communications.    |
| - Enforce IMDSv2 with HttpPutResponseHopLimit=1 on worker nodes to block pods.    |
| - Restrict Kubernetes API endpoint to internal corporate VPN CIDR blocks.         |
| - Block outbound Stratum mining ports (3333, 4444, 5555, 7777) at firewalls.      |
+-----------------------------------------------------------------------------------+
| LAYER 4: SIEM CORRELATION & IMMUTABLE DISASTER RECOVERY                           |
| - Stream Kubernetes audit logs and CWPP findings to centralized SIEM.            |
| - Automated SOAR playbooks: Cordon, drain, and quarantine nodes upon T0/T1 alert. |
| - Configure AWS S3 Object Lock (Compliance Mode) for Velero backups and snapshots|
| - Multi-party approval required for snapshot deletion or retention adjustments.   |
+-----------------------------------------------------------------------------------+
```

Layer 1 (Preventative Admission Controls): Deployed Kyverno policies enforcing the Pod Security Standards Restricted profile. Policies block pods requesting root capabilities, writable root filesystems (readOnlyRootFilesystem: true), or host namespaces. Admission rules inject automountServiceAccountToken: false on all application pods. Image admission requires valid Sigstore Cosign cryptographic signatures.

Layer 2 (Runtime Behavioral Profiling & Sensor Protection): Hardened CWPP runtime agents on all worker nodes. Falco rules hook file operations to prevent log deletion (unlinkat) and kill unauthorized shell processes immediately. Sensor daemons run with systemd protection (Restart=always, RestartSec=2s) and communicate with host watchdogs that raise P0 alerts if monitoring agents disconnect.

Layer 3 (Network Microsegmentation & Metadata Hardening): Enforced default-deny Calico network policies across all application namespaces. Worker nodes configure HttpPutResponseHopLimit=1 on EC2 metadata, preventing packets originating in container network namespaces from reaching 169.254.169.254. Blocked external egress ports associated with cryptocurrency mining pools. Restricted EKS control plane API access to corporate CIDRs.

Layer 4 (SIEM Correlation & Immutable Disaster Recovery): Unified audit log streams into the enterprise SIEM with sub-30-second latency. Automated SOAR playbooks isolate compromised pods, revoke affected service account tokens, and cordon worker nodes within 60 seconds of a confirmed T0/T1 alert. Velero backup buckets and Amazon EBS volume snapshots enforce S3 Object Lock in Compliance Mode with a 90-day retention lock, preventing attackers from deleting recovery artifacts even with administrative credentials.

---

## 3. Exam Question Bank & Distractor Forensics

### Question 1: Operational Sequence (FIRST Action)
During a financial reporting cycle, the Security Operations Center (SOC) detects concurrent alerts indicating that an unprivileged microservice container inside the payment processing namespace has executed rm -rf /var/log/* (T1070) and sent a SIGKILL signal to the local CWPP monitoring agent daemon (T1685). Which operational action must the incident response engineer execute FIRST?

- A. Issue an automated orchestrator command to cordon and isolate the affected worker node via network policy default-deny.
- B. Submit a ticket to the cloud provider support desk requesting host snapshot retrieval.
- C. Connect into the container via kubectl exec to run diagnostic commands and collect memory artifacts.
- D. Delete the affected Kubernetes deployment manifest to trigger automatic pod recreation.

#### Distractor Forensics:
- Option A is the CORRECT answer. When a threat actor actively tampers with security sensors (T1685) and deletes indicator logs (T1070), immediate containment is mandatory to stop lateral movement and cluster-wide evasion. Cordoning the worker node and enforcing an immediate network policy default-deny halts network communication and prevents scheduling new workloads on the compromised host, while preserving volatile memory state for forensic analysis.
- Option B is incorrect. Submitting an external cloud support ticket introduces unacceptable delays during an active defense evasion incident, violating the 15-minute MTTR mandate.
- Option C is incorrect. Executing kubectl exec into an active compromise modifies process trees, alters file access timestamps, contaminates forensic integrity, and warns the attacker of SOC detection.
- Option D is incorrect. Deleting the deployment manifest destroys the running container environment and ephemeral storage, eradicating critical digital forensic evidence.

### Question 2: Architectural Optimization (BEST/MOST Effective Control)
A banking architecture team seeks to prevent workload pods from querying the cloud Instance Metadata Service (169.254.169.254) to steal node-level IAM credentials (T1526, T1552). Which combination of controls provides the BEST and MOST effective architectural protection?

- A. Installing antivirus software inside all container base images during the build stage.
- B. Enforcing IMDSv2 with HttpPutResponseHopLimit=1 on worker nodes and deploying default-deny container network policies restricting egress to link-local addresses.
- C. Granting full administrative IAM roles to worker node instance profiles so individual pods do not require tokens.
- D. Increasing worker node compute memory limits to absorb metadata connection requests.

#### Distractor Forensics:
- Option A is incorrect. Antivirus software embedded within container images cannot intercept network layer packets directed at link-local addresses and increases container image attack surfaces.
- Option B is the CORRECT answer. Setting the IMDSv2 hop limit to 1 ensures that HTTP PUT packets generated inside container network namespaces cannot traverse the node network bridge, as the IP packet Time-To-Live (TTL) decrements to zero. Pairing this with Kubernetes network policies restricting egress to 169.254.169.254 provides deterministic defense-in-depth against cloud metadata harvesting.
- Option C is incorrect. Granting full administrative IAM roles to worker node instance profiles violates least privilege, dramatically increasing the impact of node compromise.
- Option D is incorrect. Adjusting memory limits addresses compute performance rather than network security boundaries.

### Question 3: Incident Response Pipeline (NEXT Step)
A cluster administrator detects and terminates an illicit XMRig cryptomining container (T1496.001) that was deployed by an external identity using a stolen service account token (T1550.001). Active mining network traffic on port 3333 has halted. What is the NEXT operational step the response team must execute?

- A. Mark the incident closed in the ticketing system and return monitoring dashboards to standard view.
- B. Invalidate the compromised ServiceAccount token, revoke active API server sessions, review audit logs for unauthorized RBAC or resource changes, and audit backup integrity.
- C. Permanently wipe all underlying storage arrays and reinstall the physical virtualization hypervisors.
- D. Purchase reserved cloud compute instances to offset computational losses caused by the mining process.

#### Distractor Forensics:
- Option A is incorrect. Closing the ticket immediately after terminating the mining process ignores the compromised authentication credential, leaving the cluster vulnerable to re-infection.
- Option B is the CORRECT answer. After initial containment, the eradication and recovery phase requires revoking the compromised credential, invalidating tokens, auditing control plane logs for secondary backdoors or RBAC modifications (T1528, T1098.006), and verifying that backup snapshots remain untampered (T1490).
- Option C is incorrect. Rebuilding physical hypervisors is a disproportionate response for an isolated credential compromise that has already been contained.
- Option D is incorrect. Purchasing compute capacity validates adversary resource theft and fails to remediate the underlying vulnerability.

### Question 4: Architectural Boundary (PRIMARY/EXCEPT Analysis)
When configuring CWPP runtime detection engines and admission controls to defend financial container environments against data destruction and system recovery inhibition (T1485, T1490), all of the following controls represent valid hardening practices EXCEPT:

- A. Enforcing S3 Object Lock in Compliance Mode on container backup repositories to prevent snapshot deletion.
- B. Deploying admission controllers that prevent containers from mounting the host root filesystem (hostPath: /).
- C. Disabling automated backup deletion lifecycle pruning policies across backup controllers.
- D. Configuring workload containers with privileged: true and CAP_SYS_ADMIN to enable automated local volume formatting.

#### Distractor Forensics:
- Option A is incorrect (valid practice). S3 Object Lock in Compliance Mode prevents data destruction by prohibiting deletion of backup objects even by root cloud credentials until the retention period expires.
- Option B is incorrect (valid practice). Preventing hostPath: / volume mounts blocks containers from accessing and destroying underlying node block devices and filesystems.
- Option C is incorrect (valid practice). Removing automated lifecycle pruning policies prevents adversaries from exploiting automated deletion jobs to purge restore points during an incident.
- Option D is the CORRECT answer (the invalid practice to identify). Granting privileged: true and CAP_SYS_ADMIN dismantles container namespace and capability barriers, giving workloads unrestricted ability to wipe host storage devices (T1485) and escape to the host. This directly violates CIS Kubernetes Benchmark Controls 5.2.1 and 5.2.5.
