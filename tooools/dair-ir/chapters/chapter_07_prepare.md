# Chapter 7: Prepare Activity: Visibility & Telemetry

> Source: PDF Pages 90-161 (Total Pages: 72)

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

affected and the potential impact on the organization.

For example, if we identify a phishing email as the initial vector of attack, we can use the domain name of

the phishing lure to determine any other systems that may have been involved in the attack. This insight

allows us to better understand the breadth of the incident and identify the systems involved that require

additional investigation.

RESPONSE ACTIONS LOOP

A Dynamic Approach to Incident Response | Chapter 6 | 67

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

In many ways, the DAIR model does not significantly deviate from the PICERL or the NIST SP 800-61

models, continuing to embrace the important elements of incident response that have been developed over

time and proven to be effective for many organizations. Rather, it helps us to reshape the existing models

while identifying important additional considerations. The DAIR model allows us to apply the same phases

to more effectively prepare for, identify, respond to, and review the effectiveness of the incident response

function.

Next, we’ll look at each of the important waypoints in the DAIR model in more detail.

A Dynamic Approach to Incident Response | Chapter 6 | 69

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

Prepare Activity | Chapter 7 | 71

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

development can be challenging and requires significant time and effort. By supplying the decision-

maker with well-considered options, incident response leads can help minimize the time and effort

required to develop the policies that are a necessary element of effective incident response.

Develop Organizational Policies

Organizational policies are an essential tool for guiding the organization’s incident response approach.

When responding to an incident, technical analysts and managers are often asked to make decisions with

significant implications for the organization. Policies and guidance on how to respond to incidents should

be developed in advance to ensure the organization is prepared to respond effectively.

Policies are most effective when they are clear, concise, and easy to understand. They should be developed

in collaboration with relevant stakeholders and approved by organization leadership to provide the

necessary authority for the incident response team to make decisions and act in accordance with the

policies.

Policies are developed to set the expectations for how responders should act during an

incident. A clear policy that is well-communicated and understood by the team will be the

easiest to follow during an incident when responders are under pressure.

Some organizations may wish to develop a single policy that covers all aspects of incident response, while

others may prefer to develop separate policies for different areas. A single policy is sometimes easier to

Prepare Activity | Chapter 7 | 73

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

[2]

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

Organizations can also leverage AI platforms to assist with drafting incident response policies and

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

Prepare Activity | Chapter 7 | 75

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

Other organizations may prefer more specific risk assessment criteria that provide detailed guidance

for responders. This form of risk-criticality assessment is better presented in a decision tree or

flowchart format that guides responders through a series of questions to arrive at a risk classification,

similar to the CISA Incident Scoring rubric.

Prepare Activity | Chapter 7 | 77

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

Prepare Activity | Chapter 7 | 79

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

actions disrupt communications. Network isolation measures that block external traffic can cut off cloud-

based platforms like Slack or Microsoft Teams, leaving the response team without its primary coordination

tool during active response. The backup platform should use independent authentication, separate from the

organization’s primary directory (such as Active Directory or Entra ID). If domain administrator accounts

are compromised, an attacker who controls the directory may also have access to any platform that

authenticates against it, including the backup communications channel.

Document Contact Information

As part of the prepare activity, document contact information for the people who will be involved in the

incident response process. Consider filling out a contact information template that includes the following

information for each stakeholder. An example template is provided in Table 4.

Table 4 | Contact Information Template

IRT Contact Information Template

Incident Response Role UNIX specialist

Name Joshua Wright

Title Senior Systems Administrator

Prepare Activity | Chapter 7 | 81

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

$ curl -q https://www.microsoft.com/.well-known/security.txt

# Our security acknowledgements page

Acknowledgments: https://msrc.microsoft.com/update-guide/acknowledgement

# Canonical URI

Canonical: https://www.microsoft.com/.well-known/security.txt

# Our Researcher Portal

Contact: https://msrc.microsoft.com/report/vulnerability/new

# Our PGP Key

Encryption: https://msrc.microsoft.com/.well-

known/csaf/openpgp/998D7EC1A516E3D17FF90480EF148D3CDE714E0D.asc

Expires: 2026-09-23T16:00:00.000Z

# Our Bounty policy

Policy: https://www.microsoft.com/en-us/msrc/bounty/

# Our Coordinated Vulnerability Disclosure Policy

Policy: https://www.microsoft.com/en-us/msrc/cvd

# Our Bounty Legal Safe Harbor Policy

Policy: https://www.microsoft.com/en-us/msrc/bounty-safe-harbor

# Our Common Security Advisory Framework (CSAF) publications

CSAF: https://msrc.microsoft.com/csaf/provider-metadata.json

Preferred-Languages: en

Publishing a security.txt file is only half the work: the contact address it advertises should route to the

security team, not to a generic help desk queue or unmonitored inbox. Organizations should document

internal routing so that external disclosures reach analysts who can assess them promptly. The effort

required to create and maintain this file pays off when it accommodates disclosure efforts that inform

internal cybersecurity teams, often providing the earliest notice that a compromise has occurred.

Establish Reporting Procedures

Throughout the incident, the incident response team will need to report its status to a variety of

stakeholders. By establishing reporting procedures in advance, the team can ensure that the necessary

information is communicated effectively and efficiently.

Consider developing incident response reporting guidelines in the IR plan that capture important details for

the organization while providing clear, concise guidance to the team. These reporting guidelines should

Prepare Activity | Chapter 7 | 83

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

Prepare Activity | Chapter 7 | 85

within four business days of determining materiality.

• PCI DSS : The Payment Card Industry Data Security Standard (PCI DSS) requires organizations

that process, store, or transmit cardholder data to report suspected or confirmed breaches to

their acquiring bank and payment card brands. [7]

Forensic investigation by a PCI Forensic

Investigator (PFI) is typically required, and organizations may face penalties or lose the ability to

process card payments if they fail to comply.

• NIS2: The Network and Information Security Directive (NIS2) requires essential and important

entities in the EU to notify the relevant national authority of significant incidents within twenty-

four hours of becoming aware, with a full incident report due within seventy-two hours. [8]

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

responding to security incidents. Establishing the team structure, roles, and responsibilities during

preparation ensures clear accountability when incidents occur.

Prepare Activity | Chapter 7 | 87

Organizations can structure their incident response capabilities in several ways depending on size,

resources, and risk profile. Smaller organizations may designate incident response as an additional

responsibility for existing IT or security staff. Larger organizations may maintain dedicated incident

response teams with specialized roles.  Some organizations augment internal capabilities with managed

security service providers (MSSPs) or incident response retainer agreements that provide access to external

expertise when needed.

Document the team structure, including primary and backup personnel. Ensure contact information is up-

to-date and accessible across multiple channels. Define escalation paths for situations requiring additional

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

correlated, and compared across incidents, helping the organization identify patterns in attacker

Prepare Activity | Chapter 7 | 89

behavior and measure detection coverage over time. When evaluating incident-tracking platforms,

consider the ability to categorize incidents using ATT&CK tactics and techniques.

Account for Cyber Insurance Requirements

Many organizations carry cyber insurance policies, but these policies are frequently purchased by risk

management or finance teams without direct involvement from the cybersecurity group. This creates a

situation in which the incident response team is bound by contractual requirements they had no input on,

discovering insurance policy constraints only when an incident forces them to engage with the carrier

(sometimes called the insurer). During incidents, the carrier’s requirements can significantly influence

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

Ask the carrier or broker what policyholder services are available, and use carrier-

facilitated tabletop exercises to build relationships with panel providers before a real

incident occurs.

CYBER SAFE HARBOR LEGISLATION

A growing number of U.S. states have enacted cyber safe harbor laws that provide organizations with

an affirmative legal defense against certain claims following a data breach, provided the organization

demonstrates compliance with a recognized cybersecurity framework. [14]

Ohio enacted the first such

law in 2018, followed by Utah, Connecticut, Iowa, Oregon, Tennessee, and Texas. Florida and West

Virginia legislators passed cyber safe harbor bills in 2024, but the governors of states vetoed them.

Prepare Activity | Chapter 7 | 91

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

• Reporting procedures : Every employee should know how to report suspected security incidents,

including who to contact and what information to provide. Clear, accessible reporting channels

encourage prompt notification.

• Social engineering resistance: Training should cover common social engineering techniques, including

phishing, pretexting, and baiting. Employees who understand these tactics are less likely to fall victim to

them.

• Data handling : Employees should understand data classification requirements and proper handling

procedures for sensitive information. This knowledge reduces the likelihood of accidental data

exposure.

Training effectiveness improves when programs include practical exercises rather than relying solely on

passive content consumption. Simulated phishing campaigns, for example, provide measurable feedback on

employee awareness while identifying individuals who may benefit from additional training.

Coordinate security awareness training with the incident response team. When employees

report suspected incidents, even if they turn out to be false alarms, recognize and thank

them for their vigilance. This positive reinforcement encourages continued reporting and

demonstrates that reports are valued.

Prepare the Incident Response Team

Preparing the incident response team involves developing the skills, tools, relationships, and processes that

enable effective response when incidents occur. This preparation ensures that team members can act

decisively under pressure, collaborate effectively with other departments, and execute response activities

with confidence. Where the previous section focused on organizational structure and policy, the activities

here bridge people, process, and technology: training the team, building playbooks, and assembling the tools

and access needed for response operations.

Train the Incident Response Team

Technical competence forms the foundation of effective incident response. Team members should possess

the skills necessary to detect threats, collect evidence, analyze attacker activity, and execute containment

and eradication actions. Training programs should address both foundational skills and advanced

techniques appropriate to each team member’s role.

Core technical training areas for incident responders include:

• Security Orchestration, Automation, and Response (SOAR) : Familiarity with SOAR platforms to

automate repetitive tasks, orchestrate workflows, and manage incident response processes.

• Digital forensics : Evidence collection, preservation, and analysis across Windows, Linux, and cloud

environments. Understanding file systems, registry analysis, memory forensics, and timeline

construction.

• Network analysis: Packet capture analysis, network flow interpretation, and identification of command-

and-control communications.  Familiarity with tools like Wireshark, Zeek, and network detection

platforms.

• Malware analysis : Basic static and dynamic analysis techniques for understanding malicious code

Prepare Activity | Chapter 7 | 93

behavior. Safe handling procedures for malware samples.

• Log analysis: Proficiency with SIEM platforms, log parsing, and correlation techniques. Understanding

of common log formats and their investigative value.

• Scripting and automation : Ability to automate repetitive analysis tasks and develop custom tools for

specific investigation needs. Python, PowerShell, and UNIX shell scripting are particularly valuable.

• Leadership and negotiation : Ability to lead cross-functional response efforts and communicate

effectively with executives and stakeholders who may not share the responder’s technical background.

Together, these training areas equip responders with the breadth of skills needed to investigate incidents

across diverse environments.

Beyond technical skills, incident responders benefit from training in communication, documentation, and

decision-making under pressure. These soft skills often differentiate effective responders from those who

struggle during high-stress incidents.

Training should be ongoing rather than a one-time event. The threats that organizations

face are constantly evolving, and responders should regularly update their skills to address

new attack techniques and tools. Budget for annual training and conference attendance to

maintain team capabilities.

Develop and Validate System Backup and Recovery Procedures

Backup and recovery capabilities directly impact the organization’s ability to recover from incidents,

particularly ransomware attacks that encrypt or destroy data, as well as other non-malicious incidents, such

as hardware failures or accidental deletions. Preparation should ensure that backups exist, are protected

from compromise, and can be restored within acceptable timeframes.

Start by documenting the current backup architecture and organizational requirements. Identify what

systems and data are backed up, along with the frequency and retention periods for each. Document backup

storage locations, whether on-premises, cloud-based, and/or at off-site facilities. Identify the access

controls and authentication requirements that protect backup systems. Establish recovery time objectives

(RTO) and recovery point objectives (RPO, the maximum acceptable data loss between backups) for critical

systems to define acceptable restoration timeframes.

Evaluate backup resilience against common attack scenarios. Modern ransomware operators specifically

