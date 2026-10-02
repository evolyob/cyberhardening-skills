# Chapter 12-1: Containment: Response Strategy, Active/Passive Decisions & Timeline Coordination

> Modular Sub-Chapter | Source: DAIR-IR Framework

---

# Chapter 12: Contain Activity: Isolation & Network Segmentation

The extended activity search revealed that the service principal had been accessed from the external IP address as early as October 8th, more than a week before the first management operations Priya had initially identified. The role assignment query confirmed that the attacker had granted the service principal Contributor access to a second resource group, rg-analytics-eastus2, expanding the potential scope of compromise beyond the production environment.

Priya compiled a summary of her scoping findings for the incident commander, including the confirmed timeline of attacker activity, the scope of compromised resources across both resource groups, an assessment of the volume and sensitivity of exfiltrated data, and recommended next steps for containment. This summary provided leadership with the context needed to make informed decisions about notification obligations, containment priorities, and resource allocation as the investigation continued.

SCOPE: STEP-BY-STEP

The following steps provide a condensed reference for scoping activities. Each step corresponds to topics covered earlier in this chapter, organized for use when determining the full extent of compromise across the environment.

Step 1. Identify Indicators of Compromise from Detection and Verification

Categorize the IOCs handed off from verify and triage into the canonical inventory used for sweeps. Representative IOC categories include:

• File-based indicators (hashes, filenames, file paths).

• Network indicators (IP addresses, domains, URLs, signatures).

• Process and service indicators (process names, command-line arguments).

• Registry and configuration indicators (registry keys, configuration changes).

• Account-based indicators (unauthorized accounts, suspicious usage patterns).

• Behavioral indicators (temporal patterns, data movement, lateral movement).

Step 2. Conduct Enterprise-Wide Hunting for Identified IOCs

This is the IOC-driven sweep during a verified incident, distinct from the standing hypothesis-driven hunting program owned by detect. Representative activities include:

• Search centralized log analysis tools (SIEM, log aggregation systems).

• Leverage EDR platforms to search across managed endpoints.

• When EDR is not available, use inventory management tools, active scanning, network scans, or custom scripts to probe for IOCs.

• Apply threat-hunting platforms that combine endpoint, network, and logging data to provide overlapping analysis coverage.

Step 3. Apply Progressive Scoping Methodology

Representative activities include:

• Prioritize critical assets (domain controllers, file servers, databases, systems with sensitive data).

• Expand laterally to systems connected to known-compromised hosts.

• Conduct an environmental sweep across all systems.

Step 4. Reconstruct the Attack Timeline

Scope owns the canonical attack-progression timeline; subsequent activities annotate it (eradicate adds eradication-sequencing markers; debrief consolidates into the final narrative). Representative activities include:

• Identify the initial compromise and the patient zero system.

• Map lateral movement through authentication logs and file access patterns.

• Identify the persistence mechanism deployment timeline.

• Determine when sensitive data was accessed or exfiltrated.

Step 5. Document Scoping Findings

Representative activities include:

• List all compromised systems identified.

• Record IOCs discovered during scoping.

• Create a timeline visualization of the attack’s progression.

• Note any visibility gaps or systems requiring additional investigation.

Step 6. Address Scoping Challenges

Representative activities include:

• Identify and document visibility gaps (unmanaged systems, limited logging, IoT, and ICS devices).

• For systems with limited logging, use alternative evidence sources such as network flow data and authentication logs from connected systems.

• For ICS and industrial devices without centralized logging (for example, programmable logic controllers), rely on network flow data as the primary source of evidence.

• Watch for anti-forensic techniques (log deletion, timestomping, encryption and obfuscation, living off the land).

• Use counter-strategies, including log manipulation detection, alternative timestamp sources, behavioral analysis, and command-line argument review.

• Apply cloud-specific scoping tools and techniques for cloud and hybrid environments, including cloud provider audit logs and container runtime security.

• Scope cloud environments quickly. Ephemeral resources can deallocate and take evidence with them if scoping is delayed.

• Manage scale and complexity through prioritization and automation.

• Document false positive sources for future reference.

Step 7. Prepare Scoping Results for Containment, Eradication, and Recovery

Hand off the scoped system list, the canonical IOC inventory (Step 1), and the attack-progression timeline (Step 4) so each downstream activity can build on settled artifacts rather than re-derive them.

12 Contain Activity

The containment activity represents an inflection point in incident response, where teams transition from scoping the incident’s breadth to taking decisive action against the threat. Containment serves dual purposes: stopping the attacker from causing additional harm while preserving evidence for investigation. This balance between aggressive action and careful preservation of evidence requires both technical sophistication and strategic thinking.

Figure 74 | Contain Activity Waypoint

This chapter explores the objectives of containment, implementation strategies, timing considerations, and technical methods for effective containment in modern environments. We will also examine the challenges unique to cloud, remote work, and encrypted communications to provide guidance on developing effective containment approaches for these environments. The chapter also addresses the importance of validating containment success and documenting actions taken throughout the process.

