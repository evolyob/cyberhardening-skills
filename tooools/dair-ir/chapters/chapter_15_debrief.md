# Chapter 15: Debrief Activity: Root Cause & Post-Mortem

> Source: PDF Pages 430-467 (Total Pages: 38)

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

◦ Present scheduling options and associated risks to decision-makers, recommending off-hours

restoration where feasible to reduce user impact, ease monitoring, and provide rollback flexibility.

◦ Recognize that timing decisions ultimately belong to organizational leadership.

◦ Document guidance provided and decisions made regarding timing, including rationale when

leadership chooses immediate restoration against recommendations.

◦ Communicate the restoration schedule to all affected teams.

◦ Prepare rollback procedures in case restoration encounters problems.

3. Select phased or coordinated restoration based on context, including:

◦ Use phased recovery when eradication confidence is limited or capacity is constrained. Restore a

small set of systems first, enable monitoring, and watch for anomalies before scaling up.

◦ Use coordinated recovery for interconnected systems with well-documented dependencies that

require simultaneous restoration.

◦ Restore systems according to the planned sequence.

◦ Validate each system or phase before proceeding to the next.

◦ Monitor for issues during and immediately after each restoration.

◦ Document any deviations from the planned restoration sequence.

4. Manage recovery coordination complexity, including:

◦ Designate an incident response coordinator for incidents spanning multiple systems and teams to

track progress, facilitate communication, and ensure steps execute in the proper sequence.

◦ Define explicit handoff criteria between restoration, validation, acceptance testing, and production

release.

◦ Translate technical recovery work into business language when engaging with leadership to manage

business pressure for rapid restoration.

◦ Prepare communication templates for common scenarios (delays, partial restoration, user action

required) before recovery begins.

◦ Establish post-recovery baseline documentation through thorough acceptance testing and owner

sign-off to defend against misplaced problem attribution when unrelated issues emerge later.

5. Address cloud recovery considerations (when applicable), including:

◦ Verify cloud snapshot creation dates against the incident timeline before restoring instances.

◦ Audit IAM access mechanisms, including API keys, access tokens, service account credentials, role

assignments, and policies.

◦ Validate that multi-factor authentication is enabled for all users with access to cloud resources.

◦ Review infrastructure-as-code templates and version control history for unauthorized

modifications.

◦ Consider increasing the verbosity of cloud logging (API access, network connections, resource

changes) during post-recovery monitoring.

6. Coordinate user communications, including:

◦ Designate communication leads to manage messaging to affected users and stakeholders.

◦ Establish a regular communication cadence with stakeholders and stick to it, even when there is no

new information.

◦ Avoid overpromising specific restoration timelines, as delays may erode credibility.

◦ Prepare template messages for common scenarios (delays, partial restoration, user action required).

◦ Use multiple communication channels, recognizing that some systems (email, chat) may be

unavailable.

7. Address data loss from clean-backup recovery, including:

◦ Identify data created or modified since the last clean backup.

◦ Recover user-created files and application data from newer backups only after verifying they are

free of attacker artifacts.

◦ Coordinate with business owners on acceptable data loss thresholds.

◦ Document data recovery decisions and any accepted losses.

Step 6. Remove Containment Measures

Containment removal for individual systems occurs incrementally during Step 5 as each system completes

validation and returns to production; a fully isolated system cannot be restored or tested in place without

selectively lifting the measures that block its operation. Step 6 consolidates that work by inventorying all

measures implemented during contain, tracking their status as each system returns, and evaluating which

measures should be retained as durable controls rather than removed when recovery closes.

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

Recover Activity | Chapter 14 | 407

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

◦ Hand off the recovery documentation in the form expected by debrief Step 3 (which consolidates

documentation across all phases into the unified incident record).

◦ Ensure documentation is accessible for post-incident review.

◦ Prepare a summary handoff for ongoing enhanced monitoring (Step 4) and for the AAR.

[1] Eze Sunday, "AWS Outage Breaks Most of the Internet: My Thoughts," AWS in Plain English, December 2021, aws.plainenglish.io/

aws-outage-breaks-most-of-the-internet-my-thoughts-630975d88bea

[2] Andy Greenberg, "The Untold Story of NotPetya, the Most Devastating Cyberattack in History," Wired, August 2018,

www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/; see also Gavin Ashton, "Maersk, me &

NotPetya," gvnshtn.com/posts/maersk-me-notpetya/

Recover Activity | Chapter 14 | 409

15 Debrief Activity

The debrief activity marks the conclusion of the active incident and transitions the organization into post-

incident learning and improvement. After completing the response actions loop, the debrief activity

provides critical reflection on the incident and the response effort. The transition to debrief occurs when

organizational decision makers direct it, or when no further threats remain to address. This activity

transforms experience gained during the response effort into actionable improvements that strengthen

future incident response capabilities.

Figure 131 | Debrief Activity Waypoint

DEBRIEF OBJECTIVES

The debrief activity serves two primary objectives: incident closure, which formally concludes the active

response effort, and organizational learning, which transforms incident experience into lasting

improvement. While the response actions loop focused on operational urgency, the debrief shifts to

reflection and deliberate analysis. This transition requires a different mindset, moving from reactive

response to planned assessment.

Incident Closure

Formally ending the response effort requires more than stopping the response actions loop. Throughout the

response, the incident response team creates temporary assets (isolated systems, forensic images,

temporary accounts, and enhanced monitoring configurations) and accumulates documentation across

ticketing systems, chat channels, shared documents, and individual notes. The closure objective evaluates

each temporary asset for retention, modification, or decommissioning, consolidates dispersed

documentation into an authoritative incident record, and captures metrics that quantify the response

effort. This work preserves organizational memory, maintains regulatory compliance, supports potential

legal proceedings, and provides the baseline data that informs the after-action review and future response

improvements.

Organizational Learning

Transforming a single incident into lasting improvement requires deliberate analysis after the pressure of

active response has subsided. While root cause analysis began during eradication, the debrief provides an

opportunity for deeper reflection. This broader perspective accounts for each iteration of the response

actions loop. The analysis examines not only what the attacker did, but also the organizational shortcomings

that enabled the attack and the response gaps that complicated remediation. The learning objective

produces an after-action review, a finalized incident report, a stakeholder presentation, and an

improvement plan that converts observations into action items with assigned owners and accountability

mechanisms.

This chapter examines strategies for conducting effective debriefs, the challenges organizations commonly

face during this activity, and best practices for capturing insights from the incident to support

organizational improvement.

ATTACKERS KEEP IMPROVING: SO SHOULD WE

Threat actors continuously refine their tactics, techniques, and procedures based on what works

against their targets. Each successful campaign teaches them which tactics work, which defenses to

expect, which detection gaps to exploit, and which evasion techniques prove effective. Organizations

that fail to learn from incidents fall progressively further behind adversaries who treat every

operation as a learning opportunity.

The period immediately following an incident offers a unique window to drive security improvements.

Stakeholders who might otherwise resist security investments (including time, resources, and money)

become more receptive when confronted with tangible evidence of compromise. The incident

response team can leverage this heightened awareness to advocate for resources and changes that

would face resistance during normal operations.

“Never let a good crisis go to waste.

— Winston Churchill

Debrief Activity | Chapter 15 | 411

This principle applies directly to incident response. The debrief provides the mechanism to convert

crisis awareness into lasting organizational change before attention shifts to other priorities. Incident

response teams that capture this momentum can secure funding, staff, and policy changes that

strengthen the organization’s security posture for future threats.

DEBRIEF STRATEGIES

The debrief activity encompasses strategies for both incident closure and organizational learning. Closure

strategies come first: transitioning from active response, managing temporary assets, consolidating

documentation, and capturing incident metrics. Organizational learning strategies follow: conducting the

after-action review, driving organizational improvement, developing the incident report, and presenting

findings to stakeholders.

Transitioning to Debrief

Determining when to transition from active response to the debrief activity requires judgment from both

the incident response team and organizational decision makers. Two primary conditions signal readiness for

this transition: the response actions loop yields no new information about attacker presence or activity, or

organizational leadership determines that the incident is sufficiently resolved to conclude active response.

The first condition emerges organically from the response process. As iterations through scope, contain,

