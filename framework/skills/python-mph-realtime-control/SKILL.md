---
name: python-mph-realtime-control
description: Python mph realtime-control skill for COMSOL 6.4 shared server sessions, parameter modification, model inspection, safe solve/run, export, and save/lock policy.
---


# Python mph Realtime Control Skill

## Workflow

1. Confirm COMSOL Server is running.
2. Confirm port, usually `2036`.
3. Connect with `mph.Client(version="6.4", port=2036)`.
4. List server models.
5. Identify target model.
6. Run engineering review.
7. Modify only approved items.
8. Do not save by default.
9. Let GUI save final model unless Python save-as is approved.

## Safe Connection Template

```python
import mph

client = mph.Client(version="6.4", port=2036)
models = client.models()

for i, model in enumerate(models):
    print(i, model)
```

## Safe Modification Rule

Do not modify if target model is ambiguous.

Do not overwrite `.mph` from Python during shared GUI session.

## Dangerous Actions Requiring Approval

- save/overwrite model
- remove model from server
- delete model nodes
- run expensive study
- remesh large model
- parametric sweep
- optimization

## Output

```text
Server:
Target model:
Action:
Save policy:
Risk:
Script:
```
