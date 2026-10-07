# Chapter 6: IBM Cloud & Red Hat OpenShift Container Security Monitoring Baseline

## Section 1: Statutory Baseline & Technical Control Matrix

### 1.1 Regulatory Mandates and Architectural Foundations

Financial institutions operating containerized workloads must maintain strict auditability, workload isolation, and configuration governance. Cloud environments require rigorous compliance mapping across commercial and open-source orchestration distributions. The primary regulatory frameworks governing these deployments include the IBM Cloud Framework for Financial Services (FS Cloud), the Center for Internet Security (CIS) Benchmarks, and the MITRE ATT&CK for Containers taxonomy. Compliance requires establishing continuous configuration monitoring, runtime workload protection, and immutable telemetry retention.

IBM Cloud Kubernetes Service (IKS) and Red Hat OpenShift on IBM Cloud (ROKS) deliver enterprise container orchestration where the control plane is fully managed by cloud provider infrastructure teams. The managed control plane isolates Kubernetes master components, API servers, controller managers, and etcd data stores within dedicated, provider-monitored network zones. Financial organizations retain operational responsibility for worker nodes, network isolation policies, identity bindings, and container runtime security. IBM Cloud Security and Compliance Center (SCC) provides unified posture management and workload protection:
- **SCC Workload Protection (SCCWP)**: Delivers Cloud Workload Protection Platform (CWPP) capabilities using an eBPF-based instrumentation engine. It monitors Linux kernel system calls in real time, inspects container images for Common Vulnerabilities and Exposures (CVE), and alerts on anomalous execution behaviors such as privilege escalations, reverse shells, and container escapes.
- **SCC Posture Management**: Delivers Cloud Security Posture Management (CSPM) capabilities by continuously evaluating cloud configurations against the CIS IBM Cloud Foundations Benchmark, FS Cloud baseline, and MITRE ATT&CK for Enterprise. It tracks configuration drift and provides automated remediation guidance.

Red Hat OpenShift Container Platform (OCP) delivers a hardened hybrid cloud application platform built upon Kubernetes. When deployed as OpenShift Platform Plus, the platform incorporates an integrated defensive toolchain:
- **Red Hat Advanced Cluster Security for Kubernetes (RHACS)**: Built upon the StackRox architecture, RHACS provides Kubernetes-native security across build, deploy, and runtime lifecycles. Its distributed architecture consists of `Central` (the central management plane handling policy management, risk scoring, and data persistence), `Sensor` (the in-cluster monitoring agent handling Kubernetes API event collection and admission control enforcement), and `Collector` (a DaemonSet running on every cluster node that uses eBPF probes or kernel modules to capture process execution, network connections, and file activity).
- **Compliance Operator**: Automates compliance auditing by executing declarative OpenSCAP scans directly against cluster nodes and platform resources. It continuously measures posture against CIS Red Hat OpenShift Container Platform Benchmark v1.9.0 (profiles `ocp4-cis` and `ocp4-cis-1-9`), NIST SP 800-53, and PCI-DSS.
- **Red Hat Quay**: Serves as a private container registry providing automated container image vulnerability scanning via Clair, cryptographic image signing validation, and automated build pipelines.

---

### 1.2 Quantitative Telemetry Architecture & Operational Telemetry Metrics

To satisfy regulatory oversight, financial container platforms must collect continuous telemetry across API requests, kernel syscalls, process executions, and network flows. Security Operations Centers (SOC) must monitor defined Key Performance Indicators (KPI), Key Risk Indicators (KRI), and Key Control Indicators (KCI) to detect attacks and control configuration drift.

| Metric Identifier | Metric Category | Formula & Telemetry Source | Regulatory Target Threshold | Assessment Cadence |
|---|---|---|---|---|
| **KPI-SEC-01** | Mean Time to Detect (MTTD) | Time from initial kernel syscall execution to alert creation in SCCWP / RHACS | $\le 60	ext{ seconds}$ | Continuous (P0/P1 alerts) |
| **KPI-SEC-02** | Mean Time to Isolate (MTTI) | Time elapsed from alert generation to automated network isolation or pod termination | $\le 120	ext{ seconds}$ | Continuous automated response |
| **KPI-SEC-03** | Telemetry Ingestion Fidelity | $rac{	ext{Successfully Ingested Audit Events}}{	ext{Total Emitted Audit Events}} 	imes 100\%$ | $100\%	ext{ (zero dropped traces)}$ | Hourly automated heartbeat |
| **KPI-SEC-04** | Compliance Drift Resolution Time | Time from discovery of non-compliant configuration to verification of applied fix | $\le 24	ext{ hours (Critical/High)}$; $\le 7	ext{ days (Medium/Low)}$ | Daily posture report |
| **KRI-SEC-01** | Anonymous API Invocation Count | Sum of authorized API requests where `ka.user.name == "system:anonymous"` | $0	ext{ permitted transactions}$ | Real-time immediate trigger |
| **KRI-SEC-02** | Privileged Workload Ratio | $rac{	ext{Pods with Privileged Flag or Host Mounts}}{	ext{Total Running Pods}} 	imes 100\%$ | $< 2\%	ext{ (strictly limited to system namespaces)}$ | Daily scheduled audit |
| **KRI-SEC-03** | Unapproved Image Deployment Volume | Count of containers instantiated from registries outside Quay / IBM ICR allowlists | $0	ext{ unapproved executions}$ | Real-time admission alert |
| **KCI-SEC-01** | Break-Glass Annotation Expiration | Percentage of emergency bypass annotations revoked within the authorized maintenance window | $100\%	ext{ revoked within } \le 4	ext{ hours}$ | Continuous admission check |
| **KCI-SEC-02** | Service Account Token Isolation | Percentage of workload pods configured with `automountServiceAccountToken: false` | $\ge 95\%	ext{ of business workloads}$ | Continuous deployment audit |

