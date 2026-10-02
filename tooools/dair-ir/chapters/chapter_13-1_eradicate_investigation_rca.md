# Chapter 13-1: Eradication: Root Cause Analysis (RCA), 5 Whys & Forensic Investigation

> Modular Sub-Chapter | Source: DAIR-IR Framework

---

# Chapter 13: Eradicate Activity: Persistence Removal & Patching

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

◦ Apply per-user or per-device VPN access policies to restrict compromised sessions without disrupting all remote workers.

◦ Leverage identity-based controls and conditional access policies for SaaS applications accessed directly over the internet.

◦ Coordinate with employees for secure device recovery through shipping or on-site visits.

◦ Balance forensic evidence preservation against business continuity and logistical complexity.

2. Manage BYOD and personal device scenarios, including:

◦ Use MDM or MAM solutions to selectively manage corporate data without affecting personal information.

◦ Apply conditional access policies requiring device compliance for corporate resource access.

◦ Respect privacy boundaries while maintaining organizational security requirements.

3. Account for encrypted communications challenges, including:

◦ Implement TLS inspection proxies where possible to analyze encrypted communications from attackers.

◦ Restrict egress TLS traffic to pass through inspection points and investigate connections that bypass them.

◦ Address DNS over HTTPS (DoH) limitations by using host-based DNS overrides, local DoH servers, or browser policy controls to redirect attacker domains.

◦ Balance the benefits of security inspection against privacy concerns and application compatibility issues.

4. Address non-traditional compromise scenarios, including:

◦ Implement email flow redirection and conditional access for Business Email Compromise incidents.

◦ Coordinate with external parties for supply chain and partner ecosystem breaches.

◦ Focus containment on access control boundaries when direct system control is unavailable.

◦ Revoke API access tokens to prevent further data synchronization with compromised third parties.

Step 6. Collect and Preserve Evidence This step preserves volatile evidence; eradicate Step 1 interprets the captured artifacts during short-form investigation.

1. Determine evidence collection timing based on organizational priorities, including:

◦ Weigh the loss of possible evidence due to containment actions against the risk of allowing attackers to maintain access while evidence is collected.

◦ Organizations with robust logging and external data sources (network flow logs, host telemetry agents, NDR) can isolate first, then collect, reducing attacker interference.

◦ Organizations without alternate data sources for volatile network connections should collect before isolation so evidence of active connections is not lost.

2. Prioritize volatile data collection immediately, including:

◦ Capture memory dumps from affected systems using a whole-system memory acquisition tool appropriate to the OS.

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

◦ Validate containment using external data sources (network flow logs, host telemetry agents, NDR tools) when network isolation severs direct connections to contained systems.

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

4. Establish baselines and compare pre-containment and post-containment activity, including:

◦ Document expected process activity on contained systems and investigate deviations.

◦ Compare network traffic, process execution, and log activity before and after containment.

◦ Verify that malicious activities have ceased rather than shifted to different techniques or alternative infrastructure.

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

13 Eradicate Activity

The eradicate activity represents an important waypoint in the incident response process where the focus shifts from containing the attacker’s operations to systematically removing their presence and undoing the changes they made to the environment. Unlike containment, which aims to stop the attacker’s ongoing activities and prevent continued access, eradication focuses on eliminating the attacker’s access and restoring systems to a secure state. Eradication stops short of full recovery, instead focusing on building the understanding needed to safely restore normal operations in the subsequent recover activity.

Figure 91 | Eradicate Activity Waypoint

This chapter covers the objectives of eradication, strategies for timing and sequencing eradication actions, investigation techniques to inform eradication efforts, and practical steps for removing attacker artifacts and persistence mechanisms from the environment. It also addresses validating eradication success and documenting eradication activities for future reference before looking at activity examples.

ERADICATE OBJECTIVES

Effective eradication requires comprehensive insight gained through investigative actions and careful analysis of collected evidence. Like the contain activity, the eradicate activity consists of two primary components: analyzing the collected data and eliminating the attacker’s presence. However, decisions made during eradication will have a significant impact on the environment, requiring a careful balance between investigative rigor and urgency to restore operations while meeting the organization’s needs. In this section, we’ll examine why thorough investigation prevents recurrence rather than only treating symptoms, how short-form and long-form investigation tracks run in parallel to balance urgency against forensic depth, and how root cause analysis uncovers the conditions that enabled the compromise.

Preventing Incident Recurrence Through Investigation

The temptation to skip investigation and jump straight to system rebuild is a common problem during eradication. Wiping a drive, reinstalling the operating system from scratch, and restoring from backup appear to guarantee a clean system. Decision makers may show a preference for this approach because it even offers a specific, tested timeline learned during Business Disaster Recovery (BDR) preparedness: "The system will be back online in four hours."

However, this shortcut fails to address the underlying causes of the compromise. Without determining what caused the incident and identifying the root cause, the risk of recompromise through the same vector remains. Organizations repeatedly experience a familiar pattern: analysts take systems down and rebuild them from clean media or gold images, then return them to production, only for the attacker to compromise the same systems again hours, days, or weeks later. In the eradicate activity, incident response teams need enough understanding to answer specific questions:

• What was the initial access vector? (Has it been closed?)

• What credentials were compromised? (Have they been rotated?)

• What other systems did the attacker access? (Are they also eradicated?).

• What persistence mechanisms did the attacker deploy? (Are they all identified and removed?).

• What vulnerability enabled the attack? (Has it been patched?).

