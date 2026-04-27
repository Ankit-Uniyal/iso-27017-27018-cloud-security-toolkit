"""
dpia_cloud_scorer.py
Cloud DPIA Risk Scorer (ISO/IEC 27018 + GDPR Art. 35 aligned)

Reads a DPIA YAML/JSON descriptor file, applies a deterministic risk-scoring
matrix, and outputs a recommendation (PROCEED / PROCEED-WITH-MITIGATIONS /
DO-NOT-PROCEED / CONSULT-REGULATOR).

Usage:
    python dpia_cloud_scorer.py --input dpia.yaml --output dpia_score.md
"""

from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

try:
    import yaml  # optional
    _YAML = True
except ImportError:
    _YAML = False


# ----- Scoring weights -------------------------------------------------------

LIKELIHOOD_SCORES = {"rare": 1, "unlikely": 2, "possible": 3, "likely": 4, "almost_certain": 5}
IMPACT_SCORES = {"negligible": 1, "minor": 2, "moderate": 3, "major": 4, "catastrophic": 5}

PII_VOLUME_WEIGHT = {
    "lt_100": 0,
    "100_1k": 1,
    "1k_10k": 2,
    "10k_100k": 3,
    "100k_plus": 4,
}

SPECIAL_CATEGORY_BONUS = 2          # GDPR Art. 9 / sensitive PII
CHILDREN_BONUS = 2
CROSS_BORDER_NON_ADEQUATE_BONUS = 1
NEW_TECHNOLOGY_BONUS = 1            # GenAI, biometrics, novel cloud service


def load_descriptor(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if path.suffix in {".yaml", ".yml"} and _YAML:
        return yaml.safe_load(text)
    return json.loads(text)


def base_score(d: dict) -> int:
    likelihood = LIKELIHOOD_SCORES.get(d.get("likelihood", "possible"), 3)
    impact = IMPACT_SCORES.get(d.get("impact", "moderate"), 3)
    return likelihood * impact  # 1-25


def adjust_score(score: int, d: dict) -> int:
    score += PII_VOLUME_WEIGHT.get(d.get("pii_volume", "lt_100"), 0)
    if d.get("special_category"):
        score += SPECIAL_CATEGORY_BONUS
    if d.get("involves_children"):
        score += CHILDREN_BONUS
    if d.get("cross_border_non_adequate"):
        score += CROSS_BORDER_NON_ADEQUATE_BONUS
    if d.get("new_technology"):
        score += NEW_TECHNOLOGY_BONUS
    return min(score, 35)  # cap


def classify(score: int) -> str:
    if score >= 25:
        return "DO-NOT-PROCEED-OR-CONSULT-REGULATOR"
    if score >= 18:
        return "CONSULT-REGULATOR"
    if score >= 10:
        return "PROCEED-WITH-MITIGATIONS"
    return "PROCEED"


def render(d: dict, raw: int, adj: int, verdict: str) -> str:
    return f"""# DPIA Risk Score Report

**Project:** {d.get('project','(unspecified)')}
**DPIA ID:** {d.get('dpia_id','(unspecified)')}

## Inputs
- Likelihood: {d.get('likelihood')}
- Impact: {d.get('impact')}
- PII Volume: {d.get('pii_volume')}
- Special Category: {d.get('special_category', False)}
- Involves Children: {d.get('involves_children', False)}
- Cross-border (non-adequate): {d.get('cross_border_non_adequate', False)}
- New Technology: {d.get('new_technology', False)}

## Score
- Base (L × I): **{raw}**
- Adjusted: **{adj}**

## Verdict: **{verdict}**

## Notes
- Verdict thresholds: <10 PROCEED · 10-17 PROCEED-WITH-MITIGATIONS · 18-24 CONSULT-REGULATOR · 25+ DO-NOT-PROCEED-OR-CONSULT
- This is a decision-support tool. Final determination requires DPO opinion.
"""


def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, type=Path)
    p.add_argument("--output", required=True, type=Path)
    args = p.parse_args(argv)

    if not args.input.exists():
        print(f"Input not found: {args.input}", file=sys.stderr)
        return 2

    d = load_descriptor(args.input)
    raw = base_score(d)
    adj = adjust_score(raw, d)
    verdict = classify(adj)
    args.output.write_text(render(d, raw, adj, verdict), encoding="utf-8")
    print(f"Wrote {args.output}: score={adj} verdict={verdict}")
    return 0 if verdict == "PROCEED" else 1


if __name__ == "__main__":
    sys.exit(main())
