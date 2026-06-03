#!/usr/bin/env python3
"""
create-workspace.py — materialize a fresh ieops project workspace.

Usage:
    python3 create-workspace.py <name-or-path>

Single positional argument:
    - A name (e.g. "my-project"): destination is ~/ieops-workspaces/<name>/.
    - An absolute path or ~/-prefixed path: used as-is.

Copies `workspace-template/` verbatim into the destination (zero variable
substitution), then runs `git init` and makes one initial commit. The new
workspace opens in a bootstrap state: its vision is not yet set.

Exits non-zero on any failure with a clear, actionable message.
"""

from __future__ import annotations

import argparse
import atexit
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


# ---------- errors ----------

class ActionableError(SystemExit):
    """Exits with code 1 and a structured message: what happened + what to do."""

    def __init__(self, what: str, found: str, action: str):
        msg = (
            f"\nERROR: {what}\n"
            f"  Found: {found}\n"
            f"  Action: {action}\n"
        )
        super().__init__(msg)


# ---------- Source ----------

@dataclass
class Source:
    """The ieops repo checkout. Locates the workspace template.

    Unlike a deliverable-generating scaffolder, ieops ships the template
    verbatim — there is no annotated-source/render step — so the source need
    not be a git repository or have a clean working tree. The only
    preconditions are that git is installed (used to init the new workspace)
    and that the template directory is present and non-empty.
    """

    cwd: Path

    TEMPLATE_DIR = "workspace-template"

    def verify(self) -> None:
        if shutil.which("git") is None:
            raise ActionableError(
                what="git is not installed or not on PATH",
                found="`git` executable not found",
                action="install git from https://git-scm.com/downloads and re-run.",
            )

        template = self.cwd / self.TEMPLATE_DIR
        if not template.is_dir():
            raise ActionableError(
                what=f"template directory missing: {self.TEMPLATE_DIR}",
                found=f"expected directory at {template}",
                action=(
                    "run this script from the root of the ieops repo "
                    f"(the directory that contains `{self.TEMPLATE_DIR}/`)."
                ),
            )
        if not any(template.iterdir()):
            raise ActionableError(
                what=f"template directory is empty: {self.TEMPLATE_DIR}",
                found=f"no files under {template}",
                action="re-clone the ieops repo; the template appears incomplete.",
            )

    def template_path(self) -> Path:
        return self.cwd / self.TEMPLATE_DIR


# ---------- Destination ----------

@dataclass
class Destination:
    """The target directory. Hides path resolution and empty-vs-nonempty rules."""

    path: Path

    @classmethod
    def resolve(cls, name_or_path: str, default_parent: Path) -> "Destination":
        if name_or_path.startswith("~") or Path(name_or_path).is_absolute():
            raw = Path(name_or_path).expanduser()
        else:
            if "/" in name_or_path or "\\" in name_or_path or name_or_path in (".", ".."):
                raise ActionableError(
                    what="workspace name contains path separators or is a special name",
                    found=f"name={name_or_path!r}",
                    action=(
                        "use a simple name (letters, digits, dashes, underscores) "
                        "or an absolute path / ~-prefixed path."
                    ),
                )
            raw = default_parent.expanduser() / name_or_path

        resolved = raw.resolve() if raw.exists() else (raw.parent.resolve() / raw.name)

        if resolved.exists():
            if not resolved.is_dir():
                raise ActionableError(
                    what="destination path exists and is not a directory",
                    found=str(resolved),
                    action="remove the existing file or choose a different destination.",
                )
            if any(resolved.iterdir()):
                raise ActionableError(
                    what="destination directory exists and is not empty",
                    found=str(resolved),
                    action="choose a different name, or empty the directory first.",
                )

        parent = resolved.parent
        if not parent.exists():
            try:
                parent.mkdir(parents=True, exist_ok=True)
            except OSError as e:
                raise ActionableError(
                    what="cannot create parent directory for destination",
                    found=f"parent={parent}, error={e}",
                    action="check filesystem permissions and re-run.",
                )

        return cls(path=resolved)


# ---------- Repo ----------

