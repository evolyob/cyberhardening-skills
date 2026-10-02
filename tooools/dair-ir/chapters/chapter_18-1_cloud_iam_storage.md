# Chapter 18-1: Cloud Systems Playbook: IAM Credential Leakage, S3/Blob Exfiltration & Billing Alerts

> Modular Sub-Chapter | Source: DAIR-IR Framework

---

# Chapter 18: Specialized IR for Cloud Systems (AWS/Azure/GCP)

CLOUD INTRODUCTION

Cloud environments introduce unique challenges for incident response that differ significantly from traditional on-premises investigations.  This chapter addresses cloud-specific considerations within the broader DAIR model established in Part 2: A Dynamic Approach to Incident Response . Organizations responding to cloud incidents should reference the relevant sections in Part 2 for comprehensive guidance on each response activity, using this chapter to supplement that foundation with cloud-specific considerations. We start by examining common cloud attack patterns and their impacts, then cover preparation topics including logging and permissions. From there, we look at cloud-native detection tooling before diving into response actions such as scoping compromises, isolating resources, and eradicating persistence. Finally, we discuss cloud-specific debrief questions, how to leverage the cloud itself for incident response, and considerations for multi-cloud environments.

Common Cloud Attacks

As more organizations move workloads to the cloud, threat actors have adapted their techniques accordingly. The tactics used in on-premises environments did not translate directly to cloud environments, requiring new approaches to initial access, lateral movement, and persistence. This section covers the most common attack patterns observed in cloud environments, starting with initial access vectors and then examining their impacts.

Initial Access Vectors

The first question to understand about cloud attacks is how threat actors gain unauthorized access. According to the Google Threat Horizons report in both H1 and H2 of 2025, weak or absent credentials, misconfigurations, and API/UI compromises accounted for the initial access vectors in over 80% of observed threat actor activity. [1]

Figure 185 | Distribution of Cloud Initial Access Vectors

Weak or Absent Credentials

These have consistently been the most targeted initial access vector in cloud environments.  When combined with a lack of Multi-Factor Authentication (MFA) and poor permissions management, a single effective social engineering attempt can give a threat actor broad access to the environment and enable them to carry out their objectives.

Misconfigurations

Many organizations transitioned to the cloud without an equivalent depth of expertise in cloud security. The skills gap created by this transition, combined with insufficient change control and human error, has led to numerous incidents resulting from the exploitation of cloud misconfigurations. Whether the misconfiguration exposes data that should be restricted or grants excessive privileges that enable lateral movement, threat actors are actively scanning for and exploiting these weaknesses.

API/UI Compromise

Organizations deploying cloud workloads across worldwide regions benefit from improved end-user accessibility. However, if proper access controls are not in place, these applications can be exposed to the internet, creating a broad attack surface. Combined with weak credentials or vulnerable software, threat actors can gain an initial foothold through these exposed interfaces. Once a foothold is established, reconnaissance of the hosts running those workloads may lead to lateral movement to other hosts or, in the worst case, into the management plane.

Impacts

Once threat actors gain access to a cloud environment, several important trends emerge in attacker objectives. Mandiant’s M-Trends 2025 Report provides insight into threat actor motivations:

> ... data theft was observed in nearly two-thirds of cloud compromises (66%).  > Over a third of cases (38%)

served financially motivated goals, including data theft extortion without ransomware encryption (16%), business email compromise (BEC) (13%), ransomware (9%), as well as cryptocurrency theft and employment fraud. [3]

> - Mandiant, M-Trends 2025 Report

Cloud environments host vast amounts of valuable data across storage services, databases, and compute workloads. Orca Security’s 2025 State of Cloud Security Report found that:

• 33% of organizations with publicly exposed storage buckets contained sensitive data.

• 38% of organizations with publicly exposed databases had sensitive data in them.

• 28% of organizations with publicly accessible cloud functions had plaintext secrets in the code packages and environment variables. [4] In cases like these, attackers need zero or minimal permissions to access sensitive data.

WHAT MOTIVATES CLOUD ATTACKERS?

