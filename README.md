# Modelfiles

**Custom model definitions for running in [Ollama](https://ollama.com).**

Each model is defined by an Ollama [Modelfile][modelfile-spec],
a plain-text recipe that takes a base model and tunes it into a reusable capability.

The Modelfiles are compiled from a single [source config](./src/models.yaml)
by [`run/build`](./run/build). Multiple profiles may be configured, allowing
different model configurations for different target machines — eg. local
models for workstations, cloud models for laptops.

```bash
./run/build              # Compile the default profile → dist/default/
./run/build workstation  # Compile a named profile     → dist/workstation/
```

The Modelfiles define generic capabilities, which can be reused for agents
performing different roles. For example, the same base model could be reused
for a software tester agent and a software architect agent. For this reason,
the Modelfiles do NOT specify a system prompt (via the `SYSTEM` block) — this
is expected to be supplied by the agent harness, defining the agent's role.

## 📦 Models

See [**`./src/models.yaml`**](./src/models.yaml) for the models configuration.

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
./run/build              # Default profile.
./run/build workstation  # A named profile.
```

The compiled Modelfiles are written to `dist/<profile>/<model-name>/Modelfile`.

Next, create a custom model in Ollama from one of the compiled Modelfiles:

```bash
ollama create <model-name> -f ./dist/<profile>/<model-name>/Modelfile
```

Repeat for each of the Modelfiles you want to use.

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
