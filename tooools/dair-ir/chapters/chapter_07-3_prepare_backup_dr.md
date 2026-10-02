# Chapter 07-3: Preparation: Golden Backups, Disaster Recovery & Readiness Drills

> Modular Sub-Chapter | Source: DAIR-IR Framework

---

observed indicators against known threat signatures. NDR solutions reduce the manual analysis burden on security teams by automatically identifying suspicious activity thereby reducing the mean time to detect (MTTD) for active threats.

One particularly valuable feature of NDR platforms is the ability to integrate CTI insights to detect emerging threats. By incorporating IOCs from commercial and free CTI feeds, ISACs, and government sources, NDR platforms can identify communications with known malicious infrastructure, detect command-and-control patterns associated with specific threat actors, and flag file transfers matching known malware signatures.

This integration transforms NDR into a platform that combines behavioral anomalies with known-threat identification, providing broader coverage across the threat landscape.

Many NDR systems also support event correlation, combining host-based telemetry with network data to provide richer context for detection and investigation. This correlation enables analysts to connect network-level indicators with endpoint activity, building a more complete picture of attacker behavior.

Position network monitoring at critical points, including internet egress, network segment boundaries, and connections to sensitive systems. For broad detection and investigative opportunities, organizations should deploy monitoring sensors at points where traffic enters and leaves networks (North-South traffic) and between internal networks (East-West traffic) where lateral movement occurs.

Invest in Detection Engineering

Deploying security monitoring tools is a necessary first step, but the tools themselves only provide value when backed by a sustained detection engineering practice. Detection engineering is the discipline of designing, building, testing, and maintaining the detection rules and logic that turn raw telemetry into actionable insight. Without ongoing investment in this discipline, organizations accumulate monitoring tools that generate noise rather than insight.

A monitoring tool without well-maintained detection rules is an expensive log collector.

Detection engineering connects the endpoint, network, and log monitoring capabilities described in the preceding sections. An EDR deployment provides telemetry, but a detection engineer writes the rules to identify suspicious process relationships or unapproved credential access patterns using that telemetry. A SIEM ingests logs, but detection engineers develop the correlation logic that catches lateral movement across multiple log sources. NDR platforms analyze traffic, but detection engineers define which behavioral patterns warrant analyst attention.

Effective detection engineering programs include several ongoing activities:

• Rule development : Writing detection rules tied to specific attacker techniques, informed by threat intelligence and mapped to frameworks like MITRE ATT&CK.

• Testing and validation : Verifying that detection rules fire correctly using adversary simulation tools (such as Atomic Red Team).

• Tuning: Reducing false positives by refining rule logic based on the organization’s environment, and removing or revising rules that generate alerts without investigative value.

• Coverage tracking: Mapping detection rules against the ATT&CK matrix to identify which techniques are covered and where gaps remain.

• Lifecycle management : Retiring outdated rules, updating rules when the environment changes, and documenting the intent and logic behind each rule so others can maintain them.

Organizations that treat detection as a one-time configuration task rather than an ongoing engineering practice inevitably fall behind as attackers adapt their techniques.

Establish a Threat Hunting Program

Threat hunting complements automated detection by using analyst expertise to search proactively for threats that rules and signatures miss. Rather than waiting for alerts, analysts formulate hypotheses about how attackers might operate in the environment, then investigate the telemetry for evidence that those hypotheses are true. Treating this work as a documented program rather than an ad hoc effort ensures coverage across the threats the organization cares about and provides evidence of diligence under regulator review.

A threat hunting program typically includes the following elements:

• Hypothesis catalog: A maintained list of hunt hypotheses tied to MITRE ATT&CK tactics and techniques (e.g., command and control beaconing, lateral movement via WMI, data staging in unusual directories).

• Target data sources: For each hypothesis, the logs or telemetry required to investigate it, such as proxy logs, DNS queries, or process creation events.

• Cadence: How often each hypothesis is reviewed, prioritized by risk and data freshness.

• Audit trail: A tracking data set capturing hypothesis, data source, cadence, last-run date, analyst, and findings, supporting both internal coverage reviews and external regulator inquiries.

• Feedback loop: A process for promoting findings from hunts into automated detection rules, ensuring the detection engineering program benefits from analyst discoveries.

Organizations just starting with threat hunting can begin with a small set of high-priority hypotheses and grow the catalog over time as the team builds expertise. Documenting the program also protects the organization’s investment in hunting activity: when staff turnover occurs, the next analyst inherits the hypothesis catalog and knows where the previous team member left off.

Catalog All Critical Data, Systems, and Infrastructure

A comprehensive asset inventory enables rapid scoping during incidents and ensures critical systems receive appropriate protection. When responders can quickly identify which systems exist, who owns them, and how they integrate with other resources, the incident response team can complete scoping more quickly and with greater accuracy and insight. Without accurate inventory, responders waste time identifying affected systems, leading to longer delays in initial verification of the incident, and may miss the compromise of unknown or forgotten assets.

