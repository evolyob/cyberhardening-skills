# 第 18-2 章：雲端專用劇本－虛擬工作負載鑑識與 IIoT 邊緣閘道應變

> 模組化子章節 | 隸屬來源: DAIR-IR Framework

---

Beyond direct role assignments, additional mechanisms may change the true scope of an identity

compromise. A compromised identity in AWS may appear able to manage users in an account, but a

permission boundary, Service Control Policy (SCP), session policy, or resource-based policy could ultimately

prevent those actions after the full access evaluation flow. Understanding the full policy evaluation chain is

important for accurately scoping what a compromised identity can actually do.

In AWS, the policy evaluation logic follows a specific order: first, explicit denies in any applicable policy take

precedence; then, organization SCPs are evaluated, followed by resource-based policies, identity-based

policies, IAM permission boundaries, and finally session policies. At each layer, an explicit deny overrides

any allow. This means a compromised identity with AdministratorAccess may still be unable to perform

certain actions if an SCP or permission boundary restricts them. AWS documents this evaluation chain in

detail in the IAM User Guide, and responders should reference it when the apparent permissions do not

match observed behavior.

After identifying affected identities, identify affected resources. This helps establish the threat actor’s

actions in the environment and determine whether unauthorized changes were made. For storage accounts,

buckets, and other data stores, the organization will want to know whether any data was exposed. Certain

resources could also facilitate lateral movement.  Virtual machines in the cloud often host an Instance

Metadata Service (IMDO) service that provides access tokens to service accounts or roles, which can then

be used to escalate privileges.

Finally, examine the cloud network architecture to evaluate potential lateral movement. If the compromised

cloud environment has direct access to additional cloud organizations within the same provider, the on-

premises environment, or another cloud provider, there may be additional logs to collect and analyze to

determine whether those connected environments were also compromised.

CIRCLECI: WHEN A STOLEN SESSION TOKEN COMPROMISES THE SUPPLY

CHAIN

In January 2023, CircleCI, a continuous integration development platform, disclosed that an attacker

had compromised an engineer’s laptop with malware and stolen a valid SSO session token. [6]

Because

the token was already authenticated past MFA, the attacker bypassed multi-factor controls entirely

and used the session to access CircleCI’s internal systems.

From that single session token, the attacker accessed the production environment and exfiltrated

customer secrets, including environment variables, API tokens, and encryption keys stored in

CircleCI’s platform. The scope was significant: CircleCI advised all customers to rotate every secret

stored in their environment, affecting thousands of organizations that relied on the platform for

CI/CD pipelines. An attacker with the stolen credentials could access any of the platforms and

services that customers integrated with CircleCI, including cloud platforms, code repositories, and

SaaS applications.

What makes this incident instructive for cloud responders is the attack chain: a stolen session token

provided access without triggering credential-based detections, and the blast radius extended to

every downstream customer whose secrets were stored in the platform. The investigation required

analyzing session logs, internal access patterns, and data-plane activity rather than traditional host-

based forensics.

This case illustrates two important lessons in cloud IR. First, MFA alone does not prevent token-based

access, and session token theft should be considered as an important factor during scoping. Second,

when a cloud platform is compromised, the incident extends to every customer and integration that

trusted that platform with credentials.

Log Sources

We mentioned during preparation the importance of enabling and centralizing logs prior to incidents. This

section discusses control-plane and data-plane logs, what data they contain, and their relevance to incident

response.

Management/control plane logs  record Identity and Access Management (IAM) events, administrative

events, and resource management events. As mentioned earlier, these logs are enabled by default.

IAM events are one of the most critical categories available during an investigation. For initial access, these

logs help determine who logged in, when, from where, and how.

Additional context in these logs, such as success/failure status and login method, provides a more complete

picture of the intrusion. The example in Listing 143 from an Azure sign-in log shows that a user correctly

authenticated with their password but failed both MFA attempts. This pattern could indicate that a

password was successfully stolen but MFA controls are preventing a compromise.

Listing 143 | Azure Sign-In Log Authentication Details

[

{

"authenticationStepDateTime": "2025-05-25T01:54:30.9375542+00:00",

"authenticationMethod": "Password",

"authenticationMethodDetail": "Password in the cloud",

"succeeded": true,

"authenticationStepResultDetail": "Authentication in progress"

},

{

"authenticationStepDateTime": "2025-05-25T01:54:30.9375542+00:00",

"authenticationMethod": "Mobile app notification",

"succeeded": false,

"authenticationStepResultDetail": "MFA denied; user did not select the correct number"

},

{

"authenticationStepDateTime": "2025-05-25T01:54:30.9375542+00:00",

"authenticationMethod": "Text message",

"succeeded": false,

"authenticationStepResultDetail": "MFA denied; invalid verification code"

}

]

