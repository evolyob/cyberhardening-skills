# Chapter 10: Response Actions Loop: Operational Synchronization

> Source: PDF Pages 209-219 (Total Pages: 11)

incident information.

• Be prepared to answer questions: Decision makers may have questions about the incident, the potential

impact on the organization, and the recommended response actions.

The decision-maker should consider the impacted service, the potential impact of the incident on the

organization, regulatory exposure, and the resources available for the response effort. While the incident

response analyst provides insight into the incident, the decision-maker is ultimately responsible for

determining appropriate response actions and allocating resources to the response effort based on the

organization’s overall needs.

Establishing open communication between the incident response team and decision makers occurs during

the preparation activity. See the sidebar Building Management Support for Policy Development  for insight

on how to build management support for the incident response process.

TRIAGE EXAMPLE: THE THIRD-PARTY VENDOR BREACH

A third-party SaaS vendor used for customer relationship management notified the organization of a data

breach. The breach affected customer contact information (names, email addresses, and phone numbers)

for approximately 45,000 customers. Before escalating to decision-makers, the IRT gathered independent

evidence rather than relying on the vendor’s account alone. The analyst pulled the following:

• API gateway logs and egress traffic records showing which data fields the vendor integration had

accessed during the window the vendor described.

• Single sign-on authentication events identifying which internal users had active sessions with the

vendor during that window.

• Cloud Access Security Broker (CASB) telemetry for any anomalous session behavior or bulk data

transfers.

Cross-referencing this telemetry against the customer records held in the organization’s own system of

record, the IRT estimated an affected record count below the vendor’s figure. The analyst classified the

incident as high-risk due to potential regulatory notification requirements under GDPR and state privacy

laws, and flagged the scope discrepancy as an open item requiring further reconciliation with the vendor.

The IRT presented the verified incident to the VP of Customer Experience, the accountable decision-maker

who owned the customer relationship and the business process affected by the vendor breach. The VP of

Legal joined in an advisory capacity to interpret regulatory obligations and coordinate external counsel.

The analyst’s presentation covered:

• Independent evidence of which customer records fell within scope, including the discrepancy against

the vendor’s figure.

• Regulatory notification timelines that may apply (seventy-two hours for GDPR-covered residents).

• The legal obligation to notify customers, contingent on confirming which data fields were actually

exposed.

• Coordination dependencies across Customer Experience, Legal, Marketing, and the IRT.

As the accountable decision-maker, the VP of Customer Experience authorized IRT resources to continue

vendor coordination for the next week and committed her team to reconcile the affected record count

against the organization’s own customer system of record. The VP of Legal engaged external counsel

specializing in privacy law to advise on notification drafting once scope was confirmed. She allocated

budget for that engagement and set the notification-drafting timeline. Together, they established a daily

Verify and Triage Activities | Chapter 9 | 185

thirty-minute status call with Marketing and executive leadership to keep stakeholders informed as details

emerged.

The IRT analyst’s role shifted from technical investigation to coordination and documentation support. The

analyst continued the independent reconciliation effort, working directly with the Customer Experience

team and Legal to ensure the organization met its regulatory obligations without issuing notifications that

exceeded the confirmed scope.

When presenting incidents involving third parties to decision makers, analysts should be

prepared to explain how external dependencies affect resource allocation and response

timelines. The analyst’s role may shift from technical investigation to coordination support,

particularly when regulatory requirements or legal considerations drive the response effort.

Decision makers need to understand not only the technical details of the incident but also

the organizational and legal context to make informed resource-allocation decisions.

VERIFY AND TRIAGE: STEP-BY-STEP

The following steps provide a condensed reference for verification and triage activities. Each step

corresponds to topics covered earlier in this chapter, organized for use when validating a potential incident,

assessing risk, and working with decision-makers to determine response priorities. Verification serves as a

gating function before engaging the broader team: it ensures that the response effort is appropriate for the

risk and avoids expending resources on incidents that are not real.

This step-by-step guide is available for download in PDF and Markdown formats on the

companion website at dynamicincidentresponse.com.

Step 1. Document the Incident Details

Use the incident tracking platform established during preparation. Representative documentation fields

include:

• Incident identifier

• Title

• Handler ID

• Summary

• Classification

• Evidence references

Maintain documentation integrity by keeping notes focused on the incident at hand, avoiding contamination

that could compromise the documentation’s validity as evidence in legal proceedings.

Step 2. Enrich Events of Interest with Cyber Threat Intelligence

Representative activities include:

• Query CTI platforms using technical indicators such as IP addresses, domain names, URLs, or file hashes

observed in the environment.

• Cross-reference multiple CTI sources to increase confidence in the assessment.

• Check indicators against the organization’s local knowledge base of known false positive sources.

• Pivot to related indicators revealed by CTI platforms and spot-check the environment for them, only to

the extent needed to inform the verification decision. Enterprise-wide hunting for the full IOC set is the

scope activity’s responsibility once the incident is verified.

Step 3. Perform an Initial Risk Assessment

Classify the incident as low, medium, high, or critical (or use another classification system that more closely

matches the needs of the organization). Representative considerations include:

• Consider attribution confidence, relevance to the organization, attacker capability, and typical impact

from CTI sources when calibrating the risk classification.

• Remember that the absence of threat intelligence does not indicate the absence of a threat.

Step 4. Verify the Incident

Use the information collected during the detect activity and CTI enrichment to select one of three

verification outcomes.

• Continue: The incident is real. Escalate and engage the broader incident response team and

stakeholders.

• Stop: The incident is not real. Closing an unusual-but-benign finding is harder than it sounds, and the

analyst’s confidence should match the strength of the documentation.

◦ Document the reasoning: what triggered the alert, what evidence ruled out compromise, and what

time window and data sources were examined.

◦ Add the benign source to the organization’s local false-positive knowledge base so future alerts

referencing the same indicator close faster.

◦ Notify stakeholders who reported or expected action, including the original reporter and any

downstream teams.

◦ Close the incident in the tracking platform with a clear classification (false positive, authorized

activity, duplicate, or other) for reporting and trend analysis.

• Defer: The available information is insufficient. Request additional information from the reporting party

or other sources before making a determination.

Step 5. Triage by Presenting to Decision-Makers

Present the verified incident to decision-makers (managers, executives, data owners, legal counsel, or

business unit leaders with authority over the response). Representative activities include:

• Use plain language to explain the incident and the potential impact on the organization.

• Provide context by connecting the incident to the organization’s policies, procedures, and operations.

• Offer recommendations for response actions based on the risk classification and available incident

information.

• Be prepared to answer questions about the incident, its potential impact, and recommended response

actions.

Verify and Triage Activities | Chapter 9 | 187

Step 6. Work with Decision-Makers on Response Actions and Resource

Allocation

Representative activities include:

• Decision-makers should consider the impacted service, the potential impact of the incident on the

organization, regulatory exposure, and the resources available for the response effort.

• Response actions may include assigning resources to investigate, engaging legal counsel, or notifying

law enforcement.

• Recognize that the analyst’s role may shift from technical investigation to coordination support,

particularly when regulatory requirements or legal considerations drive the response effort.

Step 7. Review and Improve the Verification and Triage Process

Representative activities include:

• Track false-positive rates at triage as a quality indicator, watching for drift that suggests upstream

detection tuning is needed.

• Track outcomes of incidents initially stopped or deferred. If any are reopened later as real incidents,

diagnose what was missed and update verification criteria.

• Exercise the verification workflow periodically by rerunning prior incidents through the current process

to confirm that risk assessment, CTI enrichment, and decision-maker presentation still work as

intended.

• Capture recurring patterns that slow verification, including ambiguous alerts, missing enrichment

sources, and unclear escalation paths, and feed improvements back into the Prepare and Detect

activities.

• Solicit decision-maker feedback on whether presentations enabled informed decisions, and whether

recurring follow-up questions signal gaps in how incidents are framed.

10 Response Actions Loop

The response actions loop represents the core operational cycle of the Dynamic Approach to Incident

Response, embodying the iterative nature of effective incident handling.  Unlike traditional linear models

that progress sequentially through containment, eradication, and recovery, the response actions loop

recognizes that incident response is a learning process in which each iteration reveals new information that

requires additional action.  This cyclic approach comprising the scope, contain, eradicate, and recover

activities may be executed multiple times before an incident is resolved.

Figure 66 | Response Actions Loop Activities

ON THE ITERATIVE NATURE OF INCIDENT RESPONSE

The response actions loop fundamentally changes how organizations approach incident response by

acknowledging that complete understanding rarely comes from a single pass through response activities.

Response Actions Loop | Chapter 10 | 189

Each iteration through the loop provides new insights that inform subsequent cycles, creating a continuous

learning process that adapts to the evolving understanding of the incident.

The response actions loop is loop-structured like Colonel John Boyd’s OODA loop (Observe, Orient, Decide,

Act). [1]

