# Chapter 20: Integrating DAIR with NIST CSF 2.0 Framework

> Modular Sub-Chapter | Source: DAIR-IR Framework

---

UNDERSTANDING NIST SP 800-61 R3 AND CSF 2.0

The release of NIST SP 800-61 Revision 3 represents a fundamental shift in how NIST positions incident response within organizational cybersecurity programs. Where Revision 2 provided specific incident handling procedures and a four-phase lifecycle model, Revision 3 reframes incident response as an integrated component of enterprise cybersecurity risk management. This shift reflects an important evolution in cybersecurity thinking: effective incident response cannot exist as an isolated function. Response capabilities are influenced by and influence governance decisions, asset identification, protective controls, detection mechanisms, and recovery planning.  The CSF 2.0 framework captures these interdependencies through six core functions that provide a common language for describing and organizing cybersecurity activities. In this section, we’ll walk through each of the six CSF functions and how they relate to incident response

The Six CSF Functions

The CSF 2.0 framework organizes cybersecurity activities into six functions, each relevant to incident response capabilities: Govern (GV) The Govern function establishes the organizational context for cybersecurity activities. This includes cybersecurity risk management strategy, expectations, and policy that are communicated and monitored across the organization. For incident response, the Govern function addresses how organizations define incident severity thresholds, establish escalation procedures, allocate response resources, and integrate incident handling with enterprise risk management. Organizations demonstrate compliance by documenting how incident response decisions align with broader organizational risk tolerance and strategic objectives. Identify (ID) The Identify function ensures organizations understand their current cybersecurity risks. This involves maintaining awareness of assets, vulnerabilities, threats, and potential business impacts. Effective incident response depends on this understanding: responders need to know which systems are critical, what data requires protection, and how different systems interconnect. The Identify function also encompasses threat intelligence activities that inform detection strategies and response priorities. Protect (PR) The Protect function encompasses safeguards that manage cybersecurity risks before incidents occur. While primarily preventive, protective controls directly impact incident response by influencing the attack surface, available evidence sources, and recovery options. Incident response teams benefit from protective controls such as network segmentation, access management, and data protection mechanisms that limit incident scope and preserve forensic artifacts. Detect (DE) The Detect function covers capabilities for finding and analyzing cybersecurity attacks and compromises. This function aligns most directly with the early stages of incident response, encompassing the monitoring, alerting, and initial analysis activities that transform security events into actionable incident reports. Detection capabilities determine how quickly organizations identify incidents and how much context responders have when beginning their investigation. Respond (RS) The Respond function addresses actions taken in response to detected cybersecurity incidents. This is where the bulk of tactical incident response activity occurs, including analysis, containment, eradication, and communication activities. The Respond function explicitly recognizes the need for iterative response activities that adapt based on new information discovered during the incident. Recover (RC) The Recover function focuses on restoring assets and operations affected by cybersecurity incidents. Recovery activities include restoring system availability, rebuilding trust with stakeholders, and implementing improvements that prevent recurrence. The Recover function also encompasses postincident activities that capture lessons learned and improve organizational resilience. These six functions provide the structure within which organizations demonstrate incident response capability maturity and compliance.

What Compliance Requires

Organizations subject to CSF 2.0 requirements face several compliance obligations related to incident response, summarized in Table 60.

Table 60 | CSF 2.0 Incident Response Compliance Requirements

REQUIREMENT DESCRIPTION

Documented

Capabilities

Organizations should document incident response capabilities across all relevant CSF functions, describing detection methods, response procedures, decision authority, and external coordination. Documentation provides the foundation for demonstrating that capabilities exist and are maintained.

Demonstrated

Effectiveness

Organizations should demonstrate that incident response capabilities function as intended through exercises, tabletop scenarios, or actual incident response activities. Auditors look for evidence that documented procedures are followed in practice and produce intended outcomes. Metrics and

Measurement

