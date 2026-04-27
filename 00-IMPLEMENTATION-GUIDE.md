# Implementation Guide — ISO/IEC 27017:2015 + ISO/IEC 27018:2019

**Document ID:** CLOUD-IG-001 | **Version:** 1.0 | **Classification:** Public

This guide explains how to use this toolkit to implement, operate, and prepare for certification audits of the cloud security extensions to ISO/IEC 27001:2022.

---

## 1. Audience

- **Cloud Service Customers (CSCs)** — organisations consuming cloud services who want assurance over CSP controls and to implement their own ISO 27017 customer-side controls.
- - **Cloud Service Providers (CSPs)** — IaaS / PaaS / SaaS providers seeking ISO 27017 and ISO 27018 certification alongside ISO 27001.
  - - **GRC, Risk, Privacy and Audit teams** — preparing for combined ISO 27001 + 27017 + 27018 audits.
   
    - ---

    ## 2. Pre-requisite

    This toolkit assumes you already have (or are concurrently implementing) an ISO/IEC 27001:2022 ISMS. ISO 27017 and ISO 27018 are **not standalone certifications** — they are extensions audited together with ISO 27001.

    If you do not yet have an ISMS, start with the `iso-27001-isms-toolkit` repository first.

    ---

    ## 3. Implementation Roadmap (12-week plan)

    | Week | Phase | Activities | Outputs |
    |------|-------|-----------|---------|
    | 1 | Initiation | Define cloud scope; identify CSP/CSC role(s); confirm services in scope (IaaS/PaaS/SaaS) | Cloud Scope Statement |
    | 2 | Gap Assessment | Run `01-GAP-ASSESSMENT/CLOUD-GAP-ASSESSMENT-CHECKLIST.md` | Gap report, prioritised remediation list |
    | 3–4 | Context & Leadership | Document interested parties, legal register, governance, RACI | Folder 03 + 04 deliverables |
    | 5–6 | Risk & Planning | Cloud risk assessment, treatment plan, SoA for 27017 + 27018 | Risk register, SoA |
    | 7–8 | Operation | Shared responsibility matrix, CSA review, PII processing notice, breach response | Folder 07 deliverables |
    | 9 | Support | Training, awareness, documented information control | Folder 06 deliverables |
    | 10 | Performance | KPIs, internal audit, management review | Folder 08 deliverables |
    | 11 | Improvement | NCR log, corrective actions, continual improvement plan | Folder 09 deliverables |
    | 12 | Stage 1 Readiness | Pre-certification check using `15-SUPPLEMENTARY-TEMPLATES/CERTIFICATION-READINESS-CHECKLIST.md` | Readiness sign-off |

    ---

    ## 4. Folder-by-Folder Workflow

    1. **`01-GAP-ASSESSMENT/`** — Score current state against each ISO 27017 cloud control and ISO 27018 PII obligation. Identify owners.
    2. 2. **`02-CLOUD-POLICY/`** — Approve the Cloud Security Policy and Cloud PII Policy at top management level.
       3. 3. **`03-SCOPE-AND-CONTEXT/`** — Document the cloud scope, declare CSP vs CSC role(s), record interested parties and legal/regulatory obligations.
          4. 4. **`04-LEADERSHIP/`** — Assign cloud security roles, RACI, PII processor accountability, and (where applicable) DPO interface.
             5. 5. **`05-PLANNING/`** — Run the cloud risk assessment, build the SoA, and produce the risk treatment plan.
                6. 6. **`06-SUPPORT/`** — Build awareness for cloud-specific risks (mis-configuration, identity, sub-processor management).
                   7. 7. **`07-OPERATION/`** — Implement and evidence operational controls — shared responsibility, CSA, sub-processor, PII handling, breach.
                      8. 8. **`08-PERFORMANCE/`** — Measure KPIs, run internal audits, and hold management reviews.
                         9. 9. **`09-IMPROVEMENT/`** — Capture nonconformities and drive continual improvement.
                            10. 10. **`10-ISO27017-CONTROLS/`** — Use as the authoritative implementation reference for cloud controls.
                                11. 11. **`11-ISO27018-CONTROLS/`** — Use as the authoritative implementation reference for PII-in-public-cloud controls.
                                    12. 12. **`12-WORKED-EXAMPLE/`** — Reference the Nexus Cloud Services worked example.
                                        13. 13. **`13-SCRIPTS/`** — Run automation for SoA and gap tracking.
                                            14. 14. **`14-CROSS-MAPPING/`** — Demonstrate coverage of GDPR / NIST / SOC 2 / CSA CCM / FedRAMP.
                                                15. 15. **`15-SUPPLEMENTARY-TEMPLATES/`** — Use ready-to-issue templates (CSA review, supplier assurance, PII notice).
                                                   
                                                    16. ---
                                                   
                                                    17. ## 5. Audit Strategy
                                                   
                                                    18. - **Combined audit** with ISO 27001 — auditor will use the same SoA and evidence trail.
                                                        - - **Stage 1** — documentation review (policies, scope, SoA, risk).
                                                          - - **Stage 2** — implementation effectiveness (sample evidence, walkthroughs, configuration review).
                                                            - - **Surveillance** — annual; **Recertification** — every 3 years.
                                                             
                                                              - ---

                                                              ## 6. Key Success Factors

                                                              - Clear declaration of CSP vs CSC role(s) per service in scope.
                                                              - - A signed Shared Responsibility Matrix per service.
                                                                - - Evidence of CSP due diligence (SOC 2 / ISO 27017 / ISO 27018 reports from sub-processors).
                                                                  - - Demonstrable PII processor controls (purpose limitation, sub-processor disclosure, return/transfer/disposal, breach notification).
                                                                    - - Continuous monitoring of cloud configuration and identity.
                                                                     
                                                                      - ---

                                                                      *Document Owner: GRC Lead | Review cycle: Annual | Next review: April 2027*
                                                                      
