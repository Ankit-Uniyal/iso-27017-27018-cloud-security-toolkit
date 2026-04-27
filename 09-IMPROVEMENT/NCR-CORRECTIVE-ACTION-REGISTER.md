# Cloud Nonconformity & Corrective Action Register

**Document ID:** CLOUD-NCR-001 | **Version:** 1.0 | **Classification:** Internal

| NCR ID | Source | Date | Description | Clause / Control | Root Cause | Containment | Corrective Action | Owner | Target Date | Status |
|--------|--------|------|-------------|------------------|-----------|-------------|-------------------|-------|-------------|--------|
| NCR-001 | Internal Audit | | Sub-processor list not updated | ISO 27018 A.3 | Process gap | Notify CSC | Update register + automate | DPO | | Open |
| NCR-002 | CSPM finding | | S3 bucket public-read in dev | ISO 27017 5.10 | No IaC guardrail | Re-private + alerting | Add IaC policy gate | Cloud Architect | | Open |
| NCR-003 | Customer audit | | Logs not exposed at tenant level | CLD.12.4.5 | CSP feature gap | Manual log export | Implement tenant log API | CSP Eng | | Open |
| NCR-004 | Internal Audit | | No deletion certificate for terminated CSC | CLD.8.1.5 | Procedure gap | Issue retroactive | Update exit procedure | Service Owner | | Open |

---

*Owner: CISO + DPO | Review cycle: Monthly during open NCRs; quarterly trend review*