Start by documenting assets using the broad categories in Table 11. Each category captures different aspects of the environment that become relevant during incident response. Hardware and software inventories help identify affected systems, while network architecture documentation is valuable to understand potential lateral movement paths. Data asset records indicate what sensitive information may be at risk, and third-party connection documentation identifies external parties who may need notification or will be asked to provide insight for investigative analysis.

Table 11 | Asset Inventory Categories

CATEGORY ELEMENTS TO DOCUMENT Hardware Assets Servers, workstations, network devices, mobile devices, and IoT systems with location, owner, and criticality.

Software Assets Applications, operating systems, and middleware with version information, licensing, and support status.

Data Assets Sensitive data repositories, locations, classification levels, and regulatory requirements.

Cloud Resources Virtual machines, containers, storage, databases, and services across cloud environments.

Network Architecture Network diagrams, IP addressing schemes, VLAN assignments, and firewall rule collections.

Third-Party Connections VPN connections, API integrations, and data sharing relationships with external parties.

Critical Assets Systems and services essential to the organization’s objectives, In many organizations, these categories are maintained by different teams in different systems: network engineering maintains network diagrams and firewall rules, server and cloud teams maintain infrastructure inventories, and business units track their own data assets and third-party relationships. The incident response team should maintain local copies of this documentation for offline access during incidents, but should also establish relationships with the authoritative source owners to ensure access to current data.

Local copies provide availability when primary systems are compromised, while access to authoritative sources ensures the information used during scoping and containment reflects the current state of the environment.

Not all systems require the same level of attention during response. Using a classification system to identify assets by business criticality will help decision makers prioritize actions during incidents. The Critical Assets category in the inventory identifies which systems warrant priority attention during scoping, containment, and recovery. Document these classifications in advance so decision makers can make informed prioritization decisions without delay.

Consider maintaining asset inventory in a format that supports rapid querying during incidents.

Spreadsheets work for smaller environments, but larger organizations benefit from dedicated Configuration Management Database (CMDB) platforms or asset management tools that support search, filtering, and integration with other security tools. Whatever format the organization chooses, ensure the inventory remains accessible during incidents, including scenarios where primary systems may be compromised.

Asset inventory is only useful if it is accurate. Implement processes to maintain inventory currency, including automated discovery tools, change management integration, and periodic audits. Stale inventory data can mislead responders and delay effective response.

Monitor the Attack Surface

A comprehensive asset inventory captures what the organization knows about its environment, but attackers target what the organization exposes, which is not always the same thing. Attack Surface Monitoring (ASM) extends the asset inventory by continuously discovering and evaluating accessible assets: internet-facing services, cloud resources, domains, certificates, distributed computing endpoints, exposed APIs, and more. Where the asset inventory answers what do we have?  ASM answers what can an attacker see?

THE MODERN ATTACK SURFACE

The attack surface for most organizations extends well beyond servers and workstations connected to the corporate network. As Ron Eddings and MJ Kaufmann observe in Attack Surface Management : “When we start looking at attack surfaces, it’s no longer as simple as it was in the early days of IT and the internet. We still have all of the traditional components of IT that keep businesses running, including workstations, networks, and servers, but IT is so much more now. IT and how we do business has expanded to include a wider variety of technologies that are just as integral to business operations as the traditional components.

- Eddings & Kaufmann, Attack Surface Management Today’s attack surface includes cloud environments, SaaS applications, APIs, mobile devices, IoT systems, AI infrastructure, and third-party dependencies, each with its own security characteristics and visibility challenges. An organization’s internal asset inventory may account for traditional IT components while missing the cloud resources, SaaS integrations, and vendor connections that attackers increasingly target.

ASM tools help organizations discover and monitor this broader attack surface, providing a more complete picture of where attacks are likely to originate. For incident response teams, this visibility is particularly valuable. Assets that are unknown during preparation are assets that will be missed during scoping.

“After all, you can’t manage what you don’t know exists.

- Ron Eddings and MJ Kaufmann, Attack Surface Management ASM tools discover externally accessible assets, identifying resources that may not appear in internal inventories. These discoveries can include forgotten development servers, test environments with production data, acquired company infrastructure that was never integrated, and cloud resources provisioned outside standard change management processes.

Assets that do not appear in the internal inventory are unlikely to appear in the incident scope. ASM helps close this visibility gap by discovering what the organization exposes before an attacker does.

For incident response preparation, ASM provides two specific benefits. First, it reduces the likelihood of incidents by identifying exposures before attackers exploit them. A newly exposed administrative interface or an expiring certificate on a customer-facing service can be addressed proactively rather than discovered during an incident investigation. Second, it improves scoping accuracy during incidents by giving responders a current view of the organization’s accessible attack surface, which may differ from what should feed back into the asset inventory and hardening processes to close the loop between discovery and remediation.

Assess Security Posture Through Adversary Simulation

Assessing security posture requires more than identifying known vulnerabilities. Vulnerability scanning identifies missing patches and misconfigurations, but it does not determine whether detection and response capabilities work when an attacker moves through the environment after initial access. Post-exploitation gaps such as undetected lateral movement, missed credential harvesting, or silent persistence mechanisms do not appear in vulnerability scan results.