Once access is gained, IAM logs provide insight into persistence or privilege escalation activities, such as

creating new users or assigning additional roles to compromised accounts. Depending on the attacker’s

tactics and techniques, organization-level management events may also appear, such as changes to logging

configuration or domain settings.

Resource management events include the creation, deletion, starting, and stopping of resources. These

events provide significant insight into attacker intentions. Attempts to perform destructive attacks by

deleting critical resources would appear in these logs, as would the creation of GPU-enabled virtual

machines that may indicate a cryptomining attack. The CloudTrail event in Listing 144 shows a RunInstances

call launching a p3.2xlarge GPU instance, a common indicator of cryptomining activity. Details worth noting

include the instance type, the region (attackers often target regions the organization does not normally

use), and the identity that initiated the request.

Listing 144 | CloudTrail Event: GPU Instance Creation

{

"eventTime": "2025-08-14T03:22:17Z",

"eventSource": "ec2.amazonaws.com",

"eventName": "RunInstances",

"awsRegion": "ap-southeast-1",

"sourceIPAddress": "198.51.100.47",

"userIdentity": {

"type": "AssumedRole",

"arn": "arn:aws:sts::471903287148:assumed-role/LambdaExecRole/i-0e83f91a7c42d1b05"

},

"requestParameters": {

"instanceType": "p3.2xlarge",

"instancesSet": { "items": [{ "imageId": "ami-0c7ea5497c02abcf5" }] },

"minCount": 4,

"maxCount": 4

}

}

Data plane logs , also known as resource logs, contain resource-level operations. These logs are off by

default, but without them, responders often lack the full picture of an incident. Table 56  illustrates the

difference between what each log plane captures for common cloud resources.

Table 56 | Control Plane vs. Data Plane Logging

RESOURCE CONTROL PLANE (DEFAULT ON) DATA PLANE (DEFAULT OFF)

Storage

(S3/Blob/GCS)

Bucket creation, deletion, policy

changes

Individual object reads, writes, and

deletions

Virtual machines Instance creation, termination,

security group changes

OS-level logs, network flow logs,

process execution

Databases Instance provisioning, configuration

changes, backup operations

Individual queries, data access, row-

level operations

IAM User creation, role assignments,

policy modifications

Authentication attempts, token

issuance, session activity

Consider an incident where an attacker accesses sensitive files in an S3 bucket.  Control plane logs

(CloudTrail) would show if the attacker modified the bucket policy, but only S3 server access logs or

CloudTrail data events would reveal which specific objects were downloaded. Similarly, if initial access was

gained by compromising a public-facing virtual machine, only the operating system logs on the endpoint or

network flow logs on the VPC would show evidence of the access vector.

Without data plane logs, responders may be able to confirm that a resource was compromised but not what

the attacker did with it. This gap directly affects the organization’s ability to assess data exposure and meet

breach notification requirements.

Without data-plane logs, a breach notification assessment may be impossible. Regulatory

frameworks such as GDPR, HIPAA, and PCI DSS require organizations to determine which

data was accessed during a breach. If the only available logs show that a policy was

changed but not what objects were subsequently downloaded, the organization may be

forced to assume worst-case exposure and notify all affected parties.

Together, control-plane and data-plane logs allow responders to trace an attacker’s path through a cloud

environment. Understanding which log sources are available and what they capture is essential for building

a complete timeline of attacker activity.

Isolating Compromised Resources

When resources are exposed or compromised, it is important to quickly remediate the issues that allow the

threat actor to continue their attack or that could enable a new threat actor to enter the environment.

While different approaches apply depending on the impacted service, this section covers two of the most

commonly targeted public-facing resources: virtual machines and storage accounts/buckets.

Virtual Machine Isolation

When a virtual machine is compromised, it may seem like the only option is to shut down the host. There is

a better approach that maintains the host for deeper analysis and provides insight into the threat actor’s

intent. With virtual network controls, we can isolate VMs in a configuration that blocks inbound and

outbound traffic, except for designated forensic networks. Combined with flow logs on the isolated subnet

or compromised host, we can monitor what an active threat actor or malware infection is trying to do.

For example, using the Azure CLI, analysts can create a Network Security Group (NSG) with rules designed

to deny all access except for a designated forensics subnet, as shown in Listing 145. This approach keeps the

VM running for continued observation while cutting off the threat actor’s access.

Listing 145 | Isolating a Compromised VM with an Azure NSG

$ az network nsg create --resource-group rg-prod-eastus --name nsg-isolation 1

$ az network nsg rule create --resource-group rg-prod-eastus --nsg-name nsg-isolation --name

