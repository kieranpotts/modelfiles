# technical-lead

A technical lead that turns requirements and an agreed design into an executable implementation plan — a sequence of small, independently shippable steps, each with clear scope and acceptance, plus risks and dependencies.

- **Base model:** `qwen2.5-coder:7b`
- **Purpose:** Implementation planning. Reach for it after design is agreed and before coding begins, to decompose a change into safe, ordered, testable steps.

## Build

```bash
ollama create technical-lead -f ./src/technical-lead/Modelfile
```

## Run

```bash
ollama run technical-lead
```
