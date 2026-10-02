# Chapter 16-3: AI-Assisted Response: Safety Guardrails & Automation Efficacy Evaluation

> Modular Sub-Chapter | Source: DAIR-IR Framework

• Search authentication logs from the past 24 hours for any failed logins followed by successful logins from the same user.

• Check threat intelligence for any information about the domain login.c1ic.link

• Create a ticket for this incident and assign it to the on-duty analyst.

The model translates natural language intent into appropriate tool calls, retrieves results, and uses the model’s processing features to generate a coherent response.

Defensive Applications

MCP integration with AI models allows analysts to utilize powerful defensive capabilities that accelerate common incident response tasks.

Natural Language Threat Hunting

Analysts can describe what they are looking for in natural language, rather than learning and constructing complex query syntax. An MCP server connected to SIEM data and CTI services automatically translates queries like "Show me any systems that communicated with newly registered domains in the past week " into appropriate backend queries. This natural language interface lowers the barrier to threat hunting for analysts who understand threat-hunting techniques but lack platform-specific SIEM query-language expertise. Experienced analysts benefit as well by expressing complex hunt hypotheses without context- switching to query documentation. Natural language access to SIEM platform interrogation offers a strategic benefit beyond analyst productivity: by abstracting from query language complexity, organizations reduce dependence on proprietary SIEM interfaces and mitigate vendor lock-in that arises when institutional knowledge becomes tied to platform-specific syntax.

Automated Enrichment

When investigating an indicator, MCP-connected tools can automatically gather context from multiple sources. Threat intelligence reputation, historical sightings in organizational logs, related indicators, and asset information for affected systems can all be retrieved and integrated into the response to a single analyst question. This automated enrichment eliminates the manual process of checking each data source individually, copying relevant findings, and assembling them into a coherent picture.

Cross-Platform Correlation

MCP servers connecting different security tools can empower queries that span multiple platforms. Finding all alerts related to a specific IP address across EDR, firewall, and email security platforms often requires logging into each platform, running separate queries, and manually correlating results. MCP-enabled correlation performs these lookups automatically and presents unified results. This cross-platform visibility helps analysts identify the full scope of activity without platform-specific access barriers.

Incident Documentation

MCP connections to ticketing systems allow analysts to update incident records through conversation. Documentation can be maintained without context-switching to separate interfaces. As analysts discover new findings, they can instruct the AI to update the incident ticket with specific details, maintaining documentation currency throughout the investigation. This conversational documentation reduces the common problem of outdated tickets that do not reflect the current investigation status.

Security Considerations

MCP integration introduces significant security considerations that organizations should understand.

Prompt Injection

Prompt injection is an attack technique where an adversary manipulates the model to circumvent controls or produce unintended output. When AI systems integrate data from external sources (including MCP server output), the model processes this content alongside its instructions. AI models have difficulty

MCP SUPPLY CHAIN AND REGISTRY RISKS

MCP servers are often built by independent developers without established security standards. Users often install using the "pipe cURL to Bash" anti-pattern (the opposite of best practices), with no version pinning, signing, or package locking in the current specification. This creates a plugin-like ecosystem where unvetted code from GitHub repositories can gain access to sensitive data or local system capabilities.

Figure 168 | Box.com MCP Server Installation Anti-Pattern

MCP server ecosystems introduce familiar supply chain risks, including typosquatting, impersonation, malicious updates for formerly safe code, and account takeovers of legitimate developers. Further, many MCP clients allow tools to update and run automatically for a seamless user experience, but this implicitly trusts tool developers and the integrity of installation sources, creating ongoing exposure to supply chain compromise. Organizations adopting MCP should treat servers like packages with elevated privileges: audit before usage, apply least privilege to credentials, consider sandboxing servers with containerization and network egress controls, and maintain internal registries of vetted MCP servers to reduce exposure to unknown code.

MCP Integration for Threat Hunting

