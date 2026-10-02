# Chapter 12-3: Containment: Host Token Revocation, Session Termination & Evidence Preservation

> Modular Sub-Chapter | Source: DAIR-IR Framework

---

Persistent disk snapshots

Termination

Protection

Instance termination protection (disable-api-termination) Resource deletion locks Instance deletion protection

Encrypted Communications

Pervasive network encryption complicates traditional containment strategies by obscuring attacker activity. While widespread network cryptography has significantly improved the overall security of modern systems, it has also created new opportunities for threat actors to use encryption as an evasion technique to bypass network-based detection and containment controls.

Transport Layer Security (TLS) interception is particularly valuable to organizations, enabling analysts to analyze malicious traffic patterns during containment activities. Balance security benefits against privacy concerns and potential application compatibility issues, documenting clear policies about what traffic will be inspected and ensuring legal review and authorization of monitoring practices.

Remote Worker Environments

Distributed workforces create unique containment challenges that extend organizational security boundaries far beyond traditional corporate networks into uncontrolled home networks, personal devices, and diverse geographic locations.

Table 23 | Remote Worker Containment Challenges
CHALLENGE IMPACT ON CONTAINMENT RECOMMENDED APPROACH
Network
Visibility
No control over home network
infrastructure; traditional network
isolation unavailable
Shift to endpoint-focused controls using
EDR isolation features
Personal Device
Contamination
Containment actions may affect
personal data on BYOD devices
Use MDM/MAM to selectively manage
corporate data; document policies in
advance
Home Network
Compromise
Attackers may pivot to family devices,
creating liability and notification
obligations
Establish legal review and employee
notification policies before incidents occur
VPN Isolation Disabling all remote access disrupts
legitimate workers
Use per-user or per-device VPN access
policies to restrict only compromised
sessions
Cloud Service
Dependencies
Remote workers access SaaS directly,
bypassing corporate network
controls
Leverage identity-based controls and
conditional access policies
Physical Device
Recovery
Compromised devices spread across
employee homes in different
locations
Ship replacement devices; arrange secure
return shipping for compromised systems

Each row in the table should be backed by a documented process owned by a named team. Containment of a remote worker is rarely a single-action step. Practical details such as who ships the replacement device, how MDM selectively wipes corporate data, and which VPN policy template is applied take too long to work out during an active incident. Capture these procedures during the prepare activity and exercise them in tabletop scenarios.

Network Visibility and Endpoint Controls

Network visibility limitations arise when remote devices operate on home networks outside organizational control, preventing traditional network-based containment and monitoring techniques. Organizations lack visibility into the network infrastructure between remote devices and the internet, cannot control which devices connect to the same home network, and cannot implement network-based isolation when those home routers are owned by internet service providers or employees. For remote work environments, organizations should shift containment strategies toward endpoint-focused controls rather than network-based approaches. This is often implemented using EDR isolation features to quarantine remote devices while preserving the communication channel required for incident response.

Personal Device Contamination

Personal device contamination requires containment strategies that distinguish between corporate and personal data while respecting employee privacy boundaries and legal restrictions. Many organizations permit or require employees to use personal devices for work through Bring Your Own Device (BYOD) programs, creating scenarios in which containment actions might affect personal device use. For BYOD programs, organizations should implement Mobile Device Management (MDM) or Mobile Application Management (MAM) solutions that can selectively manage and eliminate corporate data, revoke access to company resources, or isolate business applications without affecting personal information. Document clear policies about the extent of organizational control over personal devices and ensure employees understand containment capabilities before incidents occur.

Home Network Compromise

Home network compromise scenarios present complex ethical and legal considerations when attackers pivot from compromised corporate devices to family systems owned by non-employees. This pivot is largely a consequence of inadequate remote-worker configuration rather than an inherent risk of remote work. For example, a managed device with an enforced always-on VPN, strict host firewall, and no routable path to the local (residential) subnet cannot scan the household network in the first place. A work laptop that can see a family member’s network-attached storage already had a path suitable for data exfiltration regardless of attacker presence. Where the controls are weaker, attackers who compromise a corporate laptop on a home network might scan for other devices, such as personal computers, smart home systems, or family members' devices, creating potential liability and notification obligations when employee family members become collateral victims.

