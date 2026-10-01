# Chapter 12: Contain Activity: Isolation & Network Segmentation

> Source: PDF Pages 240-295 (Total Pages: 56)

The extended activity search revealed that the service principal had been accessed from the external IP

address as early as October 8th, more than a week before the first management operations Priya had

initially identified. The role assignment query confirmed that the attacker had granted the service principal

Contributor access to a second resource group, rg-analytics-eastus2, expanding the potential scope of

compromise beyond the production environment.

Priya compiled a summary of her scoping findings for the incident commander, including the confirmed

timeline of attacker activity, the scope of compromised resources across both resource groups, an

assessment of the volume and sensitivity of exfiltrated data, and recommended next steps for containment.

This summary provided leadership with the context needed to make informed decisions about notification

obligations, containment priorities, and resource allocation as the investigation continued.

SCOPE: STEP-BY-STEP

The following steps provide a condensed reference for scoping activities. Each step corresponds to topics

covered earlier in this chapter, organized for use when determining the full extent of compromise across

the environment.

This step-by-step guide is available for download in PDF and Markdown formats on the

companion website at dynamicincidentresponse.com.

Step 1. Identify Indicators of Compromise from Detection and

Verification

Categorize the IOCs handed off from verify and triage into the canonical inventory used for sweeps.

Representative IOC categories include:

• File-based indicators (hashes, filenames, file paths).

• Network indicators (IP addresses, domains, URLs, signatures).

• Process and service indicators (process names, command-line arguments).

• Registry and configuration indicators (registry keys, configuration changes).

• Account-based indicators (unauthorized accounts, suspicious usage patterns).

• Behavioral indicators (temporal patterns, data movement, lateral movement).

Step 2. Conduct Enterprise-Wide Hunting for Identified IOCs

This is the IOC-driven sweep during a verified incident, distinct from the standing hypothesis-driven

hunting program owned by detect. Representative activities include:

• Search centralized log analysis tools (SIEM, log aggregation systems).

• Leverage EDR platforms to search across managed endpoints.

• When EDR is not available, use inventory management tools, active scanning, network scans, or custom

scripts to probe for IOCs.

• Apply threat-hunting platforms that combine endpoint, network, and logging data to provide

overlapping analysis coverage.

Step 3. Apply Progressive Scoping Methodology

Representative activities include:

• Prioritize critical assets (domain controllers, file servers, databases, systems with sensitive data).

• Expand laterally to systems connected to known-compromised hosts.

• Conduct an environmental sweep across all systems.

Step 4. Reconstruct the Attack Timeline

Scope owns the canonical attack-progression timeline; subsequent activities annotate it (eradicate adds

eradication-sequencing markers; debrief consolidates into the final narrative). Representative activities

include:

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

• For systems with limited logging, use alternative evidence sources such as network flow data and

authentication logs from connected systems.

• For ICS and industrial devices without centralized logging (for example, programmable logic

controllers), rely on network flow data as the primary source of evidence.

• Watch for anti-forensic techniques (log deletion, timestomping, encryption and obfuscation, living off

the land).

• Use counter-strategies, including log manipulation detection, alternative timestamp sources, behavioral

analysis, and command-line argument review.

• Apply cloud-specific scoping tools and techniques for cloud and hybrid environments, including cloud

provider audit logs and container runtime security.

• Scope cloud environments quickly. Ephemeral resources can deallocate and take evidence with them if

scoping is delayed.

• Manage scale and complexity through prioritization and automation.

• Document false positive sources for future reference.

Scope Activity | Chapter 11 | 217

Step 7. Prepare Scoping Results for Containment, Eradication, and

Recovery

Hand off the scoped system list, the canonical IOC inventory (Step 1), and the attack-progression timeline

(Step 4) so each downstream activity can build on settled artifacts rather than re-derive them.

[1] Siemens S7-1200 G2 PLC, image used courtesy of Siemens.

Scope Activity | Chapter 11 | 219

12 Contain Activity

The containment activity represents an inflection point in incident response, where teams transition from

scoping the incident’s breadth to taking decisive action against the threat. Containment serves dual

purposes: stopping the attacker from causing additional harm while preserving evidence for investigation.

This balance between aggressive action and careful preservation of evidence requires both technical

sophistication and strategic thinking.

Figure 74 | Contain Activity Waypoint

This chapter explores the objectives of containment, implementation strategies, timing considerations, and

technical methods for effective containment in modern environments. We will also examine the challenges

unique to cloud, remote work, and encrypted communications to provide guidance on developing effective

containment approaches for these environments. The chapter also addresses the importance of validating

containment success and documenting actions taken throughout the process.

CONTAINMENT OBJECTIVES

Containment encompasses two primary objectives: stopping attacker activity and collecting evidence. In

this section, we’ll explore each objective in detail to understand its importance and implementation

considerations.

Stopping Attacker Activity

The first objective of containment is to prevent the attacker from continuing malicious activities. In the

past, this meant unplugging affected systems from the network, an approach that is no longer practical for

many organizations with disparate and distributed systems. Modern containment strategies require more

sophisticated approaches that balance security needs with operational requirements. This includes

techniques such as network isolation, account restrictions, and process termination.

Network isolation uses technologies such as private VLANs, access control lists, cloud security groups, and

software-defined networking to restrict the movement of attackers without completely disrupting business

operations. Rather than disconnecting systems entirely, responders can sever specific communication paths

while maintaining critical business functions. For example, isolating a compromised web server from

internal systems while maintaining its internet-facing services allows containment without complete

service disruption.

Account restrictions disable or limit access to compromised accounts, ideally without alerting the attacker

to defensive measures. This can include changing account passwords, revoking privileges, or implementing

conditional access policies that limit access while maintaining the appearance of normal operations.

Organizations should coordinate credential resets carefully to avoid triggering attacker awareness while

still achieving effective containment.

Process termination stops identified malicious processes, though this action should also be executed

carefully to avoid tipping off sophisticated attackers who may have monitoring capabilities in place.

Advanced adversaries may implement watchdog processes that respawn terminated malware, and human-

operated ransomware groups have been observed accelerating encryption timelines when they detect

defensive actions, making subtle containment approaches preferable to aggressive process killing in many

scenarios.

Aggressive containment actions can backfire. Human-operated ransomware groups have

been observed accelerating encryption timelines when they detect defensive actions, and

watchdog processes can respawn terminated malware or trigger destructive payloads.

Consider subtle, coordinated containment approaches before killing processes on systems

where adversary behavior is not yet fully understood.

Evidence Collection and Preservation

The second objective ensures that critical evidence is captured before it disappears or becomes corrupted.

This evidence is subsequently used to gain further insight into the attacker’s tactics, techniques, and

procedures (TTPs) during the eradicate activity, to help responders understand the attack, and potentially

to support future legal action. Organizations should prioritize evidence collection by volatility, collecting

the most transient data first.

Memory acquisition captures volatile data that would be lost if systems were powered down or rebooted.

Memory dumps preserve information about running processes, host configuration details, network

Contain Activity | Chapter 12 | 221

connections, and other artifacts critical for understanding attacker activities.  Tools like WinPMEM (and the

companion Linux memory acquisition tool Linpmem) enable rapid memory capture with minimal system

impact, allowing analysts to preserve evidence while maintaining system availability.

Forensic imaging of affected systems preserves the complete state for detailed analysis. While full disk

imaging has become less common due to storage costs and time constraints, selective imaging of critical

systems or specific directories remains valuable for detailed investigation. Organizations can focus imaging

efforts on systems that contain unique evidence, such as the initial point of compromise or systems where

attackers deployed custom tools.

Log preservation ensures that evidence of attacker activity isn’t lost to rotation or deletion. This includes

not only security logs but also application logs, authentication records, and network flow data that might

reveal attack patterns. Forward logs to a centralized, secure location immediately upon discovering a

compromise to prevent attackers from deleting or modifying local log files to cover their tracks.

CONTAINMENT STRATEGIES

Now that we’ve established the objectives of containment, we can explore various implementation

strategies.

Organizations should choose containment strategies appropriate to their specific incident, balancing

effectiveness with operational impact and the level of attacker awareness. In this section, we’ll explore

passive, active, and adaptive containment strategies, and how organizations can transition between them

based on evolving threat intelligence and operational needs.

Figure 75 | Containment Strategy Evolution

TERMINATE OR MONITOR: ORGANIZATIONAL CONSIDERATIONS

Organizations face an important decision during the contain activity: immediately terminate the

attacker’s access or continue monitoring to gather intelligence. This choice carries significant

implications for both incident outcomes and organizational risk posture.

Immediate termination offers the clearest benefit of stopping ongoing damage. Attackers can no

longer exfiltrate data, deploy ransomware, or establish additional persistence mechanisms. However,

premature action may alert sophisticated threat actors who then accelerate their timeline, triggering

rapid data destruction or immediate ransomware deployment before responders can implement

comprehensive containment.

Continued monitoring provides valuable intelligence about attacker objectives, techniques, and the

full scope of compromise. Organizations can identify all affected systems, understand data targeting

patterns, and prepare thorough remediation strategies. This approach becomes particularly critical

during ransomware negotiations, where isolating the attacker’s access to a subset of systems could

prompt immediate encryption or higher payment demands.

The decision ultimately depends on organizational risk tolerance, operational constraints, and

incident specifics. High-value targets, safety-critical systems, and regulated environments typically

require immediate protection regardless of intelligence gathering opportunities. Conversely,

organizations with robust backup strategies and strong forensic capabilities may choose to extend

monitoring to develop a comprehensive understanding of threats before taking action.

Choosing between passive, active, and adaptive containment under pressure benefits from pre-agreed

criteria rather than judgment made in the moment. Table 16 lists common factors and which strategy each

one favors. Analysts can scan the table during an incident (or one like it customized to the organization’s

needs) to identify which factors apply and where the weight of evidence points.

Table 16 | Factors Influencing Containment Strategy Selection

FACTOR PASSIVE ADAPTIVE ACTIVE

Active data destruction or

ransomware underway

Required

Regulated data with compliance-

driven timeline

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

Possible

The sections that follow examine passive, active, and adaptive containment in detail, covering the

techniques, trade-offs, and transition points analysts apply once the initial decision is made.

Contain Activity | Chapter 12 | 223

Passive Containment

Passive containment focuses on limiting damage without alerting the attacker to defensive actions, allowing

organizations to gather intelligence while reducing risk. This approach works best when organizations have

strong monitoring capabilities and can afford to accept some continued attacker presence in exchange for a

better understanding of the threat.

When it is available to the incident response team, analysts can gain valuable insight by monitoring attacker

tactics, techniques, and procedures before implementing containment actions. This insight can reveal

additional compromised systems, help responders understand data targeting patterns, and inform

comprehensive remediation strategies. For example, monitoring an attacker’s lateral movement attempts

reveals which systems they consider high-value targets, informing both immediate containment priorities

and long-term security improvements.

Honeypots and deception technologies divert attackers from real assets to decoy systems designed to

appear valuable while actually containing no sensitive data. These controlled environments allow

observation of attacker techniques while protecting production systems from damage. Organizations can

deploy honeypots that closely mirror production systems to attract attacker attention, but mark them

clearly in backend systems to distinguish legitimate alerts from deception-based detections.

Passive containment is uncommon in modern incidents. Capable attackers detect

defensive monitoring quickly and either accelerate their timeline or burn their access

deliberately, reducing the intelligence window to a fraction of what strong-monitoring

organizations hope for. Reserve this strategy for narrow scenarios such as commodity

malware on low-value assets or controlled deception environments, and expect to

transition to active containment at the first sign of attacker awareness.

Active Containment

Active containment takes decisive action to stop attacker activities, accepting that the attacker may become

aware of defensive efforts and potentially accelerate their timeline. Organizations choose this approach

when the risk of continued attacker access outweighs the intelligence value of observation, or when

immediate triggers, such as active data destruction, demand an urgent response.

Network segmentation isolates compromised segments from the rest of the network through multiple

technical approaches. This might involve introducing firewall rules or access control lists that block traffic

associated with attacker activity, activating pre-configured network segmentation policies to isolate

systems, or physically disconnecting network segments when software controls prove insufficient.

System isolation removes specific compromised systems from the network while maintaining forensic

integrity and, where possible, management access for investigation.  Modern Endpoint Detection and

Response (EDR) tools can isolate systems while maintaining forensic connections for investigation, allowing

analysts to collect evidence, analyze running processes, and observe attacker behavior without granting

attackers network access to other systems. Prefer EDR isolation features over network-based isolation

controls when available, allowing responders to continue using EDR solutions to collect evidence while

preventing attacker access.

Service disruption disables compromised services or applications to prevent further damage when other

containment methods prove insufficient. This might include stopping web services that attackers are using

to exfiltrate data, disabling remote access protocols such as Remote Desktop Protocol (RDP) or Secure Shell

(SSH) that provide attacker entry points, or shutting down specific business applications that attackers have

compromised. Organizations should coordinate service disruption with business stakeholders to

understand operational impacts and identify alternative workflows during the containment period.

WHEN RMM TOOLS TURN AGAINST YOU: THE STRYKER COMPROMISE