CONTAINMENT OBJECTIVES

Containment encompasses two primary objectives: stopping attacker activity and collecting evidence. In this section, we’ll explore each objective in detail to understand its importance and implementation considerations.

Stopping Attacker Activity

The first objective of containment is to prevent the attacker from continuing malicious activities. In the past, this meant unplugging affected systems from the network, an approach that is no longer practical for many organizations with disparate and distributed systems. Modern containment strategies require more sophisticated approaches that balance security needs with operational requirements. This includes techniques such as network isolation, account restrictions, and process termination. Network isolation uses technologies such as private VLANs, access control lists, cloud security groups, and software-defined networking to restrict the movement of attackers without completely disrupting business operations. Rather than disconnecting systems entirely, responders can sever specific communication paths while maintaining critical business functions. For example, isolating a compromised web server from internal systems while maintaining its internet-facing services allows containment without complete service disruption.

Account restrictions disable or limit access to compromised accounts, ideally without alerting the attacker to defensive measures. This can include changing account passwords, revoking privileges, or implementing conditional access policies that limit access while maintaining the appearance of normal operations. Organizations should coordinate credential resets carefully to avoid triggering attacker awareness while still achieving effective containment.

Process termination stops identified malicious processes, though this action should also be executed carefully to avoid tipping off sophisticated attackers who may have monitoring capabilities in place. Advanced adversaries may implement watchdog processes that respawn terminated malware, and human-operated ransomware groups have been observed accelerating encryption timelines when they detect defensive actions, making subtle containment approaches preferable to aggressive process killing in many scenarios.

Aggressive containment actions can backfire. Human-operated ransomware groups have been observed accelerating encryption timelines when they detect defensive actions, and watchdog processes can respawn terminated malware or trigger destructive payloads. Consider subtle, coordinated containment approaches before killing processes on systems where adversary behavior is not yet fully understood.

Evidence Collection and Preservation

The second objective ensures that critical evidence is captured before it disappears or becomes corrupted. This evidence is subsequently used to gain further insight into the attacker’s tactics, techniques, and procedures (TTPs) during the eradicate activity, to help responders understand the attack, and potentially connections, and other artifacts critical for understanding attacker activities.  Tools like WinPMEM (and the companion Linux memory acquisition tool Linpmem) enable rapid memory capture with minimal system impact, allowing analysts to preserve evidence while maintaining system availability. Forensic imaging of affected systems preserves the complete state for detailed analysis. While full disk imaging has become less common due to storage costs and time constraints, selective imaging of critical systems or specific directories remains valuable for detailed investigation. Organizations can focus imaging efforts on systems that contain unique evidence, such as the initial point of compromise or systems where attackers deployed custom tools.

Log preservation ensures that evidence of attacker activity isn’t lost to rotation or deletion. This includes not only security logs but also application logs, authentication records, and network flow data that might reveal attack patterns. Forward logs to a centralized, secure location immediately upon discovering a compromise to prevent attackers from deleting or modifying local log files to cover their tracks.

CONTAINMENT STRATEGIES

Now that we’ve established the objectives of containment, we can explore various implementation strategies.

Organizations should choose containment strategies appropriate to their specific incident, balancing effectiveness with operational impact and the level of attacker awareness. In this section, we’ll explore passive, active, and adaptive containment strategies, and how organizations can transition between them based on evolving threat intelligence and operational needs.

Figure 75 | Containment Strategy Evolution

TERMINATE OR MONITOR: ORGANIZATIONAL CONSIDERATIONS

Organizations face an important decision during the contain activity: immediately terminate the attacker’s access or continue monitoring to gather intelligence. This choice carries significant implications for both incident outcomes and organizational risk posture. Immediate termination offers the clearest benefit of stopping ongoing damage. Attackers can no longer exfiltrate data, deploy ransomware, or establish additional persistence mechanisms. However, premature action may alert sophisticated threat actors who then accelerate their timeline, triggering rapid data destruction or immediate ransomware deployment before responders can implement comprehensive containment.

Continued monitoring provides valuable intelligence about attacker objectives, techniques, and the full scope of compromise. Organizations can identify all affected systems, understand data targeting patterns, and prepare thorough remediation strategies. This approach becomes particularly critical during ransomware negotiations, where isolating the attacker’s access to a subset of systems could prompt immediate encryption or higher payment demands.

The decision ultimately depends on organizational risk tolerance, operational constraints, and incident specifics. High-value targets, safety-critical systems, and regulated environments typically require immediate protection regardless of intelligence gathering opportunities. Conversely, organizations with robust backup strategies and strong forensic capabilities may choose to extend monitoring to develop a comprehensive understanding of threats before taking action. Choosing between passive, active, and adaptive containment under pressure benefits from pre-agreed criteria rather than judgment made in the moment. Table 16 lists common factors and which strategy each one favors. Analysts can scan the table during an incident (or one like it customized to the organization’s needs) to identify which factors apply and where the weight of evidence points.

