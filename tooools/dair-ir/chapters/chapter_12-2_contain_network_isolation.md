# Chapter 12-2: Containment: Network Microsegmentation, Conduit Isolation & Traffic Blocking

> Modular Sub-Chapter | Source: DAIR-IR Framework

---

months) Revoke via IdP token management High: generates new access tokens silently

OAuth Offline

Access Token

Long (months or indefinite) Revoke via IdP; may require app-specific action High: enables access without user interaction

SAML

Assertion

Short (minutes) Expires naturally; clear SP session caches Medium: may be cached by service providers

JSON Web

Token (JWT) Variable (configured at issuance) No native revocation; requires token deny lists at each resource server High: stateless and self-contained For example, when containing a compromised service account in a microservices environment using OAuth authentication, responders should use the authorization server’s API to revoke both the access tokens currently being used for API calls and the refresh tokens stored in the application’s configuration, then monitor authentication logs over the next several days to verify that no new tokens are successfully issued using the old credentials. Watch for token endpoint requests that would indicate an attacker’s attempts to use cached credentials.

Organizations should document the token types and revocation capabilities for critical applications during preparation activities, creating a reference guide that identifies which tokens can be revoked centrally through the IdP and which require application-specific revocation procedures. This documentation proves invaluable during incidents when responders need to quickly understand whether resetting an account password will actually terminate all attacker access or if additional token revocation steps are necessary.

Conditional Access Policy Implementation

After invalidating existing credentials and sessions, implement conditional access policies that prevent attackers from re-authenticating while allowing legitimate users to regain access through verified channels. Create temporary policies specific to the incident that block authentication attempts matching attacker patterns while preserving the organization’s operational capability. Deploy location-based restrictions that block authentication from geographic regions where the attacker operated. For accounts accessed from known employee locations, create conditional access policies that block sign-ins from countries or regions where the organization has no legitimate presence. While not a comprehensive defense, this additional control can be effective when the legitimate user operates from a known location outside the attacker’s infrastructure.

Where possible, combine geographic restrictions with device compliance requirements that allow authentication only from managed devices enrolled in the organization’s endpoint management platform. accessing resources even if they obtain valid credentials again.

Risk-based conditional access policies leverage identity provider risk detection to automatically restrict access when suspicious authentication patterns appear. Typically integrated with a Cyber Threat Intelligence (CTI) feed, these policies adapt dynamically to emerging threats without requiring manual rule updates. A sample decision tree for applying different controls based on risk-based conditional access is shown in Figure 81.

Figure 81 | Risk-Based Conditional Access Policy Example

Enable account risk policies that block sign-in when the IdP detects credential leakage, impossible travel patterns, or authentication from suspicious IP addresses known to host malicious infrastructure.  Configure sign-in risk policies that require step-up authentication with phishing-resistant Multi-Factor Authentication (MFA) when authentication attempts exhibit risk indicators such as unusual user-agent strings, anomalous authentication timing, or unfamiliar device fingerprints.

Multi-Application Containment Through SSO

Single Sign-On (SSO) platforms enable simultaneous containment across connected applications through centralized identity controls. When implemented consistently, incident responders can significantly reduce the time required to contain widespread account compromises. Rather than logging into each SaaS application individually to revoke access, analysts can disable the account at the IdP level to block authentication to all SSO-connected applications that rely on the identity provider for authentication decisions.

When disabling accounts via SSO, verify which applications use the IdP for authentication and which use local accounts or other authentication mechanisms. Many organizations maintain hybrid authentication where some applications federate to the central IdP while others use local credential stores that require separate revocation actions. For example, an organization’s Salesforce instance might use Okta for SSO authentication, but a legacy on-premises Enterprise Resource Planning (ERP) system might have local accounts with the same username that require separate disabling through the ERP’s administration interface.

Coordinate MFA enforcement across the environment to prevent attackers from bypassing additional verification, even when they possess valid passwords stolen through infostealer tools. Wherever possible, enable MFA requirement policies at the IdP level that apply uniformly to all connected applications, ensuring a consistent security posture across the SaaS ecosystem.  During containment, escalate MFA to phishing-resistant methods like FIDO2 security keys, which cannot be compromised by browser-in-the-middle phishing attacks, and block SMS-based or Time-Based One-Time Password (TOTP) authenticator apps, which are more susceptible to attacker interception.

Monitor for authentication synchronization delays between the IdP and connected applications, recognizing that some applications cache authentication decisions or maintain local session state that might preserve access briefly after the IdP disables accounts centrally. Enterprise SaaS applications typically check authentication status with the IdP frequently (every few minutes to hours), but some legacy or custom applications might only validate credentials during initial login and maintain sessions indefinitely thereafter. Track timing between account disabling actions and when attacker activity ceases, documenting synchronization delays that inform future containment timing decisions.

