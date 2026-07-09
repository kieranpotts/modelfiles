# Contributing

<!-- Agents MUST read ./AGENTS.md. This document is for humans. -->

The models are defined in a single source config, [`models.yaml`](../src/models.yaml),
and compiled into Modelfiles by [`run/build`](../run/build).

```
run/
  build              # `run/build [profile]` compiles `src/models.yaml`.
  compile.py         # The compiler (invoked by `build`).
src/
  models.yaml        # Config for the model profiles.
dist/                # Compiled output (Git-ignored):
  <profile>/
    <model-name>/
      Modelfile      # Generated — do not edit by hand.
```

## `models.yaml`

The file holds a single **`profiles`** map. Each profile is a self-contained
set of models — keyed by capability name — with each model's `from` (base
model) and parameters defined in full.

There MUST be a `default` profile; others are optional.

Profiles do not inherit from one another.

A profile is the set of models to install on one kind of machine — for example
cloud models on a laptop versus local models on a workstation.