Table 16 | Factors Influencing Containment Strategy Selection
FACTOR PASSIVE ADAPTIVE ACTIVE
Active data destruction or
ransomware underway
Required
Regulated data with compliance-driven timeline
Required
Safety-critical or high-availability
system at risk
Required
Attacker shows awareness of
defenders
Strongly favored
Short dwell time, limited monitoring
maturity
Strongly favored
Extended dwell time, mature
monitoring in place
Strongly favored
Unknown scope, uncertain attacker
sophistication
Preferred
Commodity malware on low-value
asset
Possible
Controlled deception environment
(honeypot, sandbox)
Passive Containment

Passive containment focuses on limiting damage without alerting the attacker to defensive actions, allowing organizations to gather intelligence while reducing risk. This approach works best when organizations have strong monitoring capabilities and can afford to accept some continued attacker presence in exchange for a better understanding of the threat.

When it is available to the incident response team, analysts can gain valuable insight by monitoring attacker tactics, techniques, and procedures before implementing containment actions. This insight can reveal additional compromised systems, help responders understand data targeting patterns, and inform comprehensive remediation strategies. For example, monitoring an attacker’s lateral movement attempts reveals which systems they consider high-value targets, informing both immediate containment priorities and long-term security improvements.

Honeypots and deception technologies divert attackers from real assets to decoy systems designed to appear valuable while actually containing no sensitive data. These controlled environments allow observation of attacker techniques while protecting production systems from damage. Organizations can deploy honeypots that closely mirror production systems to attract attacker attention, but mark them clearly in backend systems to distinguish legitimate alerts from deception-based detections. Passive containment is uncommon in modern incidents. Capable attackers detect defensive monitoring quickly and either accelerate their timeline or burn their access deliberately, reducing the intelligence window to a fraction of what strong-monitoring organizations hope for. Reserve this strategy for narrow scenarios such as commodity malware on low-value assets or controlled deception environments, and expect to transition to active containment at the first sign of attacker awareness.

Active Containment

Active containment takes decisive action to stop attacker activities, accepting that the attacker may become aware of defensive efforts and potentially accelerate their timeline. Organizations choose this approach when the risk of continued attacker access outweighs the intelligence value of observation, or when immediate triggers, such as active data destruction, demand an urgent response. Network segmentation isolates compromised segments from the rest of the network through multiple technical approaches. This might involve introducing firewall rules or access control lists that block traffic associated with attacker activity, activating pre-configured network segmentation policies to isolate systems, or physically disconnecting network segments when software controls prove insufficient. System isolation removes specific compromised systems from the network while maintaining forensic integrity and, where possible, management access for investigation.  Modern Endpoint Detection and Response (EDR) tools can isolate systems while maintaining forensic connections for investigation, allowing analysts to collect evidence, analyze running processes, and observe attacker behavior without granting attackers network access to other systems. Prefer EDR isolation features over network-based isolation controls when available, allowing responders to continue using EDR solutions to collect evidence while preventing attacker access.

Service disruption disables compromised services or applications to prevent further damage when other containment methods prove insufficient. This might include stopping web services that attackers are using to exfiltrate data, disabling remote access protocols such as Remote Desktop Protocol (RDP) or Secure Shell (SSH) that provide attacker entry points, or shutting down specific business applications that attackers have compromised. Organizations should coordinate service disruption with business stakeholders to understand operational impacts and identify alternative workflows during the containment period.

WHEN RMM TOOLS TURN AGAINST YOU: THE STRYKER COMPROMISE

Stryker is one of the world’s largest medical technology companies, producing devices and equipment used in hospitals and surgical settings worldwide. Based in Kalamazoo, Michigan, the company manufactures products ranging from joint replacement implants and surgical instruments to hospital beds and robotic-assisted surgery systems. With $25 billion in annual revenue and approximately 56,000 employees worldwide, a disruption to Stryker’s operations has far-reaching consequences for healthcare providers and patients.

In March 2026, attackers compromised Stryker’s Microsoft Intune environment, a Mobile Device Management (MDM) platform, and used it to remotely wipe devices across the organization, including laptops, phones, and other endpoints enrolled in the platform. [1] The attack was attributed to Handala, an Iran-linked group believed to be a front for Void Manticore, a threat actor sponsored by the Iranian government. Handala claimed to have wiped more than 200,000 servers, mobile devices, and other systems, forcing Stryker to shut down offices in seventy-nine countries. The impact was immediate and global. Staff reported that their personal devices were wiped, and they lost access to eSIMs, two-factor authentication, email, and collaboration tools. The company closed office facilities and posted notices instructing employees to stay off the network, avoid using computers, and disconnect from WiFi. For work phones, Stryker recommended that employees remove the device management profile entirely to prevent further damage from the compromised MDM platform.

Figure 76 | Stryker Facility Employee Notice

