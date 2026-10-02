# Chapter 15-1: Debrief: Visual Timeline Reconstruction & Post-Incident Review

> Modular Sub-Chapter | Source: DAIR-IR Framework

---

# Chapter 15: Debrief Activity: Root Cause & Post-Mortem

3. Establish monitoring duration and procedures, including:

◦ Define a monitoring period appropriate to incident severity (typically thirty days minimum).

◦ Document what constitutes abnormal behavior requiring investigation.

◦ Establish response procedures for alerts on recovered systems.

◦ Assign responsibility for monitoring review during the enhanced monitoring period.

Step 5. Execute Coordinated Production Restoration

1. Identify system dependencies and restoration sequence, including:

◦ Map dependencies between affected systems.

◦ Identify foundational services (AD, DNS, network infrastructure) requiring early restoration.

◦ Document the restoration sequence based on dependency analysis.

◦ Coordinate sequence with system owners and IT operations teams.

2. Coordinate restoration timing with stakeholders, including:

◦ Present scheduling options and associated risks to decision-makers, recommending off-hours restoration where feasible to reduce user impact, ease monitoring, and provide rollback flexibility.

◦ Recognize that timing decisions ultimately belong to organizational leadership.

◦ Document guidance provided and decisions made regarding timing, including rationale when leadership chooses immediate restoration against recommendations.

◦ Communicate the restoration schedule to all affected teams.

◦ Prepare rollback procedures in case restoration encounters problems.

3. Select phased or coordinated restoration based on context, including:

◦ Use phased recovery when eradication confidence is limited or capacity is constrained. Restore a small set of systems first, enable monitoring, and watch for anomalies before scaling up.

◦ Use coordinated recovery for interconnected systems with well-documented dependencies that require simultaneous restoration.

◦ Restore systems according to the planned sequence.

◦ Validate each system or phase before proceeding to the next.

◦ Monitor for issues during and immediately after each restoration.

◦ Document any deviations from the planned restoration sequence.

4. Manage recovery coordination complexity, including:

◦ Designate an incident response coordinator for incidents spanning multiple systems and teams to track progress, facilitate communication, and ensure steps execute in the proper sequence.

◦ Define explicit handoff criteria between restoration, validation, acceptance testing, and production release.

◦ Translate technical recovery work into business language when engaging with leadership to manage business pressure for rapid restoration.

◦ Prepare communication templates for common scenarios (delays, partial restoration, user action required) before recovery begins.

◦ Establish post-recovery baseline documentation through thorough acceptance testing and owner sign-off to defend against misplaced problem attribution when unrelated issues emerge later.

5. Address cloud recovery considerations (when applicable), including:

◦ Verify cloud snapshot creation dates against the incident timeline before restoring instances.

◦ Audit IAM access mechanisms, including API keys, access tokens, service account credentials, role assignments, and policies.

◦ Validate that multi-factor authentication is enabled for all users with access to cloud resources.

◦ Review infrastructure-as-code templates and version control history for unauthorized modifications.

◦ Consider increasing the verbosity of cloud logging (API access, network connections, resource changes) during post-recovery monitoring.

6. Coordinate user communications, including:

◦ Designate communication leads to manage messaging to affected users and stakeholders.

◦ Establish a regular communication cadence with stakeholders and stick to it, even when there is no new information.

◦ Avoid overpromising specific restoration timelines, as delays may erode credibility.

◦ Prepare template messages for common scenarios (delays, partial restoration, user action required).

◦ Use multiple communication channels, recognizing that some systems (email, chat) may be unavailable.

7. Address data loss from clean-backup recovery, including:

◦ Identify data created or modified since the last clean backup.

◦ Recover user-created files and application data from newer backups only after verifying they are free of attacker artifacts.

◦ Coordinate with business owners on acceptable data loss thresholds.

◦ Document data recovery decisions and any accepted losses.

Step 6. Remove Containment Measures

