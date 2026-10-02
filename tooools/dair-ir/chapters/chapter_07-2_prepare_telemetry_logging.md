# Chapter 07-2: Preparation: Telemetry Logging, Audit Baselines & Monitoring Deployment

> Modular Sub-Chapter | Source: DAIR-IR Framework

---

• Reporting procedures : Every employee should know how to report suspected security incidents, including who to contact and what information to provide. Clear, accessible reporting channels encourage prompt notification.

• Social engineering resistance: Training should cover common social engineering techniques, including phishing, pretexting, and baiting. Employees who understand these tactics are less likely to fall victim to them.

• Data handling : Employees should understand data classification requirements and proper handling procedures for sensitive information. This knowledge reduces the likelihood of accidental data exposure.

Training effectiveness improves when programs include practical exercises rather than relying solely on passive content consumption. Simulated phishing campaigns, for example, provide measurable feedback on employee awareness while identifying individuals who may benefit from additional training.

Coordinate security awareness training with the incident response team. When employees report suspected incidents, even if they turn out to be false alarms, recognize and thank them for their vigilance. This positive reinforcement encourages continued reporting and demonstrates that reports are valued.

Prepare the Incident Response Team

Preparing the incident response team involves developing the skills, tools, relationships, and processes that enable effective response when incidents occur. This preparation ensures that team members can act decisively under pressure, collaborate effectively with other departments, and execute response activities with confidence. Where the previous section focused on organizational structure and policy, the activities here bridge people, process, and technology: training the team, building playbooks, and assembling the tools and access needed for response operations.

Train the Incident Response Team

Technical competence forms the foundation of effective incident response. Team members should possess the skills necessary to detect threats, collect evidence, analyze attacker activity, and execute containment and eradication actions. Training programs should address both foundational skills and advanced techniques appropriate to each team member’s role.

Core technical training areas for incident responders include:

• Security Orchestration, Automation, and Response (SOAR) : Familiarity with SOAR platforms to automate repetitive tasks, orchestrate workflows, and manage incident response processes.

• Digital forensics : Evidence collection, preservation, and analysis across Windows, Linux, and cloud environments. Understanding file systems, registry analysis, memory forensics, and timeline construction.

• Network analysis: Packet capture analysis, network flow interpretation, and identification of command-and-control communications.  Familiarity with tools like Wireshark, Zeek, and network detection platforms.

• Malware analysis : Basic static and dynamic analysis techniques for understanding malicious code behavior. Safe handling procedures for malware samples.

• Log analysis: Proficiency with SIEM platforms, log parsing, and correlation techniques. Understanding of common log formats and their investigative value.

• Scripting and automation : Ability to automate repetitive analysis tasks and develop custom tools for specific investigation needs. Python, PowerShell, and UNIX shell scripting are particularly valuable.

• Leadership and negotiation : Ability to lead cross-functional response efforts and communicate effectively with executives and stakeholders who may not share the responder’s technical background.

Together, these training areas equip responders with the breadth of skills needed to investigate incidents across diverse environments.

Beyond technical skills, incident responders benefit from training in communication, documentation, and decision-making under pressure. These soft skills often differentiate effective responders from those who struggle during high-stress incidents.

Training should be ongoing rather than a one-time event. The threats that organizations face are constantly evolving, and responders should regularly update their skills to address new attack techniques and tools. Budget for annual training and conference attendance to maintain team capabilities.

Develop and Validate System Backup and Recovery Procedures

Backup and recovery capabilities directly impact the organization’s ability to recover from incidents, particularly ransomware attacks that encrypt or destroy data, as well as other non-malicious incidents, such as hardware failures or accidental deletions. Preparation should ensure that backups exist, are protected from compromise, and can be restored within acceptable timeframes.

Start by documenting the current backup architecture and organizational requirements. Identify what systems and data are backed up, along with the frequency and retention periods for each. Document backup storage locations, whether on-premises, cloud-based, and/or at off-site facilities. Identify the access controls and authentication requirements that protect backup systems. Establish recovery time objectives (RTO) and recovery point objectives (RPO, the maximum acceptable data loss between backups) for critical systems to define acceptable restoration timeframes.

Evaluate backup resilience against common attack scenarios. Modern ransomware operators specifically target backup infrastructure to maximize coercion over victims. Assess whether backups would remain intact if an attacker gained privileged access to backup systems. Implement protections such as:

• Immutable backups : Configure backup storage to prevent modification or deletion for a defined retention period, even by administrators (this is a common feature of cloud-based storage platforms).

• Air-gapped copies : Maintain offline backup copies that cannot be reached through network connectivity.

• Separate authentication : Use credentials for backup systems that are distinct from the production identity environment.

• Backup integrity monitoring : Implement monitoring to detect unauthorized access or modification attempts against backup infrastructure.

• Notifications for backup failures: Ensure that backup failures trigger alerts to responsible personnel for timely resolution.

Combining these protections creates a layered defense for backup infrastructure that can withstand targeted attacks against recovery capabilities.

Many ransomware incidents involve attackers disabling backup systems and waiting for old backups to age out before demanding ransom. Several high-profile ransomware campaigns have disabled backup systems without the victim organization’s knowledge.

