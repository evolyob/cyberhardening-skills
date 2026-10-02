# Chapter 5: Incident Response Models and Limitations

essential for meaningful metrics, whether tracking manually or using automated tools. Start with three to five broad incident categories (e.g., malware, unauthorized access, data loss, denial-of-service) and refine them over time. 3. Use existing tools to automate data collection : Leverage ticketing systems (e.g., ServiceNow,

Jira), SIEM platforms, or incident response platforms. Most of these tools can automatically capture timestamps for incident creation, status changes, and resolution. Configure custom fields to capture the incident occurrence time and detection time, then build simple reports or dashboards to visualize MTTD and MTTR trends. This approach requires minimal investment while providing automated, consistent tracking. When building a metrics program, focus on consistency and accuracy rather than perfection. Consistently tracked imperfect data is more valuable than no data at all. Organizations can refine

their approach over time as they learn what metrics provide the most useful insight. COMPLEMENTING MTTR WITH QUALITY SCORING MTTR captures how quickly the team resolves incidents, but a fast resolution time tells you nothing

about whether the response was thorough. A team can close tickets quickly by cutting corners:

skipping log review, accepting initial triage without validation, or declaring a system clean after a surface-level scan. These shortcuts produce favorable MTTR numbers and poor incident outcomes. To balance the speed measurement, organizations can complement MTTR with a quality score applied to each incident ticket. A simple one-to-ten scale works as a starting point. For each ticket, a

reviewer considers questions such as: • Was the initial analysis thorough, or did the analyst rush past evidence? • Did the ticket sit idle for extended periods without progress?

• Were related systems identified and investigated, or was the incident treated as isolated?

• Was the root cause documented, or did the response stop at symptom remediation?

• Did the team close the ticket prematurely, leading to reopens or escalations later?

The quality score can surface patterns that MTTR alone cannot reveal: a team member who sits on

tickets for several days, analysts who rush through P1 incidents faster than P3 incidents (an inversion

that often signals pressure to close rather than actual capability), or incident categories in which the team’s understanding remains shallow. Tracking quality scores alongside MTTR over time provides a more complete picture of response effectiveness. A team that improves its quality scores while holding MTTR steady is genuinely improving. A team whose MTTR improves while quality scores decline is trading thoroughness for

speed. INCIDENT MANAGEMENT AND RESPONSE The terms incident management and incident response are often used interchangeably, but they have

distinct meanings. A clear understanding of these terms helps teams understand their roles and

responsibilities in the overall process of responding to security incidents. Figure 15 illustrates the relationship between these two functions with distinct and overlapping responsibilities. Figure 15 | Incident Response vs. Incident Management Responsibilities Incident Response

Incident response is the technical work of detecting, analyzing, containing, eradicating, and recovering from

a security incident. Analysts and responders validate and triage alerts, collect forensic artifacts, isolate compromised hosts, and restore services. Incident response is fundamentally a technical discipline focused on the incident itself: understand what happened, stop further damage, and return to a known-good state. Effective incident response requires both breadth and depth of technical skills. Responders need familiarity

with network analysis, host forensics, log interpretation, multiple operating systems, and cloud platforms, though few individuals are experts in all areas. Teams compensate by combining specialists whose skills complement one another, enabling the team to address the full range of technical challenges an incident presents. Analysts who support an incident response process require more than technical skill. They also need to apply critical thinking, problem solving, and clear communication to navigate the complexity of an incident

and coordinate with other teams and stakeholders. Incident Management Incident management is the broader organizational framework surrounding that technical work. It encompasses the coordination, communication, decision-making, and governance functions that support and direct the response effort. These functions include: • Stakeholder communication (executives, legal, public relations, regulators, and customers)

• Resource allocation and escalation • Cross-functional coordination (bringing in legal counsel, human resources, insurance, and law

enforcement as needed)

• Timeline tracking and documentation for compliance or litigation • Post-incident review ownership and remediation tracking

the organization responds in a coordinated, documented, and defensible manner. Both functions are

essential, and in practice they operate in parallel: responders investigate and contain the threat while

managers coordinate the organizational response. The relationship between incident response and incident management is not strictly hierarchical. In smaller organizations, the same team or individual may perform both functions. In larger organizations, dedicated incident managers coordinate across multiple response teams, business units, and external parties. Regardless of organizational size, the distinction helps clarify expectations: responders focus on the technical work of resolving the incident, while managers ensure that work is supported, communicated, and

