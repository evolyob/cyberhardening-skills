# Chapter 8: Detect Activity: Monitoring & Detection Engineering

> Source: PDF Pages 162-185 (Total Pages: 24)

exercises that combine tabletop discussion with technical execution).

◦ Develop realistic scenarios based on relevant threats.

◦ Include participants from all departments involved in the response.

◦ Test authorization levels and containment decisions in addition to technical procedures.

◦ Rotate team members through different roles to build depth.

◦ Document findings and track improvement implementation.

8. Maintain preparation documentation on a regular review cycle, including:

◦ Review contact lists quarterly with verification of current information.

◦ Exercise each playbook at least once per year and conduct a separate review on an offset schedule.

◦ Review policy documents annually aligned with broader governance cycles.

◦ Develop an annual exercise plan that maps each playbook to a scheduled exercise date.

◦ Assign specific individuals responsible for keeping documents current and include document review

in their performance expectations.

Step 3. Proactive Prevention and Detection

1. Implement Cyber Threat Intelligence (CTI) capabilities, including:

◦ Identify appropriate intelligence sources (commercial, ISAC, government, OSINT).

◦ Establish processes to review and operationalize intelligence.

◦ Integrate IOCs into detection systems using standardized formats (STIX 2.1).

◦ Use intelligence to prioritize defenses and inform response.

◦ Evaluate CTI platforms to centralize intelligence management, correlate indicators across sources,

and support investigation pivots during active incidents.

2. Develop processes for software management, including:

◦ Implement risk-based patch management with defined timelines.

◦ Maintain configuration management with version control.

◦ Track software inventory including version information.

◦ Maintain Software Bill of Materials (SBOM) data to identify systems affected by vulnerabilities in

third-party components.

◦ Discover and document shadow IT through billing and expense report reviews.

◦ Track end-of-life software and establish migration or compensating control plans.

◦ Establish exception handling for systems that cannot be patched.

3. Apply system hardening processes, including:

◦ Disable unnecessary services and remove default accounts and credentials.

◦ Adopt security benchmarks (CIS, DISA STIGs) appropriate to environment.

◦ Deploy endpoint controls and forward logging data to a central collection point.

◦ Implement application allowlisting where feasible.

◦ Automate hardening through infrastructure-as-code or scripting where possible.

◦ Regularly review and update hardening baselines.

◦ Monitor for configuration drift from hardened baselines as an indicator of unauthorized changes.

◦ Document exceptions with compensating controls.

4. Implement endpoint security monitoring, including:

◦ Deploy EDR across servers, workstations, and cloud instances.

◦ Configure appropriate detection rules and tune for the environment.

◦ Establish alert review and investigation processes.

◦ Enable response capabilities (isolation, evidence collection).

5. Deploy enhanced endpoint telemetry where EDR coverage has gaps, including:

◦ Deploy a supplemental telemetry agent across endpoints lacking sufficient native or EDR-provided

event detail.

◦ Adopt a community-maintained configuration as a baseline and tune for the environment.

◦ Forward telemetry events to a central collection point for correlation and retention.

◦ Validate telemetry capture using adversary simulation tests.

6. Implement network security monitoring, including:

◦ Deploy monitoring at critical network points (egress, segment boundaries).

◦ Configure appropriate detection rules for network threats.

◦ Ensure visibility into both north-south and east-west traffic.

◦ Establish alert review and investigation processes.

7. Invest in detection engineering, including:

◦ Develop detection rules tied to specific attacker techniques, mapped to MITRE ATT&CK.

◦ Test and validate detection rules using adversary simulation tools.

◦ Tune rules to reduce false positives based on the organization’s environment.

◦ Track detection coverage against the ATT&CK matrix to identify gaps.

◦ Maintain detection rule lifecycle: retire outdated rules, update for environment changes, and

document rule intent and logic.

8. Establish a threat hunting program, including:

◦ Maintain a catalog of hunt hypotheses tied to MITRE ATT&CK tactics and techniques.

◦ Identify target data sources for each hypothesis (proxy, DNS, process creation, authentication).

◦ Define cadence for each hypothesis based on risk priority and data freshness.

◦ Track hypothesis, data source, cadence, last-run date, threat hunting analyst, and findings in an

audit table.

◦ Promote hunt findings into automated detection rules to feed the detection engineering program.

9. Catalog critical data, systems, and infrastructure, including:

◦ Maintain an accurate inventory of hardware, software, data assets, cloud resources, and third-party

connections.

◦ Identify and document critical assets essential to organizational survival.

◦ Classify assets by business criticality.

◦ Document network architecture and dependencies.

◦ Maintain both local offline copies and access to authoritative sources maintained by owning teams.

◦ Implement processes to maintain inventory accuracy.

10. Monitor the attack surface, including:

◦ Continuously discover and evaluate externally visible assets (internet-facing services, cloud

resources, domains, certificates, exposed APIs).

◦ Compare discovered assets against the internal asset inventory to identify gaps.

◦ Feed ASM findings into hardening and vulnerability management processes.

◦ Evaluate ASM tools appropriate to the organization’s size and external footprint.

11. Assess security posture through adversary simulation, including:

◦ Schedule regular vulnerability scanning and configuration assessment against security benchmarks.

◦ Conduct periodic penetration testing and application security testing.

◦ Use adversary simulation and purple teaming to validate detection coverage against known attack

techniques (e.g., MITRE ATT&CK, Atomic Red Team).

Prepare Activity | Chapter 7 | 139

◦ Prioritize remediation using CVSS severity alongside EPSS exploitation probability, asset criticality,

exposure, and threat intelligence about active exploitation.

◦ Evaluate Breach and Attack Simulation (BAS) platforms for continuous, automated validation of

detection capabilities between manual assessments.

◦ Track remediation progress and escalate persistent vulnerabilities that exceed acceptable risk

thresholds.

12. Collect and retain logging information, including:

◦ Identify critical log sources and ensure they are collected.

◦ Configure systems to capture security-relevant events.

◦ Define retention periods based on investigation and compliance needs, distinguishing between logs

retained for active detection and those retained for compliance.

◦ Store compliance-only logs in lower-cost archives and reserve SIEM capacity for sources with

active detection use cases.

◦ Periodically review and remove SIEM log sources that have no associated detection or investigation

use cases.

◦ Protect logs from tampering and implement a central collection point.

