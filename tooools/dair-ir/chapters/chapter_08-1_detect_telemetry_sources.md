# Chapter 08-1: Detection: Telemetry Data Sources, ATT&CK Mapping & Architecture Baselines

> Modular Sub-Chapter | Source: DAIR-IR Framework

---

# Chapter 8: Detect Activity: Monitoring & Detection Engineering

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

◦ Assign specific individuals responsible for keeping documents current and include document review in their performance expectations.

Step 3. Proactive Prevention and Detection

1. Implement Cyber Threat Intelligence (CTI) capabilities, including:

◦ Identify appropriate intelligence sources (commercial, ISAC, government, OSINT).

◦ Establish processes to review and operationalize intelligence.

◦ Integrate IOCs into detection systems using standardized formats (STIX 2.1).

◦ Use intelligence to prioritize defenses and inform response.

◦ Evaluate CTI platforms to centralize intelligence management, correlate indicators across sources, and support investigation pivots during active incidents.

2. Develop processes for software management, including:

◦ Implement risk-based patch management with defined timelines.

◦ Maintain configuration management with version control.

◦ Track software inventory including version information.

◦ Maintain Software Bill of Materials (SBOM) data to identify systems affected by vulnerabilities in third-party components.

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

◦ Deploy a supplemental telemetry agent across endpoints lacking sufficient native or EDR-provided event detail.

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

◦ Maintain detection rule lifecycle: retire outdated rules, update for environment changes, and document rule intent and logic.

8. Establish a threat hunting program, including:

◦ Maintain a catalog of hunt hypotheses tied to MITRE ATT&CK tactics and techniques.

◦ Identify target data sources for each hypothesis (proxy, DNS, process creation, authentication).

◦ Define cadence for each hypothesis based on risk priority and data freshness.

◦ Track hypothesis, data source, cadence, last-run date, threat hunting analyst, and findings in an audit table.

◦ Promote hunt findings into automated detection rules to feed the detection engineering program.

9. Catalog critical data, systems, and infrastructure, including:

◦ Maintain an accurate inventory of hardware, software, data assets, cloud resources, and third-party connections.

◦ Identify and document critical assets essential to organizational survival.

◦ Classify assets by business criticality.

◦ Document network architecture and dependencies.

◦ Maintain both local offline copies and access to authoritative sources maintained by owning teams.

◦ Implement processes to maintain inventory accuracy.

10. Monitor the attack surface, including:

◦ Continuously discover and evaluate externally visible assets (internet-facing services, cloud resources, domains, certificates, exposed APIs).

◦ Compare discovered assets against the internal asset inventory to identify gaps.

◦ Feed ASM findings into hardening and vulnerability management processes.

◦ Evaluate ASM tools appropriate to the organization’s size and external footprint.

11. Assess security posture through adversary simulation, including:

◦ Schedule regular vulnerability scanning and configuration assessment against security benchmarks.

◦ Conduct periodic penetration testing and application security testing.

◦ Use adversary simulation and purple teaming to validate detection coverage against known attack techniques (e.g., MITRE ATT&CK, Atomic Red Team).

◦ Prioritize remediation using CVSS severity alongside EPSS exploitation probability, asset criticality, exposure, and threat intelligence about active exploitation.

◦ Evaluate Breach and Attack Simulation (BAS) platforms for continuous, automated validation of detection capabilities between manual assessments.

◦ Track remediation progress and escalate persistent vulnerabilities that exceed acceptable risk thresholds.

12. Collect and retain logging information, including:

◦ Identify critical log sources and ensure they are collected.

◦ Configure systems to capture security-relevant events.

◦ Define retention periods based on investigation and compliance needs, distinguishing between logs retained for active detection and those retained for compliance.

◦ Store compliance-only logs in lower-cost archives and reserve SIEM capacity for sources with active detection use cases.

◦ Periodically review and remove SIEM log sources that have no associated detection or investigation use cases.