Organizations should determine in advance which notifications they will provide to employees about home network risks, what assistance they will offer to help secure personal systems, and what coordination may be necessary with employees' households during containment activities. These decisions require legal network access for individual remote sessions without affecting all remote workers. For example, to contain a system under investigation, modify the VPN access control list to restrict the compromised employee’s VPN session to only access email and the help desk ticketing system, preventing lateral movement to file shares and internal applications while allowing the employee to report issues and receive guidance. Cloud service dependencies challenge traditional containment when remote workers rely heavily on SaaS applications that may lack granular isolation capabilities and operate outside organizational network perimeters. Remote workers often access most applications directly over the internet, bypassing corporate networks and VPN connections, making network-based containment impractical. Instead, leverage identity-based controls and conditional access policies to contain compromised credentials, restrict access based on device compliance, or force re-authentication to interrupt active sessions. Document the containment capabilities of critical SaaS applications during planning activities, identifying which services support granular session termination, per-user restrictions, or conditional access policies that can be applied by the incident response team.

Physical device recovery presents logistical challenges when compromised systems reside in employee homes across different cities, states, or countries rather than being physically accessible in corporate facilities. Coordinate with employees to retrieve devices through secure shipping arrangements, schedule on-site visits where warranted by incident severity, or implement remote wiping capabilities that preserve business continuity but may destroy forensic evidence. Balance the investigative value of forensic evidence against the business impact of device unavailability and the logistical complexity of physical recovery across distributed locations. For example, for a suspected malware infection on a remote sales representative’s laptop in another state, consider shipping a pre-configured replacement laptop overnight while arranging return shipping for the compromised device with instructions to power it down until the shipping container arrives, avoiding the expense and delay of sending forensic specialists on-site for a routine malware case.

Beyond Traditional Host Compromise

Traditional incident response focuses heavily on compromised endpoints and servers, but modern organizations face increasingly complex incidents that don’t fit the attacker-on-a-host model, where responders can simply isolate infected systems from the network. These scenarios require fundamentally different containment approaches that often prioritize service disruption, data flow control, and third-party coordination over traditional network isolation.

Figure 85 | Traditional and Modern Containment Challenges

The sections that follow address modern compromise variants that each call for different containment controls.

Business Email Compromise

Business Email Compromise (BEC) is one of the most prevalent non-host incidents, in which attackers leverage legitimate email infrastructure to conduct financial fraud or data theft without traditional endpoints or servers. In BEC incidents, attackers gain access to email accounts through phishing, password reuse, or session hijacking, then use the compromised accounts to send fraudulent messages with the intention to commit fraud (such as wire transfer requests), harvest sensitive information, or redirect victims to attacker-controlled systems.

Containment requires implementing email flow redirection rules to quarantine messages from compromised accounts, deploying conditional access policies to block sign-ins from suspicious locations or devices, and coordinating with email service providers to identify and stop fraudulent messages. The challenge lies in distinguishing legitimate business communications from attacker-controlled messages while maintaining operational continuity for critical business processes. Although the attacker’s actions on objectives are often carried out in cloud infrastructure, the initial compromise often does not. A keystroke logger, infostealer, or session-cookie grabber on the user’s endpoint is a common way attackers obtain cloud access in the first place. A host investigation is still warranted even when the visible activity is entirely observed within the cloud SaaS platform. Include endpoint evidence collection and EDR review of the affected user’s devices in the BEC containment

Supply Chain Incidents

Supply chain incidents involve compromised software: either an upstream vendor’s product is poisoned and subsequently runs in the organization’s environment, or the organization’s own build pipeline is compromised and ships malicious artifacts to its customers. Containment strategies for these incidents span beyond organizational boundaries in either direction.