Stryker is one of the world’s largest medical technology companies, producing devices and equipment

used in hospitals and surgical settings worldwide. Based in Kalamazoo, Michigan, the company

manufactures products ranging from joint replacement implants and surgical instruments to hospital

beds and robotic-assisted surgery systems. With $25 billion in annual revenue and approximately

56,000 employees worldwide, a disruption to Stryker’s operations has far-reaching consequences for

healthcare providers and patients.

In March 2026, attackers compromised Stryker’s Microsoft Intune environment, a Mobile Device

Management (MDM) platform, and used it to remotely wipe devices across the organization, including

laptops, phones, and other endpoints enrolled in the platform. [1]

The attack was attributed to

Handala, an Iran-linked group believed to be a front for Void Manticore, a threat actor sponsored by

the Iranian government. Handala claimed to have wiped more than 200,000 servers, mobile devices,

and other systems, forcing Stryker to shut down offices in seventy-nine countries.

The impact was immediate and global. Staff reported that their personal devices were wiped, and

they lost access to eSIMs, two-factor authentication, email, and collaboration tools. The company

closed office facilities and posted notices instructing employees to stay off the network, avoid using

computers, and disconnect from WiFi. For work phones, Stryker recommended that employees

remove the device management profile entirely to prevent further damage from the compromised

MDM platform.

Figure 76 | Stryker Facility Employee Notice

The disruption extended beyond IT systems into manufacturing operations. The attack destroyed

critical software tools for product design and supply chain management, forcing a temporary halt to

manufacturing. At Stryker’s Cork, Ireland, headquarters, over 4,000 employees lost network access,

Contain Activity | Chapter 12 | 225

and modern factory systems that relied on the digital infrastructure saw regional manufacturing

output slow.

This incident illustrates a containment challenge that organizations with remote management

platforms should plan for: the same capabilities that enable rapid response can also become an attack

vector. When attackers gain access to tools like Microsoft Intune, they can issue commands at scale,

wiping devices, pushing malicious configurations, or revoking access across the entire fleet.

Containment in these scenarios requires disconnecting from the very management infrastructure

that responders would normally rely on to contain the threat. Organizations should plan for this

possibility by establishing out-of-band communication channels and offline containment procedures

that do not depend on device management infrastructure.

Adaptive Containment

Sophisticated incidents may require adaptive containment that evolves based on attacker behavior,

adjusting response tactics as the incident unfolds and new intelligence emerges. This approach combines

passive and active techniques, transitioning between them based on threat assessment and operational

requirements.

Progressive restrictions gradually increase containment measures based on the actions of attackers,

allowing organizations to gather intelligence in the early stages while maintaining the ability to escalate to

aggressive containment when necessary. Starting with passive monitoring, teams can progressively

implement more aggressive containment measures as they understand the threat scope and the attacker’s

objectives. For example, analysts might begin by monitoring attacker lateral movement attempts to map

target systems, then implement network restrictions that prevent access to high-value targets while

preserving attacker access to lower-value decoy or honeypot systems that continue to provide intelligence.

Deceptive containment makes the attacker believe they maintain access while actually operating in a

controlled environment, providing the intelligence benefits of passive monitoring while reducing

operational risk. This might involve redirecting attacker tools to honeypot systems that appear identical to

production systems, providing false data that appears valuable but actually contains no sensitive

information, or allowing access to sandboxed environments that prevent real damage.

TIMING AND COORDINATION

Containment timing impacts incident outcomes and business operations, requiring a careful balance

between speed and comprehensiveness. Premature containment may alert attackers before responders fully

understand the scope, triggering accelerated data destruction or ransomware deployment before teams can

implement comprehensive protection. Delayed containment allows continued damage and potential data

exfiltration, increasing the incident’s impact and the potential regulatory consequences.

Organizations should establish clear decision criteria for timing containment based on threat indicators,

business impact, and intelligence-gathering needs. In this section, we’ll examine immediate containment

triggers and coordinated containment strategies for complex incident response efforts.

Immediate Containment Triggers

Certain scenarios demand immediate containment, regardless of incomplete understanding, where the risk

of delayed action outweighs the value of additional intelligence gathering or comprehensive scoping.

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

payment processing, or other safety-

critical infrastructure

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

The regulatory landscape is jurisdiction-specific, and the examples in Table 17 are illustrative rather than

exhaustive. European organizations should also consider NIS2 and DORA for operators of essential services

and financial entities, and the Cyber Resilience Act (CRA) for organizations that place products with digital

elements on the EU market, along with sector-specific requirements such as the Revised Payment Services

Directive (PSD2) and the UK Financial Conduct Authority’s operational resilience rules (PS21/3).

Ideally, decision makers and organizational leadership decide which triggers apply during

the prepare activity and maps each one to a specific response action. This allows the team

to apply those policy decisions during the incident, referencing a pre-approved position

rather than requiring fresh interpretation under pressure.

Active data destruction is the most urgent trigger, in which attackers are actively deleting or encrypting

critical data, and leaving no time for intelligence gathering or coordinated response planning. When

responders observe ransomware encryption spreading across file shares, attackers wiping event logs to

cover their tracks, or database tables being dropped in real time, immediate containment may be the most

reasonable action to best meet the organization’s needs. The speed of modern ransomware can encrypt

thousands of files per minute, making every second of delay costly in terms of data loss and recovery effort.

Ongoing data exfiltration of sensitive information to external locations demands urgent action, particularly

when the data includes intellectual property, customer records, or regulated information that could result

in significant financial or reputational damage. Monitor for large data transfers to cloud storage services,

suspicious database queries that retrieve thousands of customer records, or the creation and transfer of file

archives to external sites.

The volume and sensitivity of exfiltrated data will affect regulatory notification requirements, potential

fines, and the organization’s reputation. For example, when observing a compromised service account

executing database queries that have retrieved sensitive PII and establishing connections to a suspicious

external IP address, organizations will likely transition to immediate containment actions, even if

responders haven’t yet identified how the service account was initially compromised.

Contain Activity | Chapter 12 | 227

Threats to critical operations or safety systems will also warrant immediate action to prevent operational

disruption or physical harm that could affect services or employee safety. Industrial control systems,

medical devices, payment processing infrastructure, and other safety-critical or business-critical systems

can rarely tolerate extended compromise time while teams gather intelligence. The operational and safety

consequences of delayed response in these environments may outweigh the investigative benefits of

continued monitoring.

Regulatory requirements may mandate specific containment timeframes for certain incident types,

overriding tactical considerations about optimal response timing. Healthcare data breaches under the

Health Insurance Portability and Accountability Act (HIPAA), payment card compromises under the Payment

Card Industry Data Security Standard (PCI DSS), and personal data incidents under the General Data

Protection Regulation (GDPR) all carry specific notification timelines that effectively require rapid

containment to minimize the scope of affected records and demonstrate reasonable response efforts. [2]

[3]

[4]

Regulatory frameworks may also define breach severity based on the number of affected individuals and the

duration of unauthorized access, creating direct financial incentives for rapid containment. For example,

when discovering unauthorized access to a database containing Protected Health Information (PHI),

organizations should implement immediate containment within hours rather than days to limit the

compliance window and reduce the number of affected patient records requiring notification under HIPAA

breach notification rules. Delays could expand both the legal exposure and the population requiring

individual notification.

Coordinated Containment

Complex incidents affecting multiple systems require coordinated containment to prevent attackers from

maintaining access through overlooked systems or pivoting to alternative infrastructure when they detect

partial containment efforts.

Simultaneous Isolation

Simultaneous isolation of all known compromised systems prevents attackers from pivoting to maintain

access through alternative pathways that remain available during otherwise sequential containment actions.

When attackers have established a presence on multiple systems, isolating them one at a time alerts the

adversary to defensive activities and provides an opportunity to accelerate their timeline, deploy additional

persistence mechanisms, or trigger destructive payloads.

Coordinate timing and communication across technical teams to ensure comprehensive coverage where

network, endpoint, and application teams all execute containment actions within a narrow time window.

For example, when responding to a lateral movement incident in which attackers have compromised fifteen

workstations across three departments, analysts may simultaneously enable EDR isolation on all affected

systems while the network team implements VLAN restrictions and the identity team disables compromised

accounts. This coordinated approach prevents attackers from detecting partial containment and moving to

systems that remain accessible.

Isolating compromised systems one at a time is a common containment mistake.

Sequential containment alerts the adversary and gives them time to escalate privileges,

deploy additional persistence, or trigger destructive payloads on systems not yet

contained.

Credential and Infrastructure Coordination

A credential reset is necessary across the entire environment when credential theft is identified. To be

effective, the credential reset procedures should be coordinated to avoid creating windows in which

attackers maintain access through credentials that have not yet been rotated. Domain-wide credential

compromises require rotating passwords for all privileged accounts, service accounts, and potentially all

user accounts in a coordinated fashion that minimizes the gap between resets. Plan the sequence of

credential resets to prioritize the most privileged accounts first, coordinate with business units to identify

appropriate maintenance windows, and communicate clearly with users to prevent legitimate access

disruptions.

For example, when investigating a suspected Kerberos Golden Ticket attack, coordinate a comprehensive

credential reset: start with the KRBTGT account (twice to invalidate all existing tickets), then all domain

administrator accounts, then privileged service accounts, and finally standard user accounts. Implement

resets in rapid succession to minimize the window during which attackers can use not-yet-reset credentials

to regain access after detecting initial containment efforts.

Infrastructure-wide changes, such as firewall rule updates or network topology modifications, require

careful planning and testing to ensure that containment measures don’t inadvertently disrupt business-

critical communications or introduce new vulnerabilities in the environment. Large-scale firewall changes

can block legitimate business traffic if rules are too broad, while network segmentation modifications might

isolate systems needed for critical operations. Test containment changes in non-production environments,

when possible, maintain rollback procedures for rapid recovery from unintended impacts, and coordinate

with network operations teams who understand traffic dependencies.

TECHNICAL IMPLEMENTATION

Effective containment requires both tools and techniques appropriate to the environment and threat. In this

section, we’ll explore technical methods for containment across network, host, application, and identity

layers, covering the controls and techniques each layer provides and the situations in which each is most

effective.

Figure 77 | Containment Implementation Layers

Contain Activity | Chapter 12 | 229

Network-Level Containment

Network containment provides broad control over attacker communications through controls that can be

implemented quickly to manage large numbers of systems.

Network Isolation Techniques

VLAN isolation moves compromised systems to isolated network segments with restricted access,

effectively quarantining them from the production network. Private VLANs can prevent attackers from

continuing to access systems while maintaining necessary management access for incident response

activities. Designating a quarantine VLAN, for example, allows responders to configure the minimum access

requirements needed to support the investigation effort while denying attackers access to systems.

Firewall rule implementation blocks specific protocols, ports, or destinations used by attackers at network

control points. Micro-segmentation using host-based firewalls or software-defined networking provides

more granular control over individual system communications when network-wide rules prove too broad.

Implement emergency firewall rules that block known command-and-control IP addresses while

maintaining business-critical traffic flows, and refine them as analysts gather more intelligence about the

attacker’s infrastructure.

For larger organizations, network route manipulation can redirect entire network ranges to containment

infrastructure, enabling enterprise-wide isolation. This advanced technique requires coordination with

network engineering teams and careful planning to avoid disrupting legitimate business communications

while achieving effective containment of widespread compromises.

DNS Sinkholes

Another option is to leverage DNS sinkholes, allowing organizations to redirect attacker-designated

hostnames to internal systems.  By adding the attacker domains and host names to DNS servers used by

impacted systems, organizations can stop command-and-control (C2) access while maintaining visibility

into attempted connections (through DNS server logs and DNS-redirected connection logs) that can inform

threat intelligence efforts.

In a recent engagement, an attacker deployed C2 malware resolving the name www[dot]thirtjo13ht[dot]top

to communicate with their infrastructure. Internal DNS servers typically use recursive resolution to resolve

external names, allowing the malware to connect to the attacker’s C2 servers, as shown in Figure 78 . By

adding the domain thirtjo13ht[dot]top to the internal DNS server, as shown in Figure 79 , the incident

response team redirected all C2 traffic to an internal quarantine server, preventing the attacker from

maintaining control while allowing analysts to observe connection attempts to identify other compromised

systems.

Figure 78 | DNS Resolution Resolves Attacker C2 Server

Figure 79 | DNS Sinkhole Redirects Attacker C2 Traffic

While DNS sinkholes are valuable for some scenarios, they have limitations. For example, some attackers

will use hardcoded IP addresses or encrypted DNS to bypass DNS-based controls, making sinkholes

ineffective. Also, attackers may use a legitimate hosted infrastructure provider name for their malicious web

application (such as live-okta-verify[dot]vercel[dot]app), making it impractical to sinkhole a broad service

provider domain without disrupting legitimate traffic.

DNS Over HTTPS and Sinkhole Limitations

DNS over HTTPS (DoH) offers several security benefits, but it also complicates traditional DNS-based

containment strategies. Used by default in major browsers like Google Chrome and Mozilla Firefox, DoH