◦ Protect logs from tampering and implement a central collection point.

Requirements," International Organization for Standardization, www.iso.org/standard/27001 Resilience Act)," October 2024, eur-lex.europa.eu/eli/reg/2024/2847/oj Affirmative Defenses in Data Breach Litigation," www.wilsonelser.com/publications/states-enact-safe-harbor-laws-that-provide-affirmative-defenses-in-data-breach-litigation Function, 2024.

8 Detect Activity The detect activity is an important phase in the model, during which organizations identify potential incidents using various information sources and analysis techniques. As incident response analysts, we spend a significant portion of our time in detection activities, searching for signs of compromise and potential threats that require investigation.

Figure 50 | Detect Activity Waypoint

DETECTION METHODOLOGIES

Modern detection programs employ multiple methodologies to identify threats, each with distinct strengths and limitations. Understanding these approaches helps analysts select appropriate techniques for different threat scenarios. This section introduces four detection methodologies: signature-based detection, behavioral detection, machine learning detection, and hybrid approaches that combine these techniques.

Signature-Based Detection

Signature-based detection uses known patterns to identify threats, such as file hashes, byte sequences, malicious domains, network protocol and port number indicators, etc. This approach efficiently detects known malware and attack patterns, with generally low false positive rates. Automated systems excel at signature-based detection, processing data quickly to identify matches.

The primary benefit of signature-based detection lies in its efficiency and accuracy for known threats.

Signatures provide high-confidence indicators that an attack has occurred, enabling rapid automated responses such as quarantining files, blocking network connections, or alerting analysts. The rapid processing speed of signature matching allows organizations to handle large volumes of data across many potential threats.

The primary limitation of signature-based detection is its reactive nature. New malware variants, zero-day exploits, and novel attack techniques evade signature detection until researchers analyze samples and create matching patterns. Attackers who reverse-engineer detection signatures can modify their tools to avoid matches, rendering signature-based systems ineffective against sophisticated adversaries.

Organizations relying solely on signature-based detection are likely to miss novel threats.

Behavioral Detection

Behavioral detection monitors actions rather than static indicators, identifying threats by what they do rather than what they look like. This approach establishes baselines of normal activity and flags deviations that warrant investigation.

Behavioral detection excels at identifying threats that signature-based approaches miss:

• Mass file encryption: Identifying patterns characteristic of ransomware

• Unusual access patterns : Reporting off-hours authentication or access to sensitive resources in atypical ways

• Living-off-the-land techniques: Characterizing legitimate tools used in malicious ways

• Insider threats: Recognizing authorized user misuse of access privileges divisions would define "normal" so broadly that meaningful deviations disappear into the noise.

Figure 51 | Defense Contractor Baseline by Business Unit

Healthcare organizations face similar challenges. Research laboratories generate large data transfers to cloud compute resources and access specialized databases, while clinical operations produce predictable electronic health record (EHR) access patterns with periodic spikes during shift changes.

A unified baseline across both groups would either flag routine research transfers as anomalous or fail to detect unusual access in the clinical environment.

Scoping baselines to business units or functional groups produces tighter definitions of normal activity. Tighter baselines make genuine anomalies more visible and reduce false positive rates, allowing analysts to focus investigative effort on events that actually warrant attention.

Machine Learning Detection

Machine learning enhances behavioral detection by scoring events and correlating patterns at scale.

Unsupervised learning algorithms establish baselines automatically, while supervised models classify events as malicious or benign based on training data. These capabilities prove particularly valuable for high-volume telemetry analysis and detecting subtle patterns across distributed systems.

Supervised models learn from labeled examples where analysts have identified events as malicious or benign. These models excel at detecting known attack patterns but can struggle with novel techniques not present in the training data. Unsupervised models learn what normal behavior looks like without requiring labeled examples. This approach better identifies unknown threats but generates more false positives when legitimate activity deviates from established patterns.

