# Chapter 18: Specialized IR for Cloud Systems (AWS/Azure/GCP)

> Source: PDF Pages 580-608 (Total Pages: 29)

BLACKBAUD: FOUR YEARS OF REGULATORY CONSEQUENCES

The 2020 Blackbaud ransomware incident illustrates how regulatory consequences can cascade for

years after technical recovery concludes.

Blackbaud provides fundraising and administrative software to nonprofits, hospitals, and educational

institutions. On February 7, 2020, an attacker gained access to Blackbaud’s network and began

accessing and extracting customer data, remaining undetected for over three months. [16]

By the time

the company discovered the intrusion in May 2020, the attacker had exfiltrated data belonging to

approximately 13,000 customer organizations, compromising the personal information of millions of

consumers, including Social Security numbers, bank account information, healthcare records, and

donation histories.

Blackbaud paid approximately $250,000 in Bitcoin ransom in exchange for the attacker’s promise to

delete the stolen data, but the company was never able to verify that the attacker followed through.

The company then waited two months to notify affected customers, and the initial notifications

understated the severity of the breach. Even though Blackbaud knew by late July 2020 that sensitive

financial and healthcare information had been stolen, customers were not informed of the full scope

until months later.

The regulatory response arrived in waves over the years that followed:

• March 2023: The US Securities and Exchange Commission (SEC) imposed a $3 million penalty for

misleading breach disclosures in the company’s quarterly filings.

• October 2023 : Attorneys general from 49 states plus the District of Columbia reached a $49.5

million settlement.

• May 2024: The US Federal Trade Commission (FTC) finalized a settlement requiring 20 years of

security oversight and mandatory data deletion practices.

• June 2024: The California Attorney General imposed an additional $6.75 million fine.

The FTC alleged that Blackbaud failed to implement multiple industry-standard security measures,

misrepresented its security and retention practices, and retained consumer data longer than

necessary, contributing to the exposure of sensitive information. The agency also charged Blackbaud

with misrepresenting both its security practices and the scope of the breach to affected customers.

For organizations responding to ransomware, the Blackbaud case demonstrates that regulatory

scrutiny focuses not only on the security failures that enabled the attack, but also on how the

organization communicated with affected parties during and after the incident. Decisions made

under pressure during the response phase, including notification timing, disclosure completeness,

and ransom payment, become the subject of regulatory review years later. The total regulatory

penalties exceeded $59 million, arriving three to four years after the company had completed

technical recovery.

Insurance Resolution

Cyber insurance claims require extensive documentation and often involve negotiation over coverage

scope. Carriers may dispute costs, question response decisions, or require additional evidence before

approving claims. The claims process typically extends months beyond incident closure, requiring

continued access to incident documentation and personnel who can speak to response decisions.

Stakeholder Confidence

Customers, partners, and board members who witnessed operational disruption will often want more than

assurances that systems are restored. Demonstrating improved security posture through concrete

investments, third-party assessments, or enhanced monitoring capabilities helps rebuild confidence over

time. Organizations that communicate transparently about improvements often recover stakeholder trust

more effectively than those that minimize the incident.

The Blackbaud case illustrates the cost of understating breach severity. Initial notifications

that downplay impact may seem protective in the moment, but when the full scope

emerges later, stakeholders feel misled. Transparent communication, even when the news

is difficult, builds more durable trust than optimistic messaging that later requires

correction.

Ongoing Extortion Risk

In double extortion scenarios, attackers retain copies of stolen data regardless of whether the organization

pays. Ransom payment purchases a promise, not a guarantee. Threat actors may leak data despite receiving

payment due to internal group conflicts, operational errors, or simple dishonesty. Data may also resurface

months or years later when attackers sell access to other criminal groups, when group infrastructure is

seized and data becomes public, or when former affiliates splinter into new operations.

Organizations that pay ransom should not assume the transaction closes the matter. Threats to release data

may resurface if attackers believe additional pressure might yield further payment, or if the data finds its

way to other criminal actors through underground marketplaces. Even when attackers honor their

commitments initially, the organization has no way to verify that all copies of stolen data have been

destroyed.

An extortion payment purchases a promise from criminals, not a guarantee. Organizations

have no way to verify that all copies of stolen data have been destroyed, and data may

resurface months or years later.

For these reasons, organizations should prepare communications plans and legal strategies for potential

future data exposure regardless of whether ransom was paid. Stakeholder notification templates, regulatory

response procedures, and customer communication strategies developed during the initial incident should

remain accessible for potential reactivation. Legal counsel familiar with the incident should be available to

advise if stolen data surfaces publicly months or years later.

KADOKAWA: PAYMENT DID NOT PREVENT DISCLOSURE

The 2024 ransomware attack on Japanese media conglomerate Kadokawa Corporation demonstrates

that ransom payments do not guarantee against data exposure. [17]

On June 8, 2024, the BlackSuit ransomware group attacked Kadokawa’s network, disrupting

operations across its subsidiaries, including the popular video platform Niconico. The attackers

claimed to have exfiltrated 1.5 terabytes of sensitive data, including employee records, contracts, and

financial information. BlackSuit initially demanded $8.25 million as an extortion fee for not disclosing

the stolen data, but Kadokawa’s compliance policies limited any potential payment to $3 million.

Incident Response for Ransomware | Chapter 17 | 557

Facing a deadline and the threat of public exposure of its data, Kadokawa transferred approximately

$2.98 million in Bitcoin to the attackers. Despite receiving payment, BlackSuit leaked the stolen data

anyway. The company’s subsequent investigation confirmed that 254,241 individuals had their

personal information exposed, including 186,269 records from Kadokawa’s educational institute

subsidiary and comprehensive employee data from Dwango Corporation (a wholly owned subsidiary

of Kadokawa).

The financial impact extended beyond the ransom payment. Kadokawa’s stock price fell by over 20%

in the weeks following the attack. The company announced expected extraordinary losses of ¥2.3

billion (approximately $15 million) for the fiscal year, encompassing incident response costs, business

disruption, and remediation efforts. Full services did not resume until August 5, 2024, nearly two

months after the initial attack.

Reports indicate BlackSuit experienced internal fragmentation during this period, with former

members dispersing to new operations. [18]

These dynamics may explain why the group leaked data

despite receiving payment. Ransomware operations often experience affiliate disputes, leadership

changes, and splintering into new groups. Even when an organization negotiates in good faith with

one faction, other members may not honor the agreement.

The Kadokawa case illustrates a difficult truth: organizations considering ransom payment should

understand they are purchasing a promise from criminals who have already demonstrated willingness

to cause harm, and that promise may not be kept.

Prevention Remains Essential

This chapter has focused on response to ransomware incidents, but prevention remains the most effective

defense. Organizations that implement strong access controls, maintain current patching, deploy effective

endpoint protection, and train employees to recognize social engineering are less likely to face a

ransomware incident in the first place. The response capabilities described in this chapter are valuable, but

they represent a fallback when prevention fails rather than a substitute for preventive controls.

[1] Chainalysis, "The 2026 Crypto Crime Report," March 2026, www.chainalysis.com/wp-content/uploads/2026/03/the-2026-

crypto-crime-report-release.pdf

[2] Elsad, Amer, Gumarin, JR, and Barr, Abigail, "LockBit 2.0: How This RaaS Operates and How to Protect Against It," Palo Alto

Networks Unit 42, June 2022, unit42.paloaltonetworks.com/lockbit-2-ransomware/

[3] Veeam, "Replica from Backup," Veeam Backup & Replication User Guide, helpcenter.veeam.com/docs/vbr/userguide/

replica_from_backup.html?ver=13

[4] Veeam, "3-2-1-1-0 Backup Rule," www.veeam.com/blog/321-backup-rule.html

