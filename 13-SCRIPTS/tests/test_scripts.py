"""Unit tests for the ISO 27017/27018 GRC scripts.

Run from the 13-SCRIPTS directory:
    python -m pytest tests/
"""
import sys
from pathlib import Path

# Make the parent (13-SCRIPTS) importable when running pytest from anywhere.
SCRIPTS_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(SCRIPTS_DIR))
SAMPLES = SCRIPTS_DIR / "samples"

import cloud_soa_tracker as soa
import cloud_gap_checker as gap
import dpia_cloud_scorer as dpia


# --------------------------- DPIA scorer -----------------------------------

def test_classify_proceed():
    assert dpia.classify(5) == "PROCEED"


def test_classify_mitigations():
    assert dpia.classify(10) == "PROCEED-WITH-MITIGATIONS"
    assert dpia.classify(17) == "PROCEED-WITH-MITIGATIONS"


def test_classify_consult():
    assert dpia.classify(18) == "CONSULT-REGULATOR"
    assert dpia.classify(24) == "CONSULT-REGULATOR"


def test_classify_do_not_proceed():
    assert dpia.classify(25) == "DO-NOT-PROCEED"
    assert dpia.classify(35) == "DO-NOT-PROCEED"


def test_dpia_sample_scores_mitigations():
    d = dpia.load_descriptor(SAMPLES / "dpia.yaml")
    raw = dpia.base_score(d)
    adj = dpia.adjust_score(raw, d)
    assert raw == 12          # possible(3) x major(4)
    assert adj == 17          # +3 volume +1 cross-border +1 new-tech
    assert dpia.classify(adj) == "PROCEED-WITH-MITIGATIONS"


def test_dpia_score_capped():
    worst = {
        "likelihood": "almost_certain",
        "impact": "catastrophic",
        "pii_volume": "100k_plus",
        "special_category": True,
        "involves_children": True,
        "cross_border_non_adequate": True,
        "new_technology": True,
    }
    raw = dpia.base_score(worst)
    assert dpia.adjust_score(raw, worst) == dpia.SCORE_CAP


# --------------------------- SoA tracker -----------------------------------

def test_soa_default_control_count():
    controls = soa.default_controls()
    assert len(controls) == 32          # 7 CLD + 25 Annex A
    cld = [c for c in controls if c.section == "ISO27017-CLD"]
    annex = [c for c in controls if c.section == "ISO27018-AnnexA"]
    assert len(cld) == 7
    assert len(annex) == 25


def test_soa_control_score():
    c = soa.Control(ref="A.8.1", section="ISO27018-AnnexA", title="x", status="Implemented")
    assert c.score() == 1.0
    c.status = "Partial"
    assert c.score() == 0.5
    c.applicable = False
    assert c.score() is None


def test_soa_loads_sample_csv():
    controls = soa.load_controls(SAMPLES / "soa.csv")
    assert len(controls) == 12
    assert soa.overall(controls) > 0.0


# --------------------------- Gap checker -----------------------------------

def test_gap_normalize_status():
    assert gap.normalize_status("Not Implemented") == "Not_Implemented"
    assert gap.normalize_status("Implemented") == "Implemented"


def test_gap_flags_critical_pii_breach():
    rows = gap.load_rows(SAMPLES / "gap_assessment.csv")
    _overall, _domains, _by_status, critical_open = gap.score_rows(rows)
    flagged = {r["Control_ID"] for r in critical_open}
    # A.8.1 is Not_Implemented and critical -> must be flagged.
    assert "A.8.1" in flagged