AllowForensicsSubnet --priority 100 --direction Inbound --access Allow --source-address-prefixes

192.168.200.0/24 --destination-port-ranges '*' --protocol '*' 2

$ az network nsg rule create --resource-group rg-prod-eastus --nsg-name nsg-isolation --name

DenyAllInbound --priority 4096 --direction Inbound --access Deny --source-address-prefixes '*'

--destination-port-ranges '*' --protocol '*' 3

$ az network nsg rule create --resource-group rg-prod-eastus --nsg-name nsg-isolation --name

DenyAllOutbound --priority 4096 --direction Outbound --access Deny --source-address-prefixes '*'

--destination-port-ranges '*' --protocol '*' 4

$ az network nic update --resource-group rg-prod-eastus --name compromised-vm-nic --network

-security-group nsg-isolation 5

1 Create a dedicated isolation NSG in the same resource group as the compromised VM.

2 Allow inbound access only from the forensics subnet (192.168.200.0/24) at a high priority.

3 Deny all inbound traffic at a lower priority, ensuring the forensics allow rule takes precedence.

4 Deny all outbound traffic to prevent the compromised VM from communicating externally.

5 Apply the isolation NSG to the compromised VM’s network interface to immediately restrict access.

Storage Account and Bucket Remediation

Data exfiltration is one of the top impacts of cloud compromises, and some of the most valuable data resides

in storage accounts or buckets. A simple misconfiguration of a storage resource with sensitive data can

easily lead to exposure, and threat actors are constantly running automated scanners to find misconfigured

buckets.

“Weak or no authentication accounted for nearly half of initial access in H1 2025, with many

environments having overprivileged service accounts with high-privilege default credentials. [7]

- Google Threat Horizons Report, H1 2025

If a bucket has been compromised during an incident, it is important to quickly resolve any

misconfigurations to prevent further data exposure. The specific remediation procedures vary by cloud

provider.

AWS

S3 buckets can be restricted using a combination of Block Public Access  settings and policies.  Block Public

Access overrides any configurations applied via policies or ACLs, making it the most effective first step for

stopping exposure. IAM or resource-based policies can then be applied to specify which users can take what

actions on which buckets. In legacy configurations, Access Control Lists (ACLs) may control access. These

are important to check during a compromise, as attackers can abuse them, but ACLs should not be used for

new access control configurations.

The commands in Listing 146 show how to restrict public access on each provider.

Listing 146 | Restricting Public Access on Cloud Storage

$ aws s3api put-public-access-block --bucket <bucket-name> --public-access-block-configuration

BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true 1

$ aws s3api get-public-access-block --bucket <bucket-name> 2

$ az storage account update --name <account-name> --resource-group <rg-name> --allow-blob-public

-access false 3

$ gcloud storage buckets update gs://<bucket-name> --public-access-prevention=enforced 4

$ gsutil iam ch -d allUsers gs://<bucket-name>

$ gsutil iam ch -d allAuthenticatedUsers gs://<bucket-name>

1 Enable Block Public Access on an S3 bucket, overriding any policies or ACLs that grant public access.

2 Verify the current public access settings after applying the change.

3 Disable anonymous access on an Azure storage account.

4 Enforce public access prevention on a Google Cloud bucket and revoke allUsers and allAuthenticatedUsers bindings.

To assess exposure on AWS, review S3 server access logs or CloudTrail data events for the bucket to

identify what objects were accessed and by whom. The s3logparse tool can simplify the analysis of S3 server

access logs during an investigation.

Azure

If anonymous read access has been granted to an Azure storage resource, it is configured at either the

container level or the blob level, with container-level settings overriding blob-level settings. A user with

permissions to set AllowBlobAnonymousAccess should change the settings to prevent anonymous access

before further exposure occurs on containers that should not be public.

Google Cloud

Permissions on Google Cloud buckets are controlled in two ways: IAM policies and ACLs. To remediate an

exposed bucket, apply IAM policies granting only the permissions needed to the users who need them. As

with AWS, ACLs are a legacy option that should be checked during a compromise investigation but should

not be used for remediation. If both ACLs and IAM permissions are in place, only one needs to allow access

for it to be granted, so checking IAM permissions alone is not sufficient.

Time is a factor when remediating exposed storage. Automated scanners continuously probe for

misconfigured buckets, and public exposure can be discovered and exploited within hours of

misconfiguration. Once access controls are corrected, responders should verify the remediation by

attempting to access the resource from an unauthenticated context to confirm that public access is no

longer possible.

Exposed storage resources can be discovered and exploited within hours of

misconfiguration. Automated scanners continuously probe for publicly accessible buckets

