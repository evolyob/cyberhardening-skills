# Chapter 3: AWS Container Security Monitoring & Configuration Baseline

## 1. Statutory Baseline & Technical Control Matrix

### 1.1 Architecture & Governance Framework
Financial institutions deploying container workloads on Amazon Web Services (AWS) operate under a shared responsibility model governed by banking regulatory directives and cybersecurity guidelines. The container landscape spans three distinct compute models: Amazon Elastic Kubernetes Service (Amazon EKS), Amazon Elastic Container Service (Amazon ECS), and AWS Fargate serverless compute.

Amazon Elastic Kubernetes Service (Amazon EKS) delegates Kubernetes control plane management (including API server, etcd, controller manager, and scheduler) to AWS. AWS manages control plane high availability, multi-AZ resilience, and automated version maintenance. Financial institutions maintain direct responsibility for data plane operations, worker node operating systems, pod network policies, service account permissions, and workload runtime integrity. Although AWS operates the control plane infrastructure, financial supervisory frameworks mandate continuous non-repudiation and monitoring sovereignty. Financial institutions must independently collect, store, and analyze control plane diagnostic streams, worker node telemetry, and network flows without relying on provider management summaries.

Amazon Elastic Container Service (Amazon ECS) provides a managed container orchestration engine integrated with AWS foundational primitives. ECS coordinates workloads across EC2 worker instances or AWS Fargate serverless profiles. In ECS on EC2, financial institutions retain administrative access to host container daemons and operating system kernels. In ECS Anywhere architectures, on-premises physical nodes register with the AWS ECS control plane, extending AWS container monitoring policies to hybrid data centers while requiring localized audit forwarding.

AWS Fargate abstracts the underlying host instance, running containers inside isolated MicroVM environments powered by the Firecracker lightweight hypervisor. Fargate shifts host operating system maintenance, kernel patching, and container daemon isolation to AWS. Security teams cannot deploy traditional DaemonSets or kernel-level monitoring agents on Fargate instances. Runtime visibility requires managed sidecar injection or AWS native telemetry hooks. Monitoring sovereignty requires collecting container task logs, VPC Flow Logs, and CloudTrail data events to preserve an immutable digital audit trail.

```
+--------------------------------------------------------------------------------------------------+
| AWS Container Management & Security Topology                                                     |
| Control Plane (AWS Managed): EKS API Server/etcd/Controllers -> CloudWatch Diagnostic Streams    |
| EC2 Worker Data Plane: Kernel eBPF Agent, containerd/dockerd, Fluent Bit OS Journal Logging       |
| Fargate MicroVM Data Plane: Managed Sidecar Injection, Task Metadata v4, FireLens Logging        |
| CWPP Engine: Amazon GuardDuty (EKS Protection, Runtime Monitoring eBPF, Malware Protection)      |
| CSPM Engine: AWS Security Hub (CIS Amazon EKS Benchmark, AWS FSBP, PCI DSS v4.0, NIST SP 800-53) |
| SIEM Pipeline: CloudWatch / EventBridge -> Kinesis Firehose -> Splunk / Microsoft Sentinel       |
| Storage: Amazon S3 Object Lock (WORM Compliance Mode for Regulatory Archival)                    |
+--------------------------------------------------------------------------------------------------+
```

### 1.2 CWPP & CSPM Security Tooling Topology
Cloud Workload Protection Platform (CWPP) and Cloud Security Posture Management (CSPM) constitute the two foundational pillars of AWS container defense.

Amazon GuardDuty serves as the primary native CWPP engine. GuardDuty analyzes control plane audit streams, network flows, DNS queries, and kernel-level system calls using machine learning and behavioral profiling:
- GuardDuty EKS Protection evaluates Kubernetes audit logs pushed directly from EKS control plane logging pipelines. It detects credential compromise, anonymous API access, unauthorized cluster role assignments, and anomalous workload executions.
- GuardDuty Runtime Monitoring deploys an automated lightweight eBPF security agent across EC2 worker nodes or injects a managed sidecar into AWS Fargate task definitions. The eBPF agent captures kernel-level file modifications, process executions, and network socket connections at the operating system layer, detecting fileless malware, reverse shells, container breakouts, and cryptomining.
- GuardDuty Malware Protection conducts agentless scanning on underlying Amazon EBS volume snapshots attached to EC2 worker nodes when anomalous behavior is detected, identifying rootkits, trojans, and suspicious binaries.
- GuardDuty S3 Protection audits data plane interactions against Amazon S3 buckets storing container registry layers, configuration manifests, and persistent application backups.

AWS Security Hub operates as the central CSPM solution. It evaluates cloud resource configurations against industry security benchmarks and regulatory compliance frameworks:
- CIS Amazon EKS Benchmark evaluates cluster endpoint access, control plane logging configuration, KMS envelope encryption for Kubernetes Secrets, node security groups, and worker node kubelet hardening.
- AWS Foundational Security Best Practices (FSBP) identifies misconfigured IAM policies, public subnets housing cluster components, unencrypted container storage volumes, and non-compliant container definitions.
- PCI DSS v4.0 and NIST SP 800-53 Rev 5 compliance packs evaluate container segmentation, multi-tenant network access restrictions, and administrative access controls.
- Security Hub aggregates findings from GuardDuty, Amazon Inspector, and IAM Access Analyzer into a unified normalized schema (AWS Security Finding Format, ASFF).