Containment removal for individual systems occurs incrementally during Step 5 as each system completes validation and returns to production; a fully isolated system cannot be restored or tested in place without selectively lifting the measures that block its operation. Step 6 consolidates that work by inventorying all measures implemented during contain, tracking their status as each system returns, and evaluating which measures should be retained as durable controls rather than removed when recovery closes.

1. Inventory containment measures in place, including:

◦ Document all firewall rules, network segmentation, and access restrictions.

◦ Record disabled accounts, blocked services, and DNS sinkholes.

◦ Note the rationale and implementation date for each measure.

◦ Identify measures that should remain in place as permanent improvements.

2. Remove containment measures incrementally, including:

◦ Remove measures affecting each system as it completes validation and returns to production.

◦ Monitor for adverse effects after each removal of a containment measure.

◦ Document each removal action with a timestamp and the outcome.

◦ Verify system functionality after containment measures are removed.

3. Evaluate containment measures for permanent implementation, including:

◦ Assess which temporary measures provide long-term security value.

◦ Work with security architecture teams on permanent implementation.

◦ Document decisions about which measures to keep versus remove.

◦ Update security policies to reflect any permanent changes.

Step 7. Capture Recovery Metrics

1. Record recovery timeline for each system, including:

◦ Document when restoration began for each affected system.

◦ Record validation completion, owner acceptance, and production restoration timestamps.

◦ Calculate total recovery duration and identify any bottlenecks.

◦ Compare the actual timeline against any estimates provided to stakeholders.

2. Document issues and resolutions, including:

◦ Record problems encountered during restoration and how they were resolved.

◦ Document any adaptations to planned recovery procedures.

◦ Capture lessons learned while the information is fresh.

◦ Note any gaps in recovery documentation or procedures discovered during execution.

3. Track resource investment, including:

◦ Record personnel hours spent on recovery activities.

◦ Document third-party support services engaged and their contributions.

◦ Capture any additional costs incurred during recovery.

◦ Provide resource data for incident cost analysis and future planning.

4. Pass recovery documentation to debrief for consolidation, including:

◦ Hand off the recovery documentation in the form expected by debrief Step 3 (which consolidates documentation across all phases into the unified incident record).

◦ Ensure documentation is accessible for post-incident review.

◦ Prepare a summary handoff for ongoing enhanced monitoring (Step 4) and for the AAR.

15 Debrief Activity

The debrief activity marks the conclusion of the active incident and transitions the organization into post-incident learning and improvement. After completing the response actions loop, the debrief activity provides critical reflection on the incident and the response effort. The transition to debrief occurs when organizational decision makers direct it, or when no further threats remain to address. This activity transforms experience gained during the response effort into actionable improvements that strengthen future incident response capabilities.

Figure 131 | Debrief Activity Waypoint

DEBRIEF OBJECTIVES

The debrief activity serves two primary objectives: incident closure, which formally concludes the active response effort, and organizational learning, which transforms incident experience into lasting improvement. While the response actions loop focused on operational urgency, the debrief shifts to reflection and deliberate analysis. This transition requires a different mindset, moving from reactive response to planned assessment.

Incident Closure

Formally ending the response effort requires more than stopping the response actions loop. Throughout the response, the incident response team creates temporary assets (isolated systems, forensic images, temporary accounts, and enhanced monitoring configurations) and accumulates documentation across ticketing systems, chat channels, shared documents, and individual notes. The closure objective evaluates each temporary asset for retention, modification, or decommissioning, consolidates dispersed documentation into an authoritative incident record, and captures metrics that quantify the response effort. This work preserves organizational memory, maintains regulatory compliance, supports potential legal proceedings, and provides the baseline data that informs the after-action review and future response improvements.

Organizational Learning