[5] Trend Micro Research, "What To Expect In A Ransomware Negotiation," October 2021, www.trendmicro.com/en_us/research/21/

j/what-to-expect-in-a-ransomware-negotiation-.html

[6] Cimpanu, Catalin, "Conti gang threatens to dump victim data if ransom negotiations leak to reporters," The Record, October 2021,

therecord.media/conti-gang-threatens-to-dump-victim-data-if-ransom-negotiations-leak-to-reporters

[7] Verizon, "2025 Data Breach Investigations Report," www.verizon.com/business/resources/reports/dbir/

[8] Verizon, "2024 Data Breach Investigations Report," www.verizon.com/business/resources/reports/dbir/

[9] Check Point Research, "Ransomware Evolved: Double Extortion," 2020, research.checkpoint.com/2020/ransomware-evolved-

double-extortion/

[10] PricewaterhouseCoopers, "Conti Cyber Attack on the HSE - Independent Post Incident Review," December 2021, www.hse.ie/eng/

services/publications/conti-cyber-attack-on-the-hse-full-report.pdf

[11] Petcu, Alina Georgiana, "The DCH Ransomware Attack: A Teachable Moment in Cyber-History," Heimdal Security, January 2021,

heimdalsecurity.com/blog/dch-ransomware-attack/

[12] Anthropic, "Detecting and countering misuse of AI: August 2025," August 2025, www.anthropic.com/news/detecting-countering-

misuse-aug-2025

[13] Anthropic, "Disrupting the first reported AI-orchestrated cyber espionage campaign," November 2025, www.anthropic.com/news/

disrupting-AI-espionage

[14] Anthropic, "Detecting and countering misuse of AI: August 2025," August 2025, www.anthropic.com/news/detecting-countering-

misuse-aug-2025

[15] Anthropic, "Detecting and countering misuse of AI: August 2025," August 2025, www.anthropic.com/news/detecting-countering-

misuse-aug-2025

[16] Federal Trade Commission, "FTC Order Will Require Blackbaud to Delete Unnecessary Data, Boost Safeguards to Settle Charges its

Lax Security Practices Led to Data Breach," February 2024, www.ftc.gov/news-events/news/press-releases/2024/02/ftc-order-will-

require-blackbaud-delete-unnecessary-data-boost-safeguards-settle-charges-its-lax

[17] Antoniuk, Daryna, "Japanese game and anime publisher reportedly pays $3 million ransom to Russia-linked hackers," The Record,

August 2024, therecord.media/kadokawa-japan-reported-ransomware-payment

[18] Lyngaas, Sean, "Details emerge on BlackSuit ransomware takedown," CyberScoop, August 2025, cyberscoop.com/blacksuit-

ransomware-takedown/; citing Cisco Talos research indicating former BlackSuit members dispersed to new operations including the

Chaos ransomware group.

Incident Response for Ransomware | Chapter 17 | 559

18 Incident Response for

Cloud Systems

CLOUD INTRODUCTION

Cloud environments introduce unique challenges for incident response that differ significantly from

traditional on-premises investigations.  This chapter addresses cloud-specific considerations within the

broader DAIR model established in Part 2: A Dynamic Approach to Incident Response . Organizations

responding to cloud incidents should reference the relevant sections in Part 2 for comprehensive guidance

on each response activity, using this chapter to supplement that foundation with cloud-specific

considerations.

We start by examining common cloud attack patterns and their impacts, then cover preparation topics

including logging and permissions. From there, we look at cloud-native detection tooling before diving into

response actions such as scoping compromises, isolating resources, and eradicating persistence. Finally, we

discuss cloud-specific debrief questions, how to leverage the cloud itself for incident response, and

considerations for multi-cloud environments.

Common Cloud Attacks

As more organizations move workloads to the cloud, threat actors have adapted their techniques

accordingly. The tactics used in on-premises environments did not translate directly to cloud

environments, requiring new approaches to initial access, lateral movement, and persistence.

This section covers the most common attack patterns observed in cloud environments, starting with initial

access vectors and then examining their impacts.

Initial Access Vectors

The first question to understand about cloud attacks is how threat actors gain unauthorized access.

According to the Google Threat Horizons report in both H1 and H2 of 2025, weak or absent credentials,

misconfigurations, and API/UI compromises accounted for the initial access vectors in over 80% of

observed threat actor activity. [1]

[2]

Figure 185 | Distribution of Cloud Initial Access Vectors

Weak or Absent Credentials

These have consistently been the most targeted initial access vector in cloud environments.  When

combined with a lack of Multi-Factor Authentication (MFA) and poor permissions management, a single

effective social engineering attempt can give a threat actor broad access to the environment and enable

them to carry out their objectives.

Misconfigurations

Many organizations transitioned to the cloud without an equivalent depth of expertise in cloud security.

The skills gap created by this transition, combined with insufficient change control and human error, has

led to numerous incidents resulting from the exploitation of cloud misconfigurations. Whether the

misconfiguration exposes data that should be restricted or grants excessive privileges that enable lateral

movement, threat actors are actively scanning for and exploiting these weaknesses.

API/UI Compromise

Organizations deploying cloud workloads across worldwide regions benefit from improved end-user

accessibility. However, if proper access controls are not in place, these applications can be exposed to the

internet, creating a broad attack surface. Combined with weak credentials or vulnerable software, threat

actors can gain an initial foothold through these exposed interfaces. Once a foothold is established,

reconnaissance of the hosts running those workloads may lead to lateral movement to other hosts or, in the

worst case, into the management plane.

Impacts

Once threat actors gain access to a cloud environment, several important trends emerge in attacker

objectives. Mandiant’s M-Trends 2025 Report provides insight into threat actor motivations:

> ... data theft was observed in nearly two-thirds of cloud compromises (66%).  > Over a third of cases (38%)

served financially motivated goals, including data theft extortion without ransomware encryption (16%),

business email compromise (BEC) (13%), ransomware (9%), as well as cryptocurrency theft and employment

Incident Response for Cloud Systems | Chapter 18 | 561

fraud. [3]

> — Mandiant, M-Trends 2025 Report

Cloud environments host vast amounts of valuable data across storage services, databases, and compute

workloads. Orca Security’s 2025 State of Cloud Security Report found that:

• 33% of organizations with publicly exposed storage buckets contained sensitive data.

• 38% of organizations with publicly exposed databases had sensitive data in them.

• 28% of organizations with publicly accessible cloud functions had plaintext secrets in the code packages

and environment variables. [4]

In cases like these, attackers need zero or minimal permissions to access sensitive data.

WHAT MOTIVATES CLOUD ATTACKERS?

Threat actors targeting cloud environments are driven by the same motivations as those attacking

on-premises infrastructure, but the cloud offers new opportunities and a broader attack surface to

achieve those goals.

Data theft and extortion

These remain the most common objectives for cloud-focused threat actors. Cloud environments

store large volumes of sensitive data across storage services, databases, and SaaS platforms, often

accessible via a single compromised identity. Attackers who gain access to a privileged account can

potentially reach data across an entire organization without ever touching an endpoint. The cloud is

an attractive target for extortion campaigns, in which stolen data is used to pressure victims into

paying, sometimes without deploying ransomware at all.

Ransomware

Cloud-based ransomware looks different than on-premises. Rather than encrypting local drives,

attackers may delete snapshots and backups, modify storage lifecycle policies to destroy data, or lock

out administrators by manipulating IAM. The impact can be just as severe, especially when

organizations lack offline backups of their cloud-hosted data.

Cryptomining

This is a common outcome when attackers gain access to accounts with the ability to provision

compute resources. Spinning up GPU-enabled virtual machines across multiple regions can generate