eradicate, and recover produce diminishing returns, with no new compromised systems discovered, no

additional persistence mechanisms identified, and no further compromise activity observed, the incident

response team can recommend transitioning to debrief. This recommendation should be based on

confidence that the threat has been eliminated and that the organization’s residual risk is minimal.

The second condition reflects organizational priorities that extend beyond technical considerations.

Leadership may determine that business operations have recovered sufficiently, that regulatory notification

requirements have been met, or that continued active response provides insufficient value relative to its

cost. This decision belongs to organizational decision makers, informed by the incident response team’s

assessment of residual risk.

Figure 132 | Transition Considerations for Debrief Activity

Managing Temporary Assets

Throughout the response effort, the incident response team creates temporary assets for investigation and

analysis. These assets may include isolated systems held for investigation, forensic images and memory

captures, temporary accounts created for response activities, and monitoring configurations deployed to

track attacker activity.

As part of the incident closure, the organization should determine whether each asset should be retained,

modified for permanent use, or decommissioned. An explicit decision prevents temporary response

measures from becoming permanent by default, where they add unmanaged storage, alert volume, and

attack surface to the environment.

Forensic Evidence Retention

During the investigation, the incident response team will collect forensic evidence, which can be storage-

intensive. Network captures, disk images, memory dumps, and log archives can consume significant storage

resources. Organizations should decide which artifacts to retain for future reference and which to delete.

During the debrief activity, the incident response team should review all forensic artifacts

and investigative assets to determine their retention status.

Legal counsel should advise on evidence retention requirements based on potential litigation, regulatory

obligations, and law enforcement involvement. Some jurisdictions and industries mandate specific retention

periods for security incident documentation. Organizations should establish evidence-retention policies

before incidents occur, and the debrief activity is the appropriate time to apply them to specific artifacts.

Debrief Activity | Chapter 15 | 413

Retention of forensic evidence can support future investigations, threat hunting, and incident response

training. Beyond the available documentation produced during the investigation, preserved artifacts can

provide valuable reference material for understanding attacker methods and improving detection

capabilities. For evidence that has been reviewed and analyzed, and which offers no further investigative

value or legal retention requirement, organizations should weigh the ongoing storage costs against

potential future utility before deciding to retain it.

Temporary Accounts and Monitoring

Temporary accounts and elevated access granted during response should be revoked unless they serve

ongoing operational needs and can be managed through standard access control processes. The retention

of temporary accounts increases the attack surface and may introduce additional risks to the organization.

The incident response team should use the incident documentation to identify all temporary accounts

created during the response. These accounts should be disabled or deleted unless there is a compelling

reason to retain them. The incident response team should update the incident documentation to reflect

when accounts are removed, and by whom.

In some cases, new accounts created during the incident response function may prove valuable for ongoing

operations. For example, it may be desirable to retain accounts established for isolating privileges as part of

a containment effort, or to separate privileges for admin access (e.g., jwright and jwright-admin). When

retaining such accounts, the organization should integrate them into standard access management

processes, including periodic review and revocation procedures.

Enhanced Monitoring Configurations

Temporary monitoring configurations deployed during response may provide ongoing value if they address

previously unmonitored attack vectors or improve visibility into critical systems. The incident response

team should evaluate these configurations during the debrief activity to determine if they should be

retained, modified for permanent use, or removed. The following factors can help guide this determination:

• Coverage gaps: Do the temporary monitoring configurations address visibility gaps identified during the

incident?

• Operational impact: Do the configurations impose performance overhead or generate excessive alerts

that negatively impact operations teams?

• Maintenance requirements : Can the organization sustain the monitoring configurations through

regular updates and maintenance?

• Integration with existing systems : Do the configurations align with the organization’s broader

monitoring and detection strategy?

If the decision is made to retain temporary monitoring configurations, the team should document the

rationale for retention, any modifications made for permanent use, and the individuals responsible for

ongoing maintenance.

Consolidating Incident Documentation

The debrief activity provides an opportunity to consolidate the response documentation accumulated

throughout the incident into a comprehensive incident record. This record captures the incident details and

represents a valuable resource for the organization’s institutional knowledge.

As described in Documentation during the verify and triage activities, the incident response team should

build documentation continuously throughout the response rather than defer it to debrief. By the time the

debrief begins, documentation exists in multiple locations: ticketing systems, chat channels, shared

documents, and individual notes. The incident response team consolidates this dispersed information into

an authoritative incident record.

The incident response team should start by validating the incident timeline. The timeline constructed

during active response may contain gaps, inconsistencies, or timestamps that require refinement based on

subsequent analysis. Walking through the timeline with important responders helps verify accuracy and fill

in missing details while memories remain fresh.

Figure 133 | Sample Incident Timeline in Excel

The team should document the important decisions made during the response, including the alternatives

considered and the rationale for the chosen approach. To balance time investment with value to the

organization, analysts should focus on capturing decisions that had significant impact on the incident

outcome, or were otherwise controversial or complex. Where possible, the team should capture information

about decisions that later proved suboptimal along with analysis of what information would have led to

better choices (e.g., the hindsight is 20/20  perspective for future learning). This decision record proves

valuable for future incidents, regulatory inquiries, and potential legal proceedings.

DOCUMENTATION AND VALUE PROPOSITION: REQUIREMENTS FOR THE

ORGANIZATION

Writing documentation consumes resources. The investment in time and effort should be justified by

the value it provides to the organization under the direction of organizational decision makers.

For routine incidents with limited scope, a ticket entry with pertinent notes may be sufficient

documentation for the organization. The ticket should capture the detection source, affected

Debrief Activity | Chapter 15 | 415

system(s), response actions taken, and confirmation of resolution. A brief summary reviewed and

approved by the incident lead adds collaborative value from a senior analyst without excessive

overhead on the team. Incidents like commodity malware infections, single-system compromises, or

incidents resolved through standard playbook procedures may fall into this category where the

investment of extensive documentation outweighs the benefits.

More serious incidents typically warrant more formal documentation. When incidents affect multiple

systems, involve data exposure, require executive decisions, or trigger regulatory breach notification

obligations, the organization benefits from more structured incident reports. These reports preserve

institutional knowledge, support compliance requirements, and provide reference material for future

incidents.

The decision point between lightweight and formal documentation should be defined before

incidents occur. Organizations can establish severity thresholds or incident categories that trigger

different documentation requirements. For example, any incident requiring external notification,

involving a compromised privileged account, or exceeding a defined scope threshold might

automatically require formal documentation. Clear criteria prevent ad hoc decisions during the post-

incident period when teams are fatigued and eager to return to normal operations.

Figure 134 | Documentation Detail Flowchart

Debrief Activity | Chapter 15 | 417

Some organizations default to minimal documentation and later regret missing details when similar

incidents recur or when auditors request evidence of response activities. Others over-invest in

documentation for minor incidents, consuming resources that could be better allocated elsewhere.

The goal is to find the appropriate balance for your organization’s risk profile, regulatory

environment, and operational capacity.

Capturing Incident Metrics

During the debrief activity, the incident response team should calculate and record incident metrics that

measure response effectiveness. These metrics provide baseline data for tracking organizational

improvement over time. As discussed in Getting Started , organizations should focus on internal

improvement rather than external benchmarking.

Important metrics to capture include:

• Mean Time to Detect (MTTD) : The elapsed time between when the incident began and when the

organization detected it. Calculating MTTD often requires determining the incident start time

retrospectively based on investigation evidence.

• Mean Time to Respond (MTTR) : The elapsed time from detection to incident resolution. Organizations

may track MTTR in stages, such as time to containment, time to eradication, and time to full recovery, if

those metrics are valuable for the organization or as directed by decision makers.

• Scope of Impact : The number of systems, users, and data assets affected by the incident. This metric

helps quantify incident severity and correlate response effort with incident scope.

• Resource Utilization : The personnel hours, external consulting costs, and tool expenses consumed

during response. This data supports future resource planning and helps justify security investments.

• Total Incident Lifecycle : The complete duration from initial compromise to verified resolution. This

metric combines MTTD and MTTR to show the full timeline of the attacker’s presence and the

organization’s response.

For example, consider the metrics from the Colonial Pipeline ransomware incident in 2021, as shown in

