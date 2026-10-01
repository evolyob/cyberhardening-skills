# Chapter 17: Specialized IR for Ransomware & Double Extortion

> Source: PDF Pages 542-579 (Total Pages: 38)

Use Case Documentation

Documentation should capture which AI applications have proven valuable and which have not worked well

in specific organizational environments for internal distribution. Not every AI use case succeeds in every

context. Recording what worked (and what did not) helps teams focus effort on high-value applications

rather than repeatedly attempting approaches that have already proven ineffective. This documentation

also helps new team members quickly understand organizational AI practices.

Training

Team members should understand both the capabilities and limitations of AI tools through structured

training rather than relying solely on informal experimentation. Practical exercises build intuition for

effective use. Training scenarios might include analyzing malware samples with AI assistance, generating

incident reports from investigation notes, or troubleshooting common prompt issues. Hands-on practice

reveals where AI adds value and where traditional methods remain superior.

Structured Learning Paths

Effective AI training follows a progressive structure that builds skills incrementally, a learning theory known

as scaffolding. Initial training should cover fundamental concepts: how large language models work,

common failure modes like hallucination, and basic prompt construction techniques. Intermediate training

introduces domain-specific applications such as log analysis, code review, and report generation. Advanced

training addresses complex scenarios, including multi-step analysis chains, API integration, and prompt

optimization for specialized tasks.

Organizations should not assume that general AI familiarity translates into effective security applications.

An analyst who uses AI for personal productivity may still struggle to apply it effectively to malware analysis

or threat intelligence synthesis. Security-specific training bridges this gap by demonstrating how AI

capabilities map to incident response workflows.

Practical Training Exercises

Hands-on exercises often provide the fastest route to effective learning. Consider the training scenarios

organized by skill level as shown in Table 49 . These exercises cover foundational, intermediate, and

advanced skills, helping analysts build confidence progressively.

These exercises work well in a lab environment where analysts can experiment without the

pressure of production time.

Table 49 | Suggested Training Exercises for AI-Assisted Incident Response

LEVEL EXERCISE

Foundational Provide analysts with a simple obfuscated script and have them develop prompts that

successfully decode it, comparing different prompt approaches and their results

Foundational Give analysts a set of log entries containing an obvious attack pattern and have them

craft prompts that identify the malicious activity

Foundational Have analysts generate an executive summary from a provided technical incident

report, then critique the AI output for accuracy and completeness

LEVEL EXERCISE

Intermediate Present a more complex malware sample requiring multi-stage analysis, where

analysts practice breaking the problem into sequential prompts

Intermediate Provide sanitized case notes from a real incident and have analysts generate a draft

incident report, then compare results across the team

Intermediate Have analysts create detection rules from threat intelligence reports, verifying the

rules against known-good and known-bad samples

Advanced Challenge analysts to analyze an unfamiliar log format, developing prompts that help

them understand the structure and identify anomalies

Advanced Present a scenario requiring integration of multiple data sources (logs, network

captures, memory artifacts) and have analysts develop an analysis workflow using AI

assistance at appropriate stages

Advanced Have analysts attempt to make AI produce incorrect analysis through adversarial

prompting, building intuition for verification requirements

Cross-Training Considerations

AI training should not be isolated to a specialized AI team. When only certain analysts understand AI

capabilities, the organization cannot leverage these tools consistently across all incidents. Cross-training

ensures that AI assistance is available regardless of which analyst is assigned to a case.

Consider pairing experienced AI users with analysts who are developing their skills. This mentorship

approach accelerates learning while distributing knowledge across the team. Senior analysts can share

effective prompts, demonstrate troubleshooting techniques, and help newer team members develop

intuition for when AI assistance adds value.

Technical understanding of AI models is important, but equally critical is developing the

creativity and openness to experimentation and failure that drives learning.

Structured AI training improves the organization’s overall incident response capability. Teams that build

systematic training programs develop consistent, reliable AI practices rather than depending on individual

experimentation that may or may not transfer to other analysts. By investing in the consistent adoption of

AI tools, organizations position themselves to benefit from accelerating capabilities across the team rather

than being limited to a few early adopters.

LOOKING FORWARD

Generative AI capabilities continue to evolve rapidly. The specific techniques described in this chapter

reflect current best practices, but those practices will develop as models improve and integration options

continue to expand.

Several trends merit attention as organizations plan AI integration strategies. First, models are becoming

more capable at complex, multi-step analysis. Tasks that currently require careful prompting may become

Accelerating Incident Response with AI | Chapter 16 | 519

straightforward as reasoning capabilities continue to improve. Analysts should periodically revisit prompts

that require extensive structure to determine whether simpler approaches now produce equivalent results.

Agent tool integration standards, such as MCP, are maturing, making AI integration with security tools more

accessible. Broader platform support and easier deployment will reduce the implementation burden for

MCP-connected workflows. Organizations currently unable to justify custom integration development may

find that turnkey solutions become available as the ecosystem matures. Commercial solutions will continue

to emerge that embed AI capabilities into existing security platforms, reducing the need for custom

development.

Security-focused models trained specifically for cybersecurity tasks may offer improved performance for

incident response applications.  Specialized models such as Cisco’s Foundation-sec-8b are purpose-built to

understand cybersecurity language and workflows, with claims of reduced hallucination and improved

performance on security benchmarks compared to general-purpose models of similar size. [9]

These small

language models (SLMs) may provide cost-effective alternatives to large general-purpose models for specific

security tasks in minimally resourced local hosting environments, with the trade-off of reduced versatility

outside their training domain.

The fundamental principles, however, remain stable:

• AI accelerates analysis but does not replace human judgment.

• Verification remains essential regardless of model capability.

• Organizational policies should govern what data can be shared with AI platforms.

• Documentation should reflect how conclusions were reached.

Attackers are adopting AI to accelerate their operations. Defenders who leverage AI effectively can maintain

or improve response times despite increasing attack sophistication. The goal is to identify practical AI

applications that reduce the time and effort required to protect organizational assets.

Analysts who develop fluency with AI tools, understanding both their capabilities and limitations, will be

increasingly valuable as these technologies become standard elements of security operations. The

competitive advantage goes not to teams that adopt AI first, but to teams that integrate AI thoughtfully

while maintaining the verification rigor and analytical skepticism that separate good incident response from

performance theater. Experimentation, practice, and continuous learning position teams to leverage AI

effectively as capabilities continue to advance.

[1] Narayanan, A., & Shmatikov, V., "How to Break Anonymity of the Netflix Prize Dataset," arXiv preprint arXiv:cs/0610105, October

2006, arxiv.org/abs/cs/0610105

[2] Incident Response Playbook Generation Structured Prompt, gist.github.com/joswr1ght/e3902b170b08396fd2b4c46500a56498

[3] Hague, Sabastian, "A step-by-step guide to writing incident response reports," Hack The Box, www.hackthebox.com/blog/writing-

incident-response-report-template

[4] Zeltser, Lenny, "Good IR Reports with AI," zeltser.com/good-ir-reports-with-ai

[5] Anthropic, "Disrupting the first reported AI-orchestrated cyber espionage campaign," November 2025, www.anthropic.com/news/

disrupting-AI-espionage

[6] Anthropic, "Disrupting the first reported AI-orchestrated cyber espionage campaign" (PDF report), November 2025,

assets.anthropic.com/m/ec212e6566a0d47/original/Disrupting-the-first-reported-AI-orchestrated-cyber-espionage-campaign.pdf

[7] Janssen, Jan-Keno, "Autonomous AI Cyberattack: Doubts about Anthropic’s Investigation," Heise Online, November 2025,

www.heise.de/en/news/Autonomous-AI-Cyberattack-Doubts-about-Anthropic-s-Investigation-11080298.html

[8] Yao, Shunyu et al., "ReAct: Synergizing Reasoning and Acting in Language Models," ICLR 2023, openreview.net/forum?

id=WE_vluYUL-X

[9] Singer, Yaron, "Foundation-sec-8b: Cisco Foundation AI’s First Open-Source Security Model," Cisco Blogs, April 2025,

blogs.cisco.com/security/foundation-sec-cisco-foundation-ai-first-open-source-security-model

Accelerating Incident Response with AI | Chapter 16 | 521

17 Incident Response for

Ransomware

RANSOMWARE INTRODUCTION

Ransomware represents one of the most disruptive and financially damaging incident types that

organizations face today.  This chapter addresses ransomware-specific considerations within the broader

DAIR model established in Part 2: A Dynamic Approach to Incident Response . Organizations responding to

ransomware should reference the relevant sections in Part 2 for comprehensive guidance on each response

activity, using this chapter to supplement that foundation with ransomware-specific considerations.

In this section, we’ll examine current ransomware attack trends and financial impact, distinguish between

the different categories of ransomware operations, and explore how multi-vector extortion campaigns

extend leverage beyond encryption.

Ransomware Attack Trends

Ransomware (including data extortion threats) remains one of the most significant cybersecurity threats

facing organizations across all sectors. The number of data leak events, including claims of successful

attacks, has risen steadily from 2022 through the end of 2025.  Chainalysis' 2026 Crypto Crime Report notes

a 50% year-over-year increase in data leak site postings between 2024 and 2025 ( Figure 178 ). Although

victims paid ransom in fewer than 30% of reported cases in 2025, the frequency of ransomware and data

extortion events continues to increase. [1]

Even when the ransom itself is not paid, the overall financial

impact of ransomware incidents remains substantial, including the costs of business interruption, forensic

investigation, legal fees, regulatory penalties, and reputational damage.

Figure 178 | Chainalysis 2026 Crypto Crime Report

“In 2025, ransomware actors received more than $820 million in on-chain payments — an 8% decline

year-over-year (YoY) from $892 million, our updated 2024 estimate. The 2025 total is likely to approach

or exceed $900 million as we attribute more events and payments, just as our 2024 total grew from our

initial $813 million estimate this time last year.

— 2026 Crypto Crime Report, Chainalysis

Modern ransomware has evolved from simple encryption schemes into sophisticated multi-stage extortion

operations. The overlap between ransomware and broader cyber extortion has blurred the boundaries of

what constitutes a ransomware attack, with many campaigns now focusing primarily on data theft rather

than encryption.