Adversary simulation closes this gap by testing the full defensive chain, from initial access through post-compromise activity as shown in Figure 44 . This approach validates whether the organization’s detection tools can identify attack techniques in practice, and whether response processes can effectively contain and remediate incidents.

Figure 44 | Adversary Simulation Risk Assessment Coverage

Adversary simulation can take several forms, each with different levels of complexity and resource requirements. For example, an organization might start by performing vulnerability scanning, augmented by configuration assessment against security benchmarks, to establish a baseline and identify known weaknesses across the environment. Penetration testing can be applied to validate whether those weaknesses are exploitable in practice, and application security testing can be used to analyze custom software through static analysis, dynamic testing, and code review.

Adversary simulation and purple teaming go further by testing detection coverage against known attack techniques. Frameworks like MITRE ATT&CK provide a structured catalog of adversary tactics and techniques that organizations can use to map which behaviors their detection tools can identify and where gaps exist. [20] Projects such as Atomic Red Team  provide repeatable, granular test cases for individual ATT&CK techniques, allowing teams to validate specific detection rules without requiring a full red team engagement. [21] Organizations do not need a mature red team program to begin adversary simulation. Running a small set of atomic tests against ATT&CK techniques relevant to the organization’s threat profile validates whether the investment in detection tools is producing results.

For organizations seeking continuous validation rather than periodic testing, Breach and Attack Simulation (BAS) platforms automate adversary simulation by running predefined attack scenarios against production or near-production environments on a scheduled basis. BAS tools execute attack chains that mimic real threat actor behavior, testing whether security controls detect and block each step. Results are mapped to specific detection gaps, giving security teams a prioritized remediation list tied to actual control failures rather than theoretical vulnerabilities.

BAS shifts the question from could this attack succeed?  to did our controls detect and block it? This distinction helps teams prioritize remediation based on demonstrated gaps rather than hypothetical risk.

BAS complements manual adversary simulation and penetration testing rather than replacing them. Manual exercises bring human creativity and adaptability that automated tools cannot replicate, while BAS provides the continuous coverage that ensures detection capabilities remain effective between manual assessments.

Organizations with active detection engineering programs can use BAS results to validate new detection rules and measure improvement over time.

Vulnerability findings from all assessment activities should feed back into patch management and hardening processes, with remediation progress tracked and persistent vulnerabilities escalated when they exceed acceptable risk thresholds.

CVSS FOR VULNERABILITY PRIORITIZATION

The Common Vulnerability Scoring System (CVSS) provides a standardized method for rating the severity of security vulnerabilities. Maintained by FIRST, CVSS assigns numerical scores from 0 to 10 based on characteristics that describe how a vulnerability can be exploited and its potential impact.

Organizations commonly use CVSS scores to prioritize remediation efforts, with higher scores indicating more severe vulnerabilities.

CVSS version 3.1 calculates base scores using eight metrics organized into exploitability and impact categories. Exploitability metrics describe how an attacker would exploit the vulnerability, while impact metrics describe the consequences of successful exploitation. Table 12  illustrates these metrics using CVE-2025-61882, an Oracle E-Business Suite vulnerability with a critical 9.8 base score.

Table 12 | CVSS 3.1 Base Metrics for CVE-2025-61882

The combination of network-accessible exploitation that requires no privileges or user interaction, coupled with high impact across all three security dimensions, yields the critical base score of 9.8.

While CVSS provides valuable standardization, organizations should avoid using it as the sole basis for prioritization. A critical-severity vulnerability in an internet-facing system demands immediate attention, but the same vulnerability in an isolated test environment may warrant lower priority.

CVSS scores do not account for organizational context, such as whether the vulnerable software is deployed, whether compensating controls exist, or whether the asset supports critical business functions.

Use CVSS as one input among several for prioritization decisions. Combine CVSS severity with asset criticality, exposure level, and threat intelligence about active exploitation to make informed decisions about where to focus limited remediation resources.

The Exploit Prediction and Scoring (EPSS)  metric, from the Forum of Incident Response and Security Teams (FIRST), provides a data-driven approach to prioritizing vulnerability remediation based on the likelihood of exploitation. Where CVSS focuses on how difficult a vulnerability would be  to exploit, the EPSS metric estimates the probability that a vulnerability will be exploited in the wild. EPSS offers another dimension to vulnerability prioritization for software management that complements CVSS scores.

Collect and Retain Logging Information

Comprehensive logging provides the data foundation for threat detection and incident investigation.

Without adequate logs, detection capabilities are limited, and post-incident analysis may be impossible.

Start by identifying log sources that should send data to the central collection. Priority sources include authentication systems, security tools, critical servers, network devices, and cloud platforms. Configure these systems to capture security-relevant events: enable process-creation logging with command-line arguments on Windows systems, capture authentication events, including successes and failures, and log network connections and DNS queries where feasible.

FEAR THE DARK: WHEN LOGS GO MISSING

Heather Barnhart, SANS Institute head of faculty, warns that incident responders face a growing threat that no detection tool can address: dark periods - gaps in time where no reliable digital evidence exists. [22] These investigative gaps emerge from multiple causes: misconfigured logging that fails to capture critical events, default logging settings that prove too limited for forensic needs, retention policies that delete evidence before investigations begin, infrastructure changes that create coverage gaps, and malicious actors who deliberately manipulate or destroy logs.