target backup infrastructure to maximize leverage over victims. Assess whether backups would remain

intact if an attacker gained privileged access to backup systems. Implement protections such as:

• Immutable backups : Configure backup storage to prevent modification or deletion for a defined

retention period, even by administrators (this is a common feature of cloud-based storage platforms).

• Air-gapped copies : Maintain offline backup copies that cannot be reached through network

connectivity.

• Separate authentication : Use credentials for backup systems that are distinct from the production

identity environment.

• Backup integrity monitoring : Implement monitoring to detect unauthorized access or modification

attempts against backup infrastructure.

• Notifications for backup failures: Ensure that backup failures trigger alerts to responsible personnel for

timely resolution.

Combining these protections creates a layered defense for backup infrastructure that can withstand

targeted attacks against recovery capabilities.

Many ransomware incidents involve attackers disabling backup systems and waiting for

old backups to age out before demanding ransom. Several high-profile ransomware

campaigns have disabled backup systems without the victim organization’s knowledge.

Notifications for backup failures should be sent to multiple recipients and escalated if not

addressed promptly.

Regular restoration testing validates that backup investments deliver actual recovery capability. Schedule

periodic restoration tests that measure actual recovery times against RTO targets and verify data

completeness against RPO expectations. Document test results and address any gaps identified.

THE 3-2-1-1 BACKUP RULE

The traditional 3-2-1 backup rule recommends maintaining three copies of data on two different

media types, with one copy stored off-site. For ransomware resilience, extend this rule to 3-2-1-1: add

an additional immutable or air-gapped copy that cannot be deleted or manipulated via network

connectivity or compromised credentials.

Figure 35 | Backup System with Immutable Copy

This additional copy serves as the last line of defense when attackers compromise both backup

infrastructure and production systems. Organizations that lack immutable backups often find

themselves choosing between paying ransom and accepting total data loss.

Cultivate Relationships with Essential Personnel

Incident response rarely occurs in isolation. Effective response requires collaboration across departments,

each contributing specialized expertise to the overall effort. Establishing relationships with essential

personnel before incidents occur enables smoother coordination during response.

Identify important contacts in departments that commonly participate in incident response:

• Business unit leaders : Managers who can assess business impact and authorize operational decisions

affecting their areas.

• Essential stakeholders: System owners and application managers responsible for affected systems.

• Security Operations Center (SOC) : Analysts who monitor for threats and may provide initial detection

and triage support.

Prepare Activity | Chapter 7 | 95

• IT Operations : System administrators, network engineers, and database administrators who maintain

the systems that may be compromised or needed for investigation.

• Help desk : Front-line support staff who often receive initial reports of suspicious activity from end

users.

• Legal counsel : Attorneys who advise on evidence handling, regulatory obligations, and litigation

considerations.

• Human resources : HR personnel who provide insight and direction when incidents involve insider

threats or employee-related investigations.

• Public relations : Communications professionals who manage external messaging during significant

incidents.

Build relationships through regular interaction. rather than waiting for incidents to force collaboration.

Include key contacts in tabletop exercises, share relevant threat intelligence that affects their areas, and

seek their input during preparation. When incidents occur, these established relationships facilitate faster

coordination and reduce friction during high-stress situations.

CLARIFYING ROLES WITH A RACI MATRIX

A RACI matrix clarifies who is responsible for what during an incident response, reducing confusion

when multiple teams collaborate under pressure. RACI defines four levels of involvement for each

activity:

• Responsible: The person or team who performs the work.

• Accountable: The individual who has final authority and answers for the outcome (only one

person per activity).

• Consulted: Those whose input is sought before decisions are made (two-way communication).

• Informed: Those who are kept updated on progress or decisions (one-way communication).

Table 7 | Sample RACI Matrix for Incident Response Activities

ACTIVITY IR LEAD SOC IT OPS LEGAL HR COMMS

Initial detection and triage A R C I I I

Containment decisions R/A C R C I I

Evidence preservation R/A R C C I I

System recovery A I R I I I

External communications C I I C I R/A

Employee-related actions C I I C R/A C

The table above is a simplified example. Organizations should expand their RACI matrix to include

additional groups relevant to their environment, such as executive leadership, regulators, affected

business units, cyber insurance contacts, and third-party incident response providers.

Organizations that develop a RACI matrix during preparation and validate it through tabletop

exercises benefit from clearer role definitions during actual incidents. When an incident occurs,

participants already understand their responsibilities and can focus on execution rather than

negotiating roles.

Review and update the matrix annually or when organizational changes affect incident response

responsibilities.

Document Incident Response Decision Authority

A RACI matrix clarifies who participates in each activity, but it does not specify who can authorize the most

consequential decisions during a response. An incident response authority matrix fills this gap by naming

the role with authority to make each major decision, identifying a delegate when the primary authority is

unavailable, and specifying the documentation each decision should produce.

RACI and the authority matrix complement each other. RACI covers staffing and coordination across

activities. The authority matrix covers decision rights and the evidence each decision leaves behind.

Authority matrices are valuable during high-pressure incidents, when decisions about containment, scope

expansion, or external notification need to happen quickly without ambiguity about who can sign off. They

also serve as compliance evidence for the CSF 2.0 Govern function, where assessors expect to see named

decision authorities rather than generic role descriptions.

A sample matrix covering eight common incident response decisions appears in Table 8.

Table 8 | Sample Incident Response Authority Matrix

DECISION AUTHORITY DELEGATE DOCUMENTATION REQUIRED

Incident declaration Incident Commander Senior analyst on

duty

Incident ticket with

declaration timestamp and

rationale

Containment action

with material

business impact

Incident Commander

with business unit

head concurrence

CISO if Incident

Commander is

unavailable

Containment decision record

with business impact

assessment

Scope expansion to

additional business

units

Incident Commander

with notification to

CISO

None Scope expansion log entry

with trigger rationale

Response Actions

Loop exit, technical

closure

Incident Commander

based on eradication

validation

Senior analyst with

Incident

Commander’s written

approval

Signed loop exit checklist

Response Actions

Loop exit, residual

risk acceptance

CISO or designated

risk owner

Board-level executive

for significant

incidents

Signed risk acceptance

record with residual risk

description

Regulatory

notification,

decision to notify

Legal counsel with

CISO

General Counsel Notification decision log with

timeline and regulator

identified

Prepare Activity | Chapter 7 | 97

DECISION AUTHORITY DELEGATE DOCUMENTATION REQUIRED

Post-incident

improvement,

ownership

Incident Commander

from declaration

through debrief

closure, then

Security Program

Manager

None Improvement register with

named owners and milestone

dates

Media or public

communications

Communications lead

with Legal sign-off

CEO for material

incidents

Approved statement with

version control and

distribution record

This sample uses common role names, which organizations should adapt to match their actual structure.

The value of the matrix lies in two places: removing ambiguity about who can authorize each decision, and

specifying what documentation each decision generates so the record exists for both audit review and post-

incident debrief.

Review and update the matrix when organizational changes affect decision authority, and validate it through

tabletop exercises so the documented chain of authority matches what happens in practice.

Develop Playbooks for Common Incidents

Playbooks are an essential tool for incident response teams. When responding to an incident, stress levels

are often high, the incident details can be chaotic and initially misunderstood, and analysts often have

multiple tasks to complete in a short period of time. Playbooks provide a structured approach to incident

response, outlining the steps to take for a specific incident type.

Effective playbooks share several characteristics:

• Actionable steps: Each step should be specific enough that a trained responder can execute it without

additional research.

• Decision points: Include decision trees that guide responders through common scenarios.

• Tool references : Specify which tools to use for each step, including command-line syntax where

applicable.

• Communication triggers : Identify when to notify stakeholders, escalate to management, or involve

external parties.

• Documentation requirements: Specify what evidence to collect and how to document actions taken.

Playbook development is an ongoing, iterative process. Playbooks are not intended to be static documents.

They should evolve based on lessons learned from actual incidents and changes in the threat landscape.

Develop playbooks for incident types most likely to affect the organization, starting from an IOC to give

responders a clear starting point for investigation. Some publicly available playbooks include:

• CERT Societe Generale Incident Response Methodologies : A collection of incident response

methodologies, including playbooks for various incident types in English, Spanish, French, and Russian.

• Sudhakara Raju’s Playbooks : A collection of playbooks for data loss, malware, phishing, compromised

accounts, and more.

• CISA’s Cybersecurity Incident and Vulnerability Response Playbooks : A set of US Federal Government

playbooks for several incident types.

• Mike Lamb’s Playbooks: A collection of playbooks for Amazon Elastic Kubernetes Service , Amazon

Elastic Container Service, Citrix, and VMware ESXi.

• Jai Minton’s DFIR Cheat Sheet : A collection of scripts and manual investigation steps for investigating

the compromise of Microsoft Windows systems.

See Section 16.4.1 for information on using AI to help generate playbooks for specific IOCs.

Figure 36 | Sample Incident Response Playbook

Review and update playbooks after each incident where they were used and after each exercise where they

were tested. Document what worked well, what was missing, and what could be improved. This continuous

improvement process ensures playbooks remain relevant and effective.

Prepare Resources for Response Actions

The incident response team requires access to a range of tools and resources to respond effectively to

incidents. These tools provide the technical capabilities needed to contain systems, collect data, investigate

threats, eradicate them, and recover effectively.

Forensic Workstations

Dedicated analysis systems configured with investigation tools and isolated from production networks.

Forensic workstations should have sufficient processing power and storage to handle large evidence files,

memory dumps, and disk images. Maintain both Windows and Linux analysis environments to support

investigations across different system types. Where appropriate for the organization, maintain additional

Prepare Activity | Chapter 7 | 99

platforms that match the environment’s operating system (macOS, other UNIX platforms, cloud instances,

etc.). For organizations with significant cloud infrastructure, consider deploying cloud-based forensic

workstations that place analysis capability close to the data, reducing the time required to transfer large

evidence sets for analysis.

Evidence Collection Tools

Software for acquiring forensic images and volatile data from compromised systems.  This includes memory

acquisition tools like WinPMEM and LiME, disk imaging tools, and endpoint collection agents. Ensure tools

are tested and readily accessible when needed.

Analysis Tools

Software for examining collected evidence, including:

• Timeline analysis tools (Plaso, log2timeline).

• Memory analysis frameworks (Volatility, MemProcFS).

• Disk and artifact forensics tools (Autopsy, X-Ways, FTK, Magnet AXIOM).

• Log analysis and SIEM platforms.

• Network traffic analysis tools (Wireshark, Zeek).

• Endpoint detection and response (EDR), extended detection and response (XDR), and endpoint

protection platform (EPP) consoles for host-level telemetry and response actions.

• Cloud Security Posture Management (CSPM) platforms for visibility into cloud configuration changes

and policy violations.

Beyond dedicated forensic tools, organizations should also identify existing security and operational tools

that provide investigative value. Data Loss Prevention (DLP) platforms, for example, often contain detailed

records of file movements and data transfers that can be valuable during scoping and evidence analysis.

Analysts should be familiar with these tools before incidents occur, as learning new tools during an active

response slows investigation progress.

Evidence Storage

Secure storage for forensic images and artifacts with appropriate access controls, integrity verification, and

retention management. Ensure evidence storage availability meets the needs of worst-case scenarios for

data volume and retention duration.

Jump Bag/Go Kit

Portable incident response equipment for on-site investigations. Include bootable USB drives with forensic

tools, write blockers, portable storage, network cables, and documentation templates.

COMMERCIAL VS. OPEN-SOURCE FORENSIC TOOLS

Organizations should decide whether to invest in commercial forensic tools or rely on open-source

alternatives. Each approach has tradeoffs.

Commercial tools like EnCase, FTK, and X-Ways offer polished interfaces, vendor support, and

established credibility in legal proceedings. However, they require significant licensing investment

and may limit flexibility.

Open-source tools like Autopsy, Volatility, and Plaso offer powerful capabilities without licensing

costs and enable customization for specific needs. However, they may require more expertise to