Notifications for backup failures should be sent to multiple recipients and escalated if not addressed promptly.

Regular restoration testing validates that backup investments deliver actual recovery capability. Schedule periodic restoration tests that measure actual recovery times against RTO targets and verify data completeness against RPO expectations. Document test results and address any gaps identified.

THE 3-2-1-1 BACKUP RULE

The traditional 3-2-1 backup rule recommends maintaining three copies of data on two different media types, with one copy stored off-site. For ransomware resilience, extend this rule to 3-2-1-1: add an additional immutable or air-gapped copy that cannot be deleted or manipulated via network connectivity or compromised credentials.

Figure 35 | Backup System with Immutable Copy

This additional copy serves as the last line of defense when attackers compromise both backup infrastructure and production systems. Organizations that lack immutable backups often find themselves choosing between paying ransom and accepting total data loss.

Cultivate Relationships with Essential Personnel

Incident response rarely occurs in isolation. Effective response requires collaboration across departments, each contributing specialized expertise to the overall effort. Establishing relationships with essential personnel before incidents occur enables smoother coordination during response.

Identify important contacts in departments that commonly participate in incident response:

• Business unit leaders : Managers who can assess business impact and authorize operational decisions affecting their areas.

• Essential stakeholders: System owners and application managers responsible for affected systems.

• Security Operations Center (SOC) : Analysts who monitor for threats and may provide initial detection

• IT Operations : System administrators, network engineers, and database administrators who maintain the systems that may be compromised or needed for investigation.

• Help desk : Front-line support staff who often receive initial reports of suspicious activity from end users.

• Legal counsel : Attorneys who advise on evidence handling, regulatory obligations, and litigation considerations.

• Human resources : HR personnel who provide insight and direction when incidents involve insider threats or employee-related investigations.

• Public relations : Communications professionals who manage external messaging during significant incidents.

Build relationships through regular interaction. rather than waiting for incidents to force collaboration.

Include key contacts in tabletop exercises, share relevant threat intelligence that affects their areas, and seek their input during preparation. When incidents occur, these established relationships facilitate faster coordination and reduce friction during high-stress situations.

CLARIFYING ROLES WITH A RACI MATRIX

A RACI matrix clarifies who is responsible for what during an incident response, reducing confusion when multiple teams collaborate under pressure. RACI defines four levels of involvement for each activity:

• Responsible: The person or team who performs the work.

• Accountable: The individual who has final authority and answers for the outcome (only one person per activity).

• Consulted: Those whose input is sought before decisions are made (two-way communication).

• Informed: Those who are kept updated on progress or decisions (one-way communication).

Table 7 | Sample RACI Matrix for Incident Response Activities

ACTIVITY IR LEAD SOC IT OPS LEGAL HR COMMS Initial detection and triage A R C I I I Containment decisions R/A C R C I I Evidence preservation R/A R C C I I System recovery A I R I I I External communications C I I C I R/A Employee-related actions C I I C R/A C The table above is a simplified example. Organizations should expand their RACI matrix to include additional groups relevant to their environment, such as executive leadership, regulators, affected business units, cyber insurance contacts, and third-party incident response providers.

Organizations that develop a RACI matrix during preparation and validate it through tabletop exercises benefit from clearer role definitions during actual incidents. When an incident occurs, participants already understand their responsibilities and can focus on execution rather than negotiating roles.

Review and update the matrix annually or when organizational changes affect incident response responsibilities.

Document Incident Response Decision Authority

A RACI matrix clarifies who participates in each activity, but it does not specify who can authorize the most consequential decisions during a response. An incident response authority matrix fills this gap by naming the role with authority to make each major decision, identifying a delegate when the primary authority is unavailable, and specifying the documentation each decision should produce.

RACI and the authority matrix complement each other. RACI covers staffing and coordination across activities. The authority matrix covers decision rights and the evidence each decision leaves behind.

Authority matrices are valuable during high-pressure incidents, when decisions about containment, scope expansion, or external notification need to happen quickly without ambiguity about who can sign off. They also serve as compliance evidence for the CSF 2.0 Govern function, where assessors expect to see named decision authorities rather than generic role descriptions.

A sample matrix covering eight common incident response decisions appears in Table 8.

Table 8 | Sample Incident Response Authority Matrix

DECISION AUTHORITY DELEGATE DOCUMENTATION REQUIRED Incident declaration Incident Commander Senior analyst on duty Incident ticket with declaration timestamp and rationale Containment action with material business impact Incident Commander with business unit head concurrence CISO if Incident Commander is unavailable Containment decision record with business impact assessment Scope expansion to additional business units Incident Commander with notification to CISO None Scope expansion log entry with trigger rationale Response Actions Loop exit, technical closure Incident Commander based on eradication validation Senior analyst with Incident Commander’s written DECISION AUTHORITY DELEGATE DOCUMENTATION REQUIRED Post-incident improvement, ownership Incident Commander from declaration through debrief closure, then Security Program Manager None Improvement register with named owners and milestone dates Media or public communications Communications lead with Legal sign-off CEO for material incidents Approved statement with version control and distribution record This sample uses common role names, which organizations should adapt to match their actual structure.

