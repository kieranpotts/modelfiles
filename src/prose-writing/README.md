# `prose-writing`

A capability tier tuned for writing clear, accurate, well-structured English
prose. Moderate temperature for readable, natural writing without drifting into
invention. Good for tasks like requirements elicitation, specification, and
documentation.

- **Base model:** `llama3.1:8b`
- **Temperature:** `0.5`
- **Context window:** `16384`

## Build

```bash
ollama create prose-writing -f ./src/prose-writing/Modelfile
```

## Run

```bash
ollama run prose-writing
```
