# Security Scanning Notes

This repository runs automated security checks in CI:

- **Bandit**: static analysis of Python code (`bandit -r app`)
- **pip-audit**: dependency vulnerability checks (`pip-audit -r requirements.txt`)

## Policy
- Findings must be addressed before merging to `main`.
- When a fix is not immediately available, the finding must be documented with rationale and a follow-up plan.