Organizations should establish baselines for incident response metrics including detection time, response time, containment effectiveness, and recovery duration. Tracking trends over time demonstrates continuous improvement.

Continuous

Improvement

Organizations should learn from incidents and improve capabilities over time through post-incident reviews, procedure updates based on lessons learned, and root cause remediation. Compliance assessments examine mechanisms for capturing and acting on incident-related learning. The challenge for many organizations lies in bridging the gap between these compliance requirements and practical incident response operations. CSF 2.0 provides the strategic framework, but organizations need tactical methodologies to implement these requirements effectively.

DAIR AS CSF 2.0 IMPLEMENTATION

The DAIR model provides the tactical methodology organizations need to meet CSF 2.0 requirements. DAIR’s activities map directly to CSF functions, creating a practical implementation path that satisfies compliance requirements while improving the efficacy of incident response operations. This alignment is not coincidental: the DAIR model was developed to reflect incident response best practices, and CSF 2.0 demonstrate compliance without changing how effective incident response teams work. Next, we’ll map each DAIR activity to the CSF function it satisfies, examine how iterative response generates stronger compliance evidence than linear models, and show how Decision Maker coordination throughout the response satisfies the Govern function.

Mapping DAIR Activities to CSF Functions

The relationship between the DAIR model and CSF 2.0 becomes clear when examining how specific DAIR activities address each CSF function. Figure 200 provides an overview of how the six core CSF functions align with the DAIR model structure. Table 61 provides additional context and detail supporting this alignment, showing the DAIR activities that correspond to each CSF function and explaining how those activities satisfy compliance requirements. Organizations can use this mapping as a reference when documenting their incident response capabilities for compliance assessments.

Figure 200 | DAIR Model Mapped to NIST CSF 2.0 Functions

Table 61 | DAIR Activities Mapped to CSF 2.0 Functions

CSF FUNCTION DAIR ACTIVITIES HOW DAIR SATISFIES REQUIREMENTS

Govern (GV) / Identify (ID)

Decision

Maker coordination throughout all activities Decision Maker coordination aligns response with organizational risk tolerance and provides context about critical assets, acceptable impacts, and strategic considerations, satisfying the Identify function’s organizational context requirements. Govern function coverage is mapped at the CSF category level in Table 62. Protect (PR) Prepare activities The DAIR model Prepare waypoint encompasses proactive controls and readiness activities that align with the Protect function. Preparation includes establishing response procedures, deploying detection capabilities, configuring systems for forensic readiness, and training response personnel. These activities create protective capabilities that limit the impact of incidents and inform effective response actions. Detect (DE) Detect, Verify, and Triage activities The DAIR model explicitly addresses incident detection and adds verification and triage activities that ensure detection capabilities function effectively. The Verify activity confirms that detected events represent actual incidents requiring response, while the Triage activity prioritizes incidents based on organizational impact. Together, these activities satisfy Detect function requirements for finding and analyzing potential compromises.

Respond (RS) Response

Actions Loop

(Scope, Contain, Eradicate,

Recover)

The Response Actions Loop represents DAIR’s core contribution to the Respond function. By structuring response as an iterative cycle rather than a linear sequence, the DAIR model ensures thorough incident handling that adapts to new discoveries. Each iteration through Scope, Contain, Eradicate, and Recover activities generates evidence of comprehensive response effort. Recover (RC) Recover activities and

Debrief

The DAIR model’s Recover activities restore affected systems to operational status, while the Debrief activity captures lessons learned and identifies improvement opportunities. Together, these activities satisfy Recover function requirements for restoration and continuous improvement. This mapping demonstrates that organizations using the DAIR model for incident response are already performing activities that satisfy CSF 2.0 requirements. Organizations adopting the DAIR model need only document these activities in a way that makes compliance visible to assessors and auditors.

The Value of Iterative Response for Compliance