and containers, so the time between discovery and remediation directly affects the volume

of data exposure. Prioritize restricting access before conducting a full investigation of what

was accessed.

Each of these providers has detailed documentation on access controls, but this overview should point

responders in the right direction when a storage resource is compromised.

Eradicating Cloud Persistence

Cloud environments provide threat actors with numerous methods to establish persistence based on their

level of access post-compromise. While a comprehensive treatment of every persistence technique is

outside the scope of this book, this section highlights the most important areas to examine during

eradication.

Identity and Access Management

IAM is one of the most important services in cloud environments, and it is also one of the easiest places for

a threat actor to establish persistence with the right permissions. In addition to reviewing IAM logs,

responders should directly examine IAM resources for any recently created or modified items.  Areas to

examine include:

• Service accounts created by the threat actor.

• Access keys generated for existing or new accounts.

• Role assignments or policy changes that grant elevated privileges.

• OAuth application consent grants that provide API access without requiring user credentials.

• MFA configuration changes, including disabling MFA or registering attacker-controlled devices.

The CLI commands in Listing 147 can help identify common IAM persistence mechanisms across the major

cloud providers.

Listing 147 | Identifying IAM Persistence Mechanisms

$ aws iam list-users --query 'Users[*].UserName' --output text | xargs -I{} aws iam list-access-

keys --user-name {} 1

$ az ad app list --query "[].{Name:displayName,AppId:appId,Created:createdDateTime}" -o table 2

$ gcloud iam service-accounts list --format="table(email)" | xargs -I{} gcloud iam service-

accounts keys list --iam-account={} --managed-by=user 3

1 List all IAM users and their access keys with creation dates (AWS).

2 List OAuth applications and their creation timestamps to identify recently registered apps (Azure).

3 List all user-managed service account keys to identify keys created by a threat actor (Google Cloud).

Revoking credentials alone is not sufficient if active sessions remain valid. Cloud provider tokens typically

remain valid until they expire, even after the underlying credential is rotated. Responders should revoke

active sessions in addition to rotating credentials:

• In AWS, attach an inline policy to deny actions before a specific time.

• In Azure, revoke user sessions through Entra ID.

• In Google Cloud, invalidate OAuth tokens for the affected service accounts.

These persistence mechanisms should be reviewed as part of any cloud compromise investigation, as they

represent the most common methods for regaining access after an initial response.

IAM is the most common persistence vector in cloud compromises. Mandiant’s M-Trends

2025 report identifies identity-based persistence as the leading method attackers use to

maintain access in cloud environments. [8]

Responders should treat IAM review as the first

priority during eradication, before addressing compute or network persistence.

Compute and Workloads

For compute services, responders should consider virtual machines, containers, and serverless functions, all

of which can be backdoored. For virtual machines, the most common methods of retaining access include:

• Backdooring machine images used to deploy new instances.

• Installing malware on running hosts.

• Injecting malicious user data or startup scripts that execute on boot.

Startup scripts are particularly effective because they re-execute each time the instance boots, surviving

reboots and even redeployments from the same image.

Because startup scripts persist in the instance configuration and re-execute on every boot,

responders should check both running instances and the machine images or launch

templates used to create them. A compromised image will reintroduce the backdoor every

time a new instance is deployed from it.

For containers, the container registry can be poisoned to ensure newly created instances include

backdoors. Responders should compare running container images against known-good digests in the

registry and review any recently pushed images for unauthorized modifications.

Serverless functions are a frequently overlooked persistence vector. An attacker with sufficient permissions

can create a Lambda function, Azure Function, or Cloud Function that executes on a schedule or in

response to events, periodically creating new access keys or exfiltrating data. Because serverless functions

do not have a persistent host, traditional endpoint monitoring cannot detect them. Responders should list

all functions across regions and review their triggers, code, and execution history, as shown in Listing 148.

Listing 148 | Enumerating Lambda Functions Across Regions

$ for region in $(aws ec2 describe-regions --query 'Regions[*].RegionName' --output text); do

echo "=== $region ===" && aws lambda list-functions --region $region --query

'Functions[*].{Name:FunctionName,Modified:LastModified,Runtime:Runtime}' --output table; done

=== ap-south-1 ===

=== eu-north-1 ===

=== eu-west-3 ===

=== eu-west-2 ===

=== eu-west-1 ===

=== ap-northeast-3 ===

=== ap-northeast-2 ===

=== ap-northeast-1 ===

=== ca-central-1 ===

=== sa-east-1 ===

=== ap-southeast-1 ===

=== ap-southeast-2 ===

=== eu-central-1 ===

=== us-east-1 ===

-------------------------------------------------------------------------