Session Management Across Hybrid Environments

Users maintain active sessions across on-premises systems, cloud services, and remote access solutions simultaneously, any of which provide attackers with persistent access after responders implement primary containment actions. Coordinate session termination across all these environments to prevent attackers from maintaining access through alternative authentication pathways. For VPN access, identify active sessions through the VPN concentrator’s management interface and forcibly disconnect them by username or session ID. Many enterprise VPN solutions provide administrative interfaces for viewing active connections and terminating specific user sessions. After disconnecting active sessions, implement access control list restrictions that temporarily block the account from establishing new VPN connections while the investigation continues.

Remote Desktop Protocol connections require identifying active sessions on each accessible Windows server or workstation. Use PowerShell to query session information across multiple systems simultaneously using Invoke-Command and qwinsta as shown in Listing 51 . Terminate identified sessions using the rwinsta command, then verify disconnection by querying the session state again.

Listing 51 | Enumerate Active RDP Sessions Across Multiple Servers
PS C:\> Invoke-Command -ComputerName server01,server02,server03 -ScriptBlock {qwinsta}
ComputerName : server01
SESSIONNAME       USERNAME        ID  STATE   TYPE        DEVICE
>console          administrator    1  Active
rdp-tcp#12       jsmith           2  Active
rdp-tcp#13       guest            3  Disc
ComputerName : server02
SESSIONNAME       USERNAME        ID  STATE   TYPE        DEVICE
>console          svc_backup       1  Active
rdp-tcp#5        administrator    2  Active
rdp-tcp#8        jdoe             3  Disc
ComputerName : server03
SESSIONNAME       USERNAME        ID  STATE   TYPE        DEVICE
>console          system           1  Active
rdp-tcp#4        rwalker          2  Active
rdp-tcp#6        analyst          3  Active

Browser session management becomes critical as many SaaS applications rely on persistent browser sessions stored in cookies that may survive credential resets and continue providing access until they expire naturally. Identity provider platforms may increment session token versions, invalidating all issued session cookies by changing the token signing key or session identifier format.  For example, Microsoft Entra ID’s revoke refresh tokens  action increments the user’s session token version, invalidating all previously issued cookies and forcing re-authentication across all applications on the next request. Coordinate session termination timing across all these mechanisms to avoid sequential revocation that alerts attackers to defensive actions and provides time to establish additional persistence. Create a checklist of session termination actions for the environment and execute them simultaneously during a planned containment window, preferably within a limited timeframe that gives attackers minimal opportunity to respond.

Create an environment-specific session termination checklist during preparation. The number of session types in a modern environment (VPN, RDP, browser sessions, OAuth tokens, refresh tokens, mobile app sessions) is easy to underestimate under pressure, and a missed session type can leave attackers with persistent access after containment.

BACK-CHANNEL LOGOUT: A CRITICAL MISSING COMPONENT

An important feature missing from many identity platforms is back-channel logout  support. Back-channel logout allows an identity provider (IdP) to notify all connected service providers (SPs) when a user logs out, ensuring that all active sessions are terminated across the ecosystem. This capability is crucial for mitigating the risks of authorization sprawl, as it prevents attackers from maintaining access through lingering sessions after a user logs out.

Today, few identity providers support back-channel logout, largely due to a lack of integration with application service providers. When application service providers do provide IdP logout support, it is often a proprietary implementation that only works with specific IdPs, creating an NxM integration problem (where N is the number of supported service providers and M is the number of supported identity providers). This fragmentation makes it impractical for organizations to achieve comprehensive session termination across all applications.

Support for invalidating sessions for all service providers through the IdP should be a stated requirement in vendor Requests for Proposals (RFPs) and procurement documents, as well as for any integrated application service providers. Mandating compliance with the draft Internet Engineering Task Force (IETF) standard Global Token Revocation  will help drive industry adoption of this important security feature to better respond to authorization sprawl attacks.

EVIDENCE COLLECTION DURING CONTAINMENT

During containment activities, we also collect evidence to support subsequent investigation, eradication, and recovery efforts. After isolating affected systems, we can collect evidence to understand attacker tactics, techniques, and procedures (TTPs), identify persistence mechanisms, and reconstruct the timeline of compromise.

In this section, we’ll explore objectives for data collection that support the organization’s needs for a valuable response effort.

EVERY STEP IS FOR DATA COLLECTION

In the PICERL and NIST SP 800-61 models, the containment step is when the incident response team first lays hands on the affected systems to isolate them, giving us the first chance to collect data. As a result, most guides and playbooks focus heavily on data collection during the containment phase, where analysts can collect volatile data and preserve evidence.