Table 35 . Summarizing the incident metrics provides a clear picture of the response effort and its

effectiveness. In addition, organizations may choose to record these metrics in a more formalized manner

(e.g., an incident-tracking database or a codified spreadsheet) to facilitate analysis across multiple incidents.

The Colonial Pipeline incident metrics are collected from public information or otherwise

presented as estimates where noted.

Table 35 | Colonial Pipeline Incident Metrics (2021)

METRIC VALUE NOTES

Mean Time to Detect (MTTD) 8 days Initial access April 29; ransomware detected May 7

Mean Time to Respond (MTTR) 8 days Detection May 7; operations restored May 15

Time to Containment <1 day Pipeline systems isolated same day as detection

(May 7)

METRIC VALUE NOTES

Time to Eradication ~2 days Persistence removed and attacker access revoked

by May 8 (estimated)

Time to Full Recovery 8 days May 7 detection to May 15 full restoration

Scope of Impact - Systems 5,500 miles of

pipeline

IT systems compromised; OT systems proactively

shut down

Scope of Impact - Data 100 GB

exfiltrated

Data staged and exfiltrated before ransomware

deployment

Scope of Impact - Business 45% of East

Coast fuel

supply

6-day operational shutdown

Resource Utilization - Ransom $4.4 million

paid

Approximately $2.3 million recovered by DOJ in

June 2021

Resource Utilization - External Mandiant

engaged

Incident response retainer activated May 7

Total Incident Lifecycle 16 days April 29 initial access to May 15 full restoration

Organizations should track these metrics consistently across incidents to identify trends and measure

improvement. A single incident’s metrics have limited value in isolation. Tracking data consistently across

multiple incidents reveals whether detection is improving, response actions are accelerating, and security

investments are producing measurable results.

Conducting the After-Action Review

The after-action review (AAR) brings together incident responders and stakeholders to examine the

response effort. This structured review examines what was supposed to happen, what actually happened,

why differences occurred, and what changes will improve future responses. The AAR should occur soon

enough after the incident that details remain fresh, but with enough distance to allow objective reflection.

The AAR facilitates honest discussion of what worked and what did not. The facilitator should create an

environment where participants feel invited to identify problems without fear of blame. The discussion

should focus on processes and systems rather than individual performance. The goal of the AAR is to

improve the incident response effort and overall security across the organization, not to assign fault for

shortcomings.

The incident response team should structure the AAR around six core questions:

• What was supposed to happen?  The team should review the incident response plan, playbooks, and

established procedures that should have guided the response. This question identifies which procedures

were followed and which were not.

• What actually happened? Responders should walk through the incident timeline, decisions, and actions.

The discussion should note deviations from planned procedures and their outcomes.

• Why did it happen?  The team should analyze the factors that caused deviations from expected

Debrief Activity | Chapter 15 | 419

procedures. This analysis distinguishes between plan failures (procedures that did not work as designed)

and execution failures (procedures that were not followed as designed).

• What can we do better next time?  The team should develop specific, actionable recommendations for

improving detection, response procedures, tools, training, and organizational coordination.

• What worked well? Participants should identify the successful aspects of the response to be retained or

expanded.

• Why did those aspects succeed?  The team should examine the underlying reasons, which may be

deliberate design, individual initiative, or fortunate circumstance. Understanding the cause allows the

organization to engineer the favorable conditions into future responses rather than relying on them

happening to recur.

The incident response team should document AAR findings and recommendations in a format that can drive

follow-up action. Each recommendation should have an assigned owner with expected completion dates.

The team should schedule follow-up reviews to verify that recommendations have been implemented.

VALUE IN DEVELOPING A VISUAL TIMELINE

A visual timeline of the incident can enhance the AAR by providing a clear, shared reference for

discussion. Visual learners in particular will benefit from seeing the sequence of events, decisions,

and actions laid out graphically.

Visual timelines can take various forms, from Gantt charts to complex flow diagrams that illustrate

parallel activities and decision points. Even a simple, high-level, linear overview of the events can

provide valuable context for the AAR discussion.

Figure 135 | Sample Timeline for Colonial Pipeline Incident

After an incident, when details are no longer fresh in memory, a well-constructed visual timeline

serves as a useful reference for subsequent learning and training.

Driving Organizational Improvement

The debrief activity’s ultimate value lies in translating lessons learned into organizational change.

Recommendations that remain documented but unimplemented are wasted effort. The incident response

team should work with decision makers to prioritize recommendations and secure the resources needed for

implementation.

Organizations can categorize recommendations by implementation timeline:

• Immediate actions address any outstanding vulnerabilities or gaps that pose ongoing risk. These

changes should be implemented before the debrief concludes, or as soon as is practical, given resource

constraints.

• Short-term improvements require planning and coordination but can be completed within weeks or a

few months. These typically include procedure updates, additional monitoring, and targeted training.

• Long-term strategic changes require significant investment in tools, architecture, or staffing. These

recommendations should be incorporated into security roadmaps and budget planning cycles.

Continuing the Colonial Pipeline example, the incident response team might present improvement

recommendations as shown in Table 36.

Table 36 | Example Recommendations by Timeline (Colonial Pipeline)

TIMELINE RECOMMENDATION RATIONALE

Immediate Actions

Within 3 days Audit and confirm all remote access

requires MFA

Single-factor VPN authentication

enabled the initial compromise

Within 3 days Deploy initial enhanced monitoring at

IT/OT network boundary

Proactive OT shutdown was necessary

due to uncertainty about lateral

movement

Short-term Improvements

Within 30 days Design and implement network

segmentation between IT and OT

environments

Lack of segmentation forced

precautionary OT shutdown during IT

incident

Within 60 days Deploy endpoint detection and

response (EDR) across all systems

Earlier detection could have reduced

attacker dwell time from 8 days

Within 60 days Establish privileged access

management program

Limit blast radius of compromised

credentials

Within 90 days Complete ransomware-specific

incident response playbook

Response decisions (ransom payment,

decryptor vs. backup restoration)

benefit from pre-planned guidance

Long-term Strategic Changes

6-12 months Implement zero trust architecture for

remote access

Eliminate implicit trust for VPN-

connected systems

Debrief Activity | Chapter 15 | 421

TIMELINE RECOMMENDATION RATIONALE

6-12 months Deploy immutable, air-gapped backup

infrastructure

Ensure recovery capability independent

of decryptor availability

12+ months Establish dedicated OT security

operations capability

Critical infrastructure requires

specialized monitoring and response

Ongoing Conduct quarterly tabletop exercises

including ransomware scenarios

Maintain response readiness and

validate playbook effectiveness

The incident response team should leverage the post-incident window to secure approval for improvements

that might face resistance under normal circumstances. Presenting recommendations in business terms

connects security investments to risk reduction. Wherever possible, the team should align security

recommendations with other opportunities to minimize costs or optimize procedures. Incident metrics and

impact assessments can quantify the cost of inadequate capabilities.

Organizations should incorporate lessons learned into organizational processes. The team should update

incident response plans and playbooks based on what worked and what did not. Detection rules and

monitoring configurations should be revised based on how the incident was discovered and what visibility

gaps existed. The team should develop training scenarios based on the incident to prepare responders for

similar future events.

Developing the Incident Report

The incident report represents the primary deliverable of the debrief activity. This document captures what

happened, how the organization responded, what impact resulted, and what changes will prevent similar

incidents. The format and depth of incident reports vary significantly across organizations, ranging from

comprehensive, formal documents to structured entries in incident-tracking systems. The appropriate level

of documentation depends on what is valuable to the organization.

The incident report serves multiple purposes beyond documenting the incident itself. It provides training

material for future responders, supports regulatory compliance obligations, establishes a record for

potential legal proceedings, and creates institutional knowledge that persists beyond individual team

members. Long after the incident is over, the incident report remains a reference for the organization to

use in shaping future security strategies.

Report Audience

Different stakeholders require different levels of detail and different perspectives for the same incident.

Understanding the audience for incident documentation helps ensure that reports communicate effectively

and drive appropriate action.

Understanding the report audience is critical to tailoring content and format appropriately.

By focusing on what the audience needs to know rather than what the incident response