The value of the matrix lies in two places: removing ambiguity about who can authorize each decision, and specifying what documentation each decision generates so the record exists for both audit review and post-incident debrief.

Review and update the matrix when organizational changes affect decision authority, and validate it through tabletop exercises so the documented chain of authority matches what happens in practice.

Develop Playbooks for Common Incidents

Playbooks are an essential tool for incident response teams. When responding to an incident, stress levels are often high, the incident details can be chaotic and initially misunderstood, and analysts often have multiple tasks to complete in a short period of time. Playbooks provide a structured approach to incident response, outlining the steps to take for a specific incident type.

Effective playbooks share several characteristics:

• Actionable steps: Each step should be specific enough that a trained responder can execute it without additional research.

• Decision points: Include decision trees that guide responders through common scenarios.

• Tool references : Specify which tools to use for each step, including command-line syntax where applicable.

• Communication triggers : Identify when to notify stakeholders, escalate to management, or involve external parties.

• Documentation requirements: Specify what evidence to collect and how to document actions taken.

Playbook development is an ongoing, iterative process. Playbooks are not intended to be static documents.

They should evolve based on lessons learned from actual incidents and changes in the threat landscape.

Develop playbooks for incident types most likely to affect the organization, starting from an IOC to give responders a clear starting point for investigation. Some publicly available playbooks include:

• CERT Societe Generale Incident Response Methodologies : A collection of incident response methodologies, including playbooks for various incident types in English, Spanish, French, and Russian.

• Sudhakara Raju’s Playbooks : A collection of playbooks for data loss, malware, phishing, compromised accounts, and more.

• CISA’s Cybersecurity Incident and Vulnerability Response Playbooks : A set of US Federal Government playbooks for several incident types.

• Mike Lamb’s Playbooks: A collection of playbooks for Amazon Elastic Kubernetes Service , Amazon Elastic Container Service, Citrix, and VMware ESXi.

• Jai Minton’s DFIR Cheat Sheet : A collection of scripts and manual investigation steps for investigating the compromise of Microsoft Windows systems.

See Section 16.4.1 for information on using AI to help generate playbooks for specific IOCs.

Figure 36 | Sample Incident Response Playbook

platforms that match the environment’s operating system (macOS, other UNIX platforms, cloud instances, etc.). For organizations with significant cloud infrastructure, consider deploying cloud-based forensic workstations that place analysis capability close to the data, reducing the time required to transfer large evidence sets for analysis.

Evidence Collection Tools

Software for acquiring forensic images and volatile data from compromised systems.  This includes memory acquisition tools like WinPMEM and LiME, disk imaging tools, and endpoint collection agents. Ensure tools are tested and readily accessible when needed.

Analysis Tools

Software for examining collected evidence, including:

• Timeline analysis tools (Plaso, log2timeline).

• Memory analysis frameworks (Volatility, MemProcFS).

• Disk and artifact forensics tools (Autopsy, X-Ways, FTK, Magnet AXIOM).

• Log analysis and SIEM platforms.

• Network traffic analysis tools (Wireshark, Zeek).

• Endpoint detection and response (EDR), extended detection and response (XDR), and endpoint protection platform (EPP) consoles for host-level telemetry and response actions.

• Cloud Security Posture Management (CSPM) platforms for visibility into cloud configuration changes and policy violations.

Beyond dedicated forensic tools, organizations should also identify existing security and operational tools that provide investigative value. Data Loss Prevention (DLP) platforms, for example, often contain detailed Start by developing a realistic scenario based on threats relevant to the organization. Include participants from all departments involved in incident response, and assign a facilitator to guide the discussion and inject scenario developments as the exercise progresses. Designate a note-taker to capture observations and improvement opportunities throughout. Schedule sufficient time for meaningful discussion, typically two to four hours, and conduct a debrief immediately following to capture lessons learned while they are fresh.

When choosing a scenario for a tabletop exercise, consider selecting from publicly reported incidents that affected similar organizations for added realism. Alternatively, use an AI platform to review recent news articles in the organization’s industry and generate exercise scenarios based on real-world incidents.

Use tabletop exercises to test authorization levels, not technical procedures alone. Include scenario injects that force participants to make containment decisions: "The compromised server hosts the customer portal. Do you isolate it now, or wait for management approval?"

These moments reveal whether authorization policies are clear enough for real-world use and whether responders feel confident acting within their approved action authority.

Technical drills take preparation further by having responders practice hands-on skills using simulated or isolated environments. These exercises test whether team members can actually execute the procedures documented in playbooks. Evidence collection exercises using test systems, malware analysis challenges with controlled samples, log analysis scenarios with planted indicators, and containment procedure walkthroughs in lab environments all build practical competence that transfers to real incidents.

Full-scale exercises combine tabletop discussions with technical execution to provide the most realistic test of incident response capabilities. These exercises require significant planning and resources, so most organizations conduct them annually for critical scenarios. The investment pays off when responders face real incidents, having already navigated similar situations in practice.

See Section 16.4.3 for guidance on using AI to help generate tabletop exercise scenarios based on specific IOCs or attack techniques.

TABLETOP EXERCISE GAME PLAY: BACKDOORS & BREACHES

The card game Backdoors & Breaches , published by Black Hills Information Security, provides a fun and engaging way to practice incident response skills. The game uses activity-based cards to explore attack paths and practice decision-making in incident response scenarios.