---

### 1.3 Telemetry Taxonomy & Ingestion Pipelines

Establishing defensive monitoring requires mapping raw operating system and orchestrator data streams into standardized Data Component (DC) tags. The following matrices define the required telemetry streams for IBM Cloud and Red Hat OpenShift.

#### 1.3.1 IBM Cloud Telemetry Mapping

IBM Cloud uses Activity Tracker for control plane auditability and IBM Cloud Logs for cluster infrastructure and application output. SCCWP inspects runtime activity and registry events directly.

| Data Component Tag | Native Data Stream | IBM Cloud Native Service | Security Monitoring Function |
|---|---|---|---|
| `kubernetes:audit` | Kubernetes Audit Log | IBM Cloud Activity Tracker | Records identity, source IP, verb, and URI for all Kubernetes API Server interactions |
| `kubernetes:events` | Kubernetes Events | IBM Cloud Logs | Tracks cluster state transitions, pod scheduling, and health check failures |
| `kubernetes:apiserver` | K8s API Server Logs | IBM Cloud Activity Tracker | Audits authentication and admission controller evaluation results |
| `kubernetes:orchestrator` | Controller Manager / Scheduler Logs | IBM Cloud Logs | Records reconciliation operations and workload placement events |
| `docker:events` / `containerd:events` | Container Engine Events | IBM Cloud SCCWP | Monitors container creation, start, stop, pause, and destroy operations |
| `docker:daemon` / `containerd:runtime` | Container Runtime Logs | IBM Cloud Logs | Tracks node-level container runtime health and low-level execution errors |
| `docker:api` | Container Engine API Logs | IBM Cloud Activity Tracker | Audits direct administrative requests to container engines on worker nodes |
| `docker:registry` | Container Registry Logs | SCCWP / IBM Cloud Logs | Captures image upload, pull, vulnerability scan, and metadata alteration events |
| `ebpf:syscalls` | Kernel Syscall Telemetry | IBM Cloud SCCWP | Intercepts system calls (`execve`, `fork`, `connect`, `open`) via eBPF probes |
| `docker:stats` | Container Resource Metrics | IBM Cloud Logs | Measures CPU, memory, and network usage to identify resource exhaustion |

#### 1.3.2 Red Hat OpenShift Telemetry Mapping

Red Hat OpenShift categorizes telemetry into Application, Infrastructure, and Audit categories. ClusterLogForwarder routes these records to centralized storage platforms such as OpenShift Logging (Loki/Elasticsearch) or external SIEM systems over TLS.

| Log Category | Logical Data Origin | Node Path & Service Origin | Operational Definition & Content |
|---|---|---|---|
| **Application** | Non-system namespace Pod logs | `/var/log/containers/*.log` | Captures `stdout` and `stderr` streams from business microservices |
| **Infrastructure** | System pods (`openshift-*`, `kube-*`) and node OS services | `/var/log/containers/*.log`, `journald` (crio, kubelet) | Captures platform controller output, container engine events, and operating system daemon logs |
| **Audit** | Kubernetes API Server | `/var/log/kubeapiserver/audit.log` | Records administrative actions and state changes against the Kubernetes API |
| **Audit** | OpenShift API Server | `/var/log/openshiftapiserver/audit.log` | Records OpenShift-specific API actions (Routes, BuildConfigs, ImageStreams) |
| **Audit** | OAuth Authentication Server | `/var/log/oauthapiserver/audit.log`, `/var/log/oauthserver/audit.log` | Audits user logins, token grants, and identity provider interactions |
| **Audit** | Linux Kernel Audit Daemon | `/var/log/audit/audit.log` (auditd) | Captures host-level security audit events, privilege escalations, and system file changes |
| **Audit** | OVN-Kubernetes CNI | `/var/log/ovn/acl-auditlog.log` | Records network security policy enforcement and ACL packet drop/allow events |

---

### 1.4 MITRE ATT&CK for Containers Coverage & Detection Control Matrix

This matrix correlates the 36 MITRE ATT&CK for Containers techniques across IBM Cloud (SCCWP native rules / Activity Tracker) and Red Hat OpenShift (RHACS native alerts / tunable security policies). It defines detection mechanisms, severities, triggers, and architectural exclusions.