|                              ListFunctions                            |

+-------------------------------+-------------------------+-------------+

|           Modified            |         Name            |   Runtime   |

+-------------------------------+-------------------------+-------------+

|  2022-05-26T17:00:49.000+0000 |  secheaders-cloudfront  |  nodejs14.x |

|  2025-11-05T12:00:13.000+0000 |  erk-requireauth        |  nodejs22.x |

|  2016-02-12T02:09:49.179+0000 |  blackFriday            |  python2.7  |

|  2022-03-01T21:59:46.000+0000 |  testKMSAccess          |  nodejs14.x |

+-------------------------------+-------------------------+-------------+

=== us-east-2 ===

=== us-west-1 ===

=== us-west-2 ===

The challenge with many of these techniques is that they either do not appear in logs or the log entries lack

sufficient context to identify the persistence mechanism. For virtual machines, control-plane logs capture

instance creation and modifications to startup scripts, but the contents of the scripts themselves are not

logged. For serverless functions, the control plane captures function creation and updates, but the function

code and its execution output require separate log sources (such as CloudWatch Logs for Lambda).

Investigation often requires host forensics or manual review of resources in the cloud console to identify

these backdoors.

Networking

Network resources are critical security controls that, with simple modifications, can open access to both

the original threat actor and new ones. A single network security group or ACL change can make a

previously restricted resource accessible from the internet. More advanced techniques include creating

persistent VPN tunnels or reconfiguring DNS settings to redirect traffic.

These are common persistence techniques, but they are not a comprehensive list. Responders should

review network configurations as part of eradication and compare the current state against known-good

baselines where available.

Across all three categories, the common thread is that cloud persistence often requires only API-level

access rather than host-level compromise, making it faster to establish and harder to detect through

traditional endpoint monitoring.

COMMON CLOUD IR MISTAKES

I have seen several recurring mistakes during cloud incident response engagements that are worth

calling out.

First, shutting down compromised instances before capturing them. Once an instance is terminated,

volatile data (memory, running processes, network connections) is lost permanently. Always snapshot

the instance before taking any containment action.

Second, rotating credentials without revoking active sessions. A new password or access key does not

invalidate existing tokens. If an attacker has a valid session token, they can continue operating even

after the credentials are changed. Explicitly revoke sessions in addition to rotating credentials.

Third, assuming control plane logs tell the complete story. I have worked cases where the

investigation concluded based solely on CloudTrail or Activity Log analysis, missing lateral movement

and data access that only appeared in data plane logs, VPC flow logs, or host-level telemetry. Control

plane logs show what was configured, not necessarily what happened after the configuration

changed.

Fourth, checking only one region. Cloud providers operate across dozens of regions, and attackers

frequently create persistence resources in regions the organization does not normally use. An access

key created in us-east-1 can provision a Lambda function in ap-southeast-1 that the team never

checks. Always enumerate resources across all regions during eradication.

Each of these mistakes stems from applying on-premises assumptions to cloud environments.

Building cloud-specific checklists into response runbooks and rehearsing them in tabletop exercises

helps teams avoid these pitfalls when the pressure of a real incident makes shortcuts tempting.

Automated Response Capabilities

One advantage of working in cloud environments is the native tooling available for automated incident

response. The specific implementation depends on the cloud provider and the organization’s response

process, but the core concept applies across all major platforms. The following example demonstrates how

a detection can trigger an automated investigation workflow for a compromised host in AWS. [9]

Trigger: A GuardDuty alert fires for a suspected compromised EC2 instance, and a Lambda function

executes the following steps:

1. The EC2 instance is placed in a private subnet with no internet access.

2. Flow logs are enabled on the subnet, VPC, or network interface to monitor network communications.

3. A snapshot of the EC2 instance is taken and stored in an S3 bucket.

The AWS CLI commands in Listing 149  show what this Lambda function would execute. These same

commands can also be run manually by a responder if automation is not yet in place.

Listing 149 | Automated EC2 Isolation and Snapshot

$ aws ec2 modify-instance-attribute --instance-id i-0a1b2c3d4e5f67890 --groups <isolation-

security-group-id> 1

$ aws ec2 create-flow-logs --resource-type NetworkInterface --resource-ids eni-0a1b2c3d4e5f67890

--traffic-type ALL --log-destination-type s3 --log-destination arn:aws:s3:::forensics-flow-logs

$ aws ec2 create-snapshot --volume-id vol-0a1b2c3d4e5f67890 --description "Forensic snapshot -

GuardDuty finding 2025-08-14" --tag-specifications

'ResourceType=snapshot,Tags=[{Key=Case,Value=IR-2025-042}]' 3

