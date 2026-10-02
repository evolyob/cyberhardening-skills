﻿﻿# 第 17-2 章：勒索專用劇本－解密陷阱防範、WORM 還原與韌性強化

> 模組化子章節 | 隸屬來源:  (行 1343 ~ 2681)

---

negotiations and immediately publish stolen data.

Distinguishing Attack Types

Not every ransomware incident involves data exfiltration. The 2025 Verizon Data Breach Investigations

Report found ransomware in 44% of all breaches reviewed, up from 32% the prior year, with that combined

figure encompassing both traditional encryption-based ransomware and pure extortion attacks in which

adversaries steal data without encrypting systems. [7]

The 2024 report separated these categories, finding

that pure extortion accounted for 9% of all breaches compared to 23% for encryption-based ransomware.

Data theft as an additional extortion lever traces back to around 2019, when the Maze ransomware group

pioneered the technique to retain coercive pressure even when victims could restore from backups. [9]

During verification, look for indicators that help distinguish between attack types, as summarized in Table

51. This early classification shapes how the organization communicates with stakeholders and allocates

response resources.

Table 51 | Attack Type Indicators

ATTACK TYPE INDICATORS

Encryption-only • Rapid, widespread file modification

• Minimal prior attacker activity in logs

Data theft with

encryption

• Extended attacker dwell time

• Large outbound data transfers

• Staging activity before encryption

Extortion without

encryption

• Threatening communications referencing stolen data

• No corresponding file encryption

Communicating with Decision Makers

An effective ransomware response requires managing the tension between executive information needs and

investigation timelines rather than resolving it. Analysts should explicitly communicate uncertainty,

distinguishing between what is known, what is suspected, and what remains under investigation.

For example, a statement that positions known and suspected information, along with next steps, provides

leadership with the insight needed for decision-making.

“Based on current evidence, we believe the attacker accessed the file server containing customer data. We

have not yet determined what specific files were accessed or whether data was exfiltrated. We expect to

have better visibility on data access within twelve hours.

Regular briefings (every few hours early in the incident, then daily) help leadership stay informed without

the constant interruption of technical work. Consistent communication formats that show progress without

overpromising build credibility over time. Analysts should also help leadership understand that some

questions may never be definitively answered, and that reasonable assessments based on available evidence

are sometimes the best possible answers.

THE INCIDENT COMMANDER ROLE IN RANSOMWARE RESPONSE

Ransomware incidents generate a sustained volume of questions from executives, legal counsel,

insurers, and external parties that can overwhelm a response team if every analyst is fielding requests

for updates.  Designating an Incident Commander (IC) as the single point of contact between the

response team and organizational leadership protects analysts from constant interruptions while

ensuring decision makers receive timely, consistent information.

The IC does not need to be the most technical person on the team. The role requires someone who

can absorb technical findings from analysts and forensic investigators, translate them into business-

relevant language, and communicate clearly with executives who need to make decisions on

containment, notification, legal exposure, and resource allocation. The IC bridges two audiences that

often communicate differently: analysts focused on artifacts, timelines, and indicators, and leadership

focused on business impact, liability, and recovery timelines.

Effective ICs combine communication skills with enough technical literacy to understand what

analysts are reporting and enough organizational awareness to anticipate what leadership will ask

next. They should be comfortable delivering difficult messages, including "we don’t know yet" and

"the timeline has changed," without losing credibility with either audience. Organizations should

identify and prepare IC candidates before an incident occurs, and exercise them in this role during

tabletop exercises so they are ready when a real incident demands it.

Resource Planning for Extended Response

Resource allocation during triage should account for the extended duration typical of ransomware

incidents. Response efforts may continue for weeks or months through investigation, containment,

eradication, and recovery. Early engagement of external resources, including forensics firms, legal counsel,

and communications specialists, helps ensure adequate capacity for the sustained effort ahead.

When presenting the incident to decision makers for resource allocation, include realistic estimates of

response duration and the specialized skills required. Ransomware response often requires expertise in

negotiation, regulatory compliance, and crisis communications that may not exist within the internal

incident response team.

SCOPE

Ransomware scoping should be more thorough than scoping for many other incident types. While advanced

threat actors may focus narrowly on specific data or systems, ransomware attackers typically survey the

environment broadly and access whatever is immediately available. This difference means scoping must

extend across the entire environment rather than following a narrow path from initial access to a specific

target.

The biggest scoping failure in ransomware response is failing to perform it thoroughly. Organizations that

limit their scope to systems already known to be encrypted often discover during recovery that attackers

had accessed additional systems, established persistence mechanisms, or exfiltrated data from locations not

initially considered.

Failure to adequately scope ransomware incidents results in incomplete containment,

missed data exposures, and prolonged recovery times. Responders should invest the

necessary time and resources to perform comprehensive scoping throughout the response

action loop.

Framework for Ransomware Scoping

Effective ransomware scoping requires systematic data gathering across multiple categories. The

