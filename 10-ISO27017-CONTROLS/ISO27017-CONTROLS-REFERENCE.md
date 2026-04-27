# ISO/IEC 27017:2015 — Cloud Security Controls Reference

**Document ID:** CLOUD-27017-REF-001 | **Version:** 2.0 | **Classification:** Internal | **Owner:** Cloud Security Officer | **Review:** Annual

## 1. Purpose

This document provides the authoritative reference for all controls in ISO/IEC 27017:2015 — the *Code of practice for information security controls based on ISO/IEC 27002 for cloud services*. It contains:

- All 7 cloud-extended (**CLD**) controls with full guidance
- Cloud-specific implementation guidance for the relevant ISO/IEC 27002 controls
- Responsibility split between Cloud Service Provider (CSP) and Cloud Service Customer (CSC)
- Evidence and audit-test guidance

## 2. Cloud-Extended Controls (CLD.x)

### CLD.6.3.1 — Shared roles and responsibilities within a cloud computing environment

**Objective:** Ensure roles and responsibilities for both the cloud service customer and the cloud service provider are agreed, documented and communicated.

**CSP responsibilities:** Document and publish the cloud service shared responsibility model; provide a customer-facing matrix per service tier (IaaS/PaaS/SaaS); communicate changes via formal change-notice channels.

**CSC responsibilities:** Review the CSP shared-responsibility model; map to internal RACI; document residual obligations in the Shared Responsibility Matrix; verify alignment annually.

**Evidence:** Shared Responsibility Matrix (07-OPERATION/); MSA / DPA clauses; CSP attestations.

**Audit tests:** Verify presence of approved matrix; sample 5 controls and confirm responsibility assignment matches CSP documentation; confirm review evidence within last 12 months.

---

### CLD.8.1.5 — Removal of cloud service customer assets

**Objective:** Assets of the cloud service customer that are on the cloud service provider's premises should be removed, and returned if necessary, in a timely manner upon termination of the cloud service agreement.

**CSP responsibilities:** Provide documented data-deletion procedure; offer customer-triggered deletion API; issue deletion certificate on request; ensure deletion within contractually agreed window.

**CSC responsibilities:** Maintain offboarding checklist; trigger deletion or export at termination; obtain and retain deletion certificate as evidence.

**Evidence:** CSP data-deletion procedure; offboarding checklist; deletion certificates.

**Audit tests:** Inspect last termination event; verify deletion confirmation received within SLA.

---

### CLD.9.5.1 — Segregation in virtual computing environments

**Objective:** A cloud service customer's virtual environment running on a cloud service should be protected from other cloud service customers and unauthorised persons.

**CSP responsibilities:** Implement multi-tenant isolation (hypervisor, network, storage); maintain SOC 2 / ISO 27001 attestation covering isolation controls; publish architectural whitepaper.

**CSC responsibilities:** Review CSP isolation evidence; configure tenant-level controls (VPC, IAM, encryption keys) to reinforce segregation.

**Evidence:** CSP attestations (SOC 2 Type II, ISO 27001 SoA), architectural diagrams.

**Audit tests:** Confirm valid CSP attestation report; review tenant-isolation configuration in customer account.

---

### CLD.9.5.2 — Virtual machine hardening

**Objective:** Virtual machines in a cloud computing environment should be hardened to meet business needs.

**CSP responsibilities:** Provide hardened base images; publish hardening guidance per OS.

**CSC responsibilities:** Use approved hardened images (CIS-benchmark or equivalent); enforce baseline via configuration management; scan for drift.

**Evidence:** Image catalogue; hardening baseline document; drift-detection report.

**Audit tests:** Sample 5 VMs and confirm baseline compliance; verify CIS benchmark scan results within 30 days.

---

### CLD.12.1.5 — Administrator's operational security

**Objective:** Procedures for administrative operations of a cloud computing environment should be defined, documented and monitored.

**CSP responsibilities:** Define admin procedures; restrict admin access; log all admin operations.

**CSC responsibilities:** Implement Privileged Access Management (PAM); enforce just-in-time access; document break-glass procedures; review admin activity quarterly.

**Evidence:** PAM tool reports; break-glass procedure; admin activity log review records.

**Audit tests:** Confirm all admin sessions logged; verify last quarterly review; test break-glass procedure end-to-end.

---

### CLD.12.4.5 — Monitoring of cloud services

**Objective:** The cloud service customer should have the capability to monitor specified aspects of the operation of the cloud services that the cloud service customer uses.

**CSP responsibilities:** Expose service health, audit and usage telemetry via APIs (e.g., CloudTrail, Activity Log, Audit Logs); publish status dashboard.