Organizations implementing ML-based detection should understand the limitations of these systems, including model drift, concerns about training data quality, and evasion techniques.

Model drift occurs as attacker techniques evolve and organizational environments change, gradually degrading detection accuracy. A model trained on last year’s attack patterns may fail to recognize this year’s techniques, particularly as adversaries adapt their methods to evade detection. Environmental drift contributes to this problem: as organizations adopt new technologies, change business processes, or shift workforce patterns, the baseline of "normal" activity shifts.

Training data quality impacts detection accuracy and directly influences what ML-based detection can achieve. Models trained on incomplete datasets will fail to characterize attack techniques absent from training data. Further, training data contaminated with mislabeled examples teaches models to make incorrect classifications. Supervised models struggle to identify attack patterns they have never encountered.

In model evasion attacks, adversaries craft inputs designed to bypass ML classification. Attackers who understand how detection models work can modify their techniques to fall just below detection thresholds or exploit deficiencies in model training. Model evasion attacks have been applied to evade a wide range of classifiers, including malware detection, spam filtering, and image recognition systems.

Human-in-the-loop (HITL) approaches address these limitations by combining machine efficiency with human judgment. Rather than treating ML outputs as definitive determinations, effective detection programs use machine learning to surface high-priority signals for human review. Analysts bring contextual understanding that models lack: knowledge of recent organizational changes, awareness of ongoing projects that might explain unusual activity, and intuition developed through experience investigating similar alerts.

HITL workflows also create feedback loops that improve model performance over time, as analyst decisions on flagged events provide labeled data for model retraining. Where possible, organizations should design their detection workflows to utilize ML for initial triage and prioritization while preserving human decision-making authority for final classification and response actions. This approach allows human expertise to contribute to ongoing improvements in models and classifiers.

Hybrid Detection Approaches

Effective detection programs combine multiple methodologies to utilize their complementary strengths.

By integrating signature-based, behavioral, and machine learning techniques, organizations can leverage the strengths of each approach to build robust detection capabilities while minimizing false positives and false negatives. Many modern threat detection tools integrate signature matching, behavioral analysis, and machine learning within a single platform.

Detection logic increasingly maps attacker tactics, techniques, and procedures to frameworks like MITRE ATT&CK. [1] By focusing on adversary behaviors rather than specific indicators, organizations can create detection rules that remain effective even as attackers modify their tools. Further, the detection method, whether signature-based, ML-based, or behavioral, becomes less important than the underlying technique being detected. When combined, analysts can use multiple detection methods to identify threats, increasing overall detection confidence and reducing the likelihood of false positives.

This layered approach provides defense-in-depth for detection: signatures catch known threats efficiently, behavioral analysis identifies novel techniques, and machine learning surfaces subtle patterns that might escape rule-based detection.

ACTIVE VS. PASSIVE DETECTION

Detection activities fall into two primary categories: passive and active detection. Passive detection occurs Active detection, also known as threat hunting, involves proactively searching for Events of Interest (EOIs) within the environment.  Threat hunting analysts analyze logs, network traffic, system behavior patterns, and other data sources to identify compromises that may have evaded automated detection systems.  This proactive approach can substantially reduce Mean Time to Detect (MTTD), the duration between an incident’s initiation and its discovery by the organization.

Reducing MTTD remains an ongoing priority for incident response teams, as faster detection typically correlates with reduced incident impact.

THE TYRANNY OF INFINITE CHOICE

Incident response and threat hunting represent fundamentally different starting points for detection work, as noted by security researcher Faan Rossouw. [2] When responding to an incident, analysts begin with a defined indicator: an alert has fired, a user has reported suspicious activity, or a third party has notified the organization of a compromise. The starting point is given, and the investigation proceeds from that anchor.

