# Cloud Data Subject Rights (DSR) Procedure

**Document ID:** CLOUD-DSR-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** DPO | **Review:** Annual

## 1. Purpose

Defines the end-to-end process for handling data-subject rights requests in cloud-based services, satisfying ISO/IEC 27018 A.1.1, GDPR Arts. 12-22, UAE PDPL Arts. 13-19, India DPDPA Ch. III, and equivalent laws.

## 2. Rights in Scope

| Right | Source | SLA (default) |
|-------|--------|---------------|
| Information / transparency | GDPR 13/14 | At collection |
| Access | GDPR 15, PDPL, DPDPA | 30 days (extendable +60) |
| Rectification | GDPR 16 | 30 days |
| Erasure ("right to be forgotten") | GDPR 17 | 30 days |
| Restriction of processing | GDPR 18 | 30 days |
| Portability | GDPR 20 | 30 days |
| Objection | GDPR 21 | 30 days |
| Automated decision review | GDPR 22 | 30 days |
| Withdrawal of consent | GDPR 7(3) | Immediate effect |

## 3. Roles

| Role | Responsibility |
|------|----------------|
| DSR Intake Team | Receive request, verify identity, log |
| DPO | Oversight, decisions on complex / refusal |
| Engineering | Execute technical access/erasure/portability |
| Customer Success (processor mode) | Liaise with customer-controller |
| Legal | Refusal grounds, regulator referrals |

## 4. Process

### 4.1 Controller mode (we hold our own customers' / employees' PII)

1. **Intake** via privacy@org or DSR portal (web form).
2. **Identity verification** — proportionate to sensitivity.
3. **Acknowledgement** within 72h.
4. **Triage** — determine right(s) requested, scope, complexity.
5. **Fulfilment** — execute technical retrieval/erasure/export.
6. **Quality check** — DPO review of response packet.
7. **Response** delivered within SLA.
8. **Closure & log** — entry in DSR register.

### 4.2 Processor mode (we host PII on behalf of customer-controllers)

1. Forward DSR received directly from data subject to the controller-customer (do not action without instruction).
2. Provide controller with the **technical means** to fulfil DSR (API, export, delete).
3. Execute on customer instruction within agreed SLA.
4. Confirm completion to customer.
5. Log all actions for audit.

## 5. Identity Verification

| Risk Level | Verification Method |
|------------|---------------------|
| Low (anonymised request) | Email confirmation |
| Medium (account-linked) | Logged-in session or 2-factor email |
| High (sensitive PII / large volume) | Government ID + signed declaration |

## 6. Refusals & Restrictions

DSRs may be refused/restricted where:
- Manifestly unfounded or excessive (e.g., repetitive)
- Exemption applies (legal claims, freedom of expression, public interest)
- Request would adversely affect another's rights

Refusals must be documented, reasoned, with appeal/regulator-complaint information.

## 7. Cloud-Specific Execution Patterns

| Right | Cloud Pattern |
|-------|---------------|
| Access | Aggregate from primary DB + warehouse + log archive (PII-redacted) |
| Erasure | Application delete → backup-cycle waiting period notice → crypto-erase on key rotation |
| Portability | Export in machine-readable format (JSON / CSV) via tooling |
| Restriction | Tag PII record with restriction flag → enforce in app + queries |
| Objection | Update marketing-suppression list across tenants |

## 8. Backups & DSR

- Backup-aging delay communicated to data subject (typically 30-60 days).
- Restorations after backup aging must NOT re-introduce erased PII (verify with post-restore DSR re-execution).

## 9. SLAs & KPIs

- Acknowledgement < 72h: target 100%
- Response within statutory SLA: target ≥ 99%
- DPO review of all responses: 100%

## 10. Records

DSR Register entries retained 6 years post-closure.

---
**Document ID:** CLOUD-DSR-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