**CSC responsibilities:** Forward telemetry to SIEM; define alerting rules; maintain monitoring runbook.

**Evidence:** SIEM dashboards; alert catalogue; runbook.

**Audit tests:** Confirm telemetry ingest is current; review last 5 alerts and response evidence.

---

### CLD.13.1.4 — Alignment of security management for virtual and physical networks

**Objective:** Upon configuration of virtual networks, consistency of configurations between virtual and physical networks should be verified.

**CSP responsibilities:** Provide VNet/VPC primitives and security groups; publish network-architecture best practices.

**CSC responsibilities:** Maintain authoritative network architecture diagram; baseline security groups; review flow logs; align to physical-network policy.

**Evidence:** Network architecture diagram; SG/NSG baseline; flow-log review records.

**Audit tests:** Compare deployed network to baseline; sample 3 SG rules and confirm justification.

## 3. Cloud Guidance on ISO/IEC 27002 Controls

The table below summarises cloud-specific implementation guidance from ISO/IEC 27017 for the most-impacted ISO/IEC 27002 controls. (Full SoA mapping in 05-PLANNING/STATEMENT-OF-APPLICABILITY.md.)

| 27002 | Title | Cloud-Specific Guidance | Responsibility |
|-------|-------|-------------------------|:--------------:|
| 5.10 | Acceptable use | Define rules for cloud-resource provisioning and consumption | CSC |
| 5.14 | Information transfer | Encrypt all data in transit (TLS 1.2+); validate certificates | SH |
| 5.15 | Access control | Federate identity to corporate IdP; enforce least privilege | CSC |
| 5.17 | Authentication information | MFA mandatory; secrets in vault; rotate keys | CSC |
| 5.19 | Supplier relationships | Assess CSP via Cloud Assurance Questionnaire | CSC |
| 5.20 | Supplier agreements | Cloud DPA with explicit responsibility split | CSC |
| 5.23 | Use of cloud services | Cloud Security Policy + provider-selection criteria | CSC |
| 5.24–5.27 | Incident management | IR runbooks integrated with CSP support channels | SH |
| 5.30 | ICT continuity | Multi-AZ / multi-region; tested DR | SH |
| 5.34 | Privacy / PII | Implement 27018 controls (see 11-) | SH |
| 8.1 | Endpoint devices | MDM enrolment for any endpoint with cloud admin access | CSC |
| 8.2 | Privileged access | PAM + just-in-time | CSC |
| 8.5 | Secure authentication | MFA + WebAuthn / FIDO2 where available | CSC |
| 8.7 | Anti-malware | EDR + container/image scanning | SH |
| 8.8 | Vulnerability management | Cloud-native scanning (e.g., Inspector, Defender) + SLA | SH |
| 8.9 | Configuration management | Infrastructure-as-Code with drift detection | CSC |
| 8.10 | Information deletion | Crypto-erase + CSP delete API | SH |
| 8.12 | DLP | Egress controls; tenant-level DLP | CSC |
| 8.13 | Backup | Cross-region backups; immutable snapshots | SH |
| 8.15 | Logging | Centralised log archive ≥ 1 year | SH |
| 8.16 | Monitoring | SIEM + UEBA, CSP audit logs | SH |
| 8.20–8.23 | Network security | Segmentation, private endpoints, web filtering | SH |
| 8.24 | Cryptography | KMS with documented key policy; CMK preferred | SH |
| 8.25–8.29 | Secure development | SSDLC, SAST/DAST, threat modelling, security gates in CI | CSC |
| 8.31 | Environment separation | Separate cloud accounts/subscriptions per environment | CSC |

## 4. Audit Trail Mapping

| CLD Control | SoA Row | KPI Metric | Worked-Example Artifact |
|-------------|---------|------------|-------------------------|
| CLD.6.3.1 | Row 1 | Shared-responsibility review % | Shared Responsibility Matrix |
| CLD.8.1.5 | Row 2 | Termination deletions on time % | Offboarding checklist |
| CLD.9.5.1 | Row 3 | CSP attestation currency | Architectural diagram |
| CLD.9.5.2 | Row 4 | VM hardening compliance % | CIS scan report |
| CLD.12.1.5 | Row 5 | Admin sessions via PAM % | PAM report |
| CLD.12.4.5 | Row 6 | SIEM ingest health % | SIEM dashboard |
| CLD.13.1.4 | Row 7 | Network drift findings | Network diagram |

---
**Document ID:** CLOUD-27017-REF-001 | **Version:** 2.0 | **Classification:** Internal | **Next Review:** Annual
