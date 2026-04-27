# ISO/IEC 27017:2015 — Cloud Controls Reference

**Document ID:** CLOUD-27017-001 | **Version:** 1.0 | **Classification:** Public

ISO/IEC 27017:2015 provides cloud-specific guidance on ISO/IEC 27002 controls (37 controls extended) **plus** seven cloud-only controls (the "CLD." family). This document summarises both.

> Note: ISO 27017 was originally published against ISO 27002:2013 control numbering. Where helpful, cross-references to ISO 27002:2022 control numbering are noted in square brackets.

---

## Cloud-Only Controls (CLD)

### CLD.6.3.1 Shared roles and responsibilities within a cloud computing environment
Define and document who is responsible for what between CSP and CSC across the full stack. Implement via a Shared Responsibility Matrix per service.
- Evidence: signed Shared Responsibility Matrix; CSA security schedule.

### CLD.8.1.5 Removal of cloud service customer assets
On termination, the CSP shall return CSC assets and securely remove all copies. Define data return formats, deletion verification and certificate.
- Evidence: exit procedure, deletion certificates, contractual SLAs.

### CLD.9.5.1 Segregation in virtual computing environments
The CSP shall enforce logical isolation between tenants at compute, storage and network layers.
- Evidence: tenant isolation design doc, segregation testing results, independent assurance.

### CLD.9.5.2 Virtual machine hardening
Hardening baselines for VMs (and containers) shall be defined, applied and continuously monitored.
- Evidence: CIS-aligned baselines, image scan repo
