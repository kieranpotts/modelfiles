# Development

Each custom model lives in its own directory under [`src/`](../src):

```
src/
  <model-name>/
    Modelfile    # The Ollama model definition.
    README.md    # Purpose, base model, and build/run commands.
```

The [`template/`](../template) directory contains starter files for defining a new model.

## Adding a new model

1. Copy [`template/`](../template) to `src/<model-name>/`.
2. Edit the `Modelfile` — set the `FROM` base model and customize it.
3. Fill in the `README.md` for the model.
4. Build and test it (see [Usage](./usage.md)).