However, the two models optimize different things. OODA was developed for military combat

operations, in which it optimizes individual decision speed under pressure. The response actions loop

operates at the process level, optimizing team-wide thoroughness across an investigation rather than the

cognitive cycle speed of any one responder.

Both models move away from a single decision cycle toward continuous adaptation and learning. Each pass

through the response actions loop refines understanding and improves response effectiveness.

A single-pass incident response frequently fails for these reasons:

• Incomplete understanding: An incomplete initial understanding leads to partial remediation, leaving

attacker footholds intact.

• Insufficient insight: New discoveries during eradication reveal additional compromised systems

requiring scoping.

• Incomplete evidence: Evidence analysis uncovers previously unknown attack vectors or persistence

mechanisms through iterative scoping.

• Limited scope: Continued review of the incident’s breadth reveals related IOCs stemming from initial

compromise insights.

The iterative approach acknowledges these realities, building multiple learning cycles into the response

process rather than treating new discoveries as failures or setbacks.

THE FOUR RESPONSE ACTIONS LOOP ACTIVITIES

Each activity in the response actions loop serves a specific purpose while contributing to the overall

learning process. In this section, we’ll introduce each activity in turn: scope for understanding the breadth

of compromise, contain for stopping ongoing damage, eradicate for removing attacker presence, and

recover for restoring operations to the business.

Scope: Understanding Breadth

Scoping determines the extent of the compromise, providing insight into which other systems may be

involved in the incident. Initial scoping might identify a handful of compromised systems, but subsequent

iterations often reveal additional systems with the same malware variants, new indicators of compromise

discovered during analysis, previously overlooked lateral movement paths, and data repositories accessed

by the attacker. Each iteration refines the scope understanding, potentially expanding or contracting the

incident boundaries based on new evidence.

Contain: Stopping the Bleeding

Containment prevents further damage while preserving evidence for analysis. Early iterations might

implement basic containment such as isolating obviously compromised systems, blocking known malicious

IP addresses, and disabling compromised accounts.  Later iterations implement more sophisticated

containment as understanding improves, including careful network segmentation based on lateral

movement patterns, application-specific restrictions targeting attacker tools, and deceptive containment

that misleads attackers while maintaining visibility.

Eradicate: Removing the Threat

Eradication eliminates attacker presence, but rarely succeeds completely in a single attempt. Initial

eradication might remove obvious malware installations, known malicious accounts, and identified

persistence mechanisms. Subsequent iterations address sophisticated persistence discovered through

deeper analysis, backdoors revealed by behavioral monitoring, supply chain compromises requiring vendor

coordination, and living-off-the-land techniques using legitimate tools.

Recover: Restoring Operations

Recovery returns systems to normal operation while addressing the root causes of the incident. Early

recovery iterations might restore critical systems from backups, reset compromised credentials, and patch

exploited vulnerabilities. Later iterations implement systemic security improvements based on root-cause

analysis, enhanced monitoring for specific attack patterns, policy changes to address process failures, and

architectural modifications to prevent recurrence.

ITERATION TRIGGERS

In practice, multiple iterations through the response actions loop are common, driven by new discoveries

and evolving understanding. Continue the response actions loop until no new information emerges and the

incident is resolved to the organization’s satisfaction.

Iteration triggers signal that another pass through the response actions loop is needed before the incident

can move toward completion. Recognizing these signals early is valuable because the cost of a missed

trigger compounds when attacker footholds persist, evidence ages, and stakeholder confidence erodes as

the same systems surface repeatedly in new findings. Analysts should treat every new piece of information

gathered during response, whether from tooling, analysis, or business conversations, as a potential trigger.

For each one, ask whether it changes the current understanding of scope, containment, eradication, or

recovery.

These triggers tend to fall into five broad categories: new indicators of compromise surfaced through

analysis, scope expansion as existing indicators reveal broader reach, evidence of incomplete eradication,

revelations from deeper forensic work, and shifts in business priorities or external obligations that reshape

the response. The sections that follow describe each category and how it should shape the next cycle of

scoping, containment, eradication, and recovery.

New Indicators of Compromise

When analysis reveals previously unknown IOCs, teams should return to scoping to search for these

indicators across the environment. A PowerShell script discovered in one system’s registry might prompt

searches for similar registry modifications elsewhere. Network analysis revealing communication with

additional C2 infrastructure triggers scoping for other systems communicating with those servers.

Scope Expansion

Closely related to new IOCs, scope expansion occurs when existing indicators reveal broader organizational