Investigation provides the answers that prevent incident recurrence.

Investigation During Eradication

The eradication activity focuses on removing the attacker’s access and returning systems to a more secure state. However, the pressure is on: contained systems cannot serve their intended purpose, users are disrupted, and the organization is losing productivity by the hour. System owners want production assets back online immediately. The IRT should recognize that rushing eradication risks leaving persistent access mechanisms and vulnerabilities behind, which can lead to new incidents days later. At the same time, analyzing the collected evidence takes time. Analyzing logs, memory captures, disk images, and network traffic to understand the attacker’s methods and persistence mechanisms can take days or weeks. The longer the investigation takes, the longer systems remain offline, increasing business impact and stakeholder frustration.

This tension defines the eradicate activity: balance the investigative work needed to understand what the attacker did against the urgent need to restore operations. Rushing to rebuild without investigation could leave the same vulnerability open for the attacker to return. Spend too long investigating every detail, and the business impact compounds while leadership questions why systems remain offline days after the problem was contained. To best accommodate the organization’s needs, incident responders can separate the investigation into two tracks: an immediate investigation to inform eradication actions, and a deeper forensic analysis that continues in parallel.

These two investigative tracks, referred to here as short-form investigation and long-form investigation, serve distinct purposes during eradication, as shown in Short-Form vs Long-Form Investigation.

Figure 92 | Short-Form vs Long-Form Investigation

Short-form investigation focuses on quickly analyzing the evidence collected during containment to identify the attacker’s methods, persistence mechanisms, and compromised systems. The goal is to gain sufficient understanding to inform prompt eradication actions, minimizing business disruption. Long-form investigation can continue in parallel, delving deeper into the attacker’s tactics, techniques, and procedures (TTPs). This track aims to build a comprehensive understanding of the incident for future prevention, legal proceedings, or organizational learning. A long-form investigation may involve more extensive forensic analysis and collaboration with external experts. While this track will take longer and require more investigative resources (and cost), it may meet additional organizational requirements beyond immediate eradication needs, such as regulatory compliance or evidence preparation for legal proceedings. Working with decision makers throughout eradication to define the scope and priorities of these two investigative tracks helps ensure that the incident response team meets both the urgent need to restore operations and the longer-term goal of understanding and preventing future incidents.

Short-Form Investigation to Inform Eradication

The eradication activity requires that analysts investigate the evidence collected during containment to understand the attacker’s methods and persistence mechanisms, then take action to remove the attacker from the environment. Responders need enough understanding to answer critical questions:

• What did the attacker do?

• How did they get in?

• Where else might they be?

• What needs to be removed to ensure they cannot return through the same methods?

Eradication demands a practical understanding of the attacker’s TTPs sufficient to ensure their complete removal from the environment. As incident responders discover new indicators of compromise or persistence mechanisms during eradication, they should expand their efforts accordingly, contributing new insight into additional iterations of the response actions loop.

Eradication requires practical remediation: remove what the attacker installed, close the entry points they exploited, and restore systems to operation with confidence that the compromise will not immediately recur. Developing this understanding and applying it is the focus of the eradicate activity, with particular emphasis on performing root cause analysis to uncover the full scope of the compromise and prevent the same attack from succeeding again.

THE DIRTY KEBAB: SHORT-FORM INVESTIGATION

My tech editor Steve Armstrong and I were on a call discussing a compromised Windows workstation caught up in a broader incident he was coordinating. The threat hunting team suspected the workstation belonged in scope, and Steve needed to make a quick decision on what kind of priority the workstation warranted for eradication. He didn’t need a forensic masterpiece. He needed enough detail to make a decision. In his delightfully British way, he put it like this: “Sometimes all you need is a dirty kebab.

This was a new expression for me. Steve explained: a dirty kebab is the late-night staple of British pub-goers, a doner (meat cooked on a rotisserie) slathered in "an illegal amount of chili garlic sauce" from a takeaway shop you’d never visit sober. It’s not gourmet. It’s not pretty. But at one in the morning on the walk home, it’s exactly what’s called for. The closest American equivalent, he offered, is a gas station hot dog, with roughly the same gastric risk profile. The metaphor was spot-on. Sometimes, short-form investigations are all that is required to get just enough insight to inform incident response actions. A short-form investigation skips the deep forensic rigor in favor of answering the immediate question: is this system compromised, and what needs to be removed to be confident it isn’t anymore? Responders deliver an early assessment, the analysis. The dirty kebab approach is another tool available to the organization to manage resources, to gain quick insight when time is limited, and to support the urgent need to restore operations. The art is knowing when the case calls for a dirty kebab and when it calls for something more substantial.

Long-Form Investigation for Comprehensive Understanding

While short-form investigation focuses on gathering enough understanding to inform eradication actions, long-form investigation (sometimes, deep-dive investigation ) may continue in parallel to build a comprehensive understanding of the incident. Long-form investigation aims to uncover a greater understanding of the incident using forensic analysis techniques that often require more time and specialized expertise.

Long-form investigation serves purposes beyond immediate eradication needs. Organizations may require detailed forensic analysis for regulatory compliance, legal proceedings, insurance claims, or threat intelligence development. These investigations document the complete attack timeline, identify all compromised data, and build comprehensive evidence packages that meet legal standards for admissibility. It can be difficult or impossible to perform this level of detailed analysis within the time constraints of urgent eradication efforts, but it is also important not to hold up the business objectives of restoring operations. Organizations should balance the need for short-form investigation to support eradication with the benefits of long-form investigation for broader organizational goals. The depth and rigor of long-form investigation exceed what is practical during urgent eradication efforts, but they provide value for organizational learning, future prevention, and regulatory or legal proceedings.