encrypts DNS queries within HTTPS traffic, preventing an organization from controlling name resolution

behavior over the standard DNS protocol (DNS over port 53, often referred to as Do53). Instead of resolving

DNS queries through internal DNS servers where sinkholes can be implemented, DoH queries are sent

Contain Activity | Chapter 12 | 231

directly to external DoH resolvers including Google, Cloudflare, Quad9, and others, over an HTTPS request,

as shown in the following example.

$ curl -H 'accept: application/dns-json' 'https://cloudflare-dns.com/dns-

query?name=www.toteslegit.us&type=A'

{"Status":0,"TC":false,"RD":true,"RA":true,"AD":true,"CD":false,"Question":[{"name":"www.totesle

git.us","type":1}],"Answer":[{"name":"www.toteslegit.us","type":1,"TTL":300,"data":"172.104.10.2

2"}]} 1

1 Cloudflare DoH response for www.toteslegit.us

With DoH, organizations lose the ability to deploy DNS sinkhole containment through a traditional internal

DNS server. However, the order of operations for name resolution is: use the system resolver first, then

resolve the name using DoH. While this still precludes the use of Do53-based sinkholes, organizations can

implement host-based DNS overrides to redirect attacker domains to internal containment systems by

distributing a local hosts file to internal systems, by configuring a local DoH server with precedence over

public DoH resolvers, or by disallowing DoH in browsers through group policy or endpoint management

controls.

Host-based overrides require administrative control of the endpoint, so BYOD devices enrolled without full

management remain outside these controls. DoH traffic from unmanaged personal devices connected to the

corporate network will resolve attacker domains normally, limiting sinkhole coverage to the managed fleet.

Host-Level Containment

Host-based containment provides precise control over individual systems through multiple enforcement

mechanisms that balance investigation needs with operational security.

EDR isolation features quarantine systems while maintaining forensic access, allowing incident responders

to continue evidence collection while preventing attacker communications. Modern EDR platforms can

block network access except for management connections, preserving the ability to remotely collect

memory dumps, deploy analysis tools, and retrieve forensic artifacts.

Local firewall configuration restricts network access at the host level when EDR capabilities are unavailable.

Configure host firewalls to prevent both inbound and outbound connections except for specific

management protocols necessary for system administration and forensic investigation.  Host-specific

firewall tools, including Windows Firewall and Linux Netfilter (managed using iptables), can implement

connection restrictions while maintaining access to domain controllers for authentication, DNS servers for

name resolution, and incident response systems for remote management.

Process and service restrictions prevent execution of attacker tools while maintaining essential system

functionality for business operations. Application control technologies such as Windows AppLocker, macOS

Gatekeeper, and Linux AppArmor can block the execution of unauthorized executables, scripts, and libraries

based on publisher certificates, file paths, or file hashes.

Application-Level Containment

Application-specific containment addresses compromises within specific services through targeted

restrictions that maintain operational capability while limiting attacker access. This approach recognizes

that a complete service shutdown often causes unacceptable business impact, requiring more precise

intervention that contains the threat posed by the attacker while preserving system functionality.

Web Application Firewalls (WAFs) block malicious requests to compromised web applications while

maintaining legitimate access for authorized users. Organizations can introduce application-level

containment by deploying WAF rules that detect and prevent several common attack classes. WAF tools

might include Software as a Service (SaaS) offering from Cloudflare, for example, or might be locally

deployed tools such as ModSecurity rules (for Windows and Linux web servers). WAF services can help limit

what attackers can use to attack systems, but should not be relied on as long-term defenses without

resolving underlying platform vulnerabilities.

Database access restrictions can limit queries from compromised applications or accounts to prevent data

exfiltration while preserving normal business operations. Implement query monitoring that flags unusual

patterns, such as large result sets, schema enumeration, or access to sensitive tables outside intended

access methods.  Database activity monitoring tools, including IBM Security Guardium, can block or

quarantine suspicious queries based on data volume thresholds, query complexity, or access patterns that

deviate from established baselines.

Organizations increasingly deploy AI agents with broad access to internal systems via integration

frameworks such as the Model Context Protocol (MCP), enabling automated tools to query databases,

access file systems, send messages, and execute code on behalf of users. These integrations create a

containment surface that responders should address when compromised accounts have access to AI agent

capabilities, or when the agent integrations themselves are exploited through prompt injection or other

platform vulnerabilities. Containment actions include disabling AI agent tool access and MCP server

connections, revoking the service principals or API keys that grant AI systems access to organizational data,

and monitoring AI-generated outputs for signs of data leakage through carefully crafted queries.

AI agent integrations often authenticate using service principals or API keys that are

separate from the user accounts that invoke them. Revoking a compromised user’s

credentials may not revoke the AI agent’s access to organizational data. Inventory AI

integration credentials as part of preparation activities.

Identity and Access Management Containment

Modern containment strategies center on identity as the new security perimeter, recognizing that

traditional network boundaries have dissolved in hybrid cloud, remote work, and SaaS-dominated

environments. Identity providers (IdPs) now serve as the primary control plane for containment, requiring

complex procedures for comprehensive containment, including credential revocation, token invalidation,

and session management across distributed platforms.

When addressing identity-based compromises, organizations should systematically implement containment

actions to ensure complete coverage across all authentication mechanisms that attackers might leverage to

maintain access. Start by invalidating credentials immediately, then address active sessions, and finally

implement conditional access policies that prevent re-authentication while the team investigates. In this

section, we’ll explore each of these steps in more detail, with actionable recommendations for effective

identity containment.

Contain Activity | Chapter 12 | 233

Figure 80 | Identity and Access Management Containment Steps

When containment requires creating temporary accounts (for example, to preserve

administrative access after a bulk reset or to operate an isolated system), the incident

response team should record each account in the incident documentation at creation,

including the purpose, intended lifespan, and owner, so that closure activities can review

each account for retention or removal.

Credential Revocation

Begin identity containment by invalidating compromised credentials across all authentication systems

where they exist. Reset passwords for affected user accounts via the primary identity provider, preventing

attackers from using stolen credentials. In addition to conventional user accounts, remember to address

service accounts, application accounts, and programmatic integrations that might use API keys or access

tokens for authentication.

Organizations using multiple identity systems should revoke credentials in all locations where the

compromised account exists. An account synced between on-premises Active Directory and Microsoft

Entra ID requires password resets in both systems to ensure complete containment, as synchronization

delays may create brief windows when old credentials remain valid in one environment. Similarly, revoke

credentials in any federated partner directories or connected SaaS platforms that might cache

authentication information.

Credential revocation in isolated environments depends on management connectivity that may not exist. If

the team has already cut internet access as part of containment, cloud-hosted identity providers cannot

push invalidation updates to servers that no longer reach the control plane, and local authentication caches

may keep stolen credentials valid until the cache entries expire. Plan the order of operations so that

credential revocation completes before wider network isolation, or maintain a trusted management path

that survives the isolation posture.

Active Session Termination

After invalidating credentials, force-terminate all active sessions to deny attackers access via existing

authenticated sessions that survive password changes. This is most readily accomplished using an Identity

Platform’s session revocation feature to invalidate all access tokens and session cookies for the target

account(s). Modern identity platforms often provide a revoke-all-sessions feature that invalidates session

tokens across all connected applications.

The interval between credential revocation and active session termination is a window of residual attacker

access, and the team should treat it as a measurable service-level target rather than an incidental delay. An

attacker on the VPN who retains a live session after the credentials have been reset can still initiate their

own password reset flow, enroll a new MFA factor, or establish additional persistence before sessions are

terminated. Establish an in-incident SLA with the IT team during the prepare activity so that the handoff

from the IRT to the account management team happens within a defined target, and capture actual times

during exercises to validate the target is achievable.

Session termination through the IdP only affects applications that check session validity with the identity

provider on each request. Many applications, including SaaS platforms, will cache session state locally or

issue their own session cookies that remain valid even after IdP session revocation (see the sidebar on Back-

Channel Logout: A Critical Missing Component ). For accounts with extra privileges or high-risk

compromises, it may be necessary to contact the SaaS application’s support team to request forced logout

and session invalidation at the application level.

Beyond web application sessions, terminate active connections across all authentication methods the

account might use. Disconnect any remote access sessions (e.g., VPN) via the platform management

interface, identify active connections by username, and forcibly terminate them.  For Remote Desktop

Protocol (RDP) access, use tools like qwinsta and rwinsta on Windows servers to identify and disconnect

active RDP sessions associated with the compromised account, as shown in Listing 48 . SSH connections

require identifying active sessions on target systems with who or w commands, then terminating the SSH

child processes with pkill -u username or by forcing the disconnect of specific TTY sessions.

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

Contain Activity | Chapter 12 | 235

1 Attacker SSH session

Host-based queries like qwinsta and who work for targeted investigation but become impractical across the

enterprise. A complementary approach is to query the SIEM for the pattern of session opened without

matching close , which applies equally to sessions from RDP, SSH, remote monitoring and management

(RMM) tools, and cloud consoles. Each emits a logon event and a logoff event that should pair up under

normal operation, and unpaired logons after a credential reset are a reliable signal of active sessions that

need additional intervention for containment.

For Windows RDP, Event ID 4624 with LogonType 10 marks the session open, and Event ID 4634 marks the

session close. The Splunk query in Listing 50  identifies RDP sessions that were opened without a

corresponding close event, indicating active sessions that may still be accessible to attackers after

credential revocation. SSH follows the same pattern with sshd authentication and disconnect messages, and

RMM tools emit session-start and session-end events in their own audit logs.

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

Responders can adapt the query for other SIEMs by substituting the event source, logon and logoff event

identifiers, and the correlation key (username, session ID, or token ID) to match the target session type.

Refresh Token and Persistent Credential Revocation

Refresh tokens represent a persistence mechanism that allows attackers to generate new access tokens

even after revoking active sessions and resetting passwords.  In practice, OAuth refresh tokens can have

very long lifetimes measured in months and remain valid until explicitly revoked. Responders should access

the identity provider’s token management interface to revoke all refresh tokens associated with the

compromised account, preventing attackers from requesting new access tokens using previously issued

refresh tokens.

Modern authentication protocols use various token types that each require separate revocation

consideration. OAuth deployments use access tokens (short-lived, typically 1 hour), refresh tokens (long-

lived, potentially months), and sometimes offline access tokens that enable access without user interaction.

Security Assertion Markup Language (SAML) assertions are typically short-lived but may be cached by

service providers for extended periods. JSON Web Tokens (JWTs) can be stateless and self-contained. Their

lack of a revocation feature makes revocation impossible without implementing token deny lists at each

resource server.

Table 18 | Token Types and Revocation Considerations

TOKEN TYPE TYPICAL

LIFETIME

REVOCATION METHOD PERSISTENCE RISK

OAuth Access

Token

Short (typically

1 hour)

Revoke via authorization

server API

Low: expires quickly if not

refreshed

OAuth Refresh

Token

Long

(potentially

months)

Revoke via IdP token

management

High: generates new access

tokens silently

OAuth Offline

Access Token

Long (months

or indefinite)

Revoke via IdP; may require

app-specific action

High: enables access without user

interaction

SAML

Assertion

Short

(minutes)

Expires naturally; clear SP

session caches

Medium: may be cached by

service providers

JSON Web

Token (JWT)

Variable

(configured at

issuance)

No native revocation;

requires token deny lists at

each resource server

High: stateless and self-contained

For example, when containing a compromised service account in a microservices environment using OAuth

authentication, responders should use the authorization server’s API to revoke both the access tokens

currently being used for API calls and the refresh tokens stored in the application’s configuration, then

monitor authentication logs over the next several days to verify that no new tokens are successfully issued

using the old credentials. Watch for token endpoint requests that would indicate an attacker’s attempts to

use cached credentials.

Organizations should document the token types and revocation capabilities for critical

applications during preparation activities, creating a reference guide that identifies which

tokens can be revoked centrally through the IdP and which require application-specific

revocation procedures. This documentation proves invaluable during incidents when

responders need to quickly understand whether resetting an account password will

actually terminate all attacker access or if additional token revocation steps are necessary.

Conditional Access Policy Implementation

After invalidating existing credentials and sessions, implement conditional access policies that prevent

attackers from re-authenticating while allowing legitimate users to regain access through verified channels.

Create temporary policies specific to the incident that block authentication attempts matching attacker

patterns while preserving the organization’s operational capability.

Deploy location-based restrictions that block authentication from geographic regions where the attacker

operated. For accounts accessed from known employee locations, create conditional access policies that

block sign-ins from countries or regions where the organization has no legitimate presence. While not a

comprehensive defense, this additional control can be effective when the legitimate user operates from a

known location outside the attacker’s infrastructure.

Where possible, combine geographic restrictions with device compliance requirements that allow

authentication only from managed devices enrolled in the organization’s endpoint management platform.

This can be an additional layered defense mechanism, preventing attackers on unmanaged systems from

Contain Activity | Chapter 12 | 237

accessing resources even if they obtain valid credentials again.

Risk-based conditional access policies leverage identity provider risk detection to automatically restrict

access when suspicious authentication patterns appear. Typically integrated with a Cyber Threat

Intelligence (CTI) feed, these policies adapt dynamically to emerging threats without requiring manual rule

updates. A sample decision tree for applying different controls based on risk-based conditional access is

shown in Figure 81.

Figure 81 | Risk-Based Conditional Access Policy Example

Enable account risk policies that block sign-in when the IdP detects credential leakage, impossible travel

patterns, or authentication from suspicious IP addresses known to host malicious infrastructure.  Configure

sign-in risk policies that require step-up authentication with phishing-resistant Multi-Factor

Authentication (MFA) when authentication attempts exhibit risk indicators such as unusual user-agent

strings, anomalous authentication timing, or unfamiliar device fingerprints.

Multi-Application Containment Through SSO

Single Sign-On (SSO) platforms enable simultaneous containment across connected applications through

centralized identity controls. When implemented consistently, incident responders can significantly reduce

the time required to contain widespread account compromises. Rather than logging into each SaaS

application individually to revoke access, analysts can disable the account at the IdP level to block

authentication to all SSO-connected applications that rely on the identity provider for authentication

decisions.

When disabling accounts via SSO, verify which applications use the IdP for authentication and which use

local accounts or other authentication mechanisms. Many organizations maintain hybrid authentication

where some applications federate to the central IdP while others use local credential stores that require

separate revocation actions. For example, an organization’s Salesforce instance might use Okta for SSO

authentication, but a legacy on-premises Enterprise Resource Planning (ERP) system might have local

accounts with the same username that require separate disabling through the ERP’s administration

interface.

Coordinate MFA enforcement across the environment to prevent attackers from bypassing additional

verification, even when they possess valid passwords stolen through infostealer tools. Wherever possible,

enable MFA requirement policies at the IdP level that apply uniformly to all connected applications,

ensuring a consistent security posture across the SaaS ecosystem.  During containment, escalate MFA to

phishing-resistant methods like FIDO2 security keys, which cannot be compromised by browser-in-the-

middle phishing attacks, and block SMS-based or Time-Based One-Time Password (TOTP) authenticator

apps, which are more susceptible to attacker interception.

Monitor for authentication synchronization delays between the IdP and connected applications,

recognizing that some applications cache authentication decisions or maintain local session state that might

preserve access briefly after the IdP disables accounts centrally. Enterprise SaaS applications typically

check authentication status with the IdP frequently (every few minutes to hours), but some legacy or

custom applications might only validate credentials during initial login and maintain sessions indefinitely

thereafter. Track timing between account disabling actions and when attacker activity ceases, documenting

synchronization delays that inform future containment timing decisions.

Session Management Across Hybrid Environments

Users maintain active sessions across on-premises systems, cloud services, and remote access solutions

simultaneously, any of which provide attackers with persistent access after responders implement primary

containment actions. Coordinate session termination across all these environments to prevent attackers

from maintaining access through alternative authentication pathways.

For VPN access, identify active sessions through the VPN concentrator’s management interface and forcibly

disconnect them by username or session ID. Many enterprise VPN solutions provide administrative

interfaces for viewing active connections and terminating specific user sessions. After disconnecting active

sessions, implement access control list restrictions that temporarily block the account from establishing

new VPN connections while the investigation continues.

Remote Desktop Protocol connections require identifying active sessions on each accessible Windows

server or workstation. Use PowerShell to query session information across multiple systems simultaneously

using Invoke-Command and qwinsta as shown in Listing 51 . Terminate identified sessions using the rwinsta

command, then verify disconnection by querying the session state again.

Listing 51 | Enumerate Active RDP Sessions Across Multiple Servers

PS C:\> Invoke-Command -ComputerName server01,server02,server03 -ScriptBlock {qwinsta}

ComputerName : server01

SESSIONNAME       USERNAME        ID  STATE   TYPE        DEVICE

>console          administrator    1  Active

rdp-tcp#12       jsmith           2  Active

rdp-tcp#13       guest            3  Disc

Contain Activity | Chapter 12 | 239

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

Browser session management becomes critical as many SaaS applications rely on persistent browser

sessions stored in cookies that may survive credential resets and continue providing access until they expire

naturally. Identity provider platforms may increment session token versions, invalidating all issued session

cookies by changing the token signing key or session identifier format.  For example, Microsoft Entra ID’s

revoke refresh tokens  action increments the user’s session token version, invalidating all previously issued

cookies and forcing re-authentication across all applications on the next request.

Coordinate session termination timing across all these mechanisms to avoid sequential revocation that

alerts attackers to defensive actions and provides time to establish additional persistence. Create a checklist

of session termination actions for the environment and execute them simultaneously during a planned

containment window, preferably within a limited timeframe that gives attackers minimal opportunity to

respond.

Create an environment-specific session termination checklist during preparation. The

number of session types in a modern environment (VPN, RDP, browser sessions, OAuth

tokens, refresh tokens, mobile app sessions) is easy to underestimate under pressure, and

a missed session type can leave attackers with persistent access after containment.

BACK-CHANNEL LOGOUT: A CRITICAL MISSING COMPONENT

An important feature missing from many identity platforms is back-channel logout  support. Back-

channel logout allows an identity provider (IdP) to notify all connected service providers (SPs) when a

user logs out, ensuring that all active sessions are terminated across the ecosystem. This capability is

crucial for mitigating the risks of authorization sprawl, as it prevents attackers from maintaining

access through lingering sessions after a user logs out.

Today, few identity providers support back-channel logout, largely due to a lack of integration with

application service providers. When application service providers do provide IdP logout support, it is

often a proprietary implementation that only works with specific IdPs, creating an NxM integration

problem (where N is the number of supported service providers and M is the number of supported

identity providers). This fragmentation makes it impractical for organizations to achieve

comprehensive session termination across all applications.

Support for invalidating sessions for all service providers through the IdP should be a stated

requirement in vendor Requests for Proposals (RFPs) and procurement documents, as well as for any

integrated application service providers. Mandating compliance with the draft Internet Engineering

Task Force (IETF) standard Global Token Revocation  will help drive industry adoption of this

important security feature to better respond to authorization sprawl attacks.

EVIDENCE COLLECTION DURING CONTAINMENT

During containment activities, we also collect evidence to support subsequent investigation, eradication,

and recovery efforts. After isolating affected systems, we can collect evidence to understand attacker

tactics, techniques, and procedures (TTPs), identify persistence mechanisms, and reconstruct the timeline

of compromise.

In this section, we’ll explore objectives for data collection that support the organization’s needs for a

valuable response effort.

EVERY STEP IS FOR DATA COLLECTION

In the PICERL and NIST SP 800-61 models, the containment step is when the incident response team

first lays hands on the affected systems to isolate them, giving us the first chance to collect data. As a

result, most guides and playbooks focus heavily on data collection during the containment phase,

where analysts can collect volatile data and preserve evidence.

In the DAIR model, this logic still applies. We isolate the affected systems to prevent further damage

and to gain as close to unfettered access to the compromised system as possible. However, we also

recognize that every step of the incident response process is an opportunity to collect data. Each

waypoint in the DAIR model serves as both a response action and a data collection opportunity. Your

collection strategy should adapt to the specific goals and constraints of each phase.

• Prepare: Collect baseline configurations, network topologies, and asset inventories. Document

communication plans and escalation procedures. This foundational data enables effective

comparison when incidents occur.

• Identify: Gather initial event data, including logs, alerts, and user reports. Focus on establishing

timeline markers and impact scope. Network analysts should prioritize flow data and DNS

queries. Host analysts need process execution and local logging data.

• Verify/Triage: Collect evidence to confirm incident validity and assess risk impact. Decision

makers need executive-level summaries with clear risk classifications. Technical teams require

detailed indicators to support verification activities.

• Scope: Expand data collection to understand incident breadth. Analysts need lateral movement

indicators, affected system inventories, and compromise timelines.

• Contain: Collect volatile data including memory captures, active network connections, and

running processes. Consider full disk capture (if beneficial for your organization), local logging

data, registry details, and other system configuration data. Collect adversary behavior data while

maintaining operational security, where possible. Preserve evidence of attacker tactics for

eradication and recovery analysis.

• Eradicate: Focus on collecting data about attacker persistence mechanisms and tools.

• Recover: Collect vulnerability assessment data, patch deployment logs, and control

implementation verification. Document root cause analysis findings and remediation

effectiveness metrics.

The DAIR model’s iterative nature means data collected in one phase directly informs activities in

other phases. Evidence gathered during containment may reveal new systems requiring scoping.

Contain Activity | Chapter 12 | 241

Eradication findings often expose additional preparation needs. Recovery analysis feeds back into

improved detection capabilities. This interconnected approach ensures that each data collection

effort contributes to both immediate response effectiveness and long-term security improvements,

creating a comprehensive intelligence picture that evolves throughout the incident lifecycle.

Prioritized Collection

Evidence collection during containment requires prioritization based on volatility and investigative value to

ensure critical information is preserved before containment actions modify system state or destroy

transient data. Volatile data, including memory dumps, active network connections, and running processes,

deserves the highest priority because this information disappears when systems are powered down or

rebooted, or through natural attrition over time.

Volatile Data Collection

Memory analysis can reveal running malware, decrypted credentials in process memory, and active network

connections that might not appear in logs. Capture memory from compromised systems before

implementing containment actions that would alter the system state or power cycle the machine. For

example, memory acquisition tools like WinPMEM or Linux Memory Extractor (LiME) can acquire a memory

dump from the compromised web server before isolating it to a quarantine VLAN, preserving evidence of

the web shell’s in-memory configuration and active command-and-control sessions that won’t survive a

network disconnect.

PRIORITIZED COLLECTION: AN ORGANIZATIONAL-SPECIFIC APPROACH

In the DAIR model, we advocate for a two-step approach to evidence collection during containment:

isolate first, then collect data. This is based on many years of collective experience, where data

collected prior to containment may be incomplete or misleading due to attacker interference, and

where containment actions themselves can destroy critical evidence if not managed carefully, or may

trigger an attacker response in advance of containment activities.

However, the specific prioritization of evidence collection should be tailored to the organization’s

unique environment, threat landscape, and investigative goals. Organizations should weigh the loss of

possible evidence due to containment actions versus the risk of allowing attackers to maintain access

while evidence is collected.

Consider, for example, the output of Get-NetTCPConnection on a compromised Windows host, shown

in Listing 52 . This command will show active and listening TCP connections, including those

established by attacker tools.

Listing 52 | NetTCPConnection Output on Compromised Host

PS C:\> Get-NetTCPConnection

LocalAddress     LocalPort RemoteAddress    RemotePort State

------------     --------- -------------    ---------- -----

::               445       ::               0          Listen

192.168.171.142  33318     151.101.118.172  80         TimeWait

192.168.171.142  33179     13.107.5.91      443        TimeWait

192.168.171.142  33174     172.183.7.192    443        Established

192.168.171.142  27288     192.168.1.140    4444       Established

192.168.171.142  1565      162.159.142.9    80         Established

As an investigative tool, Get-NetTCPConnection provides valuable insight into ongoing attacker

communications. However, if the incident response team immediately isolates the host from the

network, these active connections will be terminated and the evidence of ongoing communications

will be lost if not captured through an external data source (such as Network Flow logs, Sysmon

network connection event logs, or other Network Detection and Response tools).

Organizations should evaluate their specific environment to determine which evidence sources are

most critical to preserve during containment, and weigh the risks of losing volatile data against the

need to quickly isolate compromised systems. Organizations without alternate data sources for

network connections or other volatile data may prioritize data collection before isolation, while those

with robust logging and monitoring systems can prioritize isolating of systems to prevent further

attacker activity.

Persistent and Log-Based Evidence

System artifacts, including registry hives, event logs, and temporary files, provide insight into attacker

activities and persistence mechanisms with less time sensitivity than volatile data. These artifacts offer a

more permanent record of compromise that can survive system restarts and most containment actions,

though some data, such as certain cache files or temporary directories, may be cleared during normal

system operations. Collect Windows registry hives to identify persistence mechanisms, event logs to

establish timeline data, and browser cache to reveal attacker reconnaissance activities.  Prefetch files,

ShimCache entries, and AmCache records provide execution history that helps reconstruct the use of the

attacker’s tools even after the malicious files are deleted.

Network evidence, including packet captures, NetFlow data, and firewall logs, reveals communication

patterns and data movement across the environment. This evidence helps analysts understand the scope of

data exfiltration, identify command-and-control infrastructure, and discover additional compromised

systems based on lateral movement patterns. Full packet captures provide the most detail but consume

significant storage, while Network Flow logs (including NetFlow logs, VPC Flow Logs, and similar log types)

offer a lighter-weight alternative that still reveals connection patterns, data volume transferred, and

communication timing details.

Application data, including web server logs, database transaction logs, and application-specific artifacts, can

also provide useful insights for the investigation. While network evidence shows communication patterns,

application logs provide context on which data attackers accessed, modified, or exfiltrated. This evidence

provides crucial information for impact assessment, regulatory notification requirements, and

understanding attacker objectives.

CLOUD CONTAINMENT

Attackers exploit cloud misconfigurations that create containment challenges distinct from traditional on-

premises compromises. Cloud containment presents unique challenges due to several factors, including the

shared responsibility model for security, the introduction of cloud control-plane access vectors as an attack

surface, and the complications posed by multitenancy and misconfigurations. While many of the

conventional containment principles still apply, cloud environments require adapted strategies that

leverage cloud-native controls and account for the unique characteristics of cloud infrastructure.

Contain Activity | Chapter 12 | 243

In this section, we’ll cover the cloud security demarcation that determines which containment actions the

customer controls; the core containment objectives specific to cloud environments; and techniques for

identity-first containment, network isolation, resource tagging, IaaS termination protection, SaaS platform

containment, and third-party integration containment.

Cloud Security Demarcation

Cloud service containment requires understanding the shared responsibility model that defines security

boundaries between cloud service providers and customer organizations. For Infrastructure as a Service

(IaaS) cloud services, providers typically manage infrastructure security, including physical hardware,

hypervisor security, and network infrastructure protection, while customers remain responsible for identity

and access management, data encryption, application security, and operating system patching. By contrast,

Software as a Service (SaaS) providers manage nearly all infrastructure and application security, leaving

customers responsible primarily for identity management, data access authorization, and user access

controls. Platform as a Service (PaaS) offerings fall somewhere between the two, with providers managing

the underlying platform security while customers handle application-level security and data protection.

The division of responsibilities between what the cloud customer and what the cloud provider are

responsible for is known as the cloud security demarcation . This separation of responsibilities determines

which containment actions the cloud customer can implement directly and which require escalation to the

cloud provider’s support teams.

For example, if attackers exploit a vulnerability in the underlying hypervisor or physical network

infrastructure, the cloud customer likely cannot directly contain the threat and needs to engage the cloud

provider’s security team, while compromised Identity and Access Management (IAM) credentials or

misconfigured user account access are within the cloud customer’s containment authority. Understanding

this demarcation before incidents occur enables faster, more effective containment by clarifying which

team controls each potential containment mechanism. A summary of common cloud security demarcation

responsibilities is shown in Figure 82.

Figure 82 | Cloud Security Demarcation Responsibility Summary

CLOUD SERVICE AND RESPONSIBILITY DEFINITIONS

All cloud providers operate under a shared responsibility model for security, in which the cloud

provider is responsible for certain aspects, and the cloud customer is responsible for others. The line

of responsibility between the provider and the customer can be complex, changing from provider to

provider and within different products from the same provider.

Cloud services are often categorized as Infrastructure as a Service (IaaS), Platform as a Service (PaaS),

and Software as a Service (SaaS). IaaS services are often the lowest-level cloud services, allowing

customers to leverage cloud-provided storage, networking, and hardware to run Linux or Windows

systems. Comparatively, PaaS enables the cloud customer to focus on the application, content, and

data while the cloud provider manages the underlying operating system and often the services to

support the application (databases, web servers). SaaS services focus on the upper-layer application

functionality and data, such as Microsoft 365, Zoom, Slack, Salesforce, etc., where the cloud provider

provides all other functionality.

Understanding the distinguishing characteristics of IaaS, PaaS, and SaaS is important for incident

responders. Cloud security demarcation helps us differentiate our responsibility for incident

response from the cloud provider’s. However, the broad service categories are not always sufficient

to show where the customer’s responsibility ends for the service.

Consider the AWS services for Elastic Compute Cloud (EC2) and Lightsail. EC2 allows users to

provision servers running a given Amazon Machine Image (AMI), then add the services and

applications to power the desired functionality. In this case, Amazon’s security responsibility ends

with the hardware, storage, and network equipment. The cloud user’s responsibility starts with the

Linux or Windows operating system. Compared to other services, Lightsail allows customers to

launch similar VMs by selecting a blueprint such as WordPress, Node.js, Drupal, and more options.

While Lightsail might seem to match the functionality of a SaaS platform, where the blueprint

provides the necessary software, Amazon takes no responsibility for the security of the operating

system, applications, services, or data. This can be non-intuitive for cloud customers, leading to

instances being deployed and populated with data, left unmaintained, exposing the platform to

vulnerabilities due to a lack of patch management and monitoring.

Fundamentally, it’s important to understand where the security demarcation lies for the products

used by your cloud provider. Begin by enumerating the cloud functions you use and reviewing the

security documentation for these products to understand where your security responsibilities begin.

Do not rely on broad IaaS, PaaS, or SaaS labels to determine security responsibility. Verify

the security demarcation for each specific product, as services that appear to offer

managed functionality may still leave full operating system and application responsibility

with the customer.

Cloud Containment Objectives

The core containment objectives for cloud systems mirror traditional incident response goals: isolate the

compromised resource to prevent further malicious activity, collect evidence for investigation and threat

intelligence, and preserve forensic data for recovery and remediation activities. Cloud platforms provide

several native features that facilitate these objectives, including flexible tagging systems to mark resources

as under investigation, snapshot capabilities to capture system state, and termination protection

mechanisms to prevent accidental destruction of evidence. Teams should leverage these cloud-native

features rather than attempting to replicate on-premises containment procedures that may not translate

effectively to cloud environments.

Identity-First Containment

Identity-first containment takes priority in cloud environments because credentials represent the most

common persistence and lateral movement mechanism for cloud-focused attackers. Compromised IAM

user access keys, service account keys, OAuth tokens, and refresh tokens provide attackers with persistent

access that survives traditional network-based containment measures. Disable compromised access keys

Contain Activity | Chapter 12 | 245

immediately to prevent their use for API calls or console access; terminate active user sessions across all

applications; revoke OAuth refresh tokens that could generate new access tokens; and rotate service

principal credentials used by automated systems. Consider the operational impact of identity-based

containment on downstream automation and business processes that depend on the affected credentials.

For example, when rotating a compromised service account key that authenticates a critical data processing

pipeline, coordinate with application teams to update the credential in all systems that use it, implement the

rotation during a maintenance window if possible, and have rollback procedures ready in case the

credential update causes unexpected failures. Document which applications and automation workflows use

each privileged identity before incidents occur, enabling rapid assessment of containment impact when

those identities are compromised.

Network Isolation Containment

Network isolation in cloud IaaS environments is implemented through multiple complementary controls

that prevent further compromise while preserving evidence for investigation. Remove compromised

instances from production scaling groups and load balancers to prevent them from receiving user traffic

while keeping the instances running for forensic analysis.  Modify security group rules, network Access

Control Lists (ACLs), or move the instance to a pre-configured isolation Virtual Private Cloud (VPC)

dedicated to incident response activities, where the team controls all network ingress and egress. Enable

termination protection and deletion protection on compromised resources to prevent accidental or

malicious destruction by other administrators who might not be aware of the ongoing investigation.

Consider using cloud provider snapshot features to create point-in-time copies of storage volumes and

virtual machine states. These features make it straightforward to preserve the compromised system’s exact

configuration for detailed forensic analysis while the team continues containment activities. Always

consider the cost-benefit analysis of snapshot storage costs versus the investigative value of preserving the

system state, especially for large-scale incidents involving many compromised resources.

Resource Tagging for Containment Visibility

Cloud platforms provide robust resource tagging capabilities that facilitate clear identification of

compromised assets during containment and throughout the investigation lifecycle. These metadata tags

serve multiple purposes: they clearly mark resources as under investigation to prevent accidental

modification or deletion, enable automated policy enforcement through tag-based access controls, and

provide audit trails for compliance and post-incident review.

Establish consistent tagging conventions before incidents occur to ensure all team members apply tags

uniformly during high-pressure containment activities. Common tagging schemes group into four broad

categories, shown in Table 19. Multiple tags can be applied to a single resource to provide comprehensive

context, and tags can be updated as the incident progresses through different phases.

Table 19 | Incident Response Tagging Schemes

CATEGORY PURPOSE EXAMPLE TAG

Status indicator Mark resource as under IR control Status:Quarantined

Case identifier Link resource to incident ticket IR-Case:2026-001

CATEGORY PURPOSE EXAMPLE TAG

Containment date Record containment timestamp for

audit review

ContainedDate:2025-10-27

Analyst owner Identify responsible IRT staff member IR-Owner:jsmith@company.com

Resource tags enable practical operational benefits during containment activities. Use tags to create filtered

views in cloud consoles that show only compromised resources; configure automated alerts when tagged

resources are accessed or modified; implement tag-based access controls that restrict who can start or

terminate quarantined instances; and generate reports for management on containment status across the

environment. Some organizations implement automation that prevents deletion of resources tagged with

incident response markers until the case is formally closed and documented.

For example, when containing a suspected compromised EC2 instance in AWS, apply multiple resource tags

to provide comprehensive tracking, as shown in Table 20. Configure AWS Resource Groups to dynamically

collect all resources tagged with Status:UnderInvestigation, providing a single dashboard view of all

contained assets across the AWS environment. Implement IAM policies that prevent anyone except incident

responders from terminating instances tagged with Status:UnderInvestigation, protecting evidence from

accidental destruction during investigation.

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

IR-Purpose:Quarantine and IR-Case:2026-001, facilitating cleanup after incident resolution and preventing

these temporary configurations from lingering indefinitely in production environments.

Tagging is only effective as a containment signal when the organization controls who can

change the tags. An attacker who retains cloud console access can simply remove the

Status:UnderInvestigation tag to hide a compromised resource from IR dashboards, or

relabel it to look like a routine production asset.

Define a RACI for tag management during the prepare activity that identifies which team members can

Contain Activity | Chapter 12 | 247

apply, modify, or remove incident response tags, and implement that RACI as an IAM policy that restricts

write access to those specific tag keys to incident response roles only.

Configure tag change event logging to record to a separate, tamper-resistant audit

destination so that unauthorized modifications are visible even if the attacker suppresses

logging elsewhere.

IaaS Termination Protection

Enabling termination protection on contained IaaS cloud resources prevents accidental deletion of critical

evidence during investigation, creating a safety mechanism that requires explicit two-step confirmation

before anyone can destroy potentially valuable forensic data. Cloud administrators and automation systems

often have the ability to terminate instances as part of routine operations, creating a risk that someone

unfamiliar with the ongoing investigation might delete a contained system, thinking it’s simply unused or

misconfigured. Termination protection is a technical control that enforces evidence preservation via the

cloud provider’s API, requiring authorized personnel to first disable protection before terminating the

resource.

For example, when a compromised EC2 instance in AWS is detected, enable termination protection

immediately via the AWS console or CLI to prevent any user or automation from deleting the instance until

protection is explicitly removed, as shown in Listing 53. This protection persists even if someone has IAM

permissions that would normally allow instance termination, providing defense against both accidental

deletion by administrators and intentional deletion by attackers who might have compromised cloud

credentials. Azure provides similar capabilities through deletion locks that prevent resource deletion until

the lock is removed, while Google Cloud Platform offers Compute Engine instance deletion protection that

can be enabled during containment operations.

Listing 53 | AWS CLI Command to Enable Termination Protection

$ aws ec2 modify-instance-attribute --instance-id i-1234567890abcdef0 --disable-api-termination

1 Replace i-1234567890abcdef0 with the EC2 instance ID.

Table 21  provides equivalent commands for enabling termination or deletion protection across cloud

providers.

Table 21 | Cloud Termination Protection Quick Reference

Enable deletion protection

AWS aws ec2 modify-instance-attribute --instance-id <instance-id> --disable-api-termination

Azure az lock create --name IR-Preserve --lock-type CanNotDelete --resource-group <rg>

--resource-name <vm> --resource-type Microsoft.Compute/virtualMachines

GCP gcloud compute instances update <instance> --deletion-protection --zone <zone>

Verify protection status

AWS aws ec2 describe-instance-attribute --instance-id <instance-id> --attribute

disableApiTermination

Azure az lock list --resource-group <rg> --resource-name <vm> --resource-type

Microsoft.Compute/virtualMachines

GCP gcloud compute instances describe <instance> --zone <zone>

--format="value(deletionProtection)"

Termination protection extends beyond compute instances to other critical resources, including Elastic

Block Storage (EBS) volumes, snapshots, databases, and network configurations that contain evidence or

support ongoing investigation. Apply protection to EBS volumes attached to contained instances to prevent

their deletion even if the instance itself is somehow terminated, and enable snapshot protection to preserve

exact copies of compromised systems throughout the investigation. Document which resources have

termination protection enabled in incident tracking systems, establishing clear procedures for removing

protection only after formal evidence preservation is complete and legal hold requirements are satisfied.

When IT or application stakeholders insist on terminating a compromised instance before the investigation

is complete, a clone-then-terminate pattern preserves most of the evidence without blocking their request.

A GuardDuty-triggered (or equivalent) Lambda function can clone the affected instance, including its

attached storage, into a separate forensic AWS account that only the incident response team can access,

producing a full-fidelity copy of disk state for later analysis. Network-connected processes and volatile

memory content are lost during the clone, so the IRT should still perform RAM collection on the original

instance before allowing termination, but persistent artifacts such as filesystem contents, event logs, and

installed binaries remain available in the cloned copy. This pattern works equally well in Azure (using Event

Grid and Azure Functions to snapshot managed disks into a forensic subscription) and Google Cloud (using

Eventarc or Pub/Sub triggers to clone persistent disks into a separate project).

SaaS Platform Containment

SaaS platform containment differs fundamentally from IaaS containment because organizations lack direct

access to the underlying systems and can only leverage containment capabilities exposed by the SaaS

provider through its administrative interfaces. While IaaS environments grant organizations control over

virtual machines, network configurations, and security groups, enabling teams to implement custom

containment measures, SaaS platforms provide only the containment features built into their administrative

consoles and APIs. This limitation requires adapting containment strategies to work within provider-defined

boundaries, often accepting less granular control than organizations would have in self-managed

infrastructure.

Identity and session containment take the highest priority in SaaS environments, where organizations

cannot directly access or isolate the underlying infrastructure. Reset passwords for compromised user

accounts immediately to invalidate current credentials, or set temporary random passwords that prevent

both attackers and legitimate users from accessing the account until the team completes the investigation.

Revoke all active sessions and refresh tokens to force re-authentication, ensuring that password resets

actually terminate attacker access rather than leaving active sessions that survive credential changes. For

service principals and application accounts, rotate API keys, client secrets, and OAuth credentials that

authenticate automated integrations and workflows.

Consider whether to disable accounts entirely or use platform-specific freeze features that preserve data

while blocking sign-in, choosing based on whether the team needs to maintain access to the account’s data

for investigation or can afford a complete lockout. For example, when containing a compromised Microsoft

Contain Activity | Chapter 12 | 249

365 administrator account, immediately reset the password through the Microsoft 365 admin center, use

the revoke sessions feature to invalidate all active authentication tokens forcing the user to re-authenticate

everywhere, disable the account to prevent any sign-in attempts, and rotate the credentials for any service

principals or application registrations that the administrator may have created, documenting each action

with timestamps for incident timeline reconstruction.

Third-Party Integration Containment

Integration and automation containment prevent compromised accounts from maintaining persistent

access through third-party applications and automated workflows that often survive credential resets.

Disable third-party applications that the compromised account authorized, including OAuth-connected

apps, browser extensions, and mobile applications that maintain their own authentication tokens. Review

and disable automation rules in platforms that could exfiltrate data or perform unauthorized actions using

the compromised account’s permissions.  Revoke outgoing webhooks that may send sensitive data to

attacker-controlled endpoints, disable Continuous Integration/Continuous Deployment (CI/CD)

deployment keys that could allow code injection into production systems, and invalidate API tokens used to

authenticate programmatic access to the SaaS platform.

After containment, replace integration credentials with new secrets and re-authorize only legitimate

integrations after verifying their configuration. For example, when investigating a compromised Slack

workspace administrator account, audit the workspace’s installed apps and custom integrations, and disable

any unfamiliar OAuth applications (especially those requesting broad permissions, such as read all messages

or access all channels ). Remove webhook configurations that send data to external URLs not expressly

authorized by the organization. Revoke any API tokens created by the compromised account, and review bot

users for unauthorized automation that might persist after the human account is disabled.

WHEN LEGITIMATE APPS LOOK LIKE COMPROMISE

The Counter Hack team and I were working on a Microsoft 365 security assessment when one of the

analysts discovered an application with broad permissions: read and send mail, access all calendar

events, and read files across SharePoint sites. When we asked, no one on the security team

recognized the application. It looked like an illicit consent grant  attack, where an attacker tricks a

user into authorizing a malicious application with excessive permissions. [5]

Our security assessment

quickly transitioned into an incident response investigation.

After investigation, the application in question turned out to be a Customer Relationship

Management (CRM) tool feature added by the sales team several months earlier. A salesperson clicked

through the OAuth consent prompt without reading the permissions, and the application had been

quietly syncing sensitive account data ever since. Not necessarily malicious, but definitely a risk and a

concern for my customer’s security team.

Figure 83 | Entra ID Application Consent Grant

Mobile apps and third-party integrations often request broad permissions that look alarming during

an investigation. Without a baseline of authorized applications, you waste time investigating

legitimate access, or worse, miss actual malicious grants hiding among dozens of legitimate ones.

Enumerate authorized applications from identity providers such as Microsoft Entra ID, Google

Workspace, or Okta as a preparation activity. In Microsoft Entra ID, the Enterprise applications pane

lists all applications with delegated or application-level permissions, including the permissions

granted and which users consented, as shown in Figure 84 . Alternatively, use the Microsoft Graph

PowerShell module to list all OAuth consent grants across the tenant, as shown in Listing 54.

Contain Activity | Chapter 12 | 251

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

During containment, compare discovered app permissions against this inventory to quickly

distinguish legitimate integrations from unauthorized access by attackers. This enumeration step can

save significant time during an investigation.

CONTAINMENT CHALLENGES

Modern environments present unique containment challenges that require adapting traditional isolation

techniques to new technologies, architectural patterns, and operational models. In this section, we’ll

examine four areas where traditional containment approaches fall short: cloud and hybrid environments,

encrypted communications that limit inspection, remote-worker environments beyond the corporate

perimeter, and modern attack vectors that extend beyond traditional host compromise.

Cloud and Hybrid Environments

Cloud infrastructure requires fundamentally different containment approaches that leverage cloud-native

controls and account for the ephemeral nature of cloud resources, where traditional network-based

isolation may be impossible or ineffective.

API-Based Isolation

API-based isolation using cloud provider APIs to modify security groups, network ACLs, or IAM policies

provides rapid, programmatic containment that can be automated and applied at scale.  Use AWS Security

Groups to block all inbound and outbound traffic to a compromised EC2 instance, Azure Network Security

Groups (NSGs) to quarantine virtual machines, or Google Cloud Platform (GCP) firewall rules to isolate

compute instances. This approach enables containment through infrastructure-as-code tools like

Terraform or CloudFormation, allowing teams to version control containment procedures and execute them

consistently across hundreds of cloud resources. For example, use the Azure CLI to create a quarantine NSG

and attach it to a compromised virtual machine’s network interface, denying all traffic except SSH access

from a specific jump box IP address. This quarantines the instance while maintaining incident response

access for investigation, as shown in Listing 55.

Listing 55 | Azure CLI Command Example for Network Isolation Containment

$ az vm show --name web-prod-01 -g rg-production-eastus2 --query

"networkProfile.networkInterfaces[0].id" -o tsv 1

/subscriptions/e7b3c1d9-a842-4f56-b6d1-8a3e5f902c4d/resourceGroups/rg-production-

eastus2/providers/Microsoft.Network/networkInterfaces/web-prod-01-nic

$ az network nsg create --name IR-Quarantine-2025-042 -g rg-production-eastus2 -o none 2

$ az network nsg rule create --nsg-name IR-Quarantine-2025-042 -g rg-production-eastus2 --name

AllowSSH-IR --priority 100 --direction Inbound --access Allow --protocol Tcp --destination-port

-ranges 22 --source-address-prefixes 198.51.100.10/32 -o none 3

$ az network nsg rule create --nsg-name IR-Quarantine-2025-042 -g rg-production-eastus2 --name

DenyAllOutbound --priority 100 --direction Outbound --access Deny --protocol '*' --destination

-port-ranges '*' --source-address-prefixes '*' --destination-address-prefixes '*' -o none 4

$ az network nic update --name web-prod-01-nic -g rg-production-eastus2 --network-security-group

IR-Quarantine-2025-042 -o none 5

1 Identify the network interface attached to the compromised virtual machine.

2 Create a quarantine NSG in the same resource group as the compromised VM.

3 Allow inbound SSH access only from the incident response team’s jump box IP address (priority 100 overrides the default

DenyAllInBound rule).

4 Deny all outbound traffic, overriding the NSG’s default AllowInternetOutBound rule to isolate the instance.

5 Attach the quarantine NSG to the compromised VM’s network interface, replacing any existing NSG association.

Serverless Containment

Serverless containment addresses unique challenges posed by compromised Lambda functions, container

instances, or other serverless compute resources that lack traditional network presence or persistent state.

Serverless functions execute on demand in isolated runtime environments, making traditional network

isolation ineffective because the next function invocation may run on completely different infrastructure.

Contain Activity | Chapter 12 | 253

Instead, disable event triggers that invoke the compromised function where possible. Preserve the

serverless function’s code, replacing it with code that returns an access denied response and logs access

attempts for further data collection. We include a Node.js example for AWS Lambda in Listing 56  and

example deployment instructions in Listing 57.

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

% aws --profile jwright lambda update-function-code --function-name lambda-function-to-log-and-

disable --zip-file fileb://function.zip 2

1 Compress the deny-and-log function code into a ZIP file for deployment.

2 Update the AWS Lambda function code to replace the specified function with the deny-and-log implementation.

The same deny-and-log containment pattern applies to Azure Functions and Google Cloud

Functions. For Azure Functions, update the function code using az functionapp deployment

source config-zip  and monitor contained invocations through Application Insights. For

Google Cloud Functions, deploy replacement code with gcloud functions deploy  and

monitor invocations through Cloud Logging.

Multi-Cloud Coordination

Multi-cloud coordination becomes critical when incidents span multiple cloud providers with different

containment capabilities, API interfaces, and security models. Each cloud provider offers distinct isolation

mechanisms with varying capabilities, where AWS security groups operate differently from Azure NSGs or

GCP firewall rules, requiring incident responders to understand the differences and adapt containment

strategies to platform-specific features.

Hybrid and multi-cloud incidents often exceed the capacity of the standing incident response team, both in

headcount and in platform-specific expertise. Cloud administrators already hold the tooling access, IAM

permissions, and operational familiarity needed to execute containment actions quickly, and should be

pulled into the incident response structure as co-opted IRT members rather than treated as an external

team receiving tickets. Capture this co-option pathway during the prepare activity, including on-call

rotations, authorization scope, and the communication channels cloud administrators will use while

operating under IR direction.

Table 22 | Multi-Cloud Containment Quick Reference

CONTAINMENT

ACTION

AWS AZURE GCP

Network

Isolation

Security Groups,

Network ACLs

Network Security Groups

(NSGs)

VPC Firewall Rules

Identity

Containment

IAM policy modification,

access key disabling

Entra ID account

disabling, conditional

access

Cloud IAM policy binding

removal

Snapshot/Eviden

ce Preservation

EBS snapshots, AMI

creation

Managed disk snapshots,

VM capture

Persistent disk snapshots

Termination

Protection

Instance termination

protection (disable-api-

termination)

Resource deletion locks Instance deletion

protection

Encrypted Communications

Pervasive network encryption complicates traditional containment strategies by obscuring attacker activity.

While widespread network cryptography has significantly improved the overall security of modern systems,

it has also created new opportunities for threat actors to use encryption as an evasion technique to bypass

network-based detection and containment controls.

Transport Layer Security (TLS) interception is particularly valuable to organizations, enabling analysts to

inspect encrypted communications from attackers during active incidents. Where possible, organizations

should implement TLS inspection proxies that decrypt, inspect, and re-encrypt traffic using trusted

certificates deployed to managed endpoints. Once deployed, restrict egress network access via TLS to only

those proxies, ensuring that all encrypted traffic passes through inspection points. Log and investigate any

TLS connections that attempt to bypass the interception proxies, as they may represent attempts by

attackers to evade analysis.

The use of TLS intercept proxies requires careful implementation to avoid breaking

legitimate business applications that use certificate pinning, while maintaining the ability to

Contain Activity | Chapter 12 | 255

analyze malicious traffic patterns during containment activities. Balance security benefits

against privacy concerns and potential application compatibility issues, documenting clear

policies about what traffic will be inspected and ensuring legal review and authorization of

monitoring practices.

Remote Worker Environments

Distributed workforces create unique containment challenges that extend organizational security

boundaries far beyond traditional corporate networks into uncontrolled home networks, personal devices,

and diverse geographic locations.

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

Each row in the table should be backed by a documented process owned by a named team. Containment of

a remote worker is rarely a single-action step. Practical details such as who ships the replacement device,

how MDM selectively wipes corporate data, and which VPN policy template is applied take too long to work

out during an active incident. Capture these procedures during the prepare activity and exercise them in

tabletop scenarios.

Network Visibility and Endpoint Controls

Network visibility limitations arise when remote devices operate on home networks outside organizational

control, preventing traditional network-based containment and monitoring techniques. Organizations lack

visibility into the network infrastructure between remote devices and the internet, cannot control which

devices connect to the same home network, and cannot implement network-based isolation when those

home routers are owned by internet service providers or employees.

For remote work environments, organizations should shift containment strategies toward endpoint-focused

controls rather than network-based approaches. This is often implemented using EDR isolation features to

quarantine remote devices while preserving the communication channel required for incident response.

Personal Device Contamination

Personal device contamination requires containment strategies that distinguish between corporate and

personal data while respecting employee privacy boundaries and legal restrictions. Many organizations

permit or require employees to use personal devices for work through Bring Your Own Device (BYOD)

programs, creating scenarios in which containment actions might affect personal device use.

For BYOD programs, organizations should implement Mobile Device Management (MDM) or Mobile

Application Management (MAM) solutions that can selectively manage and eliminate corporate data, revoke

access to company resources, or isolate business applications without affecting personal information.

Document clear policies about the extent of organizational control over personal devices and ensure

employees understand containment capabilities before incidents occur.

Home Network Compromise

Home network compromise scenarios present complex ethical and legal considerations when attackers

pivot from compromised corporate devices to family systems owned by non-employees. This pivot is largely

a consequence of inadequate remote-worker configuration rather than an inherent risk of remote work.

For example, a managed device with an enforced always-on VPN, strict host firewall, and no routable path

to the local (residential) subnet cannot scan the household network in the first place. A work laptop that can

see a family member’s network-attached storage already had a path suitable for data exfiltration regardless

of attacker presence. Where the controls are weaker, attackers who compromise a corporate laptop on a

home network might scan for other devices, such as personal computers, smart home systems, or family

members' devices, creating potential liability and notification obligations when employee family members

become collateral victims.

Organizations should determine in advance which notifications they will provide to employees about home

network risks, what assistance they will offer to help secure personal systems, and what coordination may

be necessary with employees' households during containment activities. These decisions require legal

review and clear communication with employees before incidents occur, and should be paired with a

remote-worker configuration review that eliminates the underlying pivot paths wherever practical.

Establish policies for home network compromise scenarios before an incident occurs.

Decisions about employee notification, assistance for personal devices, and coordination

with employee households should not be made for the first time during an active response.

Access and Recovery

VPN tunnel isolation prevents lateral movement while maintaining business continuity for legitimate remote

workers when responders suspect compromise but cannot immediately disable all remote access.

Implement granular access controls that distinguish between compromised and clean remote sessions,

allowing legitimate remote workers to continue accessing necessary resources while containing suspected

compromises. Configure VPN concentrators to support user- or device-specific access policies that restrict

Contain Activity | Chapter 12 | 257

network access for individual remote sessions without affecting all remote workers. For example, to contain

a system under investigation, modify the VPN access control list to restrict the compromised employee’s

VPN session to only access email and the help desk ticketing system, preventing lateral movement to file

shares and internal applications while allowing the employee to report issues and receive guidance.

Cloud service dependencies challenge traditional containment when remote workers rely heavily on SaaS

applications that may lack granular isolation capabilities and operate outside organizational network

perimeters. Remote workers often access most applications directly over the internet, bypassing corporate

networks and VPN connections, making network-based containment impractical. Instead, leverage identity-

based controls and conditional access policies to contain compromised credentials, restrict access based on

device compliance, or force re-authentication to interrupt active sessions. Document the containment

capabilities of critical SaaS applications during planning activities, identifying which services support

granular session termination, per-user restrictions, or conditional access policies that can be applied by the

incident response team.

Physical device recovery presents logistical challenges when compromised systems reside in employee

homes across different cities, states, or countries rather than being physically accessible in corporate

facilities. Coordinate with employees to retrieve devices through secure shipping arrangements, schedule

on-site visits where warranted by incident severity, or implement remote wiping capabilities that preserve

business continuity but may destroy forensic evidence. Balance the investigative value of forensic evidence

against the business impact of device unavailability and the logistical complexity of physical recovery across

distributed locations. For example, for a suspected malware infection on a remote sales representative’s

laptop in another state, consider shipping a pre-configured replacement laptop overnight while arranging

return shipping for the compromised device with instructions to power it down until the shipping container

arrives, avoiding the expense and delay of sending forensic specialists on-site for a routine malware case.

Beyond Traditional Host Compromise

Traditional incident response focuses heavily on compromised endpoints and servers, but modern

organizations face increasingly complex incidents that don’t fit the attacker-on-a-host model, where

responders can simply isolate infected systems from the network. These scenarios require fundamentally

different containment approaches that often prioritize service disruption, data flow control, and third-party

coordination over traditional network isolation.

Figure 85 | Traditional and Modern Containment Challenges

The sections that follow address modern compromise variants that each call for different containment

controls.

Business Email Compromise

Business Email Compromise (BEC) is one of the most prevalent non-host incidents, in which attackers

leverage legitimate email infrastructure to conduct financial fraud or data theft without traditional

endpoints or servers. In BEC incidents, attackers gain access to email accounts through phishing, password

reuse, or session hijacking, then use the compromised accounts to send fraudulent messages with the

intention to commit fraud (such as wire transfer requests), harvest sensitive information, or redirect victims

to attacker-controlled systems.

Containment requires implementing email flow redirection rules to quarantine messages from

compromised accounts, deploying conditional access policies to block sign-ins from suspicious locations or

devices, and coordinating with email service providers to identify and stop fraudulent messages. The

challenge lies in distinguishing legitimate business communications from attacker-controlled messages

while maintaining operational continuity for critical business processes.

Although the attacker’s actions on objectives are often carried out in cloud infrastructure, the initial

compromise often does not. A keystroke logger, infostealer, or session-cookie grabber on the user’s

endpoint is a common way attackers obtain cloud access in the first place. A host investigation is still

warranted even when the visible activity is entirely observed within the cloud SaaS platform. Include

endpoint evidence collection and EDR review of the affected user’s devices in the BEC containment

workflow rather than treating BEC as a purely cloud-side incident.

Contain Activity | Chapter 12 | 259

Supply Chain Incidents

Supply chain incidents involve compromised software: either an upstream vendor’s product is poisoned and

subsequently runs in the organization’s environment, or the organization’s own build pipeline is

compromised and ships malicious artifacts to its customers. Containment strategies for these incidents

span beyond organizational boundaries in either direction.

When attackers compromise build systems, code repositories, or deployment pipelines, containment efforts

need to address not only internal infrastructure but also the compromised software artifacts that may have

already been distributed to customers or deployed to production systems. This might involve coordinating

package repository takedowns to prevent further distribution of compromised software, revoking code-

signing certificates used by attackers to sign malicious builds, or launching customer notification campaigns

while simultaneously securing internal development processes.

The interconnected nature of modern software supply chains means that containment decisions ripple far

beyond the initially affected organization and might require coordination with repository maintainers,

platform providers, and external coordination centers to effectively mitigate the threat. For example, if an

organization discovers that attackers have compromised a company’s CI/CD pipeline and injected malicious

code into three published versions of a popular software package, the organization needs to not only

remove access to the malicious packages and respond to the initial breach but also contact users of the

software with a coordinated security advisory notifying users which versions are affected.

MODERN BREACH COMPLEXITY: THE MOVEIT SUPPLY CHAIN ATTACK

Today’s breach landscape defies traditional incident response assumptions. Consider the 2023

MOVEit attacks: a single vulnerability in file-transfer software triggered a cascading breach affecting

hundreds of organizations worldwide, none of which were directly compromised by attackers.

First National Bank of Omaha (FNBO) exemplifies this complexity. The bank discovered that 57,000

customer records, including names, Social Security numbers, and bank account numbers, had been

stolen by the Clop ransomware group. Yet FNBO’s networks remained uncompromised. The breach

occurred because FNBO used Pension Benefit Information (PBI) Research Services for pension

administration, and PBI used MOVEit Transfer for file transfers. When Clop exploited MOVEit’s zero-

day vulnerability, they gained access to PBI’s systems and consequently FNBO’s customer data.

This attack pattern reveals how modern breaches transcend organizational boundaries through

interconnected business relationships. FNBO’s experience illustrates partner ecosystem exposure as

much as supply chain compromise: FNBO had no MOVEit deployment of its own, and the compromise

reached them through their service provider PBI rather than through software running in their own

environment. Traditional containment strategies assume you can isolate compromised systems

within your control. When your data is compromised through a vendor’s vendor’s software

vulnerability, there are no internal systems to isolate, no network segments to quarantine, and no

processes to terminate.

FNBO’s containment strategy focused entirely on external coordination: assessing data exposure with

PBI, coordinating customer notifications, arranging credit monitoring services, and managing

regulatory reporting, all while lacking visibility into or direct control over the compromised

infrastructure. The bank’s incident response team had to contain a breach they couldn’t see,

investigate systems they couldn’t access, and remediate vulnerabilities they couldn’t patch.

Similar scenarios affected Deutsche Bank, ING, and hundreds of other organizations during the same

attack campaign, demonstrating that modern containment should account for systemic risks

embedded in partner ecosystems and SaaS platforms rather than focusing solely on direct system

compromise.

Partner Ecosystem Breaches

Partner ecosystem breaches compromise the organization’s data rather than its software: a SaaS provider,

managed service partner, or business vendor is attacked, and the organization’s data is exposed through the

partner’s systems even though the organization’s own environment is unaffected. These incidents require

containment strategies that focus on cutting off data flows rather than isolating systems.

SaaS provider breaches, managed service provider compromises, or vendor data exposure incidents require

rapid assessment of data exposure scope, implementation of API access restrictions to prevent further data

synchronization, revocation of integration permissions that allow third-party access to internal systems,

and coordination with external parties who may have different incident response priorities and capabilities.

The challenge lies in limited visibility into third-party security practices and no direct control over

compromised external systems, forcing organizations to implement containment through access-control

boundaries at their own perimeters.

For example, when learning that a SaaS CRM provider was breached and customer data might be exposed,

immediately revoke the provider’s API access tokens to prevent further data synchronization, disable any

automated data feeds from internal databases to the SaaS platform, audit what data was shared with the

provider to assess exposure scope, and contact the provider’s security team to coordinate investigation

activities and understand the timeline for their containment and remediation efforts. These incidents

challenge traditional containment models by requiring organizations to contain threats they cannot directly

observe or control, relying instead on trust relationships, contractual obligations, and regulatory

frameworks to ensure effective response.

CONTAINMENT VALIDATION

Confirming successful containment requires ongoing validation through multiple monitoring channels. Our

goal is to ensure that containment measures effectively stop attacker activities and that adversaries have

not maintained alternative access methods that bypass the team’s isolation efforts. Organizations should

implement multiple validation strategies to ensure containment is effective, including network and process

monitoring, and log analysis.

Table 24 | Containment Validation Channels

CHANNEL WHAT TO MONITOR KEY INDICATORS

Network

Monitoring

Firewall logs, proxy logs, DNS queries,

traffic to known attacker infrastructure

C2 communications resuming, new

connection patterns, protocol tunneling

attempts

Process

Monitoring

Process creation events, service

installations, parent-child process

relationships

Respawned malware, new persistence

mechanisms, unusual executable paths

Log

Analysis

Authentication logs, application logs,

security event logs

Failed authentication attempts, privilege

escalation, unusual file access patterns

Network monitoring confirms that malicious communications have ceased by analyzing traffic patterns for

Contain Activity | Chapter 12 | 261

connections to known attacker infrastructure and watching for new communication patterns that might

indicate alternative C2 channels. Review firewall logs, proxy logs, and DNS queries to verify that

compromised systems no longer communicate with external attacker infrastructure or suspicious

destinations. Monitor for changes in network behavior that might indicate an attacker shifting tactics to

move to different C2 infrastructure or tunneling through allowed protocols. Where possible, use a

combination of network monitoring from network appliances and external servers, and live investigation of

contained systems to verify that no unauthorized outbound connections occur.

Process monitoring verifies that malicious processes are no longer executing and that attackers have not

deployed additional persistence mechanisms during or after containment. Track system process creation on

contained systems to detect suspicious new processes, monitor for service installations that might

represent attacker persistence, and analyze running processes against known malware indicators. EDR

platforms can provide continuous process monitoring that identifies unusual parent-child process

relationships, uncommon executable paths, or processes communicating with unusual network

destinations. Lacking an EDR platform, organizations can also monitor processes using Sysinternals Process

Explorer (as shown in Figure 86) on Windows systems, or the ps, and top/htop commands on Linux systems.

Establish a baseline of expected process activity on contained systems and investigate any deviations that

might suggest continued attacker presence.

Figure 86 | Process Explorer Indicates Unusual Parent-Child Process Relationship for LSASS process

Log analysis ensures no new indicators of compromise emerge after containment by monitoring

authentication, application, and security event logs for suspicious activity. Watch for failed authentication

attempts that might indicate attackers attempting to regain access through alternative credentials, privilege

escalation attempts suggesting persistent local access, or unusual file access patterns indicating continued

data exfiltration. Compare log activity before and after containment to identify changes in attacker behavior

and verify that malicious activity has ceased rather than simply shifted to different techniques. Consider any

pertinent logging sources specific to the environment, including logs generated on the contained system(s)

and external systems.

CONTAIN ACTIVITY EXAMPLES

The following examples illustrate where containment is an important part of the incident response process.

The Multi-Tenant Credential Exposure

Sarah, the incident response team lead for a Kubernetes managed service provider, had been working on an

incident that impacted multiple customers in AWS. An AWS GuardDuty alert flagged unusual API activity

from an unfamiliar IP address, which the team traced to AWS credentials in a read-only Kubernetes

dashboard that was (unfortunately) exposed to the internet. The dashboard used a service account with

read permissions to cluster-wide secrets. Kubernetes (K8s) audit logs showed that the attacker used

dashboard access to list secrets across three customer namespaces: TechFlow Solutions, Meridian Financial,

and Cascade Logistics.

CloudTrail logs confirmed that the attacker had only used credentials from TechFlow’s namespace to launch

two EC2 instances in the TechFlow AWS account. However, because the K8s audit logs showed the attacker

had viewed secrets for all three customers, Sarah got approval to implement simultaneous coordinated

containment across all three customer AWS accounts to prevent the attacker from pivoting to the other

exposed credentials.

A different team had already taken steps to remedy the Kubernetes dashboard exposure. Sarah’s role was to

prevent unauthorized access to the customer’s AWS accounts. She began containment by disabling the

exposed AWS access keys across all three customer accounts. For TechFlow Solutions, she disabled the

access key the attacker had been actively using, as shown in Listing 58.

Listing 58 | Disable Compromised AWS Access Key for TechFlow Solutions

$ aws iam list-access-keys --user-name k8s-service-account --profile techflow-prod

{

"AccessKeyMetadata": [

{

"UserName": "k8s-service-account",

"AccessKeyId": "AKIA_SAMPLE_KEY_PLACEHOLDER",

"Status": "Active",

"CreateDate": "2025-11-09T14:22:31Z"

}

]

}

$ aws iam update-access-key --user-name k8s-service-account --access-key-id AKIA_SAMPLE_KEY_PLACEHOLDER

--status Inactive --profile techflow-prod

$ aws iam list-access-keys --user-name k8s-service-account --profile techflow-prod

{

"AccessKeyMetadata": [

{

"UserName": "k8s-service-account",

"AccessKeyId": "AKIA_SAMPLE_KEY_PLACEHOLDER",

"Status": "Inactive",

"CreateDate": "2025-11-09T14:22:31Z"

}

]

}

Contain Activity | Chapter 12 | 263

Sarah repeated the same credential-disabling process for the Meridian Financial and Cascade Logistics

accounts, even though CloudTrail showed no evidence of attacker activity in those environments. This

precautionary containment prevented the attacker from using any credentials disclosed through the K8s

dashboard.

Next, Sarah isolated the two EC2 instances launched by the attacker in the TechFlow account. She applied

resource tags to mark them as under investigation, enabled termination protection to prevent accidental

deletion, and created EBS snapshots for forensic analysis, as shown in Listing 59.

Listing 59 | Apply Tags and Termination Protection to Compromised TechFlow Instances

$ aws ec2 describe-instances --filters "Name=tag:Customer,Values=TechFlow" --query

'Reservations[].Instances[].InstanceId' --output text --profile techflow-prod

i-a09727b1175f6b58e i-8d7f7414a5081787e

$ aws ec2 create-tags --resources i-a09727b1175f6b58e i-8d7f7414a5081787e --tags

Key=Status,Value=UnderInvestigation Key=IR-Case,Value=2025-042 Key=ContainedBy,Value=sarah-ir-

team --profile techflow-prod

$ aws ec2 modify-instance-attribute --instance-id i-a09727b1175f6b58e --disable-api-termination

--profile techflow-prod

$ aws ec2 modify-instance-attribute --instance-id i-8d7f7414a5081787e --disable-api-termination

--profile techflow-prod

$ aws ec2 create-snapshot --volume-id vol-049df61146c4d7901 --description "IR-2025-042 TechFlow

instance evidence" --profile techflow-prod

{

"SnapshotId": "snap-01234567890abcdef",

"VolumeId": "vol-049df61146c4d7901",

"State": "pending",

"StartTime": "2025-11-02T15:42:18.000Z"

}

Next, she modified the security groups attached to both compromised instances to quarantine them while

maintaining SSH access for investigation, as shown in Listing 60.

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

$ aws ec2 modify-instance-attribute --instance-id i-a09727b1175f6b58e --groups sg-

0123456789abcdef0 --profile techflow-prod

$ aws ec2 modify-instance-attribute --instance-id i-8d7f7414a5081787e --groups sg-

0123456789abcdef0 --profile techflow-prod

1 Allow SSH access only from the IR team jump box at 198.51.100.10

2 Block all outbound traffic to prevent communication with the attacker.

With the AWS resources contained, Sarah addressed the Kubernetes platform compromise. Rather than

deleting the overprivileged service account (which would destroy evidence), she disabled it by removing its

Role-Based Access Control (RBAC) bindings, as shown in Listing 61.

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

To validate containment effectiveness, Sarah continued to monitor CloudTrail, confirming no new API

activity from the disabled access keys. K8s audit logs showed no new dashboard access attempts, and the

quarantined security groups prevented all outbound connections from the compromised EC2 instances. She

configured CloudWatch alarms to alert if disabled access keys were reactivated or if new access keys were

created for the compromised service accounts.

Sarah documented the containment actions for incident tracking and customer notification:

• Account-based IOCs: Compromised K8s service account dashboard-viewer, AWS IAM users k8s-service-

account for TechFlow, Meridian, and Cascade

• Network IOCs: Attacker source IP 185.220.101.42 accessing K8s dashboard

• Cloud resource IOCs : Two unauthorized EC2 instances (i-a09727b1175f6b58e, i-8d7f7414a5081787e) in

TechFlow account

• Contained resources: 3 AWS IAM access keys disabled, 2 EC2 instances quarantined with termination

protection enabled, K8s service account RBAC bindings removed, K8s dashboard ingress removed

• Customer impact : TechFlow Solutions (confirmed compromise with 2 EC2 instances launched),

Meridian Financial (precautionary credential rotation due to possible exposure), Cascade Logistics

(precautionary credential rotation due to possible exposure)

The multitenancy containment approach ensured that all potentially exposed credentials were invalidated

simultaneously, preventing the attacker from pivoting to other customer environments after detecting

defensive actions in the confirmed compromise.

Contain Activity | Chapter 12 | 265

The Ransomware Rapid Response

Marcus Chen, a senior support desk analyst at Vanguard Point Advisors, a mid-size financial services firm,

received an urgent call from Robert Dackinson in the accounting department. Robert reported that several

spreadsheets had become corrupted with unusual file extensions, and he found a text file on his desktop

titled README_RANSOM.txt. Marcus recognized the indicators immediately and escalated the ticket to Priority

1, in accordance with the organization’s ransomware response playbook.

The playbook’s first step required immediate EDR isolation to prevent further access to company systems.

Marcus opened CrowdStrike Falcon and searched for Robert’s workstation using the company’s standard

naming convention. The search returned Robert’s system RD-LAPTOP-278 as shown in Figure 87.

Figure 87 | CrowdStrike Falcon EDR Workstation Search

Marcus selected the device and initiated network containment through Falcon’s isolation feature, as shown

in Figure 88  and Figure 89 . This action immediately blocked all network communication from Robert’s

laptop except for the encrypted management channel that Falcon uses to maintain remote access for

investigation. This step prevented the ransomware from spreading to network file shares or attempting

other lateral movement while preserving the ability to collect forensic evidence remotely.

Figure 88 | CrowdStrike Falcon EDR Workstation Containment

Figure 89 | CrowdStrike Falcon EDR Workstation Containment Confirmation

After several seconds, Marcus validated the containment action by inspecting the status of Robert’s

workstation. CrowdStrike indicated that the isolation command had been successfully applied with the

status label "Update network containment status", as shown in Figure 90 . Marcus updated the incident

ticket to capture the containment time for later timeline reconstruction.

Contain Activity | Chapter 12 | 267

Figure 90 | CrowdStrike Falcon EDR Workstation Containment Validation

With the system successfully quarantined, Marcus continued to follow the playbook’s identity-containment

steps. He accessed the organization’s Okta identity platform and temporarily disabled Robert’s account to

prevent the ransomware from using any cached credentials to access cloud applications or network

resources. Marcus then revoked all active sessions and refresh tokens for Robert’s account across all

connected applications.

Marcus documented all containment actions in the incident ticket, with precise timestamps, as shown in

Table 25.

Table 25 | Containment Actions Summary

TIME ACTION TAKEN

11:47 AM Received report from Robert Dackinson about file corruption and ransom note

11:49 AM Escalated to P1 incident, initiated ransomware playbook

11:51 AM Isolated workstation RD-LAPTOP-278 using CrowdStrike Falcon EDR

11:52 AM Verified network containment using CrowdStrike Falcon console

11:54 AM Disabled user account robert.dackinson@vanguardpointadvisors.com in Okta

11:55 AM Revoked all active sessions and refresh tokens for compromised account

11:57 AM Escalated to IR team for forensic investigation and eradication planning

The rapid containment prevented the ransomware from spreading beyond Robert’s workstation. Later

investigation revealed that the ransomware had successfully encrypted 247 local files but had been isolated

before it could access network file shares that contained critical financial data. The coordinated EDR and

identity containment approach, executed in under ten minutes from initial report, demonstrated the value

of well-documented playbooks and modern containment tools for ransomware response.

CONTAIN: STEP-BY-STEP

The following steps provide a condensed reference for containment activities. Each step corresponds to

topics covered earlier in this chapter, organized for use when stopping attacker activity, preserving

evidence, and preventing further harm.

This step-by-step guide is available for download in PDF and Markdown formats on the

companion website at dynamicincidentresponse.com.

Step 1. Assess Containment Urgency and Strategy

1. Evaluate immediate containment triggers that demand urgent action, including:

◦ Active data destruction or encryption in progress.

◦ Ongoing data exfiltration of sensitive information.

◦ Threats to critical operations or safety systems.

◦ Regulatory compliance timeframes that require a rapid response.

2. Determine containment approach based on organizational context:

◦ Passive containment: Monitor attacker activities to gather intelligence while limiting damage.

◦ Active containment: Take decisive action to stop attacker activities, accepting the possibility of

alerting the attacker.

◦ Adaptive containment: Combine approaches with progressively restrictive measures based on

attacker behavior.

◦ Deceptive containment: Deploy honeypots or decoy systems that appear identical to production to

divert the attacker while gathering intelligence and protecting real assets.

3. Balance competing priorities, including:

◦ Evidence preservation needs versus operational continuity requirements.

◦ Intelligence-gathering value versus the risk of continued attacker access.

◦ Business impact of containment measures versus security benefits.

4. Plan coordination strategy for complex incidents, including:

◦ Identify all known compromised systems, accounts, and services.

◦ Coordinate timing across network, endpoint, identity, and application teams.

◦ Prepare for simultaneous containment actions to prevent attacker pivoting (sequential isolation

alerts adversaries and gives them time to escalate).

◦ Plan credential reset sequencing to prioritize the most privileged accounts first, then service

accounts, then standard user accounts.

◦ Prepare rollback procedures for infrastructure-wide changes such as firewall rule updates or

network topology modifications.

◦ Establish communication channels for coordinated execution.

Contain Activity | Chapter 12 | 269

Step 2. Implement Identity and Access Containment

1. Invalidate compromised credentials across all authentication systems for the known-compromised set

(eradicate Step 4 expands credential remediation to the blast-radius accounts revealed during scope

and to deeper identity primitives like KRBTGT and trust passwords), including:

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

◦ Enable risk-based policies that block sign-ins from suspicious IP addresses or from users exhibiting

anomalous behavior.

◦ Escalate MFA requirements to phishing-resistant methods.

5. Coordinate SSO and multi-application containment, including:

◦ Disable compromised accounts at the IdP level to block authentication to all SSO-connected

applications.

◦ Verify which applications use the IdP for authentication, versus those that use local accounts,

requiring separate revocation.

◦ Monitor for authentication synchronization delays between the IdP and connected applications.

◦ Enforce MFA requirements at the IdP level, escalating to phishing-resistant methods during

containment.

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

◦ Configure local firewall rules to block inbound and outbound connections, except for management

protocols.

◦ Remove compromised instances from production scaling groups and load balancers (cloud

environments).

◦ Implement process termination for identified malicious processes (with caution for watchdog

processes).

◦ Apply application control technologies (AppLocker, Gatekeeper, AppArmor) to block execution of

unauthorized executables, scripts, and libraries.

3. Apply application-level restrictions, including:

◦ Deploy web application firewall rules blocking malicious request patterns.

◦ Implement database access restrictions and query monitoring for unusual patterns.

◦ Disable AI agent tool access and MCP server connections for compromised accounts or exploited

integrations.

◦ Revoke service principals or API keys granting AI systems access to organizational data (these are

often separate from user account credentials).

◦ Configure email flow rules to quarantine messages from compromised accounts.

◦ Apply service disruption where other containment methods prove insufficient: stop web services

being used for exfiltration, disable remote access protocols such as RDP or SSH that provide

attacker entry points, or shut down specific compromised business applications. Coordinate service

disruption with business stakeholders.

Step 4. Implement Cloud-Specific Containment

1. Verify cloud security demarcation for affected services, including:

◦ Determine which containment actions the organization can implement directly and which require

cloud provider engagement.

◦ Do not rely on broad IaaS, PaaS, or SaaS labels to determine responsibility; verify the security

demarcation for each specific product.

◦ Engage cloud provider security teams for incidents affecting infrastructure outside customer

control (e.g., hypervisor, physical networks).

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

Contain Activity | Chapter 12 | 271