| TTP ID | Threat Technique | IBM Cloud Detection (SCCWP / Activity Tracker) | Red Hat OpenShift Detection (RHACS / Policies) | Severities | Behavioral Trigger Logic & Technical Boundaries |
|---|---|---|---|---|---|
| **T1036.005** | Masquerading: Match Legitimate Name | SCCWP: `Create files below dev` | RHACS Policy: `Kubernetes Actions: Masquerading Process Detection` | IBM: Med / RH: High | IBM flags files created in `/dev` (excluding tty/devices); RH detects processes executing from `/tmp`, `/dev/shm` matching system names (`kubelet`, `crio`). |
| **T1036.010** | Masquerading: Masquerade Task or Service | SCCWP: `Create Disallowed Namespace` | RHACS Policy: `Kubernetes Actions: Symlink Masquerading Detection` | IBM: Med / RH: Med | IBM detects spoofed administrative namespace names; RH tracks `ln` commands linking binaries (`oc`, `kubelet`, `crio`) to non-standard paths. |
| **T1046** | Network Service Discovery | SCCWP: `Launch Suspicious Network Tool in Container` | RHACS Native: `ACS: nmap Execution`, `ACS: Netcat Execution Detected` | IBM: High / RH: High | Intercepts port scanners (`nmap`, `nc`, `curl`) probing internal VPC/pod subnets; RH separates scanner execution by tool severity. |
| **T1053.007** | Scheduled Task: Container Lifecycle Hooks | SCCWP: `K8s CronJob Created/Modified` | RHACS Native: `ACS: crontab Execution` | IBM: Med / RH: Med | IBM triggers on `kevt` `kmodify` targeting `CronJob` with `response_successful`; RH blocks `crontab`, `cron`, `crond` processes inside containers. |
| **T1059.013** | Command and Scripting: Container Orchestration API | Architectural Exclusion / Activity Tracker API Logging | RHACS Policy: `Container CLI/API Execution Detected` | IBM: Low / RH: High | IBM isolates managed control plane, requiring Activity Tracker audit; RH policy alerts on `kubectl`, `oc`, `crictl`, `podman`, `docker` inside pods. |
| **T1068** | Exploitation for Privilege Escalation | SCCWP: `Anonymous Request Allowed` | RHACS Policy: `Investigate the process execution` | IBM: Crit / RH: High | IBM alerts on `system:anonymous` permitted requests (`ka.auth.decision = allow`); RH flags escape tools (`nsenter`, `capsh`, `su`), permissions (`chmod` UID 0), live text editors. |
| **T1069** | Permission Groups Discovery | SCCWP: `Active Directory Connection Detected` | RHACS Policy: `Detect RBAC and Group Discovery(T1069)` | IBM: Med / RH: High | IBM flags outbound port 389 LDAP queries; RH detects `oc/kubectl auth can-i`, `-A` dumps, or API calls enumerating `Roles` and `RoleBindings`. |
| **T1070** | Indicator Removal | SCCWP: `K8s Event Delete` | RHACS Policy: `Indicator Removal Activity` | IBM: Med / RH: High | IBM audits deletion of `Pod`, `Deployment`, `Service`; RH intercepts `rm`, `truncate`, `history -c` targeting `/var/log` or `.bash_history`. |
| **T1078.001** | Valid Accounts: Default Accounts | SCCWP: `Full K8s Administrative Access` | RHACS Native: `ACS: Secure Shell Server(sshd)Execution` | IBM: Crit / RH: High | IBM flags non-whitelisted identities using `cluster-admin`; RH blocks `sshd` daemon execution in containers using default credentials. |
| **T1078.003** | Valid Accounts: Local Accounts | SCCWP: `System user interactive` | RHACS Native: `ACS: Secure Shell Server(sshd)Execution` | IBM: High / RH: High | IBM detects interactive sessions by system accounts (`bin`, `daemon`, `nobody`); RH blocks interactive SSH sessions on workload pods. |
| **T1098.006** | Account Manipulation: Additional Cloud Roles | SCCWP: `User Management Event Detected` | RHACS Native: `ACS: Shadow File Modification`, `ACS: Password Binaries`, `ACS: Linux User/Group Add` | IBM: High / RH: High | IBM detects account and `ClusterRoleBinding` modifications; RH blocks execution of `passwd`, `useradd`, `groupadd`, `usermod`, `vipw`. |
| **T1110.001** | Brute Force: Password Guessing | SCCWP: `Brute-force Tool Detected` | RHACS Policy: `Kubernetes Actions: Brute Force Tool Execution` | IBM: High / RH: High | Detects repeated authentication failures and brute force binaries (`hydra`, `ncrack`, `medusa`, `patator`, `brutespray`). |
| **T1110.003** | Brute Force: Password Spraying | SCCWP: `Brute-force Tool Detected` | RHACS Policy: `Kubernetes Actions: Password Spraying Tool Detection` | IBM: High / RH: High | Identifies horizontal password spray attempts across accounts (`spraycharles`, `kerbrute`, `gobuster`, `ffuf`). |
| **T1110.004** | Brute Force: Credential Stuffing | SCCWP: `Brute-force Tool Detected` | RHACS Policy: `Kubernetes Actions: Credential Stuffing Tooling Detection` | IBM: High / RH: High | Detects `sshpass` execution and headless browser automation (`chromedriver`, `geckodriver`, `puppeteer`, `selenium-server`). |
| **T1133** | External Remote Services | SCCWP: `Kubernetes Dashboard exposed` | RHACS Policy: `External-Remote-Services-Exposure` | IBM: High / RH: High | IBM detects exposure of administrative dashboards; RH flags `LoadBalancer` or `NodePort` opening sensitive ports (`22`, `3389`, `1194`, `5900`). |
| **T1136.001** | Create Account: Local Account | SCCWP: `Suspicious Home Directory Creation` | RHACS Native: `ACS: Linux Group Add Execution` | IBM: Med / RH: High | IBM detects accounts mapped to `/dev/null`, `/dev/shm`, `/tmp`; RH flags group creation commands (`groupadd`, `addgroup`) in containers. |
| **T1190** | Exploit Public-Facing Application | SCCWP: `Ingress Object without TLS Certificate Created` | RHACS Policy: `Web-Exploit-Detection` | IBM: High / RH: Crit | IBM flags non-TLS ingress routes; RH detects web daemons (`java`, `nginx`, `httpd`, `node`) spawning shells (`bash`, `sh`, `nc`, `curl`). |
| **T1204.003** | User Execution: Malicious Image | SCCWP: `Launch Disallowed Container` | RHACS Policy: `User Execution: Malicious Image` | IBM: High / RH: High | Blocks pods from unapproved registries (enforcing Quay / IBM ICR allowlists and rejecting unapproved public digests). |
| **T1485** | Data Destruction | SCCWP: `Clear Log Activities` | RHACS Policy: `Unauthorized Data Destruction Activity` | IBM: High / RH: High | IBM detects processes deleting logs in `/var/log`; RH flags destructive binaries (`shred`, `rm -rf`, `mkfs`, `dd`, `wipe`). |
| **T1490** | Inhibit System Recovery | SCCWP: `Detect malicious cmdlines` | RHACS Policy: `Inhibit System Recovery Detection` | IBM: High / RH: High | IBM identifies tampering with recovery scripts or systemd targets; RH stops backup destruction tools (`velero`, `restic`, `wbadmin`). |
| **T1496.001** | Resource Hijacking: Compute Hijacking | SCCWP: `Kubernetes Dashboard exposed` (Cryptomining signature) | RHACS Native: `ACS: Cryptocurrency Mining Process Execution` | IBM: High / RH: High | Intercepts cryptomining binaries (`xmrig`, `cgminer`, `cpuminer`, `minerd`, `ethminer`) and prolonged abnormal CPU consumption. |
| **T1496.002** | Resource Hijacking: Bandwidth Hijacking | SCCWP: `Kubernetes Dashboard exposed` (Bandwidth signature) | RHACS Native: `ACS: Cryptocurrency Mining Process Execution` | IBM: High / RH: High | Detects sustained high-rate outbound connections to mining pools, proxy relays, or TOR exit nodes. |
| **T1498** | Network Denial of Service | SCCWP: `Host Port Scan Detected` | RHACS Policy: `Network Denial of Service Detection` | IBM: Med / RH: High | Identifies high-rate outbound packet floods and DoS testing suites (`hping3`, `slowhttptest`, `nping`, `mz`, `loic`). |
| **T1499** | Endpoint Denial of Service | SCCWP: `Suspicious Operations with Firewalls` | RHACS Policy: `Endpoint Denial of Service - Resource Stressing` | IBM: High / RH: High | IBM catches host firewall edits (`iptables`, `nftables`); RH flags missing CPU limits paired with stress tools (`stress`, `stress-ng`). |
| **T1525** | Implant Internal Image | SCCWP: `Container image built on host` | RHACS Policy: `Implant Internal Image` | IBM: High / RH: High | IBM alerts on `docker/podman/buildah build` on host; RH catches cluster administration tools (`oc`, `kubectl`, `vault`) querying secrets. |
| **T1528** | Steal Application Access Token | SCCWP: `Ingress NGINX Annotation Validation Potential Bypass (CVE-2024-7646)` | RHACS Policy: `Unauthorized Access to Service Account Token` | IBM: High / RH: High | IBM flags newline injection (`\r`) in ingress annotations; RH detects non-whitelisted processes reading `/var/run/secrets/.../token`. |
| **T1543.005** | Create or Modify System Process: Container Host Process | SCCWP: `Suspicious Docker Options` | RHACS Native: `ACS: chkconfig/systemctl/systemd Execution` | IBM: High / RH: Low | IBM flags dangerous flags (`--device=/dev`, `--restart always`); RH flags service initialization commands inside containers. |
| **T1550.001** | Use Alternate Authentication Material: Application Access Token | SCCWP: `Exfiltration of K8s Service Account Token` | RHACS Policy: `Kubernetes Actions: Unauthorized ServiceAccount Token Access` | IBM: High / RH: High | IBM correlates GTFO bin token extraction with exfiltration; RH flags scripts (`curl`, `python`, `nc`, `bash`) accessing SA token paths. |
| **T1552.001** | Unsecured Credentials: Credentials In Files | SCCWP: `Unusual access to bash history file` | RHACS Native: `ACS: OpenShift: Kubernetes Secret Accessed by Impersonated User / Admin Secrets` | IBM: High / RH: High | IBM detects hard links to sensitive credential files; RH flags unauthorized reads targeting `kubeadmin` and `central-htpasswd` secrets. |
| **T1552.007** | Unsecured Credentials: Container API | SCCWP: `Untrusted Node Successfully Joined the Cluster` | RHACS Native: `ACS: OpenShift: Kubernetes Secret Accessed by an Impersonated User` | IBM: High / RH: Med | IBM detects rogue worker node joins; RH intercepts API impersonation headers used to retrieve cluster secrets. |
| **T1609** | Execution in Container | SCCWP: `Create HostNetwork Pod` | RHACS Native: `ACS: Kubernetes Actions: Exec into Pod` | IBM: High / RH: High | IBM flags pods with `hostNetwork: true`; RH flags API requests targeting the `PODS_EXEC` subresource. |
| **T1610** | Deploy Container | SCCWP: `Attach/Exec Pod` | RHACS Native: `ACS: Emergency Deployment Annotation` | IBM: High / RH: High | IBM flags unauthorized pod attach/exec requests; RH detects bypass annotations (`admission.stackrox.io/break-glass`). |
| **T1611** | Escape to Host | SCCWP: `Create Sensitive Mount Pod` | RHACS Native: `ACS: Iptables or nftables Executed in Privileged Container` | IBM: High / RH: Crit | IBM flags host volume mounts (`hostPath` pointing to `/`, `/proc`); RH detects privileged containers executing `iptables` or `nft`. |
| **T1612** | Build Image on Host | SCCWP: `Container image built on host` | RHACS Policy: `Unauthorized Image Build Tool Execution` | IBM: High / RH: High | Intercepts image build utilities (`buildah`, `podman`, `docker`, `kaniko`, `img`) executed on host nodes or inside containers. |
| **T1613** | Container and Resource Discovery | SCCWP: `Brute-force Tool Detected` (Discovery signature) | RHACS Native: `ACS: Process Targeting K8s Service / Docker Stats / Kubelet Endpoint` | IBM: Med / RH: High | IBM detects discovery commands (`kubectl get pods`); RH intercepts calls targeting API Server, cAdvisor (4194), or Kubelet (10250, 10248). |
| **T1685** | Modify System Image | SCCWP: `Change memory swap options` | RHACS Policy: `Disable or Modify Security Tools and Logs`, `Kubernetes Security Resource Tampering` | IBM: Med / RH: High | IBM monitors swap modifications; RH alerts on `auditctl -e 0`, `/var/log` wiping, or `NetworkPolicy`/`EgressFirewall` deletions. |