Threat actors targeting cloud environments are driven by the same motivations as those attacking on-premises infrastructure, but the cloud offers new opportunities and a broader attack surface to achieve those goals. Data theft and extortion These remain the most common objectives for cloud-focused threat actors. Cloud environments store large volumes of sensitive data across storage services, databases, and SaaS platforms, often accessible via a single compromised identity. Attackers who gain access to a privileged account can potentially reach data across an entire organization without ever touching an endpoint. The cloud is an attractive target for extortion campaigns, in which stolen data is used to pressure victims into paying, sometimes without deploying ransomware at all.

Ransomware

Cloud-based ransomware looks different than on-premises. Rather than encrypting local drives, attackers may delete snapshots and backups, modify storage lifecycle policies to destroy data, or lock out administrators by manipulating IAM. The impact can be just as severe, especially when organizations lack offline backups of their cloud-hosted data.

Cryptomining

This is a common outcome when attackers gain access to accounts with the ability to provision compute resources. Spinning up GPU-enabled virtual machines across multiple regions can generate high costs for the victim while generating cryptocurrency for the attacker. Some organizations only discover a compromise when an unexpectedly large cloud bill arrives. What makes cloud attacks particularly dangerous is the potential for escalation from a compromised workload to the management plane. A virtual machine running in the cloud has access to a metadata service that can provide credentials to service accounts or roles. If those credentials carry broad permissions, an attacker who compromises a single host can pivot to controlling the entire cloud environment.

PREPARE

Preparation for cloud incidents requires attention to capabilities that are absent in traditional on-premises environments. The shared responsibility model means that organizations are responsible for configuring much of the visibility and access needed for effective response. While we’ve examined broader incident response preparation in Prepare Activity, this section focuses on two cloud-specific preparation areas that have the greatest impact on response effectiveness: logging and permissions.

Logging

Cloud logging places significant responsibility on the customer to ensure expected logs are enabled and collected. Within the cloud, there are two categories of logs: management (or control) plane logs and data plane logs.  As a general rule, management plane logs are enabled by default, while data plane logs are disabled by default. Ensuring logging is correctly configured is one of the most important preparation steps for cloud incident response. Few preparation failures are as costly as starting an investigation and discovering that the logs needed to understand what happened are not available. Discovering that logs are missing during an active incident is one of the costliest preparation failures in cloud environments. Unlike on-premises systems, in which logs may exist on disk even if uncollected, cloud logs that were never enabled simply do not exist, and there is no way to reconstruct them after the fact. When evaluating which logs to enable, there is a tradeoff between cost and value. In an ideal world, organizations would enable all possible log sources, but most cannot ignore the associated costs. Important data plane logs to consider include network flow logs, storage access logs, and operating system logs. Due to the volume these logs generate, identify the critical systems and resources in the environment and ensure that additional logging is enabled where it would prove most valuable during an investigation. For example, enabling access logging on a storage bucket that serves publicly accessible website assets may not be worthwhile, but a sensitive bucket containing confidential records warrants the cost of maintaining an audit trail. Prioritize enabling data-plane logging on systems that store sensitive data or are most likely to be targeted. The cost of logging is far less than the cost of investigating an incident without adequate visibility. Two additional logging considerations are lag time and retention time. Lag time matters when a threat actor is active in the environment during the investigation. If a log source has a twenty-four-hour delay in receiving entries, responders cannot confidently rule out certain threat actor activity until the lag period has passed and the full picture of events is available. Retention time impacts the ability to investigate incidents discovered after a long dwell period.  Azure Entra ID audit and sign-in logs, for example, are retained for only thirty days with a premium license and seven days on the free tier. The command example in Listing 141 demonstrates how to check the retention period for Entra ID logs. If logs were not configured for extended storage, evidence will be missing when investigating incidents that occurred as few as seven days prior to discovery.

Listing 141 | Querying Entra ID Log Retention with Azure CLI

$ az rest --method get --url

"hxxps://management[.]azure[.]com/providers/Microsoft.aadiam/diagnosticSettings?api-version=2017-04-01" 1

{

"value": [

{

"id": "/providers/Microsoft.aadiam/diagnosticSettings/EntraID-to-LogAnalytics",

"name": "EntraID-to-LogAnalytics",

"properties": { "logs": [

{

"category": "SignInLogs",

"enabled": true,

"retentionPolicy": { "days": 0, "enabled": false } 2

},

{

"category": "AuditLogs",

"enabled": true,

"retentionPolicy": { "days": 0, "enabled": false }

}

],

"workspaceId": "/subscriptions/a1b2c3d4-.../resourceGroups/rgsecurity/providers/Microsoft.OperationalInsights /workspaces/secops-workspace" 3

}

}

]

}