Despite MCP’s security concerns, many organizations are adopting this integration opportunity for AI models to utilize external applications, API servers, and data sources. One compelling use case is integrating log analysis platforms with MCP to enable natural-language threat-hunting queries. For example, in one collection of web server logs, a query to identify common web server attack patterns (shown in Listing 137) returns a set of log events that can be further scrutinized by the analyst for indicators of compromise, as shown in Figure 169. Writing this query requires knowledge of OpenSearch Lucene query syntax and an understanding of common web attack patterns. OpenSearch is an open-source fork of Elasticsearch and Kibana, created after Elastic changed its licensing model. While the platforms have diverged somewhat since the fork, OpenSearch retains much of the same query syntax and capabilities as Elasticsearch, enabling users to ingest, search, and analyze log data.

Listing 137 | OpenSearch Lucene Web Log Threat Hunting Query Example

(http.response.status_code:(400 OR 401 OR 403 OR 404 OR 500) AND -source.address:"127.0.0.1") OR url.original:(*..* OR *%2e%2e* OR *passwd* OR *wp-admin* OR *phpMyAdmin* OR *shell* OR *eval* OR *base64*) OR url.original:(*union* AND *select*) OR url.original:(*%27* AND *OR*) OR url.original:(*SLEEP* OR *BENCHMARK* OR *information_schema*) OR user_agent.original:(*nikto* OR *sqlmap* OR *nmap* OR *masscan* OR *zgrab* OR *gobuster* OR *dirbuster* OR *wfuzz* OR *nuclei*) OR tags:(potential_attack OR scanner)

Figure 169 | OpenSearch Lucene Web Log Threat Hunting Query Result

As an alternative, organizations can use the OpenSearch MCP server to integrate AI model capabilities with the OpenSearch cluster containing security logs. Using MCP, analysts can issue natural-language queries that the AI model automatically translates into OpenSearch queries. “Review the Apache logging data for the last two weeks. Provide insight into SQL injection attacks against containing SQL injection attempts. For each MCP call, Claude Desktop prompted us to approve the generated OpenSearch query before execution, ensuring analyst oversight (human-in-the-loop or HITL) of automated queries, as shown in Figure 170. After approving the query, Claude Desktop executed it against the OpenSearch cluster and returned summarized findings revealing attack patterns, as shown in Figure 171.

Figure 170 | Claude Desktop OpenSearch MCP Query Approval

Figure 171 | OpenSearch MCP Natural Language Threat Hunting Query Example

By connecting an MCP server to an OpenSearch cluster containing security logs, analysts can perform threat hunting using conversational queries rather than learning complex query syntax. This allows analysts who are less familiar with OpenSearch to apply their threat hunting expertise without the barrier of mastering query languages. Further, analysts who are new to threat hunting can use natural language queries to explore log data and learn effective search patterns through model-generated queries. Analysts should not rely solely on AI-generated queries without review. In our testing, Claude Opus did an excellent job reviewing data and designing queries to illustrate attack patterns; however, it did not comprehensively identify all attacks captured in the web server logs. Organizations can use MCP as an augmentation to analyst capabilities, but human expertise remains essential for comprehensive threat hunting. In addition to abstracting the details of the query syntax from users, MCP integration allows the analyst to iteratively refine their search based on initial findings and to transform the findings into other formats. Through the integration of multiple MCP tools, analysts can build complex workflows that combine data retrieval, analysis, and reporting: “Take these results and produce a brief summary of the attack activity, followed by the detailed log entries in a table. Submit the data to JIRA as a new incident ticket assigned to the web security team with an appropriate title. By integrating multiple MCP servers, a human analyst can more quickly perform many otherwise manual threat-hunting tasks, benefiting from consistent operational procedures while freeing up time for higher- value analysis and decision-making.

Forensic Analysis Acceleration with Protocol SIFT

AI systems are transforming many aspects of cybersecurity, including offensive and defensive operations. As attackers adopt AI to accelerate attack campaigns, defenders must evolve their investigative capabilities to maintain parity.

Autonomous Adversaries