### 1.3 Telemetry Taxonomy & Data Component Tagging
Financial container monitoring establishes end-to-end traceability across infrastructure layers. Telemetry data components are mapped to AWS native logging services across three primary execution environments: EKS on EC2, ECS on EC2, and ECS on Fargate.

| Data Component Tag | Canonical Telemetry Category | EKS on EC2 Source & Path | ECS on EC2 Source & Path | ECS on Fargate Source & Path |
| --- | --- | --- | --- | --- |
| `kubernetes:audit` | Kubernetes Audit Log | CloudWatch Logs (`/aws/eks/<cluster>/cluster` audit) | N/A (Non-K8s orchestrator) | N/A (Non-K8s orchestrator) |
| `kubernetes:events` | Kubernetes Cluster Events | CloudWatch Logs (Fluent Bit reading K8s Events API) | N/A (EventBridge task events) | N/A (EventBridge task events) |
| `kubernetes:apiserver` | API Server Diagnostic Logs | CloudWatch Logs (`/aws/eks/<cluster>/cluster` api) | N/A (CloudTrail ECS API logs) | N/A (CloudTrail ECS API logs) |
| `kubernetes:orchestrator` | Controller / Scheduler Logs | CloudWatch Logs (`controllerManager`, `scheduler`) | N/A (AWS managed orchestration) | N/A (AWS managed orchestration) |
| `docker:events / containerd:events` | Runtime Lifecycle Events | Container Insights via Fluent Bit daemonset | EventBridge ECS state changes | EventBridge ECS state changes |
| `docker:daemon / containerd:runtime` | Engine Runtime Logs | CloudWatch Logs (`/var/log/journal` via CW Agent) | CloudWatch Logs (`/var/log/ecs/` & daemon) | N/A (Managed execution engine) |
| `docker:api` | Container Engine API Activity | CloudTrail data events for container API actions | CloudTrail management events | CloudTrail management events |
| `docker:registry` | Container Registry Logs | CloudTrail ECR API logs (`PutImage`, `BatchGetImage`)| CloudTrail ECR API logs | CloudTrail ECR API logs |
| `ebpf:syscalls` | Kernel Syscall Telemetry | GuardDuty Runtime Monitoring eBPF / Falco | GuardDuty Runtime Monitoring / Falco | GuardDuty Fargate sidecar |
| `docker:stats` | Compute Resource Metrics | CloudWatch Container Insights (enhanced metrics) | CloudWatch Container Insights | Container Insights (task metadata v4) |

To guarantee non-repudiation, financial institutions configure CloudWatch Logs subscription filters with AWS KMS customer managed key (CMK) encryption. Log streams are delivered to Amazon S3 buckets configured with Object Lock in Compliance mode.

### 1.4 Native Alert Catalog & MITRE ATT&CK for Containers Mapping
Amazon GuardDuty and AWS native security services provide coverage against the core techniques in the MITRE ATT&CK for Containers matrix.