Using a twenty-sided die to introduce randomness, players draw cards representing initial compromise, pivoting, privilege escalation, persistence, command and control, and data exfiltration.

Using collaborative play, participants win or lose together based on their collective decisions to respond to an incident.

Figure 37 | Backdoors & Breaches: Compromised Web Server Card

The game is suitable for a wide range of skill levels, offering opportunities for both beginners and experienced responders to learn different techniques and to practice response strategies. Players can purchase cards in English and Spanish, including a core set and expansion packs that introduce additional gameplay options. Alternatively, the cards are available as a free download for printing or digital use.

NCSC EXERCISE TOOLKIT

Another valuable resource for tabletop exercises is the NCSC Exercise Toolkit , provided by the UK National Cyber Security Centre (NCSC). Offering pre-planned micro exercises and full tabletop

Figure 38 | NCSC Insider Threat Tabletop Exercise

Each NCSC exercise in a box scenario includes a facilitator guide, a collection of injects (updates to introduce in the exercise to simulate evolving events), and a list of desirable and optional attendee roles (senior incident leader, cybersecurity engineer, HR advisor, PR officer, etc.). Each participant gets a short briefing to help them understand their role and responsibilities during the exercise.

The NCSC tabletop-in-a-box exercises are a great way to get started with incident response practice with minimal setup effort. Designed for brief sessions of thirty to sixty minutes, they allow for in-person and remote teams to collaborate and practice their incident response skills.

Proactive Prevention and Detection

Proactive prevention and detection measures reduce the likelihood of successful attacks and improve the organization’s ability to identify threats early. While these activities extend beyond traditional incident response boundaries, they directly contribute to response effectiveness by reducing incident frequency and severity. These activities are primarily technology-focused: deploying monitoring and detection capabilities, hardening systems, and ensuring the logging and infrastructure needed to support investigation and response are in place.

Implement Cyber Threat Intelligence (CTI) Capabilities Cyber threat intelligence provides context that transforms security data into actionable insight.

Understanding the threats targeting the organization and industry allows the incident response team to prioritize defenses, recognize attack patterns, and respond more effectively when incidents occur.

CTI capabilities support incident response in several ways: through proactive defenses, detection enhancement, support for investigations with additional context, and prioritization of response efforts.

Table 9 summarizes several CTI capabilities for incident response.

Table 9 | CTI Capabilities for Incident Response

CAPABILITY DESCRIPTION Proactive Defense Intelligence about emerging threats enables organizations to implement protections before attacks materialize. When threat intelligence reveals a new campaign targeting the industry, security teams can deploy detections and harden systems before becoming victims.

Detection Enhancement Indicators of compromise (IOCs) from threat intelligence feeds can be integrated into detection systems to identify known malicious infrastructure, file hashes, and behavioral patterns.

Investigation Context During incidents, threat intelligence helps analysts understand attacker motivations, typical tactics, and what to look for during scoping. Attribution information can inform response decisions and help predict attacker behavior.

Prioritization Not all vulnerabilities and threats pose equal risk. Threat intelligence helps prioritize remediation efforts based on active exploitation and relevance to the environment.

Organizations can obtain threat intelligence from commercial providers, industry Information Sharing and Analysis Centers (ISACs), government sources such as CISA and sector-specific agencies, open-source intelligence (OSINT) feeds and communities, and internal intelligence developed from past incidents. Each source offers different perspectives and coverage, so most organizations benefit from combining multiple feeds.

Threat intelligence is only valuable when it is operationalized for the organization and the incident response team. To obtain value from CTI sources, organizations should establish processes to review incoming intelligence, assess relevance, and take appropriate action.

Intelligence that sits unread provides no actionable security benefit.

Standardized Threat Intelligence with STIX

Structured Threat Information eXpression (STIX) is an open standard for representing cyber threat intelligence in a machine-readable format. STIX enables organizations to share and consume threat data consistently across different platforms and tools. When an ISAC distributes indicators of compromise, or when a commercial threat feed delivers new intelligence, STIX defines a common data structure that enables automated ingestion and correlation.

Defined by the OASIS Cyber Threat Intelligence Technical Committee (CTI TC), the current STIX version is 2.1, using JSON as the underlying serialization format. [15] A STIX indicator for a malicious URL used in a spear phishing campaign might look like this:

{

"type": "indicator",

"spec_version": "2.1",

"id": "indicator--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",

"created": "2025-12-31T14:30:00.000Z",

"modified": "2025-12-31T14:30:00.000Z",

"name": "Credential phishing URL",

"description": "Malicious URL mimicking corporate login page",

"indicator_types": ["malicious-activity"], "pattern": "[url:value = 'hxxps://login-secure-verify[.]com/auth']", 1

"pattern_type": "stix",

"valid_from": "2025-12-31T14:30:00.000Z"

}

1 Pattern matching a malicious URL The pattern field in the STIX data object uses STIX Patterning Language to define what the indicator matches. Security tools that support STIX can automatically parse this structure and create detection rules or blocklist entries. This automation transforms raw intelligence into operational defense without manual intervention.