reach than initially understood. This is not a new indicator surfacing through analysis, but recognition that

an existing indicator extends into systems, accounts, or business units not previously considered in scope

for the incident. For example, a compromised service account first identified in a marketing application may

also be active in finance systems hosting regulated data, expanding the incident’s blast radius without

changing the underlying IOC. Similarly, a malware sample contained on one network segment may be found

Response Actions Loop | Chapter 10 | 191

running on hosts in a different subsidiary acquired during a recent merger. These discoveries trigger

another scoping pass, often with different stakeholders, regulatory considerations, and containment

requirements than the initial response.

Incomplete Eradication

Failed eradication attempts often reveal sophisticated persistence mechanisms requiring another iteration.

Systems that appear clean may show signs of reinfection, indicating missed persistence mechanisms or

ongoing attacker access via unidentified vectors. Each failed eradication provides valuable intelligence

about attacker techniques, informing more comprehensive subsequent attempts.

Evidence Analysis Revelations

Detailed analysis of collected evidence frequently uncovers new insights requiring new response iterations.

This might include memory forensics revealing additional malware families, timeline reconstruction

showing earlier compromise dates, log analysis identifying previously unknown affected systems, or

malware reverse engineering exposing hidden capabilities.

Changing Business Priorities and Obligations

Business priorities frequently shift during an incident, prompting new iterations. A new critical system

identified during scoping may require immediate containment and eradication. Regulatory requirements

might mandate additional scoping to ensure compliance. New business objectives may necessitate revisiting

recovery plans to align with updated operational needs. Cyber insurance requirements may require

additional iterations to satisfy policy conditions.

External obligations from law enforcement or regulators can also reshape the response mid-incident.

Investigators may request preservation of specific systems, defer containment actions to enable continued

observation of attacker activity, or require coordination on public disclosure timing. Regulator contact

carries similar weight, with notification deadlines, evidence handover requirements, and mandated scope

expansion that warrant additional iterations of the response actions loop regardless of where the team is in

the response process.

Like the activities in the response actions loop, these triggers are not failures but rather expected parts of

the learning process. Each iteration builds on prior knowledge, progressively refining understanding and

improving response effectiveness, aligning with the dynamic nature of modern cyber incidents and any

changes to business priorities.

Stakeholder Communication

Stakeholder communication keeps leadership and affected parties informed of progress through regular

updates tailored to different audience needs and authority levels. Create executive summaries for senior

leadership that focus on business impact, risk reduction, and resource requirements, without excessive

technical detail.

Deliver technical briefings for IT teams and security staff that include implementation details, monitoring

requirements, and validation procedures. Communicate with affected users about service disruptions,

workarounds, and expected resolution timelines to manage expectations and maintain trust.

Adjust communication frequency and detail based on incident severity and stakeholder needs, recognizing

that communication requirements may intensify during critical phases and decrease as the incident

stabilizes. Documentation needs vary across organizations and can be as simple or as complex as necessary

to support the business.

Effective documentation and communication practices create a foundation for informed decision-making

throughout the response actions loop. Documentation is an additional responsibility for analysts that

requires time and effort, but it is essential for ensuring that response actions are transparent, defensible,

and aligned with organizational objectives. The records generated during each iteration of the response

actions loop support not only the current incident but also future response efforts by capturing lessons

learned and preserving institutional knowledge. As teams cycle through multiple iterations, this

documentation will accumulate into a comprehensive incident narrative.

DOCUMENTATION AND COMMUNICATION

Each activity in the response actions loop requires thorough documentation to meet legal requirements,

support organizational learning, and enable effective stakeholder communication. Scoping decisions,

containment actions, eradication procedures, and recovery steps all generate information that should be

captured systematically throughout the incident lifecycle. This documentation serves multiple purposes: it

provides a defensible record of response decisions, enables knowledge transfer between team members

across shifts and iterations, and supports post-incident analysis that improves future response capabilities.

Documentation should be captured in a controlled yet accessible manner for authorized incident response

personnel, ensuring that all response actions are recorded in a centralized incident tracking system or case

management platform. For many organizations, security labels and access controls within existing ticketing

systems can restrict access to sensitive incident documentation while allowing incident responders to

update and review actions as needed. Maintain documentation continuity across multiple iterations of the

response actions loop, linking related findings and actions so that the full incident narrative remains

coherent as understanding evolves.

Organizations may require specific documentation resources to meet business and industry-specific

regulatory requirements. At a minimum, response actions documentation should include decision

documentation, impact assessment, and stakeholder communication logs for each phase of the response.