The consequences can be severe. In the 2022 Idaho murders investigation, critical cell tower data gaps created dark periods that complicated the timeline reconstruction for victims like Kaylee Goncalves. The 2025 Bybit cryptocurrency breach, attributed to APT38, resulted in $1.5 billion in losses partly because the attack behavior appeared normal to AI-based detection systems, and investigators faced significant evidence gaps.

Barnhart’s guidance is direct: "Log for normal so you can find evil."

Organizations should establish baselines for expected activity and ensure that logging captures sufficient context to distinguish legitimate operations from malicious ones. Without complete logs, even the most skilled incident response teams face preventable gaps that attackers will exploit.

“We need to be afraid of the dark... because the dark is the lack of data.

- Heather Barnhart, SANS Institute Head of Faculty Define retention periods based on investigation needs, compliance requirements, and storage constraints.

Most organizations retain security logs for between ninety days and one year. Longer retention may be necessary for compliance or to support the investigation of advanced persistent threats that may have persisted for extended periods before detection.

When planning retention, distinguish between logs retained for compliance and logs retained for active detection and investigation. Compliance retention satisfies regulatory and audit requirements but does not require the query performance or correlation capabilities of a SIEM. Organizations can reduce costs by storing compliance-only logs in a lower-cost archive or log management platform while reserving SIEM capacity for log sources that support active detection rules and investigation workflows.

Protect logs from tampering or deletion by attackers who gain system access. Forward logs to a central collection system promptly and implement appropriate access controls for log storage. Attackers routinely attempt to delete or modify logs to cover their tracks.

SIEM OR SINK?

Security Information and Event Management (SIEM) platforms aggregate logs across the environment, normalize data into consistent formats, and enable correlation analysis. SIEMs provide significant value for detection and investigation when properly implemented and maintained.

However, many organizations deploy SIEMs without investing in the ongoing effort required to make them effective. Logs flow into the platform but are never reviewed. Detection rules generate alerts that no one investigates. The SIEM becomes a very expensive log sink rather than a security tool.

Effective SIEM operation requires:

• Dedicated analysts to investigate alerts and hunt for threats.

• Continuous tuning to reduce false positives and improve detection accuracy.

• Regular review of coverage to ensure critical log sources are ingested.

• Periodic removal of log sources that have no associated detection or investigation use cases, freeing capacity and improving retention for sources that do.

• Development of custom detections for organization-specific threats.

• Integration with incident response processes for seamless escalation. provide more value than an underutilized SIEM.

PREPARATION CHALLENGES

Effective preparation requires sustained effort during periods in which incidents are not actively occurring.

This creates challenges that can undermine preparation activities even in organizations that recognize their importance. Table 13 summarizes several important challenges and mitigation strategies.

Table 13 | Preparation Challenges Summary

CHALLENGE IMPACT Resource Constraints Operational demands leave little time for preparation work Readiness Erosion Skills atrophy and complacency develops during quiet periods Documentation Drift Plans and playbooks become outdated as the environment changes Knowledge Loss Institutional knowledge leaves with departing team members Value Demonstration Preparation benefits are difficult to quantify Understanding these challenges helps incident response teams anticipate obstacles and implement countermeasures before preparation efforts stall. The following sections examine each challenge in detail and provide practical guidance for maintaining effective preparation programs.

Resource Constraints

Preparation activities compete with operational demands for limited resources. Security teams often find themselves responding to alerts, managing security tools, and supporting business initiatives with little time left for preparation. When a critical vulnerability requires immediate patching or a suspicious alert demands investigation, updating the incident response plan naturally falls to a lower priority.

Budget constraints present a separate but related challenge. Training courses, forensic tools, and incident response exercises all require funding that competes with other security investments. Organizations facing tight budgets may struggle to justify investment in preparation spending when the return on investment is difficult to quantify, particularly when more visible projects compete for the same resources.

Frame preparation investments as risk reduction rather than optional enhancement when seeking management support. For many decision makers, risk reduction is a more compelling justification than preparedness for hypothetical future events. Where possible, quantify potential incident costs using industry data and compare against the relatively modest investment in preparation activities.

Teams can address resource constraints through several approaches:

• Integrate preparation into operations : Document lessons learned immediately after incidents while context is fresh, update playbooks as part of tool deployment projects, and conduct brief tabletop discussions during regular team meetings.

• Prioritize high-impact activities: Focus on the most likely incident scenarios, the most critical systems, and the most significant capability gaps.

• Utilize existing meetings : Use standing team meetings for fifteen-minute tabletop discussions or playbook reviews rather than scheduling separate preparation sessions.

TURNING INCIDENTS INTO PREPARATION FUNDING

Few things are more frustrating for an incident response team than flagging a missing capability or underfunded tool, watching the request sit in a backlog, and then seeing that exact gap delay an active response. When it happens, document the delay and its impact on the incident timeline.

