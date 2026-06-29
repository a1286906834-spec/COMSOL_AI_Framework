---
name: solver-diagnosis
description: COMSOL 6.4 solver diagnosis skill for convergence failure, singular matrix, inconsistent initial values, time-step failure, and multiphysics solver instability.
---


# Solver Diagnosis Skill

## Diagnosis Order

Do not start with mesh.

Check in this order:

1. Boundary-condition conflict
2. Missing reference pressure / ground / constraint
3. Material property units
4. Initial conditions
5. Coupling consistency
6. Source-term magnitude
7. Dependent-variable scaling
8. Time-step size
9. Mesh quality
10. Linear solver memory/conditioning

## Error Patterns

### Singular Matrix

Likely causes:

- unconstrained pressure
- missing ground
- free rigid body motion
- disconnected domain
- invalid selection
- missing material

### Failed to Find Consistent Initial Values

Likely causes:

- conflicting BCs
- poor initial values
- strong nonlinear source
- coupled physics initialized inconsistently

### Nonlinear Solver Did Not Converge

Likely causes:

- over-aggressive load
- too-large velocity/source
- outlet backflow
- strong coupling
- poor scaling

## Output

```text
Error:
Likely causes:
Checks:
Minimal fix:
Validation after fix:
```