Decision Documentation

Decision documentation records the actions taken, when they were executed, who authorized them, and

the rationale for each decision. During scoping, document which systems were examined, what indicators

were searched, and what findings emerged from each iteration.

For containment, record which isolation measures were implemented, what alternatives were considered,

and why particular approaches were selected. Eradication documentation should capture which artifacts

were removed, how removal was verified, and what challenges arose during the process. Recovery records

should include which systems were restored, what validation steps confirmed successful restoration, and

what security improvements were implemented.

This documentation provides important information for post-incident analysis, potential legal proceedings,

and regulatory inquiries that might question response decisions.

Impact Assessment

Impact assessment tracks the operational impact of response actions on business processes, user

productivity, and system availability. During the incident, analysts should identify and record which

Response Actions Loop | Chapter 10 | 193

business functions were affected by each action, the approximate number of users affected by disruptions,

the revenue impact of system downtime, and the workarounds implemented to maintain critical operations.

This assessment helps improve future response strategies by identifying which approaches provided

effective security with minimal business disruption.

Track impact across all four response activities, as scoping activities may require system access that affects

performance, containment disrupts normal operations, eradication may require service outages, and

recovery involves transition periods with reduced functionality.

Impact assessment data increasingly feeds regulator submissions in the days and weeks after an incident

closes. Regulations such as the Digital Operational Resilience Act (DORA) require financial-sector

organizations to report the impact and associated costs of significant incidents, including direct

remediation expenses, lost revenue, and follow-on business disruption. [2]

Capture impact details in a form

that can be shared with the person responsible for regulator notifications. Use clear attribution of which

business functions were affected, for how long, and under what response action. Recording this information

as the incident progresses is substantially easier than reconstructing it after closure, when memory fades

and log-retention windows begin to expire.

KNOWING WHEN TO STOP

Determining when to exit the response actions loop requires careful judgment informed by technical

indicators, business considerations, and input from organizational decision makers.  From a technical

perspective, teams look for signs that the incident is truly resolved, such as no new IOCs discovered during

scoping, monitoring showing no signs of attacker activity, eradication verification confirming threat

removal, and systems operating normally after recovery. These indicators provide confidence that the

threat has been successfully addressed and the organization can safely conclude active response efforts.

Business indicators also play a critical role in the decision to exit the loop. Organizations should assess

whether operational objectives are met, whether an acceptable risk level has been achieved, and whether

the cost-benefit analysis supports the conclusion that active response activities should continue. Resource

constraints may require prioritization, forcing difficult decisions about when to conclude response efforts

even when some uncertainty remains.

The decision to exit the response actions loop often involves organizational leadership providing input on

acceptable risk levels and operational priorities. Leadership should weigh the risk of accepting residual

uncertainties against business pressure to resume normal operations. Regulatory requirements for incident

closure may mandate specific conditions before the incident can be formally closed. Strategic decisions

about ongoing monitoring help balance the need for continued vigilance against the need to return

resources to normal operations.

In some organizations, these decisions require formal sign-off, while others rely on consensus among key

stakeholders. This reflects organizational culture and risk tolerance rather than process maturity.

Whichever model applies, the decision to exit the loop should be captured in writing as a positive, attributed

decision rather than an implied agreement. The record should name the decision-maker, the supporting

technical and business indicators, the residual risks accepted, and the date and time the decision was taken.

Documenting the decision in this form ensures that all participants recognize they had input and that the

rationale remains defensible if the incident is later reopened or reviewed by regulators.

The prospect of being named in the documented exit decision can itself improve decision

quality. Executives who were prepared to verbally agree that an incident could be closed

sometimes reconsider when told their name will appear against the decision in the record.

PRACTICAL CONSIDERATIONS

In my experience working with different teams to refine their incident response processes, the response

actions loop seems to increase effort and complexity. This is true, as the iterative approach requires more

time and resources upfront. However, it is necessary to address all elements of a sophisticated incident

effectively, which would otherwise be missed in a linear approach.

Consider the example shown in Figure 67. In this example, the incident response team works from an initial

threat report and responds to the incident, but fails to learn about additional threats in the process.  In

contrast, using an iterative model as shown in Figure 68, the team uncovers multiple related threats through

successive iterations of the response actions loop.

Figure 67 | Linear Response Threat Processing

Figure 68 | Iterative Response Threat Processing

To successfully implement the response actions loop, teams should address several practical considerations

arising from the process’s iterative nature.

Response Actions Loop | Chapter 10 | 195