1 Replace the instance’s security groups with an isolation group that denies all inbound and outbound traffic.

2 Enable flow logs on the instance’s network interface to capture any attempted communications.

3 Create a tagged snapshot of the instance’s EBS volume for forensic analysis.

With this automation in place, responders can be confident the host is isolated without making manual

changes, and they can quickly retrieve the snapshot for host-level forensics.

This is a basic demonstration of the concept, but these types of workflows extend to many response

scenarios. Most manual steps taken during active response can be converted into scripts and actions

triggered automatically by an alert or initiated manually by a responder.

Even without a fully automated pipeline, wrapping the CLI commands shown above in

simple scripts ensures consistent execution under the pressure of an active incident. A

shell script that isolates an instance, enables flow logs, and captures a snapshot can be

written in minutes and eliminates the risk of missed steps or typos during manual

responses.

DEBRIEF

Cloud incidents often reveal gaps in configuration, visibility, and access management that are unique to

cloud environments. The debrief phase is an opportunity to identify these gaps and translate them into

concrete improvements for cloud security posture.  General debrief guidance, including facilitating After-

Action Review (AAR) sessions, documentation requirements, and implementation tracking, is covered in

Debrief Activity . This section focuses on cloud-specific debrief questions and explores how cloud

capabilities themselves can improve future incident response.

Cloud-Specific Debrief Questions

Beyond the standard AAR questions covered in Conducting the After-Action Review, cloud incident debriefs

should address considerations unique to cloud environments:

• Identity and access:  What identities were compromised, and what permissions was the threat actor

able to obtain? Were the identities following the principle of least privilege? If not, what identity

controls should be implemented to reduce the blast radius?

• Resources: What resources were compromised? Did the identities that provided access to those

resources actually need that access, or should more restrictive policies be applied?

• Networking: Did the threat actor bypass any network controls? Were network rules too permissive or

misconfigured? What additional network controls would prevent unauthorized access while maintaining

functionality?

• Data exfiltration: Are there any resources within the blast radius that contain sensitive data (storage

buckets, virtual machines, databases, etc.)? Did the threat actor access these resources? Is there any

evidence of mass exfiltration?

These questions help focus the debrief on cloud-specific lessons that generic incident reviews may

overlook.

Leveraging the Cloud for Incident Response

In the response actions section, we mentioned the ability to use serverless functions to build an automated

response pipeline. This is one of many ways to leverage cloud capabilities for incident response. The same

infrastructure that organizations use for production workloads can be repurposed for forensic analysis,

evidence storage, and automated response, often at a fraction of the cost of maintaining dedicated on-

premises forensic infrastructure. The following sections highlight several ways the cloud can improve

incident response efficiency and effectiveness.

Cloud Infrastructure for Forensic Workstations

Cloud compute resources and infrastructure-as-code templates provide a modern way to equip responders

with forensic workstations. Rather than distributing physical workstations to work locations, organizations

can deploy pre-configured virtual machines with the compute and memory resources needed for intensive

forensics workloads. These images can be maintained with current tooling and deployed on demand,

ensuring responders always have access to a consistent, up-to-date analysis environment.  Infrastructure-

as-code tools such as AWS CloudFormation, Azure Resource Manager templates, or Terraform enable

forensic environments to be created and destroyed with a single command. This makes it practical to spin

up a fresh workstation for each investigation and tear it down when the case is closed.

Secure, Read-Only Log Storage

In cases where forensic integrity is critical, cloud storage simplifies the management of evidence that

requires a chain of custody. Cloud storage provides effectively unlimited capacity at relatively low cost, with

built-in logging capabilities that create an audit trail documenting any access. Access controls and retention

policies can restrict access to read-only for authorized personnel and automatically archive or delete data

based on organizational policies.

Cloud providers also offer immutable storage configurations that prevent evidence from being modified or

deleted, even by administrators.  The AWS CLI example in Listing 150 demonstrates how to configure an S3

bucket with Object Lock, which enforces write-once-read-many (WORM) protection on stored evidence.

Listing 150 | Configuring Immutable Forensic Storage on S3

$ aws s3api create-bucket --bucket forensic-evidence-ir2025 --region us-east-1 --object-lock

-enabled-for-bucket 1

$ aws s3api put-object-lock-configuration --bucket forensic-evidence-ir2025 --object-lock

-configuration '{"ObjectLockEnabled": "Enabled", "Rule": {"DefaultRetention": {"Mode":

"COMPLIANCE", "Days": 365}}}' 2

1 Create a new S3 bucket with Object Lock enabled at creation time.

2 Apply a default retention policy in compliance mode, which prevents any user (including root) from deleting or overwriting

objects for 365 days.

