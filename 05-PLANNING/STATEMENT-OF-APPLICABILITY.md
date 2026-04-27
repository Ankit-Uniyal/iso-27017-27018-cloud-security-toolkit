# Statement of Applicability — ISO/IEC 27017 + ISO/IEC 27018

**Document ID:** CLOUD-SOA-001 | **Version:** 2.0 | **Classification:** Internal | **Owner:** CISO / Cloud Security Officer | **Review:** Annual

## 1. Purpose

This Statement of Applicability (SoA) records the applicability, implementation status, and justification for every control under ISO/IEC 27017:2015 (Cloud Security) and ISO/IEC 27018:2019 (PII protection in public clouds). It supplements the organisation's base ISO/IEC 27001:2022 / 27002:2022 SoA and is mandatory evidence for certification.

## 2. Status Legend

| Code | Meaning |
|------|---------|
| I | Implemented |
| P | Partially implemented |
| N | Not implemented |
| NA | Not applicable (justification required) |
| CSP | Inherited from Cloud Service Provider |
| CSC | Customer responsibility |
| SH | Shared responsibility |

## 3. ISO/IEC 27017 — Cloud-Extended Controls (CLD.x)

| Control | Title | Applicable | Status | Responsibility | Justification / Evidence |
|---------|-------|:----------:|:------:|:--------------:|--------------------------|
| CLD.6.3.1 | Shared roles and responsibilities within a cloud computing environment | Yes | I | SH | Shared Responsibility Matrix (07-OPERATION); contractual roles in MSA |
| CLD.8.1.5 | Removal of cloud service customer assets | Yes | I | CSP | Data deletion procedure; CSP attestation; offboarding checklist |
| CLD.9.5.1 | Segregation in virtual computing environments | Yes | I | CSP | VPC/tenant isolation; CSP SOC 2 report |
| CLD.9.5.2 | Virtual machine hardening | Yes | I | SH | CIS-benchmarked AMIs; hardening baselines |
| CLD.12.1.5 | Administrator's operational security | Yes | I | SH | PAM; break-glass procedures; admin activity logs |
| CLD.12.4.5 | Monitoring of cloud services | Yes | I | SH | CloudTrail / Activity Log forwarded to SIEM; alerting runbook |
| CLD.13.1.4 | Alignment of security management for virtual and physical networks | Yes | I | SH | Network architecture diagram; NSG/SG baseline; flow-log review |

## 4. ISO/IEC 27017 — Cloud Guidance on ISO/IEC 27002 Controls (selected)

