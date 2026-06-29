# Engineering Validation Checks

## Universal

- unit consistency
- geometry completeness
- material assignment
- boundary condition completeness
- initial condition consistency
- solver convergence
- result sanity

## CFD

- mass conservation
- pressure drop sanity
- y+ for turbulent wall flow
- mesh independence
- outlet backflow check

## Heat Transfer

- energy balance
- heat flux continuity
- maximum temperature
- outlet temperature
- Nusselt correlation if applicable

## Structure

- rigid body mode removal
- reaction force balance
- displacement sanity
- stress singularity awareness

## Electromagnetics

- ground/reference
- current balance
- power balance

## Multiphysics

- coupling variable units
- interface continuity
- coupled solver stability
