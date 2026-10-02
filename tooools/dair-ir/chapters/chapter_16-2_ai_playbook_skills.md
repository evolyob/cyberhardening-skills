﻿﻿# 第 16-2 章：AI 輔助應變－Playbook as Skill 架構與提示工程

> 模組化子章節 | 隸屬來源:  (行 1361 ~ 2719)

---

manual analysis.

An analyst reviewing proxy logs for suspected C2 beaconing can upload the log file and request analysis

using a prompt, such as the one shown in Figure 150.

Figure 150 | Beaconing Detection Prompt

In this example, Claude Opus analyzed the proxy log structure and identified the need for statistical analysis

to detect beaconing behavior based on the regularity of request intervals.  Rather than providing a simple

pattern match, the model recognized that effective beaconing detection would require calculating the

coefficient of variation for request intervals to distinguish machine-generated traffic from human browsing.

It then generated a Python script to perform this analysis, as shown in Figure 151.

Figure 151 | Beaconing Analysis Python Script

Figure 152 | Beaconing Analysis Results

The analysis revealed multiple compromised hosts communicating with suspected C2 infrastructure,

including a typosquat domain masquerading as Google Analytics services. The model integrated online

cyber threat intelligence during its analysis, identifying that www1-google-analytics.com used a common

typosquatting technique with the www1- prefix to deceive users and security tools. Key findings from the

analysis are summarized in Table 47.

Table 47 | Beaconing Detection Findings Summary

DOMAIN SUSPICIOUS INDICATORS BEACON INTERVAL AFFECT

ED

HOSTS

CONFIDENCE

www1-google-

analytics.com

Typosquat domain, HTTP

protocol (not HTTPS),

extremely regular intervals

(CV=0.02), high volume

(9,075 requests)

~5 seconds 4 hosts Very High

email.falsimentis

.com

Unknown domain, HTTP

protocol, near-perfect 60-

second intervals (CV=0.004),

POST method with query

string

~60 seconds 4 hosts High

This example demonstrates how AI models can not only identify suspicious patterns but also determine the

appropriate analytical approach, implement the analysis methodology, and integrate external threat

intelligence to provide comprehensive findings that would traditionally require manual statistical analysis

and open-source intelligence gathering.

Limitations and Considerations

AI log analysis can accelerate incident response, but it also has several inherent limitations that analysts

should understand when evaluating findings.

Incomplete Detection

Models may miss subtle indicators that experienced analysts would recognize. Complex attack patterns,

novel techniques, or carefully crafted evasion methods might escape detection when relying solely on AI

analysis. AI serves as a valuable first-pass triage tool, not a comprehensive security control.

False Positive Risk

Models can generate false-positive alerts that mislead the analysis team and waste valuable time during

response efforts. Legitimate but unusual patterns may be flagged as suspicious, requiring analysts to verify

each finding before taking action.

Lack of Definitive Conclusions

AI log analysis may struggle to provide definitive conclusions about attacker activity. Models that lack the

contextual understanding for authoritative attribution often hedge assertions with may be  or looks like ,

leaving it up to the analyst to make an impact assessment. Thorough manual review remains essential for

critical investigations.

Context Window Constraints

AI models operate within fixed context window limits that constrain how much log data can be analyzed in a

single interaction. Frontier models like Claude Opus 4.5 support context windows of 200,000 tokens,

roughly equivalent to 150,000 words or 500 pages of text. While substantial, this limit poses challenges

when analyzing enterprise log collections that routinely contain millions of entries.

Direct analysis approaches work well for focused investigations involving small to medium log sets. An

analyst can attach several thousand lines of authentication logs, proxy records, or application events to a

chat interface and receive useful pattern analysis within the model’s context window. This approach suits

initial triage, spot checks, or targeted investigations where relevant log segments have already been

identified.

However, comprehensive log analysis during major incidents often requires processing volumes that exceed

context window capacity. Analyzing a week of authentication logs from an enterprise directory service,

reviewing firewall logs across multiple network boundaries, or correlating application logs from distributed

systems generates data volumes that cannot fit in a single model interaction.

For large-scale log analysis, agentic approaches offer solutions that overcome limitations of context

windows. Agent-based systems can process log data iteratively, analyzing segments within context window

constraints and maintaining state across multiple interactions. We’ll explore these use cases in Section

Translating Technical Findings for Stakeholders

Incident response teams need to communicate with diverse audiences: executive leadership needs

business-impact summaries, legal teams need specific technical details for regulatory filings, and

stakeholders need clear guidance on service disruptions. Producing the messaging that meets each

audience’s needs can be challenging. Analysts skilled at digital forensics, threat hunting, and vulnerability

assessment are not always equally proficient at technical writing and audience-appropriate communication.