When attackers compromise build systems, code repositories, or deployment pipelines, containment efforts need to address not only internal infrastructure but also the compromised software artifacts that may have already been distributed to customers or deployed to production systems. This might involve coordinating package repository takedowns to prevent further distribution of compromised software, revoking code-signing certificates used by attackers to sign malicious builds, or launching customer notification campaigns while simultaneously securing internal development processes.

The interconnected nature of modern software supply chains means that containment decisions ripple far beyond the initially affected organization and might require coordination with repository maintainers, platform providers, and external coordination centers to effectively mitigate the threat. For example, if an organization discovers that attackers have compromised a company’s CI/CD pipeline and injected malicious code into three published versions of a popular software package, the organization needs to not only remove access to the malicious packages and respond to the initial breach but also contact users of the software with a coordinated security advisory notifying users which versions are affected.

MODERN BREACH COMPLEXITY: THE MOVEIT SUPPLY CHAIN ATTACK

Today’s breach landscape defies traditional incident response assumptions. Consider the 2023 MOVEit attacks: a single vulnerability in file-transfer software triggered a cascading breach affecting hundreds of organizations worldwide, none of which were directly compromised by attackers. First National Bank of Omaha (FNBO) exemplifies this complexity. The bank discovered that 57,000 customer records, including names, Social Security numbers, and bank account numbers, had been stolen by the Clop ransomware group. Yet FNBO’s networks remained uncompromised. The breach occurred because FNBO used Pension Benefit Information (PBI) Research Services for pension administration, and PBI used MOVEit Transfer for file transfers. When Clop exploited MOVEit’s zero-day vulnerability, they gained access to PBI’s systems and consequently FNBO’s customer data. This attack pattern reveals how modern breaches transcend organizational boundaries through interconnected business relationships. FNBO’s experience illustrates partner ecosystem exposure as much as supply chain compromise: FNBO had no MOVEit deployment of its own, and the compromise reached them through their service provider PBI rather than through software running in their own environment. Traditional containment strategies assume you can isolate compromised systems within your control. When your data is compromised through a vendor’s vendor’s software vulnerability, there are no internal systems to isolate, no network segments to quarantine, and no processes to terminate.

FNBO’s containment strategy focused entirely on external coordination: assessing data exposure with PBI, coordinating customer notifications, arranging credit monitoring services, and managing regulatory reporting, all while lacking visibility into or direct control over the compromised infrastructure. The bank’s incident response team had to contain a breach they couldn’t see, investigate systems they couldn’t access, and remediate vulnerabilities they couldn’t patch. Similar scenarios affected Deutsche Bank, ING, and hundreds of other organizations during the same attack campaign, demonstrating that modern containment should account for systemic risks embedded in partner ecosystems and SaaS platforms rather than focusing solely on direct system compromise.

Partner Ecosystem Breaches

Partner ecosystem breaches compromise the organization’s data rather than its software: a SaaS provider, managed service partner, or business vendor is attacked, and the organization’s data is exposed through the partner’s systems even though the organization’s own environment is unaffected. These incidents require containment strategies that focus on cutting off data flows rather than isolating systems. SaaS provider breaches, managed service provider compromises, or vendor data exposure incidents require rapid assessment of data exposure scope, implementation of API access restrictions to prevent further data synchronization, revocation of integration permissions that allow third-party access to internal systems, and coordination with external parties who may have different incident response priorities and capabilities. The challenge lies in limited visibility into third-party security practices and no direct control over compromised external systems, forcing organizations to implement containment through access-control boundaries at their own perimeters.

For example, when learning that a SaaS CRM provider was breached and customer data might be exposed, immediately revoke the provider’s API access tokens to prevent further data synchronization, disable any automated data feeds from internal databases to the SaaS platform, audit what data was shared with the provider to assess exposure scope, and contact the provider’s security team to coordinate investigation activities and understand the timeline for their containment and remediation efforts. These incidents challenge traditional containment models by requiring organizations to contain threats they cannot directly observe or control, relying instead on trust relationships, contractual obligations, and regulatory frameworks to ensure effective response.