Then use the incident to get the fix approved. Brief leadership that the team intends to address the gap during or immediately after the response, and seek their approval while the cost of the gap is still visible. Decision makers who have just watched a missing tool or process slow down a response are far more receptive to funding the fix than they would be during routine budget discussions. Incident budgets often absorb remediation costs that would otherwise face months of procurement review, and the urgency of an active incident often cuts through the inertia that blocked the original request.

Even modest preparation investments compound over time. An organization that dedicates just two hours per week to preparation activities accumulates over 100 hours of preparation work annually, building capabilities that prove invaluable when incidents occur.

Maintaining Readiness During Quiet Periods

Extended periods without significant incidents create a paradox: the absence of incidents may indicate that cybersecurity controls and preparation efforts are working, but it also reduces the urgency that drives continued investment. Team members can become complacent when they have not encountered an incident that required response efforts in months or years. Even the best analysts will experience skills atrophy without regular practice, especially when organizational attention shifts to more visible priorities.

To address this challenge, organizations should practice incident response efforts with regular exercises:

• Monthly tabletop discussions : Brief scenario walkthroughs that test decision-making and communication.

• Quarterly technical drills: Hands-on exercises using forensic tools and evidence collection procedures.

• Annual full-scale exercises: Comprehensive simulations involving all stakeholders.

Rotate team members through different roles during exercises to build depth and prevent single points of failure. The analyst who always handles evidence collection during drills should occasionally practice coordination or communication roles. Team leads should periodically work through technical procedures to maintain hands-on familiarity.

INCIDENT RESPONSE INVESTIGATION CHALLENGES

One opportunity for organizations to keep their incident response skills sharp is to allocate time for continued professional development. Traditionally, professional development is viewed as training courses or on-the-job work, but another valuable approach is to practice investigative skills in Capture the Flag (CTF) competitions. These competitions simulate real-world incident scenarios, Many people are drawn to CTFs for the competitive aspect, but this can also be a drawback for those with imposter syndrome. Consider allocating time for team members to participate in CTFs as a group activity, focusing on learning and collaboration rather than competition. This approach fosters teamwork, encourages knowledge sharing, and builds confidence in investigative skills that directly translate to incident response.

One excellent resource for CTFs is the SANS Skills Quest (SSQ) program , a low-cost self-paced training option that presents realistic scenarios designed to enhance practical skills. As a contributor to the team that developed SSQ, I have first-hand experience with its effectiveness in helping teams develop and measure important cybersecurity and incident response skills.

Another option is to use the free resources available through the Splunk Boss of the SOC  platform, which offers analysts an opportunity to complete a variety of incident response and forensics investigation challenges. While primarily focused on Splunk users, the scenarios provide valuable practice for general investigative skills, and the supplied evidence for analysis can often be examined with other forensic tools as well.

Figure 45 | Splunk Boss of the SOC Platform

Keeping Plans and Playbooks Current

Organizational changes, technology updates, and evolving threats can make preparation documents obsolete. An incident response plan finalized six months ago may reference systems that have been decommissioned, contacts who have changed roles, and procedures that no longer match current tool capabilities. Outdated documentation can lead to false confidence, where responders believe they have guidance that is no longer accurate.

Playbooks face similar drift. A ransomware playbook written before the organization adopted cloud infrastructure may miss critical containment steps. Procedures that assume external consulting support contracts become problematic when budget cuts or contract renegotiation reduce resource availability.

To mitigate the challenge of outdated documents, organizations should establish regular review cycles with assigned ownership for each preparation document:

• Contact lists: Quarterly reviews with verification of current information.

• Playbooks: Exercise each playbook at least once per year and conduct a separate review on an offset schedule. Scheduling exercises and reviews six months apart keeps playbooks validated and current throughout the year. Update playbooks after each exercise or incident in which they were used.

• Policy documents: Annual reviews aligned with broader governance cycles.

Consider developing an annual exercise plan that maps each playbook to a scheduled exercise date. This plan ensures all playbooks are validated throughout the year and provides auditors with evidence of a structured review program.

Assign specific individuals responsible for keeping documents current and include document review in their performance expectations. Organizations that treat documentation maintenance as an ongoing discipline rather than a periodic project maintain more accurate and useful preparation materials. The investment in keeping documents current pays dividends during incidents when responders can trust their guidance.

Organizational Change and Turnover

Personnel changes can erode the effectiveness of preparation when institutional knowledge leaves with departing team members. The senior analyst who has responded to dozens of incidents carries irreplaceable context about how systems actually behave, which stakeholders need careful handling, and which documented procedures work better in theory than in practice. When that analyst departs, their replacement inherits documentation but not the nuanced understanding that makes the response effective.

Turnover affects preparation beyond direct knowledge loss.  Relationships with stakeholders need to be rebuilt as legal counsel, HR partners, and business unit leaders learn to trust new team members. Response dynamics shift when team composition changes, requiring adjustment to communication patterns and role assignments.

TABLETOP INJECT: SARAH’S DEPARTURE

I was working with a large media company on a series of tabletop exercises. The team was doing well, demonstrating strong decision-making and communication skills. However, I noticed significant reliance on the incident response team leader, Sarah, who had deep institutional knowledge.