| TTP ID | MITRE Technique Name | Native GuardDuty Finding Name | Telemetry Source | Severity | Detection Mechanism |
| --- | --- | --- | --- | --- | --- |
| T1046 | Network Service Discovery | `Recon:EC2/Portscan` | VPC Flow Logs | Medium | Outbound port scanning from worker nodes toward remote endpoints. |
| T1046 | Network Service Discovery | `Discovery:Runtime/SuspiciousCommand` | Runtime eBPF | Medium | Execution of discovery tools (`nmap`, `masscan`, `netstat`) in containers. |
| T1068 | Privilege Escalation | `PrivilegeEscalation:Runtime/RuncContainerEscape` | Runtime eBPF | High | Container breakout attempts exploiting runc file descriptor overwriting. |
| T1068 | Privilege Escalation | `PrivilegeEscalation:Runtime/CGroupsReleaseAgentModified` | Runtime eBPF | High | Unauthorized writes to cgroups release_agent files. |
| T1068 | Privilege Escalation | `PrivilegeEscalation:Runtime/DockerSocketAccessed` | Runtime eBPF | High | Processes interacting with `/var/run/docker.sock` to escape containment. |
| T1068 | Privilege Escalation | `PrivilegeEscalation:Runtime/ContainerMountsHostDirectory` | Runtime eBPF | High | Container deployment mounting root host directories (`/`, `/etc`, `/proc`). |
| T1068 | Privilege Escalation | `PrivilegeEscalation:Runtime/ElevationToRoot` | Runtime eBPF | High | Unprivileged container processes executing setuid binaries for root access. |
| T1070 | Indicator Removal | `Stealth:IAMUser/CloudTrailLoggingDisabled` | CloudTrail | High | Management API actions attempting to stop or alter CloudTrail logging. |
| T1070 | Indicator Removal | `DefenseEvasion:Runtime/FilelessExecution` | Runtime eBPF | High | Binary executions originating entirely from memory (`memfd_create`). |
| T1078.001 | Valid Accounts: Default Accounts | `Policy:Kubernetes/AdminAccessToDefaultServiceAccount` | EKS Audit Logs | Medium | Admin cluster role bindings assigned to default service accounts. |
| T1078.001 | Valid Accounts: Default Accounts | `Policy:Kubernetes/AnonymousAccessGranted` | EKS Audit Logs | High | RBAC policies permitting anonymous user requests to cluster resources. |
| T1098.006 | Additional Cloud Roles | `PrivilegeEscalation:Kubernetes/AnomalousBehavior.RoleBindingCreated` | EKS Audit Logs | Medium | Anomalous cluster role binding creation granting elevated privileges. |
| T1110.001 | Password Guessing: Brute Force | `UnauthorizedAccess:EC2/SSHBruteForce` | VPC Flow Logs | Low | High-volume repeated SSH authentication failures targeting worker nodes. |
| T1133 | External Remote Services | `Policy:Kubernetes/ExposedDashboard` | EKS Audit Logs | High | Kubernetes Dashboard exposed via internet-facing LoadBalancers. |
| T1136.001 | Create Account: Local Account | `Persistence:Runtime/SensitiveFileModified` | Runtime eBPF | High | Modifications to `/etc/passwd` or `/etc/shadow` inside active containers. |
| T1204.003 | Malicious Image Execution | `Execution:Runtime/NewBinaryExecuted` | Runtime eBPF | Variable | Execution of unbaselined binary files absent from initial image manifests. |
| T1496.001 | Compute Hijacking: Cryptomining | `CryptoCurrency:Runtime/BitcoinTool.B` | Runtime eBPF | High | Cryptocurrency mining software process signatures operating in containers. |
| T1496.001 | Compute Hijacking: Cryptomining | `CryptoCurrency:Runtime/BitcoinTool.B!DNS` | DNS Query Logs | High | DNS queries resolving cryptocurrency mining pool domains from containers. |
| T1498 | Network Denial of Service | `Backdoor:EC2/DenialOfService.Udp` | VPC Flow Logs | High | Abnormal high-packet UDP outbound traffic from worker nodes. |
| T1528 | Steal Application Access Token | `CredentialAccess:Kubernetes/AnomalousBehavior.SecretsAccessed` | EKS Audit Logs | High | Bulk Secret access requests executed by untrusted service accounts. |
| T1543.005 | Container Process Manipulation | `Execution:Kubernetes/AnomalousBehavior.WorkloadDeployed` | EKS Audit Logs | Medium | Unexpected DaemonSet or deployment creation using unapproved registries. |
| T1609 | Container Admin Command | `Execution:Kubernetes/ExecInKubeSystemPod` | EKS Audit Logs | High | Interactive exec operations directed against pods in `kube-system`. |
| T1610 | Deploy Container | `PrivilegeEscalation:Kubernetes/AnomalousBehavior.WorkloadDeployed!PrivilegedContainer` | EKS Audit Logs | High | Admission and deployment of containers with `securityContext.privileged: true`. |
| T1611 | Escape to Host | `PrivilegeEscalation:Runtime/UserfaultfdUsage` | Runtime eBPF | High | Abuse of `userfaultfd` system calls commonly used in kernel race conditions. |
| T1613 | Container & Resource Discovery | `Discovery:Runtime/SuspiciousCommand` | Runtime eBPF | Medium | Container execution of cluster enumeration commands targeting internal APIs. |

### 1.5 Custom Sigma Detection Rules for CWPP Gaps
Certain adversary techniques circumvent automated machine learning baselines or require specialized business context. Financial institutions deploy five canonical Sigma detection rules into SIEM environments consuming raw EKS Audit Logs and AWS CloudTrail streams.

#### Rule 1: Creation of Pod in System Namespace (T1036.005)
Detects unauthorized pod deployments in the sensitive `kube-system` namespace executed by human identities or unapproved service accounts. Attackers deploy backdoors directly into system namespaces to blend in with legitimate orchestration components.

```yaml
title: Creation Of Pod In System Namespace
id: 25b9c01c-350d-4b95-bed1-836d04a4f325
status: production
description: Detects unauthorized pod creation in the kube-system namespace by non-system accounts.
tags:
  - attack.defense_evasion
  - attack.t1036.005
logsource:
  category: eks_audit
detection:
  selection:
    objectRef.namespace: 'kube-system'
    objectRef.resource: 'pods'
    verb: 'create'
  filter:
    user.username:
      - 'system:kube-scheduler'
      - 'system:kube-controller-manager'
      - 'system:serviceaccount:kube-system:daemon-set-controller'
      - 'system:serviceaccount:kube-system:replicaset-controller'
      - 'system:serviceaccount:kube-system:job-controller'
      - 'eks:node-manager'
  condition: selection and not filter
level: high
```

#### Rule 2: Masqueraded System Component Service Account in Non-System Namespace (T1036.010)
Adversaries create ServiceAccounts mimicking system components (e.g. `coredns`, `kube-proxy`, `aws-node`) inside application namespaces to evade detection and establish persistence.