The disruption extended beyond IT systems into manufacturing operations. The attack destroyed critical software tools for product design and supply chain management, forcing a temporary halt to manufacturing. At Stryker’s Cork, Ireland, headquarters, over 4,000 employees lost network access, and modern factory systems that relied on the digital infrastructure saw regional manufacturing output slow.

This incident illustrates a containment challenge that organizations with remote management platforms should plan for: the same capabilities that enable rapid response can also become an attack vector. When attackers gain access to tools like Microsoft Intune, they can issue commands at scale, wiping devices, pushing malicious configurations, or revoking access across the entire fleet. Containment in these scenarios requires disconnecting from the very management infrastructure that responders would normally rely on to contain the threat. Organizations should plan for this possibility by establishing out-of-band communication channels and offline containment procedures that do not depend on device management infrastructure.

Adaptive Containment

Sophisticated incidents may require adaptive containment that evolves based on attacker behavior, adjusting response tactics as the incident unfolds and new intelligence emerges. This approach combines passive and active techniques, transitioning between them based on threat assessment and operational requirements.

Progressive restrictions gradually increase containment measures based on the actions of attackers, allowing organizations to gather intelligence in the early stages while maintaining the ability to escalate to aggressive containment when necessary. Starting with passive monitoring, teams can progressively implement more aggressive containment measures as they understand the threat scope and the attacker’s objectives. For example, analysts might begin by monitoring attacker lateral movement attempts to map target systems, then implement network restrictions that prevent access to high-value targets while preserving attacker access to lower-value decoy or honeypot systems that continue to provide intelligence. Deceptive containment makes the attacker believe they maintain access while actually operating in a controlled environment, providing the intelligence benefits of passive monitoring while reducing operational risk. This might involve redirecting attacker tools to honeypot systems that appear identical to production systems, providing false data that appears valuable but actually contains no sensitive information, or allowing access to sandboxed environments that prevent real damage.

TIMING AND COORDINATION

Containment timing impacts incident outcomes and business operations, requiring a careful balance between speed and comprehensiveness. Premature containment may alert attackers before responders fully understand the scope, triggering accelerated data destruction or ransomware deployment before teams can implement comprehensive protection. Delayed containment allows continued damage and potential data exfiltration, increasing the incident’s impact and the potential regulatory consequences. Organizations should establish clear decision criteria for timing containment based on threat indicators, business impact, and intelligence-gathering needs. In this section, we’ll examine immediate containment triggers and coordinated containment strategies for complex incident response efforts.

Immediate Containment Triggers

Certain scenarios demand immediate containment, regardless of incomplete understanding, where the risk of delayed action outweighs the value of additional intelligence gathering or comprehensive scoping.

Table 17 | Considerations for Immediate Containment
TRIGGER INDICATORS RECOMMENDED ACTION
Active Data
Destruction
Ransomware encryption spreading
across file shares, event log wiping,
database tables being dropped
Immediate isolation to stop ongoing
damage
Data Exfiltration Large transfers to cloud storage, bulk
database queries retrieving PII, file
archives sent to external sites
Urgent containment to limit exposure
scope and regulatory impact
Safety/Critical
Systems
Threats to ICS, medical devices,
payment processing, or other safety-critical infrastructure
Immediate action to prevent
operational disruption or physical harm
Regulatory
Requirements
Incidents involving data or services
covered by HIPAA, PCI DSS, GDPR,
NIS2, DORA, CRA, or similar
jurisdiction-specific frameworks
Rapid containment to minimize
affected records and meet compliance
timelines

The regulatory landscape is jurisdiction-specific, and the examples in Table 17 are illustrative rather than exhaustive. European organizations should also consider NIS2 and DORA for operators of essential services and financial entities, and the Cyber Resilience Act (CRA) for organizations that place products with digital elements on the EU market, along with sector-specific requirements such as the Revised Payment Services Directive (PSD2) and the UK Financial Conduct Authority’s operational resilience rules (PS21/3). Ideally, decision makers and organizational leadership decide which triggers apply during the prepare activity and maps each one to a specific response action. This allows the team to apply those policy decisions during the incident, referencing a pre-approved position rather than requiring fresh interpretation under pressure.

Active data destruction is the most urgent trigger, in which attackers are actively deleting or encrypting critical data, and leaving no time for intelligence gathering or coordinated response planning. When responders observe ransomware encryption spreading across file shares, attackers wiping event logs to cover their tracks, or database tables being dropped in real time, immediate containment may be the most reasonable action to best meet the organization’s needs. The speed of modern ransomware can encrypt thousands of files per minute, making every second of delay costly in terms of data loss and recovery effort. Ongoing data exfiltration of sensitive information to external locations demands urgent action, particularly when the data includes intellectual property, customer records, or regulated information that could result in significant financial or reputational damage. Monitor for large data transfers to cloud storage services, suspicious database queries that retrieve thousands of customer records, or the creation and transfer of file archives to external sites.