operate effectively and often lack formal support channels.

Many organizations adopt a hybrid approach, using commercial tools for primary investigations while

leveraging open-source tools for specific analysis needs and automation. Regardless of tool selection,

ensure analysts are trained and proficient with the tools before incidents require their use.

Prepare Access to Systems

Responders need rapid access to systems for investigation, containment, and eradication. Waiting for

access approvals during an active incident wastes critical time and allows attackers to extend their foothold.

Preparation ensures that access mechanisms are in place and that responders can obtain the necessary

privileges without delay.

Start by establishing break-glass accounts for emergency access. These accounts provide elevated

privileges when normal access methods are unavailable or compromised. Secure break-glass credentials

with hardware tokens or a secured credential vault, so they are accessible only with the appropriate

organizational approval. Configure alerting for any use of these accounts, and test them periodically to

verify they function when needed.

Access preparation should balance response speed with security. Break-glass accounts

and elevated privileges pose a significant risk if misused. Implement controls, including

monitoring, multi-person authorization for sensitive actions, and regular access reviews, to

guard against and identify potential misuse.

Next, document access procedures that responders can follow during incidents. Identify who can authorize

investigative access to production systems and how to request access after hours or during emergencies.

Clarify procedures for accessing systems owned by different business units, as well as cloud environments

and third-party services. Make these procedures accessible to the team before incidents occur.

Finally, document procedures for obtaining support from cloud providers and critical vendors. Record

security team contacts, escalation paths, and prerequisites for obtaining assistance, such as account

numbers, support contracts, and verification procedures. Test these escalation paths periodically to confirm

they work as expected.

Conduct Tabletop Exercises and Incident Response Drills

Exercises and drills validate the effectiveness of preparation and identify gaps before real incidents expose

them. Teams that practice together respond more effectively under pressure because they have already

worked through decision points, communication challenges, and coordination issues in a low-stakes

environment. When these drills are realistic and even fun, they build team collaboration and confidence,

which are valuable attributes to have when responding to a real incident.

Tabletop exercises are discussion-based sessions in which participants discuss their responses to a

hypothetical scenario. They require relatively low effort to organize and can involve participants across

departments and management levels. Tabletop exercises excel at testing communication procedures,

decision-making processes, and team coordination.

Prepare Activity | Chapter 7 | 101

Start by developing a realistic scenario based on threats relevant to the organization. Include participants

from all departments involved in incident response, and assign a facilitator to guide the discussion and

inject scenario developments as the exercise progresses. Designate a note-taker to capture observations

and improvement opportunities throughout. Schedule sufficient time for meaningful discussion, typically

two to four hours, and conduct a debrief immediately following to capture lessons learned while they are

fresh.

When choosing a scenario for a tabletop exercise, consider selecting from publicly

reported incidents that affected similar organizations for added realism. Alternatively, use

an AI platform to review recent news articles in the organization’s industry and generate

exercise scenarios based on real-world incidents.

Use tabletop exercises to test authorization levels, not technical procedures alone. Include

scenario injects that force participants to make containment decisions: "The compromised

server hosts the customer portal. Do you isolate it now, or wait for management approval?"

These moments reveal whether authorization policies are clear enough for real-world use

and whether responders feel confident acting within their approved action authority.

Technical drills take preparation further by having responders practice hands-on skills using simulated or

isolated environments. These exercises test whether team members can actually execute the procedures

documented in playbooks. Evidence collection exercises using test systems, malware analysis challenges

with controlled samples, log analysis scenarios with planted indicators, and containment procedure

walkthroughs in lab environments all build practical competence that transfers to real incidents.

Full-scale exercises combine tabletop discussions with technical execution to provide the most realistic test

of incident response capabilities. These exercises require significant planning and resources, so most

organizations conduct them annually for critical scenarios. The investment pays off when responders face

real incidents, having already navigated similar situations in practice.

See Section 16.4.3 for guidance on using AI to help generate tabletop exercise scenarios

based on specific IOCs or attack techniques.

TABLETOP EXERCISE GAME PLAY: BACKDOORS & BREACHES

The card game Backdoors & Breaches , published by Black Hills Information Security, provides a fun

and engaging way to practice incident response skills. The game uses activity-based cards to explore

attack paths and practice decision-making in incident response scenarios.

Using a twenty-sided die to introduce randomness, players draw cards representing initial

compromise, pivoting, privilege escalation, persistence, command and control, and data exfiltration.

Using collaborative play, participants win or lose together based on their collective decisions to

respond to an incident.

Figure 37 | Backdoors & Breaches: Compromised Web Server Card

The game is suitable for a wide range of skill levels, offering opportunities for both beginners and

experienced responders to learn different techniques and to practice response strategies. Players can

purchase cards in English and Spanish, including a core set and expansion packs that introduce

additional gameplay options. Alternatively, the cards are available as a free download for printing or

digital use.

NCSC EXERCISE TOOLKIT

Another valuable resource for tabletop exercises is the NCSC Exercise Toolkit , provided by the UK

National Cyber Security Centre (NCSC). Offering pre-planned micro exercises and full tabletop

exercises, teams can choose from a variety of scenarios including ransomware attacks, Wi-Fi

breaches, remote work compromises, insider data breach, and many more.

Prepare Activity | Chapter 7 | 103

Figure 38 | NCSC Insider Threat Tabletop Exercise

Each NCSC exercise in a box scenario includes a facilitator guide, a collection of injects (updates to

introduce in the exercise to simulate evolving events), and a list of desirable and optional attendee

roles (senior incident leader, cybersecurity engineer, HR advisor, PR officer, etc.). Each participant

gets a short briefing to help them understand their role and responsibilities during the exercise.

The NCSC tabletop-in-a-box exercises are a great way to get started with incident response practice

with minimal setup effort. Designed for brief sessions of thirty to sixty minutes, they allow for in-

person and remote teams to collaborate and practice their incident response skills.

Proactive Prevention and Detection

Proactive prevention and detection measures reduce the likelihood of successful attacks and improve the

organization’s ability to identify threats early. While these activities extend beyond traditional incident

response boundaries, they directly contribute to response effectiveness by reducing incident frequency and

severity. These activities are primarily technology-focused: deploying monitoring and detection capabilities,

hardening systems, and ensuring the logging and infrastructure needed to support investigation and

response are in place.

Implement Cyber Threat Intelligence (CTI) Capabilities

Cyber threat intelligence provides context that transforms security data into actionable insight.

Understanding the threats targeting the organization and industry allows the incident response team to

prioritize defenses, recognize attack patterns, and respond more effectively when incidents occur.

CTI capabilities support incident response in several ways: through proactive defenses, detection

enhancement, support for investigations with additional context, and prioritization of response efforts.

Table 9 summarizes several CTI capabilities for incident response.

Table 9 | CTI Capabilities for Incident Response

CAPABILITY DESCRIPTION

Proactive Defense Intelligence about emerging threats enables organizations to implement

protections before attacks materialize. When threat intelligence reveals a

new campaign targeting the industry, security teams can deploy detections

and harden systems before becoming victims.

Detection

Enhancement

Indicators of compromise (IOCs) from threat intelligence feeds can be

integrated into detection systems to identify known malicious infrastructure,

file hashes, and behavioral patterns.

Investigation Context During incidents, threat intelligence helps analysts understand attacker

motivations, typical tactics, and what to look for during scoping. Attribution

information can inform response decisions and help predict attacker

behavior.

Prioritization Not all vulnerabilities and threats pose equal risk. Threat intelligence helps

prioritize remediation efforts based on active exploitation and relevance to

the environment.

Organizations can obtain threat intelligence from commercial providers, industry Information Sharing and

Analysis Centers (ISACs), government sources such as CISA and sector-specific agencies, open-source

intelligence (OSINT) feeds and communities, and internal intelligence developed from past incidents. Each

source offers different perspectives and coverage, so most organizations benefit from combining multiple

feeds.

Threat intelligence is only valuable when it is operationalized for the organization and the

incident response team. To obtain value from CTI sources, organizations should establish

processes to review incoming intelligence, assess relevance, and take appropriate action.

Intelligence that sits unread provides no actionable security benefit.

Standardized Threat Intelligence with STIX

Structured Threat Information eXpression (STIX) is an open standard for representing cyber threat

intelligence in a machine-readable format. STIX enables organizations to share and consume threat data

consistently across different platforms and tools. When an ISAC distributes indicators of compromise, or

when a commercial threat feed delivers new intelligence, STIX defines a common data structure that

enables automated ingestion and correlation.

Defined by the OASIS Cyber Threat Intelligence Technical Committee (CTI TC), the current STIX version is

2.1, using JSON as the underlying serialization format. [15]

A STIX indicator for a malicious URL used in a spear

phishing campaign might look like this:

{

"type": "indicator",

"spec_version": "2.1",

"id": "indicator--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",

Prepare Activity | Chapter 7 | 105

"created": "2025-12-31T14:30:00.000Z",

"modified": "2025-12-31T14:30:00.000Z",

"name": "Credential phishing URL",

"description": "Malicious URL mimicking corporate login page",

"indicator_types": ["malicious-activity"],

"pattern": "[url:value = 'https://login-secure-verify.com/auth']", 1

"pattern_type": "stix",

"valid_from": "2025-12-31T14:30:00.000Z"

}

1 Pattern matching a malicious URL

The pattern field in the STIX data object uses STIX Patterning Language to define what the indicator

matches. Security tools that support STIX can automatically parse this structure and create detection rules

or blocklist entries. This automation transforms raw intelligence into operational defense without manual

intervention.

STIX 2.1 defines a rich set of object types beyond simple URL or IP address matches. STIX domain objects

include threat actor identifiers, specific campaigns, intrusion sets, malware definitions, attack patterns,

vulnerabilities, and courses of action. Observable objects represent the technical artifacts analysts

encounter during investigations: IP addresses, domain names, file hashes, email messages, network traffic,

and registry keys. Relationship objects connect these elements together, linking a threat actor to the

campaigns they conduct, the malware they deploy, and the vulnerabilities they exploit.

This interconnected structure enables threat intelligence to tell a complete story about a domain of activity

and its actions, rather than providing isolated data points. When an organization receives a STIX bundle

describing a new ransomware campaign, analysts gain not only the IOCs for detection but also insight into

the threat actor’s tactics, the targeted vulnerabilities, and recommended defensive actions to inform an

appropriate response plan.

CTI Platforms

Without a dedicated platform, managing multiple intelligence feeds, correlating indicators across sources,

and maintaining context over time becomes increasingly difficult. A CTI platform provides a centralized

environment for ingesting, enriching, analyzing, and sharing threat intelligence. Organizations can use a CTI

platform to aggregate intelligence from commercial feeds, ISACs, government sources, and internal

investigations into a single repository, with relationships between threat actors, campaigns, indicators, and

vulnerabilities maintained automatically.

During active incidents, analysts can search the platform for intelligence related to newly identified

indicators, discover connections to known campaigns or threat actors, and identify additional indicators to

feed into scoping efforts. This capability transforms threat intelligence from a preparation activity into an

active investigation resource.

CTI platforms can provide visibility into trends across observed attacks. By aggregating indicators over time,

analysts can identify which threat actors are most active against the organization’s sector, which techniques

are trending in recent campaigns, and which infrastructure patterns recur across incidents. This trend

analysis helps to inform decisions during active response. When a new incident shares characteristics with a

campaign the platform has been tracking, analysts can draw on the accumulated intelligence to anticipate

the attacker’s next steps, prioritize which systems to scope, and recommend containment actions based on

observed patterns rather than starting from scratch.

OpenCTI is one option for organizations looking to centralize their CTI capabilities. As an open-source

platform, the Community Edition is free and provides core capabilities including STIX 2.1 ingestion, entity

correlation, and integration with detection tools through connectors. The commercially-supported

Enterprise Edition adds collaborative workspaces, advanced analytics, and role-based access controls

designed for larger teams. Example views of the OpenCTI dashboard and indicator drill-down are shown in

Figure 39 and Figure 40.

