# Modelfiles

**Custom model definitions for running in [Ollama](https://ollama.com).**

Each model is defined by an Ollama [Modelfile](https://docs.ollama.com/modelfile),
a plain-text recipe that takes a base model and tunes it — runtime parameters,
prompt template, and seeded message history — into a reusable capability.
Building a Modelfile produces a named model that runs against a native
Ollama install.

These models define generic capabilities, not roles. The role or persona a
model plays is supplied by the agent harness's system prompt, so the
Modelfiles here deliberately carry no `SYSTEM` block.

## 📦 Models

See [**`./src/`**](./src/README.md) for the index of available custom models.

## 📓 Documentation

- [**Requirements**](./docs/requirements.md)
- [**Usage**](./docs/usage.md)
- [**Development**](./docs/development.md)

-----

Copyright © 2020-present Kieran Potts, [MIT license](./LICENSE.txt)