In the DAIR model, this logic still applies. We isolate the affected systems to prevent further damage and to gain as close to unfettered access to the compromised system as possible. However, we also recognize that every step of the incident response process is an opportunity to collect data. Each waypoint in the DAIR model serves as both a response action and a data collection opportunity. Your collection strategy should adapt to the specific goals and constraints of each phase.

• Prepare: Collect baseline configurations, network topologies, and asset inventories. Document communication plans and escalation procedures. This foundational data enables effective comparison when incidents occur.

• Identify: Gather initial event data, including logs, alerts, and user reports. Focus on establishing timeline markers and impact scope. Network analysts should prioritize flow data and DNS queries. Host analysts need process execution and local logging data.

• Verify/Triage: Collect evidence to confirm incident validity and assess risk impact. Decision makers need executive-level summaries with clear risk classifications. Technical teams require detailed indicators to support verification activities.

• Scope: Expand data collection to understand incident breadth. Analysts need lateral movement indicators, affected system inventories, and compromise timelines.

• Contain: Collect volatile data including memory captures, active network connections, and running processes. Consider full disk capture (if beneficial for your organization), local logging data, registry details, and other system configuration data. Collect adversary behavior data while maintaining operational security, where possible. Preserve evidence of attacker tactics for eradication and recovery analysis.

• Eradicate: Focus on collecting data about attacker persistence mechanisms and tools.

• Recover: Collect vulnerability assessment data, patch deployment logs, and control implementation verification. Document root cause analysis findings and remediation effectiveness metrics.

The DAIR model’s iterative nature means data collected in one phase directly informs activities in Eradication findings often expose additional preparation needs. Recovery analysis feeds back into improved detection capabilities. This interconnected approach ensures that each data collection effort contributes to both immediate response effectiveness and long-term security improvements, creating a comprehensive intelligence picture that evolves throughout the incident lifecycle.

Prioritized Collection

Evidence collection during containment requires prioritization based on volatility and investigative value to ensure critical information is preserved before containment actions modify system state or destroy transient data. Volatile data, including memory dumps, active network connections, and running processes, deserves the highest priority because this information disappears when systems are powered down or rebooted, or through natural attrition over time.

Volatile Data Collection

Memory analysis can reveal running malware, decrypted credentials in process memory, and active network connections that might not appear in logs. Capture memory from compromised systems before implementing containment actions that would alter the system state or power cycle the machine. For example, memory acquisition tools like WinPMEM or Linux Memory Extractor (LiME) can acquire a memory dump from the compromised web server before isolating it to a quarantine VLAN, preserving evidence of the web shell’s in-memory configuration and active command-and-control sessions that won’t survive a network disconnect.

PRIORITIZED COLLECTION: AN ORGANIZATIONAL-SPECIFIC APPROACH

In the DAIR model, we advocate for a two-step approach to evidence collection during containment: isolate first, then collect data. This is based on many years of collective experience, where data collected prior to containment may be incomplete or misleading due to attacker interference, and where containment actions themselves can destroy critical evidence if not managed carefully, or may trigger an attacker response in advance of containment activities. However, the specific prioritization of evidence collection should be tailored to the organization’s unique environment, threat landscape, and investigative goals. Organizations should weigh the loss of possible evidence due to containment actions versus the risk of allowing attackers to maintain access while evidence is collected.

Consider, for example, the output of Get-NetTCPConnection on a compromised Windows host, shown in Listing 52 . This command will show active and listening TCP connections, including those established by attacker tools.

Listing 52 | NetTCPConnection Output on Compromised Host
PS C:\> Get-NetTCPConnection
LocalAddress     LocalPort RemoteAddress    RemotePort State

------------     --------- -------------    ---------- ----- ::               445       ::               0          Listen 192.168.171.142  33318     151.101.118.172  80         TimeWait 192.168.171.142  33179     13.107.5.91      443        TimeWait 192.168.171.142  33174     172.183.7.192    443        Established 192.168.171.142  27288     192.168.1.140    4444       Established 192.168.171.142  1565      162.159.142.9    80         Established As an investigative tool, Get-NetTCPConnection provides valuable insight into ongoing attacker communications. However, if the incident response team immediately isolates the host from the network, these active connections will be terminated and the evidence of ongoing communications will be lost if not captured through an external data source (such as Network Flow logs, Sysmon network connection event logs, or other Network Detection and Response tools). Organizations should evaluate their specific environment to determine which evidence sources are most critical to preserve during containment, and weigh the risks of losing volatile data against the need to quickly isolate compromised systems. Organizations without alternate data sources for network connections or other volatile data may prioritize data collection before isolation, while those with robust logging and monitoring systems can prioritize isolating of systems to prevent further attacker activity.

Persistent and Log-Based Evidence

