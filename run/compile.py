#!/usr/bin/env python3

"""
Compile Ollama Modelfiles from src/models.yaml.

Reads the target profile and writes one Modelfile per model it defines to
dist/<profile>/<model>/Modelfile. Each profile is self-contained. Only the
models defined for the target profile are compiled.

Invoked by run/build. Run that rather than this script directly.

Usage: compile.py [profile]   (profile defaults to "default")
"""

import sys
from pathlib import Path

import yaml

# Order in which PARAMETER lines are emitted, when present.
PARAM_ORDER = ("temperature", "top_p", "num_ctx", "stop")

REPO_ROOT = Path(__file__).resolve().parent.parent
SOURCE = REPO_ROOT / "src" / "models.yaml"


def die(message: str) -> None:
    print(f"compile: {message}", file=sys.stderr)
    sys.exit(1)


def render(params: dict) -> str:
    """Build the text of a single Modelfile from a model's parameters."""
    out = [f"FROM {params['from']}"]
    for key in PARAM_ORDER:
        if key in params:
            out.append(f"PARAMETER {key} {params[key]}")
    return "\n".join(out) + "\n"


def main() -> None:
    profile = sys.argv[1] if len(sys.argv) > 1 else "default"

    if not SOURCE.is_file():
        die(f"source config not found: {SOURCE}")

    config = yaml.safe_load(SOURCE.read_text()) or {}
    profiles = config.get("profiles") or {}

    if "default" not in profiles:
        die("src/models.yaml has no `default` profile")
    if profile not in profiles:
        available = ", ".join(sorted(profiles)) or "(none)"
        die(f"unknown profile '{profile}'. Available: {available}")

    models = profiles[profile] or {}
    if not models:
        die(f"profile '{profile}' defines no models")

    out_dir = REPO_ROOT / "dist" / profile
    written = []
    for name, params in models.items():
        if not isinstance(params, dict) or "from" not in params:
            die(f"model '{name}' in profile '{profile}' has no `from` (base model)")

        target = out_dir / name / "Modelfile"
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(render(params))
        written.append(target.relative_to(REPO_ROOT))

    print(f"Compiled {len(written)} Modelfile(s) for profile '{profile}':")
    for path in written:
        print(f"  {path}")


if __name__ == "__main__":
    main()