Sarah had been with the company for over a decade and had led it through several high-profile, public incidents. She knew the key stakeholders, the quirks of their systems, and the unwritten rules governing organizational incident response. She had institutional knowledge and relationships that the incident response team leaned on heavily.

After an hour into the two-hour exercise, I dropped an inject on the team: “Sarah has been sequestered for jury duty and won’t be available for the rest of the exercise.

To the team’s credit, they responded professionally. Sarah sat back and observed as the rest of the team adjusted to her absence, arms crossed. While secondary team members stepped up admirably, the exercise quickly fell apart without Sarah’s guidance. Decisions slowed, communication faltered, and the team struggled to maintain cohesion, eventually falling into arguments and failing to complete the exercise objectives.

The company’s Chief Information Security Officer (CISO) later thanked me for the input, recognizing the risk of over-reliance on a single individual. When I spoke with Sarah afterward, she admitted the experience was eye-opening. She had always known she carried significant institutional knowledge, but watching her team struggle made the risk tangible in a way that abstract discussions about succession planning never had. Sarah became a champion for cross-training initiatives, actively mentoring teammates in leadership skills, and documenting the unwritten knowledge she had accumulated.

Cross-training provides the foundation for turnover resilience:

• Rotate responsibilities: Ensure multiple team members can perform each critical function.

• Document reasoning: Explain why certain approaches work, not only which steps to follow.

• Pair experienced and new responders: During exercises and actual incidents when possible.

Knowledge transfer processes should begin before departures occur. Exit interviews that capture undocumented knowledge and transition periods that allow for job shadowing help preserve important institutional knowledge.

Consider creating knowledge repositories that capture lessons learned, incident post-mortems, and informal guidance that might otherwise exist only in experienced responders' memories. These repositories become particularly valuable when team composition changes or when responding to incident types not encountered recently.

Demonstrating Value Without Incidents

Preparation investments face a fundamental measurement problem: success means incidents that do not happen or impacts that do not materialize.

Cybersecurity leaders can struggle to justify preparation budgets when the primary benefit is avoiding hypothetical future losses. Executives reasonably ask what the organization received for its investment, and "we didn’t have a major incident" is an unsatisfactory measure of returns.

This challenge intensifies during budget discussions when preparation competes with projects that offer more tangible returns. A new customer-facing feature delivers measurable revenue growth, while an updated incident response plan delivers promised risk reduction that is difficult to quantify.

To better demonstrate the value of incident response preparation activities, organizations can track metrics that demonstrate preparation value independent of actual incidents:

• Exercise performance: Response times during drills and improvement trends across exercises

• Capability gaps addressed: Issues identified during exercises and subsequently remediated

• Detection improvements : New detection rules deployed, false positive rates reduced, MTTD in simulated scenarios

• Documentation currency: Percentage of documents reviewed on schedule Tracking these metrics over time provides tangible evidence of progress in preparation that supports budget discussions and resource allocation decisions.

BENCHMARKING PREPARATION INVESTMENTS

External reference points help justify investment levels in preparation. Industry surveys provide concrete data for comparison: the SANS Institute 2025 SOC Survey found that 62% of SOC professionals believe their organization is not doing enough to retain top staff, highlighting the importance of training and development investments. [23] The Ponemon Institute’s 2025 Cybersecurity Threat and Risk Management Report found that 71% of organizations are increasing cybersecurity budgets, with 51% now applying incident response plans consistently across the enterprise. [24]

Figure 46 | SANS 2025 SOC Survey Key Findings

Building the Bridge Before the Flood

Dana joined Meridian Financial as the incident response team lead eight months ago. Her predecessor had focused on technical capabilities: an impressive forensic lab and advanced detection tools. But Dana noticed something troubling during her first month: when she needed to coordinate with other departments, she was introducing herself to people who should have been close partners.

Dana started building relationships systematically. She scheduled monthly meetings with Ron in IT operations, Rachel in Legal, and Vincent in Human Resources. Each conversation revealed coordination gaps. Ron mentioned that his team recently migrated applications to cloud infrastructure without notifying security. Rachel had handled a vendor breach notification as a contract matter, without involving incident response. Vincent initially questioned why HR would need to coordinate with security until Dana explained that premature technical actions during insider investigations can expose the organization to wrongful termination claims.

Figure 47 | Meridian Financial Incident Response Team Coordination

Dana included these contacts in quarterly tabletop exercises focused on cross-functional coordination.

During one ransomware simulation, Ron discovered that his vendor contact list was outdated; Rachel learned that the cyber insurance policy requires 24-hour breach notification; and Vincent realized that his termination procedures conflicted with evidence preservation requirements. Each exercise revealed gaps that could be addressed before they negatively impacted the organization.

Seven months after Dana joined, the preparation proved its value. A security analyst detected unusual data access patterns from Thomas, a senior accountant with twelve years at the company. The pattern suggested data staging for exfiltration of customer financial records.

Dana called Vincent within minutes. Because of their established relationship, she didn’t need to explain who she was or why HR should care.

"We need to be careful here," Vincent said. "Thomas is well-respected. If we’re wrong, this could hurt his reputation. But if we’re right, we need to act before more data leaves."

