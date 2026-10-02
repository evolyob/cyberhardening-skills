﻿# 第 07-1 章：準備階段－策略、政策與漏洞揭露計畫

> 模組化子章節 | 隸屬來源:  (行 1 ~ 1651)

---

# Chapter 7: Prepare Activity: Visibility & Telemetry

organizationally damaging, such as taking all systems offline simultaneously for imaging.

Throughout the incident response process, we’ll communicate with and get input from decision makers to

ensure that incident response actions align with organizational priorities.

NEW WAYPOINTS: VERIFY AND TRIAGE, AND SCOPING

Figure 26 | Verify and Triage Waypoint

The DAIR model introduces two new waypoints not explicitly called out in other incident response models:

verify and triage, and scoping. These waypoints are essential for effective incident response, and warrant

inclusion as dedicated waypoints in the incident response process.

The verify and triage waypoint follows the detect waypoint to emphasize the need to validate that an

incident is indeed an incident, and to prioritize incidents based on organizational goals, as shown in Figure

26.

When an incident is declared and the team responds, it can negatively affect the organization, including

diverting resources from other projects or reducing the performance of systems under investigation. The

verify action ensures that the observed event is indeed an incident, and one that requires an incident

response action.

Next, the triage action helps to prioritize incidents based on organizational objectives, ensuring that the

incident response team focuses on the most important incidents first. This is especially important for

incidents with broad organizational impact, allowing decision makers in the organization to coordinate with

the incident response team to ensure that the most important incidents are addressed first.

The verify and triage waypoint is unique in the DAIR model in that both actions happen concurrently. This is

because both require insight and coordination with decision makers to ensure that the incident response

team responds to the right incidents with the right resources.

SCOPE

Figure 27 | Scope Waypoint

The scope waypoint is essential for understanding the breadth of the incident, the systems involved, and the

potential impact on the organization. When we perform scoping, we use the information gathered during

the detect and verify actions to gain insight into the attacker’s TTPs to identify Indicators of Compromise

(IOCs). Once we identify one or more IOCs, we can use them to scope the incident, identifying the systems

Figure 28 | Response Actions Loop

The response actions loop is an important element of the DAIR model, emphasizing the inherent need to

repeat multiple actions in the incident response process. The loop itself is not necessarily linear, where we

perform each action in sequence. Instead, it represents an iterative analysis function, using the conventional

contain, eradicate, and recover waypoints as necessary to respond to the incident, while integrating the

scope activity to improve our understanding of the incident details.

For example, a response action loop may start with a single system being compromised following the

verification of an unauthorized user account IOC. Upon containing the system and collecting data for

analysis, the incident response team may identify that the user account is associated with a scheduled task

that runs malicious code. This insight is valuable for additional scoping, to identify other systems with

similarly-configured scheduled tasks that may indicate additional compromises. Only after continued

investigation and scoping can the incident response team effectively eradicate the threat and recover the

systems.

The response actions loop is repeated as many times as necessary to perform the required response

functions, guided by the needs of the business. In practice, these actions are repeated multiple times until

no new evidence of compromise is found, and the incident response team (and decision makers) are

confident that the incident has been effectively addressed.

REVIEWING THE DAIR MODEL

The Dynamic Approach to Incident Response (DAIR) model emphasizes the dynamic nature of incident

response, and the need for flexibility and agility in responding to incidents. It prioritizes new waypoints,

such as verify and triage, and scoping, to ensure that the incident response team responds to the right

incidents with the right resources. It also emphasizes the response actions loop, which is an iterative

process that is repeated as many times as necessary to effectively respond to the incident, while

coordinating with decision makers to ensure that incident response actions align with organizational

priorities.

In many ways, the DAIR model does not markedly deviate from the PICERL or the NIST SP 800-61

models, continuing to embrace the important elements of incident response that have been developed over

time and proven to be effective for many organizations. Rather, it helps us to reshape the existing models

while identifying important additional considerations. The DAIR model allows us to apply the same phases

to more effectively prepare for, identify, respond to, and review the effectiveness of the incident response

function.

Next, we’ll look at each of the important waypoints in the DAIR model in more detail.

7 Prepare Activity

The prepare activity in incident response prepares the organization for the possibility of an incident. This

includes creating an incident response plan, training staff, and ensuring the necessary tools and resources

are in place and ready for when an incident occurs.  Preparation is called out in the DAIR, PICERL, and NIST

SP 800-61 models, and is an important element for any organization’s incident response capability.

Figure 29 | Prepare Activity Waypoint

Much of the incident response team’s time should be spent in preparation. When not actively responding to

an incident, the team should be preparing for the eventuality of an incident while actively looking for any

threats in the organization’s environment (the detect activity). It’s common to get overwhelmed with the

amount of work that needs to be done in preparation, but the more prepared the team is, the better they’ll

be able to respond to an incident when it occurs. Preparation is a process in itself that can be developed and

improved over time.

This chapter explores the objectives of preparation, strategies for building organizational and team

readiness, and challenges that complicate preparation efforts. The chapter also discusses practical

techniques for developing policies, training teams, and establishing proactive detection capabilities, before

examining activity examples.

PREPARE OBJECTIVES

The prepare activity serves three objectives: building organizational readiness for incident response,

developing the incident response team’s capabilities, and establishing proactive prevention and detection

measures. While other DAIR activities focus on responding to active threats, preparation lays the foundation

for an effective response.

The first objective focuses on organizational readiness. This includes developing the policies, plans, and

playbooks that govern decision-making during incidents, establishing communication channels and

reporting procedures, and securing management support for incident response capabilities. Organizations

that invest in these foundational elements respond more effectively when incidents occur because critical

decisions about priorities, authority, and coordination have already been made.

