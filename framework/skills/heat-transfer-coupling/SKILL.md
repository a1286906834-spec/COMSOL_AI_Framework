---
name: heat-transfer-coupling
description: COMSOL 6.4 heat transfer coupling skill for non-isothermal flow, conjugate heat transfer, thermal stress, heat sources, and energy validation.
---


# Heat Transfer Coupling Skill

## Use Cases

- conjugate heat transfer
- non-isothermal flow
- heat sink
- heat exchanger
- thermal stress
- Joule/electromagnetic heating

## Required Data

```text
Fluid thermal properties:
Solid thermal properties:
Heat source or thermal BC:
Flow regime:
Interface/contact assumptions:
Initial temperature:
Outputs:
```

## COMSOL Interfaces

- Heat Transfer in Solids
- Heat Transfer in Fluids
- Non-Isothermal Flow
- Conjugate Heat Transfer
- Thermal Expansion / Thermal Stress if structural coupling exists

## Dimensionless Checks

- Re
- Pr
- Pe
- Bi
- Nu target if applicable
- Ra for natural convection

## Validation

- energy balance
- heat flux continuity
- outlet temperature
- maximum temperature
- Nusselt correlation where applicable

## Output

```text
Thermal objective:
Coupling:
Thermal BC:
Material data:
Validation:
Risk:
```