aligned with organizational objectives. This book focuses primarily on incident response, the technical discipline of detecting, investigating, and resolving security incidents. However, responders should understand incident management functions, as effective response depends on the support and coordination incident management provides. In Part 2: A Dynamic Approach to Incident Response we present a response model that addresses both the technical and organizational dimensions of incident handling.

In this chapter, we introduced the foundational vocabulary of incident response: incidents, events, events of interest, and indicators of compromise. We also examined the metrics organizations use to measure detection and response effectiveness, and the distinction between incident response and incident management. Next, we’ll examine the incident response models that organizations have used to structure their response efforts, along with the limitations that have emerged as incidents have grown in complexity and scale. Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains (hxxps://www[.]lockheedmartin[.]com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf).

5 Incident Response Models and Their Limitations Incident response models provide a structured approach to managing and responding to cybersecurity incidents. These models outline the important phases and steps in the incident response process, helping organizations effectively prepare for, detect, respond to, and recover from incidents. Several incident response models have been developed and adopted by organizations worldwide, each with a unique approach and emphasis. THE CLASSIC MODEL: PICERL The classic model used for incident response is the PICERL model (pronounced Pick Earl), developed by Dr.

Eugene Schultz in 1990. [1]

The PICERL model was refined over the following years by the US Navy, the Carnegie Mellon University Software Engineering Institute, and the SANS Institute. It provides a systematic framework for incident response. PICERL is an acronym for the following steps: • Preparation • Identification

• Containment

• Eradication

• Recovery

• Lessons Learned

Each step builds on the previous one, providing a logical progression from readiness through resolution.

This model is often illustrated as a linear set of steps or as a stepped process, as shown in Figure 16 and

Figure 17 . In both illustrations, the process starts by preparing the organization for an incident and performing identification steps to discover incidents (e.g., threat hunting, log analysis, incident reporting). When an incident is identified, the incident response team limits its impact by containing it and collecting evidence for analysis. Using this evidence, the incident response team assesses the incident details and eradicates the threat. After the threat is eradicated, the organization recovers from the incident, followed by a lessons learned analysis to improve future incident response. Figure 16 | PICERL Model, Linear Figure 17 | PICERL Model, Stepped

The PICERL incident response model provides organizations with a clear framework for responding to

incidents and has been widely adopted across the industry. It offers a practical set of steps to follow, and it

emphasizes the need for actions that are often overlooked, such as limiting the attacker’s opportunities through containment and learning from incidents to improve future responses. THE NIST MODEL: SP 800-61 In 2012, the National Institute of Standards and Technology (NIST) published Special Publication 800-61

Revision 2 . NIST SP 800-61r2 provides recommendations for preparing for, detecting, analyzing, and

responding to incidents. It describes a process known as the Incident Response Life Cycle, as shown in Figure 18, focusing on four main phases: • Phase 1: Preparation • Phase 2: Detection and Analysis

• Phase 3: Containment, Eradication, and Recovery

• Phase 4: Post-Incident Activity

Figure 18 | NIST Incident Response Life Cycle

The NIST model is similar to the PICERL model; however, it prescribes a more flexible approach to the

elements that follow incident discovery, summarizing the containment, eradication, and recovery steps in

the PICERL model as a single phase. SP 800-61r2 offers more detailed guidance on the detection and analysis phases, with a post-incident activity phase that emphasizes not only lessons learned analysis (like PICERL) but also the collection and analysis of metrics for future resource allocation, and incident information sharing with a broader community. However, the revision 2 document is also a substantial reduction in the level of detail provided, with a notable lack of specific guidance on how organizations should recover following an incident.

NIST SP 800-61 REVISION 3 AND THE CYBERSECURITY FRAMEWORK

The evolution from NIST SP 800-61 Revision 2 to Revision 3 reflects a structural change in how NIST positions incident response within organizational cybersecurity programs. While the Revision 2 guide provided tactical incident handling guidance, the Revision 3 guide reframes incident response as an integrated component of broader cybersecurity risk management activities, eliminating the former four-step incident response life cycle model. The new revision, retitled Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile , aligns incident response with the NIST Cybersecurity Framework 2.0, moving away from the discrete incident handling methodology that characterized the previous version.

This restructuring changes the guidance on how organizations should approach incident response planning and implementation. Revision 3 requires incident response capabilities to be considered across the core CSF guidelines:

• Govern (GV): The organization’s cybersecurity risk management strategy, expectations, and policy are established, communicated, and monitored.

• Identify (ID): The organization’s current cybersecurity risks are understood.

• Protect (PR): Safeguards are used to manage the organization’s cybersecurity risks.

• Detect (DE): Possible cybersecurity attacks and compromises are found and analyzed.

• Respond (RS): Actions regarding a detected cybersecurity incident are taken.

• Recover (RC): Assets and operations affected by a cybersecurity incident are restored.

Together, these functions position incident response as one component of a comprehensive cybersecurity program rather than a standalone capability. [2]

The document now serves as a CSF 2.0 community profile, meaning organizations using the Cybersecurity Framework must integrate incident response considerations into their broader risk management processes and control implementations. The formerly circular incident response model is replaced with a flow that aligns with the CSF functions, as shown in Figure 19.

Figure 19 | NIST SP 800-61 Revision 3 Functions Aligned with the Cybersecurity Framework

Revision 3 shifts from Revision 2’s prescriptive incident-handling procedures to Revision 3’s framework-oriented approach that emphasizes organizational integration. Where Revision 2 provided specific methodologies and workflows for incident response teams, Revision 3 focuses on how incident response activities should inform and be informed by enterprise-wide cybersecurity decisions. As a high-level strategy for organizations, the Revision 3 guide encourages a more holistic view of incident response, embedding it within the overall cybersecurity posture rather than treating it as a standalone function. This is an important evolution. It reflects the growing recognition that effective incident response requires coordination across multiple organizational domains, including IT, legal, communications, and executive leadership. However, it does so by removing the detailed, step-by-step guidance that many incident response teams have relied on to guide the technical aspects of incident response.

VARIATIONS ON THE CLASSIC MODEL

Many product and consulting service providers publish their own incident response models. These variations are often minor modifications of the PICERL model, with additional emphasis that reflects the publishing organization’s incident response practices and experiences.

For example, several organizations advocate a seven-step incident response model that adds a re-testing step after the lessons learned step.

“In the event of a cybersecurity incident, best practice incident response guidelines follow a well-established seven step process: Prepare; Identify; Contain; Eradicate; Restore; Learn; Test and Repeat.

— Applied Risk, Seven steps to implementing a successful incident response plan

Figure 20 | Seven-Step Incident Response Model, Applied Risk BV (a DNV Company)

Other variations include a communication or documentation step following the eradication step. These variations are not substantively different from the PICERL model, but they may offer additional guidance or greater emphasis on specific aspects of incident response important to the publishing organization.

Other guidelines advocate for a circular model. One example is the Virginia Tech Guide for Cyber Security Incident Response . This guide advocates for a response process that includes preparation, identification/detection/analysis, containment, eradication, recovery, and incident closure, returning to the preparation phase.

Figure 21 | Virginia Tech Incident Response Process Model

Each of these models aims to provide a structured, organized methodology for incident response, with slight variations that reflect the experiences and priorities of the organization that developed them. While these variations of the classic model may offer additional insights or emphasis, they generally fall short of addressing important shortcomings in how organizations should best respond to modern cybersecurity incidents.

SHORTCOMINGS IN EXISTING MODELS

While these models provide helpful guidance based on their authors' experience, several common shortcomings persist across them, including:

• Insufficient emphasis on scoping

• Emphasis on linear models

• Inadequate resource prioritization guidance

• Lack of incident verification requirements

• Lack of root cause analysis

Understanding these limitations helps organizations adapt existing models to better fit their operational needs.

Insufficient Emphasis on Scoping

Scoping in incident response is the process of understanding the breadth of an incident. Neither the NIST SP 800-61 nor the PICERL models explicitly address this important step, which can lead to an incomplete understanding of the incident.

For example, consider an incident in which an analyst identifies that an unauthorized user has been added to a local system. Without proper scoping, the analyst may not realize that they were also added to multiple systems, resulting in an incomplete response. Scoping encourages responders to use available information to better understand the extent of the incident as part of the response effort.

Emphasis on Linear Models

In most representations of the PICERL model, the incident response process is a linear set of steps, starting with preparation and ending with lessons learned. In some adaptations, the process includes an iterative step, couched in phrases such as may or could to indicate the need to return to previous steps.

The NIST SP 800-61 model emphasizes a non-linear approach, with the detection and analysis steps repeated as more affected hosts are identified.

“If more affected hosts are discovered (e.g., new malware infections), repeat the Detection and Analysis steps (1.1, 1.2) to identify all other affected hosts, then contain (5) and eradicate (6) the incident for them.

— NIST SP 800-61r2 table 3-5, Incident Handling Checklist