framework checklist in Table 52  provides guidance to help responders ensure comprehensive scoping

coverage.

Table 52 | Ransomware Scoping Checklist

CATEGORY KEY QUESTIONS AND DATA POINTS

Incident Overview How was the incident identified? Which hosts are known to be impacted? What

actions have already been taken? What are the organization’s expectations for

response? What would be considered the organization’s most sensitive

information assets? Do backups exist and are they unencrypted? Do current

network diagrams exist?

Host Inventory How many Windows, Linux, macOS, and ESXi hosts exist in the environment?

Which systems are domain-joined? What virtualization platforms are in use?

Where are backup servers located?

Host Data Sources What Windows Event Logs are available and at what retention? What Linux audit

or syslog data exists? What application-specific logs are available? Is Endpoint

Detection and Response (EDR) telemetry available?

Network Data

Sources

What firewall logs are available? What VPN authentication logs exist? Is NetFlow

data collected? Is there a Network Detection and Response (NDR) solution in

place?

Security Systems Is a Security Information and Event Management (SIEM) system deployed and

what data does it contain? What EDR coverage exists? What endpoint protection

or antivirus data is available? Are there cloud security logs (Microsoft Entra ID,

AWS CloudTrail)?

Cloud Logging What cloud platforms are in use (AWS, Azure, GCP)? What logging and

monitoring services are enabled (CloudTrail, Azure Monitor, etc.)? What is the

retention period for cloud logs? What logging resources are available for

Software as a Service (SaaS) applications (e.g., Microsoft 365 audit logs, Google

Workspace logs)?

This scoping data serves multiple purposes: understanding the environment where the attack occurred,

identifying available evidence sources, and planning collection and analysis activities. Internal teams may

already know many of these answers, but external responders or consultants should systematically gather

this information before proceeding.

Scoping Activities for Ransomware

Ransomware scoping activities focus on understanding the full extent of attacker activity across the

environment. Start by identifying all affected systems, looking beyond those showing obvious encryption to

every system the attacker accessed, authenticated against, or used for staging tools. This broader view

reveals the true scope of compromise rather than the visible symptoms of encryption.

Next, determine data exposure by examining which systems containing sensitive data the attacker accessed.

File servers, databases, document repositories, and backup systems all warrant scrutiny. Understanding

data exposure informs breach notification decisions and helps leadership assess regulatory and reputational

risk.

Map the attacker’s lateral movement path from initial access through to the systems ultimately encrypted.

This reconstruction reveals how attackers navigated the environment and which credentials or

vulnerabilities they exploited along the way. Similarly, identify any persistence mechanisms the attacker

established, including backdoors, scheduled tasks, registry modifications, or unauthorized accounts that

could enable re-entry after recovery.

Finally, establish a comprehensive timeline of the attacker’s activity. Determine when initial access occurred

and how long the attacker was present before deploying encryption. This dwell-time measurement helps

identify the window during which data exfiltration may have occurred and informs decisions about which

backup restore points are most likely trustworthy.

ERADICATE

Eradication in ransomware incidents involves two parallel objectives: understanding what data attackers

accessed, and removing all attacker presence from the environment. Both objectives need to be completed

thoroughly before recovery can proceed safely.

In this section, we’ll assess what data attackers accessed and exfiltrated, work through investigative

techniques and detection strategies for hunting exfiltration evidence, and evaluate whether decryption

options exist that may eliminate the need for backup restoration or ransom payment.

Assessing Data Access and Exfiltration

Understanding what data attackers accessed is critical for regulatory compliance, notification decisions,

and business risk assessment. In double-extortion scenarios, this assessment determines the organization’s

exposure even if the encryption is resolved.

Data access assessment begins with identifying which systems attackers touched:

• Authentication, Authorization, and Accounting (AAA) records: Where did compromised accounts

authenticate? Each successful authentication represents a system that the attacker could access.

• File access telemetry: What files were opened, copied, or modified on accessed systems?

• Network share access: Which file servers and shared drives did the attacker browse or access?

• Database access: Did attackers connect to databases containing sensitive information?

Software inventory and data classification become valuable during this assessment. Understanding what

data types reside on each system helps translate "the attacker accessed the backup server" into "the

attacker potentially accessed customer personally identifiable information (PII) and financial records stored

on that system."

Investigative Techniques for Data Exfiltration Hunting

Ransomware attackers commonly stage data before exfiltration using archival tools and temporary storage

locations. Investigators should hunt for evidence of these staging activities, summarized in Table 53.

Table 53 | Exfiltration Hunting Techniques

TECHNIQUE WHAT TO LOOK FOR

Archival artifacts Tools like WinRAR, 7-Zip, and native Windows compression utilities leave

forensic traces:

• WinRAR archive history: NTUSER.DAT\Software\WinRAR\ArcHistory

• 7-Zip history: NTUSER.DAT\Software\7-Zip\

