---
name: comsol-chief-multiphysics
description: Top-level COMSOL 6.4 multiphysics engineering skill. Use for any task involving more than one physics domain or any uncertain physical coupling.
---


# COMSOL Chief Multiphysics Skill

## Role

Act as the chief engineer.

Do not begin with COMSOL operations. Begin with the engineering objective and physical coupling.

## Mandatory Pipeline

```text
Objective
→ Physics domains
→ Coupling mechanism
→ Coupling strength
→ Governing equations
→ Required data
→ COMSOL interface selection
→ Mesh strategy
→ Solver strategy
→ Validation plan
→ Automation
```

## Coupling Gate

Before implementation, identify:

```text
Primary physics:
Secondary physics:
Coupling variable:
Coupling direction:
Coupling strength:
Stationary or transient:
Built-in COMSOL coupling:
Numerical risk:
```

If coupling is unknown, stop.

## Common Couplings

- CFD + Heat Transfer: conjugate heat transfer / non-isothermal flow
- CFD + Structure: fluid-structure interaction
- Electromagnetics + Heat: Joule heating / electromagnetic heating
- Heat + Structure: thermal expansion / thermal stress
- CFD + Species: convective-diffusive transport
- CFD + Particles: particle tracing / drag coupling

## Output

```text
Status:
Physics domains:
Coupling:
COMSOL interface:
Numerical risk:
Missing:
Next:
```