STIX 2.1 defines a rich set of object types beyond simple URL or IP address matches. STIX domain objects include threat actor identifiers, specific campaigns, intrusion sets, malware definitions, attack patterns, vulnerabilities, and courses of action. Observable objects represent the technical artifacts analysts encounter during investigations: IP addresses, domain names, file hashes, email messages, network traffic, and registry keys. Relationship objects connect these elements together, linking a threat actor to the campaigns they conduct, the malware they deploy, and the vulnerabilities they exploit.

This interconnected structure enables threat intelligence to tell a complete story about a domain of activity and its actions, rather than providing isolated data points. When an organization receives a STIX bundle describing a new ransomware campaign, analysts gain not only the IOCs for detection but also insight into the threat actor’s tactics, the targeted vulnerabilities, and recommended defensive actions to inform an appropriate response plan.

CTI Platforms

Without a dedicated platform, managing multiple intelligence feeds, correlating indicators across sources, and maintaining context over time becomes increasingly difficult. A CTI platform provides a centralized environment for ingesting, enriching, analyzing, and sharing threat intelligence. Organizations can use a CTI platform to aggregate intelligence from commercial feeds, ISACs, government sources, and internal investigations into a single repository, with relationships between threat actors, campaigns, indicators, and vulnerabilities maintained automatically.

During active incidents, analysts can search the platform for intelligence related to newly identified indicators, discover connections to known campaigns or threat actors, and identify additional indicators to feed into scoping efforts. This capability transforms threat intelligence from a preparation activity into an active investigation resource.

CTI platforms can provide visibility into trends across observed attacks. By aggregating indicators over time, analysts can identify which threat actors are most active against the organization’s sector, which techniques are trending in recent campaigns, and which infrastructure patterns recur across incidents. This trend analysis helps to inform decisions during active response. When a new incident shares characteristics with a campaign the platform has been tracking, analysts can draw on the accumulated intelligence to anticipate the attacker’s next steps, prioritize which systems to scope, and recommend containment actions based on observed patterns rather than starting from scratch.

OpenCTI is one option for organizations looking to centralize their CTI capabilities. As an open-source platform, the Community Edition is free and provides core capabilities including STIX 2.1 ingestion, entity correlation, and integration with detection tools through connectors. The commercially-supported Enterprise Edition adds collaborative workspaces, advanced analytics, and role-based access controls designed for larger teams. Example views of the OpenCTI dashboard and indicator drill-down are shown in Figure 39 and Figure 40.

Figure 39 | OpenCTI Platform Dashboard

Figure 40 | OpenCTI Indicator Drill-Down

for correlation and context becomes more important for effective incident response.

Develop Processes and Procedures for Software Management

Effective software management reduces the attack surface available to attackers. Five areas deserve particular attention: patch management, configuration management, software inventory, software supply chain security, and end-of-life management.

Core Software Management Areas: Patch, Config, and Inventory

Patch management establishes processes to identify, test, and deploy security patches across the environment. Start by identifying vulnerabilities through vendor advisories, scanning tools, and threat intelligence feeds. Prioritize remediation based on exploitability and asset criticality, giving accelerated attention to vulnerabilities under active exploitation. Establish testing procedures to validate patches before broad deployment, and define exception handling for systems that cannot be patched immediately.

Configuration management maintains documented, version-controlled configurations for systems and applications. During incidents, configuration baselines help analysts identify unauthorized changes that may indicate compromise. When recovery requires rebuilding systems, documented configurations enable rapid restoration to known-good states. Configuration management also documents dependencies and integration points relevant to scoping, and supports rollback when changes introduce problems during recovery.

Software inventory tracks installed software, including version information across the environment.

Software Bill of Materials (SBOM) capabilities help identify systems affected by vulnerabilities in third-party components. When a new vulnerability emerges in a widely used library, accurate software inventory enables rapid identification of affected systems.

Formal software inventory processes often miss shadow IT, where departments or individuals purchase SaaS subscriptions, cloud services, or software licenses outside of approved procurement channels. A practical discovery technique is to review recurring billing statements and expense reports for subscription services that may not appear in official asset inventories. These shadow services expand the organization’s attack surface and create gaps during incident scoping, and attackers increasingly target unmanaged SaaS platforms and cloud accounts where security monitoring and hardening controls are absent.

Supply Chain Security and End-of-Life Management

Software supply chain security addresses the reality that every application an organization deploys carries implicit trust in a broad chain of upstream contributors. A vendor’s product may appear to come from a single source, but modern software typically assembles components from dozens or hundreds of open-source libraries, third-party software development kits (SDKs), and developer packages. Each upstream dependency represents an additional organization, maintainer, or project that an attacker could compromise to reach downstream targets. This reality expands the attack surface well beyond what traditional vendor risk assessments capture.

Attackers exploit this expanded surface through multiple vectors: compromising package repositories such as the Node Package Manager (NPM) or the Python Package Index (PyPI), injecting malicious code through dependency confusion or typosquatting, or compromising the accounts of trusted maintainers. [16] A single compromised component can propagate across an organization’s software portfolio through transitive dependencies, affecting systems that never directly referenced the malicious package.

