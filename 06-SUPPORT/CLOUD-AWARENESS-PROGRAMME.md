# Cloud Security & Privacy Awareness Programme

**Standard:** ISO/IEC 27001:2022 (Cl. 7.3) + ISO/IEC 27017:2015 + ISO/IEC 27018:2019
**Document ID:** SUP-AWR-001
**Version:** 1.0
**Classification:** Internal

---

## 1. Purpose
To ensure that every person performing work under the organisation's control — including employees, contractors, third-party administrators and developers — is aware of (a) the Cloud Information Security Policy, (b) their contribution to the Cloud ISMS, (c) the implications of non-conformance and (d) the specific obligations arising from ISO/IEC 27017 and ISO/IEC 27018 when handling cloud services and customer PII.

## 2. Scope
All workforce members, all cloud service consumption (IaaS, PaaS, SaaS), and all roles that access, design, operate, audit or oversee cloud workloads or PII.

## 3. Audience segmentation and minimum content

| Audience | Minimum modules | Frequency |
|---|---|---|
| All staff | Cloud Acceptable Use, phishing, password / MFA hygiene, data classification, incident reporting, PII basics | At onboarding + annual refresher |
| Developers & DevOps | Secure cloud SDLC, secrets management, IaC scanning, OWASP cloud risks, key management | At onboarding + 6-monthly |
| Cloud / Platform engineers | Shared responsibility, network segmentation, IAM hardening, logging, KMS / HSM, backup & DR | At onboarding + 6-monthly |
| Privileged administrators | Just-in-time access, break-glass, privileged session monitoring, change control | Quarterly |
| Data Protection & Legal | DPIA process, cross-border transfers, sub-processor management, DSR handling | Quarterly |
| Auditors & risk team | ISO 27001 / 27017 / 27018 control framework, evidence expectations, sampling | Annual |
| Executives / ISMS Committee | Cloud risk appetite, regulator landscape, incident escalation, metrics | Annual + on-demand |

## 4. Topic catalogue (ISO 27017 + 27018 specific)

1. Shared-responsibility model — who does what across IaaS / PaaS / SaaS.
2. Cloud-specific threats — misconfiguration, exposed storage, identity sprawl, supply-chain.
3. Encryption everywhere — at-rest, in-transit, in-use; customer-managed keys.
4. Secrets and key management — vaults, rotation, no secrets in code.
5. PII lifecycle — collect, use, retain, delete; lawful basis; consent records.
6. Cross-border transfers — SCCs, adequacy, BCRs, transfer impact assessments.
7. Sub-processor governance — onboarding, due diligence, customer notification.
8. DSR handling — access, rectification, erasure, portability; SLAs.
9. Cloud incident response — detection, containment, regulator and customer notification.
10. Logging, monitoring and tamper-evidence in shared environments.
11. Backup, restore and Cloud BCP / DR testing.
12. Personal accountability — disciplinary process for policy violations.

## 5. Delivery channels

- **Mandatory e-learning:** modules with knowledge-check quizzes; minimum 80% pass mark.
- **Targeted workshops:** scenario-based exercises for engineering and DPO teams.
- **Phishing simulations:** monthly with role-aware lures (cloud console, MFA push, supplier impersonation).
- **Tabletop exercises:** quarterly cloud incident scenarios involving CSP, sub-processor or PII breach.
- **Newsletters and bulletins:** monthly cloud threat brief; ad-hoc on emerging issues.
- **Onboarding pack:** Cloud Acceptable Use, ISMS overview, reporting channels.
- **Off-boarding briefing:** confidentiality reminder, IP return, ongoing obligations.

## 6. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Cloud Security Officer (CSO) | Programme owner; approves content; reports KPIs to ISMS Committee |
| HR | Tracks completion at onboarding and annually; integrates with disciplinary process |
| Line managers | Confirm completion before granting cloud access; reinforce expectations |
| Communications team | Delivers bulletins, phishing simulations, awareness campaigns |
| DPO | Owns 27018 / privacy-specific content |
| All staff | Complete training on time; report incidents and concerns |

## 7. KPIs and KRIs

| Indicator | Target | Frequency |
|---|---|---|
| Onboarding training completion within 14 days | >= 98% | Monthly |
| Annual refresher completion | >= 95% | Quarterly |
| Phishing simulation click rate | <= 5% (declining trend) | Monthly |
| Phishing simulation report rate | >= 30% | Monthly |
| Privileged role re-certification | 100% within window | Quarterly |
| Incident-reporting volume | Trending up at maturity | Quarterly |

## 8. Records and evidence

- LMS completion exports (per user, per module, per date).
- Phishing simulation campaign results.
- Tabletop exercise after-action reports.
- Workshop attendance lists.
- Bulletin distribution logs.

Records are retained for a minimum of three years and made available to internal and external auditors.

## 9. Review and continual improvement

- Annual programme review by CSO + DPO + HR.
- Content updated on regulatory change (e.g. new transfer mechanism), incident lessons learned, and threat-intelligence shifts.
- Effectiveness measured against KPIs and through targeted post-training assessments.
- Improvements logged in folder 10 Continual Improvement Log.

## 10. Linked clauses & controls

- ISO/IEC 27001:2022 Clauses 7.2, 7.3, 7.4
- ISO/IEC 27002:2022 controls 6.3 (awareness), 5.4, 5.10, 5.13
- ISO/IEC 27017:2015 cloud-specific awareness obligations
- ISO/IEC 27018:2019 PII-handler awareness and confidentiality

---
**Document ID:** SUP-AWR-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** CSO | **Review:** Annual