[1] European Union, "Directive (EU) 2022/2555 on Measures for a High Common Level of Cybersecurity Across the Union (NIS2),"

December 2022, www.nis-2-directive.com/

[2] European Union, "Regulation (EU) 2022/2554 on Digital Operational Resilience for the Financial Sector (DORA)," January 2023,

www.digital-operational-resilience-act.com/

[3] ISO/IEC 27001:2022, "Information security, cybersecurity and privacy protection  — Information security management systems  —

Requirements," International Organization for Standardization, www.iso.org/standard/27001

[4] CISA, "National Cyber Incident Scoring System," www.cisa.gov/sites/default/files/2023-01/

cisa_national_cyber_incident_scoring_system_s508c.pdf

[5] InvGate, "ITIL Priority Matrix: How to Use it for Incident, Problem, Service Request, and Change Management," blog.invgate.com/

itil-priority-matrix

[6] Security.txt Project, securitytxt.org/

[7] PCI Security Standards Council, "Responding to a Cardholder Data Breach," listings.pcisecuritystandards.org/documents/

Responding_to_a_Cardholder_Data_Breach.pdf

[8] European Union, "Directive (EU) 2022/2555 on Measures for a High Common Level of Cybersecurity Across the Union (NIS2),"

December 2022, www.nis-2-directive.com/

[9] European Union, "Regulation (EU) 2022/2554 on Digital Operational Resilience for the Financial Sector (DORA)," January 2023,

www.digital-operational-resilience-act.com/

[10] European Union, "Regulation (EU) 2024/2847 on Horizontal Cybersecurity Requirements for Products with Digital Elements (Cyber

Resilience Act)," October 2024, eur-lex.europa.eu/eli/reg/2024/2847/oj

[11] Keierleber, Mark, "PowerSchool Paid Off Hackers After Huge Breach — Now They’re Extorting Districts," The 74 Million, May 2025,

www.the74million.org/article/powerschool-paid-off-hackers-after-huge-breach-now-theyre-extorting-districts/

[12] MITRE ATT&CK, attack.mitre.org/

[13] Travelers, "What Is a Data Breach Coach?" www.travelers.com/resources/business-topics/cyber-security/what-is-a-data-

breach-coach

[14] For a summary of state cybersecurity safe harbor legislation, see Wilson Elser, "States Enact Safe Harbor Laws that Provide

Affirmative Defenses in Data Breach Litigation," www.wilsonelser.com/publications/states-enact-safe-harbor-laws-that-provide-

affirmative-defenses-in-data-breach-litigation

[15] OASIS Cyber Threat Intelligence Technical Committee, "Introduction to STIX," oasis-open.github.io/cti-documentation/stix/intro

[16] GitLab, "GitLab discovers widespread npm supply chain attack," about.gitlab.com/blog/gitlab-discovers-widespread-npm-supply-

chain-attack/

[17] Sysinternals Suite, learn.microsoft.com/en-us/sysinternals/

[18] Microsoft, "eBPF for Windows," github.com/microsoft/ebpf-for-windows

[19] Eddings, Ron and Kaufmann, MJ, Attack Surface Management: Strategies and Techniques for Safeguarding Your Digital Assets ,

Function, 2024.

[20] MITRE ATT&CK, attack.mitre.org/

[21] Atomic Red Team - Library of Tests Mapped to the MITRE ATT&CK Framework, github.com/redcanaryco/atomic-red-team

[22] Barnhart, Heather, "Fear the Dark: How Dark Periods Are Threatening Forensic Investigations," SANS Institute White Paper, 2025,

www.rsaconference.com/-/media/project/rsac/rsac-website/reports/white-paper_rsac_sans_fear-the-dark.pdf

[23] SANS Institute, "2025 SOC Survey," www.sans.org/white-papers/sans-2025-soc-survey

[24] Ponemon Institute and Optiv, "2025 Cybersecurity Threat and Risk Management Report," www.optiv.com/insights/discover/

downloads/2025-cybersecurity-threat-and-risk-management-report

Prepare Activity | Chapter 7 | 141

8 Detect Activity

The detect activity is an important phase in the model, during which organizations identify potential

incidents using various information sources and analysis techniques. As incident response analysts, we

spend a significant portion of our time in detection activities, searching for signs of compromise and

potential threats that require investigation.

Figure 50 | Detect Activity Waypoint

DETECTION METHODOLOGIES

Modern detection programs employ multiple methodologies to identify threats, each with distinct strengths

and limitations. Understanding these approaches helps analysts select appropriate techniques for different

threat scenarios. This section introduces four detection methodologies: signature-based detection,

behavioral detection, machine learning detection, and hybrid approaches that combine these techniques.

Signature-Based Detection

Signature-based detection uses known patterns to identify threats, such as file hashes, byte sequences,

malicious domains, network protocol and port number indicators, etc. This approach efficiently detects

known malware and attack patterns, with generally low false positive rates. Automated systems excel at

signature-based detection, processing data quickly to identify matches.

The primary benefit of signature-based detection lies in its efficiency and accuracy for known threats.

Signatures provide high-confidence indicators that an attack has occurred, enabling rapid automated

responses such as quarantining files, blocking network connections, or alerting analysts. The rapid

processing speed of signature matching allows organizations to handle large volumes of data across many

potential threats.

The primary limitation of signature-based detection is its reactive nature. New malware variants, zero-day

exploits, and novel attack techniques evade signature detection until researchers analyze samples and

create matching patterns. Attackers who reverse-engineer detection signatures can modify their tools to

avoid matches, rendering signature-based systems ineffective against sophisticated adversaries.

Organizations relying solely on signature-based detection are likely to miss novel threats.

Behavioral Detection

Behavioral detection monitors actions rather than static indicators, identifying threats by what they do

rather than what they look like. This approach establishes baselines of normal activity and flags deviations

that warrant investigation.

Behavioral detection excels at identifying threats that signature-based approaches miss:

• Mass file encryption: Identifying patterns characteristic of ransomware

• Unusual access patterns : Reporting off-hours authentication or access to sensitive resources in

atypical ways

• Living-off-the-land techniques: Characterizing legitimate tools used in malicious ways

• Insider threats: Recognizing authorized user misuse of access privileges

Behavioral detection requires careful tuning to balance detection coverage with false-positive rates.

Analysts should work with their teams to establish accurate baselines that reflect normal organizational

operations.

SCOPING BASELINES TO BUSINESS UNITS

