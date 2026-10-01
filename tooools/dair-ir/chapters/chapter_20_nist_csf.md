# Chapter 20: Integrating DAIR with NIST CSF 2.0 Framework

> Source: PDF Pages 633-655 (Total Pages: 23)

OT-Specific Debrief Questions

Beyond the standard post-incident review topics covered in the debrief activity chapter, OT incidents raise

questions that only engineering and operations personnel can answer. These questions help the debrief

team evaluate whether the organization’s industrial architecture, engineering processes, and operational

awareness were sufficient to support an effective response.

• Cyber safe position and island mode.  Was cyber safe mode, manual operations, or island mode

considered during the incident? If executed, did it provide value for containment, scoping, or

eradication? If not executed, what prevented the transition?

• Engineering system exposure.  Were the engineering workstations, project repositories, or

configuration management systems exposed? Did the adversary gain the ability to interact directly with

PLC engineering tools or modify project files?

• Controller integrity verification.  Was the controller logic validated during recovery? Were logic

baselines available and trustworthy, and could the organization rapidly confirm controller integrity

through engineering tools or offline project comparisons?

• Protocol-level visibility.  Did the organization have sufficient OT-aware visibility into industrial

protocols (Modbus, EtherNet/IP, DNP3, PROFINET) to determine whether unauthorized control

commands or configuration changes occurred?

• Operational impact awareness. How quickly could responders determine whether the physical process

was affected? Did operators have sufficient visibility through HMIs, historians, and alarms to confidently

assess process state?

• Backup access and validation.  Did the organization have backup access to critical systems, such as

engineering workstation system images, HMIs, or historians, that could be used for validation and

recovery if primary access was compromised?

• Architectural trust relationships.  Which architectural decisions enabled adversary access or lateral

movement? Examples include shared Active Directory environments, vendor remote access pathways,

flat Level 3 networks, or insufficient segmentation between IT and control networks.

• Containment and operational risk decisions.  Were containment actions delayed, modified, or

sequenced to preserve controlled operations? Did responders have sufficient engineering context to

understand when isolating systems could affect process control, visibility, or required functions?

The answers to these questions reveal gaps that standard IT-focused debriefs often miss: weaknesses in

engineering workflows, blind spots in protocol-level monitoring, and architectural trust relationships that

enabled the adversary to access OT systems. Capturing these findings ensures that post-incident

improvements address the OT-specific conditions that shaped the incident, not the IT infrastructure

surrounding it alone.

Engineering and Architecture Improvements

The outcome of an OT debrief should be actionable technical improvements, including:

• Improved industrial protocol monitoring and detection engineering.

• Refinement of OT incident response playbooks, particularly containment sequencing.

• Enhanced controller baseline management and configuration tracking.

• Architectural changes to reduce unnecessary trust relationships.

• Improved segmentation between IT, OT, and remote access environments.

These improvements help ensure the organization is better prepared for the next incident and that

response capabilities evolve alongside the threat landscape.

Incident Response for Operational Technology | Chapter 19 | 609

OT IR lessons learned should also inform targeted OT tabletop exercises. These exercises should reflect

realistic operational scenarios such as loss of operator visibility, unauthorized engineering access, remote

vendor compromise, controller logic manipulation, or abuse of trusted industrial protocols.

THE FIVE ICS CYBERSECURITY CRITICAL CONTROLS

Effective OT incident response requires both cybersecurity expertise and industrial engineering knowledge.

OT response exists at the intersection of cyber defense and industrial engineering, where responders need

to understand not only how networks and adversaries behave, but also how physical processes operate and

how they can safely continue during disruption. A successful response depends on close collaboration

among IT security practitioners, OT cybersecurity specialists, operators, and engineers who understand the

systems that control the process. When these teams work together, responders gain the operational

awareness needed to distinguish real threats from operational noise and to take actions that protect both

digital systems and the physical environments they control.

Overall, succeeding in OT incident response is about being prepared to respond safely, deliberately, and

with engineering knowledge when an industrial incident inevitably occurs. The Five ICS Cybersecurity

Critical Controls, including the ICS dedicated response plan and related exercises, provide a practical

foundation for achieving this safety-focused and engineering-informed outcome. [9]

Together, they form an

adaptable set of controls that aligns with an organization’s risk model. They also directly support an

effective DAIR-based approach to OT threat detection, incident response, and recovery. Figure 199

illustrates the five controls and their relationships.

Figure 199 | The Five ICS Cybersecurity Critical Controls

#1 ICS-Specific Incident Response

The first and most critical control is OT-specific incident response. Effective OT incident response should

be operations-informed and engineered for control system realities, not adapted after the fact from IT

playbooks. This includes response plans that prioritize safety, process integrity, and controlled recovery

over speed alone. OT incident response capabilities should assume that attacks may target engineering

systems directly and may require responders to operate through an active incident while maintaining

control and visibility. Exercises and simulations are essential, but they should reflect real industrial risk

scenarios such as loss of view, manipulation of logic, and unauthorized remote access, not abstract cyber

events. Without control system-specific preparation, response efforts will either be too aggressive or too

slow, both of which introduce unacceptable risk.

#2 Defensible Control System Network Architecture

A defensible control system network architecture is the second pillar of success. Incident response is only

as effective as the architecture in which it operates. Proper segmentation, well-defined trust boundaries,

and industrial demilitarized zones enable responders to contain threats without unnecessarily disrupting

operations. Architecture should support visibility into control system traffic, asset identification, log

collection, and deterministic communication enforcement between systems. In poorly segmented

environments, responders struggle to determine scope, trace lateral movement, or assess the blast radius,

often leading to overly broad or disruptive response actions.

#3 OT Network Visibility and Monitoring

The third control, OT network visibility and monitoring, is foundational to nearly every phase of incident

response discussed in this chapter. Because most OT assets cannot host endpoint agents, continuous,

protocol-aware network monitoring becomes the primary source of forensic evidence. Visibility into

industrial protocols and system-to-system interactions enables responders to verify incidents, identify

affected assets and processes, and understand how adversaries interact with control systems. More

importantly, it enables defenders to distinguish malicious behavior from legitimate engineering activity,

reducing false positives and supporting safe response decisions.

#4 Secure Remote Access

Secure remote access forms the fourth control and represents one of the most frequently abused paths into