System artifacts, including registry hives, event logs, and temporary files, provide insight into attacker activities and persistence mechanisms with less time sensitivity than volatile data. These artifacts offer a more permanent record of compromise that can survive system restarts and most containment actions, though some data, such as certain cache files or temporary directories, may be cleared during normal system operations. Collect Windows registry hives to identify persistence mechanisms, event logs to establish timeline data, and browser cache to reveal attacker reconnaissance activities.  Prefetch files, ShimCache entries, and AmCache records provide execution history that helps reconstruct the use of the attacker’s tools even after the malicious files are deleted.

Network evidence, including packet captures, NetFlow data, and firewall logs, reveals communication patterns and data movement across the environment. This evidence helps analysts understand the scope of data exfiltration, identify command-and-control infrastructure, and discover additional compromised systems based on lateral movement patterns. Full packet captures provide the most detail but consume significant storage, while Network Flow logs (including NetFlow logs, VPC Flow Logs, and similar log types) In this section, we’ll cover the cloud security demarcation that determines which containment actions the customer controls; the core containment objectives specific to cloud environments; and techniques for identity-first containment, network isolation, resource tagging, IaaS termination protection, SaaS platform containment, and third-party integration containment.

Cloud Security Demarcation

Cloud service containment requires understanding the shared responsibility model that defines security boundaries between cloud service providers and customer organizations. For Infrastructure as a Service (IaaS) cloud services, providers typically manage infrastructure security, including physical hardware, hypervisor security, and network infrastructure protection, while customers remain responsible for identity and access management, data encryption, application security, and operating system patching. By contrast, Software as a Service (SaaS) providers manage nearly all infrastructure and application security, leaving customers responsible primarily for identity management, data access authorization, and user access controls. Platform as a Service (PaaS) offerings fall somewhere between the two, with providers managing the underlying platform security while customers handle application-level security and data protection. The division of responsibilities between what the cloud customer and what the cloud provider are responsible for is known as the cloud security demarcation . This separation of responsibilities determines which containment actions the cloud customer can implement directly and which require escalation to the cloud provider’s support teams.

For example, if attackers exploit a vulnerability in the underlying hypervisor or physical network infrastructure, the cloud customer likely cannot directly contain the threat and needs to engage the cloud provider’s security team, while compromised Identity and Access Management (IAM) credentials or misconfigured user account access are within the cloud customer’s containment authority. Understanding this demarcation before incidents occur enables faster, more effective containment by clarifying which team controls each potential containment mechanism. A summary of common cloud security demarcation responsibilities is shown in Figure 82.

Figure 82 | Cloud Security Demarcation Responsibility Summary

CLOUD SERVICE AND RESPONSIBILITY DEFINITIONS

All cloud providers operate under a shared responsibility model for security, in which the cloud provider is responsible for certain aspects, and the cloud customer is responsible for others. The line of responsibility between the provider and the customer can be complex, changing from provider to provider and within different products from the same provider.

Cloud services are often categorized as Infrastructure as a Service (IaaS), Platform as a Service (PaaS), and Software as a Service (SaaS). IaaS services are often the lowest-level cloud services, allowing customers to leverage cloud-provided storage, networking, and hardware to run Linux or Windows systems. Comparatively, PaaS enables the cloud customer to focus on the application, content, and data while the cloud provider manages the underlying operating system and often the services to support the application (databases, web servers). SaaS services focus on the upper-layer application functionality and data, such as Microsoft 365, Zoom, Slack, Salesforce, etc., where the cloud provider provides all other functionality.

Understanding the distinguishing characteristics of IaaS, PaaS, and SaaS is important for incident responders. Cloud security demarcation helps us differentiate our responsibility for incident response from the cloud provider’s. However, the broad service categories are not always sufficient to show where the customer’s responsibility ends for the service. Consider the AWS services for Elastic Compute Cloud (EC2) and Lightsail. EC2 allows users to provision servers running a given Amazon Machine Image (AMI), then add the services and applications to power the desired functionality. In this case, Amazon’s security responsibility ends with the hardware, storage, and network equipment. The cloud user’s responsibility starts with the Linux or Windows operating system. Compared to other services, Lightsail allows customers to launch similar VMs by selecting a blueprint such as WordPress, Node.js, Drupal, and more options. While Lightsail might seem to match the functionality of a SaaS platform, where the blueprint provides the necessary software, Amazon takes no responsibility for the security of the operating system, applications, services, or data. This can be non-intuitive for cloud customers, leading to instances being deployed and populated with data, left unmaintained, exposing the platform to vulnerabilities due to a lack of patch management and monitoring. Fundamentally, it’s important to understand where the security demarcation lies for the products used by your cloud provider. Begin by enumerating the cloud functions you use and reviewing the security documentation for these products to understand where your security responsibilities begin. Do not rely on broad IaaS, PaaS, or SaaS labels to determine security responsibility. Verify the security demarcation for each specific product, as services that appear to offer managed functionality may still leave full operating system and application responsibility with the customer.

