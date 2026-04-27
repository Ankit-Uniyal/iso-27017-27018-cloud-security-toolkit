# Cloud Breach Response Procedure (ISO 27017 / ISO 27018)

**Document ID:** CLOUD-BR-001 | **Version:** 1.0 | **Classification:** Internal

## 1. Purpose

Defines how cloud-related security and PII breaches are detected, contained, notified and recovered, including the ISO 27018 obligation to notify the CSC.

## 2. Scope
- Incidents in CSP-operated infrastructure that affect CSC tenants.
- Incidents in CSC-operated cloud workloads.
- Sub-processor incidents that flow up to the CSP.

## 3. Phases

### 3.1 Detect
Sources: SIEM alerts, CSPM findings, CSP advisories, customer reports, threat intel, audit logs (CLD.12.4.5).

### 3.2 Triage
Confirm scope, services, regions, tenants, data classes (PII?), severity. Severity matrix: P1 confirmed PII breach or major outage; P2 confirmed exposure limited; P3 attempted only.

### 3.3 Contain
Isolate workloads, revoke compromised credentials, rotate keys, block sub-processors as needed.

### 3.4 Notify

| Audience | Trigger | Target SLA |
|----------|---------|------------|
| Internal IR / Crisis | P1/P2 | Immediate |
| DPO | Any PII breach | Immediate |
| CSC (when org is CSP) | Confirmed CSC-impacting breach | 24–72 hours per contract (ISO 27018 A.8) |
| Regulators (controller) | PII breach meeting threshold | 72 hours (GDPR Art. 33), per UAE PDPL etc. |
| Data subjects | High-risk breach | Without undue delay |
| Sub-processors | If they need to act | Immediately |

### 3.5 Eradicate & Recover
Patch, restore, validate, sign-off return to BAU.

### 3.6 Post-Incident Review
Lessons learned, NCR if needed, control updates, evidence retained for audit.

## 4. CSC Notification Content (ISO 27018 A.8)
- Nature of the breach and PII categories affected
- Likely consequences and approximate number of records
- Containment and remediation steps taken
- Contact point at CSP (DPO / IR Lead)
- Information needed by CSC to discharge controller obligations

## 5. Records and Evidence
- Incident ticket, communications log, CSC notification copy, regulator submission, post-mortem.

---

*Owner: CISO (lead) + DPO (PII) | Review cycle: Annual + post-incident*