Vincent disclosed to Dana that Thomas recently submitted a resignation notice effective in two weeks, information that substantially changed the risk calculation. Dana’s next call was to Rachel, who immediately recognized the regulatory implications and advised on evidence preservation for potential law enforcement referral.

Figure 48 | Meridian Financial Coordinated Response Timeline

Within two hours, Dana had a coordinated response plan in place. Ron’s team quietly disabled Thomas’s remote access, citing a "routine security update." Legal had drafted a data hold notice. HR had administrative leave documentation ready for immediate execution if the investigation confirmed malicious activity.

Dana’s investment in relationships transformed a potential crisis into coordinated action. The relationships she built weren’t just professional courtesy. Those relationships formed the foundation of an effective response, as essential as forensic tools or detection systems.

Intelligence-Driven Detection

Isaac Morgan had three weeks to finish integrating threat intelligence feeds into Warren Health’s NDR platform. The healthcare organization subscribed to an ISAC feed specific to the healthcare sector, and Isaac configured the NDR to correlate network traffic with known indicators of compromise. His manager questioned the time investment, but Isaac knew that detection without context was just noise.

The integration was straightforward but required careful tuning. Isaac mapped the STIX data indicators to the NDR’s detection engine, focusing on infrastructure associated with threat actors known to target healthcare organizations. He configured alerting thresholds to balance sensitivity against false positives, testing with historical traffic samples before enabling production alerts.

Listing 28 | ISAC STIX Indicator for Velvet Tempest C2 Infrastructure

{

"type": "indicator",

"spec_version": "2.1",

"id": "indicator--8f43b2e1-6d9a-4c5b-b8e7-3f2a1d9c4e6b",

"created": "2026-01-13T08:15:00.000Z",

"modified": "2026-01-13T08:15:00.000Z",

"name": "Velvet Tempest C2 Infrastructure",

"description": "IP address hosting C2 for ransomware targeting healthcare",

"indicator_types": ["malicious-activity"],

"pattern": "[ipv4-addr:value = '165.227.88.15']",

"pattern_type": "stix",

"valid_from": "2026-01-13T08:15:00.000Z"

}

NDR flagged outbound connections from a workstation in the billing department to an IP address associated with Velvet Tempest, a threat actor group known for targeting healthcare organizations with ransomware.

The ISAC had published the indicator just thirty-six hours earlier based on activity observed at another healthcare provider.

Isaac pulled the alert details using AC-Hunter, their network threat detection platform.  The connections were periodic, occurring every four hours, consistent with C2 beaconing behavior.  Without the CTI integration, this traffic would have appeared as routine HTTPS connections to an uncategorized external host. With the threat intelligence context, Isaac immediately recognized the severity.

Figure 49 | Velvet Tempest C2 Detection Alert

Within an hour, the incident response team had isolated the affected workstation and begun forensic analysis. The investigation revealed that a billing specialist had opened a malicious attachment from a phishing email two days earlier. The malware had established persistence but had not yet moved laterally or accessed patient data.

Early detection through CTI integration transformed what could have been a ransomware incident into a contained compromise. Isaac’s investment in preparation paid dividends in avoided downtime, preserved patient data, and incident costs that never materialized.

PREPARE: STEP-BY-STEP

The following steps provide a condensed reference for preparation activities. Each step corresponds to topics covered earlier in this chapter, organized for use when building organizational readiness, training the incident response team, and strengthening proactive defenses.

This step-by-step guide is available for download in PDF and Markdown formats on the companion website at dynamicincidentresponse.com.

Step 1. Prepare the Organization

1. Develop organizational policies that outline the organization’s approach to incident response, including:

◦ Company mission and goals for the incident response program.

◦ Priorities for the organization before, during, and following an incident.

◦ Policy on involving management teams in the organization, including GRC, legal, and public relations.

◦ Policy on paying ransom or extortion.

◦ Policy on communicating with attackers.

◦ Policy on data retention and evidence preservation.

◦ Policy on reporting incidents to law enforcement, government, or industry partners.

◦ Policy on public disclosure of incidents.

◦ Policy on engaging with third-party incident response providers.

◦ Containment authorization policies defining who can authorize systems to be taken offline, including tiered authorization levels (SOC/IRT-authorized actions like endpoint isolation, service owner-authorized actions like server or service isolation, executive-authorized actions like shutting down production systems or actions affecting regulated services).

◦ Recovery time objectives (RTO) and recovery point objectives (RPO) for critical systems.

◦ Evidence retention requirements and chain of custody procedures.

2. Develop management support for incident handling capability, including:

◦ Establish relationships with decision-makers before incidents occur.

◦ Communicate the value of incident response using industry examples and metrics.

◦ Seek management input on policy development.

◦ Define communication expectations during incidents.

◦ Assign management actionable responsibilities, such as participating in tabletop exercises or breach simulations.

3. Identify critical assets and risk assessment processes, including:

◦ Identify systems and services essential to the organization’s survival, including revenue-generating operations, customer-facing services, and regulatory compliance systems.

◦ Define risk tolerance thresholds for low, medium, high, and critical events.

◦ Develop incident classification criteria based on impact factors (systems affected, data sensitivity, business impact, regulatory implications).

