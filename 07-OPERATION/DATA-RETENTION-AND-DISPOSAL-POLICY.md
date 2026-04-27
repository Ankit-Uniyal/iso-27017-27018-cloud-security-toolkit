# Cloud Data Retention & Disposal Policy

**Document ID:** CLOUD-RET-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** DPO + CISO | **Review:** Annual

## 1. Purpose

Defines retention periods and secure-disposal practices for data held in cloud services, satisfying ISO/IEC 27001:2022 controls 5.33, 8.10; ISO/IEC 27018 A.4.1, A.10.7, A.11.2; and applicable laws (GDPR Art. 5(1)(e), tax/financial retention, sector regulations).

## 2. Principles

1. PII retained only as long as necessary for the documented purpose.
2. Customer-instructed retention overrides default unless legally prohibited.
3. Backups subject to retention rules with documented restoration constraints.
4. Disposal must be irreversible (crypto-erase, overwrite, or media destruction).
5. Disposal must be evidenced.

## 3. Retention Schedule (illustrative)

| Data Class | Retention | Trigger | Storage Location | Disposal Method |
|------------|-----------|---------|------------------|-----------------|
| Customer end-user account data | Per customer DPA (default 7y after termination) | Contract end + DPA period | Region-pinned RDS/object | Crypto-erase via CMK |
| Customer support tickets (with PII) | 5y | Ticket close | Zendesk + S3 | Sub-processor delete + S3 lifecycle |
| Financial records / invoices | 7-10y (jurisdiction) | Invoice date | Accounting SaaS + S3 | Lifecycle + DPA |
| Tax records | 7-10y | Filing | Accounting SaaS | Lifecycle |
| Employee HR records | 7y after leaver | Termination | Workday | DPA + retention rules |
| Recruitment / candidates | 6 months | Process end | Greenhouse | DPA delete |
| CCTV / physical access logs | 90 days | Capture | Office system (not cloud) | Auto-overwrite |
| Cloud audit logs (CloudTrail/Activity) | 1y hot, 7y cold | Generation | S3 + Glacier | Lifecycle + crypto-erase |
| Application logs (PII-light) | 90 days | Generation | SIEM | Auto-purge |
| Application logs (PII redacted) | 1y | Generation | SIEM | Auto-purge |
| Backups | 35 days incremental, 1y monthly | Snapshot | Cross-region | Lifecycle + crypto-erase |
| DR replicas | Mirror primary lifecycle | Sync | Other region | Crypto-erase |
| Marketing CRM | Until objection | Lead created | Salesforce | DPA delete |
| Cookie / consent logs | 2y | Capture | Consent platform | Auto-purge |
| Security incident records | 7y | Closure | NCR register | Archive |

## 4. Disposal Methods

| Method | Use Case | Evidence |
|--------|----------|----------|
| Cryptographic erasure | Cloud volumes/objects encrypted with CMK; destroy key | KMS audit log |
| Lifecycle policy | Object stores, log archives | S3/Blob lifecycle config |
| API / SaaS delete | Sub-processors with delete API | API response |
| Data-subject right to erasure | Targeted record deletion | DSR ticket |
| Tenant deletion (offboarding) | Whole-customer removal | Deletion certificate |

## 5. Backup & Restore Considerations

- Backups inherit retention rules; PII removal requests in production trigger documented waiver/queue for backup-cycle aging.
- Customers are informed of the backup-cycle delay in DPA Annex.

## 6. Legal Holds

- Legal hold suspends scheduled disposal; tracked in Legal Hold Register.
- Hold released only by Legal counsel.

## 7. Exceptions

Retention beyond schedule must be approved by DPO with documented justification (legal hold, regulatory request).

## 8. Records

- Disposal log (date, dataset, method, evidence)
- Deletion certificates issued to customers on request
- Annual retention-policy compliance audit

## 9. Customer-Visible Documentation

- DPA Annex II
- Trust Centre retention page
- Privacy Notice (where controller)

---
**Document ID:** CLOUD-RET-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