Initial access methods have evolved in response to improvements in defender capabilities and endpoint

protection. Remote access mechanisms remain a persistent threat vector, with Remote Desktop Protocol

(RDP) and Remote Monitoring and Management (RMM) tools frequently appearing in ransomware

investigations. Credential attacks against exposed authentication endpoints, such as VPN services, remain

common, particularly against organizations that lack consistent multi-factor authentication requirements.

Phishing and related attacks (voice phishing, SMS phishing, etc.) remain a valuable tactic for adversaries to

harvest credentials and establish initial access. These stolen credentials are often used to subsequently

access VPN concentrators, cloud services, remote desktop systems, or other remote access portals.

Stolen credentials used for initial access may have been compromised weeks or months

before the attack, often on mobile devices, personal computers, or other hosts outside the

response team’s telemetry. The credential theft itself may have occurred entirely outside

Incident Response for Ransomware | Chapter 17 | 523

the victim organization’s environment, leaving no evidence in organizational logs.

SIDEBAR: THE UNTRACEABLE CREDENTIAL PROBLEM

One of the most frustrating findings in ransomware investigations is identifying that attackers used

valid credentials for initial access, and yet having no idea where, when, or how those credentials were

compromised.

This happens often. The response team will identify the first authenticated session from the attacker,

trace it to a VPN or remote access portal, and confirm that the attacker used a legitimate username

and password. But the trail ends there. The credential may have been harvested months earlier

through phishing, stolen by infostealer malware on a personal device, purchased from an

underground marketplace, or obtained through any number of other means that leave no evidence in

the victim organization’s logs.

This uncertainty has practical implications:

Investigation scope : Without knowing how credentials were compromised, responders cannot

confidently close the initial access vector. The organization may implement multi-factor

authentication (MFA) on VPN access, but if credentials were stolen through a phishing campaign

targeting cloud services, additional exposure may remain.

Lessons learned limitations : Given the relevance of  Attacker-in-the-Middle (AitM) attacks that can

negate the effectiveness of MFA implementations, simple implement MFA everywhere  advice is no

longer adequate. Since AitM attacks may occur outside an organization’s security team’s purview, it is

now even more difficult to learn from successful credential-harvesting attacks.

Stakeholder communication: Executives and boards often want to know how did they get in? and how

do we prevent it from happening again?  Honest answers sometimes require acknowledging that the

initial access vector cannot be determined definitively.

When root cause analysis cannot identify the source of the credential compromise, organizations

should focus on controls that reduce the value of stolen credentials, regardless of how they were

obtained: MFA everywhere, conditional access policies, privileged access management, and

monitoring for anomalous authentication patterns. Accepting some uncertainty about initial access is

preferable to false confidence based on incomplete evidence.

Some ransomware campaigns operate without traditional command-and-control infrastructure, relying

instead on legitimate Remote Monitoring and Management (RMM) tools such as ScreenConnect, AnyDesk,

or TeamViewer for remote access. These tools can blend into enterprise environments, making detection

more difficult because the same software may be used without malicious intent by IT support teams or end

users.

The use of Initial Access Brokers (IABs) has professionalized the initial compromise phase of ransomware

operations. IABs specialize in gaining access to victim networks and then sell that access to ransomware

affiliates. This division of labor means that the time between initial compromise and ransomware

deployment can extend to weeks or months as affiliates conduct reconnaissance, escalate privileges, and

position themselves for maximum impact.  Because IABs often use stealthy techniques to maintain access

and disclose credential details only when selling access, Cyber Threat Intelligence (CTI) resources may lack

insight into the specific credentials available for an extended period.

Figure 179 | BreachStars Forum Credential Sales Post

Ransomware operators have increasingly focused on virtual infrastructure and backup systems as primary

targets. Hypervisors running VMware ESXi or similar platforms represent high-value targets because

compromising a single hypervisor can impact dozens of virtual machines. Backup servers, storage systems,

and underlying remote lights-out management (LOM) systems are targeted specifically to eliminate

recovery options before encryption begins.

Attack Differentiation

Ransomware attacks fall into several distinct categories, each requiring different response considerations.

Human-Operated Ransomware (HumOR)

Human-operated ransomware attacks are often the most sophisticated form of ransomware. Skilled

operators or affiliates actively navigate the victim network, conducting reconnaissance, escalating

privileges, and moving laterally before deploying encryption payloads. Attackers make real-time decisions

about which systems to target, how to disable security controls, and when to execute the final encryption

phase. Extended dwell times allow attackers to identify and exfiltrate high-value data, disable backup

systems, and position themselves to encrypt as much of the environment as possible.

In HumOR attacks, the increased use of AI and Large Language Models (LLMs) by threat actors is lowering

the technical barrier to entry. Tasks that previously required skilled operators, including writing convincing

social engineering lures, analyzing complex identity platform permission inheritance, identifying high-value

targets, and adapting tooling to specific environments, can now be accelerated and automated using AI. This

allows ransomware affiliates with limited technical expertise to execute campaigns that previously

demanded experienced operators, effectively expanding the pool of actors capable of conducting

sophisticated, hands-on-keyboard attacks. The practical impact on defenders is an acceleration of

ransomware campaign volume and scope without a corresponding increase in attacker skill.

Incident Response for Ransomware | Chapter 17 | 525

Automated or Mass-Distributed Ransomware

Automated or mass-distributed ransomware campaigns prioritize volume over the precision often

associated with HumOR attacks. Automated delivery mechanisms, such as malicious email attachments or

exploit kits, infect as many systems as possible. The ransomware executes immediately upon delivery

without the reconnaissance and lateral movement characteristic of HumOR attacks. Recovery from

automated ransomware is often simpler because the scope of compromise is limited to systems directly

manipulated through the delivery mechanism.

Encryptionless Extortion

Encryptionless extortion attacks are a growing trend where attackers focus on data theft without deploying

encryption. The threat of data exposure becomes the primary leverage rather than operational disruption

from encrypted systems. Some groups have shifted entirely to this model, recognizing that data theft alone

can generate ransom payments without the technical complexity of reliable encryption and decryption.

Response to encryptionless extortion emphasizes breach notification workflows, data classification to

understand exposure, and regulatory compliance considerations.

Pseudo-Ransomware and Wipers

These attacks appear to be ransomware but offer no viable path to data recovery. Attackers may demand

ransom payments, but either never intended to provide decryption keys or use destructive techniques that

make recovery impossible regardless of payment. Responders should consider the possibility that apparent

ransomware may actually be a wiper, particularly when the ransom note lacks typical negotiation details or

when early decryption attempts fail despite valid keys.

SIDEBAR: RANSOMWARE-AS-A-SERVICE (RAAS) - LOCKBIT’S AFFILIATE

OPERATION

Two significant evolutions have shaped the modern ransomware landscape: the rise of Human-

Operated Ransomware (HumOR) and the Ransomware as a Service (RaaS) business model.

RaaS has democratized ransomware attacks by providing turnkey solutions to affiliates who lack the

technical capability to develop their own ransomware. In this model, operators develop and maintain

the ransomware payload, infrastructure, and negotiation platforms. Affiliates conduct the actual

attacks, from initial access through data exfiltration and ransomware deployment. Revenue is

typically shared between operators and affiliates, with splits varying by operation but often favoring

affiliates who take on the operational risk of conducting attacks.

The May 2025 breach of LockBit’s affiliate panel provided extensive insight into the inner workings of

a mature RaaS operation. [2]

An unknown attacker defaced LockBit’s infrastructure and leaked a

MySQL database dump containing the complete backend of their affiliate program. The leaked data

revealed an operation structured like a legitimate software business, with tiered affiliate

management, standardized tooling, and formalized revenue sharing.

Figure 180 | LockBit Data Breach Defacement [104]

The affiliate panel provided a self-service platform that allowed affiliates to generate customized

ransomware payloads for Windows, Linux, and ESXi environments. Each build was logged with

victim-specific configurations, including encryption keys, target domains, and notes on the victim’s

estimated revenue to calculate ransom demands. The database contained 1,183 ransomware builds

targeting 631 unique organizations over a five-month period.

Figure 181 | LockBit RaaS Database Schema

LockBit’s affiliate management system categorized users with tags such as "verified," "pentester,"

"newbie," and "scammer," allowing operators to track affiliate reputation and performance. New

affiliates paid approximately $777 USD for panel access. The seventy-five registered affiliates operated

Incident Response for Ransomware | Chapter 17 | 527

under a consistent 20/80 revenue split, with operators retaining 20% of each ransom payment. Top-

performing affiliates developed distinct negotiation styles, ranging from professional, businesslike

approaches to calculated coercion and intimidation.

The leaked negotiation logs revealed standardized playbooks that affiliates followed when engaging

victims. Across 208 victim conversations containing over 4,400 messages, affiliates consistently

demonstrated decryption capability by decrypting sample files before discussing payment. Ransom

demands ranged from $3,800 to $4.5 million USD, depending on the victim’s size and industry.

Despite the volume of attacks, less than 10% of negotiations resulted in payment, suggesting that

many victims either restored from backups or accepted data loss rather than paying.

Multi-Vector Extortion Campaigns

Early ransomware families focused almost exclusively on encrypting data and demanding payment for

decryption. Modern groups have evolved into broader extortion operations that apply pressure for payment

across multiple channels simultaneously. In these multi-vector campaigns, encryption is only one part of a

broader strategy that may include data theft, data leaks, distributed denial-of-service (DDoS) attacks, and

direct harassment of executives, employees, customers, or regulators, as shown in Table 50. These tactics

all have potentially significant negative impacts on the organization, and can be combined in various ways to

increase pressure for payment and maximize the attacker’s leverage.

Table 50 | Ransomware Extortion Strategies

ATTACK TECHNIQUE DESCRIPTION

Encryption Core tactic of ransomware to disrupt operations and pressure payment for

decryption keys.

Data Theft Attackers exfiltrate sensitive data, sometimes in conjunction with data encryption,

using the threat of public exposure as leverage for payment.

Data Leaks Attackers publish stolen data on dark web leak sites or send targeted notifications

to customers, partners, or regulators to increase pressure for payment or threaten

reputational damage.

DDoS Attacks Attackers may launch DDoS attacks against the victim’s public-facing

infrastructure to extort payment, threatening prolonged service disruption if