CONTAINMENT VALIDATION

Confirming successful containment requires ongoing validation through multiple monitoring channels. Our goal is to ensure that containment measures effectively stop attacker activities and that adversaries have not maintained alternative access methods that bypass the team’s isolation efforts. Organizations should implement multiple validation strategies to ensure containment is effective, including network and process monitoring, and log analysis.

Table 24 | Containment Validation Channels
connections to known attacker infrastructure and watching for new communication patterns that might
indicate alternative C2 channels. Review firewall logs, proxy logs, and DNS queries to verify that
compromised systems no longer communicate with external attacker infrastructure or suspicious
destinations. Monitor for changes in network behavior that might indicate an attacker shifting tactics to
move to different C2 infrastructure or tunneling through allowed protocols. Where possible, use a
combination of network monitoring from network appliances and external servers, and live investigation of
contained systems to verify that no unauthorized outbound connections occur.

Process monitoring verifies that malicious processes are no longer executing and that attackers have not deployed additional persistence mechanisms during or after containment. Track system process creation on contained systems to detect suspicious new processes, monitor for service installations that might represent attacker persistence, and analyze running processes against known malware indicators. EDR platforms can provide continuous process monitoring that identifies unusual parent-child process relationships, uncommon executable paths, or processes communicating with unusual network destinations. Lacking an EDR platform, organizations can also monitor processes using Sysinternals Process Explorer (as shown in Figure 86) on Windows systems, or the ps, and top/htop commands on Linux systems. Establish a baseline of expected process activity on contained systems and investigate any deviations that might suggest continued attacker presence.

Figure 86 | Process Explorer Indicates Unusual Parent-Child Process Relationship for LSASS process

Log analysis ensures no new indicators of compromise emerge after containment by monitoring authentication, application, and security event logs for suspicious activity. Watch for failed authentication attempts that might indicate attackers attempting to regain access through alternative credentials, privilege escalation attempts suggesting persistent local access, or unusual file access patterns indicating continued data exfiltration. Compare log activity before and after containment to identify changes in attacker behavior and verify that malicious activity has ceased rather than simply shifted to different techniques. Consider any pertinent logging sources specific to the environment, including logs generated on the contained system(s) and external systems.

CONTAIN ACTIVITY EXAMPLES

The following examples illustrate where containment is an important part of the incident response process.

The Multi-Tenant Credential Exposure

Sarah, the incident response team lead for a Kubernetes managed service provider, had been working on an incident that impacted multiple customers in AWS. An AWS GuardDuty alert flagged unusual API activity from an unfamiliar IP address, which the team traced to AWS credentials in a read-only Kubernetes dashboard that was (unfortunately) exposed to the internet. The dashboard used a service account with read permissions to cluster-wide secrets. Kubernetes (K8s) audit logs showed that the attacker used dashboard access to list secrets across three customer namespaces: TechFlow Solutions, Meridian Financial, and Cascade Logistics.

CloudTrail logs confirmed that the attacker had only used credentials from TechFlow’s namespace to launch two EC2 instances in the TechFlow AWS account. However, because the K8s audit logs showed the attacker had viewed secrets for all three customers, Sarah got approval to implement simultaneous coordinated containment across all three customer AWS accounts to prevent the attacker from pivoting to the other exposed credentials.

A different team had already taken steps to remedy the Kubernetes dashboard exposure. Sarah’s role was to prevent unauthorized access to the customer’s AWS accounts. She began containment by disabling the exposed AWS access keys across all three customer accounts. For TechFlow Solutions, she disabled the access key the attacker had been actively using, as shown in Listing 58.

