---
name: em-heat-coupling
description: COMSOL 6.4 electromagnetic heating skill for Joule heating and electromagnetic-thermal coupling.
---


# Electromagnetic Heating Skill

## Use Cases

- Joule heating
- resistive heating
- electromagnetic heating
- temperature-dependent electrical conductivity

## Required Data

```text
Electrical material properties:
Thermal material properties:
Electrical BC:
Thermal BC:
Heat source definition:
Temperature dependence:
Study type:
```

## COMSOL Interfaces

- Electric Currents
- Heat Transfer in Solids
- Joule Heating
- Electromagnetic Heating where applicable

## Coupling Direction

- electric current generates heat
- temperature may change conductivity
- thermal expansion may be added if structural effects matter

## Stability Risks

- strong nonlinear conductivity-temperature coupling
- missing ground/reference
- insufficient heat removal BC
- unit mismatch in heat source

## Validation

- electrical power balance
- heat generation equals thermal output at steady state
- maximum temperature sanity check