The scope of long-form investigation should be defined in coordination with decision makers based on organizational requirements:

• Legal counsel confirms which evidence standards apply for potential litigation or regulatory reporting (ideally as part of the prepare activity rather than mid-incident).

• Compliance teams can specify the documentation required to satisfy audit requirements or regulatory obligations.

• Risk management can determine the level of investigation warranted based on the severity and impact of the incident.

This coordination ensures that investigative resources focus on activities that provide tangible value to the organization.

Incident response teams should work with decision makers to define the scope and priorities of investigation tracks during the eradication activity. Wherever possible, organizations should focus on short-form investigations to inform eradication actions, while long-form investigations continue in parallel to meet broader organizational goals.

LONG-FORM INVESTIGATION EXAMPLE: IDAHO MURDERS

Heather Barnhart, DFIR Curriculum Lead and Head of Faculty at SANS Institute, was a principal investigator on a high-profile criminal case involving the murders of four University of Idaho students: Madison Mogen, 21; Kaylee Goncalves, 21; Xana Kernodle, 20; and Ethan Chapin, 20. In an RSAC 2025 webcast, Heather shared insights from her experience applying long-form digital forensics techniques to support the criminal investigation and dispel the alibi of the perpetrator, Bryan Kohberger (BK). [1]

Figure 93 | BK Android Device Log

The investigating team seized BK’s Android phone and performed a comprehensive forensic analysis of the device, using Magnet GrayKey to unlock it and extract a full image of the phone storage. Using Cellebrite Physical Analyzer, Barnhart reviewed the device logs to reconstruct BK’s actions leading up to and following the murders. Through native data extraction and subsequent manual analysis, including the use of the Android eRR.p log file, Barnhart identified when BK powered down his phone then powered it back on at 100% battery. This evidence revealed actions inconsistent with his alibi and corroborated his anti-forensic efforts to hide his presence at the crime scene. Barnhart’s long-form investigation provided critical evidence that BK had been at the crime scene during the time of the murders, contradicting his claims of being elsewhere. The thoroughness of the forensic analysis contributed to BK’s guilty plea, supporting investigators in achieving justice for the victims and their families.

The same forensic rigor that Barnhart applied to criminal investigation translates directly to incident response. Long-form investigation in IR contexts demands similar depth: full device imaging, manual

Pursuing Root Cause Analysis

Whether during short-form or long-form investigation, root cause analysis remains a central objective of the eradicate activity. Root cause analysis serves an important purpose: understanding the vulnerabilities or shortcomings in the organization’s security that led to the attacker’s opportunity. While addressing the underlying security weaknesses discovered through this analysis belongs in the recover activity, understanding how the attacker exploited those weaknesses is essential to effective eradication. When incident responders understand only the symptoms of compromise without investigating the root cause, they risk leaving behind persistence mechanisms or overlooking compromised systems. For example, discovering malware on a system is a symptom, but understanding that the malware arrived through a phishing email that compromised multiple user accounts reveals the scope of systems that require eradication efforts.

In the eradication activity, incident responders evaluate the information collected during containment to assess and understand the attacker’s methods. Working backwards from the symptoms of compromise to identify shortcomings in the organization’s defenses builds the understanding needed to effectively remove the attacker from the environment.

In modern incidents, attackers often leverage multiple opportunities and security shortcomings to gain and maintain access to the environment. Root cause analysis helps identify all these opportunities, ensuring that eradication efforts address the full scope of the compromise rather than just the most obvious symptoms.

FINTECH SSH COMPROMISE: ROOT CAUSE ANALYSIS

Bob wanted to fire Alan. I wanted to know what Bob was covering up. Several years ago, I worked on an incident response engagement for a fintech company that had suffered an SSH compromise of its Linux transaction-processing cluster. An external attacker gained root access to one of their servers, and we were called in to investigate. Bob, the security lead, met us at the door with his conclusion ready: "Alan set a weak root password. The attacker guessed it. Alan needs to be fired. You’re not needed here." I thanked him for the input and explained we’d be conducting our own investigation anyway. During our analysis, we learned that Alan was a junior sysadmin: recently hired, he had some IT background, but was light on cybersecurity and Linux experience. He’d been working a ticket and changed a root password to company123. The server was internet-facing with SSH password authentication enabled. An attacker found it and walked right in. Bob was right about the password. He was wrong about everything else. When we presented our findings to the executive team, Bob repeated his theory: "Alan’s weak password caused the breach. We need to fire Alan." "The password was definitely a factor," I said. "But let’s talk about what else we found." Our root cause analysis revealed a stack of failures:

• SSH was exposed to the internet with no documented business justification.

• Remote root login was enabled, a non-default SSH server setting.

• Password authentication was allowed instead of key-based authentication.

• Failed authentication attempts were logged, but no one monitored them.

• No password complexity policy existed to prevent weak passwords.

• No change control process required approval for root password changes on production systems.

The executives started asking the obvious questions: Why wasn’t monitoring in place? Who approved the SSH configuration? Why weren’t these basic controls implemented? We later learned that Bob was responsible for all of these. He’d prioritized changes to make remote access and management easier, while deprioritizing SSH security features. Alan wasn’t fired. Root cause analysis isn’t about finding who to blame or focusing on a single element of the incident. Instead, it’s about finding what to fix. Often, those are different things.