A significant shift in attacker techniques has occurred with the emergence of AI-orchestrated intrusion campaigns, in which large language models execute substantial portions of the attack lifecycle with minimal human supervision. This represents a new class of threat for organizations where AI acts as an intrusion operator rather than merely as an assistant to human operators. The implication of this evolving threat is that adversaries can increase both speed and scale of attacks through parallel reconnaissance, rapid iteration, and simultaneous delivery across many targets. Further, the required skill set for threat actors is reduced, lowering the barrier to entry for larger groups of threat actors to conduct sophisticated campaigns. This forces defenders to reconsider assumptions about the attacker’s dwell time, the speed of attack progression, and the amount of attacker labor required to run large campaigns. In September 2025, Anthropic detected and disrupted what it assessed as the first documented case of a large-scale cyber espionage campaign executed largely without substantial human intervention. [5] The campaign, attributed to a Chinese state-sponsored group dubbed GTG-1002, targeted approximately thirty global organizations, including technology companies, financial institutions, chemical manufacturers, and government agencies. The attackers used Claude Code’s agentic capabilities to execute reconnaissance, vulnerability discovery and validation, exploitation, credential harvesting, and data collection. Anthropic stated that the Claude model performed roughly 80-90% of the operational work on behalf of the attackers, with humans mostly setting direction and making a small number of decisions at key moments.

Figure 172 | Anthropic GTG-1002 Threat Actor Campaign Architecture [6]

While Anthropic has not publicly released detailed forensic evidence or IOCs to support its claims (leading to some controversy about the veracity of the report [7] ), the implications of AI-orchestrated campaigns are significant, and defenders should use this report as an early indicator of future threat actor capabilities.

Accelerating Forensic Investigations

For many organizations, investigative capabilities have not kept pace with the speed and scale of modern attacks. Attackers have always had an advantage in time-to-action, with forensic processes often requiring considerably longer to complete than the attack lifecycle itself. The use of autonomous AI by threat actors increases this gap to an untenable level, making manual forensic techniques insufficient for a timely response. When responding to AI-powered, autonomous attacks, responders need to adopt new approaches to maintain parity with threat actors' capabilities while maintaining the rigor required for forensic investigations. Responding to this need is Protocol SIFT, a framework from the SANS Institute that addresses this challenge by integrating Claude Code’s agentic capabilities into the SIFT Workstation project. With Protocol SIFT, analysts can utilize Anthropic models to automate the use of hundreds of forensic utilities into an orchestrated system guided by natural-language instructions. This integration leverages the capabilities of LLM ReAct (Reasoning and Acting [8] ) agents to provide autonomous investigative capabilities at accelerated speeds (see the sidebar ReAct Agents: Reasoning and Acting for Enhanced AI Capabilities).

Figure 173 | Protocol SIFT Analyst Opportunity

The application of Protocol SIFT for forensic investigations represents a shift from tool execution to tool orchestration. Instead of analysts choosing tools, reading and re-reading documentation about tool use, struggling with complex command-line options, and troubleshooting errors, the analyst role shifts. Analysts describe investigative goals, and the ReAct agent determines the appropriate tool chain, executes commands iteratively, evaluates results, and adjusts its approach based on findings until the investigation objective is satisfied.

From Tool Use to Tool Orchestration

Traditional forensic analysis requires analysts to remember complex command-line syntax for hundreds of specialized tools. An analyst investigating a Windows compromise must know the precise flags for log2timeline.py to process event logs, the correct syntax for RECmd to parse registry hives, and how to filter results with psort.py. This cognitive overhead slows investigations and creates barriers for less experienced analysts. Protocol SIFT transforms this workflow by embedding Claude Code within the SIFT terminal environment. Analysts state investigative intent in plain language, and the AI translates that intent into precise tool invocations. The analyst role shifts from memorizing syntax and running complex command-line tools to directing strategy and evaluating analysis results. For example, supplying Protocol SIFT with a directory of evidence from a target system used as a target in a red team engagement, we issued the following prompt with Claude Code: “Use the forensics data included in /mnt/hgfs to build a timeline of activity for November 2025. Identify threats that indicate malicious activity against the system.

Figure 174 | Claude Code Analysis Prompt on SIFT Workstation

Using Claude Code as an orchestrator, Protocol SIFT autonomously executed a multi-step forensic workflow:

• Identified the assets available in the /mnt/hgfs directory for analysis as VMware Workstation files.

• Examined VMware artifacts (logs, screenshots, disk images, memory dumps) to scope the investigation.

• Mounted VMDK virtual disk image using qemu-nbd for read-only file system analysis.

• Identified malware samples ( AnalyticsInstaller.exe, analytics.exe) and decoded embedded payloads using strings and base64.