team wants to document, the incident report becomes a more effective communication

tool.

• Executive Leadership needs high-level summaries focused on business impact, risk exposure, and

resource requirements. These reports are often high-level with minimal technical detail.

• Technical Teams require detailed technical documentation of attacker methods, affected systems, and

remediation steps. IT and security staff responsible for implementing improvements need specific

guidance on what to change and why.

• Legal and Compliance stakeholders need documentation that supports regulatory obligations and

potential litigation. These reports emphasize evidence preservation, chain of custody, and adherence to

legal standards.

• External Partners, such as customers, regulators, or industry-sharing groups, may receive sanitized

versions of incident reports. These documents focus on transparency while protecting sensitive

organizational information.

The report length varies based on audience needs. Few stakeholders will read a 150-page document in its

entirety. To best meet the needs of the audience, organizations should consider the benefits of multiple

report formats and structures tailored to different stakeholders.

Report Contents

Regardless of format, effective incident reports share common characteristics. They present information as

objectively as possible, differentiating facts from analyst interpretation and inference. They maintain

credibility by acknowledging uncertainty and documenting confidence and the reasoning behind

conclusions. They provide actionable recommendations rather than just describing what happened.

Before developing a report, the team should establish the intended purpose and constraints:

• Primary audience: Who will read this report, and what decisions will it inform?

• Distribution scope: Is this report strictly internal, or will it be shared with external parties?

• Evidentiary requirements: Does this report need to meet forensic standards for potential legal

proceedings, or is it primarily an operational document?

• Compliance obligations: Do regulatory frameworks such as HIPAA, PCI DSS, or GDPR impose specific

documentation requirements? Does the organization need to consider legal requirements like breach

notification laws in the context of the report content?

• Format preferences: Does the organization prefer a single comprehensive document or separate reports

for different audiences?

The answers to these questions shape both content and delivery format. For example, a report intended for

regulatory submission differs substantially from an internal lessons-learned document.

Table 37 | Sample Report Contents: Purpose Considerations

Primary Audience Internal leadership and security teams

Distribution Internal, tightly controlled distribution

Evidentiary

Requirements

Moderate; focus on operational accuracy rather than forensic standards

Compliance

Obligations

Supporting document for HIPAA breach notification requirements

Format Preferences Two separate reports: executive summary and technical details

Debrief Activity | Chapter 15 | 423

Two-Report Approach

A single incident report rarely serves all audiences effectively. Common challenges with a unified report

include:

• Executives skip technical sections that dominate the document.

• Technical teams distrust sanitized summaries that omit important details.

• Legal teams may excerpt content out of context, losing its surrounding technical nuance.

Incident response teams that try to satisfy all audiences in a single document often spend too much time

rewriting the same content for different readers, producing a report that fails to meet anyone’s needs.

Instead of a one-size-fits-all report, the DAIR model advocates for a two-report approach. By separating

technical details from a broader focus on business impact and organizational response, each report can be

tailored to its audience. There’s no guarantee that every stakeholder will be satisfied, but this approach

maximizes the likelihood that each group receives the information they need in a format they can use.

A two-report approach offers a practical compromise to the dilemma of wasted time in developing a single

unified report: an incident summary report for leadership and other stakeholders, and a technical incident

response report for security teams and detailed documentation needs. This separation allows each report

to serve its intended audience better than a single document could.

Incident Summary Report

The incident summary report communicates essential information to leadership and business stakeholders

in a concise format. This report should be short enough that busy executives will actually read it, typically

one to two pages plus any required attachments.

The summary report typically includes:

• Report metadata , including incident identifier, report version, date issued, author, and data

classification.

• Executive overview with incident type, detection date, a brief description of what occurred, business

impact summary, important findings, and specific requests for leadership action.

• Business impact assessment  covering operational disruption, data exposure, and financial or

reputational consequences.

• Response actions summary  highlighting important containment, eradication, and recovery steps at a

high level.

• Incident metrics , including detection time, containment time, and total resolution time, with

comparison to organizational baselines.

• Risk and control assessment  summarizing root cause in non-technical terms, identifying gaps in

organizational security controls that led to the incident, and characterizing residual risk to the

organization.

• Recommendations and resource requirements to address the factors that contributed to the incident.

• Decisions required explicitly stating what leadership needs to approve, fund, or decide.

While an internal incident summary report for the Colonial Pipeline incident is not publicly available, a

sample format is shown in Figure 136 to illustrate the typical structure and content.

Figure 136 | Incident Summary Report Sample

The summary report should conclude with a reference to the technical report for readers requiring

additional detail.

Debrief Activity | Chapter 15 | 425

EXECUTIVE REPORTING LEVERS

Figure 137 | Collection of Levers (photo credit happyphoton)

My friend John Strand taught me to frame recommendations as a collection of levers: broad controls

that decision makers can evaluate, prioritize, and act on after an incident. Each lever should give

decision makers enough context to make an informed decision without requiring them to read the

technical report. Present recommendations with a consistent framework that covers the dimensions

decision makers care about:

• Opportunity: What gap or weakness does this address, and why does it matter now?

• Benefit: What risk reduction or capability improvement does the organization gain?

• Cost: What is the estimated investment in tools, licensing, or services?

• Time: How long will implementation take, and are there quick wins along the way?

• Resources: What staffing or expertise is required, and does the organization have it today?

• Compliance: Does this address a regulatory requirement or support audit readiness?

• Protections: What specific threats or attack techniques does this control mitigate?

For example, one lever might be titled "Limit attacker movement between business functions." The

opportunity section would explain that during this incident, a single compromised account was able

to reach financial systems, customer databases, and backup infrastructure without restriction. The

benefit of pulling this lever: future incidents would be contained to the affected area, reducing the

volume of sensitive data exposed and protecting critical operations from cascading disruptions.

Table 38 | Sample Executive Lever: Limit Attacker Movement Between Business Functions

DIMENSION DETAIL

Opportunity During this incident, a single compromised account accessed financial

systems, customer databases, and backup infrastructure without restriction.

DIMENSION DETAIL

Benefit Future incidents contained to the affected area, reducing data exposure and

protecting critical operations from cascading disruptions.

Cost Estimated $180,000 in infrastructure investment with ongoing maintenance

absorbed by existing staff.

Time Phased rollout over 6 months, with the highest-risk boundaries in place within

60 days.

Resources Implementation managed by the infrastructure team with support from an

external integrator during the initial phase.

Compliance Addresses PCI DSS network segmentation requirements and supports HIPAA

access control obligations.

Protections Directly mitigates the lateral movement technique used in this incident and

reduces the blast radius of future compromises.

Each lever should be supported by a detailed technical analysis in the accompanying technical

incident response report, giving decision makers confidence that the recommendation is well-

grounded and achievable. This structure transforms the recommendations section from a wish list

into a decision framework, providing decision makers with clear options they can evaluate, prioritize,

and fund.

Technical Incident Response Report

The technical report provides comprehensive documentation of the incident for security teams and forensic

analysts, and serves as the detailed record of the response. This document is often longer, depending on

incident complexity and organizational documentation standards.

The technical report typically includes:

• Report metadata with version control and distribution restrictions.

• Scope and methodology documenting what was investigated and what constraints applied.

• Environment overview describing affected systems, network architecture, identity infrastructure, and

logging coverage.

• Detection and triage documenting how the incident was discovered and initial response actions.

• Incident timeline presenting both attacker activity and response actions in chronological sequence.

• Attack analysis  organized by attack phase: initial access, execution, persistence, privilege escalation,

lateral movement, command and control, collection, exfiltration, and impact.

• Affected assets and identities cataloging compromised hosts, accounts, services, and cloud resources.

• Vulnerabilities and control failures, documenting what weaknesses the attacker exploited.

• Indicators of compromise organized by confidence level with detection guidance.

• Response actions detailing scope, containment, eradication, and recovery steps with validation results.

• Root cause analysis examining the contributing causes that led to the incident.

• Conclusions summarizing findings with confidence assessment and acknowledged unknowns.

• Appendices containing detailed artifacts, including query listings, tool output, forensic tables, complete

Debrief Activity | Chapter 15 | 427

indicator lists, and supporting evidence.

While an internal technical report on the Colonial Pipeline incident is not publicly available, Figure 138