```yaml
title: Kubernetes Masqueraded System Component ServiceAccount in Non-System Namespace
id: a1b2c3d4-1036-4a7b-8c9d-0e1f2a3b4c5d
status: production
description: Detects creation of service accounts mimicking core system components in customer namespaces.
tags:
  - attack.defense_evasion
  - attack.t1036.010
logsource:
  category: eks_audit
detection:
  selection:
    objectRef.resource: 'serviceaccounts'
    verb: 'create'
    requestObject.metadata.name:
      - 'coredns'
      - 'kube-proxy'
      - 'aws-node'
      - 'vpc-cni'
      - 'kube-scheduler'
  filter_namespace:
    objectRef.namespace:
      - 'kube-system'
      - 'kube-public'
      - 'kube-node-lease'
  condition: selection and not filter_namespace
level: high
```

#### Rule 3: Unauthorized Kubernetes CronJob or Scheduled Task Modification (T1053.007)
Adversaries manipulate Kubernetes CronJobs to maintain persistence or schedule unauthorized commands. This rule audits Batch API modifications while filtering standard automated controller actions.

```yaml
title: Kubernetes Suspicious CronJob or Job Creation
id: c8e2b104-5047-4921-9e23-7fa3d189012a
status: production
description: Detects creation or modification of CronJobs and Jobs by non-system identities.
tags:
  - attack.execution
  - attack.persistence
  - attack.t1053.007
logsource:
  category: eks_audit
detection:
  selection:
    objectRef.apiGroup: 'batch'
    objectRef.resource:
      - 'cronjobs'
      - 'jobs'
    verb:
      - 'create'
      - 'update'
      - 'patch'
  filter_controller:
    user.username:
      - 'system:serviceaccount:kube-system:cronjob-controller'
      - 'system:serviceaccount:kube-system:job-controller'
      - 'system:kube-controller-manager'
  condition: selection and not filter_controller
level: medium
```

#### Rule 4: Kubernetes Namespace Deletion by IAM Identity (T1485)
Adversaries seeking operational disruption or evidence destruction attempt to delete entire namespaces, destroying contained pods, services, secrets, and local storage.

```yaml
title: Kubernetes Namespace Deletion by IAM Identity
id: e7a2c5d9-3f81-4b6a-9c24-1d8e6f0a3b57
status: production
description: Detects deletion of a Kubernetes namespace initiated by AWS IAM users or assumed roles.
tags:
  - attack.impact
  - attack.t1485
logsource:
  category: eks_audit
detection:
  selection:
    objectRef.resource: 'namespaces'
    verb: 'delete'
    user.username|startswith: 'arn:aws:'
  condition: selection
level: critical
```

#### Rule 5: AWS Recovery Inhibition via Snapshot, Cluster, or Backup Deletion (T1490)
Before executing ransomware payload encryption or data destruction, attackers attempt to inhibit recovery by deleting EBS snapshots, tearing down EKS clusters, or destroying AWS Backup recovery points.

```yaml
title: AWS Container Recovery Inhibition - Snapshot, Cluster, or Backup Deletion
id: d5f8a3c7-2e94-4b16-8d3a-6f1c9e0b7a52
status: production
description: Detects manual deletion of EBS snapshots, EKS clusters, or AWS Backup vaults.
tags:
  - attack.impact
  - attack.t1490
logsource:
  category: cloudtrail
detection:
  selection:
    eventName:
      - 'DeleteSnapshot'
      - 'DeleteCluster'
      - 'DeleteBackupVault'
      - 'DeleteRecoveryPoint'
  filter_aws_services:
    userIdentity.invokedBy:
      - 'backup.amazonaws.com'
      - 'dlm.amazonaws.com'
  condition: selection and not filter_aws_services
level: critical
```

### 1.6 Architectural Exclusions & Alternative Compensating Controls
Certain techniques in the MITRE ATT&CK for Containers taxonomy cannot be directly monitored via GuardDuty runtime findings due to cloud architecture boundaries. These techniques are managed through architectural exclusions and compensating controls:

1. T1059.013 (Execution: Cloud Controller API & CLI Commands): Amazon EKS control planes are fully managed by AWS behind hardened AWS API endpoints. Kubernetes API access requires authentication through AWS IAM Authenticator or EKS OIDC identity integration. Adversaries cannot execute arbitrary commands against host control plane operating systems. Compensating control: Financial institutions enforce IAM least privilege via condition keys (`aws:SourceIp`, `aws:PrincipalArn`), require multi-factor authentication (MFA) for administrative roles, and monitor CloudTrail for unusual `AssumeRole` and `eks:AccessKubernetesApi` operations.

2. T1110.003 (Credential Access: Password Spraying & Brute Force): Node-level authentication on AWS Fargate is structurally absent because Fargate eliminates host-level login shells. For EC2 worker nodes, direct password-based interactive logins are prohibited by architectural design. Compensating control: Financial institutions disable password authentication, eliminate public IPv4 addressing on worker nodes, mandate AWS Systems Manager Session Manager for host access, and deploy AWS WAF Account Takeover Prevention (ATP) on public web ingress endpoints.

