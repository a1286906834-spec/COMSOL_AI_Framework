---
name: cfd-chief-engineer
description: Chief CFD skill for COMSOL 6.4. Use for laminar/turbulent flow, internal/external flow, multiphase, porous flow, compressible flow, rotating flow, pressure drop, mixing, and solver decisions.
---


# CFD Chief Engineer Skill

## First Action

Do not generate scripts first.

Run the CFD intake:

```text
Objective:
Geometry:
Fluid:
Density:
Viscosity:
Driving condition:
Inlet:
Outlet:
Walls:
Study type:
Outputs:
Accuracy level:
```

## Mandatory CFD Checks

Compute or request inputs for:

- Reynolds number
- Mach number if gas/high-speed
- Peclet number for heat/species
- Prandtl number for heat
- Schmidt number for species
- Rayleigh/Grashof for buoyancy
- Weber/Capillary for multiphase
- Courant number for transient
- y+ for turbulent wall flow

## Flow Regime Logic

- Do not select Laminar Flow solely because geometry is small.
- Do not select Turbulent Flow solely because velocity is high.
- Use Re and physical context.
- Transitional flows require caution.

## COMSOL Mapping

- Low Re/Stokes: Creeping Flow
- Laminar: Laminar Flow
- Turbulent: Turbulent Flow with selected turbulence model
- Heat-coupled flow: Non-Isothermal Flow / Conjugate Heat Transfer
- Species-coupled flow: Transport of Diluted Species + velocity field
- Porous flow: Darcy / Brinkman / Free and Porous Media Flow
- Multiphase: Level Set / Phase Field / Mixture / Euler-Euler depending on interface need

## Output

```text
Status:
CFD objective:
Regime:
Physics interface:
BC status:
Mesh requirement:
Solver risk:
Validation:
```