Assessing Root Cause

During the eradication activity, effective root cause analysis is essential for complete incident resolution. Without understanding the underlying causes of the compromise, responders risk leaving persistence mechanisms in place, missing compromised systems, or allowing the same attack to succeed again through different entry points. Root cause analysis helps responders move beyond simply removing the attacker’s immediate access to addressing the systemic weaknesses that exposed the environment to compromise. Root cause analysis during incident response serves several goals. First, it helps the response team understand the complete attack chain, from initial access through privilege escalation, lateral movement, and data exfiltration, ensuring analysts identify all compromised systems and artifacts requiring eradication. Second, it reveals systemic weaknesses in security controls, processes, and policies that enabled the attack. Finally, it guides eradication priorities by distinguishing between surface-level symptoms and underlying causes that, if left unaddressed, would enable similar attacks.

To perform systematic root cause analysis during incident response, responders follow a structured approach:

• Define the effect: what happened, which systems were compromised, what data was accessed, and what business impact occurred.

• Group possible causes into categories using a framework that organizes contributing factors, such as the four P’s: People, Process, Product, and Policy.

• Populate each category with specific findings from the investigation.

• Identify remediation activities for each root cause.

• Prioritize and implement changes that address multiple contributing factors or the highest-risk exposure areas.

The four P’s framework provides a method for categorizing root causes. Used in incident response, it helps organize findings from investigations into manageable areas for analysis and remediation. By recognizing that incidents often result from a combination of human, procedural, technical, and governance failures, responders can use the four Ps as a tool to brainstorm and document root causes:

• The People category encompasses human factors, including insufficient training, lack of security that contributed to the incident.

• The Process category captures procedural shortcomings, such as missing security reviews, inadequate change management, insufficient vulnerability scanning, or absent monitoring processes.

• The Product category addresses technical factors, including software vulnerabilities, misconfigured systems, missing security features, inadequate logging capabilities, or end-of-life (unmaintained) technology.

• The Policy category covers governance issues such as missing or inadequate security policies, unclear accountability, insufficient compliance requirements, or a lack of enforcement mechanisms.

Next, consider applying this root cause analysis approach to a cloud security incident example.

Root Cause Analysis Example: Public S3 Bucket Exposure

My team worked on an incident for a customer where an S3 bucket named sample-cdn-bucket containing customer data had been publicly accessible for several months, resulting in unauthorized data exposure. The initial investigation identified the immediate cause: a developer misconfigured the S3 bucket permissions when deploying a new feature, setting the access control to allow any authenticated S3 principal to list and read the bucket contents, as shown in Listing 62.

Listing 62 | Permissive Principal Policy for S3 Bucket

{
"Id": "sample-cdn-bucket-Policy",
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
"arn:aws:s3:::sample-cdn-bucket",
"arn:aws:s3:::sample-cdn-bucket/*"
],
"Sid": "AllowPublicRead"
},
]
}
1 Grant all Get and List privileges on the bucket to any AWS user.

This surface-level analysis pointed to a single action: a developer’s misconfiguration. However, applying systematic root cause analysis reveals a much broader risk of exposure. Using the iceberg model across the four P’s, we can envision the insecure S3 bucket as one element of risk, but the people, process, product, and policy elements should also be considered, as shown in Figure 94.

Figure 94 | S3 Bucket Root Cause Analysis

Looking at the people category, we found that developers lacked adequate training on cloud security best practices and secure AWS configuration. The developer who created the bucket had not received training on S3 access controls or data classification requirements. Additionally, there was no clear understanding within the development team about who was responsible for reviewing and approving cloud infrastructure changes, leading to assumptions that "someone else" would catch security issues. Examining the process category revealed multiple procedural gaps that allowed the misconfiguration to persist undetected. The organization lacked a code review and approval process for Infrastructure-as-Code

(IaC) templates, so the Terraform configuration that defined the bucket’s public access was never reviewed by another engineer. There was no IaC automated scanning before deployment to detect security misconfigurations. The deployment pipeline lacked a security approval gate that would require sign-off before provisioning resources with external access. After deployment, no regular auditing process scanned for publicly accessible S3 buckets across the AWS environment.

The product category identified technical control failures that compounded the problem. The organization’s IaC templates used for provisioning new buckets lacked secure defaults, requiring developers to explicitly configure security rather than inheriting safe settings. AWS CloudTrail logging was enabled, but no alerts were configured to notify the security team when there were unusual access patterns to the bucket. The organization had no automated remediation tools (like AWS Config rules) that would automatically revert dangerous permission changes.

An analysis of the policy category revealed governance and compliance gaps. The organization lacked a data classification policy requiring developers to identify sensitive data and apply appropriate access controls before storage. There was no cloud security policy establishing least-privilege requirements for S3 buckets. The change management policy didn’t require a security review for infrastructure changes, treating cloud This comprehensive root cause analysis transformed a simple developer error into a list of systemic failures that all contributed to the incident. Each identified root cause becomes a target for eradication and recovery actions: developer training programs, code review processes, IaC security scanning tools, secure default templates, automated alerting and remediation, and comprehensive cloud security policies. By addressing these underlying causes rather than simply changing the bucket permissions back to private, the organization reduced the likelihood of similar incidents across its entire cloud infrastructure. The improvements extended well beyond this single bucket.

Fishbone Diagram Mapping

