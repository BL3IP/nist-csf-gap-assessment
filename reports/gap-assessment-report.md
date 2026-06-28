# NIST CSF 2.0 Gap Assessment & Risk Register — Northwind Trading (fictional)

**Overall maturity:** 36.2% of target tier 4 (mean current 1.45/4)
**Priority gaps (>=2 tiers):** 16 of 20 categories
**Risks:** 8 (Critical 3, High 4, Medium 1, Low 0)

## Maturity by Function
| Function | Current | Target |
|----------|--------:|-------:|
| GOVERN | 1.6 | 3.2 |
| IDENTIFY | 1.3 | 3.3 |
| PROTECT | 1.6 | 3.4 |
| DETECT | 1.0 | 3.5 |
| RESPOND | 1.7 | 3.3 |
| RECOVER | 1.0 | 3.0 |

## Priority Gaps (remediation backlog)
| ID | Category | Current | Target | Gap |
|----|----------|--------:|-------:|----:|
| DE.CM | Continuous Monitoring | 1 | 4 | 3 |
| GV.RM | Risk Management Strategy | 1 | 3 | 2 |
| GV.PO | Policy | 2 | 4 | 2 |
| GV.SC | Cybersecurity Supply Chain Risk Management | 1 | 3 | 2 |
| ID.AM | Asset Management | 2 | 4 | 2 |
| ID.RA | Risk Assessment | 1 | 3 | 2 |
| ID.IM | Improvement | 1 | 3 | 2 |
| PR.AA | Identity Management and Access Control | 2 | 4 | 2 |
| PR.AT | Awareness and Training | 1 | 3 | 2 |
| PR.DS | Data Security | 2 | 4 | 2 |
| PR.IR | Technology Infrastructure Resilience | 1 | 3 | 2 |
| DE.AE | Adverse Event Analysis | 1 | 3 | 2 |
| RS.MA | Incident Management | 2 | 4 | 2 |
| RS.AN | Incident Analysis | 1 | 3 | 2 |
| RC.RP | Incident Recovery Plan Execution | 1 | 3 | 2 |
| RC.CO | Incident Recovery Communication | 1 | 3 | 2 |

## Risk Register (by score)
| ID | Risk | CSF | L | I | Score | Band | Treatment |
|----|------|-----|--:|--:|------:|------|-----------|
| R-01 | No MFA on admin accounts enables account takeover | PR.AA | 4 | 5 | 20 | Critical | Mitigate |
| R-02 | Unpatched internet-facing VPN (known CVE) | PR.PS | 4 | 5 | 20 | Critical | Mitigate |
| R-03 | No centralized logging or SIEM; blind to intrusions | DE.CM | 5 | 4 | 20 | Critical | Mitigate |
| R-04 | No tested incident response plan | RS.MA | 3 | 5 | 15 | High | Mitigate |
| R-05 | Backups never restore-tested | RC.RP | 3 | 5 | 15 | High | Mitigate |
| R-06 | Third-party vendor with excessive data access | GV.SC | 3 | 4 | 12 | High | Transfer |
| R-07 | Phishing susceptibility; no security awareness program | PR.AT | 4 | 3 | 12 | High | Mitigate |
| R-08 | Sensitive data unencrypted at rest | PR.DS | 2 | 5 | 10 | Medium | Mitigate |
