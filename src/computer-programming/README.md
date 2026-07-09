# `computer-programming`

A capability tier tuned for coding — writing, reviewing, and testing source
code. Low temperature for correct, deterministic output and a large context
window for holding a full change plus its surrounding source.

- **Base model:** `qwen2.5-coder:14b`
- **Temperature:** `0.2`
- **Context window:** `32768`

## Build

```bash
ollama create computer-programming -f ./src/computer-programming/Modelfile
```

## Run

```bash
ollama run computer-programming
```