• Analyzed Windows memory dump using strings to recover evidence of Meterpreter execution, Mimikatz usage, and network activity.

• Parsed Windows Event Logs (Security, PowerShell Operational) using evtxexport to correlate execution events.

• Reviewed Prefetch files to establish program execution timeline for November 27, 2025.

• Documented attack chain, persistence mechanisms, and compiled Indicators of Compromise (IOCs).

After several minutes, the model produced a detailed forensics report summarizing findings, including a timeline of malicious activity on November 27, 2025, as shown in Table 48.

Table 48 | Protocol SIFT Timeline of Malicious Activity

TIMESTAMP EVENT EVIDENCE SOURCE

15:55:26 VM powered on VMware log 15:56:XX System boot, user login Prefetch (explorer.exe, winlogon.exe) 15:57:XX Process Monitor launched for malware analysis Prefetch (PROCMON64.EXE) 15:58:XX analytics.exe executed (malicious payload) Prefetch (ANALYTICS.EXE- DD592902.pf)

TIMESTAMP EVENT EVIDENCE SOURCE

16:23:XX AnalyticsInstaller.exe executed (malware dropper) Prefetch

(ANALYTICSINSTALLER.EXE-

E57CE4F0.pf)

16:23:XX cmd.exe spawned by malware Prefetch, Memory dump 16:23:XX PowerShell executed with encoded command Prefetch (POWERSHELL.EXE) 16:33:XX Screenshot captured via Snipping Tool Prefetch (SNIPPINGTOOL.EXE)

Figure 175 | Protocol SIFT Forensic Findings

The combination of natural language direction, autonomous tool orchestration, and iterative reasoning allows Protocol SIFT to accelerate forensic investigations substantially, allowing analysts to focus on strategic decision-making rather than low-level tool operation.

REACT AGENTS: REASONING AND ACTING FOR ENHANCED AI CAPABILITIES

Protocol SIFT’s autonomous capabilities derive from the ReAct (Reasoning and Acting) agent architecture, a paradigm that combines Chain of Thought reasoning with external tool interaction to improve AI model capabilities on complex tasks.

The ReAct Framework

Traditional language models generate responses based solely on their training data, limiting them to the knowledge captured during training and preventing interaction with external systems. ReAct agents overcome these limitations by interleaving reasoning steps with actions that interact with the external environment. The ReAct cycle operates through three phases:

• First, the agent receives a task and reasons about how to approach it, breaking complex objectives into manageable steps.

• Second, the agent takes an action such as executing a command, searching the web, or calling an API, using available tools.

• Third, the agent observes the results of that action and incorporates the findings into its reasoning for the next iteration.

Figure 176 | Protocol SIFT ReAct Workflow Diagram

This cycle repeats until the agent determines the task is complete or requires human intervention.

Chain of Thought Reasoning

Chain of Thought (CoT) prompting enables models to solve complex problems by generating intermediate reasoning steps rather than jumping directly to conclusions. When analyzing forensic evidence, a ReAct agent might reason: "To build a timeline, I need to parse temporal artifacts using Plaso’s log2timeline.py from a disk image. I need to identify the format of the disk image first." This explicit reasoning makes the agent’s decision process transparent and allows it to recognize data.

Model Context Protocol Integration

MCP provides the standardized interface that allows ReAct agents to interact with external tools and other data sources. Through MCP, Protocol SIFT can orchestrate local forensic utilities on the SIFT Workstation, connect to remote systems via SSH for distributed evidence collection, query threat intelligence feeds for indicator enrichment, and interact with specialized analysis platforms, such as malware sandboxes. This extensibility means organizations can add new capabilities to Protocol SIFT by implementing MCP servers that expose internal tools or proprietary forensic capabilities, allowing the ReAct agent to incorporate these resources into its investigative workflows. For example, if an organization has a SIEM platform that is useful to query for scoping during investigations, the SIEM-specific MCP server can expose search capabilities, allowing the ReAct agent to retrieve relevant log data as part of its analysis.

Accuracy and Deep Understanding