DAIR’s iterative Response Actions Loop provides particular value for CSF 2.0 compliance. Traditional linear comprehensive remediation effort. Organizations can present iteration counts as positive metrics rather than evidence of failure. When documenting iterations, record what new information triggered each cycle and what additional remediation occurred as a result. This documentation transforms iteration from an apparent weakness into evidence of thorough, adaptive, and considered incident response actions. This reframing has practical compliance implications. When auditors review incident response records, they may question why incidents required extended response periods or multiple remediation attempts. Under the DAIR model, organizations can explain that the iterative response is by design: each cycle incorporates new information, appropriately expands scope, and improves overall response effectiveness. This explanation, supported by documentation from each iteration, demonstrates a mature incident response capability rather than a process deficiency.

Decision Maker Integration and the Govern Function

DAIR’s emphasis on Decision Maker coordination aligns with the CSF 2.0 Govern function across the response lifecycle. The Govern function requires organizations to establish and communicate a cybersecurity risk management strategy across the enterprise, with assessors expecting evidence that incident response decisions reflect that strategy in practice rather than as stated intent. In the DAIR model, Decision Makers are not involved just at the beginning or end of incidents. They provide ongoing guidance throughout the response lifecycle, informing decisions about scope expansion, containment approaches, acceptable operational impacts, and recovery priorities. This continuous coordination produces records that map directly to CSF 2.0 Govern categories, as shown in Table 62.

Table 62 | DAIR Activities Mapped to CSF 2.0 Govern (GV) Categories

GV

CATEGORY ASSESSOR EXPECTATIONS DAIR ACTIVITIES ARTIFACTS GENERATED GV.OC:

Organizational Context Documentation showing that incident response decisions reflect the organization’s regulatory obligations, stakeholder expectations, risk appetite, and business environment. Prepare: regulatory notification mapping, stakeholder identification, risk classification criteria definition. Verify and Triage: per-incident risk classification decisions documented against preagreed thresholds. Risk classification framework, triage decision records showing classification rationale, regulatory notification trigger log.

GV.RM:

Risk

Management Strategy Evidence that residual risk at incident closure is formally assessed, accepted by an authorized individual, and fed back into the enterprise risk register. Response Actions Loop: loop exit risk acceptance decision. Debrief: lessons learned mapped to risk register entries. Recover: recovery metrics feeding program-level trend analysis. Signed loop exit risk acceptance record, debrief report with risk register update recommendations, metrics trend data submitted to enterprise risk function. GV

CATEGORY ASSESSOR EXPECTATIONS DAIR ACTIVITIES ARTIFACTS GENERATED GV.RR:

Roles, Responsibilities, and

Authorities

A defined authority matrix for incident response covering declaration, command, business-impact decisions, loop exit, and post-incident improvement ownership, using named roles rather than generic titles. Prepare: incident response team structure, RACI matrix, escalation thresholds, and decision authority documented prior to incidents (see

Document Incident

Response Decision

Authority). Incident response authority matrix, escalation procedure documentation, named role assignments per incident type or severity tier.

GV.PO:

Policy

Documented cybersecurity policies that reflect organizational context, including an incident response policy that distinguishes policy (what should happen), procedure (how it happens), and playbooks (how it happens for specific scenario types). Prepare: incident response plan, playbooks, communication plan, contact lists, callout rosters. Documentation should use policy, procedure, and playbook taxonomy consistently to facilitate assessor review. Incident response policy document, procedure documents per DAIR phase, scenario-specific playbooks, communication plan with last-reviewed timestamp.

GV.SC:

Supply

Chain Risk