A fishbone diagram (also known as a cause-and-effect diagram or an Ishikawa diagram) is a valuable tool to visually represent root cause analysis, illustrating how multiple contributing factors led to the incident. Developed by University of Tokyo professor Kaoru Ishikawa in the 1960s for quality management purposes, the diagram resembles a fish skeleton, with the head representing the problem (the effect) and the bones branching off to represent categories of potential issues (the causes). Ishikawa designed this tool to help teams systematically identify and analyze the root causes of problems rather than just addressing symptoms, using a visual format accessible to different learning styles. Conventionally, the fishbone diagram included primary branch categories that represent the six M’s: Man (people), Machine (technology), Materials (data), Methods, Measurement, and Milieu (environment). An example of a fishbone diagram using the six M categories is shown in Figure 95. [2]

Figure 95 | Fishbone Diagram Example

While defining the six M’s provides valuable distinction for some environments, the structure of the fishbone diagram can be simplified with an approach tailored to incident response. Instead of categorizing each cause under the six M’s, responders can broadly group causes into categories relevant to security incidents using the four P’s. Using the fintech SSH compromise (see Fintech SSH Compromise: Root Cause Analysis), a fishbone diagram using the four P’s captures the root causes identified during the investigation (Figure 96).

There can be overlap between these categories, captured using the four P root cause analysis. This is not intended to be a strict taxonomy, but rather as a tool to consider, identify, and organize potential causes for analysis.

Figure 96 | Fishbone Illustration: Fintech SSH Compromise

By visually mapping root causes, the fishbone diagram helps responders see how multiple contributing factors across people, processes, products, and policies led to the incident. The four P’s approach, integrated with the visual structure of a fishbone diagram, provides analysts with a practical tool for systematically exploring and documenting root causes during incident response.

ALTERNATIVE TO FISHBONE DIAGRAM: THE FIVE WHYS

A fishbone diagram provides a structured way to visualize root cause analysis, and has the distinct advantage of producing a visual map that teams can collaboratively build and analyze. However, it is also easy to become overwhelmed by the number of potential causes and branches in complex incidents, and to waste time on the minutiae of less significant causes. As an alternative, the Five Whys technique, originally developed by Sakichi Toyoda, the founder of what later became Toyota Industries, provides a simpler approach to root cause analysis by repeatedly asking "Why?" to drill down to the underlying causes of a problem. [3] Start with the observed problem and ask, "Why did this happen?" Take the answer and ask "Why?" again, continuing this process five times or until you reach a root cause that, if addressed, would prevent the problem from recurring. The number five is not rigid. Sometimes you reach the root cause in three iterations, other times you need seven. The goal is to move beyond symptoms to identify the underlying systemic issues.

Consider the fintech SSH compromise example using the Five Whys approach:

Problem: Attacker gained unauthorized root access via SSH.

• Why 1:  Why did the attacker gain root access via SSH? Because they successfully authenticated

• Why 2:  Why could they authenticate with the root password? Because the root password was weak, and they guessed it.

• Why 3: Why was the root password weak? Because no password complexity policy was enforced, the system accepted a simple password.

• Why 4: Why was there no password complexity policy? Because no governance process requires security hardening before deploying SSH services.

• Why 5:  Why was SSH even exposed to the internet with password authentication enabled?

Because the deployment process lacked security review and exposure management, the insecure configuration went undetected.

This iterative questioning reveals multiple intervention points: weak passwords, missing complexity policies, lack of governance, and poor exposure management. Each Why layer represents a potential eradication or recovery action that addresses increasingly fundamental issues. The Five Whys works best for focused, linear root cause analysis where a single primary chain of causation exists. Use this technique when you need quick root-cause insight without extensive documentation overhead, when working with small teams that can focus on a single investigation thread, or when the incident appears to have a clear primary cause. Choose fishbone diagrams instead when multiple parallel contributing factors exist, when you need visual documentation for stakeholders, or when conducting collaborative analysis with larger cross-functional teams.

INVESTIGATION TECHNIQUES FOR ERADICATION

Before beginning eradication actions, incident responders should apply investigative techniques to understand the full extent of the compromise and identify all artifacts requiring removal. These short-form investigation techniques should be focused and time-boxed based on the urgency of restoring operations. The response team should focus on gaining sufficient understanding to effectively revoke the attacker’s access and remove their artifacts from the systems involved in the incident. Investigative techniques are an ever-evolving area for digital forensics and incident response. This book focuses on practical, widely applicable methods, but responders should stay current with emerging tools and techniques through ongoing training and professional development. This section reviews practical investigation techniques that can be applied quickly during eradication to gather the necessary insight. This is not intended to be a full treatise on investigative techniques, but rather a practical guide to the most relevant methods for gathering the information needed to inform eradication actions. In this section, we’ll work through investigative approaches by data source and then by incident type. We’ll cover log analysis, live investigation on running systems, endpoint detection and response telemetry, memory forensics, network traffic analysis, and malware examination. We’ll then turn to investigation patterns for specific incident categories: business email compromise, insider threats, supplier and supply chain attacks, and cloud environments.

This point bears repeating: this book is not intended to provide comprehensive coverage of digital forensics investigative techniques. It would be impossible to do so in a single volume. Use the information presented here as a representative sample of practical methods that can be applied for eradication actions.

Log Investigation