| Control | Title | Applicable | Status | Responsibility | Cloud-Specific Notes |
|---------|-------|:----------:|:------:|:--------------:|----------------------|
| 5.1 | Policies for information security | Yes | I | CSC | Cloud Security Policy (02-CLOUD-POLICY) |
| 5.10 | Acceptable use of information and other associated assets | Yes | I | CSC | Cloud Acceptable Use Policy |
| 5.14 | Information transfer | Yes | I | SH | TLS 1.2+, encrypted channels |
| 5.15 | Access control | Yes | I | SH | RBAC + IdP federation |
| 5.16 | Identity management | Yes | I | CSC | SSO; lifecycle automation |
| 5.17 | Authentication information | Yes | I | CSC | MFA enforced; secrets manager |
| 5.18 | Access rights | Yes | I | CSC | JML; quarterly access reviews |
| 5.19 | Information security in supplier relationships | Yes | I | CSC | Supplier Cloud Assurance Questionnaire (15-) |
| 5.20 | Addressing information security in supplier agreements | Yes | I | CSC | Cloud DPA; MSA security schedule |
| 5.21 | Managing IS in the ICT supply chain | Yes | I | CSC | 4th-party assessment process |
| 5.22 | Monitoring, review and change management of supplier services | Yes | I | CSC | Annual SOC2/ISO review |
| 5.23 | Information security for use of cloud services | Yes | I | CSC | Cloud Security Policy section 6 |
| 5.24 | IS incident management planning and preparation | Yes | I | SH | Cloud Breach Response Procedure |
| 5.25 | Assessment and decision on information security events | Yes | I | SH | SOC triage runbook |
| 5.26 | Response to information security incidents | Yes | I | SH | IR playbooks |
| 5.27 | Learning from information security incidents | Yes | I | CSC | Post-incident review template |
| 5.28 | Collection of evidence | Yes | I | SH | Forensic chain-of-custody procedure |
| 5.29 | IS during disruption | Yes | I | SH | Multi-AZ + DR plan |
| 5.30 | ICT readiness for business continuity | Yes | I | SH | DR test results |
| 5.31 | Legal, statutory, regulatory and contractual requirements | Yes | I | CSC | Legal/Regulatory Register (03-) |
| 5.32 | Intellectual property rights | Yes | I | CSC | OSS licence policy |
| 5.33 | Protection of records | Yes | I | SH | Immutable storage; retention rules |
| 5.34 | Privacy and protection of PII | Yes | I | SH | Cloud PII Policy + 27018 controls |
| 5.35 | Independent review of information security | Yes | I | CSC | Annual external audit |
| 5.36 | Compliance with policies, rules and standards for IS | Yes | I | CSC | Compliance dashboard |
| 5.37 | Documented operating procedures | Yes | I | CSC | Runbook library |
| 6.1–6.8 | People controls | Yes | I | CSC | HR policies + onboarding/offboarding |
| 7.1–7.14 | Physical controls | Yes | NA/CSP | CSP | Inherited from CSP (SOC2 / ISO27001 attest.) |
| 8.1 | User endpoint devices | Yes | I | CSC | MDM; disk encryption |
| 8.2 | Privileged access rights | Yes | I | CSC | PAM; just-in-time access |
| 8.3 | Information access restriction | Yes | I | SH | IAM policies |
| 8.5 | Secure authentication | Yes | I | CSC | MFA + WebAuthn |
| 8.6 | Capacity management | Yes | I | SH | Auto-scaling; cost/perf monitoring |
| 8.7 | Protection against malware | Yes | I | SH | EDR + container scanning |
| 8.8 | Management of technical vulnerabilities | Yes | I | SH | Vuln scanner + patch SLA |
| 8.9 | Configuration management | Yes | I | CSC | IaC + drift detection |
| 8.10 | Information deletion | Yes | I | SH | Crypto-erase; CSP delete API |
| 8.11 | Data masking | Yes | P | CSC | Tokenisation in non-prod |
| 8.12 | Data leakage prevention | Yes | I | CSC | DLP rules; egress controls |
| 8.13 | Information backup | Yes | I | SH | Cross-region backups; restore tests |
| 8.14 | Redundancy of information processing facilities | Yes | I | CSP | Multi-AZ; CSP attestations |
| 8.15 | Logging | Yes | I | SH | Centralised logging; 1y retention |
| 8.16 | Monitoring activities | Yes | I | SH | SIEM + UEBA |
| 8.17 | Clock synchronisation | Yes | I | CSP | NTP via CSP |
| 8.18 | Use of privileged utility programs | Yes | I | CSC | Restricted via PAM |
| 8.19 | Installation of software on operational systems | Yes | I | CSC | Allowlist + change control |
| 8.20 | Networks security | Yes | I | SH | NSG/SG baseline + flow logs |
| 8.21 | Security of network services | Yes | I | SH | Private endpoints; TLS |
| 8.22 | Segregation of networks | Yes | I | CSC | VPC + subnet design |
| 8.23 | Web filtering | Yes | I | CSC | Egress proxy / DNS filter |
| 8.24 | Use of cryptography | Yes | I | SH | KMS + key policy doc |
| 8.25 | Secure development life cycle | Yes | I | CSC | SSDLC policy + SAST/DAST |
| 8.26 | Application security requirements | Yes | I | CSC | Threat models; ASVS |
| 8.27 | Secure system architecture and engineering principles | Yes | I | CSC | Architecture review board |
| 8.28 | Secure coding | Yes | I | CSC | Coding standards + reviews |
| 8.29 | Security testing in development and acceptance | Yes | I | CSC | CI security gates |
| 8.30 | Outsourced development | Yes | NA | CSC | No outsourced dev currently |
| 8.31 | Separation of dev, test and production environments | Yes | I | CSC | Account/subscription separation |
| 8.32 | Change management | Yes | I | CSC | Change advisory board |
| 8.33 | Test information | Yes | I | CSC | No prod data in non-prod |
| 8.34 | Protection of information systems during audit testing | Yes | I | CSC | Read-only auditor accounts |