Listing 58 | Disable Compromised AWS Access Key for TechFlow Solutions
$ aws iam list-access-keys --user-name k8s-service-account --profile techflow-prod
{
"AccessKeyMetadata": [
{
"UserName": "k8s-service-account",
"AccessKeyId": "AKIA_DUMMY_SAMPLE_KEY_02",
"Status": "Active",
"CreateDate": "2025-11-09T14:22:31Z"
}
]
}
$ aws iam update-access-key --user-name k8s-service-account --access-key-id AKIA_DUMMY_SAMPLE_KEY_02 --status Inactive --profile techflow-prod
$ aws iam list-access-keys --user-name k8s-service-account --profile techflow-prod
{
"AccessKeyMetadata": [
{
"UserName": "k8s-service-account",
"AccessKeyId": "AKIA_DUMMY_SAMPLE_KEY_02",
"Status": "Inactive",
"CreateDate": "2025-11-09T14:22:31Z"
}
]
}

Sarah repeated the same credential-disabling process for the Meridian Financial and Cascade Logistics accounts, even though CloudTrail showed no evidence of attacker activity in those environments. This precautionary containment prevented the attacker from using any credentials disclosed through the K8s dashboard.

Next, Sarah isolated the two EC2 instances launched by the attacker in the TechFlow account. She applied resource tags to mark them as under investigation, enabled termination protection to prevent accidental deletion, and created EBS snapshots for forensic analysis, as shown in Listing 59.

Listing 59 | Apply Tags and Termination Protection to Compromised TechFlow Instances
$ aws ec2 describe-instances --filters "Name=tag:Customer,Values=TechFlow" --query 'Reservations[].Instances[].InstanceId' --output text --profile techflow-prod
i-a09727b1175f6b58e i-8d7f7414a5081787e
$ aws ec2 create-tags --resources i-a09727b1175f6b58e i-8d7f7414a5081787e --tags

Key=Status,Value=UnderInvestigation Key=IR-Case,Value=2025-042 Key=ContainedBy,Value=sarah-ir-team --profile techflow-prod $ aws ec2 modify-instance-attribute --instance-id i-a09727b1175f6b58e --disable-api-termination --profile techflow-prod $ aws ec2 modify-instance-attribute --instance-id i-8d7f7414a5081787e --disable-api-termination --profile techflow-prod $ aws ec2 create-snapshot --volume-id vol-049df61146c4d7901 --description "IR-2025-042 TechFlow instance evidence" --profile techflow-prod { "SnapshotId": "snap-01234567890abcdef", "VolumeId": "vol-049df61146c4d7901", "State": "pending", "StartTime": "2025-11-02T15:42:18.000Z" } Next, she modified the security groups attached to both compromised instances to quarantine them while maintaining SSH access for investigation, as shown in Listing 60.

Listing 60 | Create Quarantine Security Group and Apply to Compromised Instances
$ aws ec2 create-security-group --group-name IR-Quarantine-2025-042 --description "Quarantine SG
for IR case 2025-042" --vpc-id vpc-0a1b2c3d --profile techflow-prod
{
"GroupId": "sg-0123456789abcdef0"
}
$ aws ec2 authorize-security-group-ingress --group-id sg-0123456789abcdef0 --protocol tcp --port
22 --cidr 198.51.100.10/32 --profile techflow-prod 1
$ aws ec2 revoke-security-group-egress --group-id sg-0123456789abcdef0 --protocol all --cidr
0.0.0.0/0 --profile techflow-prod 2
$ aws ec2 modify-instance-attribute --instance-id i-a09727b1175f6b58e --groups sg-0123456789abcdef0 --profile techflow-prod
$ aws ec2 modify-instance-attribute --instance-id i-8d7f7414a5081787e --groups sg-0123456789abcdef0 --profile techflow-prod
1 Allow SSH access only from the IR team jump box at 198.51.100.10
2 Block all outbound traffic to prevent communication with the attacker.

With the AWS resources contained, Sarah addressed the Kubernetes platform compromise. Rather than deleting the overprivileged service account (which would destroy evidence), she disabled it by removing its Role-Based Access Control (RBAC) bindings, as shown in Listing 61.