The volume and sensitivity of exfiltrated data will affect regulatory notification requirements, potential fines, and the organization’s reputation. For example, when observing a compromised service account executing database queries that have retrieved sensitive PII and establishing connections to a suspicious external IP address, organizations will likely transition to immediate containment actions, even if responders haven’t yet identified how the service account was initially compromised. Threats to critical operations or safety systems will also warrant immediate action to prevent operational disruption or physical harm that could affect services or employee safety. Industrial control systems, medical devices, payment processing infrastructure, and other safety-critical or business-critical systems can rarely tolerate extended compromise time while teams gather intelligence. The operational and safety consequences of delayed response in these environments may outweigh the investigative benefits of continued monitoring.

Regulatory requirements may mandate specific containment timeframes for certain incident types, overriding tactical considerations about optimal response timing. Healthcare data breaches under the Health Insurance Portability and Accountability Act (HIPAA), payment card compromises under the Payment Card Industry Data Security Standard (PCI DSS), and personal data incidents under the General Data Protection Regulation (GDPR) all carry specific notification timelines that effectively require rapid containment to minimize the scope of affected records and demonstrate reasonable response efforts. [2] Regulatory frameworks may also define breach severity based on the number of affected individuals and the duration of unauthorized access, creating direct financial incentives for rapid containment. For example, when discovering unauthorized access to a database containing Protected Health Information (PHI), organizations should implement immediate containment within hours rather than days to limit the compliance window and reduce the number of affected patient records requiring notification under HIPAA breach notification rules. Delays could expand both the legal exposure and the population requiring individual notification.

Coordinated Containment

Complex incidents affecting multiple systems require coordinated containment to prevent attackers from maintaining access through overlooked systems or pivoting to alternative infrastructure when they detect partial containment efforts.

Simultaneous Isolation

Simultaneous isolation of all known compromised systems prevents attackers from pivoting to maintain access through alternative pathways that remain available during otherwise sequential containment actions. When attackers have established a presence on multiple systems, isolating them one at a time alerts the adversary to defensive activities and provides an opportunity to accelerate their timeline, deploy additional persistence mechanisms, or trigger destructive payloads.

Coordinate timing and communication across technical teams to ensure comprehensive coverage where network, endpoint, and application teams all execute containment actions within a narrow time window. For example, when responding to a lateral movement incident in which attackers have compromised fifteen workstations across three departments, analysts may simultaneously enable EDR isolation on all affected systems while the network team implements VLAN restrictions and the identity team disables compromised accounts. This coordinated approach prevents attackers from detecting partial containment and moving to systems that remain accessible.

Isolating compromised systems one at a time is a common containment mistake. Sequential containment alerts the adversary and gives them time to escalate privileges, deploy additional persistence, or trigger destructive payloads on systems not yet contained.

Credential and Infrastructure Coordination

A credential reset is necessary across the entire environment when credential theft is identified. To be effective, the credential reset procedures should be coordinated to avoid creating windows in which attackers maintain access through credentials that have not yet been rotated. Domain-wide credential compromises require rotating passwords for all privileged accounts, service accounts, and potentially all user accounts in a coordinated fashion that minimizes the gap between resets. Plan the sequence of credential resets to prioritize the most privileged accounts first, coordinate with business units to identify appropriate maintenance windows, and communicate clearly with users to prevent legitimate access disruptions.

For example, when investigating a suspected Kerberos Golden Ticket attack, coordinate a comprehensive credential reset: start with the KRBTGT account (twice to invalidate all existing tickets), then all domain administrator accounts, then privileged service accounts, and finally standard user accounts. Implement resets in rapid succession to minimize the window during which attackers can use not-yet-reset credentials to regain access after detecting initial containment efforts.

Infrastructure-wide changes, such as firewall rule updates or network topology modifications, require careful planning and testing to ensure that containment measures don’t inadvertently disrupt business-critical communications or introduce new vulnerabilities in the environment. Large-scale firewall changes can block legitimate business traffic if rules are too broad, while network segmentation modifications might isolate systems needed for critical operations. Test containment changes in non-production environments, when possible, maintain rollback procedures for rapid recovery from unintended impacts, and coordinate with network operations teams who understand traffic dependencies.

TECHNICAL IMPLEMENTATION

Effective containment requires both tools and techniques appropriate to the environment and threat. In this section, we’ll explore technical methods for containment across network, host, application, and identity layers, covering the controls and techniques each layer provides and the situations in which each is most effective.

Figure 77 | Containment Implementation Layers

Network-Level Containment

Network containment provides broad control over attacker communications through controls that can be implemented quickly to manage large numbers of systems.

Network Isolation Techniques