high costs for the victim while generating cryptocurrency for the attacker. Some organizations only

discover a compromise when an unexpectedly large cloud bill arrives.

What makes cloud attacks particularly dangerous is the potential for escalation from a compromised

workload to the management plane. A virtual machine running in the cloud has access to a metadata

service that can provide credentials to service accounts or roles. If those credentials carry broad

permissions, an attacker who compromises a single host can pivot to controlling the entire cloud

environment.

PREPARE

Preparation for cloud incidents requires attention to capabilities that are absent in traditional on-premises

environments. The shared responsibility model means that organizations are responsible for configuring

much of the visibility and access needed for effective response. While we’ve examined broader incident

response preparation in Prepare Activity, this section focuses on two cloud-specific preparation areas that

have the greatest impact on response effectiveness: logging and permissions.

Logging

Cloud logging places significant responsibility on the customer to ensure expected logs are enabled and

collected. Within the cloud, there are two categories of logs: management (or control) plane logs and data

plane logs.  As a general rule, management plane logs are enabled by default, while data plane logs are

disabled by default. Ensuring logging is correctly configured is one of the most important preparation steps

for cloud incident response. Few preparation failures are as costly as starting an investigation and

discovering that the logs needed to understand what happened are not available.

Discovering that logs are missing during an active incident is one of the costliest

preparation failures in cloud environments. Unlike on-premises systems, in which logs may

exist on disk even if uncollected, cloud logs that were never enabled simply do not exist,

and there is no way to reconstruct them after the fact.

When evaluating which logs to enable, there is a tradeoff between cost and value. In an ideal world,

organizations would enable all possible log sources, but most cannot ignore the associated costs. Important

data plane logs to consider include network flow logs, storage access logs, and operating system logs. Due

to the volume these logs generate, identify the critical systems and resources in the environment and

ensure that additional logging is enabled where it would prove most valuable during an investigation. For

example, enabling access logging on a storage bucket that serves publicly accessible website assets may not

be worthwhile, but a sensitive bucket containing confidential records warrants the cost of maintaining an

audit trail.

Prioritize enabling data-plane logging on systems that store sensitive data or are most

likely to be targeted. The cost of logging is far less than the cost of investigating an

incident without adequate visibility.

Two additional logging considerations are lag time and retention time. Lag time matters when a threat actor

is active in the environment during the investigation. If a log source has a twenty-four-hour delay in

receiving entries, responders cannot confidently rule out certain threat actor activity until the lag period

has passed and the full picture of events is available.

Retention time impacts the ability to investigate incidents discovered after a long dwell period.  Azure Entra

ID audit and sign-in logs, for example, are retained for only thirty days with a premium license and seven

days on the free tier. The command example in Listing 141 demonstrates how to check the retention period

for Entra ID logs. If logs were not configured for extended storage, evidence will be missing when

investigating incidents that occurred as few as seven days prior to discovery.

Listing 141 | Querying Entra ID Log Retention with Azure CLI

$ az rest --method get --url

"https://management.azure.com/providers/Microsoft.aadiam/diagnosticSettings?api-version=2017-04-

Incident Response for Cloud Systems | Chapter 18 | 563

01" 1