Management Evidence that third-party and supplier incident response obligations are defined, that contractual notification requirements are mapped, and that supplier access revocation is addressed in incident response procedures. Prepare: supplier incident response obligation mapping, data processing agreement review schedule, third-party access inventory. Scope and Contain: third-party access revocation procedures. Debrief: supplier-related root cause and remediation tracking. Supplier incident response obligations register, data processing agreement and contract review records, third-party access revocation log, postincident supplier remediation tracking. Organizations can demonstrate Govern function compliance by producing the artifacts in the Artifacts Generated column and linking them to the incident records that generated them. This CSF category-level documentation shows that incident response operates within the organization’s broader risk management framework rather than as an isolated technical function.

MEETING COMPLIANCE THROUGH DAIR ACTIVITIES

Effective incident response generates substantial documentation as a natural byproduct of response activities. Organizations using the DAIR model can structure this documentation to satisfy compliance requirements without creating separate administrative processes. The key lies in recognizing the compliance artifacts already present in DAIR operations and formatting them appropriately for assessment. In this section, we’ll identify the compliance artifacts that DAIR activities generate naturally, work through

Compliance Artifacts from DAIR Activities

Compliance assessments require organizations to produce tangible evidence that incident response capabilities exist, function as intended, and improve over time. Assessors and auditors expect specific artifacts that demonstrate coverage across CSF functions, and organizations that cannot supply this evidence risk compliance gaps regardless of how effective their actual response operations are. When applying the DAIR model, each waypoint generates documentation that serves these compliance purposes as a natural byproduct of response activities. Table 63 summarizes the artifacts generated by each DAIR phase and the CSF functions they address.

Table 63 | Compliance Artifacts by DAIR Phase

DAIR PHASE ARTIFACTS GENERATED CSF FUNCTION

Prepare Incident response plans, playbooks, contact lists, training records, CSF function cross-references in response procedures Protect (PR) Detect / Verify /

Triage

Alert logs, monitoring dashboards, threat intelligence reports, triage decisions, false positive records, incident declaration documentation Detect (DE)

Response Actions

Loop (Scope, Contain,

Eradicate, Recover)

Scoping analysis, containment decisions, eradication records, and recovery verification, accumulating across iterations into a comprehensive response record Respond (RS) Debrief Lessons learned reports, root cause analysis, improvement recommendations, implementation tracking records Recover (RC) Decision Maker coordination (throughout) Stakeholder consultation records, guidance documentation, business impact assessments, risk-aligned decision rationale Govern (GV) / Identify (ID) These artifacts accumulate naturally through DAIR operations, with each iteration through the Response Actions Loop adding to the evidence base. Tracking the implementation of improvement recommendations from debriefs provides additional evidence of program maturation. Organizations should ensure that documentation captures the rationale for decisionmaking in addition to the actions taken, to satisfy CSF compliance artifact requirements. Organizations that maintain thorough documentation throughout DAIR activities will find that most compliance artifacts already exist. The remaining task is to organize and present this documentation in formats that assessors expect.

Demonstrating Control Effectiveness

CSF 2.0 compliance requires organizations to demonstrate that controls function as intended, not merely that they exist. The DAIR model provides multiple opportunities to demonstrate control effectiveness through actual incident handling. Table 64 maps each CSF function to the types of evidence organizations can produce and the DAIR activities that generate them.

Table 64 | Control Effectiveness Evidence by CSF Function

CSF FUNCTION EVIDENCE OF EFFECTIVENESS DAIR SOURCE ACTIVITIES

Detect (DE) Incidents identified through monitoring and alerting rather than external notification or chance discovery. Metrics such as Mean Time to Detect (MTTD) provide quantitative evidence of detection capability.

Detect, Verify, Triage

Respond (RS) Containment limited incident scope, eradication removed attacker presence, and iterative response addressed additional incident elements that a linear approach might have missed. Response Actions Loop (Scope,

Contain, Eradicate, Recover)

Recover (RC) Successful system restoration, validation of restored system integrity, and implementation of improvements that prevent recurrence.

Recover, Debrief

Each iteration through the Response Actions Loop strengthens the evidence of response effectiveness by demonstrating that the organization adapted to new findings and addressed them systematically.