The second objective centers on developing incident response team capabilities. Technical skills,

established relationships with important personnel, documented playbooks, and access to necessary tools

and systems all contribute to response effectiveness. Teams that train together, conduct exercises, and

maintain their toolsets respond more quickly and with greater confidence than teams forced to improvise

during active incidents.

The third objective establishes proactive prevention and detection measures.  While no organization can

prevent all incidents, preparation activities such as vulnerability management, security monitoring, and the

integration of cyber threat intelligence (CTI) reduce the likelihood and impact of successful attacks. These

measures also improve detection capabilities, enabling earlier identification of threats before they cause

significant damage.

THE PREPARATION PARADOX

Incident response preparation faces an inherent challenge: its value is most apparent when it’s

needed least. That is, preparation investments are hardest to justify when they’re working.

Organizations that invest heavily in preparation may never experience a major incident, leading some

to question whether the investment was worthwhile. Conversely, organizations that experience

significant incidents often wish they had invested more in preparation beforehand.

This paradox can create tension in resource allocation decisions. Security teams can address this

tension by framing preparation investments in terms of risk reduction rather than incident

prevention. Tracking metrics that demonstrate the value of preparation provides tangible evidence:

reduced mean time to detect (MTTD), faster containment during training exercises, and improved

coordination during tabletop scenarios. These measurements provide evidence of preparation

effectiveness without requiring an actual incident to demonstrate value to the organization.

PREPARATION STRATEGIES

Preparation activities are grouped into three main areas:

• Preparing the organization: Developing the policies, plans, and playbooks that govern decision-making,

establishing management support, and defining how the organization communicates and coordinates

during an incident.

• Preparing the incident response team : Building the technical skills, playbooks, relationships, and

tooling that enable responders to act decisively when incidents occur.

• Proactive prevention and detection : Deploying monitoring, threat intelligence, and hardening

measures that reduce incident frequency and improve the team’s ability to identify threats early.

In this section, we’ll examine each of these areas in more detail.

DISTINCT BUT RELATED: POLICIES, PLANS, AND PLAYBOOKS

In this chapter, we use terms that are sometimes conflated: policies, plans, and playbooks. While

often used interchangeably, it helps to clarify who is responsible for these elements and how they

affect the incident response team.

Policies: These are high-level directives set by organizational leadership, often the CISO or executive

team. They establish the boundaries for decision-making: whether to pay ransom, when to involve

legal counsel, and under what conditions to disclose publicly. Policies answer the question "what has

the organization decided?"

Plans: The incident response plan translates policy into operational structure. It defines roles and

responsibilities (often through a RACI matrix, see Clarifying Roles with a RACI Matrix ), delegated

authority, escalation paths, and communication workflows. The plan answers the question "who does

what, and when?"

Playbooks: These provide step-by-step guidance for responding to specific incident types and using

specific tools. A ransomware playbook, for example, walks responders through containment, evidence

collection, and recovery actions tailored to that scenario. Playbooks answer the question "how do we

respond?"

These three elements work together: policies set the boundaries, the plan establishes structure and

authority, and playbooks provide tactical guidance for execution.

Prepare the Organization

Preparing the organization for an incident involves developing the policies, plans, and playbooks that outline

how it will respond. This area of focus considers broader incident response priorities, the involvement of

management teams, and whether and how the organization will communicate and coordinate with

attackers. These activities span the people and process foundations of incident response: establishing who

is involved, what authority they have, and how the organization communicates and makes decisions during

an incident.

GAINING MANAGEMENT SUPPORT FOR POLICY DEVELOPMENT

Many of the activities in the preparation phase require management support to inform policy

decisions that best suit the organization’s needs. Technical leads and incident responders will need to

work with management to ensure that the organization is prepared for an incident.

One of the best ways to get management support is to show the value of incident response to the

organization while minimizing the time management needs to invest in developing policies.

Demonstrating respect for their time and expertise by outlining or drafting policies for their review

and feedback prior to approval can go a long way toward building a strong working relationship with

management.

Consider the following two approaches when working with management to develop a policy for when

to involve the legal team in an incident.

An open-ended approach asks management to define the policy from scratch:

“"We need a policy for when to involve the legal team in an incident. When do you want to involve

the legal team when there’s an incident?"

A prepared-option approach presents a draft for management to react to:

“"I’d like to draft a policy for legal team involvement during incidents for your approval. I propose

that we engage legal for confirmed incidents involving potential public disclosure, cyber insurance

claims, or law enforcement coordination. Does that align with your expectations, or are there other

scenarios we should include?"

Presenting well-considered options to management demonstrates that the incident response lead

has thought through the issue’s implications and values management’s time and expertise. Policy

development can be challenging and requires significant time and effort. By supplying the decision-maker with well-considered options, incident response leads can help minimize the time and effort

required to develop the policies that are a necessary element of effective incident response.

Develop Organizational Policies

Organizational policies are an essential tool for guiding the organization’s incident response approach.

manage and maintain while avoiding contradictory statements. Separate policies can provide more detailed

guidance on specific topics and are easier to update individually. Regardless of the approach taken, policies

should be reviewed regularly to ensure they remain up-to-date and relevant to the organization’s needs.

When developing organizational policies for incident response, consider including the following elements:

• Company mission as it relates to incident response.

• Goals for the incident response program.

• The organization’s priorities before, during, and following an incident.

• Policy on involving management teams in the organization, including GRC, legal, and public relations

• Policy on paying ransom or extortion.

• Policy on communicating with attackers.

• Policy on data retention and preservation of evidence.

• Policy on reporting incidents to law enforcement agencies, government, or industry partners.

• Policy on public disclosure of incidents.

• Policy on engaging with third-party incident response providers or additional resources when needed.