This is another opportunity for analysts to utilize AI models, accelerating the writing of documents,

reports, summaries, and status reports for different stakeholders.

Executive Summary Generation

Given a technical timeline of attacker activity, an analyst can use a model to transform the details into

executive-appropriate language. For example, consider the prompt shown in Listing 126, which outlines a

timeline of attacker activity following a workstation breach, including lateral movement and data exfiltration

prior to detection.

Listing 126 | Executive Summary Generation Prompt

Transform the following technical incident timeline into an executive summary suitable for

senior leadership. Focus on business impact, risk exposure, and response actions. Avoid

technical jargon. The summary should be no more than five bullet points.

Technical Timeline:

- 2026-01-07 14:32 Initial access via phishing email to user jwalcott@falsimentis.com on FM-CEO

- 2026-01-07 14:45 Malware execution, C2 beacon established to 203.0.113.47

- 2026-01-07 15:12 PowerShell script execution for credential harvesting from Chrome local

storage

- 2026-01-07 15:34 Lateral movement to file server FM-FS01 using harvested credentials

- 2026-01-07 16:02 Data staging, 2.3GB archived to C:\Users\Public\backup.zip

- 2026-01-07 16:18 Data exfiltration to Box.com cloud storage

- 2026-01-07 16:45 Possible infostealer binary executed on FM-FS01

- 2026-01-07 16:45 FM-FS01 EDR alert triggered, investigation initiated

Using ChatGPT, the model produces the executive summary shown here:

“• Confirmed security incident with unauthorized access began when an employee was tricked into

opening a malicious email, allowing an external actor to gain access to a company device and then

expand into a critical internal file server.

• Business risk includes potential data exposure: approximately 2.3GB of company data was collected

and appears to have been transferred outside the organization to a third-party cloud storage service,

creating potential confidentiality, regulatory, and contractual impact.

• The attacker attempted to capture account credentials (saved login information) and used them to

move deeper into the environment, increasing the risk of continued access to additional systems

beyond what has been identified so far.

• Security monitoring detected the activity and triggered an alert, prompting the organization to begin

incident response actions, including investigation and containment efforts focused on preventing

further access and limiting additional data loss.

• Immediate response priorities are to confirm exactly what data was accessed, secure affected

accounts and systems, assess legal/notification obligations if sensitive data is involved, and

implement additional controls to reduce the likelihood of recurrence (e.g., stronger email protections

and access safeguards).

This transformation preserves essential information for the intended audience, allowing the analyst to focus

on investigation efforts while still communicating pertinent information. This technique is also easily

adaptable to other audiences, including legal teams, key stakeholders, and GRC teams.

The analyst should always verify the accuracy of the model-generated output and adjust

the tone to match organizational communication standards before distribution.

INTERMEDIATE USE CASES

Now that we’ve looked at some introductory use cases, let’s explore more sophisticated AI applications to

accelerate incident response. The following use cases employ more complex, structured prompts to

generate more sophisticated output: playbooks that guide investigation procedures, report drafts that

document incident findings, and exercise scenarios that test organizational readiness.

Generating Incident Response Playbooks

Playbooks provide step-by-step guidance for responding to specific incident types. Effective playbooks

integrate a response process (such as the DAIR model or NIST SP 800-61) with techniques specific to the

Event of Interest (EOI) being investigated.

Playbooks are valuable for analysts, especially during active incidents, providing guidance on what to do

next when investigating an EOI or IOC. They are also valuable for the organization, ensuring consistent

response practices across different analysts and teams. Playbooks should be customized for the

organization’s environment, tools, and policies.

tactics. AI models can accelerate playbook development by generating initial drafts that analysts then refine

and customize.

Structured Prompt for Playbook Generation

Supporting the response process described in the DAIR model, I wrote a structured prompt to guide the

model in generating incident response playbooks. [2]

This prompt is lengthy but provides clear instructions,

output format definitions, reasoning steps, and context to help the model produce high-quality playbooks

based on the described EOI, available at [課程範例連結]

Figure 153 | IR Playbook Generation Structured Prompt

I developed and tested the IR playbook prompt for the DAIR model primarily using ChatGPT

models, though it will also work with other platforms that support structured prompting.

The prompt uses structured Markdown formatting and XML-style tags to delineate instructions, context,

and output requirements. An excerpt of the structure in the prompt is shown in Listing 127.

Listing 127 | DAIR Model Incident Response Playbook Generation Prompt

$ wget -q [課程範例連結] -O playbookprompt.txt

$ grep -E "^#" playbookprompt.txt

# Role and Objective/Task 1

# Instructions

# Reasoning Steps

# Output Format

## Overview

## Description