class Repo:
    """Initialize a git repo and make one unattended initial commit."""

    @staticmethod
    def init_and_commit(path: Path, message: str) -> None:
        rc, out, err = _run_git(["init", "-b", "main"], cwd=path)
        if rc != 0:
            # Fall back if -b is unsupported (older git).
            rc, out, err = _run_git(["init"], cwd=path)
        if rc != 0:
            raise ActionableError(
                what="`git init` failed in the new workspace",
                found=f"exit code {rc}: {err.strip() or out.strip()}",
                action="investigate the destination and re-run.",
            )

        rc, out, err = _run_git(["add", "-A"], cwd=path)
        if rc != 0:
            raise ActionableError(
                what="`git add` failed in the new workspace",
                found=f"exit code {rc}: {err.strip() or out.strip()}",
                action="investigate the destination and re-run.",
            )

        # Per-invocation identity overrides — does not mutate global config.
        rc, out, err = _run_git(
            [
                "-c", "user.name=workspace-init",
                "-c", "user.email=workspace-init@localhost",
                "commit", "-m", message,
            ],
            cwd=path,
        )
        if rc != 0:
            raise ActionableError(
                what="`git commit` failed in the new workspace",
                found=f"exit code {rc}: {err.strip() or out.strip()}",
                action="investigate the destination and re-run.",
            )


# ---------- helpers ----------

def _run_git(args, cwd: Path) -> "tuple[int, str, str]":
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=str(cwd),
            capture_output=True,
            text=True,
            check=False,
        )
        return result.returncode, result.stdout, result.stderr
    except FileNotFoundError:
        return 127, "", "git: command not found"


def _ieops_workspaces_root() -> Path:
    return Path.home() / "ieops-workspaces"


# ---------- main ----------

def main(argv: Optional[list] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="create-workspace.py",
        description="Materialize a fresh ieops project workspace at the given destination.",
    )
    parser.add_argument(
        "name_or_path",
        help=(
            "Workspace name (placed under ~/ieops-workspaces/) or an absolute path "
            "/ ~-prefixed path to use directly."
        ),
    )
    args = parser.parse_args(argv)

    source = Source(cwd=Path.cwd())
    source.verify()

    template = source.template_path()

    destination = Destination.resolve(args.name_or_path, _ieops_workspaces_root())

    # Stage-then-rename: copy into a sibling temp directory, then os.rename atomically.
    # The destination is either fully present or absent — never a half-state.
    stage = destination.path.parent / (destination.path.name + ".staging.tmp")
    cleanup_done = {"value": False}

    def _cleanup() -> None:
        if cleanup_done["value"]:
            return
        if stage.exists():
            shutil.rmtree(stage, ignore_errors=True)

    atexit.register(_cleanup)

    # Crash-recovery: a prior run killed by SIGKILL / power loss may have left a
    # .staging.tmp directory behind. Clear it before copying.
    if stage.exists():
        shutil.rmtree(stage)

    try:
        shutil.copytree(template, stage)
    except OSError as e:
        raise ActionableError(
            what="failed to copy the template into the staging directory",
            found=f"error={e}",
            action="check filesystem permissions and available space, then re-run.",
        )

    Repo.init_and_commit(stage, message="Initial workspace")

    # If destination exists (empty), remove it so rename can land there.
    if destination.path.exists():
        try:
            destination.path.rmdir()
        except OSError as e:
            raise ActionableError(
                what="destination became non-empty during materialization",
                found=f"path={destination.path}, error={e}",
                action="ensure nothing is writing to the destination and re-run.",
            )

    try:
        os.rename(stage, destination.path)
    except OSError as e:
        raise ActionableError(
            what="failed to move the staged workspace into place",
            found=f"from={stage}, to={destination.path}, error={e}",
            action=(
                "this can happen across filesystem boundaries; verify "
                "the destination's parent is writable and on the same volume."
            ),
        )

    cleanup_done["value"] = True

    print(f"Workspace created at: {destination.path}")
    print("Open it with Claude Code; it will read CLAUDE.md / README.md and orient")
    print("you. The workspace vision is not yet set.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
