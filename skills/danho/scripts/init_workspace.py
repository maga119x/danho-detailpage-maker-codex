#!/usr/bin/env python3
"""Initialize a Danho detail-page working directory with AGENT.MD."""

from __future__ import annotations

import argparse
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create AGENT.MD for a Danho detail-page workspace."
    )
    parser.add_argument(
        "--target",
        default=".",
        help="Workspace directory to initialize. Defaults to the current directory.",
    )
    parser.add_argument(
        "--filename",
        default="AGENT.MD",
        help="Instruction filename to create. Defaults to AGENT.MD.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing file.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    skill_dir = Path(__file__).resolve().parents[1]
    template_path = skill_dir / "assets" / "AGENT.MD.template.md"
    target_dir = Path(args.target).expanduser().resolve()
    output_path = target_dir / args.filename

    if not template_path.exists():
        raise SystemExit(f"Template not found: {template_path}")

    target_dir.mkdir(parents=True, exist_ok=True)

    if output_path.exists() and not args.force:
        print(f"exists: {output_path}")
        print("No changes made. Re-run with --force to overwrite.")
        return 0

    content = template_path.read_text(encoding="utf-8")
    output_path.write_text(content, encoding="utf-8", newline="\n")
    print(f"created: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