Transforming a single incident into lasting improvement requires deliberate analysis after the pressure of active response has subsided. While root cause analysis began during eradication, the debrief provides an opportunity for deeper reflection. This broader perspective accounts for each iteration of the response actions loop. The analysis examines not only what the attacker did, but also the organizational shortcomings that enabled the attack and the response gaps that complicated remediation. The learning objective produces an after-action review, a finalized incident report, a stakeholder presentation, and an improvement plan that converts observations into action items with assigned owners and accountability mechanisms. This chapter examines strategies for conducting effective debriefs, the challenges organizations commonly face during this activity, and best practices for capturing insights from the incident to support organizational improvement.

ATTACKERS KEEP IMPROVING: SO SHOULD WE

Threat actors continuously refine their tactics, techniques, and procedures based on what works against their targets. Each successful campaign teaches them which tactics work, which defenses to expect, which detection gaps to exploit, and which evasion techniques prove effective. Organizations that fail to learn from incidents fall progressively further behind adversaries who treat every operation as a learning opportunity. The period immediately following an incident offers a unique window to drive security improvements. Stakeholders who might otherwise resist security investments (including time, resources, and money) become more receptive when confronted with tangible evidence of compromise. The incident response team can utilize this heightened awareness to advocate for resources and changes that would face resistance during normal operations. “Never let a good crisis go to waste.

- Winston Churchill This principle applies directly to incident response. The debrief provides the mechanism to convert crisis awareness into lasting organizational change before attention shifts to other priorities. Incident response teams that capture this momentum can secure funding, staff, and policy changes that strengthen the organization’s security posture for future threats.

DEBRIEF STRATEGIES

The debrief activity encompasses strategies for both incident closure and organizational learning. Closure strategies come first: transitioning from active response, managing temporary assets, consolidating documentation, and capturing incident metrics. Organizational learning strategies follow: conducting the after-action review, driving organizational improvement, developing the incident report, and presenting findings to stakeholders.

Transitioning to Debrief

Determining when to transition from active response to the debrief activity requires judgment from both the incident response team and organizational decision makers. Two primary conditions signal readiness for this transition: the response actions loop yields no new information about attacker presence or activity, or organizational leadership determines that the incident is sufficiently resolved to conclude active response. The first condition emerges organically from the response process. As iterations through scope, contain, eradicate, and recover produce diminishing returns, with no new compromised systems discovered, no additional persistence mechanisms identified, and no further compromise activity observed, the incident response team can recommend transitioning to debrief. This recommendation should be based on confidence that the threat has been eliminated and that the organization’s residual risk is minimal. The second condition reflects organizational priorities that extend beyond technical considerations. Leadership may determine that business operations have recovered sufficiently, that regulatory notification requirements have been met, or that continued active response provides insufficient value relative to its cost. This decision belongs to organizational decision makers, informed by the incident response team’s assessment of residual risk.

Figure 132 | Transition Considerations for Debrief Activity

Retention of forensic evidence can support future investigations, threat hunting, and incident response training. Beyond the available documentation produced during the investigation, preserved artifacts can provide valuable reference material for understanding attacker methods and improving detection capabilities. For evidence that has been reviewed and analyzed, and which offers no further investigative value or legal retention requirement, organizations should weigh the ongoing storage costs against potential future utility before deciding to retain it.

Temporary Accounts and Monitoring

Temporary accounts and elevated access granted during response should be revoked unless they serve ongoing operational needs and can be managed through standard access control processes. The retention of temporary accounts increases the attack surface and may introduce additional risks to the organization. The incident response team should use the incident documentation to identify all temporary accounts created during the response. These accounts should be disabled or deleted unless there is a compelling reason to retain them. The incident response team should update the incident documentation to reflect when accounts are removed, and by whom. In some cases, new accounts created during the incident response function may prove valuable for ongoing operations. For example, it may be desirable to retain accounts established for isolating privileges as part of a containment effort, or to separate privileges for admin access (e.g., jwright and jwright-admin). When retaining such accounts, the organization should integrate them into standard access management processes, including periodic review and revocation procedures.

Enhanced Monitoring Configurations

