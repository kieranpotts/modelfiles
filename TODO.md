# TODO

## Ollama: custom cloud-based models lose tool-calling capability

**Symptom:** `workstation/ANALYSIS_DEEP` (and `ANALYSIS_STANDARD`) show up in `ollama ls`,
but Zed reports no tools available for the model, and it doesn't appear at all in the
VS Code Chat model picker.

**Root cause:** Both models are built with `FROM deepseek-v4-flash:cloud` plus only
`PARAMETER` lines (see `dist/workstation/ANALYSIS_DEEP/Modelfile`). When `ollama create`
builds a model from a `:cloud` remote base, it does not inherit the parent's `model_info`
(context length, architecture, base name, etc.) or capability metadata (`tools`,
`completion`, `thinking`). `ollama show` on the derived model returns an empty
Capabilities section, whereas `ollama show deepseek-v4-flash:cloud` correctly lists
`completion`, `tools`, `thinking`.

Confirmed via a minimal repro: even `FROM deepseek-v4-flash:cloud` + a single
`PARAMETER temperature` line, with nothing else touched, produces a model with no
capabilities reported. Not specific to this Modelfile's content — it's an Ollama bug
in how `ollama create` handles `:cloud` bases.

Zed and VS Code both query `/api/show` to decide whether to enable tool-calling or list
a model as chat-selectable at all. Empty capabilities → Zed disables tools, VS Code
filters the model out of the picker.

**Known upstream issue:** [ollama/ollama#16891](https://github.com/ollama/ollama/issues/16891)
— "ollama create does not inherit model_info from parent model — context_length is
lost" (open, labeled `cloud`). Filer's repro is the same pattern (`FROM x:cloud` +
`PARAMETER`) and calls out the same VS Code breakage via `model_info`.

**Fix in progress:** [ollama/ollama#16956](https://github.com/ollama/ollama/pull/16956)
(open, not merged) — patches `server/create.go` to copy `ModelFamily`,
`ModelFamilies`, `ModelType`, `FileType`, `ContextLen`, `EmbedLen`, `BaseName` from the
parent manifest when creating from a base model whose manifest is present locally.
Doesn't explicitly mention capability tags (`tools`/`thinking`) but likely fixes them
as a side effect since capability advertisement is derived from the same config.

**No workaround exists today** other than pointing Zed/VS Code at the base
`deepseek-v4-flash:cloud` model directly (unwrapped, no custom parameters) when tool
support is required. `ANALYSIS_DEEP`/`ANALYSIS_STANDARD` remain usable via `ollama run`
on the CLI, where the capability gate doesn't apply.

**Next steps:**
- [ ] Watch ollama/ollama#16956 for merge; re-test `ANALYSIS_DEEP` capabilities after
      upgrading once it ships.
- [ ] Consider commenting on #16891 with the tools/capabilities angle — the issue as
      filed only discusses `context_length`, not the broader capability-tag loss.
- [ ] Decide whether other `dist/workstation/*` models built `FROM *:cloud` have the
      same gap (likely all of them, given the repro was base-agnostic).