• Password-protected archives chunked into 1-2GB segments

Staging locations Attackers stage data in predictable locations:

• C:\Users\Public

• C:\Perflogs

• %TEMP%

• Hidden shares and publicly accessible folders

Exfiltration tools Hunt for file transfer utilities, including:

• Archiving tools (WinRAR, 7-Zip)

• File transfer clients (FileZilla, WinSCP, rclone)

• Cloud storage clients (Mega sync client, Dropbox)

• Command-line utilities (cURL, Wget, FTP)

Deleted artifacts Attackers often delete staging archives after exfiltration:

• NTFS Update Sequence Number Journal ( $UsnJrnl) analysis reveals file

creation and deletion

• File system timeline analysis reveals deleted archive evidence

Systematic hunting across these artifact categories helps investigators reconstruct the data exfiltration

timeline and estimate what information left the environment, even when attackers attempted to cover their

tracks.

Data Exfiltration Detection Strategies

When the specific data accessed is unknown, detection focuses on identifying anomalous data movement.

Start by examining network telemetry for large outbound data transfers to external IP addresses,

particularly transfers destined for hosting providers or known file-sharing services. Use network monitoring

tools to identify spikes in data volume to narrow down investigation windows, as shown in the examples in

Figure 184 . File system analysis should look for the creation of large archive files, especially in unusual

locations where archives would not normally appear.

Figure 184 | Cacti Network Monitoring Reveals Egress Data Transfer Spikes

User and Entity Behavior Analytics (UEBA), often supported with AI-based technology platforms, provides

additional detection opportunities. Execution of archival tools by unexpected accounts or on systems where

such activity is abnormal warrants investigation. Similarly, network connections to cloud storage services

from systems that do not normally use such services may indicate unauthorized data staging or exfiltration.

Decryption Possibilities

Before committing to backup restoration or considering a ransom payment, responders should investigate

whether free decryption options are available. Law enforcement operations, security researchers' efforts,

and implementation flaws in ransomware encryption have led to decryption tools for numerous

ransomware families.

Some circumstances allow organizations to perform decryption without payment:

• Implementation vulnerabilities: Although less common today, some ransomware families have included

cryptographic implementation flaws that allow researchers to recover encryption keys or decrypt files

directly. These vulnerabilities are uncommon in modern, well-maintained ransomware operations, but

older or less sophisticated variants may contain exploitable weaknesses.

• Law enforcement operations: Coordinated efforts have led to the seizure of ransomware infrastructure,

including decryption keys. Operations against groups such as Hive, ALPHV/BlackCat, and LockBit have

yielded decryption capabilities that were subsequently made available to victims.

• Leaked keys: Internal conflicts within ransomware groups, disgruntled affiliates, or operational security

failures have occasionally resulted in decryption keys being leaked publicly.

• Security researcher efforts: Independent researchers and antivirus vendors analyze ransomware

samples and, when they identify weaknesses, sometimes develop decryption tools.

The No More Ransom Project  serves as the primary repository for free ransomware decryption tools. This

initiative, supported by Europol, law enforcement agencies, and security vendors, aggregates decryption

tools for over 150 ransomware families. Responders should check this resource early in the response

process.

Additional decryption resources include:

• Vendor-provided tools from security companies, including Kaspersky, Avast, Emsisoft, and Bitdefender.

• Decryption tools from law enforcement agencies (sometimes not publicly released but available through

direct contact).

• Security researcher publications and tool releases.

• Commercial decryption services, including Unidecrypt from Coveware.

Responders should maintain realistic expectations about the likelihood of decryption. Most modern

ransomware uses properly implemented encryption without known vulnerabilities. Decryption without

obtaining the attacker’s keys is typically not feasible for current, actively maintained ransomware families.

Even when decryption tools exist, they may have limitations:

• Tools may only work for specific ransomware versions or variants.

• Some encrypted files may not be recoverable even with the correct keys.

• Decryption processes can be slow and resource-intensive, particularly for large file volumes.

• Partial file corruption may occur even after successful decryption.

• Tools may not provide sufficient scalability to handle enterprise-scale recovery.

Given these constraints, responders should evaluate decryption possibilities early but continue pursuing

backup restoration and system rebuild options in parallel.

DECRYPTOR LIMITATIONS

Organizations should also set realistic expectations with stakeholders about recovery timelines. Even

after organizations pay the ransom and receive a functioning decryptor, recovery takes months, not

days. The 2021 Conti ransomware attack against Ireland’s Health Service Executive (HSE) illustrates

this reality: despite obtaining a decryptor, the organization took approximately four months to

restore critical healthcare services nationwide. [10]

Decryption alone does not restore operations. Systems need to be validated, rebuilt where necessary,

and reintegrated into the environment, all while maintaining security controls to prevent

recompromise. Communicating this reality early helps maintain stakeholder confidence throughout

the recovery process and reduces the pressure on response teams to meet unrealistic timelines.

