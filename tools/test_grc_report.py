import os

from grc_report import (
    DATA, load_assessment, load_risks, maturity_pct, priority_gaps,
    risk_band, risk_summary,
)

ASSESS = load_assessment(os.path.join(DATA, "csf2-assessment.csv"))
RISKS = load_risks(os.path.join(DATA, "risk-register.csv"))


def test_assessment_loaded():
    assert len(ASSESS) == 20


def test_overall_maturity():
    # mean current 29/20 = 1.45 -> 36.25%
    assert abs(maturity_pct(ASSESS) - 36.25) < 0.01


def test_priority_gap_count():
    gaps = priority_gaps(ASSESS)
    assert len(gaps) == 16
    # largest gap is DE.CM (1 -> 4 = 3)
    assert gaps[0]["ID"] == "DE.CM" and gaps[0]["Gap"] == 3


def test_risk_bands():
    assert risk_band(20) == "Critical"
    assert risk_band(15) == "High"
    assert risk_band(10) == "Medium"
    assert risk_band(4) == "Low"


def test_risk_summary():
    counts = risk_summary(RISKS)
    assert counts["Critical"] == 3
    assert counts["High"] == 4
    assert counts["Medium"] == 1
    assert len(RISKS) == 8


def test_top_risk_score():
    assert max(r["Score"] for r in RISKS) == 20