• Containment authorization policies defining who can authorize systems to be taken offline.

The incident response plan should also address operational elements that translate these policies into

practice, including recovery time objectives (RTO) and recovery point objectives (RPO) for critical systems,

evidence retention requirements and chain of custody procedures, and role assignments for coordination

across teams.

This is not an exhaustive list. Organizations will need to develop policies and plans tailored to their unique

needs and risk profile.

Among these policy elements, containment authorization deserves particular attention. During active

incidents, responders frequently hesitate over questions like "Am I allowed to shut down this server?" or

"Can I isolate this network segment?" This hesitation, sometimes called escalation paralysis , delays

containment while responders seek approval through ad hoc channels. Documenting authorization levels in

advance reduces this delay by establishing clear decision rights for common containment actions.

Consider defining authorization tiers that map actions to approval requirements:

• Tier 1 (SOC/IRT-authorized) : Isolating individual endpoints and user workstations, disabling

compromised user accounts, and blocking known malicious IP addresses

• Tier 2 (Service owner-authorized) : Isolating servers or services, disabling service accounts,

implementing broader firewall rules that affect specific business functions, and activating the IR

retainer or cyber insurance IR provider

• Tier 3 (Executive-authorized) : Shutting down production systems, isolating network segments, taking

actions that affect regulated systems or public-facing services, and engaging external parties such as

law enforcement or regulators

These tiers should reflect the organization’s risk tolerance and operational requirements. The important

distinction between tiers is impact, not seniority: Tier 1 actions affect individual users and endpoints with

limited business disruption, Tier 2 actions affect services and require the service owner to assess

operational impact, and Tier 3 actions carry organization-wide or regulatory consequences that require

executive approval. Depending on the organization’s culture and level of incident response preparation, the

specific actions that fall into each tier may vary. The goal is to give responders confidence to act quickly on

low-impact containment actions while ensuring that decisions with significant business or regulatory

impact receive appropriate authorization.

Organizations subject to regulatory frameworks such as the Network and Information

Security Directive (NIS2) or the Digital Operational Resilience Act (DORA) should account

for these obligations when defining authorization tiers, as containment actions that affect

regulated systems or services may trigger notification and impact assessment

requirements. [1]

SAMPLE INCIDENT RESPONSE POLICY AND PLAN TEMPLATES

Writing incident response policies and plans from scratch can be daunting. Fortunately, several

template documents are available with permissive licenses that organizations can use as a starting

point. Some of these templates focus on high-level policy, while others blend policy with plan

elements such as roles, escalation paths, and procedures.

• FRSecure Incident Response Plan Template

• ICIMS Incident Response Policy Template

• GovRAMP Incident Response Plan Template

• Prima Incident Response Plan Template

• CIS Incident Response Policy Template

• CRF Resilience Management Policy Template

Many of these templates preserve the linear approach to incident response rather than the DAIR

model prescribed in this book, but they still provide a valuable starting point for developing

organizational incident response policies and plans.

Organizations can also utilize AI platforms to assist with drafting incident response policies and

plans. See Chapter 16  for more information on using AI to assist with incident response tasks,

including drafting incident response documentation.

Develop Management Support

The DAIR model emphasizes the importance of management support for incident response. Throughout an

incident, the incident response team will rely on management for decision-making, resource allocation, and

communication with external stakeholders. Developing management support for incident response is

essential to the success of the incident response effort.

One of the best ways to secure management support during an incident is to build strong relationships with

management beforehand. Every organization is different, and different managers will have different

priorities and different working styles. What works to establish a strong relationship with one manager

might not work for another. However, there are several common elements that incident response leads can

use to develop management support:

• Communicate the value of incident response to the organization, using examples from other industries

or organizations.

• Keep management informed about industry events that affect the organization, such as regulatory

changes or new threats, and explain why they are relevant.

• Seek management’s insight and expertise throughout the preparation activity of the incident response

process.

• Develop a communication plan that outlines how management will be informed during an incident, and

how they will guide the incident response team during the incident.

• Demonstrate valuing their time and expertise with clear, concise, and well-considered options for

decision-making.

• Assign management actionable responsibilities such as participating in tabletop exercises, breach

simulations, or on-call rotations during incidents, aligning with frameworks like ISO 27001 that define

specific management requirements for information security. [3]

By establishing a role as a source of expertise and insight, incident response leads can build trust with

management and establish a supportive working relationship. This will help ensure that management is

engaged and supportive during an incident, and that the incident response team has the resources and

authority needed to respond effectively.

Identify Risk Assessment and Classification Processes

Effective incident response requires clear criteria for assessing risk and classifying incidents. Without

predefined risk assessment thresholds, responders waste valuable time determining severity levels and

appropriate responses. Establishing risk assessment processes during preparation ensures consistent, rapid

decision-making when incidents occur.

During an incident, responders often feel pressure to quickly classify it and determine the

appropriate response. Having predefined risk assessment criteria allows responders to

make these decisions confidently and consistently, reducing uncertainty and delays.

Risk tolerance thresholds define acceptable risk levels and escalation triggers for the organization. Work

with decision makers to establish clear criteria for what constitutes low, medium, high, and critical risk

events. These thresholds should consider factors such as data sensitivity, system criticality, regulatory

implications, and potential business impact. Document these thresholds in a format that responders can

quickly reference during incidents.

Some organizations find a severity level-label (e.g., level-0, level-1, level-2) useful for

quickly communicating risk levels during incidents, rather than descriptive terms that can

be more subjective. Other organizations use a color-based scheme (such as CISA’s green,

yellow, orange, red, black) to indicate severity levels. [4]

Consult with decision makers in

the organization to determine which approach will work best to communicate risk.

