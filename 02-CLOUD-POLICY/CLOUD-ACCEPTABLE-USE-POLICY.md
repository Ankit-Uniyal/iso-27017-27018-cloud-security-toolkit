# Cloud Acceptable Use Policy

**Document ID:** CLOUD-AUP-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CISO | **Review:** Annual

## 1. Purpose & Scope

Defines acceptable use of cloud services and cloud resources by all employees, contractors, interns and any other parties with access to the organisation's cloud accounts. Aligned with ISO/IEC 27002 control 5.10 and the cloud-specific guidance of ISO/IEC 27017.

## 2. General Principles

1. Cloud resources are organisational assets, used solely for legitimate business purposes.
2. Personal data, including PII, must be handled per the Cloud PII Policy and applicable laws.
3. Users access only the cloud resources required for their role (least privilege).
4. All cloud actions are logged; users have no expectation of privacy regarding administrative use.

## 3. Acceptable Uses

- Building, operating and supporting authorised products and services
- Approved research and development within sanctioned accounts
- Standard productivity SaaS use (email, chat, docs) within company tenants

## 4. Prohibited Uses

- Storing or processing personal customer or employee PII outside approved accounts/regions
- Using shared / generic credentials to access cloud consoles
- Disabling or tampering with security tooling (CSPM, EDR, logging agents)
- Mining cryptocurrency on company cloud resources
- Hosting personal projects, websites or media in production cloud accounts
- Sharing cloud credentials, access keys or session tokens
- Bypassing approved networking paths (e.g., personal VPN to access cloud resources)
- Disabling logging, MFA or encryption on any cloud resource
- Using customer PII for development, demo or testing
- Storing secrets in source code or unencrypted in cloud storage
- Using non-approved sub-processors / SaaS without security review

## 5. Identity & Access

- Federated SSO is the only sanctioned authentication path for cloud consoles.
- MFA is mandatory for all cloud-console and privileged access.
- Service accounts and IAM roles must be requested via the standard process and reviewed quarterly.
- Break-glass accounts are restricted, monitored, and may only be used per the documented procedure.

## 6. Data Handling in Cloud

- Classify data per the Asset Classification Schedule.
- Restricted data must be encrypted at rest and in transit.
- Cross-region replication only with documented justification and DPO approval (for PII).
- No printing or local-storage download of customer PII without authorisation.

## 7. Development & Configuration

- Production cloud changes must follow the Change Management Procedure.
- Infrastructure-as-Code is mandatory; click-ops in production is prohibited.
- Public-facing buckets, databases and admin consoles are forbidden unless explicitly approved.
- Branch-protection, code review and security gates apply to all IaC and application code.

## 8. Monitoring & Investigations

- All cloud actions are logged in the central log archive.
- The organisation may inspect any cloud activity for security or compliance reasons.
- Suspected misuse should be reported via the Security Incident channel.

## 9. Sanctions

Violations may result in disciplinary action up to and including termination, and may result in civil or criminal liability under applicable law.

## 10. Acknowledgement

All personnel acknowledge this policy at onboarding and annually thereafter via the awareness platform.

---
**Document ID:** CLOUD-AUP-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
