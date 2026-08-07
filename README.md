# Modelfiles

**Custom model definitions for running in [Ollama](https://ollama.com).**

> [!IMPORTANT]
> This project is no longer maintained. Ollama's system for defining custom
> model works well for extending open-weight models with custom parameters
> when those models are downloaded and run locally. Unfortunately, when you
> use `ollama create` to build on cloud models (eg. `FROM deepseek-v4-flash:cloud`)
> the custom models do not inherit the parent model's configuration (eg. context
> length) or capability metadata (eg. tools, thinking).
>
> In effect, custom models defined on a laptop but actually backed by cloud
> models have very limited capabilities — they're good only for using in
> `ollama run` but not in coding agent harnesses.
>
> This project could be revisited in the future if `ollama`'s capabilities
> are extended to support this use case. Related issues:
>
> https://github.com/ollama/ollama/issues/16891
> https://github.com/ollama/ollama/pull/16956

Each model is defined by an Ollama [Modelfile][modelfile-spec],
a plain-text recipe that takes a base model and tunes it into a reusable
capability.

The Modelfiles are compiled from a single [source config](./src/models.yaml)
by [`run/build`](./run/build). Multiple profiles may be configured, allowing
different model configurations for different target machines — eg. local
models for workstations, cloud models for laptops.

```bash
./run/build              # Compile the default profile → dist/default/
./run/build workstation  # Compile a named profile     → dist/workstation/
```

The purpose is to create an abstraction layer between agents and the underlying
models. For example, multiple agents may be configured to use the `CODE_STANDARD`
model. The underling model may be swapped in one place — in `src/models.yaml` —
without needing to update the configuration of multiple agents.

These Modelfiles do NOT specify system prompts (via the `SYSTEM` block). This
is expected to be configured in the agent harness.

## 📦 Models

See [**`./src/models.yaml`**](./src/models.yaml) for the models configuration.

Models are named `<DOMAIN>_<TIER>`. The **domain** is the material the model
works over. The **tier** is how much model the work needs to do. Deeper work
needs a more capable, bigger model.

<!-- NOTE: This table needs to be kept synchronized with skills → create-skill
→ reference: choosing the preferred model. -->

| Capability          | Use cases                                                                   |
| ------------------- | --------------------------------------------------------------------------- |
| `WORKFLOW_BASIC`    | Workloads that run a fixed procedure requiring no judgment.                 |
| `WORKFLOW_STANDARD` | Applying a documented convention or readiness gate to a concrete case.      |
| `CODE_BASIC`        | Small edits to code where the change itself is already determined.          |
| `CODE_STANDARD`     | Writing and modifying program code from scratch. Diagnosing issues.         |
| `ANALYSIS_STANDARD` | Reasoning over a bounded problem, or eliciting from the user interactively. |
| `ANALYSIS_DEEP`     | Reasoning open-endedly, or synthesizing over a large corpus.                |
| `PROSE_STANDARD`    | Editing or summarizing text that already exists.                            |
| `PROSE_DEEP`        | Authoring a structured document from scratch.                               |
| `SECURITY_DEEP`     | Reasoning adversarially about a system.                                     |

Several of the custom models share a base model, differing only in their settings
for temperature and context window.

## 🛠️ Requirements

A native [Ollama](https://ollama.com) install on the host, to create and run
the models:

```bash
ollama --version
```

Python 3 with [PyYAML](https://pyyaml.org/), to compile the Modelfiles from
[`models.yaml`](../src/models.yaml):

```bash
python3 -c 'import yaml'
```

## 🚀 Usage

use `./run/build` to compile the Modelfiles from the
[`models.yaml`](../src/models.yaml) config.

With no argument this builds the `default` profile. Pass a profile name
to build that profile instead:

```bash
./run/build              # Default profile (installs cloud models only).
./run/build workstation  # A named profile.
```

The compiled Modelfiles are written to `dist/<profile>/<model-name>/Modelfile`.

Next, create a custom model in Ollama from one of the compiled Modelfiles:

```bash
ollama create <model-name> -f ./dist/<profile>/<model-name>/Modelfile
```

Repeat for each of the Modelfiles you want to use. Ollama will pull any base
models defined in the Modelfile.

Run the model directly in Ollama as you would any other model:

```bash
ollama run <model-name>
```

List installed models, or remove one:

```bash
ollama list
ollama rm <model-name>
```

## 📓 Developer docs

See the [contributing guidelines](./CONTRIBUTING.md).

-----

Copyright © 2020-present Kieran Potts, [MIT license](./LICENSE.txt)

[modelfile-spec]: https://docs.ollama.com/modelfile