Decryption Assessment Process

When investigating decryption options, follow a structured approach:

1. Identify the ransomware family: Analyze ransom notes, encrypted file extensions, and any available

malware samples to accurately identify the ransomware variant. Misidentification leads to wasted effort

with incompatible tools.

2. Check available resources: Search the No More Ransom project, vendor tools, and recent security news

for decryption options matching the identified family.

3. Validate tool applicability: Confirm that available tools match the specific variant and version

encountered. Tools developed for older versions may not work on newer variants.

4. Test on sample files: Before committing to full-scale decryption, test tools on a subset of encrypted files

to verify they work correctly. Measure the time and resources required for decryption to inform

broader planning.

5. Plan decryption execution: If tools prove effective, plan the decryption process, including prioritizing of

critical files and validating recovered data.

6. Backup encrypted data: Before attempting decryption, create secure backups of the encrypted files to

prevent data loss if the tool fails or corruption occurs during decryption.

7. Execute decryption: Run the decryption process according to the plan, using dedicated systems with a

copy of the encrypted data, where possible, instead of live systems.

8. Validate and Monitor: Continue monitoring for any issues and validating recovered data as it becomes

available.

Decryption tools, when available, may represent the least costly recovery path. Even a few hours spent

investigating decryption options is worthwhile before committing to longer restoration or payment

alternatives.

RECOVER

Recovery is typically the longest and most resource-intensive phase of ransomware response. Organizations

often underestimate the time and effort required to restore operations, particularly when critical

infrastructure such as domain controllers, identity platforms, or backup systems has been compromised.

Too often, an organization will pay the ransom, obtain a decryptor, and expect to be back up and running

within hours or days. This is seldom the case, especially when the organization hasn’t prepared for recovery

in advance. In this section, we’ll cover key principles for ransomware recovery, including planning and

prioritization, restoring from backups, system rebuild, monitoring for an attacker’s return, and

communication during recovery.

Recovery Planning and Prioritization

Recovery planning prioritizes systems based on organizational criticality, with infrastructure dependencies

addressed before application services. As with any other major incident, critical systems receive priority,

but ransomware recovery requires particular attention to the order of operations, since foundational

services must be trustworthy before dependent systems can be restored.

Recovery prioritization considers several factors, including:

• Business criticality: Revenue-generating systems, patient care capabilities, and critical operations

platforms.

• Infrastructure dependencies: Identity services, DNS, and network infrastructure must be restored

before systems that depend on them.

• Data availability: Systems with verified clean backups versus those requiring rebuild.

• Regulatory requirements: Notification deadlines and compliance obligations that may drive timeline

constraints.

• Resource availability: Staff, hardware, software licenses, and vendor support capacity.

Coordinate recovery priorities with decision makers to align technical work with organizational needs.

Important questions include which systems are most critical for resuming organizational operations, what

operational workarounds can sustain the organization while recovery proceeds, and what resources can be

allocated to accelerate recovery of priority systems. Answering these questions early in the recovery

process helps align technical efforts with organizational priorities and sets realistic expectations for

stakeholders. Clear communication and priority setting help reduce frustration when recovery timelines

extend longer than hoped.

Restoration from Backups

As we saw in Section 17.2.5 , restoration is the primary recovery method when backups are available and

verified to be clean. However, restoration requires careful attention to avoid reintroducing attacker access

or compromised data.

Critical considerations for backup restoration:

• Identify clean restore points: The restore point must predate the attacker’s compromise, not the

encryption event itself. A threat actor (such as an IAB) may have been present collecting information

about the organization’s systems for weeks or months before selling access to a ransomware threat

actor.

• Verify backup infrastructure: Confirm that backup servers, storage systems, and control planes were not

compromised or manipulated by attackers.

• Validate backup integrity: Test restoration on isolated test systems before deploying to production.

• Understand data loss: Accept that data created between the last clean backup and the encryption event

may be unrecoverable.

Challenges with backup restoration include determining the correct restore point when attacker dwell time

is uncertain, accepting potentially significant data loss when restoring from older backups, and the time

required to restore large systems and datasets.

System Rebuild

For critical infrastructure, particularly Active Directory domain controllers, system rebuild is often

preferable to restoration. Compromised domain controllers pose unique risks because attackers can embed

their persistence deeply within Active Directory (AD) objects, Group Policy, and trust relationships.

Restoring a compromised DC may reintroduce attacker access that is extremely difficult to detect or

remove.

Recovering a compromised Active Directory environment when an attacker has had

domain admin access is complex and risky. Organizations should carefully consider the

perceived cost-benefits of restoration against the long-term security risks of incomplete

eradication of attackers.

Rebuild is recommended when:

• Domain controllers or other identity infrastructure were compromised.

• Backup integrity is uncertain, or backups may contain attacker persistence.

• Systems are substantially outdated, and recovery offers an opportunity to modernize.

• The time to validate backup cleanliness exceeds the time to rebuild.