The ReAct architecture improves accuracy through several mechanisms. Iterative refinement enables the agent to test hypotheses, evaluate results, and adjust its approaches when initial attempts fail. External tool verification grounds findings in deterministic tool output rather than in model inference, reducing the risk of hallucination. Web access provides access to current information beyond the model’s training cutoff date. Transparent reasoning displayed during the model’s analysis allows analysts to understand and verify the decision-making process. In forensic applications, these improvements translate to greatly accelerated analysis that can still be validated by human analysts. The combination of reasoning capabilities, access to external tools, and iterative problem-solving makes ReAct agents particularly well-suited for complex investigative tasks we need to solve, where the path to a solution is not immediately obvious and may require multiple approaches before achieving success.

Trust Mechanisms in Autonomous Forensics

Trust in forensic findings is essential not only for legal defensibility but also for organizational confidence in incident response decisions. Autonomous AI systems offer significant opportunities for speed and scale, but they also raise concerns about evidence integrity, reproducibility, and the potential for AI hallucinations to contaminate findings. Protocol SIFT implements multiple layers of control to ensure it produces valid forensic assessment results. The use of autonomous AI in forensic investigations raises significant concerns about evidence integrity, reproducibility, and legal defensibility. The nature of AI non- determinism creates challenges for forensic soundness, as findings must be verifiable and reproducible to withstand legal scrutiny. At the time of this writing, these are active areas of research and debate within the digital forensics community, and early adopters should carefully consider the implications of AI integration on their forensic practices.

Inference Constraint

Inference constraints define the boundary between AI inference and deterministic tool output. Protocol SIFT maintains a high inference constraint. Claude Code orchestrates tools and reasons over the structured output those tools produce, but the underlying evidentiary facts come from the tools rather than from the model’s inference. Instead of asking the model to directly interpret binary data or to guess file contents, Protocol SIFT routes evidence through vetted SIFT utilities. For example, when analyzing a registry hive, Protocol SIFT invokes RECmd, a well-known and trusted tool, to parse the binary structure of the hive and produce structured output. The model reasons over that structured output rather than over the raw bytes, so its analytical conclusions are grounded in deterministic parsing. This approach limits hallucinations that would otherwise contaminate the evidence analysis. The AI cannot fabricate registry keys or invent timeline entries because the facts it works with come from deterministic parsing tools.

Human in the Loop (HITL)

Protocol SIFT implements mandatory human checkpoints for critical operations. By default, the system operates in read-only mode and prompts analysts for permission before executing any command that could alter the system or evidence. Before running commands, Protocol SIFT displays the exact syntax it will execute and asks for approval. This visibility allows analysts to verify correctness and maintain audit trails showing which commands were executed and when approval was granted. Analysts can configure allowlists for common read-only tools like fls, icat, or exiftool to optimize workflows without compromising control. Commands that write data, modify files, or alter system state always require explicit approval.

Forensically Sound Tools

Protocol SIFT orchestrates only well-established, vetted forensic utilities included in the SIFT Workstation. Tools like The Sleuth Kit, the Volatility Framework, and Eric Zimmerman’s utilities have established track involvement in evidence analysis. For example, in our earlier investigation of the Windows system using VMware virtual disk evidence, the audit log captured every command Claude Code generated, the analyst approvals granted, and the output from each tool in the ~/.claude/projects directory tree. JSON files capture each step of the ReAct reasoning process, allowing reviewers to trace how the model arrived at each decision. An example of an audit log entry is included in Listing 138, with the tool output also captured alongside the logging entry.

Listing 138 | Claude Code Audit Log Example

"message": { "model": "claude-opus-4-5-20251101", "content": [ { "type": "thinking", "thinking": "Found Windows event logs. There's also a procmon.png on the desktop which could be a screenshot of process monitor showing malicious activity. Let me:\n1. View the procmon.png\n2. Check the live Windows event logs\n3. Look for PowerShell history\n4. Use hayabusa to analyze the event logs", } 1 ], }, // [...] omitted for brevity "message": { "model": "claude-opus-4-5-20251101", "content": [ { "type": "tool_use", "id": "toolu_01LHyUN5JiNoGc4PnCkKqiYQ", "name": "Bash", "input": { "command": "find /mnt/windows/Users/Sec504 -name \"*PowerShell*\" -o -name \"*history*\" -o -name \"ConsoleHost_history.txt\" 2>/dev/null", 2 "description": "Find PowerShell history files" } } ], } 1 JSONL output edited for brevity. 2 Example command generated by Claude Code to locate PowerShell history files. These trust mechanisms work together to enable analysts to employ autonomous operation while meeting forensic soundness requirements. Analysts gain speed and scale advantages without sacrificing the auditing, verification, and reproducibility needs essential for legal proceedings.