$ az monitor log-analytics workspace show --resource-group rg-security  --workspace-name secops-

workspace  --query "retentionInDays" 4 1 Query Entra ID diagnostic settings using the Azure REST API. 2 The retentionPolicy.days value of 0 indicates that logs are not being retained beyond the default retention period. 3 The workspaceId field identifies the Log Analytics workspace name and resource group. 4 Query the workspace to determine the actual retention period. The best case for an organization is to configure a Security Information and Event Management (SIEM) platform or other centralized logging platform (such as a Log Analytics workspace or storage account) to consume cloud platform logs and store them with an extended retention period to account for longdwelling threats. Centralizing logs also simplifies investigation by eliminating the need to pivot between applications to search through different log sources.

Permissions

Another important preparation consideration for cloud environments is permissions. During an active incident, responders should not have to spend valuable time requesting the access needed to investigate. Coordinating with other teams to assign permissions delays the investigation and can allow a threat actor to continue operating while access is being provisioned. Instead, response teams should have the privileges needed to investigate and respond to incidents established in advance. At the organization level, all incident responders should have global read-only access. This provides the ability to read logs, view users, roles, and policies to scope incidents, and investigate suspicious resources. Each provider offers built-in roles suited for this purpose: AWS provides the SecurityAudit managed policy, Azure offers the Security Reader role, and Google Cloud includes the Security Reviewer role. These roles provide sufficient visibility for investigation but do not allow modification of resources. If performing forensics in the cloud, there should be a dedicated project, account, or subscription where forensics VMs and other tooling can be deployed, with investigators having the appropriate permissions to manage resources in that account. Separating forensic infrastructure from production environments prevents contamination of evidence and reduces the risk of an attacker interfering with the investigation. Pre-provisioned forensic accounts with elevated access to the forensics project (but read-only access elsewhere) allow responders to begin analysis immediately without waiting for access approvals. Response procedures may also require global write actions, such as modifying network resources to isolate compromised hosts, revoking credentials, or snapshotting volumes. Granting standing write access across the environment conflicts with least-privilege principles, but requiring access requests during an active incident wastes time. Table 55  summarizes several approaches for managing this need while balancing security principles.

Table 55 | Approaches for IR Write Access

APPROACH DESCRIPTION

Automated service accounts A service account with scoped write permissions executes containment and isolation actions on behalf of responders through pre-built automations, avoiding the need to grant individuals broad access. Just-in-time elevation Responders activate pre-approved elevated roles on demand with automatic expiration. Azure Privileged Identity Management (PIM), AWS IAM Identity Center with temporary permission sets, and Google Cloud IAM Conditions with time-based access all support this pattern. Break-glass accounts Sealed credentials stored securely (e.g., in a hardware safe or secrets vault with audit logging) provide emergency access when other mechanisms are unavailable. Use of break glass accounts should trigger an alert and require post-incident review. Each approach has trade-offs in operational complexity, audit coverage, and access speed. Organizations should select and test an approach before an incident forces the question, as provisioning access during active response introduces delays that benefit the threat actor.

DETECT

Detection in cloud environments relies on different tools and data sources than traditional on-premises monitoring. General detection guidance is covered in Detect Activity. This section introduces cloud-native detection services offered by major cloud providers, providing responders with a starting point for understanding the built-in capabilities available.

Cloud-Native Detection Tooling

Cloud providers have developed built-in detection services that monitor environments for threats without requiring third-party tools. These services analyze control-plane logs, network traffic, and resource behavior to identify suspicious activity, including compromised credentials and cryptomining. “Attackers are moving away from exploiting traditional infrastructure vulnerabilities and instead are targeting the cloud fabric itself, leveraging misconfigurations, identity weaknesses, and overpermissioned access as primary entry points.

- Orca Security, 2025 State of Cloud Security Report In the best case, an organization will have a SIEM configured with detection capabilities to monitor logs from cloud data sources. If not, cloud providers offer native detection services that can monitor the environment. While selecting commercial products is outside the scope of this book, we’ll introduce options from the major cloud providers to illustrate what cloud-native tooling is capable of.