A critical principle for recovery: do not decrypt and reuse encrypted data without validation . Victims

sometimes assume that paying ransom and decrypting systems returns them to a clean state. This

assumption is dangerous. Decrypted systems retain whatever attacker tools, persistence mechanisms, and

compromised configurations existed before encryption. Decryption restores data accessibility but does not

remove the attacker’s presence.

Decrypting a system restores data accessibility but does not remove attacker tools,

backdoors, or compromised configurations. Treat decrypted systems as compromised and

validate or rebuild them before returning to production.

Watching for Attacker Return

Ransomware victims face an elevated risk of re-attack, particularly if they paid the ransom. Payment

establishes the organization as willing to pay, making it an attractive target for secondary ransom or

extortion attacks from the same group or others who purchase victim lists.

Organizations should maintain heightened monitoring during and after recovery:

• Enhanced detection rules based on TTPs observed during the incident.

• Increased scrutiny of authentication activity, particularly for privileged accounts.

• Network monitoring for command-and-control (C2) patterns similar to those used in the initial attack.

• Regular hunting for indicators associated with the ransomware group that attacked the organization.

Re-ransoming attacks on victims who did not thoroughly eradicate the attacker’s access or address the root

causes represent a common pattern. Recovery is not complete when systems are restored; it is complete

when the organization has confidence that attacker access has been eliminated and the vulnerabilities that

enabled the attack have been remediated.

Paying ransom establishes the organization as willing to pay, making it an attractive target

for repeat attacks. Recovery is not complete until attacker access is eliminated and the

vulnerabilities that enabled the attack are remediated.

Communication During Recovery

Ransomware recovery often extends for weeks or months, requiring sustained communication with multiple

stakeholder groups. Unlike shorter incidents where a single status update may be all that is needed,

ransomware response often requires ongoing communication management throughout an extended

recovery period.

In Section 10.3.6 , we covered broad stakeholder communication guidance. This section

addresses ransomware-specific communication considerations.

Internal Communication Efforts

Recovery progress updates keep leadership informed and help manage organizational expectations.

Establish a regular cadence for internal updates, adjusting frequency based on recovery phase and

stakeholder needs.

Leadership Updates

Executive leadership needs visibility into recovery progress, resource requirements, and timeline estimates.

These updates should focus on business impact, risk posture, and the decisions required, rather than on

technical details. Regular briefings (daily during active recovery, then transitioning to weekly) maintain

leadership engagement without overwhelming executives with operational minutiae.

User Communication

Affected users need clear information about service availability, workarounds, and expected restoration

timelines. Be honest about timeline uncertainty rather than providing optimistic estimates that will be

missed. Users can adapt to known constraints more easily than they can to repeated delays in optimistic

projections.

Recovery Team

Multiple teams typically participate in ransomware recovery, including infrastructure, applications, security,

and business units. Regular coordination meetings ensure teams remain aligned on priorities and

dependencies. Document decisions and assignments to prevent confusion during extended operations.

External Communication Efforts

External communication during ransomware incidents requires coordination between technical teams, legal

counsel, communications staff, and executive leadership.

Regulatory Notifications

Ransomware incidents involving data exposure may trigger notification requirements under HIPAA, state

breach notification laws, the GDPR, the Network and Information Security (NIS2) Directive, the Digital

Operational Resilience Act (DORA), the 8-K market transparency report, or industry-specific regulations.

Work with legal counsel to identify applicable requirements and manage notification timelines. Some

regulations impose specific deadlines that must be tracked regardless of recovery status.

Customer and Partner Notifications

Customers and business partners may need to be notified of service disruptions, data exposure, or changes

to business processes during recovery. Coordinate these communications with legal counsel and

communications staff to ensure consistent messaging.

Insurance Carrier Coordination

Contact the cyber insurance carrier as early as possible in the response, ideally before engaging third-party

forensics firms or making significant response decisions. Many cyber insurance policies include specific

requirements regarding which vendors may be used, how evidence should be handled, and which actions

require prior approval. Organizations that engage outside counsel, sign forensic investigation contracts, or

begin remediation work before notifying their carrier risk having those costs denied during the claims

process.

Law Enforcement Engagement

If law enforcement is involved, coordinate communications to avoid compromising any ongoing

investigation. Law enforcement may request that certain details not be disclosed publicly.

DEBRIEF

Ransomware incidents generate critical lessons about technical defenses, response procedures, and

organizational resilience. The debrief phase is an opportunity to convert the stress and disruption of the

incident into improvements that reduce the likelihood and impact of future attacks.

The stakes of a thorough debrief are high: documented cases of victims being re-ransomed by the same or

similar threat actors demonstrate that organizations that fail to address root causes or thoroughly eradicate

attacker access face an elevated risk of repeat incidents. Organizations that treat ransomware as a one-time

crisis rather than a learning opportunity may find themselves responding to the same attackers again.

