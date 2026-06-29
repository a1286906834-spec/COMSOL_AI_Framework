---
name: numerics-stability
description: Numerical stability skill for COMSOL multiphysics simulations, including scaling, stabilization, nonlinear coupling, time stepping, solver choice, and mesh-quality impact.
---


# Numerics Stability Skill

## Purpose

Prevent numerically unstable models before solving.

## Checkpoints

```text
Equation stiffness:
Coupling strength:
Variable scaling:
Source-term magnitude:
Convection dominance:
Time-step requirement:
Mesh quality:
Boundary compatibility:
```

## CFD Stability

- high Re may require turbulence model or stabilization
- outlet backflow may destabilize stationary solves
- transient cases require time-step control
- convection-dominated scalar transport may need stabilization

## Multiphysics Stability

- strong two-way coupling may require segregated solver
- thermal-electrical coupling may require ramping
- FSI may require small time step and moving mesh checks
- nonlinear material properties may require continuation

## Output

```text
Stability risk:
Cause:
Recommended solver strategy:
Stabilization:
Validation:
```