For large networks, a single organization-wide baseline is often too broad to produce meaningful

anomaly detection. Different business units operate in fundamentally different technical

environments, and averaging across them dilutes the very differences that make anomalies visible.

Consider a large defense contractor with separate divisions for aeronautics, mission systems, and

corporate IT. The aeronautics division generates heavy CAD/CAM file transfers and communicates

with specialized supply chain partners. The mission systems division operates classified networks

with strict access controls and minimal external connectivity. Corporate IT runs standard business

applications with predictable Office 365 and SaaS traffic patterns. A baseline built across all three

Detect Activity | Chapter 8 | 143

divisions would define "normal" so broadly that meaningful deviations disappear into the noise.

Figure 51 | Defense Contractor Baseline by Business Unit

Healthcare organizations face similar challenges. Research laboratories generate large data transfers

to cloud compute resources and access specialized databases, while clinical operations produce

predictable electronic health record (EHR) access patterns with periodic spikes during shift changes.

A unified baseline across both groups would either flag routine research transfers as anomalous or

fail to detect unusual access in the clinical environment.

Scoping baselines to business units or functional groups produces tighter definitions of normal

activity. Tighter baselines make genuine anomalies more visible and reduce false positive rates,

allowing analysts to focus investigative effort on events that actually warrant attention.

Machine Learning Detection

Machine learning enhances behavioral detection by scoring events and correlating patterns at scale.

Unsupervised learning algorithms establish baselines automatically, while supervised models classify events

as malicious or benign based on training data. These capabilities prove particularly valuable for high-volume

telemetry analysis and detecting subtle patterns across distributed systems.

Supervised models learn from labeled examples where analysts have identified events as

malicious or benign. These models excel at detecting known attack patterns but can

struggle with novel techniques not present in the training data. Unsupervised models learn

what normal behavior looks like without requiring labeled examples. This approach better

identifies unknown threats but generates more false positives when legitimate activity

deviates from established patterns.

Organizations implementing ML-based detection should understand the limitations of these systems,

including model drift, concerns about training data quality, and evasion techniques.

Model drift occurs as attacker techniques evolve and organizational environments change, gradually

degrading detection accuracy. A model trained on last year’s attack patterns may fail to recognize this year’s

techniques, particularly as adversaries adapt their methods to evade detection. Environmental drift

contributes to this problem: as organizations adopt new technologies, change business processes, or shift

workforce patterns, the baseline of "normal" activity shifts.

Training data quality impacts detection accuracy and directly influences what ML-based detection can

achieve. Models trained on incomplete datasets will fail to characterize attack techniques absent from

training data. Further, training data contaminated with mislabeled examples teaches models to make

incorrect classifications. Supervised models struggle to identify attack patterns they have never

encountered.

In model evasion attacks, adversaries craft inputs designed to bypass ML classification. Attackers who

understand how detection models work can modify their techniques to fall just below detection thresholds

or exploit deficiencies in model training. Model evasion attacks have been applied to evade a wide range of

classifiers, including malware detection, spam filtering, and image recognition systems.

Human-in-the-loop (HITL) approaches address these limitations by combining machine efficiency with

human judgment. Rather than treating ML outputs as definitive determinations, effective detection

programs use machine learning to surface high-priority signals for human review. Analysts bring contextual

understanding that models lack: knowledge of recent organizational changes, awareness of ongoing projects

that might explain unusual activity, and intuition developed through experience investigating similar alerts.

HITL workflows also create feedback loops that improve model performance over time, as analyst decisions

on flagged events provide labeled data for model retraining. Where possible, organizations should design

their detection workflows to leverage ML for initial triage and prioritization while preserving human

decision-making authority for final classification and response actions. This approach allows human

expertise to contribute to ongoing improvements in models and classifiers.

Hybrid Detection Approaches

Effective detection programs combine multiple methodologies to leverage their complementary strengths.

By integrating signature-based, behavioral, and machine learning techniques, organizations can leverage the

strengths of each approach to build robust detection capabilities while minimizing false positives and false

negatives. Many modern threat detection tools integrate signature matching, behavioral analysis, and

machine learning within a single platform.

Detection logic increasingly maps attacker tactics, techniques, and procedures to frameworks like MITRE

ATT&CK. [1]

By focusing on adversary behaviors rather than specific indicators, organizations can create

detection rules that remain effective even as attackers modify their tools. Further, the detection method,

whether signature-based, ML-based, or behavioral, becomes less important than the underlying technique

being detected. When combined, analysts can use multiple detection methods to identify threats, increasing

overall detection confidence and reducing the likelihood of false positives.

This layered approach provides defense-in-depth for detection: signatures catch known threats efficiently,

behavioral analysis identifies novel techniques, and machine learning surfaces subtle patterns that might

escape rule-based detection.

ACTIVE VS. PASSIVE DETECTION

Detection activities fall into two primary categories: passive and active detection. Passive detection occurs

when organizations learn about incidents through reports, whether from internal staff noticing unusual

activity, external partners sharing threat intelligence, or automated alerting systems triggering

notifications. This reactive approach, while necessary, often results in longer detection times and

potentially greater impact on the organization.

Detect Activity | Chapter 8 | 145

Active detection, also known as threat hunting, involves proactively searching for Events of Interest (EOIs)

within the environment.  Threat hunting analysts analyze logs, network traffic, system behavior patterns,

and other data sources to identify compromises that may have evaded automated detection systems.  This

proactive approach can significantly reduce Mean Time to Detect (MTTD), the duration between an

incident’s initiation and its discovery by the organization.

Reducing MTTD remains an ongoing priority for incident response teams, as faster

detection typically correlates with reduced incident impact.

THE TYRANNY OF INFINITE CHOICE

Incident response and threat hunting represent fundamentally different starting points for detection

work, as noted by security researcher Faan Rossouw. [2]

When responding to an incident, analysts

begin with a defined indicator: an alert has fired, a user has reported suspicious activity, or a third

party has notified the organization of a compromise. The starting point is given, and the investigation

proceeds from that anchor.

Threat hunters face a different challenge: finding unknown threats without predefined indicators. No

alert has fired. No system has flagged anything suspicious. The hunter stares at millions of log entries,

thousands of systems, and hundreds of potential threat vectors, all while nothing appears obviously

wrong. Rossouw calls this the tyranny of infinite choice : hunters face not only the question of what

to investigate, but where to begin, how to prioritize, and why one hunting hypothesis deserves