OT environments. Winning in incident response requires knowing exactly how remote access is

implemented, which users and vendors are authorized, and which systems can be reached. Secure designs

rely on time-based controlled access, strong authentication, such as multi-factor authentication where

feasible, and controlled jump hosts that provide both segmentation and monitoring. During incidents, these

access paths often become critical choke points for containment and investigation, making prior visibility

and governance essential.

#5 Risk-Based Vulnerability Management

The fifth OT cybersecurity critical control, risk-based vulnerability management, directly supports informed

response and recovery decisions. In OT environments, vulnerability management is not about patching

everything. It is about understanding which vulnerabilities matter, which systems can be safely updated,

and which risks need to be mitigated through compensating controls or monitoring. During an incident,

responders need to understand device operating conditions, existing safeguards, and potential exploit paths

to decide whether remediation should occur immediately, be deferred, or be monitored. This risk-based

approach ensures that response actions do not inadvertently compromise safety or reliability.

Together, these five controls enable effective, repeatable, and defensible OT incident response. They align

security operations with engineering realities discussed here, ensure that responders have the visibility and

context needed to make safe decisions, and reduce the likelihood that response efforts themselves become

a source of operational risk. When implemented cohesively, they transform incident response from an

improvised reaction into a controlled, engineering-led capability, one that supports safety, resilience, and

long-term operational trust.

Incident Response for Operational Technology | Chapter 19 | 611

[1] The Purdue Enterprise Reference Architecture (PERA), developed by Theodore J. Williams at Purdue University in the 1990s, defines

a hierarchical model for industrial network segmentation. It remains the most widely referenced framework for structuring OT

network zones and conduits. See ISA-95 (Enterprise-Control System Integration) and ISA/IEC 62443 (Industrial Automation and

Control Systems Security) for current standards that build on the Purdue model.

[2] IEC 61511, "Functional safety - Safety instrumented systems for the process industry sector," International Electrotechnical

Commission, www.iec.ch/homepage. IEC 61511 defines the requirements for specification, design, installation, operation, and

maintenance of Safety Instrumented Systems (SIS) in the process industry.

[3] The high-impact, low-frequency (HILF) risk classification is used in critical infrastructure sectors to describe events that are

unlikely but carry severe consequences. NERC applies this framework to bulk power system risk assessment. See NERC, "High-Impact,

Low-Frequency Event Risk to the North American Bulk Power System," June 2010, www.nerc.com/pa/CI/Resources/Documents/

High-Impact_Low-Frequency_Event_Risk_to_the_North_American_Bulk_Power_System_-_2010.pdf

[4] CISA, "Compromise of U.S. Water Treatment Facility," Alert AA21-042A, February 2021, www.cisa.gov/news-events/cybersecurity-

advisories/aa21-042a

[5] Miller, Ben, "Recommendations Following the Oldsmar Water Treatment Facility Cyber Attack," Dragos, Inc., February 2021,

www.dragos.com/blog/industry-news/recommendations-following-the-oldsmar-water-treatment-facility-cyber-attack/

[6] CISA, NSA, FBI, and international partners, "People’s Republic of China State-Sponsored Cyber Actor Living off the Land to Evade

Detection," Joint Cybersecurity Advisory, February 2024, www.cisa.gov/news-events/cybersecurity-advisories/aa24-038a

[7] Locard’s Exchange Principle, attributed to French forensic scientist Edmond Locard (1877-1966), holds that every contact between

two items results in an exchange of material. In digital forensics, the principle is applied broadly: any interaction with a system leaves

traces, whether in logs, memory, network traffic, or configuration state.

[8] The concept of transitioning to manual operations or "island mode" during OT incidents is discussed in SANS, "The Five ICS

Cybersecurity Critical Controls," and in Dragos, "ICS/OT Cybersecurity Year in Review," www.dragos.com/year-in-review/

[9] SANS Institute, "The Five ICS Cybersecurity Critical Controls," www.sans.org/white-papers/five-ics-cybersecurity-critical-

controls/

20 Integrating DAIR with

NIST CSF 2.0

Organizations operating under regulatory requirements, government contracts, or industry mandates often

face a dual challenge: they need to demonstrate compliance with established frameworks while also

responding effectively to real-world incidents. For many organizations, particularly US federal agencies and

critical infrastructure operators, NIST SP 800-61 Revision 3 and the Cybersecurity Framework (CSF) 2.0

define the compliance needs for incident response. [1]

The Dynamic Approach to Incident Response (DAIR)

provides the tactical methodology these organizations need to operationalize CSF 2.0 requirements while

achieving practical incident response effectiveness.

This chapter explores how DAIR activities map to CSF 2.0 functions, demonstrating that compliance and

operational effectiveness are not mutually exclusive goals. Organizations can satisfy audit requirements,

generate necessary documentation, and demonstrate control effectiveness while using DAIR’s dynamic

approach to handle incidents more thoroughly than traditional linear models allow. The integration

between the DAIR model and CSF 2.0 creates a practical framework in which compliance is achieved

through effective response activities rather than being treated as a separate administrative burden.

UNDERSTANDING NIST SP 800-61 R3 AND CSF 2.0

The release of NIST SP 800-61 Revision 3 represents a fundamental shift in how NIST positions incident

response within organizational cybersecurity programs. Where Revision 2 provided specific incident

handling procedures and a four-phase lifecycle model, Revision 3 reframes incident response as an

integrated component of enterprise cybersecurity risk management. This shift reflects an important

evolution in cybersecurity thinking: effective incident response cannot exist as an isolated function.

Response capabilities are influenced by and influence governance decisions, asset identification, protective

controls, detection mechanisms, and recovery planning.  The CSF 2.0 framework captures these

interdependencies through six core functions that provide a common language for describing and

organizing cybersecurity activities.

In this section, we’ll walk through each of the six CSF functions and how they relate to incident response

capabilities, then examine the specific compliance obligations that organizations subject to CSF 2.0 face.

Integrating DAIR with NIST CSF 2.0 | Chapter 20 | 613

The Six CSF Functions

The CSF 2.0 framework organizes cybersecurity activities into six functions, each relevant to incident

response capabilities:

Govern (GV)

The Govern function establishes the organizational context for cybersecurity activities. This includes

cybersecurity risk management strategy, expectations, and policy that are communicated and monitored

