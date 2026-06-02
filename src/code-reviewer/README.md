# code-reviewer

A code reviewer that performs static analysis of a diff — auditing correctness, design, clarity, security, and completeness, and classifying every finding as blocking or non-blocking.

- **Base model:** `qwen2.5-coder:14b`
- **Purpose:** Reviewing a code change by reading it (not running it). Reach for it after a step is implemented and before it is merged or tested.

## Build

```bash
ollama create code-reviewer -f ./src/code-reviewer/Modelfile
```

## Run

```bash
ollama run code-reviewer
```