Cloud Containment Objectives

The core containment objectives for cloud systems mirror traditional incident response goals: isolate the immediately to prevent their use for API calls or console access; terminate active user sessions across all applications; revoke OAuth refresh tokens that could generate new access tokens; and rotate service principal credentials used by automated systems. Consider the operational impact of identity-based containment on downstream automation and business processes that depend on the affected credentials. For example, when rotating a compromised service account key that authenticates a critical data processing pipeline, coordinate with application teams to update the credential in all systems that use it, implement the rotation during a maintenance window if possible, and have rollback procedures ready in case the credential update causes unexpected failures. Document which applications and automation workflows use each privileged identity before incidents occur, enabling rapid assessment of containment impact when those identities are compromised.

Network Isolation Containment

Network isolation in cloud IaaS environments is implemented through multiple complementary controls that prevent further compromise while preserving evidence for investigation. Remove compromised instances from production scaling groups and load balancers to prevent them from receiving user traffic while keeping the instances running for forensic analysis.  Modify security group rules, network Access Control Lists (ACLs), or move the instance to a pre-configured isolation Virtual Private Cloud (VPC) dedicated to incident response activities, where the team controls all network ingress and egress. Enable termination protection and deletion protection on compromised resources to prevent accidental or malicious destruction by other administrators who might not be aware of the ongoing investigation. Consider using cloud provider snapshot features to create point-in-time copies of storage volumes and virtual machine states. These features make it straightforward to preserve the compromised system’s exact configuration for detailed forensic analysis while the team continues containment activities. Always consider the cost-benefit analysis of snapshot storage costs versus the investigative value of preserving the system state, especially for large-scale incidents involving many compromised resources.

Resource Tagging for Containment Visibility

Cloud platforms provide robust resource tagging capabilities that facilitate clear identification of compromised assets during containment and throughout the investigation lifecycle. These metadata tags serve multiple purposes: they clearly mark resources as under investigation to prevent accidental modification or deletion, enable automated policy enforcement through tag-based access controls, and provide audit trails for compliance and post-incident review.

Establish consistent tagging conventions before incidents occur to ensure all team members apply tags uniformly during high-pressure containment activities. Common tagging schemes group into four broad categories, shown in Table 19. Multiple tags can be applied to a single resource to provide comprehensive context, and tags can be updated as the incident progresses through different phases.

Table 19 | Incident Response Tagging Schemes
CATEGORY PURPOSE EXAMPLE TAG
Status indicator Mark resource as under IR control Status:Quarantined
Case identifier Link resource to incident ticket IR-Case:2026-001
CATEGORY PURPOSE EXAMPLE TAG
Containment date Record containment timestamp for
audit review
ContainedDate:2025-10-27

Analyst owner Identify responsible IRT staff member IR-Owner:jsmith@company.com Resource tags enable practical operational benefits during containment activities. Use tags to create filtered views in cloud consoles that show only compromised resources; configure automated alerts when tagged resources are accessed or modified; implement tag-based access controls that restrict who can start or terminate quarantined instances; and generate reports for management on containment status across the environment. Some organizations implement automation that prevents deletion of resources tagged with incident response markers until the case is formally closed and documented. For example, when containing a suspected compromised EC2 instance in AWS, apply multiple resource tags to provide comprehensive tracking, as shown in Table 20. Configure AWS Resource Groups to dynamically collect all resources tagged with Status:UnderInvestigation, providing a single dashboard view of all contained assets across the AWS environment. Implement IAM policies that prevent anyone except incident responders from terminating instances tagged with Status:UnderInvestigation, protecting evidence from accidental destruction during investigation.

Table 20 | Example Tag Set for a Contained EC2 Instance
TAG PURPOSE
Status:UnderInvestigation Indicate active IR activities
IR-Case:2026-001 Link to ticketing system
ContainedBy:security-team Identify responsible team
ContainedDate:2025-10-27 Support timeline reconstruction
EvidencePreserved:Yes Confirm snapshots captured
Cloud provider tagging capabilities extend beyond compute instances to storage volumes, network
interfaces, load balancers, and even snapshots themselves, enabling comprehensive tracking of all resources
related to an incident. Apply consistent tags to snapshots created during containment to link them back to
the original incident case number and establish a clear chain of custody for forensic evidence. Tag network
security groups or firewall rules created specifically for containment purposes with descriptive labels like

