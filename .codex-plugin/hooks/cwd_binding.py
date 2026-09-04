#!/usr/bin/env python3
"""Codex PreToolUse hook — CWD binding enforcement (ADR-098 Tier 1, E-FLEET-1).

Precondición: session_id llega en el JSON stdin de Codex (campo 'session_id').
No hay env var equivalente a RAISE_CC_SESSION_ID en Codex v1.

Limitación v1: Todos los tools de Codex (shell_command, exec_command, apply_patch)
devuelven None de extract_target_path → fail-open. La infrastructure queda
instalada para cuando Codex exponga tools con file_path extraíble (ADR-098 §Lim).
"""
import json
import os
import sys
from pathlib import Path


def main() -> int:
    try:
        data: dict[str, object] = json.loads(sys.stdin.read() or "{}")
        cwd = str(data.get("cwd") or os.getcwd())
        from raise_cli.cwd_binding import LocalCoordinationStore, evaluate_pretooluse

        store = LocalCoordinationStore(project=Path(cwd))
        return evaluate_pretooluse(data, dict(os.environ), store)
    except ImportError:
        print(
            "[cwd-binding] WARNING: raise-cli not available — fail-open",
            file=sys.stderr,
        )
        return 0
    except Exception as exc:  # noqa: BLE001 — fail-open by design
        print(
            f"[cwd-binding] ERROR: internal failure — fail-open: {exc}",
            file=sys.stderr,
        )
        return 0


if __name__ == "__main__":
    sys.exit(main())