3. T1190 (Initial Access: Exploit Public-Facing Application): GuardDuty CWPP operates at the workload runtime layer and does not perform inline web application firewall inspection. Compensating control: Deploy AWS WAF on Application Load Balancers and Amazon CloudFront with `AWSManagedRulesCommonRuleSet`, `AWSManagedRulesSQLiRuleSet`, and `AWSManagedRulesKnownBadInputsRuleSet`. Continuously scan container images in Amazon ECR using Amazon Inspector for Common Vulnerabilities and Exposures (CVEs).

4. T1499 (Impact: Endpoint Denial of Service): Network volumetric flood mitigation is handled at the network edge rather than inside container runtimes. Compensating control: Deploy AWS Shield Advanced across Route 53, CloudFront, and internet-facing Application Load Balancers. Configure AWS WAF rate-limiting rules to restrict single-IP request velocities.

5. T1525 (Persistence: Implant Internal Image): GuardDuty does not intercept container image build steps prior to registry push. Compensating control: Enforce Amazon ECR Tag Immutability to prevent overwriting existing release tags. Implement AWS Signer container image digital signatures and configure Kubernetes admission controllers (e.g. Kyverno or Gatekeeper) to reject unsigned container images.

### 1.7 SIEM Export & Observability Pipeline
To satisfy financial supervisory mandates for independent digital non-repudiation, container telemetry is exported in near real time to central enterprise SIEM solutions (e.g. Splunk, Microsoft Sentinel).

The enterprise export pipeline architecture incorporates three core components:
1. High-Throughput Audit Streaming: CloudWatch Logs subscription filters extract EKS control plane audit logs and container application logs, streaming events through Amazon Kinesis Data Firehose directly into SIEM HTTP Event Collector (HEC) endpoints.
2. Event-Driven Security Hub & GuardDuty Routing: Amazon EventBridge captures GuardDuty findings and Security Hub compliance events within seconds of generation. EventBridge rules route structured JSON events to Kinesis Firehose and automated remediation Lambda functions.
3. Immutable Regulatory Log Archive: All telemetry streams replicate to an Amazon S3 storage bucket configured with S3 Object Lock in Compliance mode. Data cannot be deleted or overwritten by any identity (including the AWS root account) throughout the statutory retention lifecycle.

### 1.8 Quantitative Control Metrics (KPI/KRI/KCI)
Financial institutions monitor the health, resilience, and compliance of container security controls using quantitative telemetry thresholds.

| Metric Identifier | Metric Name | Category | Target Threshold | Measuring Tool & Source | Evaluation Frequency |
| --- | --- | --- | --- | --- | --- |
| KCI-AWS-01 | EKS Control Plane Log Latency | Key Control Indicator | <= 180 seconds | CloudWatch Logs Metric Filter | Continuous (Real-time) |
| KPI-AWS-02 | GuardDuty Runtime Detection SLA | Key Performance Indicator | <= 30 seconds | GuardDuty Finding Timestamp Delta | Continuous (Real-time) |
| KRI-AWS-03 | Unencrypted Kubernetes Secrets Ratio | Key Risk Indicator | 0.00% | Security Hub CIS EKS Benchmark Control | Hourly Automated Audit |
| KRI-AWS-04 | Privileged Container Deployment Count | Key Risk Indicator | 0 active workloads | Admission Controller Metrics | Continuous (Block & Alert) |
| KPI-AWS-05 | Critical ECR CVE Remediation MTTR | Key Performance Indicator | <= 48 hours | Amazon Inspector Dashboard | Daily Automated Assessment |
| KCI-AWS-06 | SIEM Telemetry Delivery Reliability | Key Control Indicator | >= 99.999% success | Kinesis Firehose Delivery Metrics | Continuous 5-minute rollups |
| KCI-AWS-07 | Immutable Log Retention Verification | Key Control Indicator | 100% compliance | S3 Object Lock Compliance Policy | Weekly Cryptographic Audit |

---

## 2. Production Incident & Remediation Architecture

### 2.1 Incident Context & Production Failure Scenario
A tier-one financial institution operates a production Amazon EKS cluster hosting retail payment authorization microservices under PCI DSS Level 1 requirements. The environment comprises 24 EC2 worker nodes running managed node groups across three Availability Zones.

During an active business day, the security operations center (SOC) receives high-severity alerts from Amazon GuardDuty indicating suspicious activity. An adversary achieved initial access through an exposed continuous deployment (CI/CD) worker IAM key. The key possessed broad ECR push permissions but lacked IP condition boundaries. The attacker pushed a malicious container image containing an embedded reverse shell and privilege escalation toolkit into an existing unpinned container repository (`payment-processor:latest`).

### 2.2 Attack Progression & Exploitation Chain
The attack progressed through seven tactical phases across 18 minutes:

