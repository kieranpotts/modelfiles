# `technical-reasoning`

A capability tier tuned for structured technical reasoning: design, planning,
and trade-off analysis. Balanced temperature to explore options while staying
grounded, with room to hold requirements, constraints, and system context.

- **Base model:** `qwen2.5:14b`
- **Temperature:** `0.5`
- **Context window:** `16384`

## Build

```bash
ollama create technical-reasoning -f ./src/technical-reasoning/Modelfile
```

## Run

```bash
ollama run technical-reasoning
```