IR-Purpose:Quarantine and IR-Case:2026-001, facilitating cleanup after incident resolution and preventing these temporary configurations from lingering indefinitely in production environments. Tagging is only effective as a containment signal when the organization controls who can change the tags. An attacker who retains cloud console access can simply remove the Status:UnderInvestigation tag to hide a compromised resource from IR dashboards, or apply, modify, or remove incident response tags, and implement that RACI as an IAM policy that restricts write access to those specific tag keys to incident response roles only. Configure tag change event logging to record to a separate, tamper-resistant audit destination so that unauthorized modifications are visible even if the attacker suppresses logging elsewhere.

IaaS Termination Protection

Enabling termination protection on contained IaaS cloud resources prevents accidental deletion of critical evidence during investigation, creating a safety mechanism that requires explicit two-step confirmation before anyone can destroy potentially valuable forensic data. Cloud administrators and automation systems often have the ability to terminate instances as part of routine operations, creating a risk that someone unfamiliar with the ongoing investigation might delete a contained system, thinking it’s simply unused or misconfigured. Termination protection is a technical control that enforces evidence preservation via the cloud provider’s API, requiring authorized personnel to first disable protection before terminating the resource.

For example, when a compromised EC2 instance in AWS is detected, enable termination protection immediately via the AWS console or CLI to prevent any user or automation from deleting the instance until protection is explicitly removed, as shown in Listing 53. This protection persists even if someone has IAM permissions that would normally allow instance termination, providing defense against both accidental deletion by administrators and intentional deletion by attackers who might have compromised cloud credentials. Azure provides similar capabilities through deletion locks that prevent resource deletion until the lock is removed, while Google Cloud Platform offers Compute Engine instance deletion protection that can be enabled during containment operations.

Listing 53 | AWS CLI Command to Enable Termination Protection
$ aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --disable-api-termination
1 Replace i-1234567890abcdef0 with the EC2 instance ID.

Table 21  provides equivalent commands for enabling termination or deletion protection across cloud providers.

Table 21 | Cloud Termination Protection Quick Reference
Enable deletion protection
AWS aws ec2 modify-instance-attribute --instance-id <instance-id> --disable-api-termination

Azure az lock create --name IR-Preserve --lock-type CanNotDelete --resource-group <rg> --resource-name <vm> --resource-type Microsoft.Compute/virtualMachines GCP gcloud compute instances update <instance> --deletion-protection --zone <zone> Verify protection status AWS aws ec2 describe-instance-attribute --instance-id <instance-id> --attribute disableApiTermination Azure az lock list --resource-group <rg> --resource-name <vm> --resource-type

Microsoft.Compute/virtualMachines

GCP gcloud compute instances describe <instance> --zone <zone> --format="value(deletionProtection)" Termination protection extends beyond compute instances to other critical resources, including Elastic Block Storage (EBS) volumes, snapshots, databases, and network configurations that contain evidence or support ongoing investigation. Apply protection to EBS volumes attached to contained instances to prevent their deletion even if the instance itself is somehow terminated, and enable snapshot protection to preserve exact copies of compromised systems throughout the investigation. Document which resources have termination protection enabled in incident tracking systems, establishing clear procedures for removing protection only after formal evidence preservation is complete and legal hold requirements are satisfied. When IT or application stakeholders insist on terminating a compromised instance before the investigation is complete, a clone-then-terminate pattern preserves most of the evidence without blocking their request. A GuardDuty-triggered (or equivalent) Lambda function can clone the affected instance, including its attached storage, into a separate forensic AWS account that only the incident response team can access, producing a full-fidelity copy of disk state for later analysis. Network-connected processes and volatile memory content are lost during the clone, so the IRT should still perform RAM collection on the original instance before allowing termination, but persistent artifacts such as filesystem contents, event logs, and installed binaries remain available in the cloned copy. This pattern works equally well in Azure (using Event Grid and Azure Functions to snapshot managed disks into a forensic subscription) and Google Cloud (using Eventarc or Pub/Sub triggers to clone persistent disks into a separate project).

SaaS Platform Containment

SaaS platform containment differs fundamentally from IaaS containment because organizations lack direct access to the underlying systems and can only leverage containment capabilities exposed by the SaaS provider through its administrative interfaces. While IaaS environments grant organizations control over virtual machines, network configurations, and security groups, enabling teams to implement custom containment measures, SaaS platforms provide only the containment features built into their administrative consoles and APIs. This limitation requires adapting containment strategies to work within provider-defined boundaries, often accepting less granular control than organizations would have in self-managed infrastructure.

Identity and session containment take the highest priority in SaaS environments, where organizations cannot directly access or isolate the underlying infrastructure. Reset passwords for compromised user accounts immediately to invalidate current credentials, or set temporary random passwords that prevent both attackers and legitimate users from accessing the account until the team completes the investigation. Revoke all active sessions and refresh tokens to force re-authentication, ensuring that password resets actually terminate attacker access rather than leaving active sessions that survive credential changes. For service principals and application accounts, rotate API keys, client secrets, and OAuth credentials that authenticate automated integrations and workflows.