VLAN isolation moves compromised systems to isolated network segments with restricted access, effectively quarantining them from the production network. Private VLANs can prevent attackers from continuing to access systems while maintaining necessary management access for incident response activities. Designating a quarantine VLAN, for example, allows responders to configure the minimum access requirements needed to support the investigation effort while denying attackers access to systems. Firewall rule implementation blocks specific protocols, ports, or destinations used by attackers at network control points. Micro-segmentation using host-based firewalls or software-defined networking provides more granular control over individual system communications when network-wide rules prove too broad. Implement emergency firewall rules that block known command-and-control IP addresses while maintaining business-critical traffic flows, and refine them as analysts gather more intelligence about the attacker’s infrastructure.

For larger organizations, network route manipulation can redirect entire network ranges to containment infrastructure, enabling enterprise-wide isolation. This advanced technique requires coordination with network engineering teams and careful planning to avoid disrupting legitimate business communications while achieving effective containment of widespread compromises.

DNS Sinkholes

Another option is to leverage DNS sinkholes, allowing organizations to redirect attacker-designated hostnames to internal systems.  By adding the attacker domains and host names to DNS servers used by impacted systems, organizations can stop command-and-control (C2) access while maintaining visibility into attempted connections (through DNS server logs and DNS-redirected connection logs) that can inform threat intelligence efforts.

In a recent engagement, an attacker deployed C2 malware resolving the name www[dot]thirtjo13ht[dot]top to communicate with their infrastructure. Internal DNS servers typically use recursive resolution to resolve external names, allowing the malware to connect to the attacker’s C2 servers, as shown in Figure 78 . By adding the domain thirtjo13ht[dot]top to the internal DNS server, as shown in Figure 79 , the incident response team redirected all C2 traffic to an internal quarantine server, preventing the attacker from maintaining control while allowing analysts to observe connection attempts to identify other compromised systems.

Figure 78 | DNS Resolution Resolves Attacker C2 Server

Figure 79 | DNS Sinkhole Redirects Attacker C2 Traffic

While DNS sinkholes are valuable for some scenarios, they have limitations. For example, some attackers will use hardcoded IP addresses or encrypted DNS to bypass DNS-based controls, making sinkholes ineffective. Also, attackers may use a legitimate hosted infrastructure provider name for their malicious web application (such as live-okta-verify[dot]vercel[dot]app), making it impractical to sinkhole a broad service provider domain without disrupting legitimate traffic.

DNS Over HTTPS and Sinkhole Limitations

DNS over HTTPS (DoH) offers several security benefits, but it also complicates traditional DNS-based containment strategies. Used by default in major browsers like Google Chrome and Mozilla Firefox, DoH encrypts DNS queries within HTTPS traffic, preventing an organization from controlling name resolution behavior over the standard DNS protocol (DNS over port 53, often referred to as Do53). Instead of resolving directly to external DoH resolvers including Google, Cloudflare, Quad9, and others, over an HTTPS request, as shown in the following example.

$ curl -H 'accept: application/dns-json' 'hxxps://cloudflare-dns[.]com/dns-query?name=www.toteslegit.us&type=A' {"Status":0,"TC":false,"RD":true,"RA":true,"AD":true,"CD":false,"Question":[{"name":"www.toteslegit.us","type":1}],"Answer":[{"name":"www.toteslegit.us","type":1,"TTL":300,"data":"172.104.10.22"}]} 1

1 Cloudflare DoH response for www.toteslegit.us With DoH, organizations lose the ability to deploy DNS sinkhole containment through a traditional internal DNS server. However, the order of operations for name resolution is: use the system resolver first, then resolve the name using DoH. While this still precludes the use of Do53-based sinkholes, organizations can implement host-based DNS overrides to redirect attacker domains to internal containment systems by distributing a local hosts file to internal systems, by configuring a local DoH server with precedence over public DoH resolvers, or by disallowing DoH in browsers through group policy or endpoint management controls.

Host-based overrides require administrative control of the endpoint, so BYOD devices enrolled without full management remain outside these controls. DoH traffic from unmanaged personal devices connected to the corporate network will resolve attacker domains normally, limiting sinkhole coverage to the managed fleet.

Host-Level Containment

Host-based containment provides precise control over individual systems through multiple enforcement mechanisms that balance investigation needs with operational security. EDR isolation features quarantine systems while maintaining forensic access, allowing incident responders to continue evidence collection while preventing attacker communications. Modern EDR platforms can block network access except for management connections, preserving the ability to remotely collect memory dumps, deploy analysis tools, and retrieve forensic artifacts. Local firewall configuration restricts network access at the host level when EDR capabilities are unavailable. Configure host firewalls to prevent both inbound and outbound connections except for specific management protocols necessary for system administration and forensic investigation.  Host-specific firewall tools, including Windows Firewall and Linux Netfilter (managed using iptables), can implement connection restrictions while maintaining access to domain controllers for authentication, DNS servers for name resolution, and incident response systems for remote management. Process and service restrictions prevent execution of attacker tools while maintaining essential system functionality for business operations. Application control technologies such as Windows AppLocker, macOS Gatekeeper, and Linux AppArmor can block the execution of unauthorized executables, scripts, and libraries based on publisher certificates, file paths, or file hashes.