illustrates the typical structure and content.

Figure 138 | Incident Detail Report Sample

REPORTING THAT MATCHES THE ORGANIZATION’S NEEDS

The appropriate level of incident reporting varies significantly across organizations. In the DAIR

model, we advocate for a two-report approach that separates executive summaries from technical

details. This structure allows each report to be tailored to its audience, maximizing the likelihood that

stakeholders receive the information they need in a usable format. However, this won’t always be the

best approach for every organization.

In my work as a consultant, I’ve written and contributed to over a thousand customer reports. I’ve

written reports that exceed 500 pages, full of technical detail and comprehensive analysis. I’ve also

written attestation reports that are little more than a few sentences that say, essentially, "we

performed an investigation" with no further detail. The appropriate level of reporting depends on the

organization’s needs, cybersecurity maturity, regulatory environment, and risk profile.

Determining the right reporting approach requires understanding what the organization values and

where the shortcomings lie in achieving the report’s intended goals. Try to avoid a rigid adherence to

a particular format or structure simply because "that’s how it’s always been done." Instead, focus on

delivering value to the organization through effective communication. Always ask stakeholders and

executives what they need from the report, and adapt your reporting approach accordingly.

USING A STRUCTURED TEMPLATE FOR TECHNICAL REPORTS

Organizations developing technical incident reports can benefit from starting with an established

framework rather than creating documentation structures from scratch.  My friend and SANS

Institute Fellow Lenny Zeltser (with support from Elisabetta Tiani and Daniel Trauner) developed a

comprehensive incident report template that organizes information around five essential questions:

what happened and when, what was the root cause, what was and remains to be done, what lessons

can be learned, and what are the remaining action items to be addressed.

Figure 139 | Cybersecurity and Privacy Incident Report Template

The template addresses a common challenge in incident response: ensuring that report authors

systematically capture all critical details. By structuring documentation as a series of guided

questions, the template helps incident coordinators gather comprehensive information from team

members handling various response tasks. The framework also bridges the gap between technical

detail and business communication, presenting findings in formats that meet stakeholder

expectations across different audiences.

The template is available in both Microsoft Word and Markdown formats under a Creative Commons

Attribution license, allowing organizations to customize it to align with their specific documentation

requirements while maintaining a consistent baseline structure. The question-based approach makes

Debrief Activity | Chapter 15 | 429

it particularly valuable for teams that conduct formal debriefs on significant incidents, as it naturally

aligns with the AAR process of examining what happened, why, and what should improve.

The template is available at zeltser.com/incident-response-report-template.

Presenting Findings and Recommendations

The written incident report serves as a permanent record, but a presentation to stakeholders provides an

opportunity for direct engagement and alignment on next steps. The presentation serves as a formal close-

out of the incident, ensuring that decision makers understand what happened, what the organization

learned, and what actions are needed going forward.

The incident response team should schedule the presentation session promptly after consolidating the

incident documentation, typically within one to two weeks of concluding active response. The session

should last approximately one hour, though more complex incidents may require additional time. Longer

sessions risk losing executive attention (or the inability to get important stakeholders to attend) and may

dilute the important messages.

Some organizations treat the presentation itself as the primary incident report rather than a companion

artifact. In that model, intentionally dense slides carry the substantive findings, recommendations, and

supporting detail, with the written report either omitted or reduced to a short cover memo. The session

structure described in this section applies whether the presentation supplements a written report or stands

as the primary deliverable.

Figure 140 | Incident Presentation Example

Session Objectives

The presentation session serves several distinct purposes:

• Shared understanding : All stakeholders should have a consistent view of what happened during the

incident and how the organization responded.

• Findings review: The presenter should communicate important findings from the investigation in terms

accessible to non-technical stakeholders.

• Recommendations alignment : The team should review proposed improvements and secure

commitment for implementation.

• Formal closure: The session marks the official transition from incident response to normal operations

with clear accountability for follow-up actions.

The session is not an opportunity to re-litigate decisions made during active response, to assign blame for

the incident or response shortcomings, or to debate technical details that belong in separate working

sessions. The facilitator should establish these ground rules at the start of the meeting and redirect

discussions that stray into unproductive territory.

Attendees and Roles

The incident response team should invite stakeholders who need to understand the incident and who have

the authority to approve recommended improvements. Typical attendees include:

• Executive sponsor: Senior leader with authority to approve resources and policy changes.

• Incident response lead: Primary presenter who can speak to technical findings and response actions.

• Business stakeholders: Representatives from affected business units.

• IT leadership: CIO, CISO, or delegates responsible for implementing technical recommendations.

• Legal and compliance: Counsel who can address regulatory implications.

• Communications: If external messaging occurred or may be required.

The team should designate a facilitator to manage the session flow and a note-taker to capture decisions

and action items. The facilitator role may be separate from the presenter, allowing the incident response

lead to focus on content delivery.

Follow-Up and Accountability

The presentation session should conclude with documented outcomes:

• Decisions made during the session.

• Recommendations approved, modified, or deferred.

• Action items with assigned owners and due dates.

• Schedule for follow-up review to verify implementation progress.

The incident response team should distribute a brief summary of decisions and action items to all attendees

within twenty-four to forty-eight hours. This summary serves as the official record of commitments made

during the session and provides accountability for follow-through.

The team should schedule a follow-up review, typically thirty to ninety days after the presentation, to assess

implementation progress on approved recommendations. This review maintains organizational attention on

improvements and provides an opportunity to address obstacles that have emerged since the initial session.

Debrief Activity | Chapter 15 | 431

DEBRIEF CHALLENGES

The debrief activity faces obstacles that can undermine its effectiveness if not addressed proactively. These

challenges arise from organizational dynamics, resource constraints, and the nature of post-incident

reflection. Understanding these challenges helps incident response teams anticipate difficulties and develop

strategies to overcome them.

In this section, we’ll examine five challenges that commonly undermine debrief effectiveness:

documentation gaps that emerge during high-pressure response, organizational attention that wanes once

the crisis subsides, blame dynamics that discourage honest discussion, legal and regulatory constraints that

shape what gets recorded, and resource constraints that compete with the return to normal operations.

Incomplete Documentation

An effective debrief depends on accurate, comprehensive documentation from the response effort. When

documentation is incomplete, analysts struggle to reconstruct what happened, when decisions were made,

and why particular approaches were chosen. This gap compromises both the incident report’s accuracy and

the organization’s ability to learn from the experience.

Documentation gaps typically emerge during high-pressure response activities when analysts prioritize

immediate actions over record-keeping. Responders focused on containing an active threat may skip or

defer documentation steps for later completion. When too much time passes between action and

documentation, details are forgotten or misremembered.

Mitigating documentation gaps requires establishing clear expectations before incidents occur.

Organizations should assign documentation responsibility to each team member, making it part of their role

during response. Standardized documentation practices, including templates and checklists, help ensure

consistent capture of essential information. The incident response team should periodically review

documentation completeness during the response rather than waiting for the debrief to discover gaps.

IF YOU’RE GOING TOO FAST...

Stephen Northcutt, the first president of the SANS Institute and my mentor for many years, told me a

story once about his time as a Navy medic.

Shortly after completing his training and starting work on a Navy base, Stephen got a call to provide

medical aid to a fellow sailor. He grabbed his med bag and started running.

Along the way, Stephen passed a senior medic who was walking calmly toward the same incident.

"You’re going too fast!" the senior medic called out as Stephen ran by.

Stephen looked back but kept running. Then he stumbled, fell, and ended up injuring himself.

As the senior medic caught up to him, he simply said, "I told you," and kept walking.

Stephen finished the story with this lesson:

“If you’re going too fast to write it down, you’re going too fast.

Stephen tells this story in a much funnier way than I can express in writing, but I never forgot the

lesson: if you’re going too fast, you’re going to make mistakes, you will miss important details, and you

may end up causing more harm than good.

Not every incident will require the same level of documentation, nor does every detail need to be

recorded, but taking the time to capture the documentation that is important to the organization is

essential to an effective incident response process.

Organizational Attention and Priority

The debrief competes for attention with other organizational priorities. Once the immediate crisis passes,

stakeholders often shift focus to the accumulated work that was deferred during the response. Executive

