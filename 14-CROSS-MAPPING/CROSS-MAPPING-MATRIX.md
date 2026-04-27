# Cross-Mapping Matrix - ISO 27017 / ISO 27018

Document ID: CLOUD-XMAP-001 | Version: 1.0 | Classification: Public

## ISO 27017 Cloud Controls

| ISO 27017 | NIST CSF 2.0 | CSA CCM v4 | SOC 2 | NIST 800-53 |
|-----------|--------------|------------|-------|-------------|
| CLD.6.3.1 | GV.RR | GRC, STA | CC1.0 | PM-1, PL-1 |
| CLD.8.1.5 | PR.DS-3 | DSP, BCR | CC6.5 | MP-6, SI-12 |
| CLD.9.5.1 | PR.AC-5 | IVS-09 | CC6.1 | SC-7, SC-32 |
| CLD.9.5.2 | PR.IP-1 | IVS-04 | CC6.6 | CM-6, CM-7 |
| CLD.12.1.5 | PR.AC-7 | IAM-12 | CC6.3 | AC-2, AC-6 |
| CLD.12.4.5 | DE.CM | LOG-09 | CC7.2 | AU-2, AU-12 |
| CLD.13.1.4 | PR.AC-5 | IVS-06 | CC6.6 | SC-7 |

## ISO 27018 PII Obligations

| ISO 27018 | GDPR | UAE PDPL | NIST Privacy |
|-----------|------|----------|--------------|
| A.1 Documented instructions | Art 28(3)(a) | Art 26 | CT.PO-P |
| A.2 Purpose limitation | Art 5(1)(b) | Art 5 | CT.PO-P1 |
| A.3 Sub-processor disclosure | Art 28(2) | Art 27 | CT.DM-P |
| A.4 Sub-processor flow-down | Art 28(4) | Art 27 | GV.PO-P |
| A.5 Geographic transparency | Art 13, 44 | Art 22 | CT.DM-P |
| A.6 Encryption | Art 32(1)(a) | Art 20 | PR.DS-P |
| A.8 Breach notification | Art 33(2) | Art 9 | CM.AW-P |
| A.9 DSR cooperation | Art 28(3)(e) | Art 14-18 | CT.DM-P |
| A.11 Independent assurance | Art 28(3)(h) | Art 26 | GV.MT-P |
| A.18 Return / disposal | Art 28(3)(g) | Art 27 | CT.DM-P |
| A.22 Law enforcement | Art 48 | sectoral | GV.PO-P |

## Coverage Summary

GDPR Art 28 (Processor): met by ISO 27018 A.1, A.3, A.4, A.8, A.9, A.11, A.18.

GDPR Art 32 (Security): met by ISO 27017 plus ISO 27018 A.6, A.10.

GDPR Art 33-34 (Breach): met by ISO 27018 A.8 plus Breach Procedure.

GDPR Art 44-49 (Transfers): met by ISO 27018 A.5 plus TIA.

NIST CSF 2.0 Govern: met by Cloud Security Policy plus Cloud PII Policy plus RACI.

Owner: GRC Lead | Review cycle: Annual