Incident classification criteria provide a framework for categorizing incidents based on their characteristics

and potential impact. Consider developing a classification matrix that maps incident types to severity levels

based on factors such as:

• Number of systems or users affected.

• Type of data potentially compromised (public, internal, confidential, regulated).

• Impact on business operations (none, degraded, disrupted, halted).

• Regulatory notification requirements triggered.

• Potential for lateral movement or escalation.

Risk assessment processes should be reviewed and updated regularly as the

organization’s environment, threat landscape, and risk tolerance evolve. Annual reviews

aligned with broader risk management activities help ensure classification criteria remain

relevant.

BROAD VS. SPECIFIC RISK ASSESSMENT CRITERIA

Some organizations will benefit from broad risk assessment criteria that provide at-a-glance

guidance for responders. For example, consider the risk Incident Prioritization Matrix published by

InvGate. [5]

This matrix provides a simple framework for assessing incident priority based on impact

and urgency, with considerations for impact scope and organizational urgency.

Figure 30 | InvGate Incident Prioritization Matrix

Figure 31 | CISA Incident Scoring Rubric

Organizations should evaluate which approach works best for their needs, considering factors such

as team experience, incident complexity, and organizational culture. Organizations with less

experienced responders may benefit from more specific criteria that provide detailed guidance, while

organizations with seasoned responders may prefer broader criteria that allow for more flexibility in

assessment.

Develop an Incident Communications Plan

Incident communications span multiple audiences, channels, and timelines, from real-time coordination

among responders to regulatory notifications days after discovery. Without a unified plan, these elements

fragment under pressure: technical teams use one channel while executives use another, contact lists go

stale, and public messaging contradicts internal updates.

A single, governed incident communications plan brings these elements together. The following sections

address its components: the channels used for coordination, the contact information needed to reach

stakeholders, the reporting procedures that keep leadership informed, and the emergency communication

plan that governs public and regulatory messaging. Taken together, these components should be

maintained as an evolving document, reviewed at least annually, and tested during tabletop exercises.

C4: A SOFTWARE DEVELOPMENT MODEL

The C4 model is a widely adopted framework for visualizing and documenting software architecture.

Created by Simon Brown, the model was designed to bring structure, clarity, and consistency to

architectural diagrams. It uses a hierarchical approach to help teams avoid getting lost in technical

details while capturing enough detail for effective communication.

During an incident, responders encounter the same challenge that software architects face with

documentation: multiple audiences need to understand the same situation, but at different levels of

detail and with different priorities. Applying C4 thinking to incident communications means

evaluating every message, update, and notification against four characteristics:

• Coherent: All messaging aligns with a single, accurate understanding of the incident. Technical

updates, executive briefings, and external statements should tell the same story at different levels

of detail, not different stories.

• Consistent: Messaging across channels and over time should not be contradictory. Establish a

single source of truth for incident details, and route all outbound communications through a

defined approval workflow.

• Concise: Recipients under pressure need actionable information, not lengthy narratives. Status

updates should lead with what changed, what the impact is, and what action is needed.

• Converted: Communications should be tailored to each audience. A board briefing requires

different framing than a technical update to the SOC, and a customer notification requires

different language than an internal all-hands message. Each audience receives the same facts,

presented in the form they need to act on them.

These four characteristics apply across every component of the incident communications plan. When

reviewing or exercising the plan, evaluate each component against them. For example, consider the

following update posted to an incident channel during a ransomware event:

“We found ransomware on a bunch of servers. IT is working on it. We think the backups are fine but

we’re not sure yet. Someone should probably tell the CEO.

This update is not coherent (a bunch of servers leaves scope to interpretation) and not consistent (we

think the backups are fine  introduces an unverified claim that later updates may contradict). It is not

concise (missing containment status and next steps) and not converted (written for no particular

audience, with no ownership of the executive notification). A C4-aligned version for the incident

channel:

“Seven servers in the finance segment confirmed encrypted by LockBit variant. All seven isolated

from the network at 09:15 UTC. Backup integrity verification is in progress. Incident commander is

preparing an executive briefing for distribution by 10:00 UTC. Next technical update at 10:30 UTC.

Using C4 effectively throughout the organization requires that each person involved with the incident

understands the expectation for communication and the importance of these characteristics.

Additional information on applying C4 principles is available at c4model.com.

Establish Communication Channels

During an incident, the response team will need to communicate with a variety of stakeholders, including

other team members, management, legal, public relations, system stakeholders, and possibly external

partners. Establishing secure, reliable communication channels is important for ensuring the team can

effectively coordinate and collaborate during an incident.

When establishing communication channels, consider the platform characteristics that are important for

incident response, including confidentiality, authentication, mobility, rich information sharing, and more. A

summary of the important factors to consider when selecting a communication platform is provided in

Table 3.

Table 3 | Communication Channel Considerations

FACTOR DESCRIPTION

Authentication Identity validation for participants through strong authentication including

MFA.

Confidentiality Encryption of messages, access-controlled channels, and access controls to

prevent unauthorized access to conversations.

Mobility Accessible from desktops and mobile devices with consistent security across

platforms. Notification controls for mobile devices.

Data Retention Conversation history preservation for documentation, stakeholder awareness,

and potential legal or regulatory inquiries.

FACTOR DESCRIPTION

Resilience and

Availability

High availability with protections against outages and denial of service

attacks during incidents.

Access Logging Recording of participant identities and platform access for audit and

accountability purposes.

Communication

Clarity

Threaded messaging and channel organization to keep discussions focused

when multiple investigations are active.

Data Provenance Ability to identify who posted information, when it was posted, and whether it

has been edited.

Rich Information

Sharing

Support for files, images, code snippets, and collaboration features including

text, voice, video, and screen sharing.