attention moves to other business concerns, and the urgency that drove rapid response dissipates.

This attention shift creates several challenges:

• Scheduling difficulties  as important participants struggle to find time for AAR meetings and report

review.

• Declining engagement as the incident recedes from immediate concern.

• Resistance to recommendations that require budget, staffing, or organizational changes.

• Incomplete follow-through on improvement actions that lack sustained attention.

The window for organizational attention is limited. Incident response teams should initiate the debrief

activity promptly while the incident remains fresh in stakeholders' and decision makers' minds. Conducting

the after-action review within days rather than weeks helps preserve memory accuracy and stakeholder

engagement.

Wherever possible, the incident response team should present recommendations in terms that resonate

with leadership priorities. Connecting security improvements to business risk reduction, regulatory

compliance, and competitive positioning helps secure buy-in. The team can quantify the cost of the incident

and the potential cost of similar future incidents to justify investment in preventive measures.

THE CONSULTANT’S SUPERPOWER

As a cybersecurity consultant, I have a superpower: executives listen to my advice. It’s not because

I’m smarter than the people doing the day-to-day security work inside an organization. It’s because

I’m the outside expert, and outside experts carry a gravitas that internal voices often don’t. I’ve seen

security teams repeatedly present a recommendation for months without traction, only to see it

approved within a week when I echoed it during an engagement.

I take that superpower seriously, and I use it to lift up the internal team. The people who do the work

every day deserve the credit, and they’re the ones who have to implement and maintain whatever

comes out of these conversations long after I’ve moved on to the next engagement.

That consultant superpower is amplified in the weeks following a major incident. There’s a window of

roughly thirty to forty-five days after a significant security event when decision-maker attention is at

its highest. Executives are engaged, boards are asking questions, and budget conversations that were

stalled for months are gaining momentum.

The window doesn’t last forever. By day 45, the crisis has faded from executive memory, competing

Debrief Activity | Chapter 15 | 433

priorities reassert themselves, and the organizational will to invest in security improvements begins

to evaporate.

You don’t have to be an outside consultant to leverage this window. Internal incident response teams

have the same opportunity, but only with the right preparation and approach.

The time to build your prioritized list of security improvements is during the response itself, not

after. When the executive sponsor asks "What do we need to prevent this from happening again?" the

answer should be prepared in advance, supported by evidence from the incident, and framed in terms

that connect to business risk and outcomes that executives care about.

Blame and Accountability Dynamics

Post-incident review can devolve into blame assignment rather than process improvement. When

individuals feel defensive about their actions during a response, honest discussion of what went wrong

becomes difficult. Organizations that punish mistakes create environments where problems are hidden

rather than examined.

A blameless postmortem culture encourages open discussion and learning from incidents.

The instinct to identify who caused the problem is natural but counterproductive. Security incidents rarely

result from a single failure by an individual actor. More often, incidents emerge from systemic weaknesses:

inadequate controls, unclear procedures, resource constraints, and organizational pressures that create

conditions for compromise.

Effective debriefs focus on processes and systems rather than individual performance. The discussion

should ask what failed rather than who failed. Participants should examine the conditions that made errors

possible rather than focusing on the people who made them. This approach facilitates honest and open

examination of problems, leading to greater opportunities for learning and improvement.

When individual performance issues do require attention, organizations should address them separately

from the debrief process. The debrief should remain focused on organizational learning rather than

performance management. Conflating these functions undermines the debrief’s effectiveness and

discourages future participation.

Legal and Regulatory Constraints

Documentation created during debrief may become relevant in litigation, regulatory proceedings, or

criminal investigations. This reality creates tension between thorough documentation and legal exposure.

Organizations should balance the learning benefits of comprehensive incident records against the risks of

creating discoverable content that could be used against them.

Legal counsel should advise on documentation practices that protect the organization while supporting

legitimate learning objectives. Some organizations use attorney-client privilege structures for sensitive

incident analysis, though the scope and durability of such protections vary by jurisdiction.

Regulatory obligations may impose specific documentation requirements that can constrain the content of

debriefs. Industries subject to HIPAA, PCI DSS, SEC regulations, or GDPR need to comply with specific

documentation requirements. Compliance teams should identify applicable requirements before finalizing

incident reports.

External sharing introduces additional constraints. Information shared with customers, regulators, or

industry groups may need to be sanitized to protect sensitive details. Coordination with legal and

communications teams helps ensure that external disclosures meet organizational and regulatory

requirements.

The potential for legal scrutiny should not paralyze the debrief process. Organizations that never document

incidents deprive themselves of learning opportunities, which can lead to even greater regulatory exposure

than organizations with robust documentation practices. The goal for organizations is to achieve informed

documentation that serves organizational needs while managing legal risk acceptance requirements.

Resource Constraints

Comprehensive debrief activities require time and attention from personnel who are often needed

elsewhere. After an extended incident response effort, team members may be exhausted and facing

backlogs of deferred work. Organizations that staff incident response from existing teams rather than

dedicated resources face particular pressure to return to normal operations.

Addressing resource constraints requires organizational commitment to the debrief as an essential

response activity rather than an optional add-on. Organizations should budget time and resources for post-

incident activities just as they budget for active response. Phased debrief approaches can capture essential

information immediately while deferring deeper analysis to when resources allow, guided by the

organization’s risk tolerance and response objectives.

For significant incidents, organizations should consider engaging external support for debrief activities.

Third-party facilitators can conduct interviews, consolidate findings, and develop reports while internal

teams return to normal operations. External perspectives may also identify issues that internal participants

overlook due to familiarity or organizational gaps.

DEBRIEF ACTIVITY EXAMPLES

The following cases illustrate how the debrief activity functions as an important part of the incident

response process.

The Compromised SaaS Account

A few days after a SaaS account compromise at Vanguard Point Advisors, Lisa Park, the security operations

manager, scheduled a quick stand-up debrief session with the response team. The incident had been

contained within fifteen minutes of an impossible-travel alert, with the attacker viewing two prospect

dashboards on the marketing analytics platform before the session was terminated. No data was exported

and no configuration changes were made. The question facing Lisa was not whether to conduct a debrief,

but how much formality the incident warranted.

Lisa reviewed the incident ticket that Marcus Chen, the security analyst, maintained throughout the

response. The ticket contained timestamps for each response action, an excerpt of the suspicious login and

access events from the marketing analytics platform’s audit log, documentation of the session termination

and password reset, and notes from the follow-up review. Marcus’s interview with the account owner,

Robert Dackinson, revealed the likely access vector: an attacker used credentials leaked in a third-party

breach to log into Dackinson’s account on the marketing analytics platform. Fortunately, the platform’s

audit log recorded only two prospect-dashboard views before Marcus terminated the session.

Debrief Activity | Chapter 15 | 435

For an incident of this scope, Lisa determined that a full incident report would provide minimal additional

value beyond what the ticket already contained. The organization’s incident documentation policy

established thresholds for formal reporting: incidents requiring external notification, involving privileged

account compromise, affecting multiple systems, or exceeding four hours of active response triggered

formal documentation requirements. This incident did not meet any of those criteria.

Lisa scheduled a thirty-minute debrief with Marcus, the IT manager, and Ellen Jasinski, Vanguard Point’s

cybersecurity director. The session followed a streamlined AAR format focused on four questions: What

happened? What worked well? Why did it work well? What should we improve?

The discussion identified several positive aspects of the response. Marcus recognized the impossible-travel

alert quickly, used the IT directory’s current contact information to reach Robert by phone within minutes,

and confirmed that he had not traveled abroad. The session termination and password reset on the

marketing analytics platform completed in under five minutes once the compromise was confirmed. The

total time from initial alert to verified containment was under fifteen minutes.

The team also identified improvement opportunities, including one that took the team by surprise. During

the response, Marcus discovered that the marketing analytics platform was not federated through Okta

SSO, contrary to the team’s assumption that Okta enforced MFA across all SaaS applications. The platform

had been onboarded directly by the marketing team three years earlier with username and password

authentication, and a planned federation effort had been deferred and forgotten.

This gap explained why the attacker’s stolen credentials succeeded without triggering an MFA challenge,