Figure 39 | OpenCTI Platform Dashboard

Figure 40 | OpenCTI Indicator Drill-Down

CTI platforms like OpenCTI provide valuable capabilities for managing and operationalizing threat

intelligence. While smaller teams may manage intelligence effectively with spreadsheets or SIEM

integrations, CTI platforms become increasingly valuable as the volume of intelligence grows and the need

Prepare Activity | Chapter 7 | 107

for correlation and context becomes more important for effective incident response.

Develop Processes and Procedures for Software Management

Effective software management reduces the attack surface available to attackers. Five areas deserve

particular attention: patch management, configuration management, software inventory, software supply

chain security, and end-of-life management.

Core Software Management Areas: Patch, Config, and Inventory

Patch management establishes processes to identify, test, and deploy security patches across the

environment. Start by identifying vulnerabilities through vendor advisories, scanning tools, and threat

intelligence feeds. Prioritize remediation based on exploitability and asset criticality, giving accelerated

attention to vulnerabilities under active exploitation. Establish testing procedures to validate patches before

broad deployment, and define exception handling for systems that cannot be patched immediately.

Configuration management maintains documented, version-controlled configurations for systems and

applications. During incidents, configuration baselines help analysts identify unauthorized changes that may

indicate compromise. When recovery requires rebuilding systems, documented configurations enable rapid

restoration to known-good states. Configuration management also documents dependencies and

integration points relevant to scoping, and supports rollback when changes introduce problems during

recovery.

Software inventory tracks installed software, including version information across the environment.

Software Bill of Materials (SBOM) capabilities help identify systems affected by vulnerabilities in third-party

components. When a new vulnerability emerges in a widely used library, accurate software inventory

enables rapid identification of affected systems.

Formal software inventory processes often miss shadow IT, where departments or

individuals purchase SaaS subscriptions, cloud services, or software licenses outside of

approved procurement channels. A practical discovery technique is to review recurring

billing statements and expense reports for subscription services that may not appear in

official asset inventories. These shadow services expand the organization’s attack surface

and create gaps during incident scoping, and attackers increasingly target unmanaged

SaaS platforms and cloud accounts where security monitoring and hardening controls are

absent.

Supply Chain Security and End-of-Life Management

Software supply chain security addresses the reality that every application an organization deploys carries

implicit trust in a broad chain of upstream contributors. A vendor’s product may appear to come from a

single source, but modern software typically assembles components from dozens or hundreds of open-

source libraries, third-party software development kits (SDKs), and developer packages. Each upstream

dependency represents an additional organization, maintainer, or project that an attacker could

compromise to reach downstream targets. This reality expands the attack surface well beyond what

traditional vendor risk assessments capture.

Attackers exploit this expanded surface through multiple vectors: compromising package repositories such

as the Node Package Manager (NPM) or the Python Package Index (PyPI), injecting malicious code through

dependency confusion or typosquatting, or compromising the accounts of trusted maintainers. [16]

A single

compromised component can propagate across an organization’s software portfolio through transitive

dependencies, affecting systems that never directly referenced the malicious package.

Organizations should account for supply chain risk as part of their software management practices. Extend

the SBOM capabilities described above to encompass vendor-supplied applications, not only internally

developed code. Where the organization develops software internally, pin dependencies to known-good

versions using lock files and hash verification, configure private registries or repository proxies to limit

direct exposure to public repositories, and integrate dependency scanning into build pipelines. For vendor-

supplied software, evaluate vendors' own supply chain security practices, including how they vet upstream

dependencies and communicate supply chain incidents to customers. Accurate dependency inventories

enable the organization to quickly identify affected systems and begin scoping when a supply chain

compromise is disclosed.

End-of-life management tracks software that is approaching or past its vendor support dates. Software that

no longer receives security updates presents an ongoing risk that cannot be mitigated through patching.

Identify systems running end-of-life software and establish plans for migration, replacement, or the

implementation of compensating controls. During incidents, end-of-life systems often represent likely

attack vectors because known vulnerabilities remain permanently unpatched.

PATCH MANAGEMENT AND PRIORITIZATION EFFORTS

For many organizations, the greatest challenge in software patch management is prioritization. All

software update processes require effort, and many organizations struggle to keep up with the

volume of monthly patches. Compounding this challenge, the more organizations fall behind on

patching, the more difficult it becomes to catch up.

For example, as I wrote this chapter in December 2025, the CVE-2025-14847 "MongoBleed"

vulnerability was receiving significant attention due to active exploitation in the wild. This

unauthenticated vulnerability affects MongoDB instances as far back as releases in 2017 (MongoDB

3.6.0), allowing an attacker to gain access to system memory chunks by exploiting a vulnerability in

the zlib library used by MongoDB. Shodan, a popular internet scanning CTI service, reports over

213,000 internet-exposed MongoDB instances as of this writing.

Prepare Activity | Chapter 7 | 109

Figure 41 | Shodan Results for Internet-Exposed MongoDB Instances

Organizations running MongoDB instances that have not applied patches for this vulnerability face

significant risk, with only a few days between the vulnerability disclosure and public exploit’s

availability on December 25, 2025.

Figure 42 | X Release of MongoBleed Exploit

For many organizations, limited resources prioritize updates to critical software only when a critical-

severity vulnerability needs to be addressed. It is common for organizations to run older versions of

MongoDB software, either locally provisioned by an in-house IT team or as part of a turnkey

application delivered by a third-party, deferring updates until a crisis forces action. When a

vulnerability like MongoBleed emerges, organizations scramble to identify affected systems and apply

patches, complicated by the need to make significant version jumps rather than incremental updates.

Organizations that defer software management pay a higher price when critical vulnerabilities

emerge. Regular patch cycles, accurate software inventory, and established testing procedures

reduce the cost and chaos of emergency response. Organizations that fall behind on patching face

compounding challenges: the more they defer, the more difficult it becomes to catch up.

Apply System Hardening Processes

System hardening reduces the attack surface by removing unnecessary features, applying security

configurations, and implementing least-privilege principles. Hardened systems are more difficult to

compromise initially and limit attacker options after initial access.

Start by disabling unnecessary services and removing features not required for system function. Each

running service represents a potential attack surface that attackers can target. Change or remove default

accounts and credentials, as attackers routinely attempt to use them during initial access attempts.

Deploy endpoint controls that monitor, alert, and block unauthorized access. Forward logging data to a

central collection server for analysis and retention (see Collect and Retain Logging Information ). Logs from

hardened systems provide valuable telemetry during incident investigation.

Apply vendor security benchmarks, such as CIS Benchmarks or DISA STIGs, appropriate to each system

type. These benchmarks provide tested configurations that address common security weaknesses. Where

feasible, implement application allowlisting to prevent execution of unauthorized software, blocking

Prepare Activity | Chapter 7 | 111

attackers from running malicious tools even after gaining access.

Figure 43 | CIS Benchmark Checklist for HPE Aruba Networks Device

Hardened systems also represent a valuable threat hunting opportunity. Following a

compromise, an attacker may attempt to disable controls to accommodate other attacks.

When a system no longer matches the hardened baseline, this deviation can serve as an

effective indicator of compromise.

Document hardening configurations and automate their application where possible. Infrastructure-as-code

approaches enable consistent hardening across environments and simplify rebuilding systems during

recovery. Alternatively, PowerShell or other shell scripts can automate hardening tasks on existing systems,

enabling organizations to achieve greater consistency in their hardening efforts. Review and update

hardening baselines regularly as new vulnerabilities and attack techniques emerge.

Implement Endpoint-Based Security Monitoring and Threat Detection

Endpoint Detection and Response (EDR) tools provide essential visibility into host-based activities. EDR

products support both proactive threat detection and incident investigation, making them a valuable tool

for protecting systems and aiding incident investigations.

Product-specific labels for endpoint protection tools vary, including Endpoint Detection

and Response (EDR), Extended Detection and Response (XDR), Next-Generation Antivirus

(NGAV), and Endpoint Protection Platform (EPP). This section refers to endpoint protection

tools as EDR for simplicity, but the concepts apply broadly across these product

categories.

EDR platforms collect telemetry, including process execution, file system changes, registry modifications,

and network connections. This telemetry enables behavioral detection of suspicious patterns, such as

process injection, credential dumping, anomalous usage, and persistent access tool deployment. Analysts

can query collected telemetry to hunt for indicators across managed endpoints. Responders can take

remote actions to isolate systems, terminate processes, or collect evidence for additional analysis.

Gaps in EDR coverage create visibility gaps that attackers can exploit. Notably, third-party

systems, legacy devices, and cloud instances are often excluded from EDR deployment.

Ensure coverage extends across the environment, including servers, workstations, and

cloud instances.

EDR effectiveness depends on proper configuration and alert tuning. Work with vendors or internal teams

to tune detection rules for the environment, reducing false positives while maintaining sensitivity to

genuine threats. Establish processes to promptly review and investigate EDR alerts, as delayed investigation

gives attackers additional time to achieve their objectives.

EDR AS A SUCCESS STORY

As a professional penetration tester, the biggest challenge I face is not in gaining initial access to a

target environment. Rather, it’s preserving that access long enough to achieve my objectives without

being detected and removed by endpoint protection systems.

Common techniques for gaining initial footholds, such as exploiting public-facing web applications or

manipulating users into authorizing malicious actions, remain well understood and frequently tested.

However, once inside an environment, maintaining persistence and moving laterally without

detection has become increasingly difficult. Even novel techniques developed internally often trigger

detection by well-configured EDR solutions.

This represents a genuine success story for organizational security. EDR deployments have

fundamentally changed the economics of attacks by making post-compromise activities expensive

and risky for attackers. Organizations with mature EDR implementations regularly detect and disrupt

intrusions that would have succeeded just a few years ago.

In response, attackers have adapted. Supply chain compromises, cloud token theft, and social

engineering techniques that bypass endpoint protections entirely have become more prominent. This

tactical shift is evidence that EDR works, but also a reminder that defenses cannot remain static. As

attackers evolve their techniques, organizations should continue investing in complementary controls

that address the gaps attackers now target.

Deploy Sysmon for Enhanced Windows Telemetry

System Monitor (Sysmon) is a free tool from the Microsoft Sysinternals suite that extends default Windows

event logging with high-fidelity telemetry for security monitoring and investigation. [17]

Where default

Windows logging captures limited event detail, Sysmon records process creation with full command-line

Prepare Activity | Chapter 7 | 113

arguments and parent process information, network connections with source and destination details, file

creation timestamps, registry modifications, and driver and DLL loading events. This telemetry fills

important gaps that default Windows audit logging does not cover.

During incidents, Sysmon logs provide investigation-grade detail that persists in the Windows Event Log.

Analysts can reconstruct process execution chains, identify lateral movement through remote service

activity, and trace attacker tooling across compromised hosts. Sysmon is particularly valuable in

environments with incomplete EDR coverage, including legacy systems, third-party-managed hosts, and lab

or development environments where EDR agents may not be deployed. For organizations with EDR

coverage, Sysmon provides a complementary and independent telemetry source that remains available even

if an attacker disables or evades the EDR agent.

From a prioritization perspective, Sysmon is a high-value preparation resource for

organizations with significant Windows environments, especially those with EDR coverage

gaps. Sysmon provides valuable visibility into Windows activity, supporting both proactive

detection and incident investigation. Investing some time into deploying and configuring

Sysmon can yield significant benefits for incident response teams.

Sysmon’s value depends heavily on its configuration. The default configuration captures a broad set of

events, but without filtering it generates significant noise that can overwhelm log collection infrastructure.

The SwiftOnSecurity Sysmon configuration  provides a highly curated community starting point that

balances noise reduction with detection coverage. Organizations should use this configuration as a baseline,

then tune it for their environment by adding exclusions for known-good activity and additional rules for

organization-specific detection needs. Forward Sysmon events to central log collection alongside other

security telemetry to enable correlation and long-term retention.

Sysmon deployment pairs well with adversary simulation. After deploying Sysmon with a

tuned configuration, run atomic tests against ATT&CK techniques relevant to the