Log investigation examines system, application, and network logs collected during the contain activity to reconstruct attacker activity and identify artifacts requiring eradication. Logs provide a temporal record of events on systems and networks, revealing summary and detailed information about both normal and abnormal activities. This historical perspective is valuable during eradication because it can reveal what the attacker did over time, helping responders identify the systems involved in the incident and the artifacts created.

Responders can use logging data collected from multiple systems to understand attacker activities. Logs gathered from multiple sources, including operating system event logs, application logs, firewall logs, VPN logs, authentication servers, and security appliances, each provide their own insight into the events that occurred. The volume of log data can be substantial: a single compromised server may generate gigabytes of logs spanning the attacker’s dwell time. Without proper aggregation and correlation tools, analyzing this data becomes a manual, time-consuming process that delays eradication.

Sigma for Log Analysis

The Sigma project provides a standardized format for writing detection rules that can be applied to log data from various sources. Unlike most detection methods built into commercial platforms, Sigma rules represent a portable set of log analysis and alerting mechanisms that can be quickly applied during log investigation to identify known IOCs and attacker behavior. [4] While Sigma rules represent opportunities to characterize threats in many different log sources, including Windows Event Logs, Syslog, cloud service logs, web server logs, and more, the Sigma project is not an analysis tool in itself. Instead, the Sigma rules and the corresponding Sigma CLI tool provide a framework for defining detection logic that can be converted into queries for specific log analysis platforms. For example, a Sigma rule defining suspicious PowerShell activity can be converted into a Splunk search query, an Elasticsearch query, or a query for other log analysis tools.

However, some tools natively support Sigma rules without requiring conversion into a backend system.  For Windows Event Log analysis, the open-source tool Hayabusa is a fast forensic analysis tool to identify threats using Sigma rules. [5] Hayabusa quickly scans Windows Event Log (EVTX) files and generates a threat report and optional timeline. For an analysis completed using EVTX files from multiple systems collected in January and February 2020, the Hayabusa command shown in Listing 63 generates a CSV timeline report of all identified threats during that period. The resulting CSV file will characterize the identified threats across all analyzed event logs, providing insight into attacker activity during the incident. The timeline of threat events is shown in Figure 97.

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

Start time: 2025/11/24 12:03 Total event log files: 361 Total file size: 35.5 MB [...]

1 Windows EVTX files stored in the eventlogs directory

Figure 97 | Hayabusa Timeline Report

Hayabusa is a valuable tool for analyzing Windows Event Logs during eradication, but Sigma rules are more broadly valuable when integrated into SIEM platforms for log investigation at scale.

SIEM for Log Investigation

Security Information and Event Management (SIEM) platforms address the challenge of analyzing disparate data from multiple log sources. SIEM platforms normalize and aggregate logs into a centralized repository where analysts can search, correlate, and analyze events across the environment. Instead of manually reviewing logs on individual systems, responders can query the SIEM for specific indicators of compromise across all ingested log sources simultaneously. This centralization significantly reduces the time required to scope an incident and identify all affected systems.

Awkwardly, SIEM is pronounced "seam" or "sim," depending on the vendor. SIEM platforms provide significant value to incident response by aggregating, normalizing, and correlating log data from disparate sources. During eradication, this centralized visibility allows responders to quickly pivot from one indicator of compromise to related events across the entire environment. Analysts can track a compromised account’s activity from initial authentication through lateral movement to data exfiltration without manually searching individual system logs. SIEM alerting rules can identify suspicious patterns that span multiple log sources, such as failed authentication attempts followed by successful logins from unusual locations. Further, many SIEM platforms support custom detection rules via frameworks such as Sigma, enabling organizations to rapidly deploy new detections as they discover attacker techniques during investigations.

However, SIEM platforms also present challenges. The platforms require substantial investment in both licensing costs and infrastructure to ingest, process, and store large volumes of log data. Effective SIEM operation demands skilled analysts who understand both the platform’s query language and the nuances of log data from different sources. Detection rules require continuous tuning to reduce false positives while maintaining sensitivity to real threats, creating an ongoing maintenance burden. Log sources need to be properly configured to send relevant data to the SIEM, requiring coordination across IT teams and careful planning about what to ingest, given storage costs.

Organizations that deploy SIEM platforms without investing in the people, processes, and ongoing maintenance required to operate them effectively gain little security benefit despite significant financial investment.

SAME LOGS, DIFFERENT OUTCOMES: THE RIBRIDGES DATA BREACH

In December 2024, the U.S. State of Rhode Island government suffered a compromise that disrupted services providing food security and health care opportunities to approximately 735,000 citizens. The threat actor team known as Brain Cipher compromised several state systems, including the RIBridges platform, after gaining access to a VPN remote access account allocated to a Deloitte contractor working with the state government. After gaining access, the threat actors exfiltrated sensitive information about state residents and then extorted the state government into paying not to disclose the stolen data. [6] In addition to introducing the vulnerability in the VPN remote access system, Deloitte also managed security operations for the state government. A subsequent investigation from CrowdStrike revealed that the threat actors gained access to the Deloitte contractor VPN account in July 2024. The compromise was not reported to the state until December 5, 2024, after Brain Cipher posted an extortion notice on its data-leak site. During this five-month dwell time, the attackers exfiltrated data from multiple systems, including large data transfers to an external cloud storage provider. CrowdStrike’s report indicates that Deloitte failed to investigate the alerts generated by the state firewall management portal regarding these large data transfers: [7] “According to the Crowdstrike (sic) investigation, the RIBridges firewall denied traffic from an external cloud storage provider IP address to an internal IP address on September 10, 2024, and between November 11, 2024 and November 28, 2024, the firewall management portal generated 397 alerts from 15 systems about large data transfers to an external cloud storage provider. — Steve Alder, The HIPAA Journal Following the breach, Deloitte agreed to pay the state government $5 million to cover incident-related expenses with no admission of liability. [8] In October 2025, Deloitte settled a class-action lawsuit from affected state residents for $6.3 million. [9] Additional legal actions remain ongoing.