Azure Blob Storage offers a similar capability through immutable storage policies, and Google Cloud Storage

supports retention policies with bucket lock. Regardless of the provider, the principle is the same: forensic

evidence should be stored in a way that prevents tampering and provides a verifiable chain of custody.

Network Logging with VPC Flow Logs

VPC flow logs capture metadata about network traffic flowing through cloud network interfaces, without

requiring specialized hardware or packet-capture infrastructure. While flow logs do not capture packet

payloads, they provide valuable context for investigations involving network-based attacks, lateral

movement, or data exfiltration. Each flow log record includes source and destination IP addresses, ports,

protocol, bytes transferred, and an accept or reject action, giving responders enough detail to identify

communication patterns, detect data exfiltration volumes, and confirm whether network isolation controls

are working as intended.

Flow log data can be directed to cloud storage or log analytics services for long-term retention and analysis,

enabling reconstruction of network communication patterns during an investigation. Because flow logs

operate at the network layer, they complement control plane logs by providing visibility into traffic that

cloud management APIs do not capture, such as lateral movement between instances within the same VPC

or outbound connections to attacker-controlled infrastructure.

Containers and Serverless for Forensic Tooling

Even without a fully automated response pipeline, containers and serverless services can accelerate triage

and response. Forensic scripts can be containerized or deployed as serverless functions to gather and

analyze evidence with minimal overhead.

Velociraptor is an open-source endpoint monitoring and digital forensics tool that uses a

lightweight agent to collect artifacts, including file system metadata, running processes,

event logs, and memory from target hosts. It supports real-time hunting queries across

large fleets using its own query language (VQL).

For example, a containerized Velociraptor server can be deployed in minutes to collect endpoint telemetry

from compromised hosts across the environment.  Using a container orchestration service, such as Amazon

ECS, Azure Container Instances, or Google Cloud Run, responders can launch a prebuilt Velociraptor server

image, connect agents to target hosts, and begin collecting artifacts without provisioning or configuring a

dedicated server. When the investigation is complete, the container can be stopped and the collected data

preserved in cloud storage.

Listing 151  demonstrates how to deploy a Velociraptor server on Amazon ECS using the AWS CLI. This

creates a Fargate task that runs the Velociraptor frontend, exposes the GUI and client communication

ports, and stores collected artifacts in an EFS volume.

Listing 151 | Deploying a Velociraptor Server on Amazon ECS

$ aws ecs create-cluster --cluster-name forensics-cluster 1

$ aws ecs register-task-definition --family velociraptor-server --network-mode awsvpc --requires

-compatibilities FARGATE --cpu 2048 --memory 4096 --container-definitions '[{"name":

"velociraptor", "image": "wlambert/velociraptor:latest", "portMappings": [{"containerPort":

8000, "protocol": "tcp"}, {"containerPort": 8001, "protocol": "tcp"}], "mountPoints":

[{"sourceVolume": "velociraptor-data", "containerPath": "/velociraptor"}]}]' --volumes

'[{"name": "velociraptor-data", "efsVolumeConfiguration": {"fileSystemId": "fs-0a1b2c3d4"}}]' 2

$ aws ecs create-service --cluster forensics-cluster --service-name velociraptor --task

-definition velociraptor-server --desired-count 1 --launch-type FARGATE --network-configuration

'{"awsvpcConfiguration": {"subnets": ["subnet-forensics"], "securityGroups": ["sg-

velociraptor"], "assignPublicIp": "DISABLED"}}' 3

1 Create a dedicated ECS cluster for forensic tooling.

2 Register a task definition with the Velociraptor container image, mapping ports 8000 (GUI) and 8001 (client

communication), and attaching an EFS volume for persistent artifact storage.

3 Deploy the service in a private subnet with a security group restricting access to authorized forensic networks.

Azure Container Instances and Google Cloud Run support similar deployments with their respective CLI

tools, following the same pattern of container image, port mapping, and persistent storage configuration.

FINAL CONSIDERATIONS

Cloud incident response is a rapidly evolving discipline, shaped by changes in cloud architecture, attacker

techniques, and available tooling. In this final section, we examine two overarching topics that apply across

the entire response lifecycle: the challenges of multi-cloud environments and the direction cloud incident

response is headed.

Multi-Cloud Environments

One of the most significant complications for cloud incident response is when a multi-cloud architecture is

involved. Many organizations use different cloud providers for different use cases, so an organization may

have resources and users spread across AWS, Azure, and Google Cloud. This complicates investigation and

scoping in two important ways.

First, log centralization becomes even more critical in multi-cloud environments. We have already

recommended centralizing logs into a SIEM regardless of cloud architecture, but operating across multiple