Satisfying Audit Requirements

Audit and assessment activities typically examine incident response capabilities through document review, interviews, and evidence examination. Organizations using the DAIR model can prepare for these assessments by maintaining organized documentation and training response personnel to explain DAIR concepts in CSF 2.0 terms. Start by organizing incident documentation to align with CSF functions. Auditors often structure their assessments around CSF categories and subcategories, so documentation organized in the same way reduces assessment friction. Cross-reference DAIR activities to CSF functions in response plans and procedures to make the mapping explicit, as in the example shown in DAIR Activities Mapped to CSF 2.0 Functions . Response personnel should understand how DAIR activities relate to CSF 2.0 requirements. When auditors ask about detection capabilities, personnel can explain DAIR’s Detect and Verify/Triage activities and describe the Response preparing for assessments after incidents. Compliance becomes a natural outcome of effective incident response rather than a separate administrative burden.

INCIDENT TRACKING PLATFORM CONFIGURATION

Organizations can configure their incident response tracking tooling to support both effective operations and compliance requirements. Careful incident tool configuration reduces manual effort and ensures that compliance artifacts are generated consistently. In this section, we’ll cover the ticketing and case management configurations that capture both operational coordination and compliance evidence, and the communication templates that document incident progress in CSF terminology.

Ticketing and Case Management

Incident tracking systems serve as the primary documentation platform for most organizations, whether a system like JIRA or Remedy, or a specialty incident response tracking system. Organizations that need to comply with CSF functions while adopting the DAIR model can configure these systems to capture information for both operational coordination and compliance demonstration. To best capture CSF function activities, configure incident status fields to reflect CSF vocabulary supported by DAIR activities. Status options might include Detection Complete, Verification Pending, Containment Active, Eradication in Progress, and Recovery Underway. These statuses map directly to CSF functions and generate records that demonstrate function coverage. Workflows can support DAIR’s iterative approach, allowing incidents to cycle through Response Actions Loop phases multiple times without treating iteration as undesirable backtracking. Where possible, include fields to document Decision Maker involvement, identify which stakeholders were consulted, record the guidance they provided, and note how their input influenced response activities. This documentation satisfies the CSF Govern function’s requirements for risk-aligned decision-making. Configure the system to link evidence artifacts to specific incident records so compliance reviewers can locate relevant evidence and ensure it is preserved in accordance with incident retention policies.

Communication Templates

Most communication templates should be developed during preparation as part of the Emergency Communication Plan (see Develop an Emergency Communication Plan ), including a template set for each major incident-type category to support consistent messaging during the first twenty-four hours. The integration with CSF 2.0 lies in how those prepared templates are tagged and adapted for compliance reporting during the response. When communicating about incident status, tag updates with the CSF function and DAIR activity that produced them. For example, an update describing initial scoping work would identify CSF Respond function activity in the DAIR Scope phase, while recovery validation would identify CSF Recover function activity. This consistent vocabulary demonstrates organizational fluency with the compliance framework and produces records that map directly to CSF function coverage during assessor review. Create template variants for different audiences. Executive communications should summarize impact and progress, while technical communications should include detailed activity descriptions in DAIR waypoint terminology. Both variants should support compliance by documenting appropriate information for their respective audiences. Tool configuration investments that optimize processes and guide analyst documentation are valuable in the long term. Setting expectations for note-taking reduces manual effort and improves documentation consistency. Organizations should review their tooling periodically to ensure configurations continue to support both operational and compliance needs.

INTEGRATING DAIR WITH NIST CSF 2.0

The integration of the DAIR model with NIST CSF 2.0 demonstrates that compliance and operational effectiveness reinforce rather than conflict with each other. The DAIR model provides the tactical methodology that organizations need to implement CSF 2.0’s strategic vision for incident response, with activities that map directly to all six CSF functions. The Response Actions Loop operationalizes CSF 2.0’s
