# Chapter 6: DAIR: A Dynamic Approach to Incident Response

identified and addressed. The linear models do not provide sufficient guidance on this important aspect of

the incident response process.

Inadequate Resource Prioritization Guidance

Few organizations have unlimited resources to respond to incidents.  When responding to an incident,

organizations need to prioritize available resources to respond effectively in alignment with business

imperatives.

Neither the NIST SP 800-61  nor the PICERL models call out the need for resource prioritization, which can

lead to inefficient resource use during incident response. This has the greatest impact when an incident

affects multiple systems used by an organization, as the organization may not have the resources to

respond to all affected systems concurrently. Further, aligning the business needs with the incident

response effort is an important factor in ensuring the response is effective.

Lack of Incident Verification Requirements

In some cases, the presence of an incident is immediately clear. A defaced website, for example, is an

obvious incident that requires a response. However, it may not always be clear that an event is an incident

that requires the attention of the incident response team.

For example, consider the case where an organization receives numerous user complaints that an

application server is slow or unresponsive throughout the workday. An investigation by the systems team

reveals that the server has several unexpected processes consuming significant CPU and memory. This

could represent an event that warrants a response from the incident response team, but it could also be a

misconfiguration or a performance issue that does not require an incident response effort.

While implicitly part of the detection and analysis phase in NIST SP 800-61 and the identification phase in

PICERL, neither process explicitly requires verifying that the event is an incident that requires a response.

This can lead to inefficient resource use and costly responses to events that interrupt other important work.

Lack of Root Cause Analysis

Understanding the root cause of an incident is important to effectively remedy future vulnerabilities.

Without understanding the root cause, organizations may find themselves responding to the same incident

multiple times, or failing to effectively remedy the vulnerability that led to it in the first place.

For example, consider an incident in which an organization is compromised due to a weak password on a

critical system. While changing the weak password would address the exploited vulnerability, root cause

analysis would indicate that several other considerations should also be addressed: password complexity

PART 2: A DYNAMIC APPROACH TO INCIDENT RESPONSE

In this section we’ll look at the process of incident response in a step-by-step approach. Using the Dynamic

Approach to Incident Response (DAIR) framework, we’ll examine each phase in the incident response

process, covering the key activities and tasks performed in each phase.

6 A Dynamic Approach to

Incident Response

Existing models for incident response are useful as a starting point, but they don’t fully capture the

complexity of modern incidents. A modern incident response model should be flexible and dynamic,

reflecting the reality that incidents are not linear and that the response process is iterative. The model

should accommodate the complexity of modern cyber incidents while taking into account organizational

priorities.

To support the modern needs of incident response teams, we have developed the Dynamic Approach to

Incident Response (DAIR, pronounced "dair"), as shown in Figure 22.

Figure 22 | Dynamic Approach to Incident Response (DAIR)

In the DAIR model, we see several waypoints that are similar to the incident response steps in PICERL and

NIST SP 800-61. However, how we apply the DAIR model and what we emphasize as essential actions are

different.

In the DAIR model, we begin the process with the prepare waypoint, which is essential for ensuring that the

Incident Response Team (IRT) is ready to respond to incidents. We then move to the detect waypoint, which

takes into account several elements of threat hunting and incident discovery as well as preparation efforts

for effective incident response.  When we detect an Event of Interest (EOI), we verify it to ensure that it is

indeed an incident and one that is important for us to respond to based on organization priorities. We then

triage the incident to prioritize it based on organizational objectives.

Next, we enter the response actions loop, where we scope the breadth of the incident, contain affected

systems, eradicate the known threats, and recover systems. The response actions loop continues as we

learn more about the incident, the attacker’s Tactics, Techniques, and Procedures (TTPs), the systems

involved, and the concerns of the business, all contributing more information for use in subsequent scoping,

eradication, and recovery.

After completing the response actions loop, we conclude the process with the debrief waypoint. At this

waypoint, we assess the strengths and weaknesses of the systems affected by the incident and our own

incident response actions to identify opportunities for improvement. Over time, we capture metrics to

measure the efficiency of the incident response process as well.

The DAIR model serves both as a reflection of the best practices developed intrinsically by incident

response teams, and as an opportunity to formalize the realities of modern incident response. Organizations

engaged in incident response regularly have learned the processes that work best and apply them as a

natural evolution of what fits their needs. The DAIR process aims to capture these practices and provide a

framework for applying them in a structured and repeatable way.

Before we dive into the details of the DAIR model, let’s first discuss the important elements of the model and

how they differ from existing incident response models.

WAYPOINTS, OUTCOMES, AND ACTIONS

Instead of thinking of incident response as multiple steps with a distinct beginning and end, it is better to

think in terms of waypoints, outcomes, and actions.

During an incident, there are usually multiple events occurring across time, some of which overlap (i.e.,

many things will happen at once). For example, the incident response team needs to detect an incident

before verifying it, but doesn’t stop everything because of an incident. Detection is an ongoing activity, and

Figure 23 | Stepped Approach to Incident Response

Figure 24 | Incident Response Waypoints and Actions

In the DAIR model, we emphasize the importance of waypoints, outcomes, and actions to better reflect the

dynamic nature of incident response, and to recognize the activities that are ongoing and iterative

throughout the incident response process.

COORDINATING WITH DECISION MAKERS

Figure 25 | Coordinating with Decision Makers

The background element surrounding the actions in Figure 25  denotes all the elements where we, as

incident response analysts, will seek insight from decision makers: important stakeholders, management,

executive leadership, and other people who reflect the interests of the organization.

As technical analysts, we bring expertise in threat detection, forensic analysis, and incident response

procedures. However, we cannot operate in isolation from the business priorities and operational realities

of the organization. Decision makers provide essential context about what matters most to the organization,

which systems are most critical, what data is most sensitive, and what operational impacts are acceptable

during an investigation.

The incident response team should actively seek guidance from decision makers throughout the incident

lifecycle. This collaboration ensures that investigative decisions align with organizational priorities rather

than pursuing every technical lead regardless of business impact. For example, decision makers can help the

IRT understand:

• Which systems and data are most critical to business operations

• What operational disruptions are acceptable during containment and recovery actions

• What regulatory, legal, or contractual obligations affect incident response decisions

• What communication and notification requirements exist for different incident types

• How to balance the need for thorough investigation against business continuity needs

This coordination ensures the IRT makes informed decisions that balance security imperatives with

operational realities.

Consider an example incident where an attacker has compromised multiple systems across the

organization, including both production database servers and employee workstations. The IRT has identified

IOCs on fifteen systems total: five production database servers that support customer-facing applications,

and ten employee workstations in the finance department. From a purely technical perspective, the team

might investigate all systems simultaneously using the same priority level.

However, by coordinating with decision makers, the IRT learns that:

• The production database servers generate $500,000 in revenue per hour, and any downtime requires

customer notification under Service Level Agreement (SLA) requirements

• The finance workstations are approaching the quarterly close period, making them critical for business

operations over the next two weeks

• The data owner for the finance systems indicates that the compromised workstations do not have

access to sensitive customer data, but do have access to internal financial records

• Executive leadership prioritizes maintaining customer service continuity while accepting some delay in