---

### 1.5 SIEM Integration & Metadata Enrichment Standards

Forwarding container alerts to enterprise SIEM platforms requires structured metadata enrichment. Without Kubernetes context (cluster identity, namespace, pod name, container ID, and service account), Security Operations Center analysts cannot triage container incidents effectively.

#### 1.5.1 IBM QRadar Integration Architecture
IBM Cloud Activity Tracker exports API audit logs directly to IBM QRadar using encrypted syslog or Object Storage ingestion pipelines. In addition, SCCWP forwards runtime eBPF detections into QRadar via standard event routing.
- **Diagnostic Forwarding Configuration**: Financial deployments must configure Activity Tracker event routing rules to stream all control plane audit logs directly to the enterprise SIEM collector with TLS 1.3 encryption.
- **Kubernetes Metadata Enrichment**: Alerts dispatched from SCCWP must retain the complete Kubernetes metadata context, including `k8s.cluster.name`, `k8s.namespace.name`, `k8s.pod.name`, `k8s.pod.id`, and `k8s.serviceaccount.name`.
- **Temporal Event Correlation**: QRadar correlation rules must join control plane identity events with worker node runtime alerts. When Activity Tracker records a credential modification or deployment creation by an unusual identity, and SCCWP generates a `Create Sensitive Mount Pod` or `Launch Disallowed Container` alert within a 300-second window, QRadar raises a high-priority incident.

