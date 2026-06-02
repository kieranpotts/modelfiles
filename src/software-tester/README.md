# software-tester

A software tester that verifies behavior at runtime — designing and executing tests against acceptance criteria, then reporting pass / fail / blocked with reproducible evidence.

- **Base model:** `qwen2.5-coder:14b`
- **Purpose:** Runtime verification of a change against its acceptance criteria. Reach for it after review has cleared a change, or before tagging a release.

## Build

```bash
ollama create software-tester -f ./src/software-tester/Modelfile
```

## Run

```bash
ollama run software-tester
```