Consider whether to disable accounts entirely or use platform-specific freeze features that preserve data while blocking sign-in, choosing based on whether the team needs to maintain access to the account’s data 365 administrator account, immediately reset the password through the Microsoft 365 admin center, use the revoke sessions feature to invalidate all active authentication tokens forcing the user to re-authenticate everywhere, disable the account to prevent any sign-in attempts, and rotate the credentials for any service principals or application registrations that the administrator may have created, documenting each action with timestamps for incident timeline reconstruction.

Third-Party Integration Containment

Integration and automation containment prevent compromised accounts from maintaining persistent access through third-party applications and automated workflows that often survive credential resets. Disable third-party applications that the compromised account authorized, including OAuth-connected apps, browser extensions, and mobile applications that maintain their own authentication tokens. Review and disable automation rules in platforms that could exfiltrate data or perform unauthorized actions using the compromised account’s permissions.  Revoke outgoing webhooks that may send sensitive data to attacker-controlled endpoints, disable Continuous Integration/Continuous Deployment (CI/CD) deployment keys that could allow code injection into production systems, and invalidate API tokens used to authenticate programmatic access to the SaaS platform.

After containment, replace integration credentials with new secrets and re-authorize only legitimate integrations after verifying their configuration. For example, when investigating a compromised Slack workspace administrator account, audit the workspace’s installed apps and custom integrations, and disable any unfamiliar OAuth applications (especially those requesting broad permissions, such as read all messages or access all channels ). Remove webhook configurations that send data to external URLs not expressly authorized by the organization. Revoke any API tokens created by the compromised account, and review bot users for unauthorized automation that might persist after the human account is disabled.

WHEN LEGITIMATE APPS LOOK LIKE COMPROMISE

The Counter Hack team and I were working on a Microsoft 365 security assessment when one of the analysts discovered an application with broad permissions: read and send mail, access all calendar events, and read files across SharePoint sites. When we asked, no one on the security team recognized the application. It looked like an illicit consent grant  attack, where an attacker tricks a user into authorizing a malicious application with excessive permissions. [5] Our security assessment quickly transitioned into an incident response investigation.

After investigation, the application in question turned out to be a Customer Relationship Management (CRM) tool feature added by the sales team several months earlier. A salesperson clicked through the OAuth consent prompt without reading the permissions, and the application had been quietly syncing sensitive account data ever since. Not necessarily malicious, but definitely a risk and a concern for my customer’s security team.

Figure 83 | Entra ID Application Consent Grant

Figure 84 | Entra ID Enterprise Application Configured Permissions

Listing 54 | Entra ID OAuth Consent Grant Enumeration
Get-MgOauth2PermissionGrant -All | ForEach-Object {
$sp = Get-MgServicePrincipal -ServicePrincipalId $_.ClientId
[PSCustomObject]@{
App=$sp.DisplayName;
Scopes=$_.Scope;
ConsentType=$_.ConsentType
}
}

During containment, compare discovered app permissions against this inventory to quickly distinguish legitimate integrations from unauthorized access by attackers. This enumeration step can save significant time during an investigation.

CONTAINMENT CHALLENGES

Modern environments present unique containment challenges that require adapting traditional isolation techniques to new technologies, architectural patterns, and operational models. In this section, we’ll examine four areas where traditional containment approaches fall short: cloud and hybrid environments, encrypted communications that limit inspection, remote-worker environments beyond the corporate perimeter, and modern attack vectors that extend beyond traditional host compromise.

Cloud and Hybrid Environments

Cloud infrastructure requires fundamentally different containment approaches that leverage cloud-native controls and account for the ephemeral nature of cloud resources, where traditional network-based isolation may be impossible or ineffective.

API-Based Isolation

API-based isolation using cloud provider APIs to modify security groups, network ACLs, or IAM policies provides rapid, programmatic containment that can be automated and applied at scale.  Use AWS Security Groups to block all inbound and outbound traffic to a compromised EC2 instance, Azure Network Security Groups (NSGs) to quarantine virtual machines, or Google Cloud Platform (GCP) firewall rules to isolate compute instances. This approach enables containment through infrastructure-as-code tools like Terraform or CloudFormation, allowing teams to version control containment procedures and execute them consistently across hundreds of cloud resources. For example, use the Azure CLI to create a quarantine NSG and attach it to a compromised virtual machine’s network interface, denying all traffic except SSH access from a specific jump box IP address. This quarantines the instance while maintaining incident response access for investigation, as shown in Listing 55.

