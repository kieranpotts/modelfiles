# Modelfiles

This repository defines a collection of custom [Ollama](https://ollama.com)
models. The `Modelfile` definitions are **compiled** from a single source
config, [`models.yaml`](./src/models.yaml), by the `run/build` script.

A built Modelfile customizes a base model — its runtime parameters, prompt
template, and seeded message history — so it can be created as a reusable
named model that runs against a native Ollama install.

These models define generic **capabilities**, not roles. The role or persona is
expected to be supplied by the agent harness's system prompt. That's why the
Modelfiles in this collection carry no `SYSTEM` block.

`models.yaml` carries a `default` profile plus optional additional profiles.
Each profile is self-contained. A profile defines, in full, the models and
parameters to install on one kind of machine — eg. cloud models for a laptop,
local models for a workstation.

`./run/build [profile]` compiles the models defined for that profile to
`dist/<profile>/<model>/Modelfile`.

The capitalized words REQUIRED, MUST, MUST NOT, RECOMMENDED, SHOULD,
SHOULD NOT, OPTIONAL, and MAY are to be interpreted as described in
[IETF RFC 2119](https://www.ietf.org/rfc/rfc2119.txt).

## Project structure

- **`run/`**:
  Build scripts.

  - **`build`**:
    `run/build [profile]` — compiles `src/models.yaml` into Modelfiles under
    `dist/`. Defaults to the `default` profile.

  - **`compile.py`**:
    The Python compiler invoked by `build`. Not run directly.

- **`src/`**:
  Source: the model definitions and their documentation.

  - **`models.yaml`**:
    The source of truth. Defines each capability model and one or more
    profiles (base models and parameters). `./run/build` compiles this into
    Modelfiles.

- **`dist/`**:
  Compiled output — `dist/<profile>/<model-name>/Modelfile`. Generated and
  git-ignored; never edited by hand.

## Requirements

- **`ollama`** (native install on the host) to create and run the models.
- **`python3`** with **PyYAML** to compile the Modelfiles from `models.yaml`.

## Rules

- MUST write docs in American English.

- Models MUST be defined in `models.yaml`. Modelfiles MUST NOT be hand-written.
  Anything generated under `dist/` MUST NOT be edited directly.

- `models.yaml` MUST define a `default` profile. Each profile is
  self-contained. Every model it defines MUST specify its own `from` (base
  model) and parameters in full. Profiles do not inherit from one another.

- A profile compiles exactly the models it defines. Different profiles MAY
  define different sets of models.

- A compiled `Modelfile` MUST begin with a `FROM` instruction and MUST NOT
  contain a `SYSTEM` block. The role and persona are defined by the agent
  harness's system prompt, not by the model.

- A model MUST be named for the capability it provides, not for a role.

- A model name MUST take the form `<DOMAIN>_<TIER>`, in upper snake case.

  The **domain** is the material the model works over, and therefore what it
  has to be good at: `WORKFLOW`, `CODE`, `ANALYSIS`, `PROSE`, `SECURITY`.

  The **tier** is how much model the work needs: `BASIC`, `STANDARD`, `DEEP`.
  The tier bundles judgment depth together with context and cost. Deeper work
  needs bigger, more capable models.

  Upper snake case is a deliberate choice. Base models from the Ollama library
  are lowercase by convention, so the casing alone distinguishes a custom
  capability model from its underlying base model in `ollama list`.

- Capabilities MAY share a `from` base model, differing only in their
  parameters.

- A `from` base model SHOULD be available from the
  [Ollama library](https://ollama.com/library) or locally.

- A `num_ctx` above ~32768 SHOULD use a cloud base model, even inside an
  otherwise-local profile.

  The KV cache scales with the context window and quickly exceeds the size of
  the weights. A 128k window costs roughly 20GB even on an 8B model. Once the
  cache spills out of VRAM and into system RAM, throughput collapses.

- The compiler MAY emit only valid Modelfile instructions: `FROM`, `PARAMETER`,
  `TEMPLATE`, `SYSTEM`, `ADAPTER`, `LICENSE`, `MESSAGE`, `REQUIRES`.