Application-Level Containment

Application-specific containment addresses compromises within specific services through targeted restrictions that maintain operational capability while limiting attacker access. This approach recognizes that a complete service shutdown often causes unacceptable business impact, requiring more precise intervention that contains the threat posed by the attacker while preserving system functionality. Web Application Firewalls (WAFs) block malicious requests to compromised web applications while maintaining legitimate access for authorized users. Organizations can introduce application-level containment by deploying WAF rules that detect and prevent several common attack classes. WAF tools might include Software as a Service (SaaS) offering from Cloudflare, for example, or might be locally deployed tools such as ModSecurity rules (for Windows and Linux web servers). WAF services can help limit what attackers can use to attack systems, but should not be relied on as long-term defenses without resolving underlying platform vulnerabilities.

Database access restrictions can limit queries from compromised applications or accounts to prevent data exfiltration while preserving normal business operations. Implement query monitoring that flags unusual patterns, such as large result sets, schema enumeration, or access to sensitive tables outside intended access methods.  Database activity monitoring tools, including IBM Security Guardium, can block or quarantine suspicious queries based on data volume thresholds, query complexity, or access patterns that deviate from established baselines.

Organizations increasingly deploy AI agents with broad access to internal systems via integration frameworks such as the Model Context Protocol (MCP), enabling automated tools to query databases, access file systems, send messages, and execute code on behalf of users. These integrations create a containment surface that responders should address when compromised accounts have access to AI agent capabilities, or when the agent integrations themselves are exploited through prompt injection or other platform vulnerabilities. Containment actions include disabling AI agent tool access and MCP server connections, revoking the service principals or API keys that grant AI systems access to organizational data, and monitoring AI-generated outputs for signs of data leakage through carefully crafted queries. AI agent integrations often authenticate using service principals or API keys that are separate from the user accounts that invoke them. Revoking a compromised user’s credentials may not revoke the AI agent’s access to organizational data. Inventory AI integration credentials as part of preparation activities.

Identity and Access Management Containment

Modern containment strategies center on identity as the new security perimeter, recognizing that traditional network boundaries have dissolved in hybrid cloud, remote work, and SaaS-dominated environments. Identity providers (IdPs) now serve as the primary control plane for containment, requiring complex procedures for comprehensive containment, including credential revocation, token invalidation, and session management across distributed platforms.

When addressing identity-based compromises, organizations should systematically implement containment actions to ensure complete coverage across all authentication mechanisms that attackers might leverage to maintain access. Start by invalidating credentials immediately, then address active sessions, and finally implement conditional access policies that prevent re-authentication while the team investigates. In this section, we’ll explore each of these steps in more detail, with actionable recommendations for effective

Figure 80 | Identity and Access Management Containment Steps

When containment requires creating temporary accounts (for example, to preserve administrative access after a bulk reset or to operate an isolated system), the incident response team should record each account in the incident documentation at creation, including the purpose, intended lifespan, and owner, so that closure activities can review each account for retention or removal.

Credential Revocation

Begin identity containment by invalidating compromised credentials across all authentication systems where they exist. Reset passwords for affected user accounts via the primary identity provider, preventing attackers from using stolen credentials. In addition to conventional user accounts, remember to address service accounts, application accounts, and programmatic integrations that might use API keys or access tokens for authentication.

Organizations using multiple identity systems should revoke credentials in all locations where the compromised account exists. An account synced between on-premises Active Directory and Microsoft Entra ID requires password resets in both systems to ensure complete containment, as synchronization delays may create brief windows when old credentials remain valid in one environment. Similarly, revoke credentials in any federated partner directories or connected SaaS platforms that might cache authentication information.

Credential revocation in isolated environments depends on management connectivity that may not exist. If the team has already cut internet access as part of containment, cloud-hosted identity providers cannot push invalidation updates to servers that no longer reach the control plane, and local authentication caches may keep stolen credentials valid until the cache entries expire. Plan the order of operations so that credential revocation completes before wider network isolation, or maintain a trusted management path that survives the isolation posture.

Active Session Termination

After invalidating credentials, force-terminate all active sessions to deny attackers access via existing authenticated sessions that survive password changes. This is most readily accomplished using an Identity Platform’s session revocation feature to invalidate all access tokens and session cookies for the target account(s). Modern identity platforms often provide a revoke-all-sessions feature that invalidates session tokens across all connected applications.

The interval between credential revocation and active session termination is a window of residual attacker access, and the team should treat it as a measurable service-level target rather than an incidental delay. An attacker on the VPN who retains a live session after the credentials have been reset can still initiate their own password reset flow, enroll a new MFA factor, or establish additional persistence before sessions are terminated. Establish an in-incident SLA with the IT team during the prepare activity so that the handoff from the IRT to the account management team happens within a defined target, and capture actual times during exercises to validate the target is achievable.