Organizations should account for supply chain risk as part of their software management practices. Extend the SBOM capabilities described above to encompass vendor-supplied applications, not only internally developed code. Where the organization develops software internally, pin dependencies to known-good versions using lock files and hash verification, configure private registries or repository proxies to limit direct exposure to public repositories, and integrate dependency scanning into build pipelines. For vendor-supplied software, evaluate vendors' own supply chain security practices, including how they vet upstream dependencies and communicate supply chain incidents to customers. Accurate dependency inventories enable the organization to quickly identify affected systems and begin scoping when a supply chain compromise is disclosed.

End-of-life management tracks software that is approaching or past its vendor support dates. Software that no longer receives security updates presents an ongoing risk that cannot be mitigated through patching.

Identify systems running end-of-life software and establish plans for migration, replacement, or the implementation of compensating controls. During incidents, end-of-life systems often represent likely attack vectors because known vulnerabilities remain permanently unpatched.

PATCH MANAGEMENT AND PRIORITIZATION EFFORTS

For many organizations, the greatest challenge in software patch management is prioritization. All software update processes require effort, and many organizations struggle to keep up with the volume of monthly patches. Compounding this challenge, the more organizations fall behind on patching, the more difficult it becomes to catch up.

For example, as I wrote this chapter in December 2025, the CVE-2025-14847 "MongoBleed" vulnerability was receiving significant attention due to active exploitation in the wild. This unauthenticated vulnerability affects MongoDB instances as far back as releases in 2017 (MongoDB 3.6.0), allowing an attacker to gain access to system memory chunks by exploiting a vulnerability in

Figure 41 | Shodan Results for Internet-Exposed MongoDB Instances

Organizations running MongoDB instances that have not applied patches for this vulnerability face significant risk, with only a few days between the vulnerability disclosure and public exploit’s availability on December 25, 2025.

Figure 42 | X Release of MongoBleed Exploit

For many organizations, limited resources prioritize updates to critical software only when a critical-severity vulnerability needs to be addressed. It is common for organizations to run older versions of MongoDB software, either locally provisioned by an in-house IT team or as part of a turnkey application delivered by a third-party, deferring updates until a crisis forces action. When a vulnerability like MongoBleed emerges, organizations scramble to identify affected systems and apply patches, complicated by the need to make significant version jumps rather than incremental updates.

Organizations that defer software management pay a higher price when critical vulnerabilities emerge. Regular patch cycles, accurate software inventory, and established testing procedures reduce the cost and chaos of emergency response. Organizations that fall behind on patching face compounding challenges: the more they defer, the more difficult it becomes to catch up.

Apply System Hardening Processes

System hardening reduces the attack surface by removing unnecessary features, applying security configurations, and implementing least-privilege principles. Hardened systems are more difficult to compromise initially and limit attacker options after initial access.

Start by disabling unnecessary services and removing features not required for system function. Each running service represents a potential attack surface that attackers can target. Change or remove default accounts and credentials, as attackers routinely attempt to use them during initial access attempts.

Deploy endpoint controls that monitor, alert, and block unauthorized access. Forward logging data to a central collection server for analysis and retention (see Collect and Retain Logging Information ). Logs from attackers from running malicious tools even after gaining access.

Figure 43 | CIS Benchmark Checklist for HPE Aruba Networks Device

Hardened systems also represent a valuable threat hunting opportunity. Following a compromise, an attacker may attempt to disable controls to accommodate other attacks.

When a system no longer matches the hardened baseline, this deviation can serve as an effective indicator of compromise.

Document hardening configurations and automate their application where possible. Infrastructure-as-code approaches enable consistent hardening across environments and simplify rebuilding systems during recovery. Alternatively, PowerShell or other shell scripts can automate hardening tasks on existing systems, enabling organizations to achieve greater consistency in their hardening efforts. Review and update hardening baselines regularly as new vulnerabilities and attack techniques emerge.

Implement Endpoint-Based Security Monitoring and Threat Detection Endpoint Detection and Response (EDR) tools provide essential visibility into host-based activities. EDR products support both proactive threat detection and incident investigation, making them a valuable tool for protecting systems and aiding incident investigations.

Product-specific labels for endpoint protection tools vary, including Endpoint Detection and Response (EDR), Extended Detection and Response (XDR), Next-Generation Antivirus (NGAV), and Endpoint Protection Platform (EPP). This section refers to endpoint protection tools as EDR for simplicity, but the concepts apply broadly across these product categories.

EDR platforms collect telemetry, including process execution, file system changes, registry modifications, and network connections. This telemetry enables behavioral detection of suspicious patterns, such as process injection, credential dumping, anomalous usage, and persistent access tool deployment. Analysts can query collected telemetry to hunt for indicators across managed endpoints. Responders can take remote actions to isolate systems, terminate processes, or collect evidence for additional analysis.

Gaps in EDR coverage create visibility gaps that attackers can exploit. Notably, third-party systems, legacy devices, and cloud instances are often excluded from EDR deployment.

Ensure coverage extends across the environment, including servers, workstations, and cloud instances.

EDR effectiveness depends on proper configuration and alert tuning. Work with vendors or internal teams to tune detection rules for the environment, reducing false positives while maintaining sensitivity to genuine threats. Establish processes to promptly review and investigate EDR alerts, as delayed investigation gives attackers additional time to achieve their objectives.