clouds makes this essential. Investigations are significantly slowed when responders need to pivot between

cloud provider consoles, and cross-cloud activity correlation becomes more complex when field names and

log formats differ between providers.

Second, the cloud architecture itself affects scope. If each cloud environment is completely isolated, the

scope of an incident is relatively clear. However, if there is connectivity between clouds, whether through a

shared identity provider, federated authentication, or direct network communication between resources,

the potential for lateral movement exists across cloud boundaries. In this case, understanding how the

clouds connect and whether those connections are in scope is essential for accurate scoping.

Treat cross-cloud identity federation as automatic scope expansion. If an organization

uses a single identity provider (such as Entra ID or Okta) across multiple cloud

environments, a compromised identity in one cloud should be assumed to have potential

access to all federated environments until proven otherwise.

Evolution of Cloud Incident Response

Cloud incident response is changing rapidly, driven by shifts in how organizations use cloud services and

how attackers target them. Several trends are reshaping what responders need to know and what tools they

need to use effectively.

Multi-cloud visibility

As organizations distribute workloads across multiple cloud providers, gaining a unified view of security

posture becomes increasingly difficult.  Cloud Security Posture Management (CSPM) tools address this

challenge by providing centralized visibility into misconfigurations, policy violations, and security risks

across AWS, Azure, Google Cloud, and SaaS platforms from a single interface. For incident responders,

CSPM data can accelerate scoping by quickly identifying which resources are exposed, what permissions

are overly broad, and where misconfigurations may have enabled the attack. Organizations operating in

multi-cloud environments should evaluate CSPM tooling as part of their incident response preparation,

rather than only for preventive security.

AI-driven SOC operations

The application of AI to security operations is moving beyond simple alert correlation. As discussed in

Accelerating Incident Response with AI, AI-driven tools are beginning to perform investigation and response

actions that previously required human analysts. In cloud environments, where API-driven infrastructure

enables automated actions, AI agents can triage alerts, gather context across multiple log sources, and

execute containment actions with minimal human oversight. Cloud-native detection services are also

integrating AI to reduce false positives and surface higher-confidence findings. While these capabilities are

still maturing, organizations should monitor developments in this space and evaluate how AI-assisted

investigation can supplement their cloud response workflows.

Runtime visibility for serverless and containers

Traditional host-based forensics assumes that responders can access a persistent filesystem, memory, and

process list on a compromised system. Serverless functions and ephemeral containers challenge this

assumption. A Lambda function or Cloud Run service may execute for seconds and leave no persistent state

to examine. Container workloads may be destroyed and replaced automatically before responders can

collect evidence.

Runtime security tools that monitor function execution, container behavior, and API calls in real time are

becoming essential for cloud environments that rely on these services. Without runtime visibility,

responders may have no evidence of what happened inside a compromised workload beyond the control

plane logs showing that it executed. Organizations deploying significant serverless or container workloads

should ensure they have monitoring in place that captures runtime behavior in addition to resource

management events.

For serverless and ephemeral container workloads, runtime monitoring is the only source

of evidence about what happened inside the workload. Without it, responders are limited to

control-plane logs that show whether a function executed or a container started, with no

visibility into which code ran, what data was accessed, or which network connections were

made.

Token-based attacks

Cloud and SaaS environments are seeing an increase in token-based attacks relative to traditional password

compromise. Rather than stealing credentials and logging in, attackers are targeting session tokens, OAuth

tokens, and API keys that bypass authentication controls entirely. A stolen session token can grant access

without triggering MFA challenges or appearing as a new login event, making these attacks harder to detect

with traditional authentication monitoring.

This shift has practical implications for detection and response. Organizations should monitor for

anomalous token usage patterns, such as tokens issued from unexpected IP addresses or geographic

locations, tokens with unusually long lifetimes, or token refresh patterns that do not align with normal user

behavior. Conditional access policies that bind tokens to specific devices or network ranges can limit the

value of stolen tokens, and short token lifetimes reduce the window of exposure.

Cloud-native forensics

As discussed in Leveraging the Cloud for Incident Response , organizations are increasingly using cloud

infrastructure itself for forensic analysis, evidence storage, and automated response. This trend is likely to

accelerate as cloud-native tooling matures and as more organizations recognize that the scalability,

accessibility, and auditability of cloud services make them well suited for incident response workloads. The

ability to deploy forensic workstations on demand, store evidence in immutable storage with automatic

chain-of-custody logging, and run automated collection scripts as serverless functions reduces the

overhead of maintaining dedicated forensic infrastructure. For organizations whose production

environments are already in the cloud, using cloud services for incident response is a natural extension that

aligns forensic capabilities with the environment being investigated.