demands are not met.

Harassment Direct contact with executives, employees, customers, or regulators through

phone calls, emails, or social media, used to apply additional pressure for payment

or to threaten reputational damage.

From an incident response perspective, this changes the problem from systems are encrypted  to the

organization is being coerced on several fronts simultaneously.  Encryption may be complete, partial, or

absent; the real leverage often comes from the attacker’s ability to threaten business relationships,

regulatory exposure, and public reputation in a combined assault, as shown in Figure 182.

Figure 182 | Multi-Vector Extortion Campaign Tiers

Multi-vector extortion has several practical implications for organizations:

• Preparation should explicitly account for extortion beyond encryption, including data classification and

mapping for rapid impact assessment, understanding legal and regulatory obligations for potential leaks,

and establishing communication strategies for customers, partners, and regulators.

• Detection efforts need to address both technical and information impacts: determining what data was

accessed or exfiltrated is as important as understanding which systems were encrypted.

• Scoping should evaluate business impact across operational disruption, data exposure, and reputational

risk.

• Response actions frequently require close coordination with legal, communications, and executive

leadership to balance technical containment with the timing and content of public and private

communications.

Recognizing ransomware as one component of a broader extortion attack helps teams frame decisions

appropriately. It also underscores the need for response playbooks, tabletop exercises, and policies that

integrate technical, legal, and business perspectives to build a comprehensive defense strategy.

Modern ransomware response extends beyond restoring encrypted systems.

Organizations should prepare for coordinated pressure across technical, legal,

reputational, and regulatory fronts simultaneously.

In the sections that follow, we’ll address ransomware-specific considerations within each waypoint of the

DAIR model with recommendations for organizations working to improve their response capabilities.

PREPARE

Preparation is the most effective phase for reducing ransomware impact. Organizations with robust

preparation can recover more quickly, limit business disruption, and avoid the worst outcomes that

ransomware can inflict. Investments made before an incident occurs pay dividends when a response

becomes necessary.

This bears repeating: Preparation is the most effective phase for reducing ransomware

Incident Response for Ransomware | Chapter 17 | 529

impact. Response efforts following ransomware incidents are complex, time-consuming,

and costly. Investing the time and resources to prepare thoroughly before an incident

occurs is the best way to limit the damage ransomware can cause.

General incident response preparation is covered in Prepare Activity. This section addresses ransomware-

specific preparation considerations that supplement baseline incident response readiness.

In this section, we’ll work through the preparation areas most relevant to ransomware: establishing crisis

communications capabilities and applying threat intelligence to anticipate attacker behavior. We’ll also

examine opportunities for employee training to recognize social engineering, steps to harden identity and

tier-0 systems against the privileged access that ransomware operators rely on, and approaches for

architecting backups to survive an attacker who has gained privileged admin credentials.

Crisis Communications and Public Relations

Ransomware incidents generate immediate and sustained communication demands that few organizations

are prepared to handle. Organizations should establish crisis communications capabilities before an

incident occurs, either through an internal communications team with incident response experience or

through a retainer agreement with an external crisis communications firm. Waiting until ransomware is

actively encrypting systems to identify a PR partner or draft a holding statement leaves the organization

reactive when controlled messaging matters most.

The speed at which information escapes organizational control during ransomware incidents is a recurring

problem. When ransom notes appear on hundreds or thousands of systems simultaneously, employees

across every department become aware of the attack within minutes. Social media posts, messages to

friends and family, and direct contacts with journalists can put the incident into public view long before the

response team has assessed the situation or leadership has approved any messaging. Organizations that lack

pre-approved holding statements and designated spokespersons find themselves reacting to media

coverage rather than shaping the narrative.

A crisis communications plan for ransomware should address:

• Pre-drafted holding statements that can be quickly adapted to specific circumstances.

• Designating spokespersons authorized to communicate externally on behalf of the organization.

• Establishing internal communication channels and procedures to keep employees informed and

reinforce that only authorized personnel should discuss the incident publicly.

• Escalation procedures that define when and how to engage external communications support.

• Social media monitoring to identify leaks and public discussion early.

• Coordination protocols between technical response teams, legal counsel, and communications staff.

These preparations allow organizations to respond to communication demands quickly and consistently

rather than improvising under pressure.

THE VALUE OF A GOOD HOLDING STATEMENT

A holding statement is a brief, pre-approved message that acknowledges a situation is under

investigation without committing to details that are not yet known or have not cleared legal review.

In crisis communications, the holding statement serves as the organization’s first public word when

news breaks, but facts are still being gathered. Rather than silence, which often invites speculation

and unmanaged disclosure, a holding statement gives the organization a voice in the conversation

before the full picture is clear.

Holding statements do not need to be complete or situation-specific to be useful. A statement

developed during preparation will lack the context of an actual incident. The preparation process is

an opportunity to work through questions the organization will face under pressure: What will be said

first? Who approves the message? How will the situation be characterized without overstating or

understating impact? Working through these questions before an incident allows communications

teams, legal counsel, and leadership to reach alignment without the urgency of an active campaign

and the risk that employees or the press will define the narrative first.

Even template language with placeholder details, such as "We are aware of a technical issue affecting

some of our systems and are actively investigating," provides meaningful value during the first hours

of response. It gives designated spokespersons something to work with immediately that aligns with

the organization’s needs and policies, and limits the negative impact of silence or unapproved

messaging that can occur when employees or the press fill the communication void with speculation.

CTI for Ransomware

Cyber threat intelligence helps organizations prepare for ransomware by identifying current threats,

understanding attacker tactics, and recognizing gaps in defensive visibility and capability. Effective CTI

enables proactive defense by surfacing information about how ransomware groups operate before they

target the organization.

CTI for ransomware preparation should prioritize the use of tactics, techniques, and procedures (TTPs) over

generic indicators of compromise (IOCs) for detection and threat hunting. Ransomware payloads are

frequently customized for each victim organization, with custom binaries containing hardcoded ransom

notes specific to the target. File hashes and other payload-specific IOCs have limited value for proactive

defense because the indicators change with each attack. This is exemplified in the LockBit RaaS operation

discussed earlier, where each affiliate-generated build produced unique binaries for each victim, as shown

in Listing 140. TTPs, by contrast, remain more consistent across campaigns and provide durable foundations

for detection and hunting.

Listing 140 | LockBit RaaS Database Victim Build Statistics

mysql> SELECT DATABASE();

+--------------+

| DATABASE()   |

+--------------+

| paneldb_dump |

+--------------+

1 row in set (0.00 sec)

mysql> SELECT COUNT(*) AS "Total Builds", COUNT(DISTINCT company_website) AS "Unique Orgs" FROM

builds;

+--------------+-------------+

| Total Builds | Unique Orgs |

+--------------+-------------+

|         1183 |         631 |

+--------------+-------------+

Incident Response for Ransomware | Chapter 17 | 531

1 row in set (0.01 sec)

Consider a common tactic: ransomware groups consistently target backup-deletion mechanisms in their

campaigns to eliminate recovery options, using tools like vssadmin, wbadmin, and bcdedit. Building detection

capabilities around the unexpected execution of these commands is more valuable than tracking specific

malware hashes that change with each attack tool build.

Ransomware payloads are customized for each victim, making file hashes and other

payload-specific IOCs short-lived. Focus detection engineering on attacker behaviors and

techniques that remain consistent across campaigns.

Important CTI sources for ransomware intelligence include:

• Government advisories from CISA, FBI, and international partners that provide detailed technical

analysis of active ransomware groups.

• Industry-specific ISACs that share threat information relevant to particular sectors.

• Commercial threat intelligence feeds that track ransomware group activity, infrastructure, and evolving

techniques.

• Open-source intelligence from security researchers, vendor blogs, and community threat tracking

projects.

Ransomware operators rapidly adapt their tactics in response to defensive improvements. Where

conventional IOCs remain valuable for broad threat awareness, TTP-focused CTI provides more actionable

insights for ransomware defenses.

Employee Training and Awareness

Employee training is a critical defense against social engineering and phishing attacks that often initiate

ransomware campaigns. Most ransomware infections begin with human interaction, whether clicking a

malicious link, opening a malicious attachment, or responding to a convincing impersonation attempt.

Effective training helps employees recognize important indicators of phishing attempts:

• Urgent or emotionally manipulative language designed to bypass careful consideration.

• Claims of dire consequences for not responding immediately.

• Requests for personal information, credentials, or financial data.

• Untrusted or shortened URLs that obscure the actual destination.

• Slight misspellings in email addresses or domain names (e.g., "amazan.com" instead of "amazon.com").

• Unexpected communications that do not align with normal business processes.

AI-generated content has improved the quality of phishing campaigns, making grammatical and stylistic

errors less reliable as indicators. Attackers without native-language skills or cultural knowledge can now

generate convincing messages that would previously have contained obvious tells. Training should

emphasize verification procedures and reporting mechanisms rather than relying solely on employees to

identify sophisticated deception.

Help desk impersonation has emerged as a particularly effective social engineering technique. Employees

should understand organizational policies regarding remote support sessions, particularly whether help

desk staff will ever request the installation of remote access tools or ask for credentials. Organizations

should clearly communicate that legitimate support staff will not request password disclosure or installation

of unfamiliar software.

Training programs should emphasize regular, ongoing engagement rather than annual compliance

exercises. Training programs are not effective when they are not engaging or when employees view them as

formalities that they click through as quickly as possible. Simulated phishing campaigns should test

recognition and reporting behavior to obtain data on resilience to these attacks and practices to follow

organizational policies.

Metrics that track reporting rates, click rates, and time-to-report help security teams identify which

departments or roles need additional attention. Clear reporting mechanisms that employees understand are

valuable when they encourage prompt escalation of suspicious activity. Feedback loops that inform

employees about the outcomes of their reports reinforce vigilance and build a security-conscious culture.

When employees report suspicious emails or activity, respond promptly with

acknowledgment and next steps. Users who report potential threats should feel that their

actions are valued and lead to meaningful outcomes. When reported incidents are not

followed up on, users often become discouraged from reporting in the future.

Identity, Access, and Tier-0 Protection

Ransomware operators rarely begin by deploying an encryptor on a random workstation. In modern