1. Initial Access & Supply Chain Tampering: The attacker authenticated to Amazon ECR using compromised long-lived IAM credentials, overwriting the `payment-processor:latest` image tag. The cluster deployment pulled the poisoned image during a scheduled rolling update.
2. Execution via Web Application: Once deployed, the pod executed the poisoned container entrypoint, initiating an outbound encrypted reverse shell connection to an external command-and-control server (C2).
3. Privilege Escalation & Container Breakout (T1611): The pod specification contained `securityContext.privileged: true` and a host directory mount (`hostPath: /var/run/docker.sock`). The adversary used the exposed Docker socket to create an auxiliary container with host root privileges, breaking out into the worker node kernel.
4. Credential Access via IMDSv1 (T1552.001): Operating on the host node, the adversary queried the EC2 Instance Metadata Service (`http://169.254.169.254/latest/meta-data/iam/security-credentials/`). Because the node launch template permitted IMDSv1 without token enforcement, the attacker extracted temporary security credentials belonging to the worker node IAM instance profile.
5. Lateral Movement & Discovery (T1613): The extracted node role possessed overly broad permissions due to policy sprawl. The attacker listed EKS cluster secrets, enumerated VPC subnets, and identified production backup repositories.
6. Recovery Inhibition Attempt (T1490): To maximize extortion impact, the adversary executed AWS CLI commands attempting to delete EBS volume snapshots and teardown the target EKS cluster:
   ```bash
   aws ec2 delete-snapshot --snapshot-id snap-09a8b7c6d5e4f3a21
   aws eks delete-cluster --name payment-prod-cluster
   ```
7. Resource Hijacking & Defense Evasion (T1036.005, T1496.001): The attacker deployed a stealthy DaemonSet named `kube-proxy-system` into the `kube-system` namespace, initiating a Monero cryptominer communicating over Stratum mining protocols.

### 2.3 Root-Cause Defect Analysis
A comprehensive post-incident forensic investigation revealed five core security configuration defects:
1. Inadequate Registry Controls: Amazon ECR repository lacked tag immutability settings, allowing the adversary to overwrite existing image tags. Furthermore, the cluster lacked image signature verification at the admission control gate.
2. Permissive Workload Security Context: The Kubernetes namespace lacked Pod Security Standard enforcement. Deployments were permitted to run as root, request Linux capabilities (`CAP_SYS_ADMIN`), and mount host sockets.
3. Unhardened Instance Metadata Service: EC2 worker nodes were configured with IMDSv1 enabled (`HttpTokens=optional`) and a metadata response hop limit of 2, allowing pods to query host instance credentials directly across the bridge network.
4. Overprivileged Worker Node IAM Profile: The worker node instance profile contained attached policies granting administrative EC2 and EKS modification permissions rather than strictly scoped worker node join permissions. Workloads failed to use IAM Roles for Service Accounts (IRSA).
5. Lack of Immutable Backup Protection: AWS Backup vaults lacked AWS Backup Vault Lock compliance policies, leaving disaster recovery snapshots vulnerable to deletion by privileged IAM identities.

### 2.4 End-to-End Remediation Architecture & Automated Containment
To eliminate identified vulnerabilities and prevent recurrence, the financial institution deployed a five-layer defense architecture.

#### Remediation Step 1: ECR Tag Immutability and Admission Signing
Enable tag immutability across all ECR repositories via AWS CLI:
```bash
aws ecr put-image-tag-mutability     --repository-name payment-processor     --image-tag-mutability IMMUTABLE
```
Integrate AWS Signer with container pipelines. Deploy Kyverno admission policies to enforce cryptographic signature validation, rejecting unsigned images:
```yaml
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: verify-image-signature
spec:
  validationFailureAction: Enforce
  rules:
    - name: verify-aws-signer
      match:
        any:
          - resources:
              kinds:
                - Pod
      verifyImages:
        - imageReferences:
            - "*.dkr.ecr.*.amazonaws.com/*"
          attestors:
            - entries:
                - certificates:
                    cert: |-
                      -----BEGIN CERTIFICATE-----
                      <CORPORATE_AWS_SIGNER_ROOT_CA>
                      -----END CERTIFICATE-----
```

#### Remediation Step 2: Admission Control and Pod Security Standard Enforcement
Enforce the Kubernetes Pod Security Standard `restricted` profile on all application namespaces:
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: payment-production
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/enforce-version: latest
    pod-security.kubernetes.io/warn: restricted
    pod-security.kubernetes.io/audit: restricted
```

#### Remediation Step 3: EC2 Launch Template IMDSv2 Enforcement
Update the node group launch template to require session tokens and restrict hop counts to 1, preventing container network bridges from traversing to the metadata endpoint:
```bash
aws ec2 modify-launch-template     --launch-template-id lt-0123456789abcdef0     --default-version     --launch-template-data '{
        "MetadataOptions": {
            "HttpTokens": "required",
            "HttpPutResponseHopLimit": 1,
            "HttpEndpoint": "enabled"
        }
    }'
```

#### Remediation Step 4: IRSA Migration & Immutable Backup Lock
Decommission node-level IAM credentials for application access. Establish IAM Roles for Service Accounts (IRSA) using the EKS cluster OIDC provider:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::112233445566:oidc-provider/oidc.eks.us-east-1.amazonaws.com/id/EXAMPLE"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "oidc.eks.us-east-1.amazonaws.com/id/EXAMPLE:sub": "system:serviceaccount:payment-production:payment-sa"
        }
      }
    }
  ]
}
```
Deploy AWS Backup Vault Lock in Compliance mode to guarantee WORM protection against recovery inhibition:
```bash
aws backup put-backup-vault-lock-configuration     --backup-vault-name ProductionPaymentVault     --min-retention-days 90     --max-retention-days 2555     --changeable-for-days 3
```