across the organization.

For incident response, the Govern function addresses how organizations define incident severity

thresholds, establish escalation procedures, allocate response resources, and integrate incident handling

with enterprise risk management. Organizations demonstrate compliance by documenting how incident

response decisions align with broader organizational risk tolerance and strategic objectives.

Identify (ID)

The Identify function ensures organizations understand their current cybersecurity risks. This involves

maintaining awareness of assets, vulnerabilities, threats, and potential business impacts.

Effective incident response depends on this understanding: responders need to know which systems are

critical, what data requires protection, and how different systems interconnect. The Identify function also

encompasses threat intelligence activities that inform detection strategies and response priorities.

Protect (PR)

The Protect function encompasses safeguards that manage cybersecurity risks before incidents occur.

While primarily preventive, protective controls directly impact incident response by influencing the attack

surface, available evidence sources, and recovery options. Incident response teams benefit from protective

controls such as network segmentation, access management, and data protection mechanisms that limit

incident scope and preserve forensic artifacts.

Detect (DE)

The Detect function covers capabilities for finding and analyzing cybersecurity attacks and compromises.

This function aligns most directly with the early stages of incident response, encompassing the monitoring,

alerting, and initial analysis activities that transform security events into actionable incident reports.

Detection capabilities determine how quickly organizations identify incidents and how much context

responders have when beginning their investigation.

Respond (RS)

The Respond function addresses actions taken in response to detected cybersecurity incidents. This is

where the bulk of tactical incident response activity occurs, including analysis, containment, eradication,

and communication activities. The Respond function explicitly recognizes the need for iterative response

activities that adapt based on new information discovered during the incident.

Recover (RC)

The Recover function focuses on restoring assets and operations affected by cybersecurity incidents.

Recovery activities include restoring system availability, rebuilding trust with stakeholders, and

implementing improvements that prevent recurrence. The Recover function also encompasses post-

incident activities that capture lessons learned and improve organizational resilience.

These six functions provide the structure within which organizations demonstrate incident response

capability maturity and compliance.

What Compliance Requires

Organizations subject to CSF 2.0 requirements face several compliance obligations related to incident

response, summarized in Table 60.

Table 60 | CSF 2.0 Incident Response Compliance Requirements

REQUIREMENT DESCRIPTION

Documented

Capabilities

Organizations should document incident response capabilities across all relevant

CSF functions, describing detection methods, response procedures, decision

authority, and external coordination. Documentation provides the foundation for

demonstrating that capabilities exist and are maintained.

Demonstrated

Effectiveness

Organizations should demonstrate that incident response capabilities function as

intended through exercises, tabletop scenarios, or actual incident response

activities. Auditors look for evidence that documented procedures are followed in

practice and produce intended outcomes.

Metrics and

Measurement

Organizations should establish baselines for incident response metrics including

detection time, response time, containment effectiveness, and recovery duration.

Tracking trends over time demonstrates continuous improvement.

Continuous

Improvement

Organizations should learn from incidents and improve capabilities over time

through post-incident reviews, procedure updates based on lessons learned, and

root cause remediation. Compliance assessments examine mechanisms for

capturing and acting on incident-related learning.

The challenge for many organizations lies in bridging the gap between these compliance requirements and

practical incident response operations. CSF 2.0 provides the strategic framework, but organizations need

tactical methodologies to implement these requirements effectively.

DAIR AS CSF 2.0 IMPLEMENTATION

The DAIR model provides the tactical methodology organizations need to meet CSF 2.0 requirements.

DAIR’s activities map directly to CSF functions, creating a practical implementation path that satisfies

compliance requirements while improving the efficacy of incident response operations. This alignment is

not coincidental: the DAIR model was developed to reflect incident response best practices, and CSF 2.0

was designed to capture effective cybersecurity activities.

When organizations adopt effective incident response practices, they often discover that

compliance follows naturally. Frameworks like CSF 2.0 codify what experienced

practitioners already do. The DAIR model formalizes these practices, making it easier to

Integrating DAIR with NIST CSF 2.0 | Chapter 20 | 615

demonstrate compliance without changing how effective incident response teams work.

Next, we’ll map each DAIR activity to the CSF function it satisfies, examine how iterative response generates

stronger compliance evidence than linear models, and show how Decision Maker coordination throughout

the response satisfies the Govern function.

Mapping DAIR Activities to CSF Functions

The relationship between the DAIR model and CSF 2.0 becomes clear when examining how specific DAIR

activities address each CSF function.

Figure 200 provides an overview of how the six core CSF functions align with the DAIR model structure.

Table 61 provides additional context and detail supporting this alignment, showing the DAIR activities that

correspond to each CSF function and explaining how those activities satisfy compliance requirements.

Organizations can use this mapping as a reference when documenting their incident response capabilities

for compliance assessments.

Figure 200 | DAIR Model Mapped to NIST CSF 2.0 Functions

Table 61 | DAIR Activities Mapped to CSF 2.0 Functions

CSF FUNCTION DAIR ACTIVITIES HOW DAIR SATISFIES REQUIREMENTS

Govern (GV) /

Identify (ID)

Decision

Maker

coordination

throughout all

activities

Decision Maker coordination aligns response with organizational

risk tolerance and provides context about critical assets, acceptable

impacts, and strategic considerations, satisfying the Identify

function’s organizational context requirements. Govern function

coverage is mapped at the CSF category level in Table 62.

Protect (PR) Prepare

activities

The DAIR model Prepare waypoint encompasses proactive controls

and readiness activities that align with the Protect function.

Preparation includes establishing response procedures, deploying

detection capabilities, configuring systems for forensic readiness,

and training response personnel. These activities create protective

capabilities that limit the impact of incidents and inform effective

response actions.

Detect (DE) Detect, Verify,

and Triage

activities

The DAIR model explicitly addresses incident detection and adds

verification and triage activities that ensure detection capabilities

function effectively. The Verify activity confirms that detected

events represent actual incidents requiring response, while the

Triage activity prioritizes incidents based on organizational impact.

Together, these activities satisfy Detect function requirements for

finding and analyzing potential compromises.

Respond (RS) Response

Actions Loop

(Scope,

Contain,

Eradicate,

Recover)

The Response Actions Loop represents DAIR’s core contribution to

the Respond function. By structuring response as an iterative cycle