### Detect Steps

### Verify Steps

### Triage Steps

### Scope Steps

### Contain Steps

### Eradicate Steps

### Recover Steps

### Debrief Steps

## Version Control

# Example Playbook

# Summary

1 Some output has been removed for brevity.

Pasting the prompt into the model chat interface prompts the model to ask for the specific EOI to be

investigated, along with organizational context such as tools in use, policies, and environmental details.

Supplying an EOI, such as a need to respond to a possible Windows infostealer malware with data exfiltration

via cloud storage, will direct the model to produce a playbook draft, as shown in the example in Figure 154.

Figure 154 | Playbook Generation Model Response

instructions and output format requirements. Explicitly specifying the use of the ChatGPT

thinking model is not required, but it helps ensure the model applies reasoning steps

effectively during generation.

The model will generate a complete playbook that integrates the DAIR response process with techniques

specific to the described EOI in Markdown format. Analysts can use the Markdown format directly, or

convert it to HTML, Microsoft Word, or other formats as needed. An excerpt from the generated playbook is

shown in Listing 128 (a full example is available at [課程範例連結]).

Listing 128 | Playbook Generation Output Excerpt

# IR Playbook - Windows Infostealer With Cloud Storage Exfiltration

## Overview

The purpose of this playbook is to guide incident responders through detection, verification,

triage, scoping, containment, eradication, and recovery for a suspected Windows infostealer

infection where stolen data is being staged and exfiltrated via a cloud storage service (e.g.,

OneDrive/SharePoint, Dropbox, Google Drive, Box).

## Description

This event involves one or more Windows endpoints exhibiting infostealer behavior (suspicious

process execution, unusual browser data access, new persistence artifacts, credential access

activity) along with indications of outbound data transfer to cloud storage. The EOI may

originate from EDR telemetry, proxy/DNS/firewall logs, abnormal user sign-ins, cloud audit logs

showing unusual file uploads, or user-reported symptoms (unexpected MFA prompts, account

lockouts, "new device" sign-ins). Typical infostealers are commodity malware-as-a-service

families with rapid delivery and frequent infrastructure churn, often used to bootstrap follow-

on access.  

## Dynamic Approach to Incident Response

Apply these steps to detect, verify and triage, scope, contain, eradicate, and recover from the

incident.

### Detect Steps

Apply the following steps to investigate the Event of Interest (EOI). Use the information

provided by the user to guide the investigation.

Start by capturing the "minimum viable facts" so your investigation doesn’t drift. You’re trying

to answer: **which hosts**, **which users/identities**, **which cloud storage provider**, **what

data**, and **when**.

**Inputs to gather immediately (answer what you can now):**

- Which telemetry exists: EDR (Defender/MDE/CrowdStrike), SIEM, web proxy, DNS logs, firewall

logs, M365/Entra audit logs, CASB?

- Cloud storage in scope: OneDrive/SharePoint, Dropbox, Google Drive, Box, others?

- Scope hints: single host/user or multiple? any VIPs? any regulated data?

Then perform endpoint-centric detection on the suspect host(s):

- Confirm basic host and logged-on user context:

```powershell

hostname

whoami

quser

ipconfig /all

Get-Date

```

The playbook continues with detailed steps for each DAIR process waypoint, tailored to the specific EOI.

Refining Generated Playbooks

AI-generated playbooks require review and refinement before operational use. Analysts can accelerate

generating playbooks but should ensure the output is accurate, complete, and customized to the

organization’s environment. Key refinement steps include:

• Verify that commands and queries are syntactically correct.

• Adjust tool references to match actual organizational tools.

• Add organization-specific contacts, escalation paths, and approval requirements.

• Remove or flag any steps that don’t apply to the environment.

• Test procedures where possible to confirm they work as described.

After refining a generated playbook, consider using the refined version as an example in subsequent

prompts. This one-shot prompting approach helps the model better match the desired output format and

level of detail.

Drafting Incident Reports

As we saw in Consolidating Incident Documentation , incident documentation is an important part of the

debrief process, preserving institutional knowledge, supporting compliance, and serving as reference

material for future incidents. AI can accelerate the transformation of investigation findings into structured

reports tailored for different audiences.

Report Draft Generation

AI models can assist in drafting incident reports by organizing investigation findings into structured

formats. By supplying incident findings along with a prompt that defines the desired report structure and

audience, analysts can quickly generate draft reports to review and refine.

For example, using the details provided for a sample incident stemming from a workstation compromise via

a vulnerable Adobe Reader exploit, we can prompt the model to draft an executive summary report, as

shown in Listing 129. [3]

Listing 129 | Executive Report Draft Prompt with Incident Findings

Using the incident findings below, create a draft incident summary report suitable for executive