Listing 61 | Disable Kubernetes Service Account by Removing RBAC Bindings
$ kubectl get clusterrolebinding dashboard-secrets-reader -o yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
name: dashboard-secrets-reader
roleRef:
apiGroup: rbac.authorization.k8s.io
kind: ClusterRole
name: cluster-secrets-reader
subjects:
- kind: ServiceAccount
name: dashboard-viewer
namespace: kubernetes-dashboard
$ kubectl delete clusterrolebinding dashboard-secrets-reader
clusterrolebinding.rbac.authorization.k8s.io "dashboard-secrets-reader" deleted
$ kubectl annotate serviceaccount dashboard-viewer -n kubernetes-dashboard IR-Case=2025-042
Status=Disabled ContainedBy=sarah-ir-team
serviceaccount/dashboard-viewer annotated

To validate containment effectiveness, Sarah continued to monitor CloudTrail, confirming no new API activity from the disabled access keys. K8s audit logs showed no new dashboard access attempts, and the quarantined security groups prevented all outbound connections from the compromised EC2 instances. She configured CloudWatch alarms to alert if disabled access keys were reactivated or if new access keys were created for the compromised service accounts.

Sarah documented the containment actions for incident tracking and customer notification:

• Account-based IOCs: Compromised K8s service account dashboard-viewer, AWS IAM users k8s-service-account for TechFlow, Meridian, and Cascade

• Network IOCs: Attacker source IP 185.220.101.42 accessing K8s dashboard

• Cloud resource IOCs : Two unauthorized EC2 instances (i-a09727b1175f6b58e, i-8d7f7414a5081787e) in TechFlow account

• Contained resources: 3 AWS IAM access keys disabled, 2 EC2 instances quarantined with termination protection enabled, K8s service account RBAC bindings removed, K8s dashboard ingress removed

• Customer impact : TechFlow Solutions (confirmed compromise with 2 EC2 instances launched), Meridian Financial (precautionary credential rotation due to possible exposure), Cascade Logistics (precautionary credential rotation due to possible exposure)

The Ransomware Rapid Response

Marcus Chen, a senior support desk analyst at Vanguard Point Advisors, a mid-size financial services firm, received an urgent call from Robert Dackinson in the accounting department. Robert reported that several spreadsheets had become corrupted with unusual file extensions, and he found a text file on his desktop titled README_RANSOM.txt. Marcus recognized the indicators immediately and escalated the ticket to Priority 1, in accordance with the organization’s ransomware response playbook. The playbook’s first step required immediate EDR isolation to prevent further access to company systems. Marcus opened CrowdStrike Falcon and searched for Robert’s workstation using the company’s standard naming convention. The search returned Robert’s system RD-LAPTOP-278 as shown in Figure 87.

Figure 87 | CrowdStrike Falcon EDR Workstation Search

Marcus selected the device and initiated network containment through Falcon’s isolation feature, as shown in Figure 88  and Figure 89 . This action immediately blocked all network communication from Robert’s laptop except for the encrypted management channel that Falcon uses to maintain remote access for investigation. This step prevented the ransomware from spreading to network file shares or attempting other lateral movement while preserving the ability to collect forensic evidence remotely.

Figure 88 | CrowdStrike Falcon EDR Workstation Containment

Figure 89 | CrowdStrike Falcon EDR Workstation Containment Confirmation

After several seconds, Marcus validated the containment action by inspecting the status of Robert’s workstation. CrowdStrike indicated that the isolation command had been successfully applied with the status label "Update network containment status", as shown in Figure 90 . Marcus updated the incident

Figure 90 | CrowdStrike Falcon EDR Workstation Containment Validation

With the system successfully quarantined, Marcus continued to follow the playbook’s identity-containment steps. He accessed the organization’s Okta identity platform and temporarily disabled Robert’s account to prevent the ransomware from using any cached credentials to access cloud applications or network resources. Marcus then revoked all active sessions and refresh tokens for Robert’s account across all connected applications.

Marcus documented all containment actions in the incident ticket, with precise timestamps, as shown in Table 25.