rather than a linear sequence, the DAIR model ensures thorough

incident handling that adapts to new discoveries. Each iteration

through Scope, Contain, Eradicate, and Recover activities generates

evidence of comprehensive response effort.

Recover (RC) Recover

activities and

Debrief

The DAIR model’s Recover activities restore affected systems to

operational status, while the Debrief activity captures lessons

learned and identifies improvement opportunities. Together, these

activities satisfy Recover function requirements for restoration and

continuous improvement.

This mapping demonstrates that organizations using the DAIR model for incident response are already

performing activities that satisfy CSF 2.0 requirements. Organizations adopting the DAIR model need only

document these activities in a way that makes compliance visible to assessors and auditors.

The Value of Iterative Response for Compliance

DAIR’s iterative Response Actions Loop provides particular value for CSF 2.0 compliance. Traditional linear

response models can leave organizations vulnerable when incidents require multiple remediation attempts

or when a new scope is discovered after initial containment. Under linear models, returning to earlier

phases might appear as process failure or incomplete response in subsequent audits.

The DAIR model reframes this iteration as expected and appropriate behavior. Each cycle through the

Response Actions Loop adds greater thoroughness to incident handling. Multiple iterations generate

additional documentation, demonstrate adaptive response capability, and provide evidence of

Integrating DAIR with NIST CSF 2.0 | Chapter 20 | 617

comprehensive remediation effort. Organizations can present iteration counts as positive metrics rather

than evidence of failure.

When documenting iterations, record what new information triggered each cycle and what

additional remediation occurred as a result. This documentation transforms iteration from

an apparent weakness into evidence of thorough, adaptive, and considered incident

response actions.

This reframing has practical compliance implications. When auditors review incident response records, they

may question why incidents required extended response periods or multiple remediation attempts. Under

the DAIR model, organizations can explain that the iterative response is by design: each cycle incorporates

new information, appropriately expands scope, and improves overall response effectiveness. This

explanation, supported by documentation from each iteration, demonstrates a mature incident response

capability rather than a process deficiency.

Decision Maker Integration and the Govern Function

DAIR’s emphasis on Decision Maker coordination aligns with the CSF 2.0 Govern function across the

response lifecycle. The Govern function requires organizations to establish and communicate a

cybersecurity risk management strategy across the enterprise, with assessors expecting evidence that

incident response decisions reflect that strategy in practice rather than as stated intent.

In the DAIR model, Decision Makers are not involved just at the beginning or end of incidents. They provide

ongoing guidance throughout the response lifecycle, informing decisions about scope expansion,

containment approaches, acceptable operational impacts, and recovery priorities. This continuous

coordination produces records that map directly to CSF 2.0 Govern categories, as shown in Table 62.

Table 62 | DAIR Activities Mapped to CSF 2.0 Govern (GV) Categories

GV

CATEGORY

ASSESSOR EXPECTATIONS DAIR ACTIVITIES ARTIFACTS GENERATED

GV.OC:

Organizatio

nal Context

Documentation showing

that incident response

decisions reflect the

organization’s regulatory

obligations, stakeholder

expectations, risk appetite,

and business environment.

Prepare: regulatory

notification mapping,

stakeholder identification,

risk classification criteria

definition. Verify and

Triage: per-incident risk

classification decisions

documented against pre-

agreed thresholds.

Risk classification

framework, triage decision

records showing

classification rationale,

regulatory notification

trigger log.

GV.RM:

Risk

Manageme

nt Strategy

Evidence that residual risk

at incident closure is

formally assessed,

accepted by an authorized

individual, and fed back

into the enterprise risk

register.

Response Actions Loop:

loop exit risk acceptance

decision. Debrief: lessons

learned mapped to risk

register entries. Recover:

recovery metrics feeding

program-level trend

analysis.

Signed loop exit risk

acceptance record, debrief

report with risk register

update recommendations,

metrics trend data

submitted to enterprise

risk function.

GV

CATEGORY

ASSESSOR EXPECTATIONS DAIR ACTIVITIES ARTIFACTS GENERATED

GV.RR:

Roles,

Responsibil

ities, and

Authorities

A defined authority matrix

for incident response

covering declaration,

command, business-impact

decisions, loop exit, and

post-incident improvement

ownership, using named

roles rather than generic

titles.

Prepare: incident response

team structure, RACI

matrix, escalation

thresholds, and decision

authority documented

prior to incidents (see

Document Incident

Response Decision

Authority).

Incident response

authority matrix, escalation

procedure documentation,

named role assignments

per incident type or

severity tier.

GV.PO:

Policy

Documented cybersecurity

policies that reflect

organizational context,

including an incident

response policy that

distinguishes policy (what

should happen), procedure

(how it happens), and

playbooks (how it happens

for specific scenario types).

Prepare: incident response

plan, playbooks,

communication plan,

contact lists, callout

rosters. Documentation

should use policy,

procedure, and playbook

taxonomy consistently to

facilitate assessor review.

Incident response policy

document, procedure

documents per DAIR phase,

scenario-specific

playbooks, communication

plan with last-reviewed

timestamp.

GV.SC:

Supply

Chain Risk

Manageme

nt

Evidence that third-party

and supplier incident

response obligations are

defined, that contractual

notification requirements

are mapped, and that

supplier access revocation

is addressed in incident

response procedures.

Prepare: supplier incident

response obligation

mapping, data processing

agreement review

schedule, third-party

access inventory. Scope

and Contain: third-party

access revocation

procedures. Debrief:

supplier-related root cause

and remediation tracking.

Supplier incident response

obligations register, data

processing agreement and

contract review records,

third-party access

revocation log, post-

incident supplier

remediation tracking.

Organizations can demonstrate Govern function compliance by producing the artifacts in the Artifacts

Generated column and linking them to the incident records that generated them. This CSF category-level

documentation shows that incident response operates within the organization’s broader risk management

framework rather than as an isolated technical function.

MEETING COMPLIANCE THROUGH DAIR ACTIVITIES

Effective incident response generates substantial documentation as a natural byproduct of response

activities. Organizations using the DAIR model can structure this documentation to satisfy compliance

requirements without creating separate administrative processes. The key lies in recognizing the

compliance artifacts already present in DAIR operations and formatting them appropriately for assessment.