campaigns, threat actors attempt to take control of the organization’s identity and administration layer so

they can push ransomware everywhere, destroy recovery options, and resist containment efforts. Domain

controllers, identity providers (IdPs), remote management platforms, virtualization consoles, and backup

servers become the distribution vehicles for broad ransomware deployment.

Preparing for ransomware requires treating these components as tier-0 assets and defending them

accordingly. The goal is to make it significantly harder for attackers to obtain persistent, global

administrative control, and to ensure that the organization can still operate if its primary identity systems

are disrupted or untrusted.

Domain controllers, identity providers, backup servers, and virtualization platforms are the

systems attackers use to push ransomware everywhere at once. Protecting these tier-0

assets limits the attacker’s ability to achieve widespread encryption with greater ease.

Important preparations include:

• Hardening domain controllers, IdPs, and key admin platforms such as remote management tools,

virtualization platforms, and backup servers. These systems should have minimal internet exposure,

tight network segmentation, and aggressive patching practices.

• Separating administrative roles and credentials so that no single account has broad, standing privileges

across the entire organization. Use distinct admin accounts for different roles, avoid shared domain

admin accounts, and implement just-in-time privilege elevation where possible.

• Implementing strong MFA for all privileged and remote access, with preference for phishing-resistant

methods for high-value accounts.

Incident Response for Ransomware | Chapter 17 | 533

• Monitoring for identity and privilege anomalies as early-warning indicators of compromise, including

unexpected changes to admin group membership, new high-privilege accounts, unusual logon patterns,

and modifications to IdP or federation configurations.

• Maintaining documented and tested break-glass accounts and procedures that remain usable if your

Single Sign-On (SSO)/IdP or primary directory is unavailable or cannot be trusted. These break-glass

options should use separate credentials, be stored and accessed under strong control, and be exercised

during tabletop exercises and technical tests.

When identity, access, and tier-0 systems are well protected, ransomware operators must work much

harder to reach the point where they can deploy encryptors broadly. Strong identity hygiene also improves

detection and scoping (through better visibility into privileged changes) and gives the organization more

options during containment and recovery.

Backups

Backups serve as the primary recovery mechanism for ransomware incidents, yet many organizations

discover during an attack that their backups cannot fulfill that role. Modern ransomware campaigns

explicitly target backup infrastructure, hypervisors, and storage snapshots before deploying encryption,

recognizing that eliminating recovery options increases the likelihood of ransom payment.

THE CRUSHING DISAPPOINTMENT OF ENCRYPTED BACKUPS

Few moments in ransomware response are more demoralizing than discovering that the backups an

organization invested in and relied upon are also encrypted, deleted, or otherwise unusable.

This discovery typically occurs during the frantic early hours of response. Leadership asks the

obvious question: "Can we restore from backups?" IT staff access the backup console, only to find

ransom notes in the backup repository, or discover that the backup server itself is encrypted, or

realize that the most recent clean backup is months old because attackers deleted all accessible

backups before encryption began.

The emotional impact is significant. Staff who assured leadership that "we have good backups" must

now explain why those backups cannot deliver. The organization’s primary recovery path has

evaporated, and the remaining options are all significantly worse: paying the ransom, rebuilding from

scratch, or recovering from inadequate backups.

This scenario is painfully common. Modern ransomware operators specifically target backup

infrastructure because they understand its importance. Attackers with privileged access credentials

can often access backup systems, delete or encrypt backup data, and disable backup jobs without

triggering alerts. Organizations that treat backup systems as IT infrastructure rather than as critical

security assets find themselves without recovery options.

The solution is not simply "better backups." The solution is a backup architecture designed under the

assumption that attackers will have privileged network access. Immutable storage, air-gapped copies,

separate authentication for backup administration, and backup integrity monitoring all address the

reality that attackers specifically target backup systems.

Organizations should validate backup resilience through tabletop exercises that include the scenario:

"The attacker has domain admin credentials. Can they destroy our backups?" If the honest answer is

yes, backup architecture requires investment before an incident forces that discovery under worse

circumstances.

Ransomware-Resistant Backup Strategies

Effective backup strategies for ransomware resilience assume that attackers will have privileged access to

the production environment. The question is not whether backups exist, but whether those backups can

survive an attacker with domain administrator or other privileged credentials.

Start with the direction of data flow. Pull-based backup architectures, where backup systems retrieve data

from production, are more resilient than push-based models. When production systems push to backup

storage, a compromised system can overwrite or delete existing backups. Pull-based systems initiate

connections from the backup infrastructure, limiting what compromised production systems can reach.

Network isolation reinforces this protection. Backup infrastructure should be accessible only through

dedicated management networks or specialized agents, not directly reachable from potentially

compromised production systems. Attackers who compromise a workstation or even a domain controller

should not have a network path to backup storage.

Immutability provides protection even when attackers reach backup systems.  Write-once-read-many

(WORM) configurations and immutability guarantees prevent modification or deletion regardless of

credential compromise. An attacker who gains access to the backup console cannot delete immutable

backups before the retention period expires. Storage-layer snapshots maintained with retention policies

separate from backup software provide additional recovery points that application-level attacks cannot

reach. Snapshot-based backup approaches also support rapid restoration by accommodating faster

recovery of virtual machines or volumes, though their storage capacity requirements make them more

costly than traditional backup methods.

Air-gapped or offline copies represent the strongest protection. At least one backup copy should be

physically disconnected from networks, eliminating any possibility of remote compromise. Removable

storage libraries or systems that are powered off except during scheduled backup windows provide this

protection.

Identity separation can also limit the blast radius of credential compromise. Backup system access managed

through credentials separate from production IdP means that domain administrator credentials alone

cannot reach backup infrastructure data. Separate identity providers, dedicated local accounts, or third-

party authentication systems create this separation.

If domain administrator credentials can access backup systems, attackers with those

credentials can destroy backups before encrypting production systems. Separate backup

authentication from production identity providers to limit the access opportunity from a

compromised domain administrator account.

Hypervisor-level protection adds another layer for virtualized environments. VM snapshots and replication

managed at the hypervisor layer with separate administrative access survive attacks that compromise guest

operating systems. Some backup platforms also support replica-from-backup capabilities, where virtual

machine replicas are created directly from backup data rather than from running source systems. [3]

This

approach allows organizations to spin up critical workloads from backup data when source systems are

unavailable or untrusted, accelerating recovery of priority systems while the primary environment is being

rebuilt. Cross-cloud storage with external identity extends these protections to cloud environments,

Incident Response for Ransomware | Chapter 17 | 535

preventing compromised on-premises credentials from reaching off-site backups authenticated through

separate identity providers.

Not all systems are equally important, and backup strategies should reflect that. Prioritizing backup

coverage and restoration testing for mission-critical systems ensures the most important workloads have

verified recovery paths before less critical systems are addressed. Attempting to restore everything

simultaneously during ransomware recovery is rarely feasible and often counterproductive. Identifying the

priority order for system recovery in advance allows teams to focus their efforts on the areas with the

highest business impact.

The 3-2-1-1-0 Backup Rule

The traditional 3-2-1 backup rule has served as a baseline for data protection, but comprehensive

preparation to defend against ransomware threats often requires an expanded strategy. The 3-2-1-1-0 rule

extends the original framework with two additions that directly address modern attack patterns: [4]

• 3 copies of data (production plus two backups).

• 2 different media types (preventing single-technology failures).

• 1 off-site copy (protecting against physical or logical site-wide events).

• 1 immutable or air-gapped copy that cannot be modified or deleted regardless of credential

compromise.

• 0 errors in backup recovery verification, confirmed through automated or scheduled restoration

testing.

The first addition, an immutable or air-gapped copy, addresses the threat that ransomware operators

specifically target backup infrastructure with compromised credentials. A backup that cannot be altered or

destroyed through network access or administrative privilege provides a recovery path that survives even a

complete domain compromise.

The second addition, zero recovery errors, shifts backup validation from assumption to verification.

Ransomware incidents compress decision timelines, and discovering that backups do not restore properly

during an active attack eliminates the primary recovery option at the worst possible moment.  Organizations

should regularly test restoration procedures, measure actual recovery times against Recovery Time

Objectives (RTO), and verify data completeness against Recovery Point Objectives (RPO). Automated

recovery verification tools can perform these checks on a scheduled basis, confirming that backups are

complete and restorable before an incident forces the question.

Ransomware recovery timelines are often significantly longer than organizations expect.

Unlike a single-system failure, ransomware can encrypt hundreds of systems

simultaneously, creating a restoration scope that can take days or weeks to work through,

even with clean backups available. Extended recovery times increase organizational

pressure to pay ransom, which is exactly why attackers target backup infrastructure in the

first place. Organizations should measure actual restoration times during testing and use

those measurements, not theoretical estimates, when setting recovery expectations with

stakeholders.

Backups Are Your Last Line of Defense

Finally, it’s important to recognize that backups function as insurance rather than prevention. Organizations

cannot rely on backup-based recovery as their primary ransomware strategy. Defense-in-depth, early

detection, and effective response remain essential even with robust backup capabilities.

VERIFY/TRIAGE

General guidance on verification and triage activities is covered in Verify and Triage Activities . This section

addresses ransomware-specific considerations for verification and triage.

In this section, we’ll examine the indicators that confirm ransomware activity, distinguish encryption-based

attacks from data theft and pure extortion, communicate uncertainty effectively to decision-makers, and

plan resources for the extended response that ransomware incidents typically require.

Ransomware Verification Indicators

Ransomware verification often occurs under compressed timelines because encryption spreads rapidly, and

additional delay can increase the impact on the organization. Unlike verification for other incident types

where analysts can take time to gather context, ransomware verification frequently happens while the

attack is still active.

Start by identifying the specific indicators that distinguish ransomware from other threats. Encrypted files

with modified extensions, ransom notes appearing across file systems, and mass file modification events in

rapid succession all point toward ransomware rather than data theft or espionage. System logs showing

widespread service disruptions, failed backup operations, or unexpected shadow copy deletions on

Windows systems further support the classification of ransomware.

Analysts should aim for early identification of the ransomware family during verification. Ransom notes

often contain identifying information, including group names, contact addresses, and payment portal URLs.

Services such as ID Ransomware allow analysts to upload ransom notes or encrypted file samples to identify