Table 25 | Containment Actions Summary
TIME ACTION TAKEN
11:47 AM Received report from Robert Dackinson about file corruption and ransom note
11:49 AM Escalated to P1 incident, initiated ransomware playbook
11:51 AM Isolated workstation RD-LAPTOP-278 using CrowdStrike Falcon EDR
11:52 AM Verified network containment using CrowdStrike Falcon console
11:54 AM Disabled user account robert.dackinson@vanguardpointadvisors.com in Okta
11:55 AM Revoked all active sessions and refresh tokens for compromised account
11:57 AM Escalated to IR team for forensic investigation and eradication planning

The rapid containment prevented the ransomware from spreading beyond Robert’s workstation. Later investigation revealed that the ransomware had successfully encrypted 247 local files but had been isolated before it could access network file shares that contained critical financial data. The coordinated EDR and identity containment approach, executed in under ten minutes from initial report, demonstrated the value of well-documented playbooks and modern containment tools for ransomware response.

CONTAIN: STEP-BY-STEP

The following steps provide a condensed reference for containment activities. Each step corresponds to topics covered earlier in this chapter, organized for use when stopping attacker activity, preserving evidence, and preventing further harm.

Step 1. Assess Containment Urgency and Strategy

1. Evaluate immediate containment triggers that demand urgent action, including:

◦ Active data destruction or encryption in progress.

◦ Ongoing data exfiltration of sensitive information.

◦ Threats to critical operations or safety systems.

◦ Regulatory compliance timeframes that require a rapid response.

2. Determine containment approach based on organizational context:

◦ Passive containment: Monitor attacker activities to gather intelligence while limiting damage.

◦ Active containment: Take decisive action to stop attacker activities, accepting the possibility of alerting the attacker.

◦ Adaptive containment: Combine approaches with progressively restrictive measures based on attacker behavior.

◦ Deceptive containment: Deploy honeypots or decoy systems that appear identical to production to divert the attacker while gathering intelligence and protecting real assets.

3. Balance competing priorities, including:

◦ Evidence preservation needs versus operational continuity requirements.

◦ Intelligence-gathering value versus the risk of continued attacker access.

◦ Business impact of containment measures versus security benefits.

4. Plan coordination strategy for complex incidents, including:

◦ Identify all known compromised systems, accounts, and services.

◦ Coordinate timing across network, endpoint, identity, and application teams.

◦ Prepare for simultaneous containment actions to prevent attacker pivoting (sequential isolation alerts adversaries and gives them time to escalate).

◦ Plan credential reset sequencing to prioritize the most privileged accounts first, then service accounts, then standard user accounts.

◦ Prepare rollback procedures for infrastructure-wide changes such as firewall rule updates or network topology modifications.

◦ Establish communication channels for coordinated execution.

Step 2. Implement Identity and Access Containment

1. Invalidate compromised credentials across all authentication systems for the known-compromised set (eradicate Step 4 expands credential remediation to the blast-radius accounts revealed during scope and to deeper identity primitives like KRBTGT and trust passwords), including:

◦ Reset passwords for affected user accounts through the primary identity provider.

◦ Rotate service account credentials, API keys, and programmatic access tokens.

◦ Coordinate credential resets for accounts synced across multiple systems (on-premises and cloud).

◦ Prioritize privileged accounts and high-risk compromises first.

2. Terminate active sessions to prevent continued access, including:

◦ Revoke all active sessions and authentication tokens through the identity provider.

◦ Force disconnect VPN connections through the concentrator management interface.

◦ Terminate active RDP sessions on Windows servers using built-in session-management commands.

◦ Kill active SSH sessions on Linux systems using process-management commands.

◦ Invalidate browser sessions by incrementing the session token version, where the IdP supports it.

◦ Contact the SaaS application support team for a forced logout when necessary.

3. Revoke refresh tokens and persistent credentials, including:

◦ Invalidate OAuth refresh tokens that could generate new access tokens.

◦ Revoke offline access tokens that enable access without user interaction.