## 5. ISO/IEC 27018 — PII Protection in Public Clouds (Annex A)

| Control | Title | Applicable | Status | Responsibility | Justification / Evidence |
|---------|-------|:----------:|:------:|:--------------:|--------------------------|
| A.1.1 | Consent and choice — Obligation to co-operate regarding PII principals' rights | Yes | I | CSC (as processor) | DSR procedure; SLA |
| A.2.1 | Purpose legitimacy — Public cloud PII processor's purpose | Yes | I | CSC | DPA Schedule of Processing |
| A.2.2 | Public cloud PII processor's commercial use | Yes | I | CSC | DPA — no secondary use |
| A.3.1 | Collection limitation | Yes | I | CSC | Data minimisation policy |
| A.4.1 | Data minimisation — Secure erasure of temporary files | Yes | I | CSC | Auto-cleanup of temp objects |
| A.5.1 | Use, retention and disclosure limitation — PII disclosure notification | Yes | I | CSC | Disclosure log; legal review |
| A.5.2 | Recording of PII disclosures | Yes | I | CSC | Disclosure register |
| A.6.1 | Accuracy and quality | Yes | I | CSC | Data quality SLAs |
| A.7.1 | Openness, transparency and notice — Disclosure of sub-contracted PII processing | Yes | I | CSC | Sub-processor list + 30-day notice |
| A.8.1 | Individual participation and access — Notification of a data breach involving PII | Yes | I | CSC | 72-hour notification SLA |
| A.9.1 | Accountability — Geographical location of PII | Yes | I | CSC | Region pinning + DPA Annex II |
| A.9.2 | Intended destination of PII | Yes | I | CSC | Cross-border transfer procedure |
| A.10.1 | Information security — Confidentiality or non-disclosure agreements | Yes | I | CSC | NDA programme |
| A.10.2 | Restriction of the creation of hardcopy material | Yes | I | CSC | Print-restriction policy |
| A.10.3 | Control and logging of data restoration | Yes | I | CSC | Restore audit log |
| A.10.4 | Protecting data on storage media leaving the premises | Yes | NA/CSP | CSP | Inherited from CSP |
| A.10.5 | Use of unencrypted portable storage media and devices | Yes | I | CSC | USB block via MDM |
| A.10.6 | Encryption of PII transmitted over public data-transmission networks | Yes | I | SH | TLS 1.2+; HSTS |
| A.10.7 | Secure disposal of hardcopy materials | Yes | I | CSC | Shred policy |
| A.10.8 | Unique use of user IDs | Yes | I | CSC | No shared accounts |
| A.10.9 | Records of authorised users | Yes | I | CSC | IAM register |
| A.10.10 | User ID management | Yes | I | CSC | JML automation |
| A.10.11 | Contract measures | Yes | I | CSC | DPA + MSA |
| A.10.12 | Sub-contracted PII processing | Yes | I | CSC | Sub-processor due diligence |
| A.10.13 | Access to data on pre-used data storage space | Yes | I | CSP | Storage zeroisation by CSP |
| A.11.1 | Privacy compliance — Geographical location of PII | Yes | I | CSC | DPA Annex II |
| A.11.2 | Return, transfer and disposal of PII | Yes | I | CSC | Termination procedure |

## 6. Approval

| Role | Name | Signature | Date |
|------|------|-----------|------|
| CISO / Cloud Security Officer | | | |
| Data Protection Officer | | | |
| CTO | | | |

---
**Document ID:** CLOUD-SOA-001 | **Version:** 2.0 | **Classification:** Internal | **Next Review:** Annual