General debrief guidance, including facilitating After-Action Review (AAR) sessions, documentation

requirements, and implementation tracking, is covered in Debrief Activity . This section focuses on

ransomware-specific debrief considerations.

Ransomware-Specific Debrief Questions

Beyond the standard AAR questions covered in Conducting the After-Action Review , ransomware debriefs

should address considerations unique to this incident type:

Backup and recovery assessment: Did backups survive the attack? If not, what architectural changes would

have protected them? How did actual recovery time compare to RTO targets, and were those targets

realistic? Did the organization have to accept data loss, and if so, what would have prevented it?

Dwell time analysis : How long were attackers present before encryption? What detection opportunities

existed during that window? Could earlier detection have prevented encryption entirely, or at a minimum,

reduced its scope?

Data exfiltration determination : Was the organization able to determine what data was accessed or

exfiltrated? If not, what logging or monitoring gaps prevented that determination? How did uncertainty

about data exposure affect notification decisions and stakeholder communications?

Ransom decision evaluation  (if applicable): Did the organization’s ransom payment policy function as

intended? Were decision makers prepared with the information they needed? If payment was made, did

decryption work as expected? If payment was declined, was data publicly disclosed or sold on the dark web,

and how did that affect the organization?

Extortion response: If the incident involved multi-vector extortion beyond encryption, how effectively did

the organization respond to each pressure channel? Were legal, communications, and executive teams

prepared to coordinate on non-technical threats like leak site postings or customer harassment?

Identity and privilege exposure : What privileged accounts were compromised? Did the organization have

visibility into the full scope of credential exposure? Were break-glass procedures needed, and did they

function correctly?

These questions help to focus on ransomware-specific lessons that generic incident debriefs may overlook.

Ransomware-Specific Metrics

Tracking ransomware-specific metrics supports the organization’s own improvement efforts, but there is

significant value when these metrics are shared across organizations. When anonymized metrics are shared

through ISACs, industry reports, and community forums, they contribute to a collective understanding of

how ransomware attacks unfold and how effectively organizations are responding. Aggregated data on dwell

times, TTPs, backup survival rates, and recovery methods across many incidents gives the broader security

community the evidence needed to identify trends, calibrate defenses, and advocate for resources.

Organizations that contribute to this shared knowledge base help improve ransomware resilience across

their industry and beyond.

In addition to standard incident metrics examined in Chapter 4 (including Mean Time To Detect and Mean

Time To Respond), ransomware incidents warrant tracking several measurements unique to this attack

type. Table 54 lists several ransomware-specific metrics that organizations should consider tracking across

incidents to evaluate their preparedness and response effectiveness.

Consider these metrics as opportunities that may provide additional value to the

organization, rather than requirements that should be tracked for every incident.

Organizations should select the metrics that best align with their organizational priorities

and data availability, and focus on consistently tracking them across incidents to identify

trends and inform improvements.

Table 54 | Ransomware-Specific Metrics

METRIC DESCRIPTION VALUE

Attacker dwell

time

Time from initial access to encryption

deployment

Reveals the detection opportunity

window where earlier identification

could have prevented encryption

Backup survival

rate

Percentage of backup systems and data

that remained accessible and

uncompromised

Indicates whether backup architecture

can withstand privileged attacker

access

Data exfiltration

confidence

Whether the organization could

definitively determine what data was

accessed

(high/medium/low/unknown)

Reflects logging and monitoring

maturity and affects notification

decision confidence

Recovery

method

distribution

Percentage of systems restored from

backup versus rebuilt versus decrypted

Informs future preparation investments

and validates backup strategy

effectiveness

Encryption

spread rate

Systems encrypted per hour during

active encryption

Measures containment effectiveness

and helps calibrate automated response

thresholds

WHEN RECOVERY LESSONS STAY BEHIND CLOSED DOORS

In October 2019, the Russian cybercrime group known as WIZARD SPIDER deployed the Ryuk

ransomware against DCH Health System, disrupting services for three hospitals in Tuscaloosa

County, Alabama. [11]

The attack forced the hospitals to implement diversion protocols, turning away

all but the most critical patients for over a week while staff reverted to paper-based workflows for

patient care.

DCH ultimately paid the ransom and obtained decryption keys, then began a staged recovery process:

decrypt, test, and bring systems back online one by one across thousands of devices. Diversion

protocols were lifted approximately ten days after the attack began, though restoration of non-

essential systems continued beyond that 10-day window.

Despite the scale of this incident, the public record contains almost no detail about how DCH

managed the operational recovery. Which clinical systems were restored first? What restoration

sequence worked, and what did not? What would DCH recommend to another hospital system facing

the same situation? Those operational details, the ones most valuable to the next hospital hit by

ransomware, were never shared publicly.

This is not a case that is unique to DCH. Across ransomware incidents, public reporting consistently

focuses on whether the ransom was paid and when services resumed. The operational recovery

details that would help other organizations, especially hospitals providing urgent patient care, are