organization’s threat profile and verify that the expected telemetry appears in the collected

logs. This validation confirms that Sysmon is capturing the events needed for detection

and investigation.

Implement Network Security Monitoring and Threat Detection

Network monitoring provides visibility into communications between systems and with external networks.

Where endpoint monitoring systems provide host-level visibility limited to a single host at a time, network

monitoring offers insight into traffic traversing the network, providing a broader perspective for threat

detection. This visibility enables analysts to detect command-and-control (C2) activity, lateral movement

traffic patterns, and data exfiltration attacks that host-based monitoring can miss.

Organizations can implement network monitoring through several complementary approaches, each

offering different tradeoffs between visibility, storage requirements, and analytical capabilities. No one

solution will meet the needs or constraints of every organization, so consider the options available in the

context of the organization’s needs, budget, and technical capabilities.

Full Packet Capture

For many years, full packet capture (FPC) represented the gold standard for network monitoring. Many

organizations invested heavily in capturing and storing complete network traffic for retrospective analysis,

including threat hunting and incident investigation. However, these investments proved costly to maintain,

and the volume of data can easily overwhelm analysts' ability to process and analyze it effectively. Further,

the use of network transport encryption for modern protocols can limit the value of captured data unless

there is a secondary capability to decrypt traffic for analysis. Additionally, the cost of storage and

processing required for capture increases significantly as network traffic rises with higher-bandwidth

connections, an increased number of devices, and the increasingly common shift to cloud-based services,

including SaaS platforms.

STRATEGIC PACKET CAPTURE

For organizations committed to packet capture, a strategic approach can maximize value while

managing costs.  Phil Hagen, a SANS instructor who has written extensively on network forensics,

offers practical guidance for optimizing capture investments.

Phil indicates that the fundamental challenge (after cost and resources) is that encryption of network

transport data makes FPC significantly less useful. Even for organizations that aim to use acquired

private key material to decrypt captured traffic (the store-now-decrypt-later approach), Perfect

Forward Secrecy (PFS) and emerging post-quantum cryptography have closed the door on this

approach. This reality demands a shift in strategy: rather than capturing everything and hoping to

analyze it later, focus resources on traffic that provides immediate analytical value.

Start by identifying what traffic can be collected through TLS-decrypting proxies. Zero Trust

solutions such as Zscaler, Netskope, and similar platforms can provide visibility into encrypted traffic

at the proxy-interception layer. For traffic that cannot be decrypted, deprioritize commonly

encrypted traffic on ports such as 22 (SSH), 443 (HTTP over TLS), and 993 (IMAP over TLS), where

payload inspection provides limited value.

For encrypted traffic worth retaining, consider truncating capture at twenty to thirty packets per

socket. This approach preserves the TLS negotiation phase, which contains valuable metadata:

certificate information, cipher suites, and TLS ClientHello message fingerprints (using multiple JA4+

fingerprinting techniques). These artifacts support detection and investigation even when payload

content remains encrypted.

For organizations with tighter constraints, excluding encrypted traffic entirely while ensuring

comprehensive Netflow coverage provides a reasonable alternative. Migrate detection heuristics and

artifact collection to focus on what remains analyzable rather than attempting comprehensive

capture.

These recommendations are often set aside for cost, complexity, sensitivity, or legal reasons.

However, they remain valuable for consideration in limited capacities or during active incident

response when targeted visibility becomes critical.

Network Flow Monitoring

As an alternative to FPC, many organizations will benefit from network flow monitoring. Flow data provides

a summary of network communications without the storage burden of full packet capture, making it

practical for long-term retention and broad deployment. Where FPC answers "what exactly was

Prepare Activity | Chapter 7 | 115

transmitted," flow data answers "who talked to whom, when, and how much," which is often sufficient for

detection and initial investigation.

Network flow data captures summary metadata about network connections rather than full packet

contents. A flow record represents a unidirectional sequence of packets sharing common attributes such as

source, destination, and protocol. Table 10 describes some of the most useful fields available in flow records

for detection and investigation.

Table 10 | Common NetFlow Fields

FIELD DESCRIPTION

Source/Destination IP IP addresses of communicating hosts.

Source/Destination Port TCP or UDP ports identifying services.

Protocol Transport protocol (TCP, UDP, ICMP, etc.).

Timestamps Flow start and end times for timeline analysis.

Byte Count Total bytes transferred; useful for detecting data exfiltration.

Packet Count Number of packets; reveals broad traffic patterns.

TCP Flags Flags observed (SYN, ACK, RST, etc.) for connection analysis.

Interface/Direction Traffic direction (ingress/egress) through the network.

This metadata enables analysts to identify anomalous communication patterns, quantify data transfer

volumes, detect beaconing behavior, and trace lateral movement paths across the network.

Several flow technologies exist, each with different origins and formats but providing similar analytical

value. Cisco NetFlow and its successor IPFIX (IP Flow Information Export) remain widely deployed in

enterprise environments. sFlow, developed by InMon Corporation, uses statistical sampling to reduce

processing overhead on high-bandwidth networks.

Flow data from network engineering equipment (routers and switches) is typically sampled,

often at ratios of 1:1000 packets or higher, missing significant portions of traffic. Security-

focused flow data from firewalls is usually unsampled by default, providing complete

visibility. When relying on router-generated flow data for incident response, verify the

sampling configuration and account for potential gaps in coverage.

Cloud environments offer native flow logging via services such as AWS VPC Flow Logs, Azure NSG Flow

Logs, and Google Cloud VPC Flow Logs. While the specific fields and formats differ across these

technologies, the core value proposition remains consistent: lightweight metadata collection that enables

traffic analysis without the cost of full packet capture.

Extended Berkeley Packet Filter (eBPF)

Extended Berkeley Packet Filter (eBPF) builds on the original Berkeley Packet Filter (BPF), a packet-filtering

mechanism introduced in the early 1990s for capturing network traffic. Where BPF operated as a

straightforward packet filtering capability, eBPF extends this concept into a general-purpose,

programmable framework for safely executing custom code within the operating system kernel. This

evolution transforms what was originally a network capture tool into a comprehensive observability

capability.

eBPF programs run in a sandboxed virtual machine within the kernel, with a built-in verifier that checks

each program for safety before execution. This design provides deep visibility into kernel-level activity,

including network connections, system calls, file operations, and process execution, without requiring

custom kernel modules or system reboots. The low overhead and safety assurances make eBPF valuable for

continuous monitoring on production systems.

For incident response preparation, eBPF offers several advantages over traditional monitoring approaches.

Network monitoring tools built on eBPF can generate flow data, capture connection metadata, and inspect

packet headers directly in the kernel, supplementing or replacing conventional NetFlow infrastructure.

Beyond network visibility, eBPF-based security tools observe process behavior, file access patterns, and

privilege changes at the system-call level, providing the kind of host telemetry that supports both detection

and forensic investigation. Open-source projects such as Cilium, Falco, and Tetragon leverage eBPF to

deliver network policy enforcement, runtime threat detection, and security observability for traditional

systems and for containerized environments.

While eBPF originated in the Linux kernel, Microsoft is actively developing eBPF support for Windows

through the eBPF for Windows project, extending this observability framework to Windows environments.

[18]

As eBPF adoption expands across operating systems, organizations that invest in eBPF-based monitoring

gain a unified observability approach that spans network, host, and container workloads.

Network Detection and Response (NDR)

Network Detection and Response (NDR) platforms analyze network traffic for threats using behavioral

analysis, signature-based detection, and threat intelligence integration. These platforms process network

data in near-real time, applying machine learning models to identify anomalous patterns and matching

observed indicators against known threat signatures. NDR solutions reduce the manual analysis burden on

security teams by automatically identifying suspicious activity thereby reducing the mean time to detect

(MTTD) for active threats.

One particularly valuable feature of NDR platforms is the ability to integrate CTI insights to detect emerging

threats. By incorporating IOCs from commercial and free CTI feeds, ISACs, and government sources, NDR

platforms can identify communications with known malicious infrastructure, detect command-and-control

patterns associated with specific threat actors, and flag file transfers matching known malware signatures.

This integration transforms NDR into a platform that combines behavioral anomalies with known-threat

identification, providing broader coverage across the threat landscape.

Many NDR systems also support event correlation, combining host-based telemetry with

network data to provide richer context for detection and investigation. This correlation

enables analysts to connect network-level indicators with endpoint activity, building a more

complete picture of attacker behavior.

Position network monitoring at critical points, including internet egress, network segment boundaries, and

connections to sensitive systems. For broad detection and investigative opportunities, organizations should

deploy monitoring sensors at points where traffic enters and leaves networks (North-South traffic) and

between internal networks (East-West traffic) where lateral movement occurs.

Prepare Activity | Chapter 7 | 117

Invest in Detection Engineering

Deploying security monitoring tools is a necessary first step, but the tools themselves only provide value

when backed by a sustained detection engineering practice. Detection engineering is the discipline of

designing, building, testing, and maintaining the detection rules and logic that turn raw telemetry into

actionable insight. Without ongoing investment in this discipline, organizations accumulate monitoring

tools that generate noise rather than insight.

A monitoring tool without well-maintained detection rules is an expensive log collector.

Detection engineering connects the endpoint, network, and log monitoring capabilities described in the

preceding sections. An EDR deployment provides telemetry, but a detection engineer writes the rules to

identify suspicious process relationships or unapproved credential access patterns using that telemetry. A

SIEM ingests logs, but detection engineers develop the correlation logic that catches lateral movement

across multiple log sources. NDR platforms analyze traffic, but detection engineers define which behavioral

patterns warrant analyst attention.

Effective detection engineering programs include several ongoing activities:

• Rule development : Writing detection rules tied to specific attacker techniques, informed by threat

intelligence and mapped to frameworks like MITRE ATT&CK.

• Testing and validation : Verifying that detection rules fire correctly using adversary simulation tools

(such as Atomic Red Team).

• Tuning: Reducing false positives by refining rule logic based on the organization’s environment, and

removing or revising rules that generate alerts without investigative value.

• Coverage tracking: Mapping detection rules against the ATT&CK matrix to identify which techniques

are covered and where gaps remain.

• Lifecycle management : Retiring outdated rules, updating rules when the environment changes, and

documenting the intent and logic behind each rule so others can maintain them.

Organizations that treat detection as a one-time configuration task rather than an ongoing engineering

practice inevitably fall behind as attackers adapt their techniques.

Establish a Threat Hunting Program

Threat hunting complements automated detection by using analyst expertise to search proactively for

threats that rules and signatures miss. Rather than waiting for alerts, analysts formulate hypotheses about

how attackers might operate in the environment, then investigate the telemetry for evidence that those

hypotheses are true. Treating this work as a documented program rather than an ad hoc effort ensures

coverage across the threats the organization cares about and provides evidence of diligence under regulator

review.

A threat hunting program typically includes the following elements:

• Hypothesis catalog: A maintained list of hunt hypotheses tied to MITRE ATT&CK tactics and techniques

(e.g., command and control beaconing, lateral movement via WMI, data staging in unusual directories).

• Target data sources: For each hypothesis, the logs or telemetry required to investigate it, such as proxy

logs, DNS queries, or process creation events.

• Cadence: How often each hypothesis is reviewed, prioritized by risk and data freshness.

• Audit trail: A tracking data set capturing hypothesis, data source, cadence, last-run date, analyst, and

findings, supporting both internal coverage reviews and external regulator inquiries.

• Feedback loop: A process for promoting findings from hunts into automated detection rules, ensuring

the detection engineering program benefits from analyst discoveries.

Organizations just starting with threat hunting can begin with a small set of high-priority hypotheses and

grow the catalog over time as the team builds expertise. Documenting the program also protects the

organization’s investment in hunting activity: when staff turnover occurs, the next analyst inherits the

hypothesis catalog and knows where the previous team member left off.

Catalog All Critical Data, Systems, and Infrastructure

A comprehensive asset inventory enables rapid scoping during incidents and ensures critical systems

receive appropriate protection. When responders can quickly identify which systems exist, who owns them,