Threat hunters face a different challenge: finding unknown threats without predefined indicators. No alert has fired. No system has flagged anything suspicious. The hunter stares at millions of log entries, thousands of systems, and hundreds of potential threat vectors, all while nothing appears obviously wrong. Rossouw calls this the tyranny of infinite choice : hunters face not only the question of what to investigate, but where to begin, how to prioritize, and why one hunting hypothesis deserves attention over countless alternatives.

Figure 52 | The Pyramid of Pain

The Pyramid of Pain, created by David Bianco in 2013, provides a mental model that can help threat hunters escape this paralysis. [3] The pyramid arranges adversary artifacts by the amount of "pain" that changing them causes attackers. At the bottom sit hash values and IP addresses, which are trivial for adversaries to modify. At the top sit tactics, techniques, and procedures (TTPs), which represent operational methods that adversaries depend on and cannot easily abandon.

This model suggests that hunters should focus their limited time where it hurts adversaries most.

Searching for known malicious hashes or IP addresses offers little value for human hunters since automated systems handle this efficiently at machine speed. Instead, hunters should move up the pyramid toward behavioral indicators: beaconing patterns that suggest command-and-control communications, suspicious process-creation chains where legitimate tools spawn each other unexpectedly, or lateral movement techniques that reveal adversary procedures.

The pyramid also reveals a practical tradeoff. Lower-level indicators, such as hashes, provide high-confidence detection with minimal false positives, but adversaries change them effortlessly. Higher-level indicators like TTPs require significant expertise to detect reliably, but they expose adversary tradecraft that persists across campaigns.

Skilled threat hunters recognize these tradeoffs and select their hunting focus based on strategic impact rather than tactical convenience.

DETECTION DATA SOURCES

Effective detection leverages both technical and human data sources. Technical sources provide the data needed to identify malicious activity, while human sources offer institutional knowledge, context, and observations that automated systems might miss.

In this section, we’ll examine the technical platforms that produce detection telemetry, the human observations that automated systems miss, and the specialized considerations that cloud-native environments introduce.

Technical Detection Sources

Detection depends on the technical infrastructure deployed during preparation activities. In Prepare Activity, we examined the deployment and configuration of detection infrastructure in detail. This section focuses on how analysts use these capabilities for threat detection.

Endpoint Detection and Response (EDR) provides host-level visibility, which is essential for detecting many attacker TTPs that generate little or no network traffic. EDR telemetry is the collection of event information that reveals complex attack patterns, including process injection attempts, credential dumping activity, persistence mechanism deployment, and suspicious parent-child process relationships, among other indicators. Analysts can query EDR platforms to hunt for indicators across managed endpoints and detect threats in the environment. The same telemetry serves as a scoping tool, identifying other compromises that match a known indicator of compromise (IOC).

EDR systems have greatly improved endpoint security, and they represent an essential component of modern security programs. In addition to providing organizations with the visibility needed to detect threats, EDR platforms make these alerting and hunting capabilities accessible in a single dashboard, such as the SentinelOne example shown in Figure 53 . These platforms often integrate with other detection, reporting, and orchestration tools as well (including SIEM and SOAR technologies) to combine advanced

Figure 53 | SentinelOne EDR Dashboard

While no single EDR solution provides perfect protection, these platforms generate valuable data for incident detection and investigation. Where endpoint systems provide focused insight into individual hosts, network monitoring provides broad visibility across the environment.  Network Detection and Response (NDR) and flow data enable threat detection by analyzing network traffic attributes and communication patterns. Detection use cases include identifying C2 beaconing through connection timing analysis, detecting lateral movement through unusual internal traffic patterns, and flagging potential data exfiltration through anomalous outbound data volumes.

Network-based detection complements endpoint visibility by revealing attacker activity that spans multiple systems.

Security Information and Event Management (SIEM) platforms allow analysts to perform simple searches and more complex correlation-based detection across diverse log sources. Detection rules can identify attack patterns spanning multiple systems, such as authentication failures followed by successful login, privilege escalation sequences, or coordinated access to sensitive resources.  SIEM tools like Splunk, Elastic Security, and Microsoft Sentinel provide powerful search capabilities that analysts can leverage for both alerting and threat hunting.