Session termination through the IdP only affects applications that check session validity with the identity provider on each request. Many applications, including SaaS platforms, will cache session state locally or issue their own session cookies that remain valid even after IdP session revocation (see the sidebar on Back-Channel Logout: A Critical Missing Component ). For accounts with extra privileges or high-risk compromises, it may be necessary to contact the SaaS application’s support team to request forced logout and session invalidation at the application level.

Beyond web application sessions, terminate active connections across all authentication methods the account might use. Disconnect any remote access sessions (e.g., VPN) via the platform management interface, identify active connections by username, and forcibly terminate them.  For Remote Desktop Protocol (RDP) access, use tools like qwinsta and rwinsta on Windows servers to identify and disconnect active RDP sessions associated with the compromised account, as shown in Listing 48 . SSH connections require identifying active sessions on target systems with who or w commands, then terminating the SSH child processes with pkill -u username or by forcing the disconnect of specific TTY sessions.

Listing 48 | Windows RDP Server Session Query and Termination
C:\> qwinsta /server:rdp-server01
SESSIONNAME       USERNAME          ID  STATE   TYPE        DEVICE
services                            0  Disc
>console           Administrator     1   Active  wdcon
rdp-tcp#0         alice             2   Active  rdpwd
rdp-tcp#1         admin             3   Active  rdpwd 1
rdp-tcp#2         bob               4   Active  rdpwd
C:\> rwinsta 3 /server:rdp-server01
SUCCESS: The session was reset.
1 Attacker RDP session

Listing 49 | SSH Server Session Query and Termination
$ who
admin    pts/0        2025-11-02 08:30 (192.168.1.140)
admin    pts/1        2025-11-01 02:53 (192.0.2.42) 1
alice    pts/2        2025-11-02 08:12 (192.0.2.10)
bob      pts/3        2025-11-02 08:20 (192.0.2.22)
$ sudo pkill -9 -t pts/1
$ who
admin    pts/0        2025-11-02 08:30 (192.168.1.140)
alice    pts/2        2025-11-02 08:12 (192.0.2.10)
bob      pts/3        2025-11-02 08:20 (192.0.2.22)
1 Attacker SSH session

Host-based queries like qwinsta and who work for targeted investigation but become impractical across the enterprise. A complementary approach is to query the SIEM for the pattern of session opened without matching close , which applies equally to sessions from RDP, SSH, remote monitoring and management (RMM) tools, and cloud consoles. Each emits a logon event and a logoff event that should pair up under normal operation, and unpaired logons after a credential reset are a reliable signal of active sessions that need additional intervention for containment.

For Windows RDP, Event ID 4624 with LogonType 10 marks the session open, and Event ID 4634 marks the session close. The Splunk query in Listing 50  identifies RDP sessions that were opened without a corresponding close event, indicating active sessions that may still be accessible to attackers after credential revocation. SSH follows the same pattern with sshd authentication and disconnect messages, and RMM tools emit session-start and session-end events in their own audit logs.

Listing 50 | Splunk SIEM Query for RDP Sessions Opened Without Close
index=wineventlog EventCode=4624 LogonType=10 1
| fields _time, TargetUserName, TargetLogonId, IpAddress, Computer
| join type=left TargetLogonId 2
[search index=wineventlog EventCode=4634
| fields TargetLogonId, EventCode]
| where isnull(EventCode) 3
| table _time, TargetUserName, IpAddress, Computer
1 Retrieve RDP logon events (LogonType 10).
2 Left join logoff events (4634) using TargetLogonId as the correlation key.
3 Keep only logons without a matching logoff.

Responders can adapt the query for other SIEMs by substituting the event source, logon and logoff event identifiers, and the correlation key (username, session ID, or token ID) to match the target session type.

Refresh Token and Persistent Credential Revocation

Refresh tokens represent a persistence mechanism that allows attackers to generate new access tokens even after revoking active sessions and resetting passwords.  In practice, OAuth refresh tokens can have very long lifetimes measured in months and remain valid until explicitly revoked. Responders should access the identity provider’s token management interface to revoke all refresh tokens associated with the compromised account, preventing attackers from requesting new access tokens using previously issued refresh tokens.

Modern authentication protocols use various token types that each require separate revocation consideration. OAuth deployments use access tokens (short-lived, typically 1 hour), refresh tokens (long-lived, potentially months), and sometimes offline access tokens that enable access without user interaction. Security Assertion Markup Language (SAML) assertions are typically short-lived but may be cached by service providers for extended periods. JSON Web Tokens (JWTs) can be stateless and self-contained. Their lack of a revocation feature makes revocation impossible without implementing token deny lists at each resource server.

Table 18 | Token Types and Revocation Considerations
TOKEN TYPE TYPICAL

LIFETIME

REVOCATION METHOD PERSISTENCE RISK

OAuth Access

Token

Short (typically 1 hour) Revoke via authorization server API Low: expires quickly if not refreshed

OAuth Refresh

Token

Long (potentially