Detection Tooling for AWS

Amazon GuardDuty is a managed threat detection service that continuously monitors AWS accounts and workloads for malicious activity and unauthorized behavior. It uses machine learning, anomaly detection, and integrated threat intelligence to identify potential threats such as cryptomining, compromised credentials, or communication with known command-and-control servers.

Figure 186 | AWS GuardDuty Finding Details: Threat Detection Validation

Within the GuardDuty interface, analysts can review a list of findings across resources in the environment. Examining an individual finding provides an in-depth view of the identities, resources, and indicators associated with it, giving responders a starting point for deeper investigation. GuardDuty also offers agentless malware scanning for EC2 instances and container workloads through its Malware Protection feature.  When GuardDuty generates a finding indicating potential malware, it can automatically trigger a scan by creating snapshots of the EBS volumes attached to the affected instance. Because scanning operates on snapshots rather than live volumes, there is no performance impact on running workloads. Responders can also manually initiate on-demand scans by specifying an EC2 instance ARN, which is useful for investigating hosts that have not yet triggered an automated finding. When malware is detected, EBS snapshots are retained to preserve forensic evidence for deeper analysis. This combination of automated detection and evidence preservation makes GuardDuty a valuable first step in AWS cloud incident response workflows.

Detection Tooling for Azure

Azure detection capabilities can be added to a cloud environment by enabling Microsoft Defender for Cloud. Defender for Cloud monitors both the resources in the environment and Microsoft 365 and Azure audit logs for suspicious activity.

Figure 187 | Azure Defender for Cloud Alert Details: SQL Injection Attack

Figure 187 shows an example of an alert for a SQL injection attack against an Azure SQL database. As with GuardDuty, the alert provides context about the resources involved and indicators to support the start of an investigation. From an incident response perspective, Defender for Cloud’s alert interface includes a "Take action" tab that provides several response options directly from the alert. Responders can inspect the resource’s activity logs for additional context, review manual remediation steps specific to the alert type, or trigger an automated response through an Azure Logic App. Alerts are also mapped to MITRE ATT&CK kill chain stages where applicable, helping analysts understand the attacker’s progression through the environment. For organizations using Microsoft Sentinel or another SIEM, Defender for Cloud alerts can be streamed directly to those platforms for centralized investigation alongside other log sources.

Detection Tooling for Google Cloud

Google Cloud offers native threat detection via Security Command Center (SCC). SCC includes several detection services that cover different parts of the environment:

• Event Threat Detection monitors Cloud Audit Logs and VPC Flow Logs for suspicious patterns such as brute-force login attempts, cryptomining activity, and outbound connections to known malicious infrastructure.

• VM Threat Detection  operates at the hypervisor level to identify malware and kernel-level rootkits on Compute Engine instances without requiring an agent.

• Container Threat Detection  monitors GKE container workloads for runtime attacks, including reverse shells, suspicious binaries, and unexpected script execution. Each of these services generates findings that responders can review, annotate, and prioritize by severity. Findings include the affected resource, the detection source, and recommended remediation steps. The SCC interface follows a similar pattern to GuardDuty and Defender for Cloud, presenting a consolidated view of findings across the environment with drill-down capability into individual alerts. For investigation, findings can be exported to BigQuery for deeper analysis or published to Pub/Sub for integration with external SIEM platforms and ticketing systems.  Organizations using Google Security Operations (formerly Chronicle) can stream SCC findings directly into their SIEM for correlation with other log sources. SCC also supports automated playbooks for remediation, allowing organizations to define response actions that execute when specific finding types are generated.

What Cloud-Native Detection Misses

While cloud-native detection services provide valuable coverage, they have limitations that responders should understand. These tools focus primarily on control plane events and known attack patterns, which means they may miss activity that falls outside their detection models. First, cloud-native detections typically focus on known patterns. Novel techniques or living-off-the-land approaches that use legitimate cloud APIs in unusual ways may not trigger alerts. An attacker who uses only the permissions already assigned to a compromised identity is difficult to distinguish from normal operations. Second, most cloud-native detection services monitor the control plane, leaving data plane activity largely unmonitored unless additional features are enabled. An attacker downloading sensitive files from a storage bucket will not generate a detection unless data plane logging and associated detection rules are configured. Third, these services lack organizational context. They do not know that a specific service account runs only during business hours, or that a particular user has never accessed a given resource. Without organizationspecific baselines, anomalous behavior that would be obvious to an analyst may not trigger an alert. Organizations should treat cloud-native detection services as a foundation, not a complete solution. Supplementing them with a SIEM that can apply custom detection rules, cross-correlate events across sources, and incorporate organizational baselines significantly improves detection coverage.