the ransomware variant. Early family identification allows responders to research known decryption

options, understand typical attacker behavior patterns, and anticipate what evidence sources may be

available.

PROTECT VICTIM IDENTIFIERS IN RANSOM NOTES

Ransom notes may include a unique victim identifier that grants access to a chat portal where the

ransomware group communicates with the victim, as shown in the example in Figure 183 . Anyone

who possesses this identifier can log in to the negotiation portal, and ransomware groups generally

cannot distinguish the victim organization from a third party using the same credentials. [5]

When employees photograph ransom notes on their screens and share them on social media, or when

responders include unsanitized ransom notes in incident reports distributed beyond the response

team, that victim identifier becomes accessible to journalists, security researchers, law enforcement,

and other threat actors. Third parties who access the negotiation portal can disrupt active

negotiations by sending messages, revealing the victim’s willingness to pay (or not pay), or provoking

the ransomware group into retaliatory action.

Incident Response for Ransomware | Chapter 17 | 537

Figure 183 | Ransom Note with Victim Identifier

The Conti ransomware group made this risk explicit in 2021 when they announced that any victim

whose negotiation details leaked to journalists would have their stolen data published immediately,

regardless of whether negotiations were in progress. After screenshots from the JVCKenwood

negotiation appeared in media reports, Conti terminated the negotiation and disclosed the stolen

data to the public. [6]

Other groups have adopted similar policies, treating leaked negotiation details as

grounds for ending discussions and accelerating data publication.

Organizations should establish clear guidance during incident response: ransom notes and

negotiation details should be treated as confidential and shared only with authorized members of the

response team, legal counsel, and law enforcement. Employees who encounter ransom notes on their

systems should be instructed to report internally through established channels and avoid

photographing, forwarding, or posting ransom note content. Screenshots shared for investigative

purposes should have victim identifiers, chat URLs, and file paths redacted before distribution.

Treat ransom notes as confidential. Victim identifiers in ransom notes grant access to

negotiation portals, and leaked identifiers have caused ransomware groups to terminate

negotiations and immediately publish stolen data.

Distinguishing Attack Types

Not every ransomware incident involves data exfiltration. The 2025 Verizon Data Breach Investigations

Report found ransomware in 44% of all breaches reviewed, up from 32% the prior year, with that combined

figure encompassing both traditional encryption-based ransomware and pure extortion attacks in which

adversaries steal data without encrypting systems. [7]

The 2024 report separated these categories, finding

that pure extortion accounted for 9% of all breaches compared to 23% for encryption-based ransomware.

[8]

Data theft as an additional extortion lever traces back to around 2019, when the Maze ransomware group

pioneered the technique to retain leverage even when victims could restore from backups. [9]

During verification, look for indicators that help distinguish between attack types, as summarized in Table

51. This early classification shapes how the organization communicates with stakeholders and allocates

response resources.

Table 51 | Attack Type Indicators

ATTACK TYPE INDICATORS

Encryption-only • Rapid, widespread file modification

• Minimal prior attacker activity in logs

Data theft with

encryption

• Extended attacker dwell time

• Large outbound data transfers

• Staging activity before encryption

Extortion without

encryption

• Threatening communications referencing stolen data

• No corresponding file encryption

Communicating with Decision Makers

An effective ransomware response requires managing the tension between executive information needs and

investigation timelines rather than resolving it. Analysts should explicitly communicate uncertainty,

distinguishing between what is known, what is suspected, and what remains under investigation.

For example, a statement that positions known and suspected information, along with next steps, provides

leadership with the insight needed for decision-making.

“Based on current evidence, we believe the attacker accessed the file server containing customer data. We

have not yet determined what specific files were accessed or whether data was exfiltrated. We expect to

have better visibility on data access within twelve hours.

Regular briefings (every few hours early in the incident, then daily) help leadership stay informed without

the constant interruption of technical work. Consistent communication formats that show progress without

overpromising build credibility over time. Analysts should also help leadership understand that some

questions may never be definitively answered, and that reasonable assessments based on available evidence

are sometimes the best possible answers.

Incident Response for Ransomware | Chapter 17 | 539

THE INCIDENT COMMANDER ROLE IN RANSOMWARE RESPONSE

Ransomware incidents generate a sustained volume of questions from executives, legal counsel,

insurers, and external parties that can overwhelm a response team if every analyst is fielding requests

for updates.  Designating an Incident Commander (IC) as the single point of contact between the

response team and organizational leadership protects analysts from constant interruptions while

ensuring decision makers receive timely, consistent information.

The IC does not need to be the most technical person on the team. The role requires someone who

can absorb technical findings from analysts and forensic investigators, translate them into business-

relevant language, and communicate clearly with executives who need to make decisions on

containment, notification, legal exposure, and resource allocation. The IC bridges two audiences that

often communicate differently: analysts focused on artifacts, timelines, and indicators, and leadership

focused on business impact, liability, and recovery timelines.

Effective ICs combine communication skills with enough technical literacy to understand what

analysts are reporting and enough organizational awareness to anticipate what leadership will ask

next. They should be comfortable delivering difficult messages, including "we don’t know yet" and

"the timeline has changed," without losing credibility with either audience. Organizations should

identify and prepare IC candidates before an incident occurs, and exercise them in this role during

tabletop exercises so they are ready when a real incident demands it.

Resource Planning for Extended Response

Resource allocation during triage should account for the extended duration typical of ransomware

incidents. Response efforts may continue for weeks or months through investigation, containment,

eradication, and recovery. Early engagement of external resources, including forensics firms, legal counsel,

and communications specialists, helps ensure adequate capacity for the sustained effort ahead.

When presenting the incident to decision makers for resource allocation, include realistic estimates of

response duration and the specialized skills required. Ransomware response often requires expertise in

negotiation, regulatory compliance, and crisis communications that may not exist within the internal

incident response team.

SCOPE

Ransomware scoping should be more thorough than scoping for many other incident types. While advanced

threat actors may focus narrowly on specific data or systems, ransomware attackers typically survey the

environment broadly and access whatever is immediately available. This difference means scoping must

extend across the entire environment rather than following a narrow path from initial access to a specific

target.

The biggest scoping failure in ransomware response is failing to perform it thoroughly. Organizations that

limit their scope to systems already known to be encrypted often discover during recovery that attackers

had accessed additional systems, established persistence mechanisms, or exfiltrated data from locations not

initially considered.

Failure to adequately scope ransomware incidents results in incomplete containment,

missed data exposures, and prolonged recovery times. Responders should invest the

necessary time and resources to perform comprehensive scoping throughout the response

action loop.

Framework for Ransomware Scoping

Effective ransomware scoping requires systematic data gathering across multiple categories. The

framework checklist in Table 52  provides guidance to help responders ensure comprehensive scoping

coverage.

Table 52 | Ransomware Scoping Checklist

CATEGORY KEY QUESTIONS AND DATA POINTS

Incident Overview How was the incident identified? Which hosts are known to be impacted? What

actions have already been taken? What are the organization’s expectations for

response? What would be considered the organization’s most sensitive

information assets? Do backups exist and are they unencrypted? Do current

network diagrams exist?

Host Inventory How many Windows, Linux, macOS, and ESXi hosts exist in the environment?

Which systems are domain-joined? What virtualization platforms are in use?

Where are backup servers located?

Host Data Sources What Windows Event Logs are available and at what retention? What Linux audit

or syslog data exists? What application-specific logs are available? Is Endpoint

Detection and Response (EDR) telemetry available?

Network Data

Sources

What firewall logs are available? What VPN authentication logs exist? Is NetFlow

data collected? Is there a Network Detection and Response (NDR) solution in

place?

Security Systems Is a Security Information and Event Management (SIEM) system deployed and

what data does it contain? What EDR coverage exists? What endpoint protection

or antivirus data is available? Are there cloud security logs (Microsoft Entra ID,

AWS CloudTrail)?

Cloud Logging What cloud platforms are in use (AWS, Azure, GCP)? What logging and

monitoring services are enabled (CloudTrail, Azure Monitor, etc.)? What is the

retention period for cloud logs? What logging resources are available for

Software as a Service (SaaS) applications (e.g., Microsoft 365 audit logs, Google

Workspace logs)?

This scoping data serves multiple purposes: understanding the environment where the attack occurred,

identifying available evidence sources, and planning collection and analysis activities. Internal teams may

already know many of these answers, but external responders or consultants should systematically gather

this information before proceeding.

Scoping Activities for Ransomware

Ransomware scoping activities focus on understanding the full extent of attacker activity across the

environment. Start by identifying all affected systems, looking beyond those showing obvious encryption to

Incident Response for Ransomware | Chapter 17 | 541

every system the attacker accessed, authenticated against, or used for staging tools. This broader view

reveals the true scope of compromise rather than the visible symptoms of encryption.

Next, determine data exposure by examining which systems containing sensitive data the attacker accessed.

File servers, databases, document repositories, and backup systems all warrant scrutiny. Understanding

data exposure informs breach notification decisions and helps leadership assess regulatory and reputational

risk.

Map the attacker’s lateral movement path from initial access through to the systems ultimately encrypted.

This reconstruction reveals how attackers navigated the environment and which credentials or

vulnerabilities they exploited along the way. Similarly, identify any persistence mechanisms the attacker

established, including backdoors, scheduled tasks, registry modifications, or unauthorized accounts that

could enable re-entry after recovery.

Finally, establish a comprehensive timeline of the attacker’s activity. Determine when initial access occurred

and how long the attacker was present before deploying encryption. This dwell-time measurement helps

identify the window during which data exfiltration may have occurred and informs decisions about which

backup restore points are most likely trustworthy.

ERADICATE

Eradication in ransomware incidents involves two parallel objectives: understanding what data attackers

accessed, and removing all attacker presence from the environment. Both objectives need to be completed

thoroughly before recovery can proceed safely.

In this section, we’ll assess what data attackers accessed and exfiltrated, work through investigative

techniques and detection strategies for hunting exfiltration evidence, and evaluate whether decryption

options exist that may eliminate the need for backup restoration or ransom payment.

Assessing Data Access and Exfiltration

Understanding what data attackers accessed is critical for regulatory compliance, notification decisions,