Many organizations will use communication platforms already in use such as Slack or Microsoft Teams

alongside additional security controls (such as private channels). This can be a reasonable approach, as long

as a secondary communication platform is identified in case the primary platform is considered

compromised or unsafe. Alternative communication platforms might include Signal or Element.

Establish and test backup communication channels before they are needed. If the primary

communication platform is compromised or unavailable during an incident, the team should

be able to transition to the backup platform without delay.

When planning backup channels, account for scenarios in which the organization’s own containment

actions disrupt communications. Network isolation measures that block external traffic can cut off cloud-based platforms like Slack or Microsoft Teams, leaving the response team without its primary coordination

tool during active response. The backup platform should use independent authentication, separate from the

organization’s primary directory (such as Active Directory or Entra ID). If domain administrator accounts

are compromised, an attacker who controls the directory may also have access to any platform that

authenticates against it, including the backup communications channel.

Document Contact Information

As part of the prepare activity, document contact information for the people who will be involved in the

incident response process. Consider filling out a contact information template that includes the following

information for each stakeholder. An example template is provided in Table 4.

Table 4 | Contact Information Template

Organization Falsimentis Corporation

Department IT

Email jwright@falsimentis.com

Alternate Email jwright@hasborg.com

Phone (office, mobile) +1-401-555-1212 (office), +1-401-555-1213 (mobile)

Messaging Platform ID @jwright (Slack)

Alternate Messaging Platform

ID

@joswr1ght.44 (Signal)

Timezone US Eastern (UTC-5)

Skills/Specializations UNIX systems, cloud infrastructure, scripting

Last Updated 2026-08-02

Make the contact information document available to the response team and other stakeholders, and ensure

it remains up-to-date. Make it available in both digital and paper formats, accessible to the team.

Beyond internal contacts, maintain contact information for external parties that may be involved in incident

response:

• Law enforcement contacts (FBI, state law enforcement, local law enforcement, relevant national

agencies).

• Regulatory bodies relevant to the organization’s industry.

• Cyber insurance carrier and claims contacts.

• Incident response retainer providers.

• Legal counsel with cybersecurity expertise.

• Public relations or crisis communications support.

• Industry Information Sharing and Analysis Centers (ISACs).

• Important vendor and cloud provider security contacts.

Maintaining current external contact information is as important as internal contacts, as delays in reaching

law enforcement or legal counsel during an incident can have significant consequences.

Establish External Reporting Channels

While internal contact information supports outbound communication during incidents, organizations

should also plan for inbound disclosures from security researchers, customers, and partners who identify

compromises or vulnerabilities. Researchers who discover issues often struggle to find the right contact

within an organization to report their findings. Without a clear reporting channel, researchers may give up

trying to reach the responsible organization, post findings publicly, or contact the wrong department

entirely.

The RFC 9116 standard addresses this problem by defining a machine-readable file that organizations place

on their web servers to communicate security contact information and vulnerability disclosure policies. [6]

Organizations publish a security.txt file at /.well-known/security.txt on their web servers. The file

contains contact information (email, phone, or URL), an expiration date, and optional fields for encryption

keys, disclosure policies, acknowledgment pages, and preferred languages.

Listing 27 | Microsoft security.txt Example

$ curl -q hxxps://www[.]microsoft[.]com/.well-known/security.txt

# Our security acknowledgements page

Acknowledgments: hxxps://msrc[.]microsoft[.]com/update-guide/acknowledgement

# Canonical URI

Canonical: hxxps://www[.]microsoft[.]com/.well-known/security.txt

# Our Researcher Portal

Contact: hxxps://msrc[.]microsoft[.]com/report/vulnerability/new

# Our PGP Key

Encryption: hxxps://msrc[.]microsoft[.]com/.well-known/csaf/openpgp/998D7EC1A516E3D17FF90480EF148D3CDE714E0D.asc

Expires: 2026-09-23T16:00:00.000Z

# Our Bounty policy

Policy: hxxps://www[.]microsoft[.]com/en-us/msrc/bounty/

# Our Coordinated Vulnerability Disclosure Policy

Policy: hxxps://www[.]microsoft[.]com/en-us/msrc/cvd

# Our Bounty Legal Safe Harbor Policy

Policy: hxxps://www[.]microsoft[.]com/en-us/msrc/bounty-safe-harbor

# Our Common Security Advisory Framework (CSAF) publications

CSAF: hxxps://msrc[.]microsoft[.]com/csaf/provider-metadata.json

Preferred-Languages: en

Publishing a security.txt file is only half the work: the contact address it advertises should route to the

include the following elements:

• Purpose statement.

• Scope of reporting (e.g., what incidents are covered, who is responsible for reporting).

• Reporting requirements (e.g., what information should be included in the report, who should receive the

report).

• Service Level Agreement (SLA) for reporting.

Most organizations will prioritize more frequent reporting requirements based on the perceived impact of

the incident. For example, a high-impact incident might require an initial report within one hour of

identification with daily updates, while a low-impact incident might only require weekly or bi-weekly

updates. A sample SLA for reporting is provided in Table 5.

Table 5 | Sample Incident Reporting SLA

IMPACT LEVEL DESCRIPTION INITIAL REPORT SLA FULL REPORT SLA

Critical Severe business disruption, data breach

affecting sensitive data, or regulatory

impact

Within 1 hour Within 24 hours

High Significant operational disruption,

targeted attack, or compromise of

critical infrastructure

Within 2 hours Within 48 hours

Medium Limited operational impact, detected

malware, or unauthorized access

attempt

Within 4 hours Within 72 hours

Low Minimal or no operational impact,

routine security event, or false positive

Within 2 days Within 5 business

days

