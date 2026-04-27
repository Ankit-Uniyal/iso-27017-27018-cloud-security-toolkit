# Worked Example — Nexus Cloud Services Ltd (NCS)

**Document ID:** CLOUD-WE-001 | **Version:** 1.0 | **Classification:** Public — fictional reference only

> Disclaimer: NCS is a fictional organisation used solely to demonstrate completed templates. Replace with your own data before use.

## Organisation Profile
- Name: Nexus Cloud Services Ltd (NCS)
- Sector: Multi-tenant SaaS HR platform serving GCC clients
- HQ: Dubai, UAE
- Cloud role: CSP for the HR SaaS; CSC for productivity, observability, IdP

## Cloud Services in Scope (extract)

| Service | Type | Role | PII? | Region |
|---------|------|------|------|--------|
| NCS HR SaaS | SaaS | CSP | Yes | UAE-North, EU-West |
| Hyperscaler IaaS | IaaS | CSC | Yes | UAE-North, EU-West |
| Productivity suite | SaaS | CSC | Limited | EU-West |

## Top Cloud Risks (excerpt)
1. Mis-configured tenant storage (CR-001) — score 20 — CSPM auto-remediation
2. Sub-processor flow-down failure (CR-003) — score 15 — annual audits
3. Cloud admin identity compromise (CR-012) — score 15 — MFA + PAM + JIT

## Sample SoA Excerpt

| Control | Status | Owner | Evidence |
|---------|--------|-------|----------|
| CLD.6.3.1 | Implemented | Cloud Architect | SRM v2 signed Q1-2026 |
| CLD.8.1.5 | Implemented | Service Owner | Termination procedure ENG-PR-031 |
| CLD.9.5.1 | Implemented | Platform Eng | Tenant isolation design v3 |
| CLD.12.4.5 | Partial | SOC | Tenant log export GA Q3-2026 |
| ISO 27018 A.2 | Implemented | DPO | Marketing exclusion control |
| ISO 27018 A.16 | Implemented | DPO | IR-PR-007 with 24-hour CSC notification |

## Sample Breach Log Entry

| Field | Value |
|-------|-------|
| Incident ID | NCS-IR-2026-014 |
| Date | 2026-03-12 |
| Type | Mis-configured tenant storage exposure |
| Affected | 1 tenant, ~ 4,200 employee records |
| PII categories | Names, work email, employee ID |
| Containment | Re-private bucket, rotated credentials |
| CSC notification | 6 hours (beat 24-hour SLA) |
| Root cause | IaC drift + missing policy gate |
| Corrective action | Add policy-as-code gate; CSPM auto-remediation |

---

*Owner: GRC Lead | Educational reference only*