What makes this incident notable is how logging data served two completely different purposes:

• Detection opportunity missed: Deloitte had actionable firewall alerts during the attacker’s dwell time, but did not analyze them, losing the chance to identify exfiltration and contain the intrusion.

• Incident investigation resource: CrowdStrike used those same firewall logs to rebuild the attacker’s timeline, quantify exfiltration activity, and anchor the eradicate activity.

The contrast underscores a core principle of incident response: logging supports both threat hunting and post-compromise analysis. To be effective, organizations need the people and processes to detect and respond to threats using those resources.

Live Investigation

Live investigation involves using tools directly on systems under investigation to examine their current configuration and state. Using integrated or third-party tools, analysts can directly collect information about the configuration of systems including Windows workstations, cloud control plane configurations, network appliances, and more. Live investigation is often considered the most authoritative source of data for an investigation, since it reflects the state of the system at the time of examination, with no intermediate layers that could introduce errors or omissions in the observed data. While this approach provides valuable insight into system activity and can quickly reveal attacker activity, it carries risks: running commands modifies system state and can destroy volatile evidence. Ideally, this will have minimal impact during eradication, since the containment action should have already preserved necessary evidence.

Use live investigation when responders need immediate answers about system compromise, and the risk of disrupting evidence is acceptable. Data collected during the contain activity should be sufficient to meet forensic requirements, allowing the live investigation to focus on rapid assessment rather than on evidence preservation.

DIFFERENTIAL ANALYSIS FOR THREAT INVESTIGATION

Differential analysis is a threat investigation technique that allows analysts to quickly sort through large volumes of data by comparing known-good baselines to current system states. It works particularly well for live investigation scenarios and for PowerShell output, where the data can be formatted into a simple structure.

Consider for example the task of identifying new or modified services on a Windows system. Running Get-Service in PowerShell produces a list of all services, but sorting through hundreds of entries to find suspicious services can be time-consuming. With a known-good baseline of services captured previously, analysts can apply differential analysis to quickly identify new or modified services. To demonstrate, start by capturing a baseline of services on a known-good system using PowerShell into a file called baseline-services-20251117.txt as shown in Listing 64 . The output is saved to a removable storage drive or network attached storage for later comparison. Next, the analyst runs the same command on the system under investigation, saving the output to services-liveinvestigation.txt as shown in Listing 65.

Listing 64 | Capturing Baseline Services on Known-Good System

PS C:\> Get-Service > E:\baseline-services-20251117.txt 1
1 Run on the known-good system, such as a freshly imaged workstation.

Listing 65 | Capturing Current Services on System Under Investigation

PS C:\> Get-Service > E:\services-liveinvestigation.txt 1
1 Run on the system under investigation.

Finally, on the analyst’s workstation, PowerShell reads the two files into variables ( $baseline and $current) then uses Compare-Object to compare the two files and identify differences, as shown in Listing 66.

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

• The sppsvc (Software Protection service) changed state from Running to Stopped on the system under investigation.

• The TrustedInstaller (Windows Modules Installer service) also changed state from Running to Stopped.

• A new service vjnxSoIt is running on the system under investigation that did not exist in the baseline.

Differential analysis can be applied to many types of data collected during live investigation, including running process names, installed software, scheduled tasks, users and groups, and more. It is an effective tool for quickly eliminating known-good data from the analysis, allowing analysts to focus on new or modified artifacts that may indicate attacker activity.

Endpoint Telemetry Investigation Tools

Using endpoint telemetry tools to investigate an endpoint is another form of live investigation, but one that is easily automated and distributed across many systems from a centralized management console. Platforms such as Velociraptor, GRR Rapid Response , and Osquery provide endpoint telemetry and investigation capabilities that enable responders to query system state, configuration, and activity across multiple endpoints. These platforms are particularly useful for analyzing attacker activity using known Indicators of Compromise (IOCs) and Events of Interest (EOIs), enabling responders to quickly identify compromised Endpoint telemetry and investigation tools are related to but distinct from EDR platforms. Where EDR platforms focus on detecting and responding to threats with preprogrammed detection logic, endpoint telemetry and investigation tools focus on providing visibility into system state and configuration for analysis. While endpoint telemetry tools may have some response capabilities, they are not designed to provide the full range of response actions available in EDR platforms, instead focusing on enabling analysts to perform investigative analysis using IOCs or other custom logic.

Endpoint telemetry platforms often leverage an agent installed on endpoints to collect and report system state, configuration, and activity information using canned or custom hunts or queries. Using a centralized management console, analysts can design queries to collect information from multiple endpoints simultaneously, guiding an investigation into attacker activity and identifying compromised systems. As part of an incident response eradication effort, analysts can use these platforms to investigate EOIs and IOCs across multiple endpoints. Often, these platforms provide asynchronous query capabilities, enabling analysts to run queries across many endpoints and obtain rapid results from accessible systems. Offline systems report their results when they come back online.

Velociraptor IOC Analysis Example