and how they integrate with other resources, the incident response team can complete scoping more

quickly and with greater accuracy and insight. Without accurate inventory, responders waste time

identifying affected systems, leading to longer delays in initial verification of the incident, and may miss the

compromise of unknown or forgotten assets.

Start by documenting assets using the broad categories in Table 11. Each category captures different aspects

of the environment that become relevant during incident response. Hardware and software inventories help

identify affected systems, while network architecture documentation is valuable to understand potential

lateral movement paths. Data asset records indicate what sensitive information may be at risk, and third-

party connection documentation identifies external parties who may need notification or will be asked to

provide insight for investigative analysis.

Table 11 | Asset Inventory Categories

CATEGORY ELEMENTS TO DOCUMENT

Hardware Assets Servers, workstations, network devices, mobile devices, and IoT

systems with location, owner, and criticality.

Software Assets Applications, operating systems, and middleware with version

information, licensing, and support status.

Data Assets Sensitive data repositories, locations, classification levels, and

regulatory requirements.

Cloud Resources Virtual machines, containers, storage, databases, and services across

cloud environments.

Network Architecture Network diagrams, IP addressing schemes, VLAN assignments, and

firewall rule collections.

Third-Party Connections VPN connections, API integrations, and data sharing relationships

with external parties.

Critical Assets Systems and services essential to the organization’s objectives,

including revenue-generating operations, customer-facing services,

and regulatory compliance systems.

Prepare Activity | Chapter 7 | 119

In many organizations, these categories are maintained by different teams in different systems: network

engineering maintains network diagrams and firewall rules, server and cloud teams maintain infrastructure

inventories, and business units track their own data assets and third-party relationships. The incident

response team should maintain local copies of this documentation for offline access during incidents, but

should also establish relationships with the authoritative source owners to ensure access to current data.

Local copies provide availability when primary systems are compromised, while access to authoritative

sources ensures the information used during scoping and containment reflects the current state of the

environment.

Not all systems require the same level of attention during response. Using a classification system to identify

assets by business criticality will help decision makers prioritize actions during incidents. The Critical

Assets category in the inventory identifies which systems warrant priority attention during scoping,

containment, and recovery. Document these classifications in advance so decision makers can make

informed prioritization decisions without delay.

Consider maintaining asset inventory in a format that supports rapid querying during incidents.

Spreadsheets work for smaller environments, but larger organizations benefit from dedicated Configuration

Management Database (CMDB) platforms or asset management tools that support search, filtering, and

integration with other security tools. Whatever format the organization chooses, ensure the inventory

remains accessible during incidents, including scenarios where primary systems may be compromised.

Asset inventory is only useful if it is accurate. Implement processes to maintain inventory

currency, including automated discovery tools, change management integration, and

periodic audits. Stale inventory data can mislead responders and delay effective response.

Monitor the Attack Surface

A comprehensive asset inventory captures what the organization knows about its environment, but

attackers target what the organization exposes, which is not always the same thing. Attack Surface

Monitoring (ASM) extends the asset inventory by continuously discovering and evaluating accessible assets:

internet-facing services, cloud resources, domains, certificates, distributed computing endpoints, exposed

APIs, and more. Where the asset inventory answers what do we have?  ASM answers what can an attacker

see?

THE MODERN ATTACK SURFACE

The attack surface for most organizations extends well beyond servers and workstations connected

to the corporate network. As Ron Eddings and MJ Kaufmann observe in Attack Surface Management :

[19]

“When we start looking at attack surfaces, it’s no longer as simple as it was in the early days of IT

and the internet. We still have all of the traditional components of IT that keep businesses running,

including workstations, networks, and servers, but IT is so much more now. IT and how we do

business has expanded to include a wider variety of technologies that are just as integral to

business operations as the traditional components.

— Eddings & Kaufmann, Attack Surface Management

Today’s attack surface includes cloud environments, SaaS applications, APIs, mobile devices, IoT

systems, AI infrastructure, and third-party dependencies, each with its own security characteristics

and visibility challenges. An organization’s internal asset inventory may account for traditional IT

components while missing the cloud resources, SaaS integrations, and vendor connections that

attackers increasingly target.

ASM tools help organizations discover and monitor this broader attack surface, providing a more

complete picture of where attacks are likely to originate. For incident response teams, this visibility is

particularly valuable. Assets that are unknown during preparation are assets that will be missed

during scoping.

“After all, you can’t manage what you don’t know exists.

— Ron Eddings and MJ Kaufmann, Attack Surface Management

ASM tools discover externally accessible assets, identifying resources that may not appear in internal

inventories. These discoveries can include forgotten development servers, test environments with

production data, acquired company infrastructure that was never integrated, and cloud resources

provisioned outside standard change management processes.

Assets that do not appear in the internal inventory are unlikely to appear in the incident

scope. ASM helps close this visibility gap by discovering what the organization exposes

before an attacker does.

For incident response preparation, ASM provides two specific benefits. First, it reduces the likelihood of

incidents by identifying exposures before attackers exploit them. A newly exposed administrative interface

or an expiring certificate on a customer-facing service can be addressed proactively rather than discovered

during an incident investigation. Second, it improves scoping accuracy during incidents by giving

responders a current view of the organization’s accessible attack surface, which may differ from what

internal documentation reflects.

Organizations can implement ASM at different levels of maturity. Smaller teams can start with periodic

external scanning using open-source tools and comparing results against the asset inventory. Larger

organizations may benefit from dedicated ASM platforms that provide continuous monitoring, change

alerting, and integration with vulnerability management workflows. Regardless of approach, the results

Prepare Activity | Chapter 7 | 121

should feed back into the asset inventory and hardening processes to close the loop between discovery and

remediation.

Assess Security Posture Through Adversary Simulation

Assessing security posture requires more than identifying known vulnerabilities. Vulnerability scanning

identifies missing patches and misconfigurations, but it does not determine whether detection and

response capabilities work when an attacker moves through the environment after initial access. Post-

exploitation gaps such as undetected lateral movement, missed credential harvesting, or silent persistence

mechanisms do not appear in vulnerability scan results.

Adversary simulation closes this gap by testing the full defensive chain, from initial access through post-

compromise activity as shown in Figure 44 . This approach validates whether the organization’s detection

tools can identify attack techniques in practice, and whether response processes can effectively contain and

remediate incidents.

Figure 44 | Adversary Simulation Risk Assessment Coverage

Adversary simulation can take several forms, each with different levels of complexity and resource

requirements. For example, an organization might start by performing vulnerability scanning, augmented by

configuration assessment against security benchmarks, to establish a baseline and identify known

weaknesses across the environment. Penetration testing can be applied to validate whether those

weaknesses are exploitable in practice, and application security testing can be used to analyze custom

software through static analysis, dynamic testing, and code review.

Adversary simulation and purple teaming go further by testing detection coverage against known attack

techniques. Frameworks like MITRE ATT&CK provide a structured catalog of adversary tactics and

techniques that organizations can use to map which behaviors their detection tools can identify and where

gaps exist. [20]

Projects such as Atomic Red Team  provide repeatable, granular test cases for individual

ATT&CK techniques, allowing teams to validate specific detection rules without requiring a full red team

engagement. [21]

Organizations do not need a mature red team program to begin adversary simulation. Running a small set of

atomic tests against ATT&CK techniques relevant to the organization’s threat profile validates whether the

investment in detection tools is producing results.

For organizations seeking continuous validation rather than periodic testing, Breach and Attack Simulation

(BAS) platforms automate adversary simulation by running predefined attack scenarios against production

or near-production environments on a scheduled basis. BAS tools execute attack chains that mimic real

threat actor behavior, testing whether security controls detect and block each step. Results are mapped to

specific detection gaps, giving security teams a prioritized remediation list tied to actual control failures

rather than theoretical vulnerabilities.

BAS shifts the question from could this attack succeed?  to did our controls detect and

block it? This distinction helps teams prioritize remediation based on demonstrated gaps

rather than hypothetical risk.

BAS complements manual adversary simulation and penetration testing rather than replacing them. Manual

exercises bring human creativity and adaptability that automated tools cannot replicate, while BAS provides

the continuous coverage that ensures detection capabilities remain effective between manual assessments.

Organizations with active detection engineering programs can use BAS results to validate new detection

rules and measure improvement over time.

Vulnerability findings from all assessment activities should feed back into patch management and hardening

processes, with remediation progress tracked and persistent vulnerabilities escalated when they exceed

acceptable risk thresholds.

CVSS FOR VULNERABILITY PRIORITIZATION

The Common Vulnerability Scoring System (CVSS) provides a standardized method for rating the

severity of security vulnerabilities. Maintained by FIRST, CVSS assigns numerical scores from 0 to 10

based on characteristics that describe how a vulnerability can be exploited and its potential impact.

Organizations commonly use CVSS scores to prioritize remediation efforts, with higher scores

indicating more severe vulnerabilities.

CVSS version 3.1 calculates base scores using eight metrics organized into exploitability and impact

categories. Exploitability metrics describe how an attacker would exploit the vulnerability, while

impact metrics describe the consequences of successful exploitation. Table 12  illustrates these

metrics using CVE-2025-61882, an Oracle E-Business Suite vulnerability with a critical 9.8 base score.

Table 12 | CVSS 3.1 Base Metrics for CVE-2025-61882

METRIC VALUE MEANING

Attack Vector Network Exploitable remotely over the network.

Attack Complexity Low No special conditions required for exploitation.

Privileges Required None Attacker needs no prior access or credentials.

User Interaction None No victim action required.

Scope Unchanged Impact limited to the vulnerable component.

Confidentiality Impact High Complete loss of confidentiality.

Integrity Impact High Complete loss of integrity.

Availability Impact High Complete denial of service possible.

Prepare Activity | Chapter 7 | 123

The combination of network-accessible exploitation that requires no privileges or user interaction,

coupled with high impact across all three security dimensions, yields the critical base score of 9.8.

While CVSS provides valuable standardization, organizations should avoid using it as the sole basis for

prioritization. A critical-severity vulnerability in an internet-facing system demands immediate

attention, but the same vulnerability in an isolated test environment may warrant lower priority.

CVSS scores do not account for organizational context, such as whether the vulnerable software is

deployed, whether compensating controls exist, or whether the asset supports critical business

functions.

Use CVSS as one input among several for prioritization decisions. Combine CVSS severity with asset

criticality, exposure level, and threat intelligence about active exploitation to make informed

decisions about where to focus limited remediation resources.

The Exploit Prediction and Scoring (EPSS)  metric, from the Forum of Incident Response

and Security Teams (FIRST), provides a data-driven approach to prioritizing vulnerability

remediation based on the likelihood of exploitation. Where CVSS focuses on how difficult a

vulnerability would be  to exploit, the EPSS metric estimates the probability that a

vulnerability will be exploited in the wild. EPSS offers another dimension to vulnerability

prioritization for software management that complements CVSS scores.

Collect and Retain Logging Information

Comprehensive logging provides the data foundation for threat detection and incident investigation.

Without adequate logs, detection capabilities are limited, and post-incident analysis may be impossible.

Start by identifying log sources that should send data to the central collection. Priority sources include

authentication systems, security tools, critical servers, network devices, and cloud platforms. Configure

these systems to capture security-relevant events: enable process-creation logging with command-line

arguments on Windows systems, capture authentication events, including successes and failures, and log

network connections and DNS queries where feasible.

FEAR THE DARK: WHEN LOGS GO MISSING

Heather Barnhart, SANS Institute head of faculty, warns that incident responders face a growing

threat that no detection tool can address: dark periods  — gaps in time where no reliable digital

evidence exists. [22]

These investigative gaps emerge from multiple causes: misconfigured logging that

fails to capture critical events, default logging settings that prove too limited for forensic needs,

retention policies that delete evidence before investigations begin, infrastructure changes that create

coverage gaps, and malicious actors who deliberately manipulate or destroy logs.

The consequences can be severe. In the 2022 Idaho murders investigation, critical cell tower data