OPERATIONAL CONSIDERATIONS

Effective AI integration into incident response requires attention to verification practices, documentation standards, and ongoing skill development. In this section, we’ll examine how these factors shape the practical use of AI in forensic workflows.

Verification and Trust

AI output requires verification before action or documentation as factual conclusions. This principle applies regardless of how confident or authoritative the AI response appears. Verification approaches vary by use case. Log analysis verification requires manually confirming that identified patterns exist in source data. If AI claims to detect beaconing behavior at five-minute intervals, analysts should examine the timestamps directly to verify this pattern is present. Timing calculations should be confirmed since models sometimes struggle with precise numerical reasoning. Pattern identification is a hypothesis that requires evidence-based confirmation. Report drafts generated by AI should have every factual claim checked against source evidence. Quotes and statistics, in particular, require verification, since models may alter wording or combine statistics from different contexts. An AI-generated executive summary should preserve the accuracy of technical findings while changing only presentation style and technical depth. Playbooks generated by AI should be tested where possible before operational use. Subject matter experts should review the technical accuracy of procedures, commands, and tool references. An untested AI- generated playbook may contain syntactically incorrect commands, reference nonexistent features, or recommend procedures inappropriate for the organizational environment. Documentation should capture verification performed for significant findings. Stating "AI-assisted analysis identified X, verified by [manual review/testing/SME confirmation]" maintains transparency about how conclusions were reached. This transparency supports both immediate trust in findings and future review if conclusions are questioned.

Documentation Practices

When AI assists in analysis, documentation should reflect this contribution and the verification performed. Incident documentation should note when AI tools were used and for what purpose. This notation allows reviewers to distinguish which findings resulted from AI assistance and which from traditional analysis methods. For example, "Code analysis performed using AI-assisted deobfuscation, findings verified through execution in an isolated environment" provides clear provenance for the document audience. Verification steps for AI-generated findings should be documented with the same rigor as for any analytical tool output. When AI identifies a pattern in log data, documentation should state "Pattern identified by AI analysis, manually confirmed in logs from [timestamp range]." This documentation supports challenges to findings by making the verification basis explicit. AI interaction logs should be preserved where they contributed to significant conclusions. Preserving these logs introduces a level of documentation accountability that analyst working notes from manual investigations rarely matched, since those notes were seldom retained or reviewed. The added burden is offset by the reproducibility, defensibility, and continuous-improvement benefits described later in this section. If an AI conversation reveals a critical insight into malware functionality, it should be retained as part of the investigation record. Review the documentation for your AI platform to understand the available logging and export options. Several platforms provide conversation export features that facilitate record-keeping, or agent frameworks may log interactions automatically (such as Claude Autonomous Forensics). Documentation should distinguish between AI-suggested hypotheses and verified findings. AI might suggest that observed behavior indicates data exfiltration based on network traffic volume, but this hypothesis requires confirmation through detailed traffic analysis. Documenting which claims are AI hypotheses and which are verified findings prevents confusion during review or legal proceedings. This documentation approach supports three critical needs: reproducibility, defensibility, and continuous improvement.

• Reproducibility allows others to understand how conclusions were reached, following the analytical path from evidence through AI assistance to verified findings.

• Defensibility ensures that if findings are challenged, the basis and verification are clear rather than relying on assertions about AI capabilities.

• Continuous improvement is possible by reviewing AI-assisted work to refine prompts and identify where AI adds value and where traditional methods remain superior.

Documentation is seldom a favorite task for analysts, but maintaining high standards in how we build documentation is essential for defensible, trustworthy incident response.

Building Organizational Capability

AI integration benefits from deliberate skill development and consistent deployment throughout the organization, rather than ad hoc adoption. At the time of this writing, using AI models for incident response is still a relatively new practice, and few organizations have mature processes for consistent AI use as part of their incident response process. While one analyst can substantially accelerate their work through AI assistance, organizational benefits grow exponentially when team members share effective practices and build collective capability across the organization. In this section, we’ll explore several practices that help organizations utilize AI for incident response across the team for greater impact.

