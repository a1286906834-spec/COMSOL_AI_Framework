---
name: fsi-coupling
description: COMSOL 6.4 fluid-structure interaction skill. Use for deformation-driven flow, pressure loading on structures, moving mesh, and transient FSI stability.
---


# FSI Coupling Skill

## Required Data

```text
Fluid:
Structure material:
Fluid geometry:
Solid geometry:
Interface:
Loads:
Constraints:
Expected deformation:
Stationary or transient:
```

## Coupling

- fluid pressure/shear loads structure
- structural displacement deforms fluid domain
- mesh movement transfers interface motion

## COMSOL Interfaces

- Laminar/Turbulent Flow
- Solid Mechanics
- Moving Mesh / ALE
- Fluid-Structure Interaction coupling

## Stability Risks

- large deformation
- weak structural constraints
- poor moving mesh quality
- too-large time step
- strong density/stiffness contrast
- inconsistent initial conditions

## Solver Strategy

- start with one-way load if needed
- use transient for dynamic FSI
- reduce time step for instability
- validate structural constraints before coupling

## Output

```text
FSI type:
Interface:
Moving mesh:
Constraints:
Solver risk:
Validation:
```