EDR AS A SUCCESS STORY

As a professional penetration tester, the biggest challenge I face is not in gaining initial access to a target environment. Rather, it’s preserving that access long enough to achieve my objectives without being detected and removed by endpoint protection systems.

Common techniques for gaining initial footholds, such as exploiting public-facing web applications or manipulating users into authorizing malicious actions, remain well understood and frequently tested.

However, once inside an environment, maintaining persistence and moving laterally without detection has become increasingly difficult. Even novel techniques developed internally often trigger detection by well-configured EDR solutions.

This represents a genuine success story for organizational security. EDR deployments have fundamentally changed the economics of attacks by making post-compromise activities expensive and risky for attackers. Organizations with mature EDR implementations regularly detect and disrupt intrusions that would have succeeded just a few years ago.

In response, attackers have adapted. Supply chain compromises, cloud token theft, and social engineering techniques that bypass endpoint protections entirely have become more prominent. This tactical shift is evidence that EDR works, but also a reminder that defenses cannot remain static. As attackers evolve their techniques, organizations should continue investing in complementary controls that address the gaps attackers now target.

Deploy Sysmon for Enhanced Windows Telemetry

System Monitor (Sysmon) is a free tool from the Microsoft Sysinternals suite that extends default Windows event logging with high-fidelity telemetry for security monitoring and investigation. [17] arguments and parent process information, network connections with source and destination details, file creation timestamps, registry modifications, and driver and DLL loading events. This telemetry fills important gaps that default Windows audit logging does not cover.

During incidents, Sysmon logs provide investigation-grade detail that persists in the Windows Event Log.

Analysts can reconstruct process execution chains, identify lateral movement through remote service activity, and trace attacker tooling across compromised hosts. Sysmon is particularly valuable in environments with incomplete EDR coverage, including legacy systems, third-party-managed hosts, and lab or development environments where EDR agents may not be deployed. For organizations with EDR coverage, Sysmon provides a complementary and independent telemetry source that remains available even if an attacker disables or evades the EDR agent.

From a prioritization perspective, Sysmon is a high-value preparation resource for organizations with significant Windows environments, especially those with EDR coverage gaps. Sysmon provides valuable visibility into Windows activity, supporting both proactive detection and incident investigation. Investing some time into deploying and configuring Sysmon can yield significant benefits for incident response teams.

Sysmon’s value depends heavily on its configuration. The default configuration captures a broad set of events, but without filtering it generates significant noise that can overwhelm log collection infrastructure.

The SwiftOnSecurity Sysmon configuration  provides a highly curated community starting point that balances noise reduction with detection coverage. Organizations should use this configuration as a baseline, then tune it for their environment by adding exclusions for known-good activity and additional rules for organization-specific detection needs. Forward Sysmon events to central log collection alongside other security telemetry to enable correlation and long-term retention.

Sysmon deployment pairs well with adversary simulation. After deploying Sysmon with a tuned configuration, run atomic tests against ATT&CK techniques relevant to the organization’s threat profile and verify that the expected telemetry appears in the collected logs. This validation confirms that Sysmon is capturing the events needed for detection and investigation.

Implement Network Security Monitoring and Threat Detection

Network monitoring provides visibility into communications between systems and with external networks.

Where endpoint monitoring systems provide host-level visibility limited to a single host at a time, network monitoring offers insight into traffic traversing the network, providing a broader perspective for threat detection. This visibility enables analysts to detect command-and-control (C2) activity, lateral movement traffic patterns, and data exfiltration attacks that host-based monitoring can miss.

Organizations can implement network monitoring through several complementary approaches, each offering different tradeoffs between visibility, storage requirements, and analytical capabilities. No one solution will meet the needs or constraints of every organization, so consider the options available in the context of the organization’s needs, budget, and technical capabilities.

Full Packet Capture

For many years, full packet capture (FPC) represented the gold standard for network monitoring. Many organizations invested heavily in capturing and storing complete network traffic for retrospective analysis, including threat hunting and incident investigation. However, these investments proved costly to maintain, and the volume of data can easily overwhelm analysts' ability to process and analyze it effectively. Further, the use of network transport encryption for modern protocols can limit the value of captured data unless there is a secondary capability to decrypt traffic for analysis. Additionally, the cost of storage and processing required for capture increases substantially as network traffic rises with higher-bandwidth connections, an increased number of devices, and the increasingly common shift to cloud-based services, including SaaS platforms.

STRATEGIC PACKET CAPTURE

For organizations committed to packet capture, a strategic approach can maximize value while managing costs.  Phil Hagen, a SANS instructor who has written extensively on network forensics, offers practical guidance for optimizing capture investments.

Phil indicates that the fundamental challenge (after cost and resources) is that encryption of network transport data makes FPC substantially less useful. Even for organizations that aim to use acquired private key material to decrypt captured traffic (the store-now-decrypt-later approach), Perfect Forward Secrecy (PFS) and emerging post-quantum cryptography have closed the door on this approach. This reality demands a shift in strategy: rather than capturing everything and hoping to analyze it later, focus resources on traffic that provides immediate analytical value.