leadership. Follow this structure:

1. Executive Overview (incident type, detection date, brief description, business impact)

2. Key Findings (what happened, what was affected, what data was at risk)

3. Response Actions Taken (containment, eradication, recovery status)

4. Recommendations (immediate actions, longer-term improvements)

5. Decisions Required (what leadership needs to approve or fund)

~~~~

# Incident Findings - SampleCorp Breach

## Affected Systems

- WKST01.samplecorp.com (development environment, source code and API credentials)

- HR01.samplecorp.com (HR system, employee PII including SSNs)

## Timeline

- 2026-01-15 00:27 - Employee opened malicious PDF (cv.pdf) exploiting Adobe Reader

vulnerability

- 2026-01-15 00:35 - Unauthorized access to development directories and API keys

- 2026-01-15 00:50 - Lateral movement via buffer overflow in HR application

- 2026-01-15 01:30 - Employee database compressed and exfiltrated via SSH tunnel

- 2026-01-15 02:30 - SOC detected activity, isolated systems via VLAN

- 2026-01-15 03:43 - Firewall rules updated blocking C2 IP 192.168.220.66

- 2026-01-15 04:11 - Malware removed from both systems

- 2026-01-15 05:21-05:58 - Both systems restored from verified backups

## Technical Details

- Initial vector: Malicious PDF exploiting CVE in Adobe Reader 10.0

[...] 1

1 Additional technical details omitted for brevity.

For this example, we used Claude Opus to generate the report. Without specifying the desired output

format, Claude Opus generated a Microsoft Word document that summarizes the technical details of the

incident findings in a structured report, as shown in Figure 155.

Figure 155 | Completed Executive Report Prompt Results

Figure 156 | Executive Report Draft Output Excerpt

I’ve covered this before in the chapter, but I think it bears repeating. Draft reports must be

thoroughly reviewed to ensure accuracy before distribution. AI may misinterpret findings

and draw incorrect conclusions, add plausible-sounding details not present in source data,

omit important findings that don’t fit expected patterns, or use inappropriate tone or

terminology for the audience. Treat AI-generated reports as starting points that accelerate

formatting and organization, not finished products ready for distribution.

Enhancing Report Quality with Specialized Knowledge

AI models can do a reasonable job of generating incident reports based on supplied findings. However,

generic models lack specialized knowledge of what makes incident response reports effective and don’t

have access to organizational preferences for report structure, tone, content, or other best-practice

guidance.

Without specialized guidance, models produce reports that are helpful but not distinctive. Reports need an

appropriate tone, clear executive summaries, prioritized remediation steps, and a structure that serves both

immediate response needs and long-term organizational learning. The difficulty is that appropriate, clear,

prioritized, and structured are not the same for every organization, and the model has no way of knowing

those preferences without explicit input.

Specialized Knowledge Integration with MCP

Providing AI models with access to specialized incident response reporting guidance and previously-

generated report samples can substantially improve the quality of AI-generated reports. Rather than relying

solely on the model’s training data about incident reports in general, the model can reference specific best

practices and quality criteria developed by experts in the field.

MCP provides a standardized method for connecting AI models to external tools and data sources that

supply specialized knowledge. MCP servers expose capabilities that AI models can query to retrieve relevant

guidance when needed. An analyst working on a report draft can request evaluation against IR-specific

quality criteria, and the model retrieves those criteria from an MCP server rather than requiring them to be

embedded in every prompt.

We’ll cover MCP in greater detail in Section 16.5.

MCP servers can provide specialized knowledge for incident response reporting. Quality criteria help

models evaluate draft reports against established standards for executive summaries, impact framing, tone,

and appropriateness of technical detail. Report structure guidance ensures that models generate reports

with sections and an organization appropriate to different incident types. Best-practice recommendations

help models suggest remediation steps, communication strategies, and post-incident actions informed by

incident response expertise.

Organizations can integrate these specialized knowledge sources through several approaches, each with

different implementation complexity and data handling characteristics. Publicly accessible MCP servers

provide general best practices that apply across organizations. Internal MCP servers can host organization-

specific guidance, templates, and quality standards. Hybrid approaches combine external best practices

with internal customizations to balance standardization with organizational needs.

For organizations unable to deploy MCP servers, specialized knowledge can be embedded

directly in prompts or maintained in local documentation that analysts can reference when

prompting models for report generation.

Zeltser IR Report Guidance

My friend and SANS faculty fellow Lenny Zeltser developed an MCP server that provides specialized

guidance for incident response report generation and evaluation. Lenny took his years of experience writing

incident reports and teaching effective report writing and codified best practices into a freely available MCP

server that AI models can query to improve report quality. [4]