{

"value": [

{

"id": "/providers/Microsoft.aadiam/diagnosticSettings/EntraID-to-LogAnalytics",

"name": "EntraID-to-LogAnalytics",

"properties": {

"logs": [

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

"workspaceId": "/subscriptions/a1b2c3d4-.../resourceGroups/rg-

security/providers/Microsoft.OperationalInsights

/workspaces/secops-workspace" 3

}

}

]

}

$ az monitor log-analytics workspace show --resource-group rg-security  --workspace-name secops-

workspace  --query "retentionInDays" 4

1 Query Entra ID diagnostic settings using the Azure REST API.

2 The retentionPolicy.days value of 0 indicates that logs are not being retained beyond the default retention period.

3 The workspaceId field identifies the Log Analytics workspace name and resource group.

4 Query the workspace to determine the actual retention period.

The best case for an organization is to configure a Security Information and Event Management (SIEM)

platform or other centralized logging platform (such as a Log Analytics workspace or storage account) to

consume cloud platform logs and store them with an extended retention period to account for long-

dwelling threats. Centralizing logs also simplifies investigation by eliminating the need to pivot between

applications to search through different log sources.

Permissions

Another important preparation consideration for cloud environments is permissions. During an active

incident, responders should not have to spend valuable time requesting the access needed to investigate.

Coordinating with other teams to assign permissions delays the investigation and can allow a threat actor to

continue operating while access is being provisioned. Instead, response teams should have the privileges

needed to investigate and respond to incidents established in advance.

At the organization level, all incident responders should have global read-only access. This provides the

ability to read logs, view users, roles, and policies to scope incidents, and investigate suspicious resources.

Each provider offers built-in roles suited for this purpose: AWS provides the SecurityAudit managed policy,

Azure offers the Security Reader role, and Google Cloud includes the Security Reviewer role. These roles

provide sufficient visibility for investigation but do not allow modification of resources.

If performing forensics in the cloud, there should be a dedicated project, account, or subscription where

forensics VMs and other tooling can be deployed, with investigators having the appropriate permissions to

manage resources in that account. Separating forensic infrastructure from production environments

prevents contamination of evidence and reduces the risk of an attacker interfering with the investigation.

Pre-provisioned forensic accounts with elevated access to the forensics project (but read-only access

elsewhere) allow responders to begin analysis immediately without waiting for access approvals.

Response procedures may also require global write actions, such as modifying network resources to isolate

compromised hosts, revoking credentials, or snapshotting volumes. Granting standing write access across

the environment conflicts with least-privilege principles, but requiring access requests during an active

incident wastes time. Table 55  summarizes several approaches for managing this need while balancing

security principles.

Table 55 | Approaches for IR Write Access

APPROACH DESCRIPTION

Automated service

accounts

A service account with scoped write permissions executes containment and

isolation actions on behalf of responders through pre-built automations,

avoiding the need to grant individuals broad access.

Just-in-time elevation Responders activate pre-approved elevated roles on demand with automatic

expiration. Azure Privileged Identity Management (PIM), AWS IAM Identity

Center with temporary permission sets, and Google Cloud IAM Conditions

with time-based access all support this pattern.

Break-glass accounts Sealed credentials stored securely (e.g., in a hardware safe or secrets vault

with audit logging) provide emergency access when other mechanisms are

unavailable. Use of break glass accounts should trigger an alert and require

post-incident review.

Each approach has trade-offs in operational complexity, audit coverage, and access speed. Organizations

should select and test an approach before an incident forces the question, as provisioning access during

active response introduces delays that benefit the threat actor.

DETECT

Detection in cloud environments relies on different tools and data sources than traditional on-premises

monitoring. General detection guidance is covered in Detect Activity. This section introduces cloud-native

detection services offered by major cloud providers, providing responders with a starting point for

understanding the built-in capabilities available.

Cloud-Native Detection Tooling

Cloud providers have developed built-in detection services that monitor environments for threats without

Incident Response for Cloud Systems | Chapter 18 | 565

requiring third-party tools. These services analyze control-plane logs, network traffic, and resource

behavior to identify suspicious activity, including compromised credentials and cryptomining.

“Attackers are moving away from exploiting traditional infrastructure vulnerabilities and instead are

targeting the cloud fabric itself, leveraging misconfigurations, identity weaknesses, and over-

permissioned access as primary entry points.

— Orca Security, 2025 State of Cloud Security Report

In the best case, an organization will have a SIEM configured with detection capabilities to monitor logs

from cloud data sources. If not, cloud providers offer native detection services that can monitor the

environment. While selecting commercial products is outside the scope of this book, we’ll introduce options

from the major cloud providers to illustrate what cloud-native tooling is capable of.

Detection Tooling for AWS

Amazon GuardDuty is a managed threat detection service that continuously monitors AWS accounts and

workloads for malicious activity and unauthorized behavior. It uses machine learning, anomaly detection,

and integrated threat intelligence to identify potential threats such as cryptomining, compromised

credentials, or communication with known command-and-control servers.

Figure 186 | AWS GuardDuty Finding Details: Threat Detection Validation

Within the GuardDuty interface, analysts can review a list of findings across resources in the environment.

Examining an individual finding provides an in-depth view of the identities, resources, and indicators

associated with it, giving responders a starting point for deeper investigation.

GuardDuty also offers agentless malware scanning for EC2 instances and container workloads through its

Malware Protection feature.  When GuardDuty generates a finding indicating potential malware, it can

automatically trigger a scan by creating snapshots of the EBS volumes attached to the affected instance.

Because scanning operates on snapshots rather than live volumes, there is no performance impact on

running workloads. Responders can also manually initiate on-demand scans by specifying an EC2 instance

ARN, which is useful for investigating hosts that have not yet triggered an automated finding. When

malware is detected, EBS snapshots are retained to preserve forensic evidence for deeper analysis. This

combination of automated detection and evidence preservation makes GuardDuty a valuable first step in

AWS cloud incident response workflows.

Detection Tooling for Azure

Azure detection capabilities can be added to a cloud environment by enabling Microsoft Defender for Cloud.

Defender for Cloud monitors both the resources in the environment and Microsoft 365 and Azure audit logs

for suspicious activity.

Figure 187 | Azure Defender for Cloud Alert Details: SQL Injection Attack

Figure 187 shows an example of an alert for a SQL injection attack against an Azure SQL database. As with

GuardDuty, the alert provides context about the resources involved and indicators to support the start of an

investigation.

From an incident response perspective, Defender for Cloud’s alert interface includes a "Take action" tab that

provides several response options directly from the alert. Responders can inspect the resource’s activity

logs for additional context, review manual remediation steps specific to the alert type, or trigger an

automated response through an Azure Logic App. Alerts are also mapped to MITRE ATT&CK kill chain stages

where applicable, helping analysts understand the attacker’s progression through the environment. For

organizations using Microsoft Sentinel or another SIEM, Defender for Cloud alerts can be streamed directly

to those platforms for centralized investigation alongside other log sources.

Detection Tooling for Google Cloud

Google Cloud offers native threat detection via Security Command Center (SCC). SCC includes several

detection services that cover different parts of the environment:

• Event Threat Detection monitors Cloud Audit Logs and VPC Flow Logs for suspicious patterns such as

brute-force login attempts, cryptomining activity, and outbound connections to known malicious

infrastructure.

• VM Threat Detection  operates at the hypervisor level to identify malware and kernel-level rootkits on

Incident Response for Cloud Systems | Chapter 18 | 567

Compute Engine instances without requiring an agent.

• Container Threat Detection  monitors GKE container workloads for runtime attacks, including reverse

shells, suspicious binaries, and unexpected script execution.

Each of these services generates findings that responders can review, annotate, and prioritize by severity.

Findings include the affected resource, the detection source, and recommended remediation steps. The

SCC interface follows a similar pattern to GuardDuty and Defender for Cloud, presenting a consolidated

view of findings across the environment with drill-down capability into individual alerts.

For investigation, findings can be exported to BigQuery for deeper analysis or published to Pub/Sub for

integration with external SIEM platforms and ticketing systems.  Organizations using Google Security

Operations (formerly Chronicle) can stream SCC findings directly into their SIEM for correlation with other

log sources. SCC also supports automated playbooks for remediation, allowing organizations to define

response actions that execute when specific finding types are generated.

What Cloud-Native Detection Misses

While cloud-native detection services provide valuable coverage, they have limitations that responders

should understand. These tools focus primarily on control plane events and known attack patterns, which

means they may miss activity that falls outside their detection models.

First, cloud-native detections typically focus on known patterns. Novel techniques or living-off-the-land

approaches that use legitimate cloud APIs in unusual ways may not trigger alerts. An attacker who uses only

the permissions already assigned to a compromised identity is difficult to distinguish from normal

operations.

Second, most cloud-native detection services monitor the control plane, leaving data plane activity largely

unmonitored unless additional features are enabled. An attacker downloading sensitive files from a storage

bucket will not generate a detection unless data plane logging and associated detection rules are

configured.

Third, these services lack organizational context. They do not know that a specific service account runs only

during business hours, or that a particular user has never accessed a given resource. Without organization-

specific baselines, anomalous behavior that would be obvious to an analyst may not trigger an alert.

Organizations should treat cloud-native detection services as a foundation, not a complete solution.

Supplementing them with a SIEM that can apply custom detection rules, cross-correlate events across

sources, and incorporate organizational baselines significantly improves detection coverage.

WHEN THE CLOUD BILL IS THE FIRST ALERT

One detection pattern I have encountered repeatedly is the unexpected billing alert as the first

indicator of compromise. An organization’s finance team notices a cloud bill that is three or four

times higher than normal, and the investigation reveals hundreds of GPU-enabled instances running

cryptomining software across regions the organization has never used.

Google’s Threat Horizons reports have consistently identified cryptomining as one of the most

common post-compromise activities in cloud environments, accounting for a significant portion of

observed attacker actions. [5]

The reason is straightforward: compromised cloud accounts provide

immediate access to compute resources that can be monetized without any lateral movement or data

exfiltration.

This pattern has an important implication for the detection strategy: billing alerts and budget

thresholds are legitimate detection mechanisms for cloud environments. Organizations should

configure alerts for unexpected spending spikes, particularly in regions where they do not normally

operate. A billing anomaly may not be the most sophisticated detection, but it may be the first to fire.

RESPONSE ACTIONS

Responding to cloud incidents involves the same core activities as any incident, but the techniques and

tools differ significantly. Identity-based access models, distributed resources, and cloud-specific

persistence mechanisms all require adapted response procedures. This section covers cloud-specific

considerations for scoping compromises, understanding log sources, isolating compromised resources,

eradicating persistence, and leveraging automation for response.

Scoping Cloud Incidents

Scoping Questions

One of the most important steps in responding to cloud incidents is scoping the compromise. Cloud

environments often require more considerations and access controls than traditional on-premises

environments.

Start by identifying what identity or identities are compromised. These could be users, access keys, or

service accounts; in the case of AWS, even a role can be compromised. Once compromised identities are

identified, scope the permissions assigned to those identities to understand what the threat actor could

access.

This is often not as simple as looking at the individual identity and seeing a list of permissions. In Azure, for

example, permissions are granted through role assignments, which bind an identity, role, and resource to

define which actions can be taken. The examples in Figure 188 , Figure 189 , and Figure 190  show how

permissions are granted at the subscription level and resource group level, and how that impacts the scope

of a compromise. We can collect similar information using the Azure CLI, as shown in Listing 142, to list all

role assignments for a user across the entire subscription.

Google Cloud uses a similar concept called bindings, where an IAM policy binds a member (user, service

account, or group) to a role on a specific resource. Bindings are applied at different levels of the resource

hierarchy (organization, folder, project, or individual resource), and permissions are inherited downward.

Responders can use the gcloud projects get-iam-policy  command to list all bindings for a project and

identify the effective permissions of a compromised identity.

In both Azure and Google Cloud, permissions inherited from higher levels of the resource

hierarchy can expand the scope of a compromise beyond what is visible at the individual

resource level.

Incident Response for Cloud Systems | Chapter 18 | 569

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

1 The --all flag returns role assignments across all scopes rather than only the current subscription default.

2 Contributor access at the resource group level, consistent with the portal view in Figure 190.

3 The owner at the subscription level indicates the compromised identity has broad access across all resources in the

subscription.

Beyond direct role assignments, additional mechanisms may change the true scope of an identity

Incident Response for Cloud Systems | Chapter 18 | 571

compromise. A compromised identity in AWS may appear able to manage users in an account, but a

permission boundary, Service Control Policy (SCP), session policy, or resource-based policy could ultimately

prevent those actions after the full access evaluation flow. Understanding the full policy evaluation chain is

important for accurately scoping what a compromised identity can actually do.

In AWS, the policy evaluation logic follows a specific order: first, explicit denies in any applicable policy take

precedence; then, organization SCPs are evaluated, followed by resource-based policies, identity-based

policies, IAM permission boundaries, and finally session policies. At each layer, an explicit deny overrides

any allow. This means a compromised identity with AdministratorAccess may still be unable to perform

certain actions if an SCP or permission boundary restricts them. AWS documents this evaluation chain in

detail in the IAM User Guide, and responders should reference it when the apparent permissions do not

match observed behavior.

After identifying affected identities, identify affected resources. This helps establish the threat actor’s

actions in the environment and determine whether unauthorized changes were made. For storage accounts,

buckets, and other data stores, the organization will want to know whether any data was exposed. Certain

resources could also facilitate lateral movement.  Virtual machines in the cloud often host an Instance

Metadata Service (IMDO) service that provides access tokens to service accounts or roles, which can then

be used to escalate privileges.

Finally, examine the cloud network architecture to evaluate potential lateral movement. If the compromised

cloud environment has direct access to additional cloud organizations within the same provider, the on-

premises environment, or another cloud provider, there may be additional logs to collect and analyze to

determine whether those connected environments were also compromised.

CIRCLECI: WHEN A STOLEN SESSION TOKEN COMPROMISES THE SUPPLY

CHAIN

In January 2023, CircleCI, a continuous integration development platform, disclosed that an attacker

had compromised an engineer’s laptop with malware and stolen a valid SSO session token. [6]

Because

the token was already authenticated past MFA, the attacker bypassed multi-factor controls entirely

and used the session to access CircleCI’s internal systems.

From that single session token, the attacker accessed the production environment and exfiltrated

customer secrets, including environment variables, API tokens, and encryption keys stored in

CircleCI’s platform. The scope was significant: CircleCI advised all customers to rotate every secret

stored in their environment, affecting thousands of organizations that relied on the platform for

CI/CD pipelines. An attacker with the stolen credentials could access any of the platforms and

services that customers integrated with CircleCI, including cloud platforms, code repositories, and

SaaS applications.

What makes this incident instructive for cloud responders is the attack chain: a stolen session token

provided access without triggering credential-based detections, and the blast radius extended to

every downstream customer whose secrets were stored in the platform. The investigation required

analyzing session logs, internal access patterns, and data-plane activity rather than traditional host-

based forensics.

This case illustrates two important lessons in cloud IR. First, MFA alone does not prevent token-based

access, and session token theft should be considered as an important factor during scoping. Second,

when a cloud platform is compromised, the incident extends to every customer and integration that

trusted that platform with credentials.

Log Sources

We mentioned during preparation the importance of enabling and centralizing logs prior to incidents. This

section discusses control-plane and data-plane logs, what data they contain, and their relevance to incident

response.

Management/control plane logs  record Identity and Access Management (IAM) events, administrative

events, and resource management events. As mentioned earlier, these logs are enabled by default.

IAM events are one of the most critical categories available during an investigation. For initial access, these

logs help determine who logged in, when, from where, and how.

Additional context in these logs, such as success/failure status and login method, provides a more complete

picture of the intrusion. The example in Listing 143 from an Azure sign-in log shows that a user correctly

authenticated with their password but failed both MFA attempts. This pattern could indicate that a

password was successfully stolen but MFA controls are preventing a compromise.

Listing 143 | Azure Sign-In Log Authentication Details

[

{

"authenticationStepDateTime": "2025-05-25T01:54:30.9375542+00:00",

"authenticationMethod": "Password",

"authenticationMethodDetail": "Password in the cloud",

"succeeded": true,

"authenticationStepResultDetail": "Authentication in progress"

Incident Response for Cloud Systems | Chapter 18 | 573

},

{

"authenticationStepDateTime": "2025-05-25T01:54:30.9375542+00:00",

"authenticationMethod": "Mobile app notification",

"succeeded": false,

"authenticationStepResultDetail": "MFA denied; user did not select the correct number"

},

{

"authenticationStepDateTime": "2025-05-25T01:54:30.9375542+00:00",

"authenticationMethod": "Text message",

"succeeded": false,

"authenticationStepResultDetail": "MFA denied; invalid verification code"

}

]

Once access is gained, IAM logs provide insight into persistence or privilege escalation activities, such as

creating new users or assigning additional roles to compromised accounts. Depending on the attacker’s

tactics and techniques, organization-level management events may also appear, such as changes to logging

configuration or domain settings.

Resource management events include the creation, deletion, starting, and stopping of resources. These

events provide significant insight into attacker intentions. Attempts to perform destructive attacks by

deleting critical resources would appear in these logs, as would the creation of GPU-enabled virtual

machines that may indicate a cryptomining attack. The CloudTrail event in Listing 144 shows a RunInstances

call launching a p3.2xlarge GPU instance, a common indicator of cryptomining activity. Details worth noting

include the instance type, the region (attackers often target regions the organization does not normally

use), and the identity that initiated the request.

Listing 144 | CloudTrail Event: GPU Instance Creation

{

"eventTime": "2025-08-14T03:22:17Z",

"eventSource": "ec2.amazonaws.com",

"eventName": "RunInstances",

"awsRegion": "ap-southeast-1",

"sourceIPAddress": "198.51.100.47",

"userIdentity": {

"type": "AssumedRole",

"arn": "arn:aws:sts::471903287148:assumed-role/LambdaExecRole/i-0e83f91a7c42d1b05"

},

"requestParameters": {

"instanceType": "p3.2xlarge",

"instancesSet": { "items": [{ "imageId": "ami-0c7ea5497c02abcf5" }] },

"minCount": 4,

"maxCount": 4

}

}

Data plane logs , also known as resource logs, contain resource-level operations. These logs are off by

default, but without them, responders often lack the full picture of an incident. Table 56  illustrates the

difference between what each log plane captures for common cloud resources.

Table 56 | Control Plane vs. Data Plane Logging

RESOURCE CONTROL PLANE (DEFAULT ON) DATA PLANE (DEFAULT OFF)

Storage

(S3/Blob/GCS)

Bucket creation, deletion, policy

changes

Individual object reads, writes, and

deletions

Virtual machines Instance creation, termination,

security group changes

OS-level logs, network flow logs,

process execution

Databases Instance provisioning, configuration

changes, backup operations

Individual queries, data access, row-

level operations

IAM User creation, role assignments,

policy modifications

Authentication attempts, token

issuance, session activity

Consider an incident where an attacker accesses sensitive files in an S3 bucket.  Control plane logs

(CloudTrail) would show if the attacker modified the bucket policy, but only S3 server access logs or

CloudTrail data events would reveal which specific objects were downloaded. Similarly, if initial access was

gained by compromising a public-facing virtual machine, only the operating system logs on the endpoint or

network flow logs on the VPC would show evidence of the access vector.

Without data plane logs, responders may be able to confirm that a resource was compromised but not what

the attacker did with it. This gap directly affects the organization’s ability to assess data exposure and meet

breach notification requirements.

Without data-plane logs, a breach notification assessment may be impossible. Regulatory

frameworks such as GDPR, HIPAA, and PCI DSS require organizations to determine which

data was accessed during a breach. If the only available logs show that a policy was

changed but not what objects were subsequently downloaded, the organization may be

forced to assume worst-case exposure and notify all affected parties.

Together, control-plane and data-plane logs allow responders to trace an attacker’s path through a cloud

environment. Understanding which log sources are available and what they capture is essential for building

a complete timeline of attacker activity.

Isolating Compromised Resources

When resources are exposed or compromised, it is important to quickly remediate the issues that allow the

threat actor to continue their attack or that could enable a new threat actor to enter the environment.

While different approaches apply depending on the impacted service, this section covers two of the most

commonly targeted public-facing resources: virtual machines and storage accounts/buckets.

Virtual Machine Isolation

When a virtual machine is compromised, it may seem like the only option is to shut down the host. There is

a better approach that maintains the host for deeper analysis and provides insight into the threat actor’s

Incident Response for Cloud Systems | Chapter 18 | 575

intent. With virtual network controls, we can isolate VMs in a configuration that blocks inbound and

outbound traffic, except for designated forensic networks. Combined with flow logs on the isolated subnet

or compromised host, we can monitor what an active threat actor or malware infection is trying to do.

For example, using the Azure CLI, analysts can create a Network Security Group (NSG) with rules designed

to deny all access except for a designated forensics subnet, as shown in Listing 145. This approach keeps the

VM running for continued observation while cutting off the threat actor’s access.

Listing 145 | Isolating a Compromised VM with an Azure NSG

$ az network nsg create --resource-group rg-prod-eastus --name nsg-isolation 1

$ az network nsg rule create --resource-group rg-prod-eastus --nsg-name nsg-isolation --name

AllowForensicsSubnet --priority 100 --direction Inbound --access Allow --source-address-prefixes

192.168.200.0/24 --destination-port-ranges '*' --protocol '*' 2

$ az network nsg rule create --resource-group rg-prod-eastus --nsg-name nsg-isolation --name

DenyAllInbound --priority 4096 --direction Inbound --access Deny --source-address-prefixes '*'

--destination-port-ranges '*' --protocol '*' 3

$ az network nsg rule create --resource-group rg-prod-eastus --nsg-name nsg-isolation --name

DenyAllOutbound --priority 4096 --direction Outbound --access Deny --source-address-prefixes '*'

--destination-port-ranges '*' --protocol '*' 4

$ az network nic update --resource-group rg-prod-eastus --name compromised-vm-nic --network

-security-group nsg-isolation 5

1 Create a dedicated isolation NSG in the same resource group as the compromised VM.

2 Allow inbound access only from the forensics subnet (192.168.200.0/24) at a high priority.

3 Deny all inbound traffic at a lower priority, ensuring the forensics allow rule takes precedence.

4 Deny all outbound traffic to prevent the compromised VM from communicating externally.

5 Apply the isolation NSG to the compromised VM’s network interface to immediately restrict access.

Storage Account and Bucket Remediation

Data exfiltration is one of the top impacts of cloud compromises, and some of the most valuable data resides

in storage accounts or buckets. A simple misconfiguration of a storage resource with sensitive data can

easily lead to exposure, and threat actors are constantly running automated scanners to find misconfigured

buckets.

“Weak or no authentication accounted for nearly half of initial access in H1 2025, with many

environments having overprivileged service accounts with high-privilege default credentials. [7]

— Google Threat Horizons Report, H1 2025

If a bucket has been compromised during an incident, it is important to quickly resolve any

misconfigurations to prevent further data exposure. The specific remediation procedures vary by cloud

provider.

AWS

S3 buckets can be restricted using a combination of Block Public Access  settings and policies.  Block Public

Access overrides any configurations applied via policies or ACLs, making it the most effective first step for

stopping exposure. IAM or resource-based policies can then be applied to specify which users can take what

actions on which buckets. In legacy configurations, Access Control Lists (ACLs) may control access. These

are important to check during a compromise, as attackers can abuse them, but ACLs should not be used for

new access control configurations.

The commands in Listing 146 show how to restrict public access on each provider.

Listing 146 | Restricting Public Access on Cloud Storage

$ aws s3api put-public-access-block --bucket <bucket-name> --public-access-block-configuration

BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true 1

$ aws s3api get-public-access-block --bucket <bucket-name> 2

$ az storage account update --name <account-name> --resource-group <rg-name> --allow-blob-public

-access false 3

$ gcloud storage buckets update gs://<bucket-name> --public-access-prevention=enforced 4

$ gsutil iam ch -d allUsers gs://<bucket-name>

$ gsutil iam ch -d allAuthenticatedUsers gs://<bucket-name>

1 Enable Block Public Access on an S3 bucket, overriding any policies or ACLs that grant public access.

2 Verify the current public access settings after applying the change.

3 Disable anonymous access on an Azure storage account.

4 Enforce public access prevention on a Google Cloud bucket and revoke allUsers and allAuthenticatedUsers bindings.

To assess exposure on AWS, review S3 server access logs or CloudTrail data events for the bucket to

identify what objects were accessed and by whom. The s3logparse tool can simplify the analysis of S3 server

access logs during an investigation.

Azure

If anonymous read access has been granted to an Azure storage resource, it is configured at either the

container level or the blob level, with container-level settings overriding blob-level settings. A user with

permissions to set AllowBlobAnonymousAccess should change the settings to prevent anonymous access

before further exposure occurs on containers that should not be public.

Google Cloud

Permissions on Google Cloud buckets are controlled in two ways: IAM policies and ACLs. To remediate an

exposed bucket, apply IAM policies granting only the permissions needed to the users who need them. As

with AWS, ACLs are a legacy option that should be checked during a compromise investigation but should

not be used for remediation. If both ACLs and IAM permissions are in place, only one needs to allow access

for it to be granted, so checking IAM permissions alone is not sufficient.

Time is a factor when remediating exposed storage. Automated scanners continuously probe for

misconfigured buckets, and public exposure can be discovered and exploited within hours of

misconfiguration. Once access controls are corrected, responders should verify the remediation by

Incident Response for Cloud Systems | Chapter 18 | 577

attempting to access the resource from an unauthenticated context to confirm that public access is no

longer possible.

Exposed storage resources can be discovered and exploited within hours of

misconfiguration. Automated scanners continuously probe for publicly accessible buckets

and containers, so the time between discovery and remediation directly affects the volume

of data exposure. Prioritize restricting access before conducting a full investigation of what

was accessed.

Each of these providers has detailed documentation on access controls, but this overview should point

responders in the right direction when a storage resource is compromised.

Eradicating Cloud Persistence

Cloud environments provide threat actors with numerous methods to establish persistence based on their

level of access post-compromise. While a comprehensive treatment of every persistence technique is

outside the scope of this book, this section highlights the most important areas to examine during

eradication.

Identity and Access Management

IAM is one of the most important services in cloud environments, and it is also one of the easiest places for

a threat actor to establish persistence with the right permissions. In addition to reviewing IAM logs,

responders should directly examine IAM resources for any recently created or modified items.  Areas to

examine include:

• Service accounts created by the threat actor.

• Access keys generated for existing or new accounts.

• Role assignments or policy changes that grant elevated privileges.

• OAuth application consent grants that provide API access without requiring user credentials.

• MFA configuration changes, including disabling MFA or registering attacker-controlled devices.

The CLI commands in Listing 147 can help identify common IAM persistence mechanisms across the major

cloud providers.

Listing 147 | Identifying IAM Persistence Mechanisms

$ aws iam list-users --query 'Users[*].UserName' --output text | xargs -I{} aws iam list-access-

keys --user-name {} 1

$ az ad app list --query "[].{Name:displayName,AppId:appId,Created:createdDateTime}" -o table 2

$ gcloud iam service-accounts list --format="table(email)" | xargs -I{} gcloud iam service-

accounts keys list --iam-account={} --managed-by=user 3

1 List all IAM users and their access keys with creation dates (AWS).

2 List OAuth applications and their creation timestamps to identify recently registered apps (Azure).

3 List all user-managed service account keys to identify keys created by a threat actor (Google Cloud).

Revoking credentials alone is not sufficient if active sessions remain valid. Cloud provider tokens typically

remain valid until they expire, even after the underlying credential is rotated. Responders should revoke

active sessions in addition to rotating credentials:

• In AWS, attach an inline policy to deny actions before a specific time.

• In Azure, revoke user sessions through Entra ID.

• In Google Cloud, invalidate OAuth tokens for the affected service accounts.

These persistence mechanisms should be reviewed as part of any cloud compromise investigation, as they

represent the most common methods for regaining access after an initial response.

IAM is the most common persistence vector in cloud compromises. Mandiant’s M-Trends

2025 report identifies identity-based persistence as the leading method attackers use to

maintain access in cloud environments. [8]

Responders should treat IAM review as the first

priority during eradication, before addressing compute or network persistence.

Compute and Workloads

For compute services, responders should consider virtual machines, containers, and serverless functions, all

of which can be backdoored. For virtual machines, the most common methods of retaining access include:

• Backdooring machine images used to deploy new instances.

• Installing malware on running hosts.

• Injecting malicious user data or startup scripts that execute on boot.

Startup scripts are particularly effective because they re-execute each time the instance boots, surviving

reboots and even redeployments from the same image.

Because startup scripts persist in the instance configuration and re-execute on every boot,

responders should check both running instances and the machine images or launch

templates used to create them. A compromised image will reintroduce the backdoor every

time a new instance is deployed from it.

For containers, the container registry can be poisoned to ensure newly created instances include

backdoors. Responders should compare running container images against known-good digests in the

registry and review any recently pushed images for unauthorized modifications.

Serverless functions are a frequently overlooked persistence vector. An attacker with sufficient permissions

can create a Lambda function, Azure Function, or Cloud Function that executes on a schedule or in

response to events, periodically creating new access keys or exfiltrating data. Because serverless functions

do not have a persistent host, traditional endpoint monitoring cannot detect them. Responders should list

all functions across regions and review their triggers, code, and execution history, as shown in Listing 148.

Listing 148 | Enumerating Lambda Functions Across Regions

$ for region in $(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text); do

echo "=== $region ===" && aws lambda list-functions --region $region --query

Incident Response for Cloud Systems | Chapter 18 | 579

'Functions[*].{Name:FunctionName,Modified:LastModified,Runtime:Runtime}' --output table; done

=== ap-south-1 ===

=== eu-north-1 ===

=== eu-west-3 ===

=== eu-west-2 ===

=== eu-west-1 ===

=== ap-northeast-3 ===

=== ap-northeast-2 ===

=== ap-northeast-1 ===

=== ca-central-1 ===

=== sa-east-1 ===

=== ap-southeast-1 ===

=== ap-southeast-2 ===

=== eu-central-1 ===

=== us-east-1 ===

-------------------------------------------------------------------------

|                              ListFunctions                            |

+-------------------------------+-------------------------+-------------+

|           Modified            |         Name            |   Runtime   |

+-------------------------------+-------------------------+-------------+

|  2022-05-26T17:00:49.000+0000 |  secheaders-cloudfront  |  nodejs14.x |

|  2025-11-05T12:00:13.000+0000 |  erk-requireauth        |  nodejs22.x |

|  2016-02-12T02:09:49.179+0000 |  blackFriday            |  python2.7  |

|  2022-03-01T21:59:46.000+0000 |  testKMSAccess          |  nodejs14.x |

+-------------------------------+-------------------------+-------------+

=== us-east-2 ===

=== us-west-1 ===

=== us-west-2 ===

The challenge with many of these techniques is that they either do not appear in logs or the log entries lack

sufficient context to identify the persistence mechanism. For virtual machines, control-plane logs capture

instance creation and modifications to startup scripts, but the contents of the scripts themselves are not

logged. For serverless functions, the control plane captures function creation and updates, but the function

code and its execution output require separate log sources (such as CloudWatch Logs for Lambda).

Investigation often requires host forensics or manual review of resources in the cloud console to identify

these backdoors.

Networking

Network resources are critical security controls that, with simple modifications, can open access to both

the original threat actor and new ones. A single network security group or ACL change can make a

previously restricted resource accessible from the internet. More advanced techniques include creating

persistent VPN tunnels or reconfiguring DNS settings to redirect traffic.

These are common persistence techniques, but they are not a comprehensive list. Responders should

review network configurations as part of eradication and compare the current state against known-good

baselines where available.

Across all three categories, the common thread is that cloud persistence often requires only API-level

access rather than host-level compromise, making it faster to establish and harder to detect through

traditional endpoint monitoring.

COMMON CLOUD IR MISTAKES

I have seen several recurring mistakes during cloud incident response engagements that are worth

calling out.

First, shutting down compromised instances before capturing them. Once an instance is terminated,

volatile data (memory, running processes, network connections) is lost permanently. Always snapshot

the instance before taking any containment action.

Second, rotating credentials without revoking active sessions. A new password or access key does not

invalidate existing tokens. If an attacker has a valid session token, they can continue operating even

after the credentials are changed. Explicitly revoke sessions in addition to rotating credentials.

Third, assuming control plane logs tell the complete story. I have worked cases where the

investigation concluded based solely on CloudTrail or Activity Log analysis, missing lateral movement

and data access that only appeared in data plane logs, VPC flow logs, or host-level telemetry. Control

plane logs show what was configured, not necessarily what happened after the configuration

changed.

Fourth, checking only one region. Cloud providers operate across dozens of regions, and attackers

frequently create persistence resources in regions the organization does not normally use. An access

key created in us-east-1 can provision a Lambda function in ap-southeast-1 that the team never

checks. Always enumerate resources across all regions during eradication.

Each of these mistakes stems from applying on-premises assumptions to cloud environments.

Building cloud-specific checklists into response runbooks and rehearsing them in tabletop exercises

helps teams avoid these pitfalls when the pressure of a real incident makes shortcuts tempting.

Automated Response Capabilities

One advantage of working in cloud environments is the native tooling available for automated incident

response. The specific implementation depends on the cloud provider and the organization’s response

process, but the core concept applies across all major platforms. The following example demonstrates how

a detection can trigger an automated investigation workflow for a compromised host in AWS. [9]

Trigger: A GuardDuty alert fires for a suspected compromised EC2 instance, and a Lambda function

executes the following steps:

1. The EC2 instance is placed in a private subnet with no internet access.

2. Flow logs are enabled on the subnet, VPC, or network interface to monitor network communications.

3. A snapshot of the EC2 instance is taken and stored in an S3 bucket.

The AWS CLI commands in Listing 149  show what this Lambda function would execute. These same

commands can also be run manually by a responder if automation is not yet in place.

Listing 149 | Automated EC2 Isolation and Snapshot

$ aws ec2 modify-instance-attribute --instance-id i-0a1b2c3d4e5f67890 --groups <isolation-

Incident Response for Cloud Systems | Chapter 18 | 581

security-group-id> 1

$ aws ec2 create-flow-logs --resource-type NetworkInterface --resource-ids eni-0a1b2c3d4e5f67890

--traffic-type ALL --log-destination-type s3 --log-destination arn:aws:s3:::forensics-flow-logs

$ aws ec2 create-snapshot --volume-id vol-0a1b2c3d4e5f67890 --description "Forensic snapshot -

GuardDuty finding 2025-08-14" --tag-specifications

'ResourceType=snapshot,Tags=[{Key=Case,Value=IR-2025-042}]' 3

1 Replace the instance’s security groups with an isolation group that denies all inbound and outbound traffic.

2 Enable flow logs on the instance’s network interface to capture any attempted communications.

3 Create a tagged snapshot of the instance’s EBS volume for forensic analysis.

With this automation in place, responders can be confident the host is isolated without making manual

changes, and they can quickly retrieve the snapshot for host-level forensics.

This is a basic demonstration of the concept, but these types of workflows extend to many response

scenarios. Most manual steps taken during active response can be converted into scripts and actions

triggered automatically by an alert or initiated manually by a responder.

Even without a fully automated pipeline, wrapping the CLI commands shown above in

simple scripts ensures consistent execution under the pressure of an active incident. A

shell script that isolates an instance, enables flow logs, and captures a snapshot can be

written in minutes and eliminates the risk of missed steps or typos during manual

responses.

DEBRIEF

Cloud incidents often reveal gaps in configuration, visibility, and access management that are unique to

cloud environments. The debrief phase is an opportunity to identify these gaps and translate them into

concrete improvements for cloud security posture.  General debrief guidance, including facilitating After-

Action Review (AAR) sessions, documentation requirements, and implementation tracking, is covered in

Debrief Activity . This section focuses on cloud-specific debrief questions and explores how cloud

capabilities themselves can improve future incident response.

Cloud-Specific Debrief Questions

Beyond the standard AAR questions covered in Conducting the After-Action Review, cloud incident debriefs

should address considerations unique to cloud environments:

• Identity and access:  What identities were compromised, and what permissions was the threat actor

able to obtain? Were the identities following the principle of least privilege? If not, what identity

controls should be implemented to reduce the blast radius?

• Resources: What resources were compromised? Did the identities that provided access to those

resources actually need that access, or should more restrictive policies be applied?

• Networking: Did the threat actor bypass any network controls? Were network rules too permissive or

misconfigured? What additional network controls would prevent unauthorized access while maintaining

functionality?

• Data exfiltration: Are there any resources within the blast radius that contain sensitive data (storage

buckets, virtual machines, databases, etc.)? Did the threat actor access these resources? Is there any

evidence of mass exfiltration?

These questions help focus the debrief on cloud-specific lessons that generic incident reviews may

overlook.

Leveraging the Cloud for Incident Response

In the response actions section, we mentioned the ability to use serverless functions to build an automated

response pipeline. This is one of many ways to leverage cloud capabilities for incident response. The same

infrastructure that organizations use for production workloads can be repurposed for forensic analysis,

evidence storage, and automated response, often at a fraction of the cost of maintaining dedicated on-

premises forensic infrastructure. The following sections highlight several ways the cloud can improve

incident response efficiency and effectiveness.

Cloud Infrastructure for Forensic Workstations

Cloud compute resources and infrastructure-as-code templates provide a modern way to equip responders

with forensic workstations. Rather than distributing physical workstations to work locations, organizations

can deploy pre-configured virtual machines with the compute and memory resources needed for intensive

forensics workloads. These images can be maintained with current tooling and deployed on demand,

ensuring responders always have access to a consistent, up-to-date analysis environment.  Infrastructure-

as-code tools such as AWS CloudFormation, Azure Resource Manager templates, or Terraform enable

forensic environments to be created and destroyed with a single command. This makes it practical to spin

up a fresh workstation for each investigation and tear it down when the case is closed.

Secure, Read-Only Log Storage

In cases where forensic integrity is critical, cloud storage simplifies the management of evidence that

requires a chain of custody. Cloud storage provides effectively unlimited capacity at relatively low cost, with

built-in logging capabilities that create an audit trail documenting any access. Access controls and retention

policies can restrict access to read-only for authorized personnel and automatically archive or delete data

based on organizational policies.

Cloud providers also offer immutable storage configurations that prevent evidence from being modified or

deleted, even by administrators.  The AWS CLI example in Listing 150 demonstrates how to configure an S3

bucket with Object Lock, which enforces write-once-read-many (WORM) protection on stored evidence.

Listing 150 | Configuring Immutable Forensic Storage on S3

$ aws s3api create-bucket --bucket forensic-evidence-ir2025 --region us-east-1 --object-lock

-enabled-for-bucket 1

$ aws s3api put-object-lock-configuration --bucket forensic-evidence-ir2025 --object-lock

-configuration '{"ObjectLockEnabled": "Enabled", "Rule": {"DefaultRetention": {"Mode":

"COMPLIANCE", "Days": 365}}}' 2

