# Physics Router

## Purpose

Route a user request to the correct engineering skill.

## Required Steps

1. Identify objective.
2. Identify physics domains.
3. Identify coupling.
4. Check missing information.
5. Select required skill files under `framework/skills/`.
6. Stop if required data is missing.

## Routing Map

| User intent | Skill |
|---|---|
| Fluid flow | cfd-chief-engineer |
| Heat + flow | heat-transfer-coupling + cfd-chief-engineer |
| Flow + structure | fsi-coupling |
| Electric heating | em-heat-coupling |
| Any multiphysics | multiphysics-coupling |
| Solver failure | solver-diagnosis |
| Numerical instability | numerics-stability |
| Python mph control | python-mph-realtime-control |
| Result trustworthiness | validation-review |

## Hard Rule

Never select COMSOL nodes before selecting physics and coupling.