The MCP server offers three primary capabilities that assist analysts throughout the report-writing process:

• Report creation assistance  provides guidance across executive summaries, technical timelines, root

cause analysis sections, and remediation recommendations. The guidance is adaptive based on incident

type (for example, recognizing that ransomware incident reports have a different emphasis than

business email compromise or insider threat documentation).

• The draft evaluation  assesses existing reports against quality criteria specific to incident response,

• Multi-report support addresses various security documentation needs beyond just incident response,

though optimization focuses on IR use cases.

Analysts can connect Claude, ChatGPT, or other compatible tools to the Zeltser report writing server using

standard MCP configuration, as shown in Listing 130 and in Figure 157.

Listing 130 | MCP Server Configuration Command

claude mcp add zeltser-search --transport http hxxps://website-mcp[.]zeltser[.]com/mcp

Figure 157 | MCP Server and Claude Code Configuration Example

Once configured, analysts working on incident response reports can request assistance with report

evaluation or generation, and the model will direct the AI client to query the MCP server for relevant

guidance. For example, after adding the MCP server as zeltser-search in Claude Code, I asked it to evaluate

a report draft using the following prompt:

“Review the IR report in @Incident\ Report.docx using zeltser-search.

Figure 158 | MCP Server and Claude Code, Report Advice Prompt

In this example, using the Hack The Box SampleCorp Breach report by Sebastian Hague, Claude Opus

evaluated the report contents, drawing on guidance from the Zeltser MCP server to identify

recommendations for improvement. Zeltser’s MCP server applied specialized knowledge about IR reporting

best practices to identify several areas for improvement, as shown in Listing 131.

Listing 131 | Zeltser MCP Server Report Evaluation Output

Areas for Improvement by Section

Executive Summary

* Issue: Too long (approximately 500+ words vs. recommended 150 words maximum)

The executive summary should be drastically shortened. Executives need the essential facts

quickly. Consider this structure:

On April 22, 2019 at 01:05 UTC, SampleCorp's SOC detected unauthorized

access after an employee opened a malicious PDF. The attacker compromised

two systems (WKST01 and HR01) containing proprietary code and employee data

including SSNs. [CLARIFY: Data was/was not exfiltrated]. SOC contained the

incident within 5 hours. Root causes: outdated Acrobat Reader, buffer overflow

in proprietary HR app, and inadequate network access controls. Immediate actions

complete; network segmentation and access controls being implemented. [If data

was exfiltrated: Regulatory notifications in progress per GDPR/state breach laws.]

Current stakeholder impact details should move to the dedicated Impact Analysis section, not

the executive summary.

Timeline Issues

* Missing timezone: The report uses times like "01:05:00" without specifying the timezone. Given

that SampleCorp may have offices or stakeholders in multiple locations, every timestamp should

include timezone (e.g., "01:05:00 UTC" or "01:05:00 EDT").

Example from timeline:

- Current: "April 22nd, 2019, 00:27:27"

- Better: "April 22nd, 2019, 00:27:27 UTC"

This is especially important for regulatory notifications with strict timeframes.

[\...]

Summary

This is a technically strong report with excellent forensic detail and clear response

documentation. The primary issues are:

1. Critical data exfiltration inconsistency that must be resolved

2. Executive summary too long for busy executives

3. Missing ownership and timelines in lessons learned

4. Regulatory obligations not addressed despite potential PII exposure

5. Lack of quantification in business impact areas

With this guidance, the analyst can make changes to the report or ask the model to review the report

accordingly. Zeltser’s MCP server enables analysts to utilize specialized incident response reporting

knowledge without having to embed that knowledge in every prompt, thereby substantially improving the quality of AI-generated reports.

Creating Tabletop Exercise Scenarios

In Section 7.2.2.8  we looked at the value of tabletop exercises for testing organizational readiness and

guiding teams through hypothetical incident scenarios. Crafting engaging, realistic scenarios is an

important part of effective exercises, but developing them can be time-consuming and challenging.

Developing an effective scenario requires balancing realism, complexity, and learning objectives. Realistic

scenarios require understanding current threats, organizational context, and insight into existing systems

for organizational-specific details. A single detractor who thinks the scenario is unrealistic can undermine

the entire exercise. It’s up to the tabletop facilitator to design scenarios that engage participants, bringing

realism, creativity, and energy to the exercise.

AI tools can help in designing tabletop scenarios, artifacts, and supporting elements, relieving some of the

burden on exercise facilitators. This section demonstrates three approaches to AI-assisted scenario

generation, progressing from simple idea generation to organizationally-grounded scenarios to interactive

and gamified exercise formats.

Generating Scenario Ideas

Facilitators beginning scenario development can use straightforward prompts to generate initial concepts