In this section, we’ll identify the compliance artifacts that DAIR activities generate naturally, work through

how those artifacts demonstrate control effectiveness across CSF functions, and examine how to organize

and present this documentation to satisfy audit and assessment requirements.

Integrating DAIR with NIST CSF 2.0 | Chapter 20 | 619

Compliance Artifacts from DAIR Activities

Compliance assessments require organizations to produce tangible evidence that incident response

capabilities exist, function as intended, and improve over time. Assessors and auditors expect specific

artifacts that demonstrate coverage across CSF functions, and organizations that cannot supply this

evidence risk compliance gaps regardless of how effective their actual response operations are. When

applying the DAIR model, each waypoint generates documentation that serves these compliance purposes

as a natural byproduct of response activities.

Table 63 summarizes the artifacts generated by each DAIR phase and the CSF functions they address.

Table 63 | Compliance Artifacts by DAIR Phase

DAIR PHASE ARTIFACTS GENERATED CSF FUNCTION

Prepare Incident response plans, playbooks, contact lists,

training records, CSF function cross-references in

response procedures

Protect (PR)

Detect / Verify /

Triage

Alert logs, monitoring dashboards, threat

intelligence reports, triage decisions, false positive

records, incident declaration documentation

Detect (DE)

Response Actions

Loop (Scope, Contain,

Eradicate, Recover)

Scoping analysis, containment decisions,

eradication records, and recovery verification,

accumulating across iterations into a

comprehensive response record

Respond (RS)

Debrief Lessons learned reports, root cause analysis,

improvement recommendations, implementation

tracking records

Recover (RC)

Decision Maker

coordination

(throughout)

Stakeholder consultation records, guidance

documentation, business impact assessments,

risk-aligned decision rationale

Govern (GV) / Identify

(ID)

These artifacts accumulate naturally through DAIR operations, with each iteration through the Response

Actions Loop adding to the evidence base. Tracking the implementation of improvement recommendations

from debriefs provides additional evidence of program maturation.

Organizations should ensure that documentation captures the rationale for decision-

making in addition to the actions taken, to satisfy CSF compliance artifact requirements.

Organizations that maintain thorough documentation throughout DAIR activities will find that most

compliance artifacts already exist. The remaining task is to organize and present this documentation in

formats that assessors expect.

Demonstrating Control Effectiveness

CSF 2.0 compliance requires organizations to demonstrate that controls function as intended, not merely

that they exist. The DAIR model provides multiple opportunities to demonstrate control effectiveness

through actual incident handling.

Table 64 maps each CSF function to the types of evidence organizations can produce and the DAIR activities

that generate them.

Table 64 | Control Effectiveness Evidence by CSF Function

CSF FUNCTION EVIDENCE OF EFFECTIVENESS DAIR SOURCE ACTIVITIES

Detect (DE) Incidents identified through monitoring and

alerting rather than external notification or

chance discovery. Metrics such as Mean Time

to Detect (MTTD) provide quantitative

evidence of detection capability.

Detect, Verify, Triage

Respond (RS) Containment limited incident scope,

eradication removed attacker presence, and

iterative response addressed additional

incident elements that a linear approach might

have missed.

Response Actions Loop (Scope,

Contain, Eradicate, Recover)

Recover (RC) Successful system restoration, validation of

restored system integrity, and implementation

of improvements that prevent recurrence.

Recover, Debrief

Each iteration through the Response Actions Loop strengthens the evidence of response effectiveness by

demonstrating that the organization adapted to new findings and addressed them systematically.

Satisfying Audit Requirements

Audit and assessment activities typically examine incident response capabilities through document review,

interviews, and evidence examination. Organizations using the DAIR model can prepare for these

assessments by maintaining organized documentation and training response personnel to explain DAIR

concepts in CSF 2.0 terms.

Start by organizing incident documentation to align with CSF functions. Auditors often structure their

assessments around CSF categories and subcategories, so documentation organized in the same way

reduces assessment friction.

Cross-reference DAIR activities to CSF functions in response plans and procedures to make the mapping

explicit, as in the example shown in DAIR Activities Mapped to CSF 2.0 Functions . Response personnel

should understand how DAIR activities relate to CSF 2.0 requirements. When auditors ask about detection

capabilities, personnel can explain DAIR’s Detect and Verify/Triage activities and describe the Response

Actions Loop when asked about response procedures.

Incident records should be maintained in formats that facilitate evidence review, since auditors typically

request specific documents such as incident reports, timeline reconstructions, and lessons learned

summaries. Having these documents readily available in standardized formats demonstrates program

maturity and reduces assessment burden.

By integrating compliance considerations into routine DAIR operations, organizations avoid the scramble of

Integrating DAIR with NIST CSF 2.0 | Chapter 20 | 621

preparing for assessments after incidents. Compliance becomes a natural outcome of effective incident

response rather than a separate administrative burden.

INCIDENT TRACKING PLATFORM CONFIGURATION

Organizations can configure their incident response tracking tooling to support both effective operations

and compliance requirements. Careful incident tool configuration reduces manual effort and ensures that

compliance artifacts are generated consistently.

In this section, we’ll cover the ticketing and case management configurations that capture both operational

coordination and compliance evidence, and the communication templates that document incident progress

in CSF terminology.

Ticketing and Case Management

Incident tracking systems serve as the primary documentation platform for most organizations, whether a

system like JIRA or Remedy, or a specialty incident response tracking system. Organizations that need to

comply with CSF functions while adopting the DAIR model can configure these systems to capture

information for both operational coordination and compliance demonstration.

To best capture CSF function activities, configure incident status fields to reflect CSF vocabulary supported

by DAIR activities. Status options might include Detection Complete, Verification Pending, Containment

Active, Eradication in Progress, and Recovery Underway. These statuses map directly to CSF functions and

generate records that demonstrate function coverage. Workflows can support DAIR’s iterative approach,

allowing incidents to cycle through Response Actions Loop phases multiple times without treating iteration

as undesirable backtracking.

Where possible, include fields to document Decision Maker involvement, identify which stakeholders were

consulted, record the guidance they provided, and note how their input influenced response activities. This

documentation satisfies the CSF Govern function’s requirements for risk-aligned decision-making.

Configure the system to link evidence artifacts to specific incident records so compliance reviewers can

locate relevant evidence and ensure it is preserved in accordance with incident retention policies.