almost entirely absent from the public record.

Every hospital that recovers from ransomware generates hard-won operational knowledge. When

that knowledge stays locked within the organization, the next hospital facing a ransomware attack

has to start from scratch. Sharing anonymized recovery metrics, including restoration sequences and

timelines, backup survival outcomes, and clinical workflow adaptations, would give the healthcare

sector a growing body of evidence to prepare against a threat that targets hospitals with increasing

frequency. While organizations understandably hesitate to share details about ransomware incidents,

the collective benefit of sharing operational recovery lessons is significant, especially in sectors

where ransomware directly impacts human lives.

These metrics help organizations evaluate ransomware-specific preparedness and identify where

investments would have the greatest impact on future incident outcomes. Tracking these measurements

across incidents reveals patterns that inform strategic decisions about detection capabilities, backup

architecture, and containment procedures. Organizations that experience multiple ransomware incidents

can use this data to validate whether improvements are delivering measurable results. Where possible,

organizations should also share anonymized metrics with ISACs, sector partners, and community threat-

sharing programs so that the broader security community can build on a larger dataset of real-world

ransomware outcomes.

FINAL CONSIDERATIONS

Ransomware incidents test every aspect of an organization’s incident response capabilities. Organizations

with strong technical defenses, well-practiced response teams, and resilient business processes fare best,

but even the most prepared organizations face significant challenges. In this final section, we’ll examine

several overarching considerations that apply across the ransomware response lifecycle.

The Human Element

Ransomware response is exhausting. Extended incidents spanning weeks or months create sustained

pressure on response teams, IT staff, and leadership. Organizations should plan for personnel rotation,

ensure adequate rest during extended operations, and provide support resources for staff experiencing

burnout or stress. The best technical response procedures fail when the people executing them are too

exhausted to function effectively. In ransomware incident response, the stakes are high, and mistakes are

costly; leadership can help reduce the likelihood of errors by prioritizing team well-being.

Just as we avoid single points of failure in high-value systems, we should avoid them in

our response teams. Cross-training all team roles helps the organization avoid gaps in

essential skills when key personnel are unavailable.

A HANGRY RESPONSE TEAM IS NOT AN EFFECTIVE RESPONSE TEAM

I have worked on ransomware incidents where leadership treated the response team as a resource to

be managed and others where leadership treated the team as people to be supported. The difference

in outcomes was significant.

When an organization is in crisis, the response team becomes the most important group in the

building. These are the people leadership is relying on to figure out what happened, stop the bleeding,

and get the organization back on its feet. They should be empowered accordingly. That means giving

them the autonomy to make technical decisions without bureaucratic delays, providing the tools and

access they need without making them justify every request through normal procurement channels,

and shielding them from the organizational politics that inevitably intensify during a crisis.

It also means something much simpler: feed them. This sounds trivial, and it is not. Response teams

working 14-hour days during a ransomware incident are not taking lunch breaks. They are not

running out to grab dinner. They are heads-down, working through problems under pressure, and

they will skip meals rather than step away from a critical analysis task. Fresh, hot food delivered to

the team, not yesterday’s cold pizza sitting in a conference room, is one of the easiest and most

effective ways leadership can demonstrate that the people doing the hardest work are valued. When

shifts change, the incoming team should find a meal waiting, not empty boxes from the previous shift.

Coffee, water, and snacks should be stocked and replenished without anyone on the response team

having to ask.

This is not about perks. It is about sustaining performance over days and weeks of high-intensity

work. A response team that feels supported by leadership will push through difficult stretches with

focus and commitment. A team that feels like an afterthought will burn out faster, make more

mistakes, and disengage at the moments when the organization needs them most.

Legal and Regulatory Complexity

Ransomware incidents increasingly intersect with complex legal and regulatory requirements. Data breach

notification laws, industry-specific regulations, contractual obligations, and the potential for sanctions

create a set of requirements that technical responders are not equipped to navigate on their own. Early

engagement of legal counsel, ideally counsel with specific experience in ransomware incidents, helps ensure

that response decisions do not create additional legal exposure.

AI as an Evolving Threat

Earlier sections of this chapter examined how AI is lowering the technical barrier for ransomware affiliates

and improving the quality of social engineering campaigns. Those developments represent the early stages

of a more fundamental shift in ransomware campaigns where AI is moving from an advisory role, where

attackers consult it for guidance, to an operational one, where AI systems actively execute phases of an

attack with minimal human direction.

Where we once made assumptions about the relationship between attacker skill and attack capability, these

considerations are no longer accurate. Threat modeling in ransomware has relied on the idea that

technically complex campaigns require technically skilled operators. With AI coding agents, minimally

competent threat actors can access instant operational competence across reconnaissance, exploitation,

lateral movement, and data exfiltration, creating new risks for organizations to consider.

AI Across the Attack Lifecycle

Threat actors are integrating AI throughout ransomware and extortion operations, extending well beyond