Temporary monitoring configurations deployed during response may provide ongoing value if they address previously unmonitored attack vectors or improve visibility into critical systems. The incident response team should evaluate these configurations during the debrief activity to determine if they should be retained, modified for permanent use, or removed. The following factors can help guide this determination:

• Coverage gaps: Do the temporary monitoring configurations address visibility gaps identified during the incident?

• Operational impact: Do the configurations impose performance overhead or generate excessive alerts that negatively impact operations teams?

• Maintenance requirements : Can the organization sustain the monitoring configurations through regular updates and maintenance?

• Integration with existing systems : Do the configurations align with the organization’s broader monitoring and detection strategy?

If the decision is made to retain temporary monitoring configurations, the team should document the rationale for retention, any modifications made for permanent use, and the individuals responsible for ongoing maintenance.

Consolidating Incident Documentation

The debrief activity provides an opportunity to consolidate the response documentation accumulated throughout the incident into a comprehensive incident record. This record captures the incident details and represents a valuable resource for the organization’s institutional knowledge. As described in Documentation during the verify and triage activities, the incident response team should build documentation continuously throughout the response rather than defer it to debrief. By the time the debrief begins, documentation exists in multiple locations: ticketing systems, chat channels, shared documents, and individual notes. The incident response team consolidates this dispersed information into an authoritative incident record. The incident response team should start by validating the incident timeline. The timeline constructed during active response may contain gaps, inconsistencies, or timestamps that require refinement based on subsequent analysis. Walking through the timeline with important responders helps verify accuracy and fill in missing details while memories remain fresh.

Figure 133 | Sample Incident Timeline in Excel

The team should document the important decisions made during the response, including the alternatives considered and the rationale for the chosen approach. To balance time investment with value to the organization, analysts should focus on capturing decisions that had significant impact on the incident outcome, or were otherwise controversial or complex. Where possible, the team should capture information about decisions that later proved suboptimal along with analysis of what information would have led to better choices (e.g., the hindsight is 20/20 perspective for future learning). This decision record proves valuable for future incidents, regulatory inquiries, and potential legal proceedings.

DOCUMENTATION AND VALUE PROPOSITION: REQUIREMENTS FOR THE

system(s), response actions taken, and confirmation of resolution. A brief summary reviewed and approved by the incident lead adds collaborative value from a senior analyst without excessive overhead on the team. Incidents like commodity malware infections, single-system compromises, or incidents resolved through standard playbook procedures may fall into this category where the investment of extensive documentation outweighs the benefits. More serious incidents typically warrant more formal documentation. When incidents affect multiple systems, involve data exposure, require executive decisions, or trigger regulatory breach notification obligations, the organization benefits from more structured incident reports. These reports preserve institutional knowledge, support compliance requirements, and provide reference material for future incidents. The decision point between lightweight and formal documentation should be defined before incidents occur. Organizations can establish severity thresholds or incident categories that trigger different documentation requirements. For example, any incident requiring external notification, involving a compromised privileged account, or exceeding a defined scope threshold might automatically require formal documentation. Clear criteria prevent ad hoc decisions during the post-incident period when teams are fatigued and eager to return to normal operations.

Figure 134 | Documentation Detail Flowchart

Some organizations default to minimal documentation and later regret missing details when similar incidents recur or when auditors request evidence of response activities. Others over-invest in documentation for minor incidents, consuming resources that could be better allocated elsewhere. The goal is to find the appropriate balance for your organization’s risk profile, regulatory environment, and operational capacity.

Capturing Incident Metrics

During the debrief activity, the incident response team should calculate and record incident metrics that measure response effectiveness. These metrics provide baseline data for tracking organizational improvement over time. As discussed in Getting Started , organizations should focus on internal improvement rather than external benchmarking. Important metrics to capture include:

• Mean Time to Detect (MTTD) : The elapsed time between when the incident began and when the organization detected it. Calculating MTTD often requires determining the incident start time retrospectively based on investigation evidence.