#### 1.5.2 Red Hat OpenShift SIEM Integration Architecture
OpenShift clusters employ the ClusterLogForwarder custom resource to stream Application, Infrastructure, and Audit logs to enterprise SIEM collectors such as Splunk, QRadar, or Microsoft Sentinel.
- **Direct Policy Violation Forwarding**: RHACS automatically translates internal policy evaluation results into standard alert messages containing the policy name (e.g., `ACS: Shadow File Modification`). SOC teams can match directly on the rule identifier without constructing manual search queries against raw audit logs.
- **Loki & SIEM Log Correlation**: Log forwarders collect container logs from `/var/log/containers/*.log` alongside node audit records from `/var/log/audit/audit.log` and API audit logs from `/var/log/kubeapiserver/audit.log`. Forwarders enrich these events with container labels, pod annotations, and node identifiers before transmitting them over mTLS channels.

---

## Section 2: Production Incident & Remediation Architecture

### 2.1 Enterprise Operating Context

A Tier-1 financial institution operates a hybrid banking architecture supporting retail customer transactions. The core transactional accounting system runs on an on-premises Red Hat OpenShift Container Platform (OCP 4.14) cluster. The customer-facing digital banking microservices run on Red Hat OpenShift on IBM Cloud (ROKS 4.14) in multi-zone regions. Both environments connect to a centralized IBM QRadar SIEM platform for enterprise threat detection.

