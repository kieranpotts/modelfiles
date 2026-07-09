# Modelfiles

This repository is a collection of custom [Ollama](https://ollama.com) model
definitions ("Modelfiles"). Each Modelfile customizes a base model — its
runtime parameters, prompt template, and seeded message history — so it can be
built into a reusable named model that runs against a native Ollama install.

These models define generic **capabilities**, not roles. The role or persona is
supplied by the agent harness's system prompt, so Modelfiles here carry no
`SYSTEM` block. Name and describe a model by the capability it provides, not by
a role it plays.

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD,
SHOULD NOT, OPTIONAL, and MAY are to be interpreted as described in
[IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

## Project structure

- **`src/`**:
  One directory per custom model.

  - **`README.md`**:
    Index of the available custom models.

  - **`<model-name>/`**:
    A single custom model.

    - **`Modelfile`**:
      The Ollama model definition.

    - **`README.md`**:
      What the model is for, the base model it derives from,
      and how to build and run it.

- **`template/`**:
  Template files for defining a new model. Copy into
  `src/<model-name>/` to start.

## Requirements

- **`ollama`** (native install on the host).

## Rules

- MUST write docs in American English.

- MUST follow the `template/` structure when adding a new model.

- Each custom model MUST live in its own directory under `src/`,
  named for the model.

- The model definition file MUST be named `Modelfile` (no extension).

- Each model directory MUST include a `README.md` documenting the model's
  purpose, base model, and build/run commands.

- When adding or removing a model, you MUST update the index in `src/README.md`
  to match.

- A `Modelfile` MUST begin with a `FROM` instruction.

- A `Modelfile` MUST NOT contain a `SYSTEM` block. The role and persona are
  defined by the agent harness's system prompt, not by the model.

- A model MUST be named for the capability it provides, not for a role.

- `FROM` SHOULD reference a model available from the
  [Ollama library](https://ollama.com/library) or a locally available base model.

- Only valid Modelfile instructions MAY be used: `FROM`, `PARAMETER`,
  `TEMPLATE`, `SYSTEM`, `ADAPTER`, `LICENSE`, `MESSAGE`, `REQUIRES`.
