# Skill Loading Tests

## Test 1

Prompt:

```text
/selfcheck
```

Expected:

```text
COMSOL-AI-FRAMEWORK-v0.5-SKILL-OPTIMIZED
```

## Test 2

Prompt:

```text
帮我直接通过 Python mph 跑一个流固耦合模型
```

Expected:

- no Python execution
- asks for fluid, solid, interface, BC, constraints, study type
- says FSI coupling review must pass first

## Test 3

Prompt:

```text
普通管道水流要不要用 FSI？
```

Expected:

- identifies single-domain CFD unless wall deformation matters
- does not force multiphysics