gaps created dark periods that complicated the timeline reconstruction for victims like Kaylee

Goncalves. The 2025 Bybit cryptocurrency breach, attributed to APT38, resulted in $1.5 billion in

losses partly because the attack behavior appeared normal to AI-based detection systems, and

investigators faced significant evidence gaps.

Barnhart’s guidance is direct: "Log for normal so you can find evil."

Organizations should establish baselines for expected activity and ensure that logging captures

sufficient context to distinguish legitimate operations from malicious ones. Without complete logs,

even the most skilled incident response teams face preventable gaps that attackers will exploit.

“We need to be afraid of the dark... because the dark is the lack of data.

— Heather Barnhart, SANS Institute Head of Faculty

Define retention periods based on investigation needs, compliance requirements, and storage constraints.

Most organizations retain security logs for between ninety days and one year. Longer retention may be

necessary for compliance or to support the investigation of advanced persistent threats that may have

persisted for extended periods before detection.

When planning retention, distinguish between logs retained for compliance and logs retained for active

detection and investigation. Compliance retention satisfies regulatory and audit requirements but does not

require the query performance or correlation capabilities of a SIEM. Organizations can reduce costs by

storing compliance-only logs in a lower-cost archive or log management platform while reserving SIEM

capacity for log sources that support active detection rules and investigation workflows.

Protect logs from tampering or deletion by attackers who gain system access. Forward

logs to a central collection system promptly and implement appropriate access controls for

log storage. Attackers routinely attempt to delete or modify logs to cover their tracks.

SIEM OR SINK?

Security Information and Event Management (SIEM) platforms aggregate logs across the

environment, normalize data into consistent formats, and enable correlation analysis. SIEMs provide

significant value for detection and investigation when properly implemented and maintained.

However, many organizations deploy SIEMs without investing in the ongoing effort required to make

them effective. Logs flow into the platform but are never reviewed. Detection rules generate alerts

that no one investigates. The SIEM becomes a very expensive log sink rather than a security tool.

Effective SIEM operation requires:

• Dedicated analysts to investigate alerts and hunt for threats.

• Continuous tuning to reduce false positives and improve detection accuracy.

• Regular review of coverage to ensure critical log sources are ingested.

• Periodic removal of log sources that have no associated detection or investigation use cases,

freeing capacity and improving retention for sources that do.

• Development of custom detections for organization-specific threats.

• Integration with incident response processes for seamless escalation.

Before investing in a SIEM platform, honestly assess whether the organization will commit the

ongoing resources required to operate it effectively. A well-managed log aggregation system may

Prepare Activity | Chapter 7 | 125

provide more value than an underutilized SIEM.

PREPARATION CHALLENGES

Effective preparation requires sustained effort during periods in which incidents are not actively occurring.

This creates challenges that can undermine preparation activities even in organizations that recognize their

importance. Table 13 summarizes several important challenges and mitigation strategies.

Table 13 | Preparation Challenges Summary

CHALLENGE IMPACT

Resource Constraints Operational demands leave little time for preparation work

Readiness Erosion Skills atrophy and complacency develops during quiet periods

Documentation Drift Plans and playbooks become outdated as the environment changes

Knowledge Loss Institutional knowledge leaves with departing team members

Value Demonstration Preparation benefits are difficult to quantify

Understanding these challenges helps incident response teams anticipate obstacles and implement

countermeasures before preparation efforts stall. The following sections examine each challenge in detail

and provide practical guidance for maintaining effective preparation programs.

Resource Constraints

Preparation activities compete with operational demands for limited resources. Security teams often find

themselves responding to alerts, managing security tools, and supporting business initiatives with little time

left for preparation. When a critical vulnerability requires immediate patching or a suspicious alert demands

investigation, updating the incident response plan naturally falls to a lower priority.

Budget constraints present a separate but related challenge. Training courses, forensic tools, and incident

response exercises all require funding that competes with other security investments. Organizations facing

tight budgets may struggle to justify investment in preparation spending when the return on investment is

difficult to quantify, particularly when more visible projects compete for the same resources.

Frame preparation investments as risk reduction rather than optional enhancement when

seeking management support. For many decision makers, risk reduction is a more

compelling justification than preparedness for hypothetical future events. Where possible,

quantify potential incident costs using industry data and compare against the relatively

modest investment in preparation activities.

Teams can address resource constraints through several approaches:

• Integrate preparation into operations : Document lessons learned immediately after incidents while

context is fresh, update playbooks as part of tool deployment projects, and conduct brief tabletop

discussions during regular team meetings.

• Prioritize high-impact activities: Focus on the most likely incident scenarios, the most critical systems,

and the most significant capability gaps.

• Leverage existing meetings : Use standing team meetings for fifteen-minute tabletop discussions or

playbook reviews rather than scheduling separate preparation sessions.

TURNING INCIDENTS INTO PREPARATION FUNDING

Few things are more frustrating for an incident response team than flagging a missing capability or

underfunded tool, watching the request sit in a backlog, and then seeing that exact gap delay an

active response. When it happens, document the delay and its impact on the incident timeline.

Then use the incident to get the fix approved. Brief leadership that the team intends to address the

gap during or immediately after the response, and seek their approval while the cost of the gap is still

visible. Decision makers who have just watched a missing tool or process slow down a response are

far more receptive to funding the fix than they would be during routine budget discussions. Incident

budgets often absorb remediation costs that would otherwise face months of procurement review,

and the urgency of an active incident often cuts through the inertia that blocked the original request.

Even modest preparation investments compound over time. An organization that dedicates just two hours

per week to preparation activities accumulates over 100 hours of preparation work annually, building

capabilities that prove invaluable when incidents occur.

Maintaining Readiness During Quiet Periods

Extended periods without significant incidents create a paradox: the absence of incidents may indicate that

cybersecurity controls and preparation efforts are working, but it also reduces the urgency that drives

continued investment. Team members can become complacent when they have not encountered an

incident that required response efforts in months or years. Even the best analysts will experience skills

atrophy without regular practice, especially when organizational attention shifts to more visible priorities.

To address this challenge, organizations should practice incident response efforts with regular exercises:

• Monthly tabletop discussions : Brief scenario walkthroughs that test decision-making and

communication.

• Quarterly technical drills: Hands-on exercises using forensic tools and evidence collection procedures.

• Annual full-scale exercises: Comprehensive simulations involving all stakeholders.

Rotate team members through different roles during exercises to build depth and prevent single points of

failure. The analyst who always handles evidence collection during drills should occasionally practice

coordination or communication roles. Team leads should periodically work through technical procedures to

maintain hands-on familiarity.

INCIDENT RESPONSE INVESTIGATION CHALLENGES

One opportunity for organizations to keep their incident response skills sharp is to allocate time for

continued professional development. Traditionally, professional development is viewed as training

courses or on-the-job work, but another valuable approach is to practice investigative skills in

Capture the Flag (CTF) competitions. These competitions simulate real-world incident scenarios,

challenging participants to analyze logs, reverse-engineer malware, and reconstruct attack timelines.

Prepare Activity | Chapter 7 | 127

Many people are drawn to CTFs for the competitive aspect, but this can also be a drawback for those

with imposter syndrome. Consider allocating time for team members to participate in CTFs as a

group activity, focusing on learning and collaboration rather than competition. This approach fosters

teamwork, encourages knowledge sharing, and builds confidence in investigative skills that directly

translate to incident response.

One excellent resource for CTFs is the SANS Skills Quest (SSQ) program , a low-cost self-paced

training option that presents realistic scenarios designed to enhance practical skills. As a contributor

to the team that developed SSQ, I have first-hand experience with its effectiveness in helping teams

develop and measure important cybersecurity and incident response skills.

Another option is to use the free resources available through the Splunk Boss of the SOC  platform,

which offers analysts an opportunity to complete a variety of incident response and forensics

investigation challenges. While primarily focused on Splunk users, the scenarios provide valuable

practice for general investigative skills, and the supplied evidence for analysis can often be examined

with other forensic tools as well.

Figure 45 | Splunk Boss of the SOC Platform

Keeping Plans and Playbooks Current

Organizational changes, technology updates, and evolving threats can make preparation documents

obsolete. An incident response plan finalized six months ago may reference systems that have been

decommissioned, contacts who have changed roles, and procedures that no longer match current tool

capabilities. Outdated documentation can lead to false confidence, where responders believe they have

guidance that is no longer accurate.

Playbooks face similar drift. A ransomware playbook written before the organization adopted cloud

infrastructure may miss critical containment steps. Procedures that assume external consulting support

contracts become problematic when budget cuts or contract renegotiation reduce resource availability.

To mitigate the challenge of outdated documents, organizations should establish regular review cycles with

assigned ownership for each preparation document:

• Contact lists: Quarterly reviews with verification of current information.

• Playbooks: Exercise each playbook at least once per year and conduct a separate review on an offset

schedule. Scheduling exercises and reviews six months apart keeps playbooks validated and current

throughout the year. Update playbooks after each exercise or incident in which they were used.

• Policy documents: Annual reviews aligned with broader governance cycles.

Consider developing an annual exercise plan that maps each playbook to a scheduled exercise date. This

plan ensures all playbooks are validated throughout the year and provides auditors with evidence of a

structured review program.

Assign specific individuals responsible for keeping documents current and include document review in their

performance expectations. Organizations that treat documentation maintenance as an ongoing discipline

rather than a periodic project maintain more accurate and useful preparation materials. The investment in

keeping documents current pays dividends during incidents when responders can trust their guidance.

Organizational Change and Turnover

Personnel changes can erode the effectiveness of preparation when institutional knowledge leaves with

departing team members. The senior analyst who has responded to dozens of incidents carries irreplaceable

context about how systems actually behave, which stakeholders need careful handling, and which

documented procedures work better in theory than in practice. When that analyst departs, their

replacement inherits documentation but not the nuanced understanding that makes the response effective.

Turnover affects preparation beyond direct knowledge loss.  Relationships with stakeholders need to be

rebuilt as legal counsel, HR partners, and business unit leaders learn to trust new team members. Response

dynamics shift when team composition changes, requiring adjustment to communication patterns and role

assignments.

TABLETOP INJECT: SARAH’S DEPARTURE

I was working with a large media company on a series of tabletop exercises. The team was doing well,

demonstrating strong decision-making and communication skills. However, I noticed significant

reliance on the incident response team leader, Sarah, who had deep institutional knowledge.

Sarah had been with the company for over a decade and had led it through several high-profile,

public incidents. She knew the key stakeholders, the quirks of their systems, and the unwritten rules

governing organizational incident response. She had institutional knowledge and relationships that

the incident response team leaned on heavily.

After an hour into the two-hour exercise, I dropped an inject on the team:

“Sarah has been sequestered for jury duty and won’t be available for the rest of the exercise.

To the team’s credit, they responded professionally. Sarah sat back and observed as the rest of the

team adjusted to her absence, arms crossed. While secondary team members stepped up admirably,

the exercise quickly fell apart without Sarah’s guidance. Decisions slowed, communication faltered,

Prepare Activity | Chapter 7 | 129

and the team struggled to maintain cohesion, eventually falling into arguments and failing to

complete the exercise objectives.

The company’s Chief Information Security Officer (CISO) later thanked me for the input, recognizing

the risk of over-reliance on a single individual. When I spoke with Sarah afterward, she admitted the

experience was eye-opening. She had always known she carried significant institutional knowledge,

but watching her team struggle made the risk tangible in a way that abstract discussions about

succession planning never had. Sarah became a champion for cross-training initiatives, actively

mentoring teammates in leadership skills, and documenting the unwritten knowledge she had

accumulated.

Cross-training provides the foundation for turnover resilience:

• Rotate responsibilities: Ensure multiple team members can perform each critical function.

• Document reasoning: Explain why certain approaches work, not only which steps to follow.

• Pair experienced and new responders: During exercises and actual incidents when possible.

Knowledge transfer processes should begin before departures occur. Exit interviews that

capture undocumented knowledge and transition periods that allow for job shadowing help

preserve important institutional knowledge.