---

### 2.2 Attack Lifecycle & Root-Cause Technical Defects

An adversary executed a multi-stage production compromise across the hybrid container environment:

1. **Ingress Vulnerability Exploitation (T1190)**: The adversary submitted malicious HTTP requests containing newline injection sequences in ingress annotations to an NGINX Ingress controller, exploiting CVE-2024-7646 to bypass routing validation.
2. **Web Process RCE & Reverse Shell**: The exploit triggered a remote code execution vulnerability in a Java web container. The process spawned `/bin/sh` and initiated an outbound reverse shell. The root cause was a container running with a writeable root filesystem and unconstrained Linux capabilities.
3. **ServiceAccount Token Extraction (T1528, T1550.001)**: The adversary accessed `/var/run/secrets/kubernetes.io/serviceaccount/token`. The root cause was omission of `automountServiceAccountToken: false` on the pod specification, mounting a token with broad discovery permissions.
4. **Admission Control Bypass via Break-Glass Annotation (T1610)**: Using the stolen token, the adversary deployed a privileged container with `hostNetwork: true` and host volume mounts. The deployment included the annotation `admission.stackrox.io/break-glass: ticket-8492`. The root cause was an RHACS admission policy that allowed emergency bypasses without validating ticket expiration against the enterprise ITSM system.
5. **Host Escape & Firewall Manipulation (T1611, T1499, T1612)**: The privileged container started with UID 0 on a worker node. The attacker executed `iptables -F` to flush host egress rules and used `buildah` to compile a backdoor container image directly on the host node.
6. **Telemetry Correlation Blindspot**: Activity Tracker recorded the API requests and SCCWP alerted on host activities, but QRadar lacked a correlation rule linking the token misuse to the privileged container launch, delaying SOC triage.

---

### 2.3 Resilient Target Architecture & Surgical Remediation Implementation

The engineering team deployed a defense-in-depth remediation architecture across four operational layers:

1. **Layer 1: Declarative Admission Control**: The RHACS Admission Webhook was enforced in blocking mode during the `Deploy` lifecycle stage. A validating webhook was deployed to reject `admission.stackrox.io/break-glass` annotations lacking cryptographic verification and active ticket validation within a 4-hour window.
2. **Layer 2: Pod Security Admission & Workload Hardening**: Enforced the OpenShift `restricted` Security Context Constraint (SCC) across all business namespaces. Configured `automountServiceAccountToken: false`, `readOnlyRootFilesystem: true`, non-root execution, and dropped `ALL` Linux capabilities.
3. **Layer 3: Automated Active Runtime Response**: Configured RHACS and SCCWP runtime policies to automatically terminate (`pod kill`) any container executing unauthorized build utilities (`buildah`, `docker`), network discovery tools (`nmap`, `nc`), or firewall commands (`iptables`, `nftables`).
4. **Layer 4: Synchronized Telemetry & Correlated Detection**: ClusterLogForwarder was configured to inject Kubernetes metadata into all exported logs. In QRadar, rule `SEC-CORR-HYBRID-ESC-01` was activated to correlate control plane identity anomalies with runtime eBPF container alerts within 300 seconds.

#### Concrete Hardening Implementations

##### 1. Hardened Workload Manifest
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: digital-banking-api
  namespace: banking-prod
  labels:
    app.kubernetes.io/name: digital-banking-api
spec:
  replicas: 3
  selector:
    matchLabels:
      app: digital-banking-api
  template:
    metadata:
      labels:
        app: digital-banking-api
    spec:
      automountServiceAccountToken: false
      serviceAccountName: banking-api-runtime-sa
      securityContext:
        runAsNonRoot: true
        runAsUser: 1000670000
        runAsGroup: 1000670000
        fsGroup: 1000670000
        seccompProfile:
          type: RuntimeDefault
      containers:
        - name: banking-api
          image: quay.apps.ocp.internal/banking/api:v2.4.1@sha256:7f9a2b8e3d4c5b6a7f8e9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d
          imagePullPolicy: IfNotPresent
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            privileged: false
            capabilities:
              drop:
                - ALL
          resources:
            requests:
              cpu: "500m"
              memory: "512Mi"
            limits:
              cpu: "2000m"
              memory: "2048Mi"
          volumeMounts:
            - name: tmp-volume
              mountPath: /tmp
      volumes:
        - name: tmp-volume
          emptyDir:
            medium: Memory
            sizeLimit: 128Mi
```

##### 2. Declarative RHACS Policy for Active Response
```yaml
apiVersion: config.stackrox.io/v1alpha1
kind: SecurityPolicy
metadata:
  name: block-privileged-firewall-tampering