#### Remediation Step 5: Automated Incident Response Containment Pipeline
Deploy an automated incident response DAG connecting GuardDuty findings to AWS Lambda via EventBridge. When GuardDuty emits `PrivilegeEscalation:Runtime/ContainerMountsHostDirectory` or `CryptoCurrency:Runtime/BitcoinTool.B`, EventBridge triggers the isolation function:
1. Step 1: Lambda extracts the compromised EC2 Instance ID and Kubernetes Pod Name from the finding payload.
2. Step 2: Lambda invokes the Kubernetes API to cordon and drain the compromised worker node, preventing new pod scheduling.
3. Step 3: Lambda attaches an isolation Security Group to the EC2 instance, revoking all ingress and egress network flows except designated forensic management IP blocks.
4. Step 4: Lambda triggers an automated EBS snapshot creation with forensic retention tags for digital evidence preservation.
5. Step 5: Lambda emits a high-priority incident message to the enterprise SOC SIEM.

---

## 3. Exam Question Bank & Distractor Forensics

### Question 1 (FIRST)
A security engineer at a financial institution observes an Amazon GuardDuty high-severity alert: `PrivilegeEscalation:Runtime/ContainerMountsHostDirectory` originating from a payment microservice pod on an Amazon EKS managed node group. Preliminary investigation reveals the container is actively mounting `/etc` from the host worker node. What is the FIRST operational action the security engineer should execute?

A. Modify the Kubernetes deployment manifest to remove the hostPath volume mount and initiate a rolling deployment update.  
B. Isolate the affected EC2 worker node at the network layer and cordon the node in Kubernetes to prevent further workload scheduling.  
C. Delete the running pod immediately using the `kubectl delete pod` command with `--force --grace-period=0`.  
D. Rotate the AWS IAM credentials associated with the worker node instance profile across the entire cluster.

#### Distractor Forensics
- **Option A is incorrect**: Modifying the deployment manifest initiates a standard rolling update, which leaves the existing compromised container running while the new replica initializes. This allows the attacker to maintain interactive access, destroy forensic evidence, or deepen persistence on the host node. Updating manifests represents a long-term configuration correction rather than the first triage action.
- **Option B is correct**: Network isolation and node cordoning represent the immediate containment standard. Isolating the worker node network security group halts active C2 communications and lateral movement without terminating volatile memory. Cordoning the node via `kubectl cordon` ensures the scheduler does not assign fresh workloads to the compromised host. This preserves digital evidence in RAM and filesystem swap for forensic analysis.
- **Option C is incorrect**: Force-deleting the pod terminates running container processes instantly, purging volatile memory, running process trees, uncommitted network sockets, and temporary files stored in the container overlay filesystem. This destroys critical digital evidence required for regulatory breach reporting and forensic root-cause analysis.
- **Option D is incorrect**: Rotating worker node IAM credentials across the cluster disrupts all running node groups, creating a broad denial of service across uncompromised business workloads. Furthermore, if the attacker already escaped to the host kernel, local persistence mechanisms (e.g. rootkits, cron jobs) remain active regardless of AWS credential revocation.

---

### Question 2 (BEST/MOST)
A financial institution hosts microservices on Amazon EKS worker nodes running on EC2 instances. The security architecture requires preventing container workloads from harvesting node instance profile credentials via the Instance Metadata Service (IMDS). Which architectural implementation provides the MOST resilient and comprehensive protection against IMDS credential theft?

A. Apply an iptables rule on each EC2 worker node to block outbound traffic to IP address `169.254.169.254` on port 80.  
B. Enforce IMDSv2 with `HttpPutResponseHopLimit=1` and `HttpTokens=required` across node launch templates, and transition application workloads to IAM Roles for Service Accounts (IRSA).  
C. Assign the worker node instance profile an empty IAM policy and rely entirely on environment variables inside container definitions for credential injection.  
D. Deploy a Kubernetes NetworkPolicy in every namespace blocking egress traffic to the link-local IP range `169.254.0.0/16`.

#### Distractor Forensics
- **Option A is incorrect**: Relying solely on host iptables rules is fragile. The AWS VPC CNI plugin or node daemonsets frequently update iptables chains, risking accidental rule overwrites. Furthermore, iptables configurations do not enforce cryptographically validated session tokens or address container network namespaces operating under host networking modes.
- **Option B is correct**: Enforcing IMDSv2 (`HttpTokens=required`) mandates a signed PUT request token before metadata retrieval. Setting `HttpPutResponseHopLimit=1` ensures that IP packets decrement their TTL when crossing the bridge network boundary from the container namespace to the host network, dropping the packet before it reaches the metadata endpoint. Combining this with IRSA establishes least-privilege credential delivery via temporary OIDC web identity tokens injected directly into the pod, removing any requirement for workloads to access the node instance profile.
- **Option C is incorrect**: Placing plaintext AWS secret keys or access credentials into container environment variables violates basic security baselines. Environment variables are visible in container inspection commands (`docker inspect`, `crictl inspect`), pod manifests, and process environment files (`/proc/$PID/environ`). Stripping the node instance profile entirely also breaks core worker node registration with the EKS control plane.
- **Option D is incorrect**: Standard Kubernetes NetworkPolicies do not govern pods running with `hostNetwork: true`. Additionally, standard CNI implementations enforce NetworkPolicies at layer 3 and 4 within the cluster overlay network; if an attacker escapes the container or operates in host network mode, NetworkPolicies provide zero enforcement.