1 Create a new S3 bucket with Object Lock enabled at creation time.

2 Apply a default retention policy in compliance mode, which prevents any user (including root) from deleting or overwriting

objects for 365 days.

Incident Response for Cloud Systems | Chapter 18 | 583

Azure Blob Storage offers a similar capability through immutable storage policies, and Google Cloud Storage

supports retention policies with bucket lock. Regardless of the provider, the principle is the same: forensic

evidence should be stored in a way that prevents tampering and provides a verifiable chain of custody.

Network Logging with VPC Flow Logs

VPC flow logs capture metadata about network traffic flowing through cloud network interfaces, without

requiring specialized hardware or packet-capture infrastructure. While flow logs do not capture packet

payloads, they provide valuable context for investigations involving network-based attacks, lateral

movement, or data exfiltration. Each flow log record includes source and destination IP addresses, ports,

protocol, bytes transferred, and an accept or reject action, giving responders enough detail to identify

communication patterns, detect data exfiltration volumes, and confirm whether network isolation controls

are working as intended.

Flow log data can be directed to cloud storage or log analytics services for long-term retention and analysis,

enabling reconstruction of network communication patterns during an investigation. Because flow logs

operate at the network layer, they complement control plane logs by providing visibility into traffic that

cloud management APIs do not capture, such as lateral movement between instances within the same VPC

