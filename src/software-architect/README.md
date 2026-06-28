# software-architect

A software architect that designs systems — enumerating architectural options, weighing them against quality attributes, and recommending a structure with explicit trade-offs and ADR-style decision records.

- **Base model:** `qwen2.5:14b`
- **Purpose:** High-level software design. Reach for it after requirements are agreed and before delivery planning, to decide *how* the system should be structured and *why*.

## Build

```bash
ollama create software-architect -f ./src/software-architect/Modelfile
```

## Run

```bash
ollama run software-architect
```
