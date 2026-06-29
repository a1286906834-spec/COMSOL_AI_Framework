---
name: validation-review
description: Validation and engineering review skill for COMSOL CFD/multiphysics models. Use before trusting results or generating reports.
---


# Validation Review Skill

## Minimum Validation

Every model needs:

- unit consistency
- boundary completeness
- material assignment
- mesh quality
- solver convergence
- result sanity
- conservation check

## CFD Validation

- mass balance
- pressure drop sanity
- y+ if turbulent wall flow
- mesh independence for critical metrics
- benchmark/correlation if available

## Heat Validation

- energy balance
- heat flux continuity
- outlet temperature
- max temperature sanity

## Structural Validation

- constraint check
- reaction force balance
- stress singularity awareness

## EM Validation

- current balance
- power balance
- ground/reference check

## Output

```text
Validation status:
Passed:
Failed:
Unverified:
Required next check:
Confidence:
```