social engineering assets to the full attack chain. AI coding agents are actively executing attack phases

rather than simply advising a human operator. Documented cases show AI conducting network scanning,

credential harvesting, lateral movement, and data exfiltration with minimal human oversight (see also

Autonomous Adversaries). [12]

The Anthropic November 2025 threat intelligence report documented a campaign in which AI performed an

estimated 80 to 90 percent of the operations, with human decision-making required only four to six times

per engagement. [13]

A single operator with AI assistance can match the output of a team, conducting

simultaneous operations against multiple organizations. Organizations should assume that even

unsophisticated actors can execute technically complex campaigns.

AI-Optimized Extortion

Extortion revenue depends on the victim’s willingness to pay, which depends on how damaging disclosure

would be and how credibly the attacker can demonstrate that damage. AI is automating both sides of this

equation: identifying the most sensitive stolen data and calibrating the extortion approach to maximize

payout.

After exfiltration, threat actors face a data analysis problem. Terabytes of stolen files need to be evaluated to

determine which creates the greatest pressure for extortion. Previously, this required manual review, which

limited both scale and speed. AI systems excel at systematically categorizing data by sensitivity, including

PII, financial records, healthcare data, trade secrets, and regulatory-sensitive documents. These systems

identify the content most likely to motivate payment. AI can also cross-reference stolen data against

regulatory frameworks to identify specific notification obligations, penalties, and reputational risks the

victim faces if data is disclosed. This turns raw, stolen data into actionable pressure for extortion.

Once sensitive data is identified, AI manages the extortion lifecycle from demand pricing through payment

collection. The Anthropic August 2025 threat intelligence report documents cases in which AI analyzed

victims' financials and generated "profit plans" with multiple monetization paths for each target: direct

organizational extortion, data sales to third parties, individual targeting of people whose data was

compromised, and regulatory threat pressure. [14]

Ransom demands in the documented case ranged from

$75,000 to $500,000, calibrated to each victim’s organizational size, industry, and regulatory exposure.

AI handles operational execution across concurrent campaigns as well, crafting psychologically targeted

communications with incremental penalty structures, generating victim-specific ransom notes with exact

financial figures and regulatory citations, and adapting strategy based on victim responses. A single actor

can manage customized extortion campaigns against many organizations simultaneously, where previously

this level of personalization required a dedicated team.

AI-Generated Ransomware Development

AI is democratizing the RaaS market by enabling actors without traditional development skills to create

functional ransomware with advanced capabilities. Documented cases describe actors who cannot

independently implement encryption algorithms or understand Windows system call (syscall) mechanics,

yet produce and sell functional ransomware packages priced between $400 and $1,200. [15]

These packages

include ChaCha20 encryption, EDR evasion techniques such as FreshyCalls and RecycledGate, and anti-

analysis capabilities.

AI allows attackers to iteratively refine their tooling through continued interaction with models, introducing

new features and capabilities over time. Ransomware tooling progresses from basic encryption to advanced

delivery and evasion as directed by the threat actor. As development barriers are eliminated, the RaaS

ecosystem expands, increasing both the volume and variety of ransomware families that organizations will

encounter.

Attribution complexity also increases as AI-generated code reflects patterns specific to the language model

(e.g., Claude Sonnet 4.6 vs. GPT-5.3-Codex) rather than distinctive human coding styles. This makes it

harder for analysts to link ransomware families to specific developers or groups based solely on code

characteristics.

Attribution is always challenging in ransomware, but AI-generated code adds new layers of

complexity.

AI for Defenders

The same AI capabilities that accelerate attackers can also accelerate defenders' actions. As we saw in

Chapter 16, AI can assist with preparation activities, accelerate the detection of IOCs, support containment

and evidence collection, and facilitate the generation of recovery actions. AI tools grounded in

organizational context, through playbooks supplied as skills or through Retrieval Augmented Generation

(RAG), can assist analysts with response guidance tailored to the organization’s specific practices,

procedures, and infrastructure.

The acceleration of ransomware capabilities through AI makes the preparation investments described

throughout this chapter more important, not less. Organizations that build strong foundational defenses,

including identity protection, backup resilience, and detection capabilities, create environments where AI-

enhanced attacks are harder to execute, regardless of the attacker’s tooling. Preparation remains the most

effective response to an evolving threat landscape.

Recovery Is Not the End

Technical recovery is an important milestone, but the impact on an organization following a ransomware

incident often extends well beyond system restoration. When systems come back online and business

operations resume, organizations often discover that the broader consequences continue across regulatory,

legal, financial, and reputational dimensions.

Regulatory and Legal Exposure

Breach notification obligations trigger timelines that continue regardless of recovery status. Regulatory

inquiries may extend for months as agencies evaluate the organization’s security practices and incident

handling. If litigation follows, discovery and depositions can span years. Organizations should expect

ongoing engagement with legal counsel well after technical teams have moved on to other priorities.