attention over countless alternatives.

Figure 52 | The Pyramid of Pain

The Pyramid of Pain, created by David Bianco in 2013, provides a mental model that can help threat

hunters escape this paralysis. [3]

The pyramid arranges adversary artifacts by the amount of "pain" that

changing them causes attackers. At the bottom sit hash values and IP addresses, which are trivial for

adversaries to modify. At the top sit tactics, techniques, and procedures (TTPs), which represent

operational methods that adversaries depend on and cannot easily abandon.

This model suggests that hunters should focus their limited time where it hurts adversaries most.

Searching for known malicious hashes or IP addresses offers little value for human hunters since

automated systems handle this efficiently at machine speed. Instead, hunters should move up the

pyramid toward behavioral indicators: beaconing patterns that suggest command-and-control

communications, suspicious process-creation chains where legitimate tools spawn each other

unexpectedly, or lateral movement techniques that reveal adversary procedures.

The pyramid also reveals a practical tradeoff. Lower-level indicators, such as hashes, provide high-

confidence detection with minimal false positives, but adversaries change them effortlessly. Higher-

level indicators like TTPs require significant expertise to detect reliably, but they expose adversary

tradecraft that persists across campaigns.

Skilled threat hunters recognize these tradeoffs and select their hunting focus based on strategic

impact rather than tactical convenience.

DETECTION DATA SOURCES

Effective detection leverages both technical and human data sources. Technical sources provide the data

needed to identify malicious activity, while human sources offer institutional knowledge, context, and

observations that automated systems might miss.

In this section, we’ll examine the technical platforms that produce detection telemetry, the human

observations that automated systems miss, and the specialized considerations that cloud-native

environments introduce.

Technical Detection Sources

Detection depends on the technical infrastructure deployed during preparation activities. In Prepare

Activity, we examined the deployment and configuration of detection infrastructure in detail. This section

focuses on how analysts use these capabilities for threat detection.

Endpoint Detection and Response (EDR) provides host-level visibility, which is essential for detecting many

attacker TTPs that generate little or no network traffic. EDR telemetry is the collection of event information

that reveals complex attack patterns, including process injection attempts, credential dumping activity,

persistence mechanism deployment, and suspicious parent-child process relationships, among other

indicators. Analysts can query EDR platforms to hunt for indicators across managed endpoints and detect

threats in the environment. The same telemetry serves as a scoping tool, identifying other compromises

that match a known indicator of compromise (IOC).

EDR systems have greatly improved endpoint security, and they represent an essential component of

modern security programs. In addition to providing organizations with the visibility needed to detect

threats, EDR platforms make these alerting and hunting capabilities accessible in a single dashboard, such as

the SentinelOne example shown in Figure 53 . These platforms often integrate with other detection,

reporting, and orchestration tools as well (including SIEM and SOAR technologies) to combine advanced

detection capabilities with other organizational reporting and control systems.

Detect Activity | Chapter 8 | 147

Figure 53 | SentinelOne EDR Dashboard

While no single EDR solution provides perfect protection, these platforms generate valuable data for

incident detection and investigation. Where endpoint systems provide focused insight into individual hosts,

network monitoring provides broad visibility across the environment.  Network Detection and Response

(NDR) and flow data enable threat detection by analyzing network traffic attributes and communication

patterns. Detection use cases include identifying C2 beaconing through connection timing analysis,

detecting lateral movement through unusual internal traffic patterns, and flagging potential data exfiltration

through anomalous outbound data volumes.

Network-based detection complements endpoint visibility by revealing attacker activity

that spans multiple systems.

Security Information and Event Management (SIEM) platforms allow analysts to perform simple searches

and more complex correlation-based detection across diverse log sources. Detection rules can identify

attack patterns spanning multiple systems, such as authentication failures followed by successful login,

privilege escalation sequences, or coordinated access to sensitive resources.  SIEM tools like Splunk, Elastic

Security, and Microsoft Sentinel provide powerful search capabilities that analysts can leverage for both

alerting and threat hunting.

Security Orchestration, Automation, and Response (SOAR) platforms reduce Mean Time to Respond (MTTR)

and risk by automating response to high-confidence alerts. When detection systems identify clear threats,

SOAR tools can immediately quarantine endpoints, block malicious IP addresses, disable compromised

accounts, and capture data for forensic analysis. This automation reduces attacker dwell time while freeing

analysts to focus on complex investigations requiring human judgment. Analysts can leverage SOAR case

management capabilities to track detection events through investigation, link related alerts, and document

findings for future reference.

OPENOBSERVE: OPEN SOURCE LOG ANALYSIS

OpenObserve is an open-source observability platform that provides log search, metrics collection,

and trace analysis in a single binary. For incident response teams, OpenObserve offers a lightweight

alternative to commercial SIEM platforms for centralized log aggregation and analysis.

OpenObserve accepts log data from common collection agents and provides a SQL-based query

interface for searching across diverse log sources. Its low resource footprint compared to traditional

log-indexing platforms makes it practical for organizations that need search capabilities without the

infrastructure overhead of a full SIEM deployment.

Figure 54 | OpenObserve Dashboard for AWS Event Analysis

OpenObserve is not a replacement for a full SIEM platform with correlation rules and automated

alerting. However, it is easy to set up and to use for teams that need to query log data quickly during

an investigation.

This is not an exhaustive list of technical detection sources. Email gateways, web proxies, cloud-native

logging, Cloud Workload Protection Platforms (CWPP), and other specialized monitoring tools all contribute

valuable data for detection activities. Organizations should use the platforms that provide the best visibility

for threat detection in their specific environments.

Detect Activity | Chapter 8 | 149

RITA: OPEN SOURCE NETWORK THREAT ANALYSIS

Real Intelligence Threat Analytics (RITA) is a free, open-source tool that applies statistical anomaly

analysis to network activity, identifying command and control communications that signature-based

detection would miss. [4]

RITA does not look for specific C2 framework signatures. Instead, it identifies

behavioral characteristics common to most C2 tools: long connection durations, beaconing intervals,

consistent packet sizes, unusual subdomain patterns, and other anomalies that distinguish attacker

activity from normal network traffic.

This approach allows RITA to detect novel C2 frameworks that have never been observed, since new

tools exhibit the same behavioral characteristics as established ones. Organizations can use RITA to

supplement commercial detection tools, gaining access to statistical analysis capabilities that some

NDR platforms lack entirely.