and business risk assessment. In double-extortion scenarios, this assessment determines the organization’s

exposure even if the encryption is resolved.

Data access assessment begins with identifying which systems attackers touched:

• Authentication, Authorization, and Accounting (AAA) records: Where did compromised accounts

authenticate? Each successful authentication represents a system that the attacker could access.

• File access telemetry: What files were opened, copied, or modified on accessed systems?

• Network share access: Which file servers and shared drives did the attacker browse or access?

• Database access: Did attackers connect to databases containing sensitive information?

Software inventory and data classification become valuable during this assessment. Understanding what

data types reside on each system helps translate "the attacker accessed the backup server" into "the

attacker potentially accessed customer personally identifiable information (PII) and financial records stored

on that system."

Investigative Techniques for Data Exfiltration Hunting

Ransomware attackers commonly stage data before exfiltration using archival tools and temporary storage

locations. Investigators should hunt for evidence of these staging activities, summarized in Table 53.

Table 53 | Exfiltration Hunting Techniques

TECHNIQUE WHAT TO LOOK FOR

Archival artifacts Tools like WinRAR, 7-Zip, and native Windows compression utilities leave

forensic traces:

• WinRAR archive history: NTUSER.DAT\Software\WinRAR\ArcHistory

• 7-Zip history: NTUSER.DAT\Software\7-Zip\

• Password-protected archives chunked into 1-2GB segments

Staging locations Attackers stage data in predictable locations:

• C:\Users\Public

• C:\Perflogs

• %TEMP%

• Hidden shares and publicly accessible folders

Exfiltration tools Hunt for file transfer utilities, including:

• Archiving tools (WinRAR, 7-Zip)

• File transfer clients (FileZilla, WinSCP, rclone)

• Cloud storage clients (Mega sync client, Dropbox)

• Command-line utilities (cURL, Wget, FTP)

Deleted artifacts Attackers often delete staging archives after exfiltration:

• NTFS Update Sequence Number Journal ( $UsnJrnl) analysis reveals file

creation and deletion

• File system timeline analysis reveals deleted archive evidence

Systematic hunting across these artifact categories helps investigators reconstruct the data exfiltration

timeline and estimate what information left the environment, even when attackers attempted to cover their

tracks.

Data Exfiltration Detection Strategies

When the specific data accessed is unknown, detection focuses on identifying anomalous data movement.

Start by examining network telemetry for large outbound data transfers to external IP addresses,

particularly transfers destined for hosting providers or known file-sharing services. Use network monitoring

tools to identify spikes in data volume to narrow down investigation windows, as shown in the examples in

Figure 184 . File system analysis should look for the creation of large archive files, especially in unusual

locations where archives would not normally appear.

Incident Response for Ransomware | Chapter 17 | 543

Figure 184 | Cacti Network Monitoring Reveals Egress Data Transfer Spikes

User and Entity Behavior Analytics (UEBA), often supported with AI-based technology platforms, provides

additional detection opportunities. Execution of archival tools by unexpected accounts or on systems where

such activity is abnormal warrants investigation. Similarly, network connections to cloud storage services

from systems that do not normally use such services may indicate unauthorized data staging or exfiltration.

Decryption Possibilities

Before committing to backup restoration or considering a ransom payment, responders should investigate

whether free decryption options are available. Law enforcement operations, security researchers' efforts,

and implementation flaws in ransomware encryption have led to decryption tools for numerous

ransomware families.

Some circumstances allow organizations to perform decryption without payment:

• Implementation vulnerabilities: Although less common today, some ransomware families have included

cryptographic implementation flaws that allow researchers to recover encryption keys or decrypt files

directly. These vulnerabilities are uncommon in modern, well-maintained ransomware operations, but

older or less sophisticated variants may contain exploitable weaknesses.

• Law enforcement operations: Coordinated efforts have led to the seizure of ransomware infrastructure,

including decryption keys. Operations against groups such as Hive, ALPHV/BlackCat, and LockBit have

yielded decryption capabilities that were subsequently made available to victims.

• Leaked keys: Internal conflicts within ransomware groups, disgruntled affiliates, or operational security

failures have occasionally resulted in decryption keys being leaked publicly.

• Security researcher efforts: Independent researchers and antivirus vendors analyze ransomware

samples and, when they identify weaknesses, sometimes develop decryption tools.

The No More Ransom Project  serves as the primary repository for free ransomware decryption tools. This

initiative, supported by Europol, law enforcement agencies, and security vendors, aggregates decryption

tools for over 150 ransomware families. Responders should check this resource early in the response

process.

Additional decryption resources include:

• Vendor-provided tools from security companies, including Kaspersky, Avast, Emsisoft, and Bitdefender.

• Decryption tools from law enforcement agencies (sometimes not publicly released but available through

direct contact).

• Security researcher publications and tool releases.

• Commercial decryption services, including Unidecrypt from Coveware.

Responders should maintain realistic expectations about the likelihood of decryption. Most modern

ransomware uses properly implemented encryption without known vulnerabilities. Decryption without

obtaining the attacker’s keys is typically not feasible for current, actively maintained ransomware families.

Even when decryption tools exist, they may have limitations:

• Tools may only work for specific ransomware versions or variants.

• Some encrypted files may not be recoverable even with the correct keys.

• Decryption processes can be slow and resource-intensive, particularly for large file volumes.

• Partial file corruption may occur even after successful decryption.

• Tools may not provide sufficient scalability to handle enterprise-scale recovery.

Given these constraints, responders should evaluate decryption possibilities early but continue pursuing

backup restoration and system rebuild options in parallel.

DECRYPTOR LIMITATIONS

Organizations should also set realistic expectations with stakeholders about recovery timelines. Even

after organizations pay the ransom and receive a functioning decryptor, recovery takes months, not

days. The 2021 Conti ransomware attack against Ireland’s Health Service Executive (HSE) illustrates

this reality: despite obtaining a decryptor, the organization took approximately four months to

restore critical healthcare services nationwide. [10]

Decryption alone does not restore operations. Systems need to be validated, rebuilt where necessary,

and reintegrated into the environment, all while maintaining security controls to prevent

recompromise. Communicating this reality early helps maintain stakeholder confidence throughout

the recovery process and reduces the pressure on response teams to meet unrealistic timelines.

Decryption Assessment Process

When investigating decryption options, follow a structured approach:

1. Identify the ransomware family: Analyze ransom notes, encrypted file extensions, and any available

Incident Response for Ransomware | Chapter 17 | 545

malware samples to accurately identify the ransomware variant. Misidentification leads to wasted effort

with incompatible tools.

2. Check available resources: Search the No More Ransom project, vendor tools, and recent security news

for decryption options matching the identified family.

3. Validate tool applicability: Confirm that available tools match the specific variant and version

encountered. Tools developed for older versions may not work on newer variants.

4. Test on sample files: Before committing to full-scale decryption, test tools on a subset of encrypted files

to verify they work correctly. Measure the time and resources required for decryption to inform

broader planning.

5. Plan decryption execution: If tools prove effective, plan the decryption process, including prioritizing of

critical files and validating recovered data.

6. Backup encrypted data: Before attempting decryption, create secure backups of the encrypted files to

prevent data loss if the tool fails or corruption occurs during decryption.

7. Execute decryption: Run the decryption process according to the plan, using dedicated systems with a

copy of the encrypted data, where possible, instead of live systems.

8. Validate and Monitor: Continue monitoring for any issues and validating recovered data as it becomes

available.

Decryption tools, when available, may represent the least costly recovery path. Even a few hours spent

investigating decryption options is worthwhile before committing to longer restoration or payment

alternatives.

RECOVER

Recovery is typically the longest and most resource-intensive phase of ransomware response. Organizations

often underestimate the time and effort required to restore operations, particularly when critical

infrastructure such as domain controllers, identity platforms, or backup systems has been compromised.

Too often, an organization will pay the ransom, obtain a decryptor, and expect to be back up and running

within hours or days. This is seldom the case, especially when the organization hasn’t prepared for recovery

in advance. In this section, we’ll cover key principles for ransomware recovery, including planning and

prioritization, restoring from backups, system rebuild, monitoring for an attacker’s return, and

communication during recovery.

Recovery Planning and Prioritization

Recovery planning prioritizes systems based on organizational criticality, with infrastructure dependencies

addressed before application services. As with any other major incident, critical systems receive priority,

but ransomware recovery requires particular attention to the order of operations, since foundational

services must be trustworthy before dependent systems can be restored.

Recovery prioritization considers several factors, including:

• Business criticality: Revenue-generating systems, patient care capabilities, and critical operations

platforms.

• Infrastructure dependencies: Identity services, DNS, and network infrastructure must be restored

before systems that depend on them.

• Data availability: Systems with verified clean backups versus those requiring rebuild.

• Regulatory requirements: Notification deadlines and compliance obligations that may drive timeline

constraints.

• Resource availability: Staff, hardware, software licenses, and vendor support capacity.

Coordinate recovery priorities with decision makers to align technical work with organizational needs.

Important questions include which systems are most critical for resuming organizational operations, what

operational workarounds can sustain the organization while recovery proceeds, and what resources can be

allocated to accelerate recovery of priority systems. Answering these questions early in the recovery

process helps align technical efforts with organizational priorities and sets realistic expectations for

stakeholders. Clear communication and priority setting help reduce frustration when recovery timelines

extend longer than hoped.

Restoration from Backups

As we saw in Section 17.2.5 , restoration is the primary recovery method when backups are available and

verified to be clean. However, restoration requires careful attention to avoid reintroducing attacker access

or compromised data.

Critical considerations for backup restoration:

• Identify clean restore points: The restore point must predate the attacker’s compromise, not the

encryption event itself. A threat actor (such as an IAB) may have been present collecting information

about the organization’s systems for weeks or months before selling access to a ransomware threat

actor.

• Verify backup infrastructure: Confirm that backup servers, storage systems, and control planes were not

compromised or manipulated by attackers.

• Validate backup integrity: Test restoration on isolated test systems before deploying to production.

• Understand data loss: Accept that data created between the last clean backup and the encryption event

may be unrecoverable.

Challenges with backup restoration include determining the correct restore point when attacker dwell time

is uncertain, accepting potentially significant data loss when restoring from older backups, and the time

required to restore large systems and datasets.