Start by identifying what traffic can be collected through TLS-decrypting proxies. Zero Trust solutions such as Zscaler, Netskope, and similar platforms can provide visibility into encrypted traffic at the proxy-interception layer. For traffic that cannot be decrypted, deprioritize commonly encrypted traffic on ports such as 22 (SSH), 443 (HTTP over TLS), and 993 (IMAP over TLS), where payload inspection provides limited value.

For encrypted traffic worth retaining, consider truncating capture at twenty to thirty packets per socket. This approach preserves the TLS negotiation phase, which contains valuable metadata: certificate information, cipher suites, and TLS ClientHello message fingerprints (using multiple JA4+ fingerprinting techniques). These artifacts support detection and investigation even when payload content remains encrypted.

For organizations with tighter constraints, excluding encrypted traffic entirely while ensuring comprehensive Netflow coverage provides a reasonable alternative. Migrate detection heuristics and artifact collection to focus on what remains analyzable rather than attempting comprehensive capture.

These recommendations are often set aside for cost, complexity, sensitivity, or legal reasons.

However, they remain valuable for consideration in limited capacities or during active incident response when targeted visibility becomes critical.

Network Flow Monitoring

As an alternative to FPC, many organizations will benefit from network flow monitoring. Flow data provides a summary of network communications without the storage burden of full packet capture, making it practical for long-term retention and broad deployment. Where FPC answers "what exactly was transmitted," flow data answers "who talked to whom, when, and how much," which is often sufficient for detection and initial investigation.

Network flow data captures summary metadata about network connections rather than full packet contents. A flow record represents a unidirectional sequence of packets sharing common attributes such as source, destination, and protocol. Table 10 describes some of the most useful fields available in flow records for detection and investigation.

Table 10 | Common NetFlow Fields

FIELD DESCRIPTION Source/Destination IP IP addresses of communicating hosts.

Source/Destination Port TCP or UDP ports identifying services.

Protocol Transport protocol (TCP, UDP, ICMP, etc.).

Timestamps Flow start and end times for timeline analysis.

Byte Count Total bytes transferred; useful for detecting data exfiltration.

Packet Count Number of packets; reveals broad traffic patterns.

TCP Flags Flags observed (SYN, ACK, RST, etc.) for connection analysis.

Interface/Direction Traffic direction (ingress/egress) through the network.

This metadata enables analysts to identify anomalous communication patterns, quantify data transfer volumes, detect beaconing behavior, and trace lateral movement paths across the network.

Several flow technologies exist, each with different origins and formats but providing similar analytical value. Cisco NetFlow and its successor IPFIX (IP Flow Information Export) remain widely deployed in enterprise environments. sFlow, developed by InMon Corporation, uses statistical sampling to reduce processing overhead on high-bandwidth networks.

Flow data from network engineering equipment (routers and switches) is typically sampled, often at ratios of 1:1000 packets or higher, missing significant portions of traffic. Security-focused flow data from firewalls is usually unsampled by default, providing complete visibility. When relying on router-generated flow data for incident response, verify the sampling configuration and account for potential gaps in coverage.

Cloud environments offer native flow logging via services such as AWS VPC Flow Logs, Azure NSG Flow Logs, and Google Cloud VPC Flow Logs. While the specific fields and formats differ across these technologies, the core value proposition remains consistent: lightweight metadata collection that enables traffic analysis without the cost of full packet capture.

Extended Berkeley Packet Filter (eBPF) Extended Berkeley Packet Filter (eBPF) builds on the original Berkeley Packet Filter (BPF), a packet-filtering mechanism introduced in the early 1990s for capturing network traffic. Where BPF operated as a straightforward packet filtering capability, eBPF extends this concept into a general-purpose, programmable framework for safely executing custom code within the operating system kernel. This evolution transforms what was originally a network capture tool into a comprehensive observability capability. eBPF programs run in a sandboxed virtual machine within the kernel, with a built-in verifier that checks each program for safety before execution. This design provides deep visibility into kernel-level activity, including network connections, system calls, file operations, and process execution, without requiring custom kernel modules or system reboots. The low overhead and safety assurances make eBPF valuable for continuous monitoring on production systems.

For incident response preparation, eBPF offers several advantages over traditional monitoring approaches.

Network monitoring tools built on eBPF can generate flow data, capture connection metadata, and inspect packet headers directly in the kernel, supplementing or replacing conventional NetFlow infrastructure.

Beyond network visibility, eBPF-based security tools observe process behavior, file access patterns, and privilege changes at the system-call level, providing the kind of host telemetry that supports both detection and forensic investigation. Open-source projects such as Cilium, Falco, and Tetragon utilize eBPF to deliver network policy enforcement, runtime threat detection, and security observability for traditional systems and for containerized environments.

While eBPF originated in the Linux kernel, Microsoft is actively developing eBPF support for Windows through the eBPF for Windows project, extending this observability framework to Windows environments.

As eBPF adoption expands across operating systems, organizations that invest in eBPF-based monitoring gain a unified observability approach that spans network, host, and container workloads.

Network Detection and Response (NDR) Network Detection and Response (NDR) platforms analyze network traffic for threats using behavioral analysis, signature-based detection, and threat intelligence integration. These platforms process network data in near-real time, applying machine learning models to identify anomalous patterns and matching
