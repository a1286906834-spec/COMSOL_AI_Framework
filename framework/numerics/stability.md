# Numerical Stability Rules

## General

Most solver failures are caused by physics definition, boundary conditions, scaling, or initial values before mesh.

## Strong Coupling Risks

- CFD + heat with temperature-dependent properties
- FSI with moving mesh
- Joule heating with temperature-dependent conductivity
- phase-field/level-set multiphase models

## Stabilization Strategy

1. Simplify physics.
2. Initialize subphysics separately.
3. Use parameter ramping.
4. Use continuation.
5. Use segregated solver if strong coupling causes fully coupled failure.
6. Reduce time step for transient coupling.
7. Improve mesh only after physics and BC checks.