Consider creating knowledge repositories that capture lessons learned, incident post-mortems, and

informal guidance that might otherwise exist only in experienced responders' memories. These repositories

become particularly valuable when team composition changes or when responding to incident types not

encountered recently.

Demonstrating Value Without Incidents

Preparation investments face a fundamental measurement problem: success means incidents that do not

happen or impacts that do not materialize.

Cybersecurity leaders can struggle to justify preparation budgets when the primary benefit is avoiding

hypothetical future losses. Executives reasonably ask what the organization received for its investment, and

"we didn’t have a major incident" is an unsatisfactory measure of returns.

This challenge intensifies during budget discussions when preparation competes with projects that offer

more tangible returns. A new customer-facing feature delivers measurable revenue growth, while an

updated incident response plan delivers promised risk reduction that is difficult to quantify.

To better demonstrate the value of incident response preparation activities, organizations can track metrics

that demonstrate preparation value independent of actual incidents:

• Exercise performance: Response times during drills and improvement trends across exercises

• Capability gaps addressed: Issues identified during exercises and subsequently remediated

• Detection improvements : New detection rules deployed, false positive rates reduced, MTTD in

simulated scenarios

• Documentation currency: Percentage of documents reviewed on schedule

Tracking these metrics over time provides tangible evidence of progress in preparation that supports

budget discussions and resource allocation decisions.

BENCHMARKING PREPARATION INVESTMENTS

External reference points help justify investment levels in preparation. Industry surveys provide

concrete data for comparison: the SANS Institute 2025 SOC Survey found that 62% of SOC

professionals believe their organization is not doing enough to retain top staff, highlighting the

importance of training and development investments. [23]

The Ponemon Institute’s 2025 Cybersecurity

Threat and Risk Management Report found that 71% of organizations are increasing cybersecurity

budgets, with 51% now applying incident response plans consistently across the enterprise. [24]

Figure 46 | SANS 2025 SOC Survey Key Findings

In addition to industry survey analysis, use public incident case studies to contextualize the value of

preparation. When breaches at peer organizations make headlines, use them to illustrate the value of

investment in preparation. Document what controls the affected organization lacked and

demonstrate how existing preparation activities address similar gaps.

While the value of preparation is difficult to quantify precisely, organizations that consistently invest in

readiness respond more effectively when incidents occur. The challenge lies not in whether preparation

provides value, but in communicating that value to stakeholders who decide on resource allocation.

PREPARE ACTIVITY EXAMPLES

The following examples illustrate the importance of preparation in the incident response process.

Prepare Activity | Chapter 7 | 131

Building the Bridge Before the Flood

Dana joined Meridian Financial as the incident response team lead eight months ago. Her predecessor had

focused on technical capabilities: an impressive forensic lab and advanced detection tools. But Dana noticed

something troubling during her first month: when she needed to coordinate with other departments, she

was introducing herself to people who should have been close partners.

Dana started building relationships systematically. She scheduled monthly meetings with Ron in IT

operations, Rachel in Legal, and Vincent in Human Resources. Each conversation revealed coordination

gaps. Ron mentioned that his team recently migrated applications to cloud infrastructure without notifying

security. Rachel had handled a vendor breach notification as a contract matter, without involving incident

response. Vincent initially questioned why HR would need to coordinate with security until Dana explained

that premature technical actions during insider investigations can expose the organization to wrongful

termination claims.

Figure 47 | Meridian Financial Incident Response Team Coordination

Dana included these contacts in quarterly tabletop exercises focused on cross-functional coordination.

During one ransomware simulation, Ron discovered that his vendor contact list was outdated; Rachel

learned that the cyber insurance policy requires 24-hour breach notification; and Vincent realized that his

termination procedures conflicted with evidence preservation requirements. Each exercise revealed gaps

that could be addressed before they negatively impacted the organization.

Seven months after Dana joined, the preparation proved its value. A security analyst detected unusual data

access patterns from Thomas, a senior accountant with twelve years at the company. The pattern suggested

data staging for exfiltration of customer financial records.

Dana called Vincent within minutes. Because of their established relationship, she didn’t need to explain

who she was or why HR should care.

"We need to be careful here," Vincent said. "Thomas is well-respected. If we’re wrong, this could hurt his

reputation. But if we’re right, we need to act before more data leaves."

Vincent disclosed to Dana that Thomas recently submitted a resignation notice effective in two weeks,

information that significantly changed the risk calculation. Dana’s next call was to Rachel, who immediately

recognized the regulatory implications and advised on evidence preservation for potential law enforcement

referral.

Figure 48 | Meridian Financial Coordinated Response Timeline

Within two hours, Dana had a coordinated response plan in place. Ron’s team quietly disabled Thomas’s

remote access, citing a "routine security update." Legal had drafted a data hold notice. HR had

administrative leave documentation ready for immediate execution if the investigation confirmed malicious

activity.

Dana’s investment in relationships transformed a potential crisis into coordinated action. The relationships

she built weren’t just professional courtesy. Those relationships formed the foundation of an effective

response, as essential as forensic tools or detection systems.

Intelligence-Driven Detection

Isaac Morgan had three weeks to finish integrating threat intelligence feeds into Warren Health’s NDR

platform. The healthcare organization subscribed to an ISAC feed specific to the healthcare sector, and

Isaac configured the NDR to correlate network traffic with known indicators of compromise. His manager

questioned the time investment, but Isaac knew that detection without context was just noise.

The integration was straightforward but required careful tuning. Isaac mapped the STIX data indicators to

the NDR’s detection engine, focusing on infrastructure associated with threat actors known to target

healthcare organizations. He configured alerting thresholds to balance sensitivity against false positives,

testing with historical traffic samples before enabling production alerts.

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

Three weeks after completing the integration, Isaac received an alert that made the effort worthwhile.  The

Prepare Activity | Chapter 7 | 133

NDR flagged outbound connections from a workstation in the billing department to an IP address associated

with Velvet Tempest, a threat actor group known for targeting healthcare organizations with ransomware.

The ISAC had published the indicator just thirty-six hours earlier based on activity observed at another

healthcare provider.

Isaac pulled the alert details using AC-Hunter, their network threat detection platform.  The connections

were periodic, occurring every four hours, consistent with C2 beaconing behavior.  Without the CTI

integration, this traffic would have appeared as routine HTTPS connections to an uncategorized external

host. With the threat intelligence context, Isaac immediately recognized the severity.

Figure 49 | Velvet Tempest C2 Detection Alert

Within an hour, the incident response team had isolated the affected workstation and begun forensic

analysis. The investigation revealed that a billing specialist had opened a malicious attachment from a

phishing email two days earlier. The malware had established persistence but had not yet moved laterally or

accessed patient data.

Early detection through CTI integration transformed what could have been a ransomware incident into a

contained compromise. Isaac’s investment in preparation paid dividends in avoided downtime, preserved

patient data, and incident costs that never materialized.

PREPARE: STEP-BY-STEP

The following steps provide a condensed reference for preparation activities. Each step corresponds to

topics covered earlier in this chapter, organized for use when building organizational readiness, training the

incident response team, and strengthening proactive defenses.

This step-by-step guide is available for download in PDF and Markdown formats on the

companion website at dynamicincidentresponse.com.

Step 1. Prepare the Organization

1. Develop organizational policies that outline the organization’s approach to incident response, including:

◦ Company mission and goals for the incident response program.

◦ Priorities for the organization before, during, and following an incident.

◦ Policy on involving management teams in the organization, including GRC, legal, and public

relations.

◦ Policy on paying ransom or extortion.

◦ Policy on communicating with attackers.

◦ Policy on data retention and evidence preservation.

◦ Policy on reporting incidents to law enforcement, government, or industry partners.

◦ Policy on public disclosure of incidents.

◦ Policy on engaging with third-party incident response providers.

◦ Containment authorization policies defining who can authorize systems to be taken offline,

including tiered authorization levels (SOC/IRT-authorized actions like endpoint isolation, service

owner-authorized actions like server or service isolation, executive-authorized actions like shutting

down production systems or actions affecting regulated services).

◦ Recovery time objectives (RTO) and recovery point objectives (RPO) for critical systems.

◦ Evidence retention requirements and chain of custody procedures.

2. Develop management support for incident handling capability, including:

◦ Establish relationships with decision-makers before incidents occur.

◦ Communicate the value of incident response using industry examples and metrics.

◦ Seek management input on policy development.

◦ Define communication expectations during incidents.

◦ Assign management actionable responsibilities, such as participating in tabletop exercises or breach

simulations.

3. Identify critical assets and risk assessment processes, including:

◦ Identify systems and services essential to the organization’s survival, including revenue-generating

operations, customer-facing services, and regulatory compliance systems.

◦ Define risk tolerance thresholds for low, medium, high, and critical events.

◦ Develop incident classification criteria based on impact factors (systems affected, data sensitivity,

business impact, regulatory implications).

◦ Document classification matrix for rapid reference during incidents.

◦ Review and update criteria annually as the risk landscape evolves.

4. Develop an incident communications plan that addresses channels, contacts, reporting, and emergency

messaging, including:

◦ Establish communication channels that are secure and reliable:

▪ Select a primary communication platform with appropriate security controls.

▪ Identify a backup communication channel for use if the primary channel is compromised.

Prepare Activity | Chapter 7 | 135

▪ Test the communication channels periodically.

▪ Document platform access procedures.

◦ Document contact information for the team and important stakeholders:

▪ Internal contacts (IRT members, IT operations, legal, HR, executives).

▪ External contacts (law enforcement, regulators, insurance, retainer providers).

▪ Vendor and cloud provider security contacts.

▪ Establish a quarterly review process to maintain accuracy.

◦ Establish reporting procedures:

▪ Define reporting requirements by incident severity.

▪ Create report templates for different audiences.

▪ Establish service level agreements for initial and ongoing reports.

▪ Document distribution lists for each report type.

◦ Develop an emergency communication plan:

▪ Define notification triggers for different incident types.

▪ Establish approval workflows for internal and external communications.

▪ Create message templates for common scenarios.

▪ Identify constituent audiences (customers, partners, regulators, employees).

▪ Establish distribution channels for each audience.

▪ Designate and train spokespersons.

▪ Document applicable regulatory notification requirements (including GDPR, HIPAA, SEC, PCI

DSS, NIS2, DORA, and applicable breach notification laws).

◦ Establish external reporting channels for security researchers:

▪ Publish a security.txt file (RFC 9116) with contact, encryption, and disclosure policy information.

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

◦ Maintain offline access to the policy, carrier contacts, claims phone number, policy number, and

procedures for engaging the carrier’s approved incident response providers.

◦ Protect the policy from disclosure on attacker-accessible systems and during ransom negotiations.

◦ Identify independent legal counsel separate from the carrier’s breach coach.

8. Implement security awareness training, including:

◦ Develop training content covering incident recognition and reporting.

◦ Establish training frequency and completion tracking.

◦ Implement practical exercises (simulated phishing).

◦ Create clear reporting channels for suspicious activity.

Step 2. Prepare the Incident Response Team

1. Train the incident response team, including:

◦ Technical skills (SOAR, digital forensics, network analysis, malware analysis, log analysis, scripting,

and automation).

◦ Soft skills (communication, documentation, decision-making under pressure, leadership, and

negotiation).

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

◦ Configure forensic workstations with the necessary tools, including cloud-based workstations for

organizations with significant cloud infrastructure.

◦ Acquire and test evidence collection tools.

◦ Establish secure evidence storage with appropriate capacity.

◦ Prepare a jump bag for on-site response.

6. Prepare access to systems, including:

◦ Establish break-glass accounts secured with hardware tokens or a credential vault, with alerting on

use and periodic testing.

◦ Document access request procedures for incident response.

◦ Pre-authorize access where possible to reduce response delays.

◦ Document vendor and cloud provider support procedures.

7. Conduct tabletop exercises and incident response drills, including:

◦ Schedule regular exercises (monthly tabletop discussions, quarterly technical drills, annual full-scale

Prepare Activity | Chapter 7 | 137