Prompt Libraries

Teams should develop and maintain collections of effective prompts for common tasks. When an analyst creates a prompt that consistently produces useful results, it becomes a reusable asset. Successful prompts should be shared across the team, reducing duplication of effort and accelerating capability for analysts who have not yet developed equivalent prompts. Sharing prompts helps accelerate team capability by providing starting points for less experienced analysts and as inspiration for further refinement and continued development. For example, a prompt that effectively guides AI-assisted malware code analysis can serve as a template for other analysts to adapt for different malware families or analysis contexts, and serves as an excellent learning tool for how less experienced analysts can structure their prompts for better results.

Skill Files and Prompt Library Integration

Prompt libraries can be stored in shared documents, wikis, or version-controlled repositories, but they can be integrated more quickly when embedded in AI platforms that support custom prompt templates. Skills files are commonly used in Claude Code, OpenAI Codex, and Gemini CLI to define reusable prompt structures that analysts can select when initiating new analysis tasks. By embedding prompts into the AI platform, organizations reduce the friction analysts face when accessing effective prompts, increasing the likelihood of consistent use. For my Claude Code environment, I maintain several skills for specific tasks that I will reuse frequently. For example, I have a Sigma detection rule generation skill that I use to create Sigma rules from analyst descriptions of observed behavior, as shown in Listing 139.

Listing 139 | Claude Code Skill File Example

$ pwd

~/forensics $ cat .claude/commands/sigma.md

---

description: Generate Sigma detection rules from attack descriptions or observed artifacts

---

Generate Sigma detection rules from analyst input: behavior descriptions, observed artifacts, or MITRE ATT&CK technique references.

## Process

1. **Parse input** to identify log source, detection fields, and attack context

2. **Map to log source** using the table below

3. **Build detection logic** with selection criteria, optional filters, and condition

4. **Generate complete YAML** with metadata, tags, and false positive notes

5. **Provide context** including conversion commands for target SIEMs Use defaults when not specified: status `experimental`, level `medium`, author `Falsimentis IR Team`.

## Log Source Reference

| Behavior | Product | Category |

|----------|---------|----------|

| Process execution | windows | process_creation |

| PowerShell | windows | ps_script |

| File events | windows | file_event |

| Registry | windows | registry_event |

| Network | windows | network_connection |

| Linux processes | linux | process_creation |

| AWS | aws | cloudtrail |

## Output Template

```yaml

title: <Descriptive title>

id: <UUID>

status: experimental

description: <Detection purpose>

references:

- <MITRE ATT&CK or relevant URL>

author: IR Team

date: YYYY/MM/DD

tags:

- attack.<tactic>

- attack.<technique_id>

logsource:

product: <product>

category: <category>

detection:

selection:

<field>: <value>

condition: selection

falsepositives:

- <Legitimate scenarios>

level: medium

```

## Example

**Input**: `/sigma outlook.exe spawning cmd.exe or powershell.exe`

```yaml

title: Email Client Spawning Command Shell

id: a1b2c3d4-e5f6-7890-abcd-ef1234567890

status: experimental

description: Detects Outlook spawning command interpreters, indicating possible malicious

attachment execution.

references:

- hxxps://attack[.]mitre[.]org/techniques/T1204/002/

author: IR Team

date: 2025/01/24

tags:

- attack.execution

- attack.t1204.002

logsource:

product: windows

category: process_creation

detection:

selection_parent:

ParentImage|endswith: '\outlook.exe'

selection_child:

Image|endswith:

- '\cmd.exe'

- '\powershell.exe'

condition: selection_parent and selection_child

falsepositives:

- Legitimate Outlook add-ins

level: high

```

This skill is available at [Course Example Link]

When I need to create a new Sigma rule, I can invoke this skill using the /sigma command (matching the skill Markdown file name) and supply the context for the desired Sigma rule: “/sigma Process created cmd.exe spawning from outlook.exe with command line containing "http" The model then generates a complete Sigma rule based on the input, as shown in Figure 177.

Figure 177 | Claude Code Sigma Rule Generation Example