spec:
  policyName: "ACS: Block Privileged Firewall Tampering (T1611)"
  description: "Detects and terminates privileged containers executing iptables or nftables commands"
  severity: CRITICAL_SEVERITY
  categories:
    - "Privilege Escalation"
    - "Network Security"
  lifecycleStages:
    - RUNTIME
  eventSource: DEPLOYMENT_EVENT
  policySections:
    - sectionName: "Execution Criteria"
      policyGroups:
        - fieldName: "Process Name"
          values:
            - "iptables"
            - "iptables-restore"
            - "nft"
            - "nftables"
        - fieldName: "Privileged Container"
          values:
            - "true"
  enforcementActions:
    - FAIL_KUBE_REQUEST
    - KILL_POD
```

##### 3. ClusterLogForwarder Metadata Pipeline
```yaml
apiVersion: logging.openshift.io/v1
kind: ClusterLogForwarder
metadata:
  name: instance
  namespace: openshift-logging
spec:
  outputs:
    - name: qradar-siem
      type: syslog
      url: tls://qradar-collector.sec.internal:6514
      secret:
        name: qradar-tls-client-cert
      syslog:
        facility: local0
        rfc: RFC5424
        severity: informational
        addFields:
          cluster_id: "ocp-prod-dc01"
          environment: "production"
  pipelines:
    - name: audit-pipeline
      inputRefs:
        - audit
      outputRefs:
        - qradar-siem
      labels:
        telemetry: "kubernetes-audit"
    - name: application-pipeline
      inputRefs:
        - application
      outputRefs:
        - qradar-siem
      labels:
        telemetry: "workload-runtime"