• Mean Time to Respond (MTTR) : The elapsed time from detection to incident resolution. Organizations may track MTTR in stages, such as time to containment, time to eradication, and time to full recovery, if those metrics are valuable for the organization or as directed by decision makers.

• Scope of Impact : The number of systems, users, and data assets affected by the incident. This metric helps quantify incident severity and correlate response effort with incident scope.

• Resource Utilization : The personnel hours, external consulting costs, and tool expenses consumed during response. This data supports future resource planning and helps justify security investments.

• Total Incident Lifecycle : The complete duration from initial compromise to verified resolution. This metric combines MTTD and MTTR to show the full timeline of the attacker’s presence and the organization’s response.

For example, consider the metrics from the Colonial Pipeline ransomware incident in 2021, as shown in Table 35 . Summarizing the incident metrics provides a clear picture of the response effort and its effectiveness. In addition, organizations may choose to record these metrics in a more formalized manner (e.g., an incident-tracking database or a codified spreadsheet) to facilitate analysis across multiple incidents. The Colonial Pipeline incident metrics are collected from public information or otherwise presented as estimates where noted.

Table 35 | Colonial Pipeline Incident Metrics (2021)

METRIC VALUE NOTES

Mean Time to Detect (MTTD) 8 days Initial access April 29; ransomware detected May 7 Mean Time to Respond (MTTR) 8 days Detection May 7; operations restored May 15 Time to Containment <1 day Pipeline systems isolated same day as detection (May 7)

METRIC VALUE NOTES

Time to Eradication ~2 days Persistence removed and attacker access revoked by May 8 (estimated) Time to Full Recovery 8 days May 7 detection to May 15 full restoration Scope of Impact - Systems 5,500 miles of pipeline IT systems compromised; OT systems proactively shut down Scope of Impact - Data 100 GB exfiltrated Data staged and exfiltrated before ransomware deployment Scope of Impact - Business 45% of East Coast fuel supply 6-day operational shutdown Resource Utilization - Ransom $4.4 million paid Approximately $2.3 million recovered by DOJ in June 2021 Resource Utilization - External Mandiant engaged Incident response retainer activated May 7 Total Incident Lifecycle 16 days April 29 initial access to May 15 full restoration Organizations should track these metrics consistently across incidents to identify trends and measure improvement. A single incident’s metrics have limited value in isolation. Tracking data consistently across multiple incidents reveals whether detection is improving, response actions are accelerating, and security investments are producing measurable results.

Conducting the After-Action Review

The after-action review (AAR) brings together incident responders and stakeholders to examine the response effort. This structured review examines what was supposed to happen, what actually happened, why differences occurred, and what changes will improve future responses. The AAR should occur soon enough after the incident that details remain fresh, but with enough distance to allow objective reflection. The AAR facilitates honest discussion of what worked and what did not. The facilitator should create an environment where participants feel invited to identify problems without fear of blame. The discussion should focus on processes and systems rather than individual performance. The goal of the AAR is to improve the incident response effort and overall security across the organization, not to assign fault for shortcomings. The incident response team should structure the AAR around six core questions:

• What was supposed to happen? The team should review the incident response plan, playbooks, and established procedures that should have guided the response. This question identifies which procedures were followed and which were not.

• What actually happened? Responders should walk through the incident timeline, decisions, and actions.

The discussion should note deviations from planned procedures and their outcomes.

• Why did it happen? The team should analyze the factors that caused deviations from expected procedures. This analysis distinguishes between plan failures (procedures that did not work as designed) and execution failures (procedures that were not followed as designed).

• What can we do better next time? The team should develop specific, actionable recommendations for improving detection, response procedures, tools, training, and organizational coordination.

• What worked well? Participants should identify the successful aspects of the response to be retained or expanded.

• Why did those aspects succeed? The team should examine the underlying reasons, which may be deliberate design, individual initiative, or fortunate circumstance. Understanding the cause allows the organization to engineer the favorable conditions into future responses rather than relying on them happening to recur.