RITA analyzes Zeek log files, but this does not mean organizations need a full Zeek sensor

deployment. Analysts can capture network traffic at a network edge location (ideally for twenty-four

hours or longer), then convert the packet capture to Zeek logs using the zeek command-line tool, as

shown in Listing 29.

Listing 29 | Zeek Log Generation and RITA Import

$ zeek -Cr capture.pcap

$ /opt/rita/rita.sh import -l ~/zeek-logs -d InvestigationDB

...

Finished Analysis! analysis_began=1723660142 analysis_finished=1723660142

Finished Import! elapsed_time=4.8s

$ /opt/rita/rita.sh view InvestigationDB

The -C flag instructs Zeek to process packets even if they have invalid checksums, which is common

in truncated captures. RITA imports the resulting logs and applies its analysis algorithms, scoring

connections based on beacon consistency, connection duration, subdomain patterns, and other

threat indicators.

Figure 55 | RITA Threat Analysis Results

RITA’s terminal interface displays identified threats ranked by severity: critical, high, medium, low, or

none. For each threat, RITA reports the source and destination addresses, beacon score (representing

interval consistency), connection duration, prevalence among internal hosts, and protocol details. A

high beacon score indicates consistent communication intervals between two hosts, a strong

indicator of automated C2 communication.

As a free tool, RITA provides organizations with powerful network threat detection capabilities

without licensing costs. The trade-off is deployment effort: RITA runs on Linux systems and requires

analyst expertise to interpret results effectively.

Human Detection Sources

Human observations remain invaluable for detection, often identifying issues that automated systems miss.

In Prepare Activity , we examined security awareness training programs that develop this detection

capability, allowing analysts to use employee observations as a source of incident detection.

Employees frequently serve as the first line of defense for threats, reporting suspicious emails, unusual

system behavior, or social engineering attempts. Effective training and a culture that encourages reporting

suspicious events help staff recognize indicators of compromise and understand reporting procedures.

Tying in pop culture references can enhance engagement, like the Dall-E-generated poster in Figure 56

encouraging employees to report suspicious activity.

Figure 56 | The Danger Things Dall-E Poster

Detect Activity | Chapter 8 | 151

When employees report suspected incidents, even false alarms, the organization gains

detection coverage that technical systems cannot provide. Fostering a culture of vigilance

encourages reporting, enhancing overall detection capabilities.

System administrators and help desk personnel often identify anomalies during routine operations: a server

that keeps crashing, unexpected network traffic patterns, or unauthorized changes to systems they manage.

These observations, when properly escalated, can reveal ongoing compromises. Establishing clear

escalation paths during preparation ensures these observations reach the incident response team promptly.

The way SOC analysts and help desk staff respond to employee reports matters as much as whether

employees make them. A dismissive response, a slow acknowledgment, or a confusing intake process

discourages future reporting and erodes the culture of vigilance that detection programs depend on.

Organizations should develop professional, supportive communication templates for acknowledging

reports, providing status updates, and closing the loop when an investigation concludes. Even when a report

turns out to be a false alarm, a brief response thanking the employee reinforces the behavior the

organization wants to encourage.

Reinforcing the value of employee reports through timely, supportive communication helps

build a culture where staff feel empowered to contribute to detection efforts.

Third-party notifications from customers, partners, or security researchers sometimes provide the first

indication of a breach. While not ideal from a detection timeline perspective, these external reports remain

an important source of detection. A published security.txt file (RFC 9116) provides a standard channel for

researchers to reach the security team directly (see Establish External Reporting Channels ). Organizations

should establish procedures for receiving and validating external notifications as part of preparation

activities.

Cloud-Native Detection Sources

Cloud-native detection is a specialized subset of technical detection that warrants separate treatment due

to the distinct characteristics of cloud environments: ephemeral workloads, API-driven infrastructure,

shared responsibility models, and distributed architectures. The tools and techniques described in the

Technical Detection Sources section (EDR, NDR, SIEM) still apply, but cloud environments introduce

additional data sources and detection patterns that analysts should understand. Specialized detection

solutions vary depending on the cloud deployment architecture: containerized, serverless, or hybrid

environments.

The Incident Response for Cloud Systems  chapter explores cloud detection strategies in

greater depth, including provider-specific tooling and cross-cloud correlation approaches.

Container and Kubernetes Detection

Container and Kubernetes detection employs multiple approaches to identify threats in containerized

environments. Kernel-level monitoring using extended Berkeley Packet Filter (eBPF) enables systems to

observe system calls from containerized workloads, identifying unexpected processes, file system

modifications, or anomalous network connections. Container runtime socket monitoring provides an

alternative detection method by observing the Docker or containerd API for container lifecycle events,

image operations, and configuration changes that might indicate compromise or policy violations.

Logging systems, including Kubernetes audit events, provide visibility into API server activity, enabling

detection of suspicious actions such as unauthorized pod creation, privilege escalation attempts, or access

to sensitive secrets. Service mesh architectures offer additional network-level visibility between services,

capturing traffic patterns that kernel-based or runtime monitoring might miss. For traffic entering or

leaving the cluster, NDR tools at ingress points provide detection capabilities that complement mesh-level

monitoring.

Container environments present unique detection challenges due to their ephemeral

nature. When containers terminate, evidence of compromise may disappear before

analysts can investigate. Organizations should configure centralized log collection and

consider runtime detection tools that capture forensic artifacts in real time for high-

sensitivity workloads.

Serverless and Microservices Detection

Detection in agentless environments, such as serverless functions and microservices, requires alternative

approaches, as traditional endpoint agents cannot run in these execution environments.

Cloud provider logs, function telemetry, and event anomaly analysis serve as the primary sources of

detection for serverless and corresponding microservices workloads. Analysts should watch for abnormal

invocation patterns, unexpected outbound connection attempts, unusual access to secrets or environment

variables, and deviations from baseline execution characteristics (such as timeouts, throttling, and unusual

memory and CPU consumption). The ephemeral nature of these environments makes real-time detection

important since evidence exists only briefly.

Hybrid Cloud

Detection across distributed infrastructure, including hybrid and multi-cloud environments, requires

unifying telemetry and detection logic across on-premises systems and multiple cloud providers.

Organizations deploy a mix of agentless approaches, including API access and snapshot-based analysis

alongside agent-based runtime monitoring for workloads that support it. Cloud-aware network detection

