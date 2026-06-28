# Custom models

An index of the custom model definitions in this repository. Each model lives in its own directory with a `Modelfile` and a `README.md` covering its purpose, base model, and build/run commands.

These models form a role-based software delivery workflow, from requirements through documentation.

| Model | Role | Base model |
| --- | --- | --- |
| [`product-manager`](./product-manager/README.md) | Elicits and specifies business requirements. | `llama3.1:8b` |
| [`software-architect`](./software-architect/README.md) | Designs systems and weighs architectural trade-offs. | `qwen2.5:14b` |
| [`technical-lead`](./technical-lead/README.md) | Turns requirements and design into an delivery plan. | `qwen2.5-coder:7b` |
| [`computer-programmer`](./computer-programmer/README.md) | Implements planned steps as code and tests. | `qwen2.5-coder:14b` |
| [`code-reviewer`](./code-reviewer/README.md) | Statically reviews a change for defects and quality. | `qwen2.5-coder:14b` |
| [`software-tester`](./software-tester/README.md) | Verifies behavior at runtime against acceptance criteria. | `qwen2.5-coder:14b` |
| [`technical-writer`](./technical-writer/README.md) | Writes clear, accurate technical documentation. | `llama3.1:8b` |

See [Usage](../docs/usage.md) to build and run a model, and [Development](../docs/development.md) to add a new one.