The incident response team should document AAR findings and recommendations in a format that can drive follow-up action. Each recommendation should have an assigned owner with expected completion dates. The team should schedule follow-up reviews to verify that recommendations have been implemented.

VALUE IN DEVELOPING A VISUAL TIMELINE

A visual timeline of the incident can enhance the AAR by providing a clear, shared reference for discussion. Visual learners in particular will benefit from seeing the sequence of events, decisions, and actions laid out graphically. Visual timelines can take various forms, from Gantt charts to complex flow diagrams that illustrate parallel activities and decision points. Even a simple, high-level, linear overview of the events can provide valuable context for the AAR discussion.

Figure 135 | Sample Timeline for Colonial Pipeline Incident

After an incident, when details are no longer fresh in memory, a well-constructed visual timeline serves as a useful reference for subsequent learning and training.

Driving Organizational Improvement

The debrief activity’s ultimate value lies in translating lessons learned into organizational change. Recommendations that remain documented but unimplemented are wasted effort. The incident response team should work with decision makers to prioritize recommendations and secure the resources needed for implementation. Organizations can categorize recommendations by implementation timeline:

• Immediate actions address any outstanding vulnerabilities or gaps that pose ongoing risk. These changes should be implemented before the debrief concludes, or as soon as is practical, given resource constraints.

• Short-term improvements require planning and coordination but can be completed within weeks or a few months. These typically include procedure updates, additional monitoring, and targeted training.

• Long-term strategic changes require significant investment in tools, architecture, or staffing. These recommendations should be incorporated into security roadmaps and budget planning cycles.

Continuing the Colonial Pipeline example, the incident response team might present improvement recommendations as shown in Table 36.

Table 36 | Example Recommendations by Timeline (Colonial Pipeline)

TIMELINE RECOMMENDATION RATIONALE

Immediate Actions

Within 3 days Audit and confirm all remote access

requires MFA Single-factor VPN authentication enabled the initial compromise Within 3 days Deploy initial enhanced monitoring at IT/OT network boundary Proactive OT shutdown was necessary due to uncertainty about lateral movement Short-term Improvements Within 30 days Design and implement network segmentation between IT and OT environments Lack of segmentation forced precautionary OT shutdown during IT incident Within 60 days Deploy endpoint detection and response (EDR) across all systems Earlier detection could have reduced attacker dwell time from 8 days Within 60 days Establish privileged access management program Limit blast radius of compromised credentials Within 90 days Complete ransomware-specific incident response playbook Response decisions (ransom payment, decryptor vs. backup restoration)

TIMELINE RECOMMENDATION RATIONALE

6-12 months Deploy immutable, air-gapped backup infrastructure Ensure recovery capability independent of decryptor availability 12+ months Establish dedicated OT security operations capability Critical infrastructure requires specialized monitoring and response Ongoing Conduct quarterly tabletop exercises including ransomware scenarios Maintain response readiness and validate playbook effectiveness The incident response team should utilize the post-incident window to secure approval for improvements that might face resistance under normal circumstances. Presenting recommendations in business terms connects security investments to risk reduction. Wherever possible, the team should align security recommendations with other opportunities to minimize costs or optimize procedures. Incident metrics and impact assessments can quantify the cost of inadequate capabilities. Organizations should incorporate lessons learned into organizational processes. The team should update incident response plans and playbooks based on what worked and what did not. Detection rules and monitoring configurations should be revised based on how the incident was discovered and what visibility gaps existed. The team should develop training scenarios based on the incident to prepare responders for similar future events.

Developing the Incident Report

The incident report represents the primary deliverable of the debrief activity. This document captures what happened, how the organization responded, what impact resulted, and what changes will prevent similar incidents. The format and depth of incident reports vary widely across organizations, ranging from comprehensive, formal documents to structured entries in incident-tracking systems. The appropriate level of documentation depends on what is valuable to the organization. The incident report serves multiple purposes beyond documenting the incident itself. It provides training material for future responders, supports regulatory compliance obligations, establishes a record for potential legal proceedings, and creates institutional knowledge that persists beyond individual team members. Long after the incident is over, the incident report remains a reference for the organization to use in shaping future security strategies.