and control plane analytics provide visibility into cross-environment activity that traditional tools may miss.

Native cloud detection tools from providers like AWS GuardDuty, Azure Defender, and

Google Cloud Security Command Center offer built-in detection capabilities tailored to their

respective platforms. This integration provides native visibility into cloud events but often

lacks the cross-environment correlation capabilities of third-party SIEM and EDR platforms.

Organizations that leverage multiple cloud providers should consider detection solutions

that unify telemetry and analysis across all environments for comprehensive threat

detection coverage.

Detect Activity | Chapter 8 | 153

CHALLENGES IN DETECTION

Plainly said, the task for detection teams is challenging. Wading through large volumes of data, contending

with encrypted traffic, facing adversaries actively evading detection, and addressing skills gaps within

security teams all complicate effective threat identification. Understanding these challenges helps

organizations develop strategies to work around limitations and improve detection capabilities over time.

Data Volume and Velocity

The volume and velocity of security data generated in modern environments can overwhelm analysis

capabilities and delay threat identification. Larger networks can easily generate terabytes of log data daily

from endpoints, network devices, cloud services, and applications, making comprehensive analysis difficult

even with sophisticated tools and automation.

The quantity of data from multiple, disparate sources requires careful prioritization and filtering to ensure

analysts focus on the most relevant signals.  Even with SIEM platforms and machine learning models, the

volume of alerts can exceed analyst capacity, leading to alert fatigue and missed detections. Data retention

costs add to this challenge, forcing organizations to make difficult decisions about which data to keep for

historical analysis and which to discard after short periods.

An effective strategy for managing data volume is to focus on detection-driven collection: every event

retained in a log should align with a specific detection use case. If no use case exists for a data source, there

is limited value in retaining it. This principle shifts the default from collect everything and hope it proves

useful to define what threats to detect and collect the data those detections require.

Organizations can implement detection-driven collection through several practical strategies:

• Start from use cases : Begin with specific attack detection scenarios and work backward to identify the

required data sources, filtering or discarding sources that do not support a defined detection objective.

• Tiered data retention : Implement hot, warm, and cold storage tiers that keep recent high-fidelity data

readily accessible while archiving older data to cost-effective storage for historical investigations.

• Filtering at the source : Wherever possible, remove known-good noise before ingestion by filtering

routine events, such as successful authentication from service accounts or expected network traffic

patterns.

• Intentional data disposal : Rather than degrading data quality through aggregation or sampling at

ingestion, retain full-fidelity data for the time needed for useful detection and investigation analysis,

then purge deliberately.

• Correlation-based alerting: Reduce alert volume by requiring multiple related signals before generating

analyst-facing notifications, converting dozens of low-confidence events into single high-confidence

alerts.

• Constant tuning: Regularly review and adjust detection rules, thresholds, and data sources to optimize

signal-to-noise ratios as the environment and threats change. Retain test environments so the team can

test changes to detection logic before deployment to production systems.

The goal is not to collect less data, but to collect the useful data and process it efficiently so analysts can

focus on signals that matter.

DETECTION-DRIVEN COLLECTION: AZURE STORAGE LOGGING

Azure Blob Storage diagnostic logging is a great way to illustrate the detection-driven collection

principle. A moderately active storage account can generate millions of StorageBlobLogs entries daily,

with the vast majority representing routine read requests for public content. Ingesting all of this data

into a Log Analytics workspace incurs storage costs and adds to the analyst burden without

proportional detection value.

Instead, organizations can use Data Collection Rules (DCR) with ingest-time transformations to filter

storage logs before they reach the workspace. Start by defining what threats storage logging should

detect: unauthorized access attempts, data exfiltration, and suspicious deletion activity. Then

configure a DCR transformation with a Kusto Query Language (KQL) query that evaluates each log

entry against detection criteria during ingestion.

The following KQL transformation demonstrates this filtering approach, keeping only security-

relevant events while discarding routine access patterns.

Listing 30 | DCR Transformation for Storage Log Filtering

source

| where StatusCode >= 400 1

or OperationType in ("DeleteBlob", "PutBlob",

"PutBlock", "CopyBlob") 2

or (CallerIpAddress !startswith "10."

and CallerIpAddress !startswith "192.168.") 3

| project TimeGenerated, OperationType, StatusCode,

CallerIpAddress, AccountName, ObjectKey, UserAgentHeader 4

1 Keep all failed requests (4xx and 5xx status codes).

2 Keep write and delete operations regardless of status.

3 Keep requests from IP addresses outside expected internal ranges.

4 Select only desirable columns to further reduce data ingestion volume.

This approach can reduce log volume significantly while preserving the events that actually support

threat detection. The transformation runs at ingestion time within the DCR pipeline, so filtered

events never consume workspace storage or processing resources.

Encrypted Traffic

Encryption limits network-based detection visibility into communications content. As more

communications use TLS encryption for web traffic, encrypted DNS, and VPN connections, network

monitoring tools increasingly rely on metadata analysis rather than deep packet inspection. While

encryption provides important privacy and security benefits, it also creates areas of reduced visibility for

threat hunting, where attackers can hide command-and-control communications or data exfiltration

activity.

ENCRYPTED TRAFFIC DETECTION TECHNIQUES

Since payload inspection is limited with encrypted traffic, detection focuses on metadata and

behavioral analysis:

Flow-based analysis techniques, including Encrypted Traffic Analysis (ETA), use packet sizes, timing

patterns, directionality, and TLS handshake attributes to detect anomalies without decrypting

content. Machine learning models can classify suspicious encrypted flows based on these

Detect Activity | Chapter 8 | 155

characteristics.

Certificate and handshake metadata inspection leverages certificate attributes, Server Name

Indication (SNI) values, TLS versions, cipher suites, and handshake fingerprints. Services like

Encrypted Client Hello (ECH, the successor to Encrypted Server Name Indication or ESNI) complicate

detection, providing less opportunity to glean useful information from encrypted sessions. For these

TLS connections, fingerprinting techniques such as JA4+ allow analysts to gain insight based on TLS

handshake parameters, helping identify malicious clients even when traffic is encrypted. [5]

For example, in the analysis shown in Listing 31 , we extract JA4 fingerprints from TLS Client Hello

messages in a packet capture file using TShark, the text-based version of the Wireshark packet

analyzer. TShark reveals the JA4 fingerprint t13i3110as_e8f1e7e78f70_1f22a2ca17c4 for the client