Listing 55 | Azure CLI Command Example for Network Isolation Containment
$ az vm show --name web-prod-01 -g rg-production-eastus2 --query "networkProfile.networkInterfaces[0].id" -o tsv 1
/subscriptions/e7b3c1d9-a842-4f56-b6d1-8a3e5f902c4d/resourceGroups/rg-production-eastus2/providers/Microsoft.Network/networkInterfaces/web-prod-01-nic
$ az network nsg create --name IR-Quarantine-2025-042 -g rg-production-eastus2 -o none 2
$ az network nsg rule create --nsg-name IR-Quarantine-2025-042 -g rg-production-eastus2 --name

AllowSSH-IR --priority 100 --direction Inbound --access Allow --protocol Tcp --destination-port -ranges 22 --source-address-prefixes 198.51.100.10/32 -o none 3 $ az network nsg rule create --nsg-name IR-Quarantine-2025-042 -g rg-production-eastus2 --name DenyAllOutbound --priority 100 --direction Outbound --access Deny --protocol '*' --destination -port-ranges '*' --source-address-prefixes '*' --destination-address-prefixes '*' -o none 4 $ az network nic update --name web-prod-01-nic -g rg-production-eastus2 --network-security-group IR-Quarantine-2025-042 -o none 5

1 Identify the network interface attached to the compromised virtual machine.

2 Create a quarantine NSG in the same resource group as the compromised VM.

3 Allow inbound SSH access only from the incident response team’s jump box IP address (priority 100 overrides the default DenyAllInBound rule).

4 Deny all outbound traffic, overriding the NSG’s default AllowInternetOutBound rule to isolate the instance.

5 Attach the quarantine NSG to the compromised VM’s network interface, replacing any existing NSG association. Instead, disable event triggers that invoke the compromised function where possible. Preserve the serverless function’s code, replacing it with code that returns an access denied response and logs access attempts for further data collection. We include a Node.js example for AWS Lambda in Listing 56  and example deployment instructions in Listing 57.

Listing 56 | JavaScript Function for AWS Lambda that Denies Access and Logs Attempts
exports.handler = async (event) => {
// Log the entire event for analysis
console.log('Lambda function invoked - logging request and rejecting');
console.log('Event details:', JSON.stringify(event, null, 2));
// Return 403 Forbidden response
const response = {
status: '403',
statusDescription: 'Forbidden',
headers: {
'content-type': [{
key: 'Content-Type',
value: 'text/html'
}]
},
body: 'Access Denied - Function in containment mode'
};
return response;
};

Listing 57 | Configure AWS Serverless Function
% head -4 index.js
exports.handler = async (event) ⇒ {
// Log the entire event for analysis
console.log('Lambda function invoked - logging request and rejecting');
console.log('Event details:', JSON.stringify(event, null, 2));
% zip function.zip index.js 1
adding: index.js (deflated 45%)
% aws --profile jwright lambda update-function-code --function-name lambda-function-to-log-and-disable --zip-file fileb://function.zip 2
1 Compress the deny-and-log function code into a ZIP file for deployment.
2 Update the AWS Lambda function code to replace the specified function with the deny-and-log implementation.

The same deny-and-log containment pattern applies to Azure Functions and Google Cloud Functions. For Azure Functions, update the function code using az functionapp deployment source config-zip  and monitor contained invocations through Application Insights. For Google Cloud Functions, deploy replacement code with gcloud functions deploy  and monitor invocations through Cloud Logging.

Multi-Cloud Coordination

Multi-cloud coordination becomes critical when incidents span multiple cloud providers with different containment capabilities, API interfaces, and security models. Each cloud provider offers distinct isolation mechanisms with varying capabilities, where AWS security groups operate differently from Azure NSGs or GCP firewall rules, requiring incident responders to understand the differences and adapt containment strategies to platform-specific features.

Hybrid and multi-cloud incidents often exceed the capacity of the standing incident response team, both in headcount and in platform-specific expertise. Cloud administrators already hold the tooling access, IAM permissions, and operational familiarity needed to execute containment actions quickly, and should be pulled into the incident response structure as co-opted IRT members rather than treated as an external team receiving tickets. Capture this co-option pathway during the prepare activity, including on-call rotations, authorization scope, and the communication channels cloud administrators will use while operating under IR direction.

Table 22 | Multi-Cloud Containment Quick Reference
CONTAINMENT

ACTION

AWS AZURE GCP

Network

Isolation

Security Groups,

Network ACLs

Network Security Groups (NSGs)

VPC Firewall Rules

Identity

Containment

IAM policy modification, access key disabling Entra ID account disabling, conditional access Cloud IAM policy binding removal Snapshot/Eviden ce Preservation EBS snapshots, AMI creation Managed disk snapshots, VM capture