Adapt the impact level labels to the organization’s needs (e.g., low to critical, level 0 to

level 4, green to black, etc.).

Develop an Emergency Communication Plan

The Emergency Communication Plan (ECP) provides guidance for the organization when sharing internal or

public information about an incident. While not all incidents will require broad messaging to a large number

of users, having the plan in place allows the team to share incident details with the appropriate audience in

a timely manner while minimizing the risk of misinformation.

The ECP should address several important elements of internal and public messaging following an incident:

• Notification triggers: Define which incident types require broader communication beyond the incident

response team. Consider regulatory requirements, contractual obligations, and organizational policy

when establishing these triggers.

• Approval workflows : Establish who should approve communications before distribution. Different

communication types may require different approval levels, with external communications typically

requiring executive or legal approval.

• Message templates : Develop template communications for the first twenty-four hours of common

incident types, when messaging mistakes are most costly to correct. Templates should be reviewed by

legal counsel and communications professionals in advance.

• Constituent audiences : Identify the different audiences that may need to be informed during an

incident. This may include customers, partners, regulators, and internal employees, but may extend

beyond those groups as well depending on the nature of the incident and data involved.

• Distribution channels: Identify how communications will be distributed to different audiences. Internal

employees may receive notifications through email or intranet, while external parties may require

different channels.

• Spokesperson designation : Identify who is authorized to speak on behalf of the organization during

incidents. Ensure designated spokespersons receive media training appropriate to their role.

Most incidents fit one of five communication categories. Producing a template set for each category

provides the team with a faster starting point during the first twenty-four hours, when accuracy and tone

are essential to maintaining stakeholder trust.

• Ransomware: encryption events, including extortion-aware messaging.

• Denial-of-service (DoS): availability impact and customer-facing service disruption.

• Cyber attack (generic) : intrusions, account compromise, or data theft not covered by ransomware or

DoS templates.

• On-premises IT outage : infrastructure failure in which a cybersecurity cause is suspected but not

confirmed.

• Third-party issue: cloud provider, data center, or vendor incident affecting the organization.

Templates can be combined or reused for hybrid cases, such as a third-party ransomware event.

The categorization here serves as an example list rather than an exhaustive taxonomy.

Organizations may have additional messaging template categories based on their industry,

regulatory environment, and risk profile.

REGULATORY NOTIFICATION REQUIREMENTS

Many regulatory frameworks impose specific notification requirements following security incidents.

These requirements vary by jurisdiction, industry, and the nature of data involved. Organizations

should document applicable notification requirements during preparation and incorporate them into

the emergency communication plan.

Common regulatory frameworks with notification requirements include:

• GDPR: Requires notification to supervisory authorities within seventy-two hours of becoming

aware of a personal data breach, and notification to affected individuals when the breach is likely

to result in high risk to their rights and freedoms.

• HIPAA: Requires covered entities to notify affected individuals, HHS, and in some cases the media

following breaches of unsecured protected health information.

• State Breach Notification Laws : Most U.S. states have breach notification laws with varying

requirements for timing, content, and notification recipients.

• SEC Cybersecurity Rules: Requires public companies to disclose material cybersecurity incidents

within four business days of determining materiality.

• PCI DSS : The Payment Card Industry Data Security Standard (PCI DSS) requires organizations

that process, store, or transmit cardholder data to report suspected or confirmed breaches to

their acquiring bank and payment card brands. [7]

Forensic investigation by a PCI Forensic

Investigator (PFI) is typically required, and organizations may face penalties or lose the ability to

process card payments if they fail to comply.

• NIS2: The Network and Information Security Directive (NIS2) requires essential and important

entities in the EU to notify the relevant national authority of significant incidents within twenty-four hours of becoming aware, with a full incident report due within seventy-two hours. [8]

• DORA: The Digital Operational Resilience Act (DORA) requires financial entities in the EU to

classify and report major ICT-related incidents to their competent authority, with initial

notification, intermediate reports, and a final report including root cause analysis. [9]

• CRA: The Cyber Resilience Act (CRA) applies to manufacturers, importers, and distributors of

products with digital elements placed on the EU market. Manufacturers are required to report

actively exploited vulnerabilities and severe product-security incidents to two external entities:

the European Union Agency for Cybersecurity (ENISA) and a designated coordinating Computer

Security Incident Response Team (CSIRT). Reporting is staged across four deadlines: an early

warning within twenty-four hours, a detailed notification within seventy-two hours, and a final

vulnerability report within fourteen days or a final incident report within one month. [10]

Reporting

obligations apply from September 2026, with full CRA requirements in force from December 2027.

This list is not exhaustive. Organizations operating in multiple jurisdictions or regulated industries

may face additional notification obligations. Legal counsel should review all applicable notification

requirements to ensure the emergency communication plan addresses each one.

The ECP can directly impact the organization’s reputation and stakeholder confidence following an incident.

For example, consider the 2025 PowerSchool data breach.

PowerSchool is a widely used student information system (SIS) platform that manages sensitive data for

millions of students and educators across the United States and Canada. In December 2024, an attacker

used a compromised credential on PowerSchool’s customer support portal to exfiltrate personal data for

approximately 62 million students and 9.5 million educators across 6,505 U.S. school districts. PowerSchool

made an incomplete notification of the breach ten days after detection, with some districts learning about

the breach from news coverage before receiving formal communication from PowerSchool. PowerSchool

did not disclose details about the specific data that was compromised, leaving thousands of school

administrators to independently draft parent notifications with incomplete and inconsistent information. A

timeline of the breach, including subsequent details regarding the investigation and extortion attempts, is

provided in Table 6.

Table 6 | PowerSchool Breach Communication Timeline

DATE EVENT

Dec 19, 2024 Attacker begins exfiltrating student and educator data from PowerSchool’s

