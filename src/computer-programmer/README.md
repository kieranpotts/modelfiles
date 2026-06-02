# computer-programmer

A programmer that implements one well-scoped step at a time — test-first, in keeping with existing conventions, strictly within the brief.

- **Base model:** `qwen2.5-coder:14b`
- **Purpose:** Writing code and tests for a single planned step. Reach for it during implementation, once a step's scope is clear, to produce correct, review-ready code.

## Build

```bash
ollama create computer-programmer -f ./src/computer-programmer/Modelfile
```

## Run

```bash
ollama run computer-programmer
```