◦ Implement token deny lists for stateless JWT tokens where applicable.

◦ Monitor authentication logs for token endpoint requests indicating cached credential use.

4. Implement conditional access policies for ongoing protection, including:

◦ Deploy location-based restrictions blocking authentication from attacker geographic regions.

◦ Require device compliance for authentication only from managed endpoints.

◦ Enable risk-based policies that block sign-ins from suspicious IP addresses or from users exhibiting anomalous behavior.

◦ Escalate MFA requirements to phishing-resistant methods.

5. Coordinate SSO and multi-application containment, including:

◦ Disable compromised accounts at the IdP level to block authentication to all SSO-connected applications.

◦ Verify which applications use the IdP for authentication, versus those that use local accounts, requiring separate revocation.

◦ Monitor for authentication synchronization delays between the IdP and connected applications.

◦ Enforce MFA requirements at the IdP level, escalating to phishing-resistant methods during containment.

6. Disable third-party integrations and automation, including:

◦ Revoke OAuth-connected applications authorized by compromised accounts.

◦ Disable automation rules, webhooks, and CI/CD deployment keys.

◦ Invalidate API tokens authenticating programmatic access.

◦ Review and disable browser extensions with broad permissions.

Step 3. Implement Network and Host Containment

1. Deploy network-level isolation, including:

◦ Move compromised systems to quarantine VLANs with restricted access.

◦ Implement firewall rules blocking specific protocols, ports, or destinations.

◦ Configure DNS sinkholes redirecting attacker domains to internal monitoring systems.

◦ Apply micro-segmentation using host-based firewalls or software-defined networking.

◦ Consider route manipulation for enterprise-wide containment of widespread compromises.

2. Isolate individual hosts while maintaining investigative access, including:

◦ Enable EDR isolation features to quarantine systems while preserving forensic connection.

◦ Configure local firewall rules to block inbound and outbound connections, except for management protocols.

◦ Remove compromised instances from production scaling groups and load balancers (cloud environments).

◦ Implement process termination for identified malicious processes (with caution for watchdog processes).

◦ Apply application control technologies (AppLocker, Gatekeeper, AppArmor) to block execution of unauthorized executables, scripts, and libraries.

3. Apply application-level restrictions, including:

◦ Deploy web application firewall rules blocking malicious request patterns.

◦ Implement database access restrictions and query monitoring for unusual patterns.

◦ Disable AI agent tool access and MCP server connections for compromised accounts or exploited integrations.

◦ Revoke service principals or API keys granting AI systems access to organizational data (these are often separate from user account credentials).

◦ Configure email flow rules to quarantine messages from compromised accounts.

◦ Apply service disruption where other containment methods prove insufficient: stop web services being used for exfiltration, disable remote access protocols such as RDP or SSH that provide attacker entry points, or shut down specific compromised business applications. Coordinate service disruption with business stakeholders.

Step 4. Implement Cloud-Specific Containment

1. Verify cloud security demarcation for affected services, including:

◦ Determine which containment actions the organization can implement directly and which require cloud provider engagement.

◦ Do not rely on broad IaaS, PaaS, or SaaS labels to determine responsibility; verify the security demarcation for each specific product.

◦ Engage cloud provider security teams for incidents affecting infrastructure outside customer control (e.g., hypervisor, physical networks).

2. Prioritize cloud identity containment, including:

◦ Disable compromised IAM user access keys to prevent API calls and console access.

◦ Rotate service principal credentials used by automated systems.

◦ Revoke OAuth tokens and refresh tokens for cloud application access.

◦ Document operational impact on downstream automation and coordinate credential updates.

3. Apply cloud network isolation controls, including:

◦ Modify security group rules or network ACLs to restrict traffic.

◦ Move instances to a pre-configured isolation VPC dedicated to incident response.

◦ Remove instances from production load balancers while maintaining running state.

4. Enable cloud resource protection and tracking, including:

◦ Apply resource tags marking compromised assets (Status:UnderInvestigation, IR-Case:NNN).

◦