based on current threat landscapes. A basic prompt requests scenario ideas without requiring detailed

organizational context or technical artifacts.

For example, a facilitator might prompt the model with a request like the one shown in Listing 132.

Listing 132 | Basic Tabletop Exercise Scenario Prompt

Generate three tabletop exercise scenario concepts for an incident response team. Each scenario

should:

- Be based on current threat actor techniques and realistic attack patterns

- Target a mid-sized organization in the healthcare sector

- Progress through multiple phases allowing discussion at each stage

- Include decision points that test communication, escalation, and containment procedures

- Run approximately 90 minutes with a facilitator guiding discussion

For each scenario, provide:

- Initial compromise method

- Three progressive injects that complicate the response

- Key learning objectives

- Discussion questions for each phase

Using Google Gemini, the model produced several scenario concepts, including the example shown in

Listing 133.

Listing 133 | Google Gemini Tabletop Exercise Scenario Example

# Scenario 1: The "Extorted Identity"

**Theme:** Adversary-in-the-Middle (AiTM) Phishing & Double Extortion Ransomware

**Target:** Mid-sized Healthcare Organization (Finance/Billing Department)

**Estimated Duration:** 90 Minutes

## 1. Concept Overview

A sophisticated threat actor utilizes a session-hijacking phishing attack to bypass Multi-Factor

Authentication (MFA). The primary goal is to target the Finance and Billing department to

exfiltrate Patient Health Information (PHI) and financial records before deploying a ransomware

payload to maximize coercive pressure.

## 2. Initial Compromise

A senior Billing Coordinator receives an "urgent" email appearing to be from the hospital's CFO.

The email contains a link to a "Video Memo" regarding urgent 2026 payroll tax changes. The video

uses **AI-generated deepfake audio and video** of the CFO.

When the coordinator clicks the link, they are directed to a proxy login page that mimics the

organization’s Microsoft 365 portal. The coordinator enters their credentials and completes the

MFA prompt. The attacker’s proxy server captures the **active session token**, allowing them to

bypass MFA entirely and access the coordinator's mailbox and cloud storage.

## 3. Progressive Injects

### Inject 1: Detection & Initial Response (T + 30 mins)

The Security Operations Center (SOC) triggers a high-severity alert: "Anomalous Data Movement."

Forensic logs show the Billing Coordinator’s account is transferring large volumes of data to an

unrecognized IP address in Eastern Europe. Simultaneously, Azure AD logs show the account is

logged in from both the hospital’s local IP and a known VPN exit node.

[...] 1

1 Content removed for brevity.

In this example, the model generated multiple scenario concepts that facilitators can evaluate for relevance

to organizational needs. This approach works well when exploring different incident types or when

facilitators need inspiration for exercise themes. Generated concepts serve as starting points that

facilitators can refine based on team maturity, recent incidents, or specific skills the exercise should

develop.

Organizationally-Grounded Scenarios

More sophisticated scenario development incorporates actual organizational data to increase realism and

relevance. By providing AI models with sanitized copies of log files, network diagrams, asset inventories, or

authentication records, facilitators can generate scenarios that reflect the actual technical environment

participants will recognize.

This approach addresses a common limitation of generic tabletop exercises where participants struggle to

connect hypothetical scenarios to their real infrastructure, tools, and procedures. Scenarios grounded in

organizational artifacts use familiar system names, realistic user accounts, and actual log formats, making

the exercise more engaging and the lessons more transferable to real incidents.

Consider a business email compromise scenario where the facilitator wants to create realistic

authentication and email activity patterns. The facilitator can provide the AI model with a Microsoft 365

audit log export (appropriately sanitized using techniques described in Data Handling Considerations) along

with a structured prompt as shown in Listing 134.

Listing 134 | Organizationally-Grounded Tabletop Exercise Scenario Prompt

Using the Microsoft 365 audit log data attached, develop a business email compromise tabletop

exercise scenario. The scenario should:

- Use actual usernames, email patterns, and authentication behaviors from the logs to establish

realistic baseline activity

- Identify a plausible initial compromise vector consistent with the authentication patterns

observed

- Create a timeline of attacker actions that would produce log entries similar in format and

structure to the provided data

- Include three progressive injects that reveal new information through additional log entries

- Provide facilitator guidance on what log patterns participants should identify at each phase

Learning objectives:

- Email header analysis for spoofing detection

- Correlation of authentication logs with email activity

- Escalation procedures for financial fraud attempts

- Communication with executive stakeholders during active fraud attempts

Target duration: 30 minutes

Figure 159 | Google Gemini Organizationally-Grounded Tabletop Exercise Scenario Generation

In this example, we used Google Gemini with a Microsoft 365 interactive login data file to supply context for

