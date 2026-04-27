# 13 — SCRIPTS

Lightweight Python utilities to support operating the Cloud ISMS.

## Scripts

| Script | Purpose | Inputs | Outputs |
|--------|---------|--------|---------|
| `cloud_soa_tracker.py` | Track SoA implementation status across cycles | SoA CSV | Tracking report |
| `cloud_gap_checker.py` | Compute gap-assessment conformance + flag critical gaps | gap CSV | Markdown report |
| `dpia_cloud_scorer.py` | Deterministic DPIA risk score + verdict | DPIA YAML/JSON | Markdown report |

## Requirements

- Python 3.9+
- `pyyaml` (optional, for YAML descriptors in dpia_cloud_scorer)

```bash
pip install pyyaml
```

## Examples

```bash
# Gap assessment scoring
python cloud_gap_checker.py --input gap_assessment.csv --output gap_report.md

# DPIA scoring
python dpia_cloud_scorer.py --input dpia.yaml --output dpia_score.md

# SoA tracking
python cloud_soa_tracker.py --input soa.csv --output soa_status.md
```

## CSV Schemas

### Gap Assessment
`Control_ID, Domain, Title, Status, Owner, Evidence, Notes`

Status values: `Implemented | Partial | Not_Implemented | Not_Applicable`

### SoA
`Control_ID, Title, Applicable, Status, Responsibility, Justification, Evidence, Last_Reviewed`

## DPIA YAML Example

```yaml
project: New AI Document Summariser
dpia_id: DPIA-2026-014
likelihood: possible       # rare|unlikely|possible|likely|almost_certain
impact: major              # negligible|minor|moderate|major|catastrophic
pii_volume: 10k_100k       # lt_100|100_1k|1k_10k|10k_100k|100k_plus
special_category: false
involves_children: false
cross_border_non_adequate: true
new_technology: true
```

## Integration

These scripts are designed for CI use:
- Add a GitHub Action that runs `cloud_gap_checker.py` against `05-PLANNING/STATEMENT-OF-APPLICABILITY.md`-derived CSV on PR.
- Fail the PR if critical gaps re-appear.
- Auto-generate management-review pack from the outputs.

## Tests

A minimal test harness can be added under `tests/` using `pytest`. Example:

```python
from dpia_cloud_scorer import classify

def test_proceed():
    assert classify(5) == "PROCEED"

def test_consult():
    assert classify(20) == "CONSULT-REGULATOR"
```

## Roadmap

- Add JSON schema validation for SoA and gap CSV inputs
- Add HTML output renderer
- Add CLI flag for delta-vs-previous reports
- Pluggable risk-matrix configuration

---
**Owner:** Compliance + Cloud Security · **Licence:** MIT