Consider an example in which an analyst is investigating a LockBit ransomware attack using Velociraptor. Working from known IOCs for LockBit, or using earlier investigative data (such as live investigation from a single host), the analyst identifies a suspicious invocation of the Windows fsutil.exe utility, as shown in Listing 67.

Listing 67 | LockBit fsutil SetZeroData Example

cmd.exe /C ping 127.0.0.7 -n 3 > Nul & fsutil file setZeroData offset=0 length=524288
"C:\Users\Jeanluc\Desktop\Lsystem-7d7904945fa2.exe" & Del /f /q
"C:\Users\jeanluc\Desktop\Lsystem-7d7904945fa2.exe"

On the system under investigation, the fsutil file setZeroData  command was used to overwrite an existing file ( Lsystem-7d7904945fa2.exe, the LockBit malware executable) using a repeating null byte range without changing its size, effectively wiping the file’s contents. This anti-forensics technique is used by LockBit and other ransomware platforms to destroy data in place as part of the ransomware operation, hampering investigators' ability to analyze the malware and its behavior. However, it also creates an opportunity for investigators to identify other systems that may have also been compromised using the fsutil file setZeroData command pattern.

To identify other systems that also observed this command execution with the setZeroData pattern, analysts can use endpoint telemetry tools including Velociraptor. The YAML artifact shown in Listing 68 hunts for the pattern setZeroData across multiple Windows logging sources.

Listing 68 | Custom Velociraptor Artifact for IOC Hunting: FsutilSetZeroData

name: Custom.Windows.Detection.FsutilSetZeroData
author: Joshua Wright
description: |
Hunts for invocations of `fsutil file setZeroData`, an in-place file-wiping technique that
zeroes a byte range inside a file without changing its size. Used by LockBit and other
ransomware platforms.
reference:

- hxxps://lolbas-project[.]github[.]io/lolbas/Binaries/Fsutil/

- hxxps://attack[.]mitre[.]org/techniques/T1485/

- hxxps://attack[.]mitre[.]org/techniques/T1070/004/ type: CLIENT parameters:

- name: IocRegex type: regex default: "(?i)setzerodata" description: | Match token `setZeroData` which is effectively unique to this fsutil verb.

- name: ChannelRegex default: "(?i)security|sysmon|powershell" description: | Restrict to the channels that carry a command line. sources:

- query: | SELECT * FROM Artifact.Windows.EventLogs.EvtxHunter( IocRegex=IocRegex, ChannelRegex=ChannelRegex)

Figure 98 | Velociraptor Artifact Hunt Results: FsutilSetZeroData

The primary advantage of endpoint telemetry platforms is the ability to quickly and efficiently investigate multiple endpoints. Used for investigating the details of an incident during eradication ( what other systems exhibit this behavior), or as part of a broader threat-hunting program for scoping an incident, telemetry data accessed through a centralized management console enables analysts to quickly pivot from one system to another. Analysts pivot using creative analysis techniques in the form of detection rules, queries, and hunts.

Memory Investigation

Memory analysis offers a less intrusive alternative to live investigation while providing deep insight into system compromise. Capturing and analyzing system memory enables responders to identify malicious processes, network connections, and other artifacts offline using only the captured memory image and analysis tools. Because it is performed offline, memory analysis can be easily distributed to multiple analysts for parallel investigation.

Memory investigation captures the otherwise volatile state of a system, preserving artifacts that may not be present on disk or in logs. Using captured memory is particularly valuable for identifying the system or process configuration without relying on the running system as an investigative target. Memory analysis can be performed at two levels: whole-system and process-specific.

Process-Specific Memory Investigation

Process memory dumps capture the working memory of a single running process rather than the entire system’s physical memory. This targeted approach reduces the volume of collected data and focuses analysis on the specific process of interest, making it ideal for investigating suspicious applications or malware.

Start by suspending the target process to ensure memory contents remain stable during capture.  The Microsoft SysInternals tool PsSuspend freezes the process without terminating it, preventing the process from modifying its memory during the capture.  After freezing the process, ProcDump (also from SysInternals) can create a complete memory dump of the suspended process, as shown in Listing 69.

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

Process-specific memory investigation is useful for focusing on artifacts from a given process with a small capture data set, but it does not provide in-depth insight into the configuration of the entire system. Use process memory captures when analysts have identified specific suspicious processes and need a detailed analysis of their runtime behavior. For broader investigations that require visibility into all running processes, network connections, and kernel artifacts, whole-system memory capture provides greater value.

Whole-System Memory Investigation

Whole-system memory investigation captures the complete physical memory of a compromised system, preserving all running processes, network connections, registry data, and kernel artifacts. This comprehensive approach to memory capture provides visibility into the entire system state, making it valuable for investigations that require broad context into attacker activity across the target system.

Capturing and Analyzing Memory with Volatility

Memory capture tools acquire physical RAM and paged memory (swap) from the running system without requiring a reboot.  Windows systems can use WinPMEM, while Linux systems commonly use LiME (Linux Memory Extractor). The time required to capture memory depends on the amount of RAM and system performance, but typically takes only a few minutes, as shown in Listing 72. The captured memory image preserves volatile artifacts that disappear when the system is powered off, including running processes, network connections, decrypted data, and malware residing only in memory.

Listing 72 | Capturing Whole-System Memory with WinPMEM

F:\> .\go-winpmem_amd64_1.0-rc2_signed.exe acquire --nosparse ircase504.dmp 1
Writing driver to C:\Users\jwrig\AppData\Local\Temp\1405366611.sys