Communication Templates

Most communication templates should be developed during preparation as part of the Emergency

Communication Plan (see Develop an Emergency Communication Plan ), including a template set for each

major incident-type category to support consistent messaging during the first twenty-four hours. The

integration with CSF 2.0 lies in how those prepared templates are tagged and adapted for compliance

reporting during the response.

When communicating about incident status, tag updates with the CSF function and DAIR activity that

produced them. For example, an update describing initial scoping work would identify CSF Respond

function activity in the DAIR Scope phase, while recovery validation would identify CSF Recover function

activity. This consistent vocabulary demonstrates organizational fluency with the compliance framework

and produces records that map directly to CSF function coverage during assessor review.

Create template variants for different audiences. Executive communications should summarize impact and

progress, while technical communications should include detailed activity descriptions in DAIR waypoint

terminology. Both variants should support compliance by documenting appropriate information for their

respective audiences.

Tool configuration investments that optimize processes and guide analyst documentation

are valuable in the long term. Setting expectations for note-taking reduces manual effort

and improves documentation consistency. Organizations should review their tooling

periodically to ensure configurations continue to support both operational and compliance

needs.

INTEGRATING DAIR WITH NIST CSF 2.0

The integration of the DAIR model with NIST CSF 2.0 demonstrates that compliance and operational

effectiveness reinforce rather than conflict with each other. The DAIR model provides the tactical

methodology that organizations need to implement CSF 2.0’s strategic vision for incident response, with

activities that map directly to all six CSF functions. The Response Actions Loop operationalizes CSF 2.0’s

expectation for adaptive, iterative response. Decision Maker coordination satisfies the CSF Govern function

requirements for risk-aligned decision-making.

Each DAIR waypoint generates compliance artifacts as a natural byproduct of response operations, from

preparation documentation and detection records through response action logs and post-incident debrief

reports. These artifacts demonstrate control effectiveness across detection, response, and recovery

functions, providing assessors with tangible evidence of capability maturity. Organizations that document

decision rationale alongside response actions strengthen this evidence further by showing that incident

handling operates within their broader risk management framework. Further, configuring incident-tracking

platforms and communication templates to reflect both DAIR terminology and CSF vocabulary reduces the

manual effort required for compliance preparation.

When compliance considerations are integrated into routine DAIR operations, organizations avoid the

scramble of assembling evidence after the fact. The result is an incident response capability that is both

demonstrably compliant and genuinely effective.

Integrating DAIR with NIST CSF 2.0 | Chapter 20 | 623

[1] Incident Response Recommendations and Considerations for Cyber Risk Management, retrieved from nvlpubs.nist.gov/nistpubs/

SpecialPublications/NIST.SP.800-61r3.pdf.

Afterword

My kids went to a private school. Not big, not fancy, just a small school where teachers and administrators

were devoted to each student and given the time to help everyone shine. I was active at the school as a

parent and occasionally helped with networking support and minor system administration tasks.

One day, the head of school, Elsie, called me. She had received an email from a job candidate who wanted to

share their resume. Elsie opened the attached PDF.

Except it wasn’t a PDF. It was a script that ran CryptoLocker malware on her system.

Elsie had been the head of school for thirty years. She had seen students all the way through their school

years, later watched them get married and have kids of their own, and then welcomed those kids to the

same school. She was committed and dedicated like few people I have met, giving every student an amazing

experience and supporting them in their pursuits long after they left.

Like me, Elsie is a photographer, and she has hundreds of thousands of pictures from her time as head of

school. Every student, every teacher, every administrator. Every field trip, every fundraiser, every

celebration. Every one of them was being ransomed.

Elsie called me, desperate for help recovering her photo archive. I asked her about backups. She had one,

but it was attached to her system when she opened the email attachment. The backup was lost, too.

After some investigation and analysis, I told Elsie she had two options: pay the ransom or lose her files. We

retained the encrypted files in case a decryption key ever becomes available, but to date, we have had no

such luck. Elsie felt it was immoral to pay what amounted to extortion, and she lost the vast majority of her

photography, the visual history of her time as head of school.

In the grand scheme of cybersecurity incidents, this was relatively minor. I have supported analysts on

much larger ransomware cases, worked on the incident response team for large-scale breaches, and

provided expert witness testimony for breaches involving more than a million compromised devices. But

Elsie’s story is one that I think about often.

I was not responsible for her IT support, but I regret not being able to offer her more help before it

mattered. I wish I had volunteered some time to help prepare her and the school’s IT staff for the threat of a

cybersecurity incident, so they might have been better positioned to respond. A conversation about offline

backups, a brief review of how the school handled email attachments, and even a short discussion about

what to do when something goes wrong. None of that would have been difficult, and any of it might have

changed the outcome.

That regret is part of why this book exists.

Incident response does not always involve nation-state adversaries, advanced persistent threats, or

breaches that make headlines. Sometimes it is a school administrator who opened the wrong attachment

and lost thirty years of photographs. The scale varies, but the pattern is consistent: organizations that have

thought through preparation, detection, and response before a crisis have better outcomes than those that

have not. That is not a complicated insight, but it is one we, as a community of cybersecurity professionals,

have struggled to consistently put into practice.

The Dynamic Approach to Incident Response is my attempt to bridge that gap. This book is not a

comprehensive guide to every forensic technique, every detection rule, or every cloud platform’s logging

capabilities. Those topics deserve, and in many cases already have, dedicated resources. What I have tried to

do is provide a framework for thinking about incident response as a discipline, one that adapts to the

realities of modern threats rather than forcing them into a sequence of steps that made more sense thirty-

five years ago.

No framework survives contact with a real incident perfectly intact, and DAIR is not meant to be followed

from top to bottom like a checklist. The organizations and teams I have seen respond most effectively are

the ones that take a framework like this, test it against their own infrastructure and threat landscape, and

refine it through tabletop exercises, after-action reviews, and honest conversations about what went

wrong. DAIR is a starting point, not a destination.

Incident response is difficult work, and the people who do it carry more weight than most organizations

realize.

Throughout this book, I have written about analysts and responders in the third person, as practitioners

applying a framework. But you, the reader, are not an abstraction. You are the person who gets the call at 2

AM, who has to explain to leadership what happened before you fully understand it yourself, who stays