WHEN THE CLOUD BILL IS THE FIRST ALERT

One detection pattern I have encountered repeatedly is the unexpected billing alert as the first indicator of compromise. An organization’s finance team notices a cloud bill that is three or four times higher than normal, and the investigation reveals hundreds of GPU-enabled instances running cryptomining software across regions the organization has never used. Google’s Threat Horizons reports have consistently identified cryptomining as one of the most common post-compromise activities in cloud environments, accounting for a significant portion of observed attacker actions. [5] The reason is straightforward: compromised cloud accounts provide immediate access to compute resources that can be monetized without any lateral movement or data exfiltration. This pattern has an important implication for the detection strategy: billing alerts and budget thresholds are legitimate detection mechanisms for cloud environments. Organizations should configure alerts for unexpected spending spikes, particularly in regions where they do not normally operate. A billing anomaly may not be the most sophisticated detection, but it may be the first to fire.

RESPONSE ACTIONS

Responding to cloud incidents involves the same core activities as any incident, but the techniques and tools differ significantly. Identity-based access models, distributed resources, and cloud-specific persistence mechanisms all require adapted response procedures. This section covers cloud-specific considerations for scoping compromises, understanding log sources, isolating compromised resources, eradicating persistence, and leveraging automation for response.

Scoping Cloud Incidents

Scoping Questions

One of the most important steps in responding to cloud incidents is scoping the compromise. Cloud environments often require more considerations and access controls than traditional on-premises environments. Start by identifying what identity or identities are compromised. These could be users, access keys, or service accounts; in the case of AWS, even a role can be compromised. Once compromised identities are identified, scope the permissions assigned to those identities to understand what the threat actor could access. This is often not as simple as looking at the individual identity and seeing a list of permissions. In Azure, for example, permissions are granted through role assignments, which bind an identity, role, and resource to define which actions can be taken. The examples in Figure 188 , Figure 189 , and Figure 190  show how permissions are granted at the subscription level and resource group level, and how that impacts the scope of a compromise. We can collect similar information using the Azure CLI, as shown in Listing 142, to list all role assignments for a user across the entire subscription. Google Cloud uses a similar concept called bindings, where an IAM policy binds a member (user, service account, or group) to a role on a specific resource. Bindings are applied at different levels of the resource hierarchy (organization, folder, project, or individual resource), and permissions are inherited downward. Responders can use the gcloud projects get-iam-policy  command to list all bindings for a project and identify the effective permissions of a compromised identity. In both Azure and Google Cloud, permissions inherited from higher levels of the resource hierarchy can expand the scope of a compromise beyond what is visible at the individual resource level.

Figure 188 | Azure Subscription and Resource Group Identification

Figure 189 | Azure Subscription Identifies Owner, Contributor Access

Figure 190 | Azure Resource Group Identifies Additional Contributor Access

Listing 142 | Azure CLI Role Assignment List for User

$ az role assignment list --all --assignee hydra@pymtechlabs.com --output json 1

[

{

"principalId": "ddaca639-d9c8-4d65-9f30-c0dcc58f9574",

"principalName": "Hydra@pymtechlabs.com",

"principalType": "User",

"roleDefinitionName": "Contributor", 2

"scope": "/subscriptions/a1b2c3d4-.../resourceGroups/rg-prod-eastus"

},

{

"principalId": "ddaca639-d9c8-4d65-9f30-c0dcc58f9574",

"principalName": "Hydra@pymtechlabs.com",

"principalType": "User",

"roleDefinitionName": "Owner", 3

"scope": "/subscriptions/a1b2c3d4-..."

}

]

1 The --all flag returns role assignments across all scopes rather than only the current subscription default. 2 Contributor access at the resource group level, consistent with the portal view in Figure 190. 3 The owner at the subscription level indicates the compromised identity has broad access across all resources in the subscription.