session. Using a local JA4 database in JSON format, we query for this fingerprint using jq, revealing

that the TLS connection corresponds to the AnyDesk remote desktop application, version 9.6.1.

Listing 31 | TLS JA4 Fingerprint Analysis

$ tshark -r netedge-20260105.pcapng -Y "tls.handshake.type == 1" -T fields -e

tls.handshake.ja4 | sort -u

t13i3110as_e8f1e7e78f70_1f22a2ca17c4

$ jq '.[] | select(.ja4_fingerprint == "t13i3110as_e8f1e7e78f70_1f22a2ca17c4")'

~/ja4db.json

{

"application": "AnyDesk",

"library": null,

"device": null,

"os": null,

"user_agent_string": "",

"certificate_authority": null,

"verified": false,

"notes": "AnyDesk v9.6.1",

"ja4_fingerprint": "t13i3110as_e8f1e7e78f70_1f22a2ca17c4",

"ja4_fingerprint_string": "",

"ja4s_fingerprint": "",

"ja4h_fingerprint": null,

"ja4x_fingerprint": null,

"ja4t_fingerprint": null,

"ja4ts_fingerprint": null,

"ja4tscan_fingerprint": null

}

JA4 fingerprinting provides valuable context for encrypted traffic analysis, enabling analysts to

identify applications and clients even when payloads are inaccessible and other privacy controls are

applied to protect client and server details.

Behavioral context analysis provides additional insight for analysts when working with encrypted traffic.

This approach focuses on detecting unusual patterns indicative of EOIs in encrypted network activity.

Indicators include abnormal outbound data volumes, connections to unusual destinations, and new

encrypted channels from systems that do not normally generate such traffic.

Organizations should focus network detection efforts on connection metadata, including destination

addresses, connection timing and duration, data volume patterns, and certificate information that remains

visible even when content is encrypted. TLS inspection capabilities for internal systems where policy

permits can provide a valuable source of detection data for threat hunting and subsequent investigation.

Combined, these metadata and behavioral approaches allow organizations to maintain meaningful detection

coverage even as encryption adoption continues to grow.

Adversary Evasion

Sophisticated attackers actively work to evade detection, treating security tools as obstacles to overcome

rather than insurmountable barriers. Understanding common evasion techniques helps analysts recognize

when attackers are attempting to hide their activities.

Attackers frequently target logging infrastructure to remove evidence of their activities. Clearing Windows

Event Logs, disabling audit policies, or timestomping files to obscure activity timelines are common

techniques. Analysts should monitor for gaps in log data and unexpected changes to logging configurations

as potential indicators of compromise. The Scope chapter’s Anti-Forensic Techniques  section examines

these further.

Rather than deploying custom malware that signature-based detection might catch, attackers increasingly

use legitimate system tools for malicious purposes. PowerShell, Windows Management Instrumentation

(WMI), PsExec, and other built-in utilities provide powerful capabilities that attackers exploit. These tools

generate activity that blends with normal administrative operations, making behavioral detection essential.

Attackers who understand detection thresholds can operate just below them. Data exfiltration spread

across many small transfers rather than one large transfer, authentication attempts spaced to avoid lockout

policies, and lateral movement timed to coincide with normal business hours all exploit threshold-based

detection limitations.

THE PRE-ATTACK LAB

Attackers with disciplined tradecraft test their techniques before deploying them against targets.

Sophisticated threat actors maintain lab environments that mirror common enterprise security

stacks, testing malware and attack procedures against EDR products, SIEM detection rules, and

network monitoring tools.

The 2022 Conti ransomware leaks revealed the extent of this practice. [6]

Internal chat logs showed

the group budgeted several thousand dollars monthly to purchase security and antivirus tools for

continuous testing against their malware. The group also invested $60,000 to acquire a legitimate

Cobalt Strike license through an intermediary company. In one chat, Conti manager Reshaev

instructed a subordinate on operational security:

“Install EDR on every computer (e.g., Sentinel, Cylance, CrowdStrike); set up a more complex

storage system; protect LSAS dumps on all computers...

This reality means detection capabilities require continuous evolution. Detection rules that worked

for previous incident detection may fail against attackers who have adapted. Organizations should

assume that determined adversaries will eventually bypass any detection methods, making layered

Detect Activity | Chapter 8 | 157

detection strategies and continuous improvement essential.

As attackers adapt their techniques, detection teams cannot solely rely on endpoint signatures or static

rules. Threat intelligence on emerging evasion techniques, regular updates to detection rules, and purple-

team exercises that test detection coverage all contribute to maintaining effective detection capabilities.

Purple teaming is particularly valuable for reducing the gap between detection capability and attacker

tradecraft. In a purple-team exercise, the red team demonstrates specific attack techniques while the blue

team observes the resulting telemetry and develops or refines detections in near real time. This

collaborative approach builds detection engineering skills that are difficult to develop from alerts alone. It

also serves as a practical litmus test: if the SOC cannot track an internal red team operating from a known

machine on the organization’s own network, detecting a sophisticated external adversary will be

significantly more difficult.

Skills Gap

The skills gap in security operations means many organizations struggle to effectively use their detection

tools and interpret the alerts they generate. The shortage of experienced analysts who can tune detection

systems, investigate alerts, perform threat hunting, and develop new detection rules limits detection

effectiveness across the industry.

Entry-level analysts often lack the deep technical knowledge needed to distinguish sophisticated attacks

from benign anomalies, while experienced analysts are in high demand and difficult to retain. Organizations

should invest in training programs that develop detection skills within their teams, leverage managed

security service providers (MSSPs) to supplement internal capabilities, and implement knowledge

management systems that capture detection expertise for future reference.

Automation and AI-assisted detection capabilities can help bridge some of the skills gap by providing

analysts with context and recommendations (see Accelerating Incident Response with AI ). While valuable,

these tools also require oversight from experienced personnel to avoid missing threats or creating excessive

false positives.

DETECT ACTIVITY EXAMPLES

The following examples illustrate where detection is an important part of the incident response process.

The External Breach Hunter

Yoshihiro, a tier-1 SOC analyst on duty, opened an email on Tuesday morning with the subject line "Security

Issue - Exposed Administrative Systems." The message had arrived through the security disclosure address

published in the organization’s security.txt file, routing it directly to the security team rather than to a

general support queue. The sender, Tom Liston, described exposed administrative portals and suspicious

accounts on the organization’s patient management system.

