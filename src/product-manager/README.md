# product-manager

A product manager that elicits and specifies business requirements — turning vague stakeholder asks into clear problem statements, user stories, and testable acceptance criteria.

- **Base model:** `llama3.1:8b`
- **Purpose:** Requirements discovery and specification in plain business language. Reach for it at the start of a change, before any design or coding, to define *what* to build and *why* — not *how*.

## Build

```bash
ollama create product-manager -f ./src/product-manager/Modelfile
```

## Run

```bash
ollama run product-manager
```