System Rebuild

For critical infrastructure, particularly Active Directory domain controllers, system rebuild is often

preferable to restoration. Compromised domain controllers pose unique risks because attackers can embed

their persistence deeply within Active Directory (AD) objects, Group Policy, and trust relationships.

Restoring a compromised DC may reintroduce attacker access that is extremely difficult to detect or

remove.

Recovering a compromised Active Directory environment when an attacker has had

domain admin access is complex and risky. Organizations should carefully consider the

perceived cost-benefits of restoration against the long-term security risks of incomplete

eradication of attackers.

Rebuild is recommended when:

• Domain controllers or other identity infrastructure were compromised.

• Backup integrity is uncertain, or backups may contain attacker persistence.

Incident Response for Ransomware | Chapter 17 | 547

• Systems are significantly outdated, and recovery offers an opportunity to modernize.

• The time to validate backup cleanliness exceeds the time to rebuild.

A critical principle for recovery: do not decrypt and reuse encrypted data without validation . Victims

sometimes assume that paying ransom and decrypting systems returns them to a clean state. This

assumption is dangerous. Decrypted systems retain whatever attacker tools, persistence mechanisms, and

compromised configurations existed before encryption. Decryption restores data accessibility but does not

remove the attacker’s presence.

Decrypting a system restores data accessibility but does not remove attacker tools,

backdoors, or compromised configurations. Treat decrypted systems as compromised and

validate or rebuild them before returning to production.

Watching for Attacker Return

Ransomware victims face an elevated risk of re-attack, particularly if they paid the ransom. Payment

establishes the organization as willing to pay, making it an attractive target for secondary ransom or

extortion attacks from the same group or others who purchase victim lists.

Organizations should maintain heightened monitoring during and after recovery:

• Enhanced detection rules based on TTPs observed during the incident.

• Increased scrutiny of authentication activity, particularly for privileged accounts.

• Network monitoring for command-and-control (C2) patterns similar to those used in the initial attack.

• Regular hunting for indicators associated with the ransomware group that attacked the organization.

Re-ransoming attacks on victims who did not thoroughly eradicate the attacker’s access or address the root

causes represent a common pattern. Recovery is not complete when systems are restored; it is complete

when the organization has confidence that attacker access has been eliminated and the vulnerabilities that

enabled the attack have been remediated.

Paying ransom establishes the organization as willing to pay, making it an attractive target

for repeat attacks. Recovery is not complete until attacker access is eliminated and the

vulnerabilities that enabled the attack are remediated.

Communication During Recovery

Ransomware recovery often extends for weeks or months, requiring sustained communication with multiple

stakeholder groups. Unlike shorter incidents where a single status update may be all that is needed,

ransomware response often requires ongoing communication management throughout an extended

recovery period.

In Section 10.3.6 , we covered broad stakeholder communication guidance. This section

addresses ransomware-specific communication considerations.

Internal Communication Efforts

Recovery progress updates keep leadership informed and help manage organizational expectations.

Establish a regular cadence for internal updates, adjusting frequency based on recovery phase and

stakeholder needs.

Leadership Updates

Executive leadership needs visibility into recovery progress, resource requirements, and timeline estimates.

These updates should focus on business impact, risk posture, and the decisions required, rather than on

technical details. Regular briefings (daily during active recovery, then transitioning to weekly) maintain

leadership engagement without overwhelming executives with operational minutiae.

User Communication

Affected users need clear information about service availability, workarounds, and expected restoration

timelines. Be honest about timeline uncertainty rather than providing optimistic estimates that will be

missed. Users can adapt to known constraints more easily than they can to repeated delays in optimistic

projections.

Recovery Team

Multiple teams typically participate in ransomware recovery, including infrastructure, applications, security,

and business units. Regular coordination meetings ensure teams remain aligned on priorities and

dependencies. Document decisions and assignments to prevent confusion during extended operations.

External Communication Efforts

External communication during ransomware incidents requires coordination between technical teams, legal

counsel, communications staff, and executive leadership.

Regulatory Notifications

Ransomware incidents involving data exposure may trigger notification requirements under HIPAA, state

breach notification laws, the GDPR, the Network and Information Security (NIS2) Directive, the Digital

Operational Resilience Act (DORA), the 8-K market transparency report, or industry-specific regulations.

Work with legal counsel to identify applicable requirements and manage notification timelines. Some

regulations impose specific deadlines that must be tracked regardless of recovery status.

Customer and Partner Notifications

Customers and business partners may need to be notified of service disruptions, data exposure, or changes

to business processes during recovery. Coordinate these communications with legal counsel and

communications staff to ensure consistent messaging.

Insurance Carrier Coordination

Contact the cyber insurance carrier as early as possible in the response, ideally before engaging third-party

forensics firms or making significant response decisions. Many cyber insurance policies include specific

requirements regarding which vendors may be used, how evidence should be handled, and which actions

require prior approval. Organizations that engage outside counsel, sign forensic investigation contracts, or

begin remediation work before notifying their carrier risk having those costs denied during the claims

process.

Law Enforcement Engagement

If law enforcement is involved, coordinate communications to avoid compromising any ongoing

investigation. Law enforcement may request that certain details not be disclosed publicly.

Incident Response for Ransomware | Chapter 17 | 549

DEBRIEF

Ransomware incidents generate critical lessons about technical defenses, response procedures, and

organizational resilience. The debrief phase is an opportunity to convert the stress and disruption of the

incident into improvements that reduce the likelihood and impact of future attacks.

The stakes of a thorough debrief are high: documented cases of victims being re-ransomed by the same or

similar threat actors demonstrate that organizations that fail to address root causes or thoroughly eradicate

attacker access face an elevated risk of repeat incidents. Organizations that treat ransomware as a one-time

crisis rather than a learning opportunity may find themselves responding to the same attackers again.

General debrief guidance, including facilitating After-Action Review (AAR) sessions, documentation

requirements, and implementation tracking, is covered in Debrief Activity . This section focuses on

ransomware-specific debrief considerations.

Ransomware-Specific Debrief Questions

Beyond the standard AAR questions covered in Conducting the After-Action Review , ransomware debriefs

should address considerations unique to this incident type:

Backup and recovery assessment: Did backups survive the attack? If not, what architectural changes would

have protected them? How did actual recovery time compare to RTO targets, and were those targets

realistic? Did the organization have to accept data loss, and if so, what would have prevented it?

Dwell time analysis : How long were attackers present before encryption? What detection opportunities

existed during that window? Could earlier detection have prevented encryption entirely, or at a minimum,

reduced its scope?

Data exfiltration determination : Was the organization able to determine what data was accessed or

exfiltrated? If not, what logging or monitoring gaps prevented that determination? How did uncertainty

about data exposure affect notification decisions and stakeholder communications?

Ransom decision evaluation  (if applicable): Did the organization’s ransom payment policy function as

intended? Were decision makers prepared with the information they needed? If payment was made, did

decryption work as expected? If payment was declined, was data publicly disclosed or sold on the dark web,

and how did that affect the organization?

Extortion response: If the incident involved multi-vector extortion beyond encryption, how effectively did

the organization respond to each pressure channel? Were legal, communications, and executive teams

prepared to coordinate on non-technical threats like leak site postings or customer harassment?

Identity and privilege exposure : What privileged accounts were compromised? Did the organization have

visibility into the full scope of credential exposure? Were break-glass procedures needed, and did they

function correctly?

These questions help to focus on ransomware-specific lessons that generic incident debriefs may overlook.

Ransomware-Specific Metrics

Tracking ransomware-specific metrics supports the organization’s own improvement efforts, but there is

significant value when these metrics are shared across organizations. When anonymized metrics are shared

through ISACs, industry reports, and community forums, they contribute to a collective understanding of

how ransomware attacks unfold and how effectively organizations are responding. Aggregated data on dwell

times, TTPs, backup survival rates, and recovery methods across many incidents gives the broader security

community the evidence needed to identify trends, calibrate defenses, and advocate for resources.

Organizations that contribute to this shared knowledge base help improve ransomware resilience across

their industry and beyond.

In addition to standard incident metrics examined in Chapter 4 (including Mean Time To Detect and Mean

Time To Respond), ransomware incidents warrant tracking several measurements unique to this attack

type. Table 54 lists several ransomware-specific metrics that organizations should consider tracking across

incidents to evaluate their preparedness and response effectiveness.

Consider these metrics as opportunities that may provide additional value to the

organization, rather than requirements that should be tracked for every incident.

Organizations should select the metrics that best align with their organizational priorities

and data availability, and focus on consistently tracking them across incidents to identify

trends and inform improvements.

Table 54 | Ransomware-Specific Metrics

METRIC DESCRIPTION VALUE

Attacker dwell

time

Time from initial access to encryption

deployment

Reveals the detection opportunity

window where earlier identification

could have prevented encryption

Backup survival

rate

Percentage of backup systems and data

that remained accessible and

uncompromised

Indicates whether backup architecture

can withstand privileged attacker

access

Data exfiltration

confidence

Whether the organization could

definitively determine what data was

accessed

(high/medium/low/unknown)

Reflects logging and monitoring

maturity and affects notification

decision confidence

Recovery

method

distribution

Percentage of systems restored from

backup versus rebuilt versus decrypted

Informs future preparation investments

and validates backup strategy

effectiveness

Encryption

spread rate

Systems encrypted per hour during

active encryption

Measures containment effectiveness

and helps calibrate automated response

thresholds

WHEN RECOVERY LESSONS STAY BEHIND CLOSED DOORS

In October 2019, the Russian cybercrime group known as WIZARD SPIDER deployed the Ryuk

ransomware against DCH Health System, disrupting services for three hospitals in Tuscaloosa

County, Alabama. [11]

The attack forced the hospitals to implement diversion protocols, turning away

all but the most critical patients for over a week while staff reverted to paper-based workflows for

patient care.

Incident Response for Ransomware | Chapter 17 | 551

DCH ultimately paid the ransom and obtained decryption keys, then began a staged recovery process:

decrypt, test, and bring systems back online one by one across thousands of devices. Diversion

protocols were lifted approximately ten days after the attack began, though restoration of non-

essential systems continued beyond that 10-day window.

Despite the scale of this incident, the public record contains almost no detail about how DCH