Listing 32 | Excerpt from Liston’s Disclosure Email

From: Tom Liston <tliston@yourflyis0pen.com>

To: security@genusight.com

Subject: Genusight Medical Security Issue - Exposed Administrative Systems

Hello,

I identify compromised systems online as a hobby (yes, really). While scanning external attack

surfaces this week I came across what looks like an active compromise in your patient management

system.

The admin interface at https://admin.genusight.com/login

is publicly reachable. From what I can see, the system was protected by default or weak

credentials that an attacker has already taken advantage of.

Two accounts on the system stand out:

admin_backup (created 2026-03-02)

svc_temp     (created 2026-03-05)

Neither matches the adm_firstname.lastname convention I can see elsewhere in your environment.

Both have been authenticating from IP addresses in Eastern Europe over the past 45 days.

Authentication logs are attached.

An outside notification usually means internal detection missed something, and that’s worth a

look too.

Glad to answer questions.

Regards,

Tom Liston

https://yourflyis0pen.com/

Yoshihiro recognized the sender’s name. Tom Liston is a longtime handler at the SANS Internet Storm

Center who has made a hobby of identifying compromised systems. However, recognition of the sender

does not substitute for verification.

Yoshihiro approached the report with healthy skepticism. He had seen plenty of false alarms from well-

meaning but mistaken researchers, and more than a fair share of social engineering attempts disguised as

security notifications. Rather than relying on any single indicator, he worked through a structured

verification process before deciding how to respond.

He first validated that the URLs in the email pointed to actual organizational infrastructure rather than

lookalike domains that a social engineer might use to impersonate a real system. Next, he cross-referenced

the suspicious account names against the (correctly-asserted) standard adm_firstname.lastname naming

convention, confirming that admin_backup and svc_temp did indeed exist and did not match the policy-

dictated provisioning pattern.

He then reviewed the authentication logs attached to the report, geolocating the source IP addresses and

confirming that the organization had no business presence or remote workers in the regions shown. Finally,

he assessed the overall quality of the report: specific technical detail, reproducible evidence, and a clear

disclosure timeline all suggested a legitimate researcher rather than an attacker attempting to social-

engineer an incident response.

Yoshihiro escalated the report to the tier-2 SOC analysts with a summary of the validated findings. This

Detect Activity | Chapter 8 | 159

detection event will transition to the verify and triage phase, where the team will validate the specific claims

and determine the appropriate response. The combination of a published disclosure channel, structured

triage, and multi-factor validation transformed a message that might otherwise have languished in a help

desk queue into actionable threat intelligence.

The SIEM Wizard

Active threat hunting enables analysts to proactively identify threats that automated alerting systems might

miss, particularly when searching for suspicious patterns rather than known malicious indicators. Mature

detection teams operate threat hunting as a documented program rather than an ad hoc effort, tracking

hunt hypotheses, target data sources, cadence, and last-run dates in a table that supports both coverage

reviews and regulator inquiries. See Establish a Threat Hunting Program  in the Prepare chapter for

guidance on designing and documenting this program.

Lucía, a threat hunter on the security operations center (SOC) team, ran beaconing detection as one of the

recurring hunts in her team’s program. Beaconing behavior in outbound traffic is a common indicator of

command and control communication, where compromised systems regularly check in with attacker

infrastructure. Beaconing is particularly suspicious because legitimate applications rarely communicate

with external servers at perfectly consistent intervals, while malware often implements regular callback

schedules to receive commands or exfiltrate data.

Lucía opened Kibana and crafted an Elasticsearch aggregation query to identify URLs with consistent access

patterns over the past seven days, shown in Listing 33. Her query grouped all proxy requests by destination

URL and analyzed the distribution of requests over time, looking for patterns that suggested automated,

scheduled communication rather than human-driven web browsing.

Listing 33 | Elasticsearch Query for Beaconing Detection

{

"size": 0, 1

"query": {

"range": {

"@timestamp": {

"gte": "now-7d", 2

"lte": "now"

}

}

},

"aggs": {

"by_url": {

"terms": {

"field": "url.keyword", 3

"size": 500

},

"aggs": {

"over_time": {

"auto_date_histogram": {

"field": "@timestamp", 4

"buckets": 50

}

},

"request_count": {

"value_count": { 5

"field": "@timestamp"

}

}

}

}

}

}

1 Don’t return individual documents, only aggregation results.

2 Search only the past seven days of proxy log data.

3 Group all requests by destination URL.

4 Create a histogram showing when requests occurred for each URL.

5 Count the total number of requests for each URL.

The query returned hundreds of URLs with varying access patterns. Lucía reviewed the results, examining

the time distribution histograms for each URL. Most showed the irregular patterns typical of human access:

bursts of activity during business hours, gaps during lunch, quiet periods overnight. Others exhibited

consistent patterns from legitimate automated systems like software update checkers and monitoring tools,

which Lucía recognized from previous hunting sessions.

One URL immediately caught her attention: api.cloudserv-cdn.com showed exactly 2,016 requests over the

past seven days, with the histogram displaying perfectly spaced intervals. Lucía calculated the timing: a

week of requests at that volume worked out to exactly five minutes between each request. This precision in

timing was unusual, and alarming.

Lucía dug deeper into this suspicious URL, crafting a follow-up query to identify which client systems were

accessing it and examining the specific timestamps. She found that all requests originated from a single

workstation in the finance department, and the timestamps confirmed the pattern: requests occurred at

exactly :05, :10, and every five minutes thereafter with no variation in timing. The domain itself raised

additional concerns when she checked threat intelligence feeds. It was registered only three weeks ago

through a registrar frequently abused by threat actors for cheap, rapidly provisioned domains, and the

hosting provider was associated with malicious infrastructure.

Lucía documented her findings, noting the suspicious beaconing pattern, the recently registered domain,

the consistent five-minute interval, and the affected workstation details. She escalated this detection event

to the incident response team for verification and triage, where they would investigate whether the

workstation was genuinely compromised or if there was a legitimate explanation for this highly regular

communication pattern.

DETECT: STEP-BY-STEP

The following steps provide a condensed reference for detection activities. Each step corresponds to topics

covered earlier in this chapter, organized for use when establishing detection sources, hunting for threats,

and refining detection capabilities.

This step-by-step guide is available for download in PDF and Markdown formats on the

companion website at dynamicincidentresponse.com.

Detect Activity | Chapter 8 | 161