or outbound connections to attacker-controlled infrastructure.

Containers and Serverless for Forensic Tooling

Even without a fully automated response pipeline, containers and serverless services can accelerate triage

and response. Forensic scripts can be containerized or deployed as serverless functions to gather and

analyze evidence with minimal overhead.

Velociraptor is an open-source endpoint monitoring and digital forensics tool that uses a

lightweight agent to collect artifacts, including file system metadata, running processes,

event logs, and memory from target hosts. It supports real-time hunting queries across

large fleets using its own query language (VQL).

For example, a containerized Velociraptor server can be deployed in minutes to collect endpoint telemetry

from compromised hosts across the environment.  Using a container orchestration service, such as Amazon

ECS, Azure Container Instances, or Google Cloud Run, responders can launch a prebuilt Velociraptor server

image, connect agents to target hosts, and begin collecting artifacts without provisioning or configuring a

dedicated server. When the investigation is complete, the container can be stopped and the collected data

preserved in cloud storage.

Listing 151  demonstrates how to deploy a Velociraptor server on Amazon ECS using the AWS CLI. This

creates a Fargate task that runs the Velociraptor frontend, exposes the GUI and client communication

ports, and stores collected artifacts in an EFS volume.

Listing 151 | Deploying a Velociraptor Server on Amazon ECS

$ aws ecs create-cluster --cluster-name forensics-cluster 1

$ aws ecs register-task-definition --family velociraptor-server --network-mode awsvpc --requires

-compatibilities FARGATE --cpu 2048 --memory 4096 --container-definitions '[{"name":

"velociraptor", "image": "wlambert/velociraptor:latest", "portMappings": [{"containerPort":