Security Orchestration, Automation, and Response (SOAR) platforms reduce Mean Time to Respond (MTTR) and risk by automating response to high-confidence alerts. When detection systems identify clear threats, SOAR tools can immediately quarantine endpoints, block malicious IP addresses, disable compromised accounts, and capture data for forensic analysis. This automation reduces attacker dwell time while freeing analysts to focus on complex investigations requiring human judgment. Analysts can leverage SOAR case management capabilities to track detection events through investigation, link related alerts, and document findings for future reference.

OPENOBSERVE: OPEN SOURCE LOG ANALYSIS

OpenObserve is an open-source observability platform that provides log search, metrics collection, and trace analysis in a single binary. For incident response teams, OpenObserve offers a lightweight alternative to commercial SIEM platforms for centralized log aggregation and analysis.

OpenObserve accepts log data from common collection agents and provides a SQL-based query interface for searching across diverse log sources. Its low resource footprint compared to traditional log-indexing platforms makes it practical for organizations that need search capabilities without the infrastructure overhead of a full SIEM deployment.

Figure 54 | OpenObserve Dashboard for AWS Event Analysis

OpenObserve is not a replacement for a full SIEM platform with correlation rules and automated alerting. However, it is easy to set up and to use for teams that need to query log data quickly during an investigation.

This is not an exhaustive list of technical detection sources. Email gateways, web proxies, cloud-native logging, Cloud Workload Protection Platforms (CWPP), and other specialized monitoring tools all contribute

RITA: OPEN SOURCE NETWORK THREAT ANALYSIS

Real Intelligence Threat Analytics (RITA) is a free, open-source tool that applies statistical anomaly analysis to network activity, identifying command and control communications that signature-based detection would miss. [4] RITA does not look for specific C2 framework signatures. Instead, it identifies behavioral characteristics common to most C2 tools: long connection durations, beaconing intervals, consistent packet sizes, unusual subdomain patterns, and other anomalies that distinguish attacker activity from normal network traffic.

This approach allows RITA to detect novel C2 frameworks that have never been observed, since new tools exhibit the same behavioral characteristics as established ones. Organizations can use RITA to supplement commercial detection tools, gaining access to statistical analysis capabilities that some NDR platforms lack entirely.

RITA analyzes Zeek log files, but this does not mean organizations need a full Zeek sensor deployment. Analysts can capture network traffic at a network edge location (ideally for twenty-four hours or longer), then convert the packet capture to Zeek logs using the zeek command-line tool, as shown in Listing 29.

Listing 29 | Zeek Log Generation and RITA Import

$ zeek -Cr capture.pcap

$ /opt/rita/rita.sh import -l ~/zeek-logs -d InvestigationDB

...

Finished Analysis! analysis_began=1723660142 analysis_finished=1723660142 Finished Import! elapsed_time=4.8s

$ /opt/rita/rita.sh view InvestigationDB

The -C flag instructs Zeek to process packets even if they have invalid checksums, which is common in truncated captures. RITA imports the resulting logs and applies its analysis algorithms, scoring connections based on beacon consistency, connection duration, subdomain patterns, and other threat indicators.

Figure 55 | RITA Threat Analysis Results

RITA’s terminal interface displays identified threats ranked by severity: critical, high, medium, low, or none. For each threat, RITA reports the source and destination addresses, beacon score (representing interval consistency), connection duration, prevalence among internal hosts, and protocol details. A high beacon score indicates consistent communication intervals between two hosts, a strong indicator of automated C2 communication.

As a free tool, RITA provides organizations with powerful network threat detection capabilities without licensing costs. The trade-off is deployment effort: RITA runs on Linux systems and requires analyst expertise to interpret results effectively.

Human Detection Sources