focused when everything around you is urgent and uncertain.

The work you do matters more than most people will ever know. When you respond to an incident well, the

story ends quietly. Systems come back online, operations resume, and the organization moves forward.

There is no headline for the breach that was contained before it spread, no award for the responder who

caught the persistence mechanism on the second pass through the logs. The absence of disaster is hard to

celebrate, but it is the direct result of your preparation, your judgment, and your effort.

You are going to face incidents where the framework does not have a clean answer, where the scope keeps

expanding, and where you have to make a call with less information than you would like. That is not a failure

of preparation. That is the job. Trust your training, lean on your team, and keep iterating.

I wrote this book so that the next time you get that call, you have a better starting point. I hope it serves you

well.

Index

@

$MFT, 208

3-2-1-1-0 backup rule, 536

A

AAA, 542

AAR, 419, 550, 582

AC-Hunter, 134

access keys, 578

account remediation, 335

account restrictions, 221

active data destruction, 226

Active Directory, 234, 337, 389, 547

cryptographic materials, 337

forest trusts, 364

krbtgt reset, 229

PDC emulator, 401

recovery, 400

Tier-0 assets, 368

active session termination, 234

AD (see Active Directory)

After-Action Review (see AAR)

AI

agentic systems, 496

code analysis, 456

commercial providers, 450

data handling, 452, 499

deobfuscation, 456

evolving threat, 553

frontier models, 448

generative, 448

hallucination, 450

human in the loop, 145

hype cycle, 448

inference constraint, 511

information synthesis, 449

limitations

context window, 471

training cutoff, 450

log analysis, 464

one-shot learning, 455

pattern recognition, 449

prompting, 452

query generation, 465

ReAct agent, 505

security

prompt injection, 499

Shadow AI, 448

Sigma rules, 515

threat actors, 504

threat evolution, 23

unsupervised learning, 144

verification requirements, 503, 513

AI interaction logs, 513

AI tools

Claude Code, 504

Google Gemini, 457

AitM, 524

Akira ransomware, 362

alert fatigue, 154

AlienVault OTX, 171

Amazon ECS (see AWS, ECS)

Amazon Web Services (see AWS)

AmCache, 243

anti-forensic techniques

fsutil setZeroData, 294

living off the land, 208

log deletion, 207

log flooding, 208

log replay, 208

timestomping, 208

AnyDesk, 362

API keys, 348

API-based isolation, 253

AppArmor, 232

application control

AppArmor, 232

AppLocker, 232

Gatekeeper, 232

AppLocker, 232

ASM, 120

assume-role policies, 324

atomic IOC, 43

Atomic Red Team, 122

Attack Surface Monitoring (see ASM)

attack surface monitoring, 120

Attacker in the Middle (see AITM)

attacks

anti-forensics, 207

business email compromise, 311

cloud data theft, 561

credential abuse, 37

credential-based

credential stuffing, 7

password spraying, 7

encryptionless extortion, 526

golden ticket, 339

human-operated ransomware, 525

IMDS exploitation, 572

lateral movement, 367

living off the land, 360, 602

OAuth token abuse, 309

supplier-side BEC, 314

supply chain, 322

vulnerability exploitation, 37

water treatment, 602

wiper, 526

audit logging, 499

auditd, 387

auditpol, 386

Authentication, Authorization, and Accounting (see

AAA)

authority matrix, 97

automated enrichment, 498

autonomous adversaries, 504

Autopsy, 100

Autoruns, 330

AWS, 209

CloudFormation, 324, 583

CloudTrail, 18, 209, 263, 323

EC2, 14, 566

ECS, 584

GuardDuty, 153, 263, 566

IAM Identity Center, 565

Lambda, 334, 579

Object Lock, 583

S3, 181, 325, 583

Security Groups, 253

snapshots, 396

VPC Flow Logs, 116, 302, 584

AWS Security Groups, 253

Azure, 209

Activity Log, 209, 323

Blob Storage, 154, 213, 325, 577, 584

Container Instances, 584

Defender for Cloud, 153, 213, 567

deletion locks, 248

Entra ID, 563

Functions, 579

Network Security Groups, 253, 576

NSG Flow Logs, 116, 584

Privileged Identity Management, 565

Resource Manager, 583

service principals, 348

snapshots, 396

B

backups, 534

3-2-1-1-0 rule, 403

air-gapped, 535

immutable, 94, 403, 535

immutable infrastructure, 441

pull-based architectures, 535

ransomware-resistant strategies, 535

retention policy, 403

system failure, 440

Barnhart, Heather, 124, 280

BAS, 122

beaconing detection, 134, 468

verification, 513

BEC, 259, 309, 561

funds recovery, 315

lookalike domain, 314

victim by proxy, 314

behavioral detection, 143

behavioral IOC, 43

Bianco, David, 146

Blackbaud, 555

BlackSuit ransomware, 557

blame dynamics, 434

blameless postmortem, 421

Block Public Access, 577

Boyd, John, 190

BPF, 116

Brain Cipher, 291

Breach and Attack Simulation (see BAS)

breach coach, 90

breach notification, 22

breach notification requirements, 575

break glass accounts, 101, 534, 565

bring your own device, 205

business email compromise (see BEC)

BYOD (see bring your own device)

C

C2, 201, 230

C4 model, 79

C4 standard (see communications)

incident communications, 79

case management, 193, 622

CERT, 30

chain of custody, 74

Chainalysis, 522

Chronicle (see Google Security Operations)

CI/CD, 13, 250, 335, 572

CircleCI incident, 572

CIS Benchmarks, 111, 357

CISA KEV, 350

Cisco Foundation-sec-8b, 520

Claude Code, 504

skills files, 514

cloud audit logs

AWS, 209

Azure, 209

GCP, 209

cloud containment

API-based, 253

AWS Security Groups, 253

GCP firewall rules, 253

identity-first, 245

network isolation, 246

Network Security Group, 253

resource tagging, 246

SaaS, 249

security groups, 246

serverless, 253

termination protection, 248

cloud control plane, 323

cloud detection

GuardDuty, 153, 263

Kubernetes, 153, 263

Microsoft Defender for Cloud, 153, 213

Security Command Center, 153

cloud environments, 560

cloud investigation, 323

CloudTrail, 18, 209, 263

VPC flow logs, 116, 243, 302

