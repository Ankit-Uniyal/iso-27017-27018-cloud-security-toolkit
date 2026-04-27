# Worked Example Pack — "NorthCloud Services" (NCS)

**Document ID:** CLOUD-WE-PACK-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** Compliance | **Review:** Annual

> *NorthCloud Services (NCS) is a fictional B2B SaaS company illustrating the application of this toolkit. All names, numbers, regions and incidents are illustrative.*

## 1. Company Profile

- **Service:** Multi-tenant SaaS document collaboration platform
- **HQ:** Amsterdam (NL); offices in Dubai (UAE), Bengaluru (IN), Austin (US)
- **Customers:** ~1,200 B2B customers across EU, UAE, India, US
- **CSP estate:** AWS (eu-west-1, eu-central-1, us-east-1, me-central-1) + Azure (centralindia)
- **End-users in customer accounts:** ~3.5 million
- **Role mix:** Processor by default; Controller for own staff/marketing/finance
- **Existing certifications:** ISO 27001:2022 (Year 2 surveillance), SOC 2 Type II (annual)

## 2. SoA Excerpt (illustrative)

| Control | Title | Applicable | Status | Resp. | Evidence |
|---------|-------|:----------:|:------:|:-----:|----------|
| CLD.6.3.1 | Shared roles & resp. | Yes | I | SH | NCS-SRM v3.2; AWS responsibility-model link |
| CLD.8.1.5 | Removal of customer assets | Yes | I | CSP | AWS deletion-API; offboarding playbook |
| CLD.9.5.1 | Tenant segregation | Yes | I | CSP | AWS SOC 2 Type II 2025; tenant-isolation white-paper |
| CLD.12.4.5 | Monitoring of cloud services | Yes | I | SH | CloudTrail → Splunk; Sentinel for Azure |
| A.7.1 | Sub-processor disclosure | Yes | I | CSC | Public sub-processor list; 30-day notice |
| A.8.1 | PII breach notification | Yes | I | CSC | Breach Response v2.1; 24h SLA |
| A.9.1 | Geographical location | Yes | I | CSC | DPA Annex II; product region-pin |
| A.10.6 | Encryption in transit | Yes | I | CSC | TLS 1.3 enforced; HSTS |
| A.11.2 | Return / disposal | Yes | I | CSC | Termination playbook; deletion certificate |

## 3. Cloud Risk Register Entry (sample)

| Field | Value |
|-------|-------|
| Risk ID | NCS-R-CL-04 |
| Description | Cross-border PII transfer non-compliance (EU customer data accessed from India support team) |
| Inherent | High (L=4, I=4) |
| Treatment | Modify |
| Controls | A.9.x; SCCs Module 3; in-product redaction; access-from-EU-only |
| Owner | DPO |
| Target Date | 2026-Q2 |
| Residual | Low (L=2, I=2) |
| Status | In progress |

## 4. Shared Responsibility Matrix (excerpt — IaaS data layer)

| Function | Customer | NCS (Processor) | AWS (CSP) |
|----------|:--------:|:---------------:|:---------:|
| Data classification | ✓ (controller) | Advise | — |
| Encryption-at-rest config | — | ✓ | Provides KMS |
| Key custody | Optional CMK | ✓ (default) | HSM-backed |
| Access reviews | ✓ (their users) | ✓ (admins) | ✓ (CSP staff) |
| Patching OS | — | ✓ | Provides image |
| Hypervisor patching | — | — | ✓ |

## 5. Incident Walkthrough — Token Leak

**Date:** 2026-01-14 03:14 UTC
**Detection:** GuardDuty alert "Anomalous IAM use" → Splunk SOC.
**Initial assessment (T+5min):** Long-lived API key from a leaver's terminal; commits to public GitHub.
**Containment (T+22min):** Key revoked in IAM; affected services restarted.
**Investigation (T+4h):** Forensics confirmed no S3 access; CloudTrail covered.
**Notification:** Internal stakeholders T+1h. No PII impact, no customer notification.
**RCA:** Pre-CI secret-scanning rollout incomplete on a legacy repo.
**Lessons learned:** Mandatory secret-scanning across 100% of repos by 2026-Q2 (CIL-25-006).

## 6. DSR Walkthrough — Erasure

**Date:** 2026-02-03
**Right:** Erasure (Art. 17 GDPR)
**Source:** Direct request to NCS (processor mode) — forwarded to controller.
**Controller decision:** Approved erasure for the data subject across their tenant.
**Execution:** App-level delete; 30-day backup retention; crypto-erase on key rotation.
**Confirmation:** Issued to controller within 25 days; deletion certificate provided.
**Logged in:** DSR Register — DSR-26-018.

## 7. Internal Audit Walkthrough — Q2 Audit (IA-26-02)

**Scope:** Cloud Operations & Shared Resp.; CLD.6.3.1, CLD.9.5.x, A.7.1, A.10.x.
**Findings:**
- 1 Minor NC: 30-day sub-processor notice missed once (NCR-26-002).
- 2 OFIs: harmonise drift-detection across AWS/Azure; tighten DSR SLA reporting cadence.
**Conformity rating:** Substantially conformant.
**Outcomes:** NCR-26-002 closed in Q3 with revised process + reminder automation.

## 8. Cross-Border Transfer Example

**Scenario:** EU customer, end-user data; support team in IN handling tickets containing PII.
**Mechanism:** EU SCCs Module 3 (controller-customer to processor-NCS-EU to sub-processor-NCS-IN).
**TIA outcome:** Adequate with supplementary measures (in-product redaction, no bulk export to IN, IN team uses just-in-time access via VPN with EU egress).
**Documentation:** Transfer-Register entry NCS-XBT-014; reviewed annually.

## 9. Cloud DPIA Example — AI Summariser

**Project:** Document AI summariser using bring-your-own-LLM in customer tenant.
**Trigger:** New technology + customer PII + cross-tenant inference risk.
**Score (dpia_cloud_scorer.py):** 17 → "PROCEED-WITH-MITIGATIONS"
**Mitigations:** Model isolation per tenant; no cross-tenant fine-tuning; explicit customer opt-in; output-redaction; audit log of prompts.
**DPO opinion:** Approved with mitigations and 6-month review.

## 10. KPI Dashboard Snapshot (illustrative)

| KPI | Target | Actual (Q1 2026) |
|-----|--------|:----------------:|
| Cloud SoA implemented | 100% | 96% |
| High/Critical risks treated within SLA | ≥ 95% | 94% |
| DSR SLA adherence | ≥ 99% | 99.6% |
| Phishing-sim click rate | < 5% | 3.1% |
| CSPM critical-finding MTTR | < 14d | 11d |
| Sub-processor reviews up-to-date | 100% | 100% |

## 11. Management Review Decision (excerpt)

- Approve additional FTE in Cloud Security (1.0) to operate CSPM closure within SLA.
- Endorse FedRAMP Moderate exploration for US public-sector pipeline.
- Schedule next surveillance audit Q3.

---
**Document ID:** CLOUD-WE-PACK-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
