# Cross-Border PII Transfer Procedure (Cloud)

**Document ID:** CLOUD-XBT-001 | **Version:** 1.0 | **Classification:** Internal | **Owner:** DPO | **Review:** Annual

## 1. Purpose

This procedure governs every cross-border transfer of PII processed in the cloud, satisfying ISO/IEC 27018 A.9.1, A.9.2, A.11.1 and applicable laws (GDPR Chapter V, UK GDPR, UAE PDPL Art. 22-23, India DPDPA s.16, KSA PDPL Art. 29, etc.).

## 2. Definitions

- **Cross-border transfer:** Any operation that makes PII accessible to, stored in, or processed from a country other than the country of origin.
- **Adequacy:** A formal determination by the originating jurisdiction that a destination country provides equivalent protection.
- **SCCs:** Standard Contractual Clauses (e.g., EU SCCs 2021).
- **TIA:** Transfer Impact Assessment.

## 3. Scope

Applies whenever PII processed by the organisation (as controller or processor) crosses a border, including:
- Storage in a non-origin region
- Replication / backup to other regions
- Sub-processor access from another country
- Support / engineering follow-the-sun access
- Analytics / telemetry exports

## 4. Decision Tree

```
Is PII leaving origin country?
  No → No XBT controls needed; document for completeness.
  Yes → Is destination adequate (per origin)?
    Yes → Document basis (adequacy decision); proceed.
    No  → Apply transfer mechanism + TIA.
```

## 5. Approved Transfer Mechanisms

| Origin → Destination | Mechanism | Owner |
|----------------------|-----------|-------|
| EU/EEA → adequate (UK, CH, etc.) | Adequacy decision | DPO |
| EU/EEA → US | EU-US DPF (where certified) or SCCs + TIA | DPO |
| EU/EEA → other | EU SCCs (2021) + TIA + supplementary measures | DPO |
| UK → non-adequate | UK IDTA or Addendum to SCCs + TIA | DPO |
| Switzerland → non-adequate | CH SCCs + TIA | DPO |
| UAE → outside | UAE PDPL transfer mechanisms (consent, contract, regulator approval) | DPO |
| India → outside | DPDPA notified-country list / restrictions | DPO |
| KSA → outside | NDMO/SDAIA approval where required | DPO |

## 6. Transfer Impact Assessment (TIA)

The TIA must consider:

1. **Nature of PII** — sensitivity, volume, categories, special categories
2. **Destination law** — government access powers, surveillance regime
3. **Recipient profile** — risk of compelled disclosure
4. **Technical & organisational measures** — encryption, key custody, pseudonymisation
5. **Contractual measures** — SCC clauses, indemnities, transparency reports
6. **Supplementary measures** — customer-managed keys, in-region key custody, split keys, BYOK/HYOK, redaction

A TIA is documented per transfer scenario and reviewed annually or on legal-environment change.

## 7. Operational Controls

- **Region pinning:** product configuration prevents data leaving origin region without explicit override.
- **Customer-Managed Keys (CMK):** keys held in origin-region KMS; envelope encryption at rest.
- **Logging:** every cross-region replication event logged in audit trail.
- **Sub-processor controls:** sub-processor list flags any sub-processor outside origin region with linked transfer mechanism.

## 8. Records

For each transfer scenario, maintain:

- Transfer Register entry (origin, destination, mechanism, TIA reference, date, owner)
- Signed SCCs / IDTA / equivalent
- TIA document
- Customer DPA reference (if processor)

## 9. Customer-Facing Disclosure

- Sub-processor list discloses location.
- DPA Annex II lists countries of processing.
- Privacy Notice (where controller) discloses transfer countries and mechanisms.

## 10. Roles

| Role | Responsibility |
|------|----------------|
| DPO | Owns this procedure; approves all TIAs |
| Legal | Reviews SCCs/IDTAs; tracks legal changes |
| CSO | Implements technical region-pinning + CMK |
| Procurement | Surfaces sub-processor changes |
| Engineering | Designs region-aware data architecture |

## 11. Annual Review

DPO reviews:
- All transfer-mechanism documents
- TIAs (refresh on legal change)
- Sub-processor list
- Customer-disclosure currency

---
**Document ID:** CLOUD-XBT-001 | **Version:** 1.0 | **Classification:** Internal | **Next Review:** Annual