customer support portal.

Dec 28, 2024 PowerSchool detects the breach (9 days after exfiltration began).

Late Dec 2024 PowerSchool pays approximately $2.85 million in ransom and receives a video

that purported to show data deletion.

DATE EVENT

Jan 7, 2025 PowerSchool makes an incomplete disclosure of the breach, 10 days after

detection.

Jan 13, 2025 PowerSchool publishes a public incident page on its website.

Late Jan 2025 PowerSchool begins sending notification emails to affected individuals.

Mar 10, 2025 CrowdStrike investigation reveals earlier unauthorized access dating back to

August 2024, over 100 days before the main exfiltration.

May 7, 2025 Attackers begin extorting school districts directly using samples of the stolen

data, proving that PowerSchool’s deletion assurance was false.

The breach exposed sensitive records, including special education status, mental health information,

custody alerts, and medication schedules, with some districts discovering that decades of historical student

data had been compromised. PowerSchool’s communication failures point to a pattern of missing ECP

elements: no pre-built notification for downstream organizations, no coordinated communication toolkits

for districts to use with parents, and no protocol for communicating ransom decisions with appropriate

transparency. This lack of preparation was costly for PowerSchool, not only in the ransom payment but also

in lost trust and reputational damage, leading several customers to leave PowerSchool for competitor

platforms after the breach. [11]

“[North Carolina Superintendent of Public Instruction Maurice] Green said the state’s contract with

PowerSchool ends in July, and officials have chosen to migrate to competitor Infinite Campus, in part

because of its promise of better cybersecurity practices.

Organizations that manage data on behalf of others should develop communication plans that account for

regulatory disclosure requirements and the needs of downstream stakeholders, including comprehensive

notification, coordinated messaging, and accurate scoping of compromised data. Investing in these plans

before an incident occurs is far less costly than rebuilding trust after a poorly managed disclosure.

Together, these components, communication channels, contact information, external reporting channels,

reporting procedures, and the emergency communication plan, form the organization’s incident

communications plan. Maintaining them in a single, governed document ensures that updates to one

component (such as a new regulatory notification requirement) are reflected alongside the others. Assign

ownership of the plan to a specific role, review it at least annually, and validate it during tabletop exercises

to confirm that it remains coherent, consistent, concise, and appropriately tailored to each audience.

Establish the Incident Response Team

The incident response team (IRT) serves as the organization’s primary resource for detecting, analyzing, and

Organizations can structure their incident response capabilities in several ways depending on size,

resources, and risk profile. Smaller organizations may designate incident response as an additional

responsibility for existing IT or security staff. Larger organizations may maintain dedicated incident

response teams with specialized roles.  Some organizations augment internal capabilities with managed

security service providers (MSSPs) or incident response retainer agreements that provide access to external

expertise when needed.

Document the team structure, including primary and backup personnel. Ensure contact information is up-to-date and accessible across multiple channels. Define escalation paths for situations requiring additional

resources or management decisions.

VIRTUAL VS DEDICATED INCIDENT RESPONSE TEAMS

Many organizations operate virtual (or soft) incident response teams in which members have incident

response as a secondary responsibility alongside their primary roles. Dedicated (or hard) teams assign

members to incident response as their primary function. Some organizations combine both

approaches, maintaining a small dedicated on-call group that is augmented by a wider virtual team

when incidents require additional capacity. Virtual teams maximize resource efficiency but create

challenges during active incidents, when team members need to balance competing priorities.

Virtual teams benefit from establishing clear activation procedures that temporarily reassign team

members from normal duties during significant incidents. Work with management to pre-approve

these temporary reassignments so activation can proceed without delay during incident response.

Document the conditions that trigger team activation and the expected duration of reassignment for

different incident severity levels.

Identify a Platform for Incident Tracking

During an incident, the response team will need to track its progress, record decisions made during the

response, and document the evidence collected. While this can be done manually, most organizations will

benefit from an incident-tracking platform for centralized, collaborative incident management.

An incident tracking platform is a tool that allows the team to record and track incidents from initial

detection through resolution. These platforms often include features such as:

• Incident categorization and prioritization

• Analyst assignment and activity tracking

• Incident status reporting

• Incident response playbook execution tracking

• Incident response documentation and evidence collection

These features help the incident response team maintain situational awareness and accountability

throughout the response effort.

Many organizations will repurpose existing ticketing systems for incident response tracking.  This can be a

reasonable approach, as long as the ticketing system is configured to support the incident response process

and is accessible to the team during an incident. Platforms such as JIRA, ServiceNow, or Zendesk can be

configured to support incident response tracking, as desired.

Alternatively, organizations might consider purpose-built incident management platforms. These platforms

are specifically designed for incident response needs and often include features such as automated incident

categorization, integration with threat intelligence feeds, and collecting and reporting on incident metrics.

Some options for commercial, purpose-built platforms for incident management include DFIR-IRIS,

Incident.io, and SmartSOAR.

For some organizations, a shared document or spreadsheet may be sufficient for incident

tracking, particularly if the organization has a low volume of incidents or limited resources.

Consider creating a spreadsheet template that includes fields for incident details, status,

assigned personnel, and other notes, then copying it as the starting point for each new

incident.

STANDARDIZED VOCABULARY WITH MITRE ATT&CK

Clarity in incident documentation is important for effective communication during an incident and

for post-incident analysis. Inconsistent terminology and varying definitions are common challenges

in cybersecurity, where different teams may use different names for the same attacker behavior. This

lack of standardization can lead to confusion and miscommunication, particularly when coordinating

across internal teams or with external partners.

The MITRE ATT&CK framework provides a widely adopted taxonomy of adversary tactics, techniques,

