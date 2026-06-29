---
name: multiphysics-coupling
description: Skill for identifying and validating coupling between physics domains before COMSOL multiphysics implementation.
---


# Multiphysics Coupling Skill

## Coupling Types

### One-way Coupling

Physics A affects Physics B, but B does not significantly affect A.

Example:
- velocity field drives species transport
- temperature field drives thermal stress without deformation feedback

### Two-way Coupling

Physics A and B influence each other.

Example:
- non-isothermal flow with temperature-dependent density/viscosity
- FSI with deformation affecting flow
- Joule heating with temperature-dependent electrical conductivity

## Coupling Strength

Classify:

```text
Weak:
Medium:
Strong:
```

Strong coupling usually requires careful solver strategy.

## Required Coupling Definition

```text
Source physics:
Target physics:
Coupled variable:
Equation location:
Unit:
Direction:
Built-in COMSOL coupling:
Manual coupling needed:
```

## Hard Stops

Stop if:

- coupling variable has no unit
- coupling direction is unknown
- physics domains are incomplete
- boundary/interface condition is missing
- solver sequence is undefined

## Output

```text
Coupling:
Strength:
COMSOL node:
Solver implication:
Risk:
```
