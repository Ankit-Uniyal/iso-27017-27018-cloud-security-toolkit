# 13 — SCRIPTS

Lightweight Python utilities to support operating the Cloud ISMS (ISO/IEC 27017 + 27018).

## Scripts

| Script | Purpose | Inputs | Outputs |
|--------|---------|--------|---------|
| cloud_soa_tracker.py | Track SoA implementation progress per section | SoA CSV (optional) | Markdown report (or stdout) |
| cloud_gap_checker.py | Compute gap-assessment conformance + flag critical gaps | gap CSV | Markdown report |
| dpia_cloud_scorer.py | Deterministic DPIA risk score + verdict | DPIA YAML/JSON | Markdown report |

## Requirements

- Python 3.9+
- pyyaml (for YAML DPIA descriptors): \`pip install -r requirements.txt\`

## Quick start (uses bundled samples/)

\`\`\`bash
# SoA tracking (no input = bundled canonical control list)
python cloud_soa_tracker.py
python cloud_soa_tracker.py --input samples/soa.csv --output soa_status.md

# Gap assessment scoring (exits non-zero if critical gaps are open)
python cloud_gap_checker.py --input samples/gap_assessment.csv --output gap_report.md

# DPIA scoring
python dpia_cloud_scorer.py --input samples/dpia.yaml --output dpia_score.md
\`\`\`

## samples/

- \`controls_master.csv\` — canonical control list (7 ISO 27017 CLD + 25 ISO 27018 Annex A); single source of truth shared by the scripts and the SoA.
- \`gap_assessment.csv\`, \`soa.csv\`, \`dpia.yaml\` — runnable example inputs.

## CSV Schemas

**Gap Assessment** — \`Control_ID, Domain, Title, Status, Owner, Evidence, Notes\`
Status values: \`Implemented | Partial | Not_Implemented | Not_Applicable\` (spaced spellings also accepted).

**SoA** — \`Control_ID, Title, Applicable, Status, Responsibility, Justification, Evidence, Last_Reviewed\`
Status values: \`Implemented | Partial | Not Implemented | Not Applicable\`; Applicable: \`Yes | No\`.

> Keep \`Control_ID\` values identical across the gap CSV, SoA and controls_master.csv (e.g. \`A.8.1\`, \`CLD.9.5.1\`) so that critical-gap flagging matches correctly.

## DPIA YAML Example

\`\`\`yaml
project: New AI Document Summariser
dpia_id: DPIA-2026-014
likelihood: possible        # rare|unlikely|possible|likely|almost_certain
impact: major               # negligible|minor|moderate|major|catastrophic
pii_volume: 10k_100k        # lt_100|100_1k|1k_10k|10k_100k|100k_plus
special_category: false
involves_children: false
cross_border_non_adequate: true
new_technology: true
\`\`\`

DPIA verdict thresholds: \`<10 PROCEED\` · \`10–17 PROCEED-WITH-MITIGATIONS\` · \`18–24 CONSULT-REGULATOR\` · \`25+ DO-NOT-PROCEED\`.

## Tests

Unit tests live in \`tests/\` and run with pytest from this directory:

\`\`\`bash
python -m pytest tests/ -v
\`\`\`

## CI

\`.github/workflows/ci.yml\` runs on every push and PR: it byte-compiles all three scripts, runs the unit tests on Python 3.9/3.11/3.12, and smoke-tests each script against the bundled samples.

## Roadmap

- JSON schema validation for SoA and gap CSV inputs
- HTML output renderer
- CLI flag for delta-vs-previous reports
- Pluggable risk-matrix configuration

Owner: Compliance + Cloud Security · Licence: MIT