the scenario. The model analyzed the log file structure, identified normal patterns in the data, and

generated a scenario in which attacker activity would appear as anomalies relative to the established

baseline. The compromise vector, injects, and facilitator guidance all reflected events in the supplied

logging data, making the exercise feel authentic to participants familiar with their environment.

The fastest way to combat participant complaints of "this isn’t realistic" is to ground the

Figure 160 | Google Gemini Tabletop Exercise Scenario Output

Facilitators can apply this approach with various organizational artifacts, including network traffic captures

for intrusion detection scenarios, cloud audit logs for insider threat exercises, or EDR telemetry for malware

response training. The important requirement is to provide sufficient sample data for the model to

understand the format, structure, and normal patterns, while applying prudent caution to sanitize sensitive

information.

Gamified, Interactive Exercise Generation with Twine

A more sophisticated AI-assisted tabletop scenario development produces interactive formats that

participants can navigate through branching decision paths. Twine, an open-source tool for creating

nonlinear interactive narratives, provides an effective platform for tabletop exercises where participant

choices affect scenario progression. Twine is widely used for interactive storytelling and game

development, allowing authors to develop complex branching scenarios with rich media and conditional

logic, as shown in Figure 161 . Twine produces HTML report output, allowing authors to customize the

storytelling experience with custom CSS and other rich content, producing interactive decision elements

like the example shown in Figure 162.

Think of Twine as a tool for creating "choose your own adventure"-style stories where the

reader makes choices that influence the narrative path. Through rich media, scripting

capabilities, and conditional logic, Twine can create complex interactive experiences as

HTML, making it a great option for gamified tabletop exercises.

Figure 161 | Twine Story Authoring Interface

Figure 162 | Twine HTML Output Example

Traditional tabletop exercises often use linear progressions in which facilitators reveal injects at

predetermined intervals or when they deem appropriate. Interactive formats allow exercises to branch

based on choices, showing participants the consequences of different response strategies. For example, if

participants choose immediate containment before scoping, the scenario might reveal unrecognized

compromises and missed opportunities to effectively contain the entire incident. Alternatively, if the

participants use an IOC to effectively scope the breadth of the incident, they might unlock more evidence

that provides valuable insight into attacker tactics that can be applied later in the scenario.

AI models can generate Twine-compatible output files ( .twee) that facilitators can import directly into

Twine for interactive exercise delivery. Twee files are plain text that define passages (scenario states) and

links (choices) in a structured format, as shown in the example in Listing 135.

Listing 135 | Twee Format Example

:: StoryTitle

The Incident Response Book Author

:: Start

You sit down at your desk, coffee in hand, ready to write your book on incident response. The

blank page stares back at you.

Where do you begin?

[[Start with the fundamentals of IR->Fundamentals]]

[[Jump straight into real-world case studies->CaseStudies]]

:: Fundamentals

You decide to lay the groundwork first. Chapter 1: "What is Incident Response?"

You write about the DAIR model: Prepare, Detect, Verify/Triage, Scope, Contain, Eradicate,

Recover, Debrief. You explain each phase with clear examples.

[[Continue to detection techniques->Detection]]

[[Add a war story from your past->WarStory]]

:: CaseStudies

You open with a gripping supply chain hack: Supply Chain Calamity. You provide first person

perspectives from the incident response analyst, and the attacker.

[[Add a brief intro chapter first->Fundamentals]]

[[Trust the reader and keep going->Detection]]

In Twine, each passage begins with :: PassageName, followed by the content presented to

the user, including possible decision links marked with -> and the target passage name.

GAMIFIED LEARNING FOR INCIDENT RESPONSE TRAINING

Gamification applies game design elements to non-game contexts to increase engagement and

improve learning outcomes. Interactive tabletop exercises using Twine incorporate several

gamification principles that enhance the effectiveness of incident response training.

Choice and Consequence

Branching scenarios, where decisions lead to different outcomes, engage participants more deeply

than passive observation. Responders see the direct results of their choices, reinforcing the

connection between actions and consequences in ways that traditional exercises cannot achieve. This

immediate feedback loop accelerates learning by making abstract concepts concrete.

Safe Experimentation

Gamified exercises create low-stakes environments where participants can explore risky decisions

without real-world consequences. An analyst can choose to delay containment to gather more

forensic evidence and observe what happens when the attacker escalates. In traditional exercises,

fear of making the "wrong" choice in front of peers can inhibit learning. Interactive formats remove

engagement and more meaningful skill development among incident response teams.

AI models can generate Twine-compatible scenarios using structured prompts that define scenario

elements, decision points, and learning objectives. By providing the model with clear instructions and

examples of the desired output format, facilitators can produce interactive scenarios that they can import

