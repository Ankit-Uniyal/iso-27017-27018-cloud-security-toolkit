# Cloud Shared Responsibility Matrix Template

**Document ID:** CLOUD-SRM-001 | **Version:** 1.0 | **Classification:** Internal

This template implements ISO 27017 control **CLD.6.3.1 — Shared roles and responsibilities within a cloud computing environment**. Complete one matrix per cloud service.

| Service Name: | _____________________ | Service Type (IaaS/PaaS/SaaS): | _____ |
| CSP: | _____________________ | CSC: | _____________________ |
| Effective Date: | _____________________ | Review Cycle: | Annual |

## Layer-by-Layer Responsibility (mark CSP / CSC / Both)

| Layer | Activity | IaaS | PaaS | SaaS | Notes |
|-------|----------|------|------|------|-------|
| Physical / Facility | Data centre security | CSP | CSP | CSP | |
| Hardware | Servers, storage, network gear | CSP | CSP | CSP | |
| Virtualisation / Hypervisor | Tenant segregation (CLD.9.5.1) | CSP | CSP | CSP | |
| Host OS | Patching, hardening (CLD.9.5.2) | CSC | CSP | CSP | IaaS = CSC owns guest OS |
| Network — Virtual | Subnets, security groups, segmentation | CSC | Both | CSP | |
| Identity & Access | Account, role, MFA, federation | CSC | CSC | CSC | CSP provides controls; CSC configures |
| Application | Code, dependencies, secure SDLC | CSC | CSC | CSP | |
| Data | Classification, encryption, retention | CSC | CSC | CSC | Data ownership always CSC |
| Encryption Keys | Key custody (BYOK / CSP-managed) | CSC | Both | Both | Document model |
| Backup | Frequency, restore tests | CSC | Both | CSP | Validate per service |
| Monitoring & Logging | App-level | CSC | CSC | Both | CSP exposes platform logs (CLD.12.4.5) |
| Incident Response | Detect / respond / notify | Both | Both | Both | RACI per phase |
| Business Continuity | RTO / RPO / regional failover | Both | Both | CSP-led | |
| Compliance & Audit | Evidence ownership | Both | Both | Both | Maintain audit reports |
| PII Processing (where applicable) | ISO 27018 obligations | Both | Both | CSP | Confirm processor/sub-processor |
| Exit / Termination | Data return + secure deletion (CLD.8.1.5) | Both | Both | CSP-led | Deletion certificate required |

## Key Configurable Items (CSC-owned by default)

- Public/private accessibility of resources
- Encryption-at-rest and in-transit configuration
- Logging destinations and retention
- IAM roles, MFA, conditional access
- Backup schedule and restore testing
- Network segmentation (VPCs, security groups)

## Approvals

| Role | Name | Signature | Date |
|------|------|-----------|------|
| CSC — CISO | | | |
| CSC — DPO (if PII) | | | |
| CSP — Customer Success / Security Lead | | | |

---

*Approved by: CISO + CSP signatory | Review cycle: Annual or on service change*