and raised a broader question: which other shadow cloud SaaS platforms had been onboarded? The team

also lacked a process for monitoring known breach dumps for exposed corporate credentials, and user

awareness training had not addressed credential-reuse risks across personal and corporate accounts.

Lisa captured these findings in the incident ticket rather than creating a separate document. She added a

Debrief Summary section that included the important findings, the three identified improvement actions,

and the names of the team members who participated in the review. The cybersecurity director reviewed

the ticket, added her approval notation, and the incident was formally closed.

Table 39 | Incident Ticket Debrief Summary (Vanguard Point Advisors)

INCIDENT ID SEC-2026-0892

Debrief

Date

April 15, 2026

Participant

s

Lisa Park (Security Ops Manager), Marcus Chen (Security Analyst), David Morrison (IT

Manager), Ellen Jasinski (Cybersecurity Director)

Incident

Summary

Successful login to marketing analytics SaaS platform via credentials leaked in a third-

party breach. Attacker viewed two prospect dashboards before session terminated. No

data exported and no configuration changes made. Contained within 15 minutes.

What

Worked

Well

Rapid recognition of impossible-travel alert, ready access to current employee contact

information, prompt verification with affected user, fast session termination and

credential rotation, clear playbook guidance

INCIDENT ID SEC-2026-0892

Improveme

nt Actions

1. Audit SSO/MFA coverage across all SaaS platforms to identify those onboarded

outside Okta (Owner: IT Security, Due: May 15)

2. Federate the marketing analytics platform through Okta with MFA enforcement

(Owner: IT, Due: May 22)

3. Update user awareness training to address credential-reuse risks across personal

and corporate accounts (Owner: Security Awareness, Due: Apr 22)

Incident

Lead

Approval

Marcus Chen, April 15, 2026

Manageme

nt Approval

Ellen Jasinski, April 15, 2026

This lightweight approach preserved the essential details without consuming resources on formal

documentation. The improvement actions were tracked in the organization’s security project management

system alongside other security initiatives. Lisa scheduled a 30-day follow-up to verify that the actions had

been completed.

The Healthcare Ransomware Recovery

Three weeks after Sarah Pesce, Lakewood Medical Center’s senior incident response analyst, completed the

phased domain controller recovery, the organization faced a comprehensive debrief spanning multiple

teams, significant business impact, and regulatory notification obligations. The ransomware encrypted 847

systems across three clinic locations, forced a six-day return to paper-based patient care, and exposed gaps

in backup practices that delayed recovery by weeks.

Dr. Patricia Davis, Lakewood’s Chief Information Security Officer, recognized that this debrief required

careful planning. The incident had consumed the IT and security teams for nearly a month. The staff was

exhausted, facing backlogs of deferred work, and ready to return to normal operations. At the same time,

the organization faced a narrow window of opportunity to capture lessons from the incident while details

remained fresh and stakeholder attention remained focused on security.

Dr. Davis structured the debrief into three phases: immediate documentation capture, a formal after-action

review, and an executive presentation with recommendations.

Phase 1: Documentation Consolidation

The first phase began while recovery operations were still concluding. Dr. Davis assigned two analysts to

consolidate the documentation that responders had been maintaining throughout the incident, drawing

from the ticketing system, the incident Slack channel, shared documents, email threads, and individual

responder notes. The goal was to assemble a unified incident record while team members remained

available to reconcile ambiguities and fill gaps in their notes.

Sarah Pesce contributed her detailed notes from the domain controller recovery, including the discovery

that backups were twenty-one days old and the decision to rebuild workstations from gold images rather

than restore from backup. Network team members provided firewall change logs and VPN access records.

The IT support desk supplied the timeline of user reports during the initial encryption wave.

Debrief Activity | Chapter 15 | 437

The documentation team constructed a comprehensive timeline spanning from the initial VPN compromise

to the final system restoration. They identified gaps where actions had been taken but not recorded,

reaching out to responders for clarification while details remained accessible.

Table 40 | Lakewood Medical Center Incident Timeline Summary

DATE PHASE KEY EVENTS

Nov. 15 Initial Access Attacker authenticates via VPN using

compromised service account credentials

Nov. 15-28 Reconnaissance & Staging Attacker maps network, identifies domain

controllers, stages ransomware payload

(undetected)

Nov. 29, 2:47

AM

Ransomware Deployment Encryption begins across multiple systems

Nov. 29, 3:12

AM

Detection Security team detects mass encryption activity via

EDR alerts; initiates incident response

Nov. 29, 3:30

AM

Verification and Triage Chen confirms ransomware activity; alerts on-call

response team

Nov. 29, 3:45

AM

Containment VPN disabled, affected network segments isolated,

compromised accounts disabled

Nov. 29 -

Dec. 1

Scoping & Eradication Full scope determined; persistence mechanisms

identified and removed; credentials rotated

Dec. 2 - Dec.

Recovery Phase 1 Domain controllers restored from Nov. 8 backup;

core infrastructure validated

Dec. 9 - Dec.

Recovery Phase 2 Member servers restored; clinical applications

brought online

Dec. 16 - Dec.

Recovery Phase 3 Workstations rebuilt from gold images; user data

restored from network backups

Dec. 21 Incident Closure All systems operational; enhanced monitoring in

place; debrief initiated

Phase 2: After-Action Review

Dr. Davis scheduled the formal AAR for the week following closure of the incident. She invited

representatives from each team involved in the response: security operations, network infrastructure,

server administration, the help desk, clinical informatics, and the privacy office. She also invited Dr. Michael

Torres, the Chief Medical Officer, to represent clinical operations disrupted during the paper-based care

period.

The AAR opened with a timeline walkthrough led by Sarah Pesce. Sarah presented the incident progression

using a visual timeline displayed on the conference room screen, pausing at important decision points to

allow team members to add context or corrections. This collaborative review surfaced details that no single

responder had captured: the network team’s late-night firewall changes, the help desk’s triage of hundreds

of user calls, and the clinical staff’s workarounds for accessing patient records during system downtime.

Figure 141 | Lakewood Medical Center Incident Timeline

Dr. Davis structured the discussion around the five core AAR questions, taking care to maintain focus on

processes and systems rather than individual performance.

What was supposed to happen?

The organization’s incident response plan called for detection within hours, containment within the same

business day, and recovery within seventy-two hours for critical systems. Backup policy required daily

backups with weekly off-site replication and monthly restoration testing.

What actually happened?

Detection occurred fourteen days after initial access, only when the ransomware began encrypting systems.

Containment was achieved within one hour of detection. Recovery required twenty-two days due to backup

age and scope of compromise. The most recent viable backup was twenty-one days old because the backup

system had been silently failing for three weeks prior to the incident.

Why did the gaps occur?

The discussion revealed a cascade of contributing factors. The VPN lacked multi-factor authentication,

allowing the attacker to authenticate with stolen credentials alone. Security monitoring focused on

endpoint alerts rather than authentication anomalies, missing the initial VPN access and subsequent lateral

movement. Backup monitoring had been configured to alert on failures, but the backup jobs were

completing "successfully" with zero files backed up due to a misconfigured storage path. No one had

performed a test restoration in over eight months.

What should improve?

Team members contributed dozens of potential improvements. Dr. Davis captured each suggestion, then

led a prioritization discussion to identify the most impactful changes.

Throughout the AAR, Dr. Davis watched for blame dynamics. When one participant suggested that

"someone should have noticed" the backup failures, she redirected the conversation: "Let’s focus on what

process changes would have surfaced this issue automatically. If we needed someone to manually notice the

problem, our monitoring wasn’t designed correctly." This reframing kept the discussion productive and

encouraged continued participation from team members who might otherwise have become defensive.

Debrief Activity | Chapter 15 | 439

Phase 3: Documentation and Presentation

Following the AAR, Dr. Davis developed two reports: an executive summary for leadership and the board,

and a detailed technical report for the security and IT teams.

The executive summary focused on business impact, risk exposure, and resource requirements. Dr. Davis

kept it to three pages, knowing that longer documents would go unread by busy executives. She led with

important metrics, summarized the attack chain in non-technical terms, and concluded with prioritized

recommendations tied to specific budget requests.

Table 41 | Lakewood Medical Center Executive Summary Metrics