managed the operational recovery. Which clinical systems were restored first? What restoration

sequence worked, and what did not? What would DCH recommend to another hospital system facing

the same situation? Those operational details, the ones most valuable to the next hospital hit by

ransomware, were never shared publicly.

This is not a case that is unique to DCH. Across ransomware incidents, public reporting consistently

focuses on whether the ransom was paid and when services resumed. The operational recovery

details that would help other organizations, especially hospitals providing urgent patient care, are

almost entirely absent from the public record.

Every hospital that recovers from ransomware generates hard-won operational knowledge. When

that knowledge stays locked within the organization, the next hospital facing a ransomware attack

has to start from scratch. Sharing anonymized recovery metrics, including restoration sequences and

timelines, backup survival outcomes, and clinical workflow adaptations, would give the healthcare

sector a growing body of evidence to prepare against a threat that targets hospitals with increasing

frequency. While organizations understandably hesitate to share details about ransomware incidents,

the collective benefit of sharing operational recovery lessons is significant, especially in sectors

where ransomware directly impacts human lives.

These metrics help organizations evaluate ransomware-specific preparedness and identify where

investments would have the greatest impact on future incident outcomes. Tracking these measurements

across incidents reveals patterns that inform strategic decisions about detection capabilities, backup

architecture, and containment procedures. Organizations that experience multiple ransomware incidents

can use this data to validate whether improvements are delivering measurable results. Where possible,

organizations should also share anonymized metrics with ISACs, sector partners, and community threat-

sharing programs so that the broader security community can build on a larger dataset of real-world

ransomware outcomes.

FINAL CONSIDERATIONS

Ransomware incidents test every aspect of an organization’s incident response capabilities. Organizations

with strong technical defenses, well-practiced response teams, and resilient business processes fare best,

but even the most prepared organizations face significant challenges. In this final section, we’ll examine

several overarching considerations that apply across the ransomware response lifecycle.

The Human Element

Ransomware response is exhausting. Extended incidents spanning weeks or months create sustained

pressure on response teams, IT staff, and leadership. Organizations should plan for personnel rotation,

ensure adequate rest during extended operations, and provide support resources for staff experiencing

burnout or stress. The best technical response procedures fail when the people executing them are too

exhausted to function effectively. In ransomware incident response, the stakes are high, and mistakes are

costly; leadership can help reduce the likelihood of errors by prioritizing team well-being.

Just as we avoid single points of failure in high-value systems, we should avoid them in

our response teams. Cross-training all team roles helps the organization avoid gaps in

essential skills when key personnel are unavailable.

A HANGRY RESPONSE TEAM IS NOT AN EFFECTIVE RESPONSE TEAM

I have worked on ransomware incidents where leadership treated the response team as a resource to

be managed and others where leadership treated the team as people to be supported. The difference

in outcomes was significant.

When an organization is in crisis, the response team becomes the most important group in the

building. These are the people leadership is relying on to figure out what happened, stop the bleeding,

and get the organization back on its feet. They should be empowered accordingly. That means giving

them the autonomy to make technical decisions without bureaucratic delays, providing the tools and

access they need without making them justify every request through normal procurement channels,

and shielding them from the organizational politics that inevitably intensify during a crisis.

It also means something much simpler: feed them. This sounds trivial, and it is not. Response teams

working 14-hour days during a ransomware incident are not taking lunch breaks. They are not

running out to grab dinner. They are heads-down, working through problems under pressure, and

they will skip meals rather than step away from a critical analysis task. Fresh, hot food delivered to

the team, not yesterday’s cold pizza sitting in a conference room, is one of the easiest and most

effective ways leadership can demonstrate that the people doing the hardest work are valued. When

shifts change, the incoming team should find a meal waiting, not empty boxes from the previous shift.

Coffee, water, and snacks should be stocked and replenished without anyone on the response team

having to ask.

This is not about perks. It is about sustaining performance over days and weeks of high-intensity

work. A response team that feels supported by leadership will push through difficult stretches with

focus and commitment. A team that feels like an afterthought will burn out faster, make more

mistakes, and disengage at the moments when the organization needs them most.

Legal and Regulatory Complexity

Ransomware incidents increasingly intersect with complex legal and regulatory requirements. Data breach

notification laws, industry-specific regulations, contractual obligations, and the potential for sanctions

create a set of requirements that technical responders are not equipped to navigate on their own. Early

engagement of legal counsel, ideally counsel with specific experience in ransomware incidents, helps ensure

that response decisions do not create additional legal exposure.

AI as an Evolving Threat

Earlier sections of this chapter examined how AI is lowering the technical barrier for ransomware affiliates

and improving the quality of social engineering campaigns. Those developments represent the early stages

of a more fundamental shift in ransomware campaigns where AI is moving from an advisory role, where

attackers consult it for guidance, to an operational one, where AI systems actively execute phases of an

attack with minimal human direction.

Incident Response for Ransomware | Chapter 17 | 553

Where we once made assumptions about the relationship between attacker skill and attack capability, these

considerations are no longer accurate. Threat modeling in ransomware has relied on the idea that

technically complex campaigns require technically skilled operators. With AI coding agents, minimally

competent threat actors can access instant operational competence across reconnaissance, exploitation,

lateral movement, and data exfiltration, creating new risks for organizations to consider.

AI Across the Attack Lifecycle

Threat actors are integrating AI throughout ransomware and extortion operations, extending well beyond

social engineering assets to the full attack chain. AI coding agents are actively executing attack phases

rather than simply advising a human operator. Documented cases show AI conducting network scanning,

credential harvesting, lateral movement, and data exfiltration with minimal human oversight (see also

Autonomous Adversaries). [12]

The Anthropic November 2025 threat intelligence report documented a campaign in which AI performed an

estimated 80 to 90 percent of the operations, with human decision-making required only four to six times

per engagement. [13]

A single operator with AI assistance can match the output of a team, conducting

simultaneous operations against multiple organizations. Organizations should assume that even

unsophisticated actors can execute technically complex campaigns.

AI-Optimized Extortion

Extortion revenue depends on the victim’s willingness to pay, which depends on how damaging disclosure

would be and how credibly the attacker can demonstrate that damage. AI is automating both sides of this

equation: identifying the most sensitive stolen data and calibrating the extortion approach to maximize

payout.

After exfiltration, threat actors face a data analysis problem. Terabytes of stolen files need to be evaluated to

determine which creates the most leverage for extortion. Previously, this required manual review, which

limited both scale and speed. AI systems excel at systematically categorizing data by sensitivity, including

PII, financial records, healthcare data, trade secrets, and regulatory-sensitive documents. These systems

identify the content most likely to motivate payment. AI can also cross-reference stolen data against

regulatory frameworks to identify specific notification obligations, penalties, and reputational risks the

victim faces if data is disclosed. This turns raw, stolen data into actionable leverage for extortion.

Once sensitive data is identified, AI manages the extortion lifecycle from demand pricing through payment

collection. The Anthropic August 2025 threat intelligence report documents cases in which AI analyzed

victims' financials and generated "profit plans" with multiple monetization paths for each target: direct

organizational extortion, data sales to third parties, individual targeting of people whose data was

compromised, and regulatory threat leverage. [14]

Ransom demands in the documented case ranged from

$75,000 to $500,000, calibrated to each victim’s organizational size, industry, and regulatory exposure.

AI handles operational execution across concurrent campaigns as well, crafting psychologically targeted

communications with incremental penalty structures, generating victim-specific ransom notes with exact

financial figures and regulatory citations, and adapting strategy based on victim responses. A single actor

can manage customized extortion campaigns against many organizations simultaneously, where previously

this level of personalization required a dedicated team.

AI-Generated Ransomware Development

AI is democratizing the RaaS market by enabling actors without traditional development skills to create

functional ransomware with advanced capabilities. Documented cases describe actors who cannot

independently implement encryption algorithms or understand Windows system call (syscall) mechanics,

yet produce and sell functional ransomware packages priced between $400 and $1,200. [15]

These packages

include ChaCha20 encryption, EDR evasion techniques such as FreshyCalls and RecycledGate, and anti-

analysis capabilities.

AI allows attackers to iteratively refine their tooling through continued interaction with models, introducing

new features and capabilities over time. Ransomware tooling progresses from basic encryption to advanced

delivery and evasion as directed by the threat actor. As development barriers are eliminated, the RaaS

ecosystem expands, increasing both the volume and variety of ransomware families that organizations will

encounter.

Attribution complexity also increases as AI-generated code reflects patterns specific to the language model

(e.g., Claude Sonnet 4.6 vs. GPT-5.3-Codex) rather than distinctive human coding styles. This makes it

harder for analysts to link ransomware families to specific developers or groups based solely on code

characteristics.

Attribution is always challenging in ransomware, but AI-generated code adds new layers of

complexity.

AI for Defenders

The same AI capabilities that accelerate attackers can also accelerate defenders' actions. As we saw in

Chapter 16, AI can assist with preparation activities, accelerate the detection of IOCs, support containment

and evidence collection, and facilitate the generation of recovery actions. AI tools grounded in

organizational context, through playbooks supplied as skills or through Retrieval Augmented Generation

(RAG), can assist analysts with response guidance tailored to the organization’s specific practices,

procedures, and infrastructure.

The acceleration of ransomware capabilities through AI makes the preparation investments described

throughout this chapter more important, not less. Organizations that build strong foundational defenses,

including identity protection, backup resilience, and detection capabilities, create environments where AI-

enhanced attacks are harder to execute, regardless of the attacker’s tooling. Preparation remains the most

effective response to an evolving threat landscape.

Recovery Is Not the End

Technical recovery is an important milestone, but the impact on an organization following a ransomware

incident often extends well beyond system restoration. When systems come back online and business

operations resume, organizations often discover that the broader consequences continue across regulatory,

legal, financial, and reputational dimensions.

Regulatory and Legal Exposure

Breach notification obligations trigger timelines that continue regardless of recovery status. Regulatory

inquiries may extend for months as agencies evaluate the organization’s security practices and incident

handling. If litigation follows, discovery and depositions can span years. Organizations should expect

ongoing engagement with legal counsel well after technical teams have moved on to other priorities.

Incident Response for Ransomware | Chapter 17 | 555