---

### Question 3 (NEXT)
During an automated compliance audit conducted by AWS Security Hub, an EKS production cluster fails the CIS Amazon EKS Benchmark control: `Ensure Kubernetes Secrets are encrypted at rest using AWS KMS`. The EKS cluster currently stores secrets in etcd with default base64 encoding. The security architect updates the cluster configuration to enable AWS Key Management Service (AWS KMS) envelope encryption using a customer managed key (CMK). What is the NEXT operational step required to achieve compliance?

A. Restart all EC2 worker nodes using an automated rolling instance refresh in the Auto Scaling group.  
B. Retrieve and re-write all existing Kubernetes Secrets across all namespaces to trigger KMS envelope encryption in etcd.  
C. Delete the AWS KMS key policy to permit the default Kubernetes service account access to the encryption key.  
D. Execute a full backup of the etcd database using `etcdctl snapshot save` and delete the unencrypted snapshot file.

#### Distractor Forensics
- **Option A is incorrect**: Restarting EC2 worker nodes refreshes the data plane compute instances but does not alter data stored in the Kubernetes etcd database. The EKS control plane manages etcd independently of worker nodes. Existing Secrets remain stored in their prior unencrypted state within etcd until an explicit write event occurs.
- **Option B is correct**: Enabling KMS envelope encryption on an active EKS cluster applies KMS encryption strictly to newly created or modified Secrets. Pre-existing Secrets in etcd remain unencrypted until they are updated. The security engineer must run a re-encryption command across all namespaces (e.g. `kubectl get secrets --all-namespaces -o json | kubectl replace -f -`) to read and write every Secret back through the API server, triggering KMS encryption.
- **Option C is incorrect**: Deleting the KMS key policy makes the customer managed key unmanageable and inaccessible, causing all subsequent secret encryption and decryption operations to fail. The cluster API server requires an IAM role with explicit `kms:Encrypt` and `kms:Decrypt` permissions defined in the key policy.
- **Option D is incorrect**: Taking an etcd snapshot does not encrypt active secrets in the database. Furthermore, in managed Amazon EKS, direct etcd access via `etcdctl` is unavailable to customers because AWS operates and manages the control plane instances and etcd storage behind private management boundaries.

---

### Question 4 (PRIMARY/EXCEPT)
Financial container baselines establish specific architectural exclusions and compensating controls for MITRE ATT&CK techniques that cannot be directly detected via native GuardDuty CWPP findings. All of the following techniques represent valid architectural exclusions paired with appropriate AWS native compensating controls EXCEPT:

A. Technique T1059.013 is architecturally excluded because EKS control planes are managed behind AWS IAM Authenticator, compensated by IAM least privilege and CloudTrail monitoring.  
B. Technique T1525 is architecturally excluded from runtime GuardDuty interception, compensated by Amazon ECR Tag Immutability and AWS Signer digital signatures.  
C. Technique T1611 is architecturally excluded because container escapes cannot occur on AWS managed infrastructure, compensated by AWS Shield Advanced.  
D. Technique T1190 is architecturally excluded from native runtime CWPP detection, compensated by AWS WAF managed rule sets and Amazon Inspector registry scanning.

#### Distractor Forensics
- **Option A is an exclusion pair**: Technique T1059.013 (Cloud Controller API & CLI Commands) is structurally mitigated because the control plane is hosted by AWS and protected by mandatory IAM authentication, meaning adversaries cannot execute arbitrary commands against the control plane operating system. CloudTrail provides the compensating audit trail.
- **Option B is an exclusion pair**: Technique T1525 (Implant Internal Image) occurs during image construction and registry storage before workload execution, outside GuardDuty runtime hooks. ECR Tag Immutability and AWS Signer signature validation in admission control provide effective compensating controls.
- **Option C is EXCEPT (the correct answer)**: Container escape (T1611) is NOT an architecturally excluded technique; on the contrary, container breakout is a primary threat on container platforms and is actively monitored by Amazon GuardDuty Runtime Monitoring via kernel eBPF probes (e.g. `PrivilegeEscalation:Runtime/RuncContainerEscape`). Furthermore, asserting that container escapes cannot occur on AWS infrastructure is false. Finally, AWS Shield Advanced provides DDoS protection at layers 3, 4, and 7 and has zero capability to prevent or mitigate container-to-host breakouts.
- **Option D is an exclusion pair**: Technique T1190 (Exploit Public-Facing Application) targets web application logic vulnerabilities before execution, which GuardDuty runtime does not intercept inline. AWS WAF and Amazon Inspector provide the necessary compensating perimeter and vulnerability shielding controls.