METRIC VALUE CONTEXT

Time to Detect 14 days Attacker present from Nov. 15; detected Nov. 29

Time to Contain 58 minutes From detection to network isolation

Time to Recover 22 days Nov. 29 detection to Dec. 21 full restoration

Systems Affected 847 Servers, workstations, and clinical systems

Clinical System Impact 6 days EHR

downtime

Paper-based operations Nov. 29 - Dec. 4

Data at Risk 143,000

patient

records

PHI potentially accessible during attacker dwell

time

Direct Costs $2.1M

(estimated)

IR consulting, overtime, hardware replacement,

regulatory notification

Recovery Source 21-day-old

backup

Backup system failure undetected for 3 weeks

prior to incident

The technical report provided comprehensive documentation for the security team and served as the

authoritative incident record. This forty-seven-page document included the complete timeline, an

inventory of affected systems, indicators of compromise, response actions with timestamps, root cause

analysis, and the full recommendation set with implementation guidance.

Dr. Davis presented findings to the executive leadership team two weeks after the AAR. She structured the

one-hour session around three themes: what happened, what it cost, and what the organization needed to

do differently. She reserved half the session for discussion, knowing that executive engagement with the

recommendations was essential for securing implementation resources.

The presentation concluded with a prioritized recommendation roadmap, as shown in Table 42.

Table 42 | Lakewood Medical Center Recommendation Roadmap

TIMELINE RECOMMENDATION RATIONALE INVESTMENT

Immediate (Within 30 Days)

TIMELINE RECOMMENDATION RATIONALE INVESTMENT

Week 1-2 Implement MFA on all remote

access (VPN, RDP, cloud admin)

Single-factor VPN

authentication enabled initial

compromise

$45K

(licensing)

Week 2-4 Remediate backup system;

validate all backup jobs with test

restores

21-day backup gap extended

recovery by weeks

$25K

(consulting)

Week 3-4 Deploy authentication

monitoring with anomaly

detection

14-day dwell time went

undetected due to focus on

endpoint alerts only

Existing SIEM,

process

improvements

Short-Term (30-90 Days)

Month 2 Implement immutable backup

infrastructure with air-gapped

copy

Current backups vulnerable to

encryption by ransomware with

admin access

$180K

(infrastructure

)

Month 2-3 Deploy EDR to remaining

endpoints

Inconsistent EDR deployment

limited visibility during scoping

$65K

(licensing)

Month 3 Establish monthly backup

restoration testing with

documented validation

Backup failures went

undetected because no one

tested restores

Staff time

Long-Term (6-12 Months)

Month 6 Implement network

segmentation between clinical

and administrative systems

Flat network enabled rapid

lateral movement across all

three clinic sites

$250K

(infrastructure

+ consulting)

Month 9 Deploy privileged access

management for administrative

credentials

Compromised service account

had excessive privileges across

environment

$125K

(licensing +

implementatio

n)

Ongoing Conduct quarterly tabletop

exercises including ransomware

scenarios

Response was effective but

revealed gaps in cross-team

coordination

Staff time

The CFO approved the immediate and short-term recommendations during the meeting. The long-term

items were added to the following year’s budget planning cycle with Dr. Davis’s supporting documentation.

Sustaining Momentum

Dr. Davis recognized that recommendations without follow-through provided no protection against future

incidents. She established a 30/60/90-day review schedule to track progress during implementation. Each

review included the CISO, CIO, and a representative from the executive team to maintain leadership

visibility into security improvements.

Debrief Activity | Chapter 15 | 441

At the ninety-day review, all immediate and short-term recommendations had been implemented or were

on track. The backup system had been remediated and validated with weekly test restores. MFA was

deployed across all remote access points. EDR coverage had reached 100% of managed endpoints. The

authentication monitoring had already generated two alerts for suspicious VPN access patterns, both of

which proved to be false positives but demonstrated that the detection capability was functioning.

The Lakewood incident transformed from a costly disruption into a catalyst for security improvements that

the organization had previously struggled to fund. The comprehensive debrief process, from documentation

consolidation through executive presentation and sustained follow-up, ensured that the organization

extracted maximum value from a painful experience.

DEBRIEF: STEP-BY-STEP

The following steps provide a condensed reference for debrief activities. Each step corresponds to topics

covered earlier in this chapter, organized for use when documenting the incident, capturing lessons

learned, and driving organizational improvement. The debrief serves three primary objectives: documenting

what happened, understanding root causes and contributing factors, and transforming the experience into

organizational improvement.

This step-by-step guide is available for download in PDF and Markdown formats on the

companion website at dynamicincidentresponse.com.

Step 1. Determine Debrief Scope and Documentation Requirements

1. Assess transition readiness, including:

◦ Confirm response actions loop has concluded with no new IOCs discovered.

◦ Verify that organizational decision-makers have approved the transition to debrief.

◦ Ensure critical systems have been restored and validated.

◦ Document any residual risks accepted by leadership.

2. Determine documentation depth based on incident characteristics, including:

◦ Review organizational thresholds for formal documentation (system count, data exposure,

regulatory notification, response duration).

◦ Assess whether the incident triggered external notification requirements.

◦ Consider potential litigation, regulatory inquiry, or law enforcement involvement.

◦ Consult with legal counsel on documentation and retention requirements.

3. Select appropriate debrief approach:

◦ Lightweight debrief: Ticket-based documentation with team lead sign-off for contained incidents.

◦ Formal debrief: Comprehensive documentation with AAR and executive reporting for significant

incidents.

◦ Phased debrief: Capture essential information immediately and defer deeper analysis when

personnel or time are constrained, guided by the organization’s risk tolerance.

◦ Document the rationale for the selected approach in incident records.

4. Address legal and regulatory considerations, including:

◦ Consult legal counsel on documentation practices that protect the organization while supporting

legitimate learning objectives.

◦ Consider whether attorney-client privilege structures are appropriate for sensitive incident

analysis, recognizing that scope and durability vary by jurisdiction.

◦ Identify regulatory frameworks that impose specific documentation and retention requirements.

◦ Balance the need for thorough learning documentation against litigation and disclosure risk.

Step 2. Manage Temporary Assets Created During Response

1. Review forensic evidence for retention decisions, including:

◦ Inventory all forensic artifacts collected (disk images, memory captures, network captures, log

archives).

◦ Consult legal counsel on retention requirements based on potential litigation or regulatory

obligations.

◦ Identify artifacts with ongoing value for threat intelligence, training, or future investigations.

◦ Document retention decisions and destroy artifacts not required for retention.

2. Address temporary accounts and elevated access, including:

◦ Review incident documentation for all temporary accounts created during the response.

◦ Disable or delete temporary accounts unless there is a compelling operational need.

◦ Revoke elevated access granted to responders during the incident.

◦ Document account disposition in incident records with timestamps.

3. Evaluate temporary monitoring configurations, including:

◦ Assess whether temporary monitoring addresses previously undetected attack vectors.

◦ Evaluate operational impact (performance overhead, alert volume) of retained monitoring.

◦ Coordinate with security operations on the permanent integration of valuable configurations.

◦ Remove monitoring configurations that impose excessive burden without proportionate value.

◦ Document decisions on monitoring retention or removal.

Step 3. Consolidate Incident Documentation

1. Gather documentation from all sources, including:

◦ Collect notes from ticketing systems, chat channels, shared documents, and email threads.

◦ Request individual responder notes while memories remain fresh.

◦ Compile forensic analysis reports, tool outputs, and investigation findings.

◦ Gather communication records, including stakeholder updates and decision documentation.

2. Validate and refine the incident timeline, including:

◦ Walk through the timeline with important responders to verify accuracy.

◦ Fill in gaps identified during documentation review.

◦ Reconcile conflicting timestamps or accounts of events.

◦ Document confidence levels for timeline elements based on the quality of the evidence.

3. Document important decisions made during the response, including:

◦ Record significant decisions with alternatives considered and rationale for chosen approach.

◦ Capture decisions that later proved suboptimal with an analysis of what information would have

improved outcomes.

◦ Note any disagreements among responders and how they were resolved.

◦ Preserve decision documentation for future reference and potential legal proceedings.

Debrief Activity | Chapter 15 | 443