cloud misconfigurations, 561

cloud persistence, 334

EC2, 14

cloud security, 22

IAM, 244

shared responsibility model, 243

cloud security demarcation, 244

Cloud Security Posture Management (see CSPM)

cloud snapshots, 396

cloud-native detection services, 565

cloud-native forensics, 587

CloudFormation, 324

CloudTrail, 18, 209, 263, 323

CMDB, 120

code analysis

deobfuscation, 456

code obfuscation, 8

Colonial Pipeline, 418

command and control (see C2)

command injection, 499

Common Vulnerabilities and Exposures (see CVE)

communications

C4 standard, 79

communications plan

incident, 79

compliance

continuous improvement, 615

demonstrated effectiveness, 615

documented capabilities, 615

metrics, 615

compliance artifacts, 619

compromised identities, 569

computed IOC, 43

Computer Incident Handling Step-by-Step Guide, 31

conditional access policies, 237

configuration hardening, 357

Configuration Management Database (see CMDB)

ConnectWise ScreenConnect, 362

container image modifications, 335

container monitoring

eBPF, 152

container registry poisoning, 579

Container Threat Detection, 568

containment, 20, 190, 220

account restrictions, 221

action removal, 391

active, 224

adaptive, 226

assessment, 17

coordinated, 228

credential reset, 229

deceptive, 190, 226

DNS sinkholing, 230

EDR isolation, 232

honeypots, 224

network isolation, 221

network segmentation, 224

objectives, 221

passive, 224

process termination, 221

progressive restrictions, 226

service disruption, 224

simultaneous isolation, 228

stopping attacker activity, 221

third-party integrations, 250

containment validation, 261

Conti ransomware group, 157

continuous improvement, 615

Continuous Integration, Continuous Deployment

(see CI/CD)

control effectiveness, 615, 620

control plane, 323

control plane logs, 563

coordinated recovery, 394

CoT (see chain of thought)

CRA, 86, 226

credential theft

Mimikatz, 368, 507

credentials

phased reset, 337

reset, 229

revocation, 234

stuffing, 7

theft, 21, 37

crisis communications, 530

cross-platform correlation, 498

cross-training, 130

CrowdStrike Falcon, 266

Crowley

Chris, 47

CSF (see NIST CSF 2.0)

CSF 2.0

community profile, 54

control effectiveness, 620

Detect function, 614

documented capabilities, 615

Govern function, 614

Identify function, 614

Protect function, 614

Recover function, 614

Respond function, 614

six functions, 613

CSPM, 100, 586

CTI, 40, 71, 104, 133, 134, 171, 524

platforms, 106

cURL, 8

cURL data exfiltration, 8

custom detection rules, 388

CVE, 350

CVE-2024-55591, 43

cyber insurance, 90

Cyber Resilience Act (see CRA)

Cyber Threat Intelligence (see CTI)

cyber threat intelligence (see CTI)

Cybersecurity Framework (see NIST CSF 2.0)

D

DAIR, 62, 70, 166, 200, 522, 560, 613

actions, 63

contain, 189

Decision Makers, 618

eradicate, 189

OT benefits, 599

outcomes, 63

recover, 189

Response Actions Loop, 68, 189, 191, 617

scope, 189

scoping, 66

structure, 616

verify and triage, 66

waypoints, 63

Data Breach Investigations Report (see DBIR)

data exfiltration, 21, 226

data exposure, 499

Data Loss Prevention (see DLP)

data plane logs, 563, 574

data sanitization, 452

risks, 452

data theft, 561

DCS, 590

deanonymization attacks, 452

debrief, 410

debrief challenges

blame dynamics, 434

incomplete documentation, 432

legal constraints, 434

organizational attention, 433

resource constraints, 435

deceptive containment, 226

Decision Maker coordination, 618

DeepSeek, 451

detection, 142

active, 146

behavioral, 143

machine learning, 144

purple teaming, 158

signature-based, 143

detection and analysis, 58

detection engineering, 118

detection improvements, 130

detection metrics

MTTD, 146

detection rules

Sigma, 43

detection tools

EDR, 147

NDR, 117, 148, 302

OpenObserve, 149

SIEM, 148

detection-driven data collection, 154

digital forensics, 93

Digital Operational Resilience Act (see DORA)

Distributed Control System (see DCS)

Distributed Network Protocol 3 (see DNP3)

DLP, 100

DNP3, 591

DNS over HTTPS (see DoH)

DNS sinkhole, 230

documentation

AI logs, 513

compliance, 619

decision, 193

incident reports, 422, 477

incident summary report, 424

incomplete, 432

technical incident response report, 424

two-report approach, 424

DoH, 231

domain controller machine account reset, 341

domain controller recovery, 400

domain registration timing, 314

DORA, 75, 86, 226

Dynamic Approach to Incident Response (see DAIR)

E

eBPF, 116, 152

EC2, 14, 245, 566

automated isolation, 581

EDR, 44, 100, 112, 147, 203, 224, 384

Elastic Compute Cloud (see EC2)

Elastic Security, 148

emergency access accounts (see break glass

accounts)

emergency communication plan, 84

encryptionless extortion, 526

Endpoint Detection and Response (see EDR)

endpoint telemetry, 293

enhanced monitoring, 386

enterprise-wide hunting

EDR, 203

SIEM, 202

Entra Connect (see Entra ID, Entra Connect)

Entra ID, 214, 215, 234, 240, 342, 364, 563

account indicators, 215

cloud identity, 214

consent grants, 251, 311

Entra Connect, 344, 364

hybrid environments, 234, 342, 364

Privileged Identity Management, 565

service principals, 214

session revocation, 240, 579

sign-in logs, 563

token revocation, 342

EOI, 39, 63, 146, 171

ephemeral cloud resources, 323

EPP, 100

EPSS, 124

eradication, 20, 191, 276

attacker access, 328

live investigation, 292

long-form investigation, 278

malware scan, 17

root cause analysis, 277, 410

short-form investigation, 278

system rebuild, 349

system restoration, 277

targeted removal, 349

eradication challenges, 360

eradication verification uncertainty, 398

EtherNet/IP, 591

Event Threat Detection, 567

events of interest (see EOI)

evidence collection

forensic imaging, 222

log preservation, 222

memory acquisition, 221

exercise performance, 130