```

---

## Section 3: Exam Question Bank & Distractor Forensics

### Question 1: Incident Triage & Initial Containment (Cognitive Focus: FIRST)

An automated alert with Critical severity fires in Red Hat Advanced Cluster Security (RHACS) indicating `ACS: Iptables or nftables Executed in Privileged Container` (matching MITRE ATT&CK technique T1611) within a production financial clearing namespace. Telemetry confirms that a container running under UID 0 spawned the `iptables` binary and modified host network filtering rules. What action must the incident response engineer execute FIRST?

- A) Deploy an automated RHACS network isolation policy to quarantine the affected pod while preserving container runtime memory for forensic extraction.
- B) Modify the cluster-wide Security Context Constraint (SCC) to remove the privileged role from the namespace service accounts.
- C) Reinstall the cluster OVN-Kubernetes CNI daemonset to regenerate default iptables filtering rules across all worker nodes.
- D) Rotate the cluster root Certificate Authority (CA) credentials and restart the OpenShift OAuth server to terminate active administrator sessions.

#### Distractor Forensics
- **Option A is CORRECT**. In container security incident response, the engineer's immediate operational priority upon confirming an active container escape or host tampering event is rapid workload isolation. Applying a network quarantine policy via RHACS immediately cuts off adversary command-and-control (C2) communication and lateral movement paths while preserving the running container state in memory. This allows responders to perform forensic acquisition (such as live memory dumps and process inspection) before terminating the process.
- **Option B is INCORRECT**. Modifying the cluster Security Context Constraint (SCC) alters future pod creation admissions but does not isolate or contain the currently running malicious container. An attacker who has already spawned a process under UID 0 on the host can continue executing commands regardless of changes to declarative admission definitions.
- **Option C is INCORRECT**. Reinstalling the CNI daemonset is a disruptive infrastructure intervention that causes cluster-wide network interruptions for healthy workloads. Executing this step before containing the compromised pod fails to stop the adversary from executing subsequent commands and risks destroying forensic artifacts.
- **Option D is INCORRECT**. Rotating the cluster root CA is a disaster recovery operation that invalidates certificates across all control plane components, kubelets, and service accounts. It causes widespread cluster downtime and does not address the localized container breakout on the compromised worker node.

---

### Question 2: Managed Control Plane Defense Architecture (Cognitive Focus: BEST/MOST)

A security architect must establish protective controls for an IBM Cloud Kubernetes Service (IKS) deployment against MITRE ATT&CK technique T1059.013 (Command and Scripting: Container Orchestration API). Because IKS operates a fully managed control plane where customers cannot install host-based agents on master nodes, which strategy represents the MOST effective architecture to mitigate this threat while maintaining operational stability?

- A) Configure IBM Cloud Activity Tracker to record all Kubernetes API Server audit trails, and deploy SCCWP with runtime policies that detect and block container management tools (such as `kubectl`, `crictl`, and `oc`) inside workload containers.
- B) Inject an eBPF sidecar container into every application pod to intercept outbound system calls and terminate connections targeting the cluster API Server.
- C) Submit an administrative request to IBM Cloud support to deploy custom kernel modules directly onto the managed master node instances.
- D) Configure worker node security groups to block all outbound TCP traffic on port 443, preventing worker node processes from reaching the Kubernetes API endpoint.

#### Distractor Forensics
- **Option A is CORRECT**. This strategy combines control plane auditability with runtime workload protection. In a managed control plane architecture, master node security is handled by the cloud provider, making direct host agent installation impossible. The customer must configure IBM Cloud Activity Tracker to capture all API invocation logs (providing forensic visibility into authentication, source IP, and requested verbs) while deploying SCCWP on customer-managed worker nodes. SCCWP uses kernel-level eBPF probes to detect and prevent unauthorized execution of cluster management tools (`kubectl`, `oc`, `crictl`) inside runtime application containers.
- **Option B is INCORRECT**. Running an eBPF collector as a sidecar inside every user pod introduces operational overhead, requires elevated Linux capabilities (`CAP_BPF` or `CAP_SYS_ADMIN`) across all application containers, and violates the principle of least privilege. eBPF telemetry should be collected by a single DaemonSet on the host node, not replicated within individual workload pods.
- **Option C is INCORRECT**. Cloud providers operate managed control planes under a strict shared responsibility model. Enterprise cloud providers do not grant customers shell access or permit custom kernel modules on managed master infrastructure.
- **Option D is INCORRECT**. Blocking outbound TCP port 443 breaks core cluster operations. Worker node kubelets, proxy agents, and controller services depend on HTTPS connections over port 443 to communicate with the Kubernetes API Server. Severing this path causes nodes to transition to a `NotReady` state.

---

### Question 3: Post-Enforcement Verification & Eradication (Cognitive Focus: NEXT)

Red Hat Advanced Cluster Security (RHACS) alerts on a deployment manifest that contains the emergency annotation `admission.stackrox.io/break-glass: ticket-9401` (matching MITRE ATT&CK technique T1610), allowing an unapproved container image from an external public registry to bypass admission control. The security team verifies that emergency maintenance ticket `ticket-9401` expired two days prior. After terminating the non-compliant deployment, what action must the security team execute NEXT?

- A) Audit cluster Deployment manifests and GitOps source repositories to locate and remove any lingering break-glass annotations, updating CI/CD admission gating rules to reject expired ticket values.
- B) Reinstall Red Hat Quay and purge all local image repositories to eliminate registry cache poisoning.
- C) Rotate the cluster master CA certificate to invalidate all active Kubernetes service account tokens.
- D) Terminate the RHACS Central and Sensor pods to force a complete re-synchronization of the admission control webhook.

#### Distractor Forensics
- **Option A is CORRECT**. After terminating the active non-compliant workload, the next required operational step is eradicating the configuration defect that allowed the bypass to occur. In modern cloud-native environments managed via GitOps, merely deleting a running deployment without cleaning source repositories causes automated controllers (e.g., ArgoCD or OpenShift GitOps) to redeploy the insecure manifest. The security team must audit all active cluster objects and Git repositories for dormant break-glass annotations and update CI/CD admission validation pipelines to reject unauthorized or expired ticket identifiers.
- **Option B is INCORRECT**. Reinstalling the private container registry is unnecessary and destructive. The issue stemmed from an admission controller bypass allowing an image from an external public registry to run; the internal Quay registry was not compromised.
- **Option C is INCORRECT**. Rotating the master CA certificate disrupts the entire cluster control plane. An unauthorized workload deployment does not compromise the cluster internal public key infrastructure, making CA rotation a disproportionate and irrelevant action.
- **Option D is INCORRECT**. RHACS Central and Sensor evaluate policies dynamically based on declarative configurations. Restarting these controller pods does not remove the root-cause defect (the presence of break-glass annotations in deployment source manifests).

---

### Question 4: Telemetry & Compliance Architecture (Cognitive Focus: PRIMARY/EXCEPT)

An enterprise architecture team is designing a unified logging and compliance telemetry architecture for IBM Cloud (IKS/ROKS) and Red Hat OpenShift to satisfy financial industry container baselines (including CIS Benchmarks and FS Cloud standards). All of the following telemetry pipelines and operational configurations are mandatory architectural requirements EXCEPT:

- A) Deploying customer-managed `auditd` logging agents directly on IBM Cloud managed control plane master nodes to record operating system syscalls.
- B) Forwarding Kubernetes API Server audit logs from IBM Cloud Activity Tracker and OpenShift Audit Logs to a central SIEM with Kubernetes metadata enrichment.
- C) Enabling eBPF-based runtime syscall telemetry via SCCWP and RHACS Collector DaemonSets across all customer-managed worker nodes.
- D) Forwarding OpenShift Infrastructure, Application, and Audit logs via ClusterLogForwarder to a central log aggregation platform over TLS.

#### Distractor Forensics
- **Option A is the CORRECT EXCEPTION (the invalid requirement)**. In IBM Cloud managed container services (IKS and ROKS), the Kubernetes control plane is fully managed and operated by IBM. Customers have neither physical nor administrative access to master node operating systems, making it impossible to install customer-managed `auditd` agents on control plane instances. Instead, control plane telemetry is provided through managed service endpoints such as IBM Cloud Activity Tracker.
- **Option B is a MANDATORY requirement**. Forwarding API audit logs to a central SIEM while injecting Kubernetes metadata (cluster identifier, namespace, pod name, and service account) is essential for regulatory auditability and threat correlation across cloud and on-premises environments.
- **Option C is a MANDATORY requirement**. Kernel-level visibility into system calls (`execve`, `fork`, `connect`) via eBPF probes deployed as DaemonSets on worker nodes is necessary to detect runtime threats, unauthorized process execution, and container breakout attempts.
- **Option D is a MANDATORY requirement**. OpenShift compliance guidelines require routing Application, Infrastructure, and Audit log streams through ClusterLogForwarder to a central log repository over encrypted TLS channels to guarantee data integrity and long-term retention.
