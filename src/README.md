# Custom models

An index of the custom model definitions in this repository. Each model lives
in its own directory with a `Modelfile` and a `README.md` covering its purpose,
base model, and build/run commands.

These models are generic **capability tiers**, not roles. Each pairs a
capable base model with tuning (temperature, context window) suited to a
_type_ of work. The role or persona — product manager, architect, programmer,
and so on — should be supplied by the agent harness's system prompt, not baked
into the model.

| Model | Capability | Base model |
| --- | --- | --- |
| [`computer-programming`](./computer-programming/README.md) | Writing, reviewing, and testing source code. | `qwen2.5-coder:14b` |
| [`technical-reasoning`](./technical-reasoning/README.md) | Design, planning, and trade-off analysis. | `qwen2.5:14b` |
| [`prose-writing`](./prose-writing/README.md) | Requirements, specification, and documentation. | `llama3.1:8b` |

See **[Usage](../docs/usage.md)** to build and run a model, and **[Development](../docs/development.md)** to add a new one.