◦ Document classification matrix for rapid reference during incidents.

◦ Review and update criteria annually as the risk landscape evolves.

4. Develop an incident communications plan that addresses channels, contacts, reporting, and emergency messaging, including:

◦ Establish communication channels that are secure and reliable: ▪ Select a primary communication platform with appropriate security controls.

▪ Identify a backup communication channel for use if the primary channel is compromised.

▪ Test the communication channels periodically.

▪ Document platform access procedures.

◦ Document contact information for the team and important stakeholders: ▪ Internal contacts (IRT members, IT operations, legal, HR, executives).

▪ External contacts (law enforcement, regulators, insurance, retainer providers).

▪ Vendor and cloud provider security contacts.

▪ Establish a quarterly review process to maintain accuracy.

◦ Establish reporting procedures: ▪ Define reporting requirements by incident severity.

▪ Create report templates for different audiences.

▪ Establish service level agreements for initial and ongoing reports.

▪ Document distribution lists for each report type.

◦ Develop an emergency communication plan: ▪ Define notification triggers for different incident types.

▪ Establish approval workflows for internal and external communications.

▪ Create message templates for common scenarios.

▪ Identify constituent audiences (customers, partners, regulators, employees).

▪ Establish distribution channels for each audience.

▪ Designate and train spokespersons.

▪ Document applicable regulatory notification requirements (including GDPR, HIPAA, SEC, PCI DSS, NIS2, DORA, and applicable breach notification laws).

◦ Establish external reporting channels for security researchers: ▪ Publish a security.txt file (RFC 9116) with contact, encryption, and disclosure policy information.

▪ Document internal routing so external security disclosures reach the security team promptly.

5. Establish the incident response team, including:

◦ Define team structure and roles (lead, analysts, communications, liaison).

◦ Identify primary and backup personnel for each role.

◦ Document escalation paths and decision authority.

◦ Establish team activation procedures.

6. Identify a platform for incident tracking, including:

◦ Select a platform appropriate to organization size and needs.

◦ Configure incident categorization and prioritization.

◦ Establish access controls and retention policies.

◦ Train team members on use of the platform.

7. Account for cyber insurance requirements, including:

◦ Obtain and review the cyber insurance policy with the IR team.

◦ Identify notification timelines, pre-approval requirements, and vendor restrictions.

◦ Negotiate to add preferred IR firms to the carrier’s approved vendor panel.

◦ Include the policy owner on the IRT contact list and in tabletop exercises.

◦ Maintain offline access to the policy, carrier contacts, claims phone number, policy number, and procedures for engaging the carrier’s approved incident response providers.

◦ Protect the policy from disclosure on attacker-accessible systems and during ransom negotiations.

◦ Identify independent legal counsel separate from the carrier’s breach coach.

8. Implement security awareness training, including:

◦ Develop training content covering incident recognition and reporting.

◦ Establish training frequency and completion tracking.

◦ Implement practical exercises (simulated phishing).

◦ Create clear reporting channels for suspicious activity.

Step 2. Prepare the Incident Response Team

1. Train the incident response team, including:

◦ Technical skills (SOAR, digital forensics, network analysis, malware analysis, log analysis, scripting, and automation).

◦ Soft skills (communication, documentation, decision-making under pressure, leadership, and negotiation).

◦ Incident response procedures and playbook execution.

◦ Company policies and escalation procedures.

◦ Schedule ongoing training to maintain and develop skills.

2. Develop and validate system backup and recovery procedures, including:

◦ Document current backup architecture and coverage.

◦ Verify backup protection against ransomware (immutable, air-gapped, separate authentication).

◦ Implement backup integrity monitoring and failure notifications.

◦ Test restoration procedures and measure against RTO/RPO targets.

◦ Document backup access procedures for incident response.

3. Cultivate relationships with essential personnel, including:

◦ Identify contacts in IT operations, SOC, help desk, legal, HR, public relations, and business units.

◦ Consider developing a RACI matrix to clarify roles during incident response.

◦ Include essential contacts in exercises and preparation activities.

◦ Establish communication preferences and escalation procedures.

◦ Build relationships through regular interaction.

4. Develop playbooks for common incidents, including:

◦ Identify incident types most likely to affect the organization.

◦ Create detailed, actionable procedures for each type.

◦ Include decision points, tool references, and communication triggers.

◦ Review and update playbooks after each exercise or incident in which they were used.

5. Prepare resources for response actions, including:

◦ Configure forensic workstations with the necessary tools, including cloud-based workstations for organizations with significant cloud infrastructure.

◦ Acquire and test evidence collection tools.

◦ Establish secure evidence storage with appropriate capacity.

◦ Prepare a jump bag for on-site response.

6. Prepare access to systems, including:

◦ Establish break-glass accounts secured with hardware tokens or a credential vault, with alerting on use and periodic testing.

◦ Document access request procedures for incident response.

◦ Pre-authorize access where possible to reduce response delays.

◦ Document vendor and cloud provider support procedures.

7. Conduct tabletop exercises and incident response drills, including:

◦ Schedule regular exercises (monthly tabletop discussions, quarterly technical drills, annual full-scale