Report Audience

Different stakeholders require different levels of detail and different perspectives for the same incident. Understanding the audience for incident documentation helps ensure that reports communicate effectively and drive appropriate action. Understanding the report audience is critical to tailoring content and format appropriately. By focusing on what the audience needs to know rather than what the incident response team wants to document, the incident report becomes a more effective communication tool.

• Executive Leadership needs high-level summaries focused on business impact, risk exposure, and resource requirements. These reports are often high-level with minimal technical detail.

• Technical Teams require detailed technical documentation of attacker methods, affected systems, and remediation steps. IT and security staff responsible for implementing improvements need specific guidance on what to change and why.

• Legal and Compliance stakeholders need documentation that supports regulatory obligations and potential litigation. These reports emphasize evidence preservation, chain of custody, and adherence to legal standards.

• External Partners, such as customers, regulators, or industry-sharing groups, may receive sanitized versions of incident reports. These documents focus on transparency while protecting sensitive organizational information.

The report length varies based on audience needs. Few stakeholders will read a 150-page document in its entirety. To best meet the needs of the audience, organizations should consider the benefits of multiple report formats and structures tailored to different stakeholders.

Report Contents

Regardless of format, effective incident reports share common characteristics. They present information as objectively as possible, differentiating facts from analyst interpretation and inference. They maintain credibility by acknowledging uncertainty and documenting confidence and the reasoning behind conclusions. They provide actionable recommendations rather than just describing what happened. Before developing a report, the team should establish the intended purpose and constraints:

• Primary audience: Who will read this report, and what decisions will it inform?

• Distribution scope: Is this report strictly internal, or will it be shared with external parties?

• Evidentiary requirements: Does this report need to meet forensic standards for potential legal proceedings, or is it primarily an operational document?

• Compliance obligations: Do regulatory frameworks such as HIPAA, PCI DSS, or GDPR impose specific documentation requirements? Does the organization need to consider legal requirements like breach notification laws in the context of the report content?

• Format preferences: Does the organization prefer a single comprehensive document or separate reports for different audiences?

The answers to these questions shape both content and delivery format. For example, a report intended for regulatory submission differs substantially from an internal lessons-learned document.

Table 37 | Sample Report Contents: Purpose Considerations

Primary Audience Internal leadership and security teams

Distribution Internal, tightly controlled distribution

Evidentiary

Requirements

Moderate; focus on operational accuracy rather than forensic standards Compliance Obligations Supporting document for HIPAA breach notification requirements Format Preferences Two separate reports: executive summary and technical details Two-Report Approach A single incident report rarely serves all audiences effectively. Common challenges with a unified report include:

• Executives skip technical sections that dominate the document.

• Technical teams distrust sanitized summaries that omit important details.

• Legal teams may excerpt content out of context, losing its surrounding technical nuance.

Incident response teams that try to satisfy all audiences in a single document often spend too much time rewriting the same content for different readers, producing a report that fails to meet anyone’s needs. Instead of a one-size-fits-all report, the DAIR model advocates for a two-report approach. By separating technical details from a broader focus on business impact and organizational response, each report can be tailored to its audience. There’s no guarantee that every stakeholder will be satisfied, but this approach maximizes the likelihood that each group receives the information they need in a format they can use. A two-report approach offers a practical compromise to the dilemma of wasted time in developing a single unified report: an incident summary report for leadership and other stakeholders, and a technical incident response report for security teams and detailed documentation needs. This separation allows each report to serve its intended audience better than a single document could.

Incident Summary Report

The incident summary report communicates essential information to leadership and business stakeholders in a concise format. This report should be short enough that busy executives will actually read it, typically one to two pages plus any required attachments. The summary report typically includes:

• Report metadata , including incident identifier, report version, date issued, author, and data classification.

• Executive overview with incident type, detection date, a brief description of what occurred, business impact summary, important findings, and specific requests for leadership action.

• Business impact assessment covering operational disruption, data exposure, and financial or reputational consequences.

• Response actions summary highlighting important containment, eradication, and recovery steps at a high level.

• Incident metrics , including detection time, containment time, and total resolution time, with comparison to organizational baselines.

• Risk and control assessment summarizing root cause in non-technical terms, identifying gaps in organizational security controls that led to the incident, and characterizing residual risk to the organization.

• Recommendations and resource requirements to address the factors that contributed to the incident.

• Decisions required explicitly stating what leadership needs to approve, fund, or decide.

While an internal incident summary report for the Colonial Pipeline incident is not publicly available, a sample format is shown in Figure 136 to illustrate the typical structure and content.

Figure 136 | Incident Summary Report Sample

EXECUTIVE REPORTING LEVERS

Figure 137 | Collection of Levers (photo credit happyphoton)

My friend John Strand taught me to frame recommendations as a collection of levers: broad controls that decision makers can evaluate, prioritize, and act on after an incident. Each lever should give decision makers enough context to make an informed decision without requiring them to read the technical report. Present recommendations with a consistent framework that covers the dimensions decision makers care about:

• Opportunity: What gap or weakness does this address, and why does it matter now?

• Benefit: What risk reduction or capability improvement does the organization gain?

• Cost: What is the estimated investment in tools, licensing, or services?

• Time: How long will implementation take, and are there quick wins along the way?

• Resources: What staffing or expertise is required, and does the organization have it today?

• Compliance: Does this address a regulatory requirement or support audit readiness?

• Protections: What specific threats or attack techniques does this control mitigate?

For example, one lever might be titled "Limit attacker movement between business functions." The opportunity section would explain that during this incident, a single compromised account was able to reach financial systems, customer databases, and backup infrastructure without restriction. The benefit of pulling this lever: future incidents would be contained to the affected area, reducing the volume of sensitive data exposed and protecting critical operations from cascading disruptions.

Table 38 | Sample Executive Lever: Limit Attacker Movement Between Business Functions

DIMENSION DETAIL

Opportunity During this incident, a single compromised account accessed financial systems, customer databases, and backup infrastructure without restriction.

DIMENSION DETAIL

Benefit Future incidents contained to the affected area, reducing data exposure and protecting critical operations from cascading disruptions. Cost Estimated $180,000 in infrastructure investment with ongoing maintenance absorbed by existing staff. Time Phased rollout over 6 months, with the highest-risk boundaries in place within 60 days. Resources Implementation managed by the infrastructure team with support from an external integrator during the initial phase. Compliance Addresses PCI DSS network segmentation requirements and supports HIPAA access control obligations. Protections Directly mitigates the lateral movement technique used in this incident and reduces the blast radius of future compromises. Each lever should be supported by a detailed technical analysis in the accompanying technical incident response report, giving decision makers confidence that the recommendation is well-grounded and achievable. This structure transforms the recommendations section from a wish list into a decision framework, providing decision makers with clear options they can evaluate, prioritize, and fund.

Technical Incident Response Report

The technical report provides comprehensive documentation of the incident for security teams and forensic analysts, and serves as the detailed record of the response. This document is often longer, depending on incident complexity and organizational documentation standards. The technical report typically includes:

• Report metadata with version control and distribution restrictions.

• Scope and methodology documenting what was investigated and what constraints applied.

• Environment overview describing affected systems, network architecture, identity infrastructure, and logging coverage.

• Detection and triage documenting how the incident was discovered and initial response actions.

• Incident timeline presenting both attacker activity and response actions in chronological sequence.

• Attack analysis organized by attack phase: initial access, execution, persistence, privilege escalation, lateral movement, command and control, collection, exfiltration, and impact.