and procedures that serves as a common language for the cybersecurity community. [12]

While MITRE

ATT&CK offers extensive capabilities for threat modeling, detection engineering, and adversary

simulation (covered later in this chapter), one of its most practical benefits for incident tracking is

vocabulary standardization. When analysts describe attacker activity using ATT&CK technique

identifiers (such as T1059 for Command and Scripting Interpreter or T1078 for Valid Accounts), the

terminology is unambiguous and consistent regardless of who is writing the report.

Figure 32 | MITRE ATT&CK Framework Website Technique Identifier

Adopting ATT&CK terminology in the incident tracking platform improves documentation quality and

enables structured analysis. Incident records tagged with ATT&CK techniques can be searched,

behavior and measure detection coverage over time. When evaluating incident-tracking platforms,

consider the ability to categorize incidents using ATT&CK tactics and techniques.

Account for Cyber Insurance Requirements

Many organizations carry cyber insurance policies, but these policies are frequently purchased by risk

management or finance teams without direct involvement from the cybersecurity group. This creates a

situation in which the incident response team is bound by contractual requirements they had no input on,

discovering insurance policy constraints only when an incident forces them to engage with the carrier

(sometimes called the insurer). During incidents, the carrier’s requirements can substantially influence

response decisions, including which IR firms to engage, when law enforcement is notified, and how breach

notification is scoped.

The carrier’s financial interest in minimizing claim costs can conflict with the organization’s need for

thorough investigation and complete remediation.  Most policies insert a breach coach (a carrier-appointed

attorney) into the response chain to direct the engagement, select vendors, and control the flow of

decisions. Some policies deny or reduce coverage if the organization engages non-panel IR vendors, and

others require the carrier to be notified before law enforcement or external IR teams are contacted.

Performing response actions in the wrong sequence can put reimbursement at risk during the most critical

early hours of an incident.

Figure 33 | Travelers Insurance Cyber Coach Promotional Article [13]

The insurance carrier’s financial interest in minimizing claim costs can conflict with the

organization’s need for thorough investigation and complete remediation.

To avoid these conflicts during an active incident, integrate cyber insurance into incident response planning

proactively:

• Obtain and review the policy : Request a copy of the cyber insurance policy from the risk management

or finance team and review it with the IR team. Ensure the incident response plan aligns with the

policy’s notification timelines, pre-approval requirements, vendor restrictions, and coverage exclusions

(such as social engineering, acts of war, or failure to maintain security controls).

• Negotiate vendor preferences early : Organizations with established relationships with IR firms should

negotiate to add those firms to the carrier’s approved vendor panel when the policy is written or

renewed, not during an active incident.

• Include the policy owner on the IRT : The person responsible for the cyber insurance policy should be

identified in the incident response team contact list and included in tabletop exercises.

• Maintain offline access : Keep a copy of the cyber insurance policy, including the carrier’s contact

information and claims procedures, available outside the primary network. Incidents that limit access to

network resources can make policy details inaccessible exactly when they are needed most. The offline

documentation should include the carrier’s claims phone number, the policy number and authorization

details needed to activate coverage.

• Protect the policy from disclosure : Do not store the cyber insurance policy on systems accessible to

attackers, and do not share policy details during ransom negotiations. Attackers who learn the coverage

limits can calibrate their demands accordingly, and disclosure of the policy to unauthorized parties can

void coverage.

• Engage independent legal counsel : The carrier’s breach coach represents the carrier’s interests.

Organizations should involve their own legal counsel in decisions about regulatory notification and

disclosure scope where the carrier’s interest in minimizing costs may not align with the organization’s

legal obligations.

The risk of an incomplete investigation can far exceed the short-term cost savings that a carrier-directed

response might prioritize. Organizations that integrate cyber insurance into their preparation activities can

coordinate effectively with carriers while advocating for the thorough investigation and remediation their

environment requires.

Many cyber insurance policies include pre-breach services that policyholders rarely use,

such as tabletop exercises, vulnerability assessments, and incident response plan reviews.

Ask the carrier or broker what policyholder services are available, and use carrier-facilitated tabletop exercises to build relationships with panel providers before a real

incident occurs.

CYBER SAFE HARBOR LEGISLATION

A growing number of U.S. states have enacted cyber safe harbor laws that provide organizations with

an affirmative legal defense against certain claims following a data breach, provided the organization

demonstrates compliance with a recognized cybersecurity framework. [14]

Figure 34 | Cybersecurity Safe Harbor Laws in the United States

These laws recognize frameworks, including the NIST Cybersecurity Framework, CIS Critical Security

Controls, ISO 27001, and others, as evidence of reasonable cybersecurity practices. For example, the

Texas Cybersecurity Safe Harbor Law (SB 2610), effective September 2025, provides protection from

punitive damages (monetary penalties imposed by courts beyond actual losses to punish negligent

behavior) for small and mid-sized businesses that implement and maintain a qualifying cybersecurity

program.

For incident response teams, safe harbor legislation provides an additional justification for

investment in preparation. Demonstrating compliance with a recognized framework not only

strengthens the organization’s security posture but can also provide legal protection that can reduce

exposure following an incident. Organizations should work with legal counsel to understand which

safe harbor provisions apply in their jurisdictions and ensure their cybersecurity programs meet the

qualifying criteria.

Implement Security Awareness Training

Security awareness training transforms employees from potential vulnerabilities into active participants in

the organization’s security posture. Well-trained employees can serve as an early detection layer,

recognizing and reporting suspicious activities that technical controls might miss.

Effective security awareness programs address multiple objectives relevant to incident response:

• Incident recognition: Employees should understand what constitutes a security incident and recognize

common indicators such as phishing attempts, unusual system behavior, or unauthorized access

requests.