directly into Twine for exercise delivery.

I have developed a sample prompt that will help analysts generate interactive tabletop exercise scenarios in

Twine format, available at [課程範例連結] Using this prompt, the model will

ask the user a series of questions to gather the necessary context for scenario generation. These questions

are optional, but providing detailed answers will better align the generated scenario with organizational

needs:

1. What type of security incident should this exercise cover?

2. Describe the target organization.

3. How was the incident first detected?

4. What are the critical systems or data assets at risk in this scenario?

5. Any specific threat actor profile you want to use?

6. What are the key learning objectives?

7. Do you have any supporting documentation, log files, or other content you would like me to integrate to

add organization-specific context and realism?

For this application of accelerating incident response with AI, I downloaded the prompt from my terminal

using wget (you can also download it from your browser), saving the file as PROMPT.md, as shown in Listing

136. Next, I launched Claude Code to generate a Twine tabletop exercise, directing it to use the prompt file

to guide scenario creation, as shown in Figure 163.

Listing 136 | Twine Tabletop Exercise Prompt Setup

$ wget -q -O PROMPT.md [課程範例連結]

$ ls -l

total 32

-rw-r--r--@ 1 jwright  staff    12K Jan 17 11:22 PROMPT.md

Figure 163 | Claude Code Twine Tabletop Exercise Prompt Processing

“Read and process the prompt directions in @PROMPT.md

In this section, we’re using Claude Code to utilize file system access for prompt

management and output handling. OpenAI’s Codex and Google Gemini CLI tools also

Figure 164 | Claude Code Twine Tabletop Exercise Prompt Question

After answering the questions, the model generates a Twine-compatible .twee file, as shown in Figure 165.

Building and viewing the scenario as an HTML file allows the participant to navigate the interactive exercise,

making decisions and exploring different paths based on their choices, as shown in Figure 166.

Figure 165 | AI-Generated Twine Tabletop Exercise Decision Passages

Figure 166 | AI-Generated Twine Tabletop Exercise Story View

Analysts can review the scenario in Twine and make any necessary adjustments. Alternatively, they can

return to Claude Code to further refine the scenario by providing additional context or requesting

modifications to specific passages or decision points to enhance the exercise experience as desired.

Using the supplied prompt, the Twee supports event saves  so the participant can save

progress, make decisions, and return to previous saves to experiment with different choice

outcomes.

The intermediate techniques covered in this section demonstrate how AI can enhance common incident

response workflows, from drafting reports and generating playbooks to building interactive training

exercises. These capabilities represent practical, immediately applicable uses of AI that require minimal

infrastructure beyond access to an AI model. In the next section, we’ll look at more advanced use cases that

integrate AI with external systems for automated data retrieval, real-time analysis, and orchestrated

response actions across security tooling.

ADVANCED USE CASES

Emerging integration standards and agentic AI systems present significant opportunities to accelerate

incident response workflows. The Model Context Protocol (MCP) enables AI models to query security tools

directly, while agentic systems can execute multi-step analysis tasks with minimal human intervention.

These capabilities allow response teams to offload routine data gathering and correlation tasks, freeing

analysts to focus on decision-making and containment actions.

In this section, we’ll first examine MCP architecture and how it enables AI models to query security tools,

automate enrichment, and correlate information across platforms. We’ll also look at Protocol SIFT as a

concrete example of using these capabilities to accelerate forensic investigations during incident response.

Model Context Protocol for Defensive Operations

As we saw earlier in this chapter, MCP provides a standardized method for connecting AI models to external

tools and data sources. MCP addresses a fundamental integration challenge: enabling AI systems to interact

with the diverse applications and data sources that security teams rely upon.

In this section, we’ll look at the structure of MCP architecture and how MCP can enhance defensive

operations by enabling AI models to retrieve real-time data from security tools, automate enrichment tasks,

and correlate information across platforms.

Understanding MCP Architecture

To understand how to best utilize MCP to accelerate incident response, it helps to examine its

architecture and components. MCP defines several components:

• MCP Client: The interface through which users interact with the AI model (chat applications, software

IDEs, custom interfaces).

• MCP Server: A service that publishes tools the AI model can invoke to retrieve data or take actions.

• Underlying Applications : The actual systems and data sources (SIEMs, ticketing systems, threat

intelligence platforms, cloud services, source code management systems, etc.).

Figure 167 | MCP Architecture Diagram

When a user issues a prompt, the MCP client informs the model about available tools. The model can then

request tool execution to gather information relevant to the user’s request. Results flow back through the

client to augment the model’s response with live data.

This architecture means an analyst can issue natural language queries that obtain data (stored or

dynamically generated) from connected security tools:
