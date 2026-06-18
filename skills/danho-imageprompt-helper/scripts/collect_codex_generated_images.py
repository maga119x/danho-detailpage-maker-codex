#!/usr/bin/env python3
"""Find and copy Codex native image outputs from generated_images or session JSONL."""

from __future__ import annotations

import argparse
import base64
import hashlib
import os
import json
import shutil
from datetime import datetime, timedelta
from pathlib import Path


IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp"}


def parse_local_datetime(value: str) -> datetime:
    normalized = value.strip().replace("Z", "+00:00")
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is not None:
        parsed = parsed.astimezone().replace(tzinfo=None)
    return parsed


def default_root() -> Path:
    return Path.home() / ".codex" / "generated_images"


def default_temp_root() -> Path:
    return Path(os.environ.get("TEMP") or os.environ.get("TMP") or Path.home())


def default_sessions_root() -> Path:
    return Path.home() / ".codex" / "sessions"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def find_candidates(root: Path, after: datetime | None, limit: int) -> list[Path]:
    if not root.exists():
        return []

    files: list[Path] = []
    for path in root.rglob("ig_*"):
        if not path.is_file() or path.suffix.lower() not in IMAGE_SUFFIXES:
            continue
        if after and datetime.fromtimestamp(path.stat().st_mtime) < after:
            continue
        files.append(path)

    files.sort(key=lambda item: item.stat().st_mtime, reverse=True)
    return files[:limit]


def find_clipboard_candidates(root: Path, after: datetime | None, limit: int) -> list[Path]:
    if not root.exists():
        return []

    files: list[Path] = []
    for path in root.glob("codex-clipboard-*.png"):
        if not path.is_file():
            continue
        if after and datetime.fromtimestamp(path.stat().st_mtime) < after:
            continue
        files.append(path)

    files.sort(key=lambda item: item.stat().st_mtime, reverse=True)
    return files[:limit]


def parse_event_timestamp(value: str) -> datetime:
    return parse_local_datetime(value)


def find_session_image_events(root: Path, after: datetime | None, limit: int) -> list[dict[str, object]]:
    if not root.exists():
        return []

    events: list[dict[str, object]] = []
    session_files = sorted(root.rglob("*.jsonl"), key=lambda item: item.stat().st_mtime, reverse=True)
    for session_path in session_files:
        if after and datetime.fromtimestamp(session_path.stat().st_mtime) < after:
            continue
        try:
            with session_path.open("r", encoding="utf-8") as handle:
                for line_number, line in enumerate(handle, 1):
                    if '"image_generation_end"' not in line or '"result"' not in line:
                        continue
                    try:
                        item = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    payload = item.get("payload") if isinstance(item, dict) else None
                    if not isinstance(payload, dict):
                        continue
                    if payload.get("type") != "image_generation_end":
                        continue
                    result = payload.get("result")
                    if not isinstance(result, str) or not result:
                        continue
                    timestamp_raw = item.get("timestamp") if isinstance(item.get("timestamp"), str) else ""
                    try:
                        timestamp = parse_event_timestamp(timestamp_raw) if timestamp_raw else datetime.fromtimestamp(session_path.stat().st_mtime)
                    except ValueError:
                        timestamp = datetime.fromtimestamp(session_path.stat().st_mtime)
                    if after and timestamp < after:
                        continue
                    events.append(
                        {
                            "timestamp": timestamp,
                            "timestamp_raw": timestamp_raw,
                            "call_id": payload.get("call_id"),
                            "status": payload.get("status"),
                            "session_path": str(session_path),
                            "line_number": line_number,
                            "result_base64": result,
                            "result_chars": len(result),
                            "estimated_bytes": (len(result) * 3) // 4,
                            "revised_prompt": payload.get("revised_prompt"),
                        }
                    )
        except OSError:
            continue

    events.sort(key=lambda item: item["timestamp"], reverse=True)
    return events[:limit]


def public_session_record(event: dict[str, object]) -> dict[str, object]:
    return {
        "timestamp": event.get("timestamp_raw") or event.get("timestamp"),
        "call_id": event.get("call_id"),
        "status": event.get("status"),
        "session_path": event.get("session_path"),
        "line_number": event.get("line_number"),
        "result_chars": event.get("result_chars"),
        "estimated_bytes": event.get("estimated_bytes"),
        "revised_prompt": event.get("revised_prompt"),
    }


def record_for(path: Path, root: Path) -> dict[str, object]:
    stat = path.stat()
    try:
        relative = path.relative_to(root)
    except ValueError:
        relative = path

    return {
        "path": str(path),
        "relative": str(relative),
        "size": stat.st_size,
        "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds"),
        "sha256": sha256(path),
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="List or copy Codex native image outputs from generated_images or session JSONL."
    )
    parser.add_argument("--root", type=Path, default=default_root(), help="Generated images root.")
    parser.add_argument("--temp-root", type=Path, default=default_temp_root(), help="Temp root for Codex clipboard diagnostics.")
    parser.add_argument("--sessions-root", type=Path, default=default_sessions_root(), help="Codex sessions root for JSONL image result recovery.")
    parser.add_argument("--minutes", type=float, default=240, help="Look back this many minutes.")
    parser.add_argument("--after", help="Only include files modified after this ISO datetime.")
    parser.add_argument("--limit", type=int, default=30, help="Maximum candidates to list.")
    parser.add_argument("--list", action="store_true", help="List recent generated images.")
    parser.add_argument("--diagnose", action="store_true", help="List generated_images plus Codex clipboard captures for troubleshooting.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    parser.add_argument("--copy", type=Path, help="Copy this generated image source.")
    parser.add_argument("--copy-latest", action="store_true", help="Copy the newest matching image.")
    parser.add_argument("--copy-latest-session", action="store_true", help="Decode and copy the newest session JSONL image_generation_end result.")
    parser.add_argument("--to", type=Path, help="Destination path inside the project.")
    parser.add_argument("--force", action="store_true", help="Overwrite destination if it exists.")
    parser.add_argument("--dry-run", action="store_true", help="Show copy action without writing.")
    args = parser.parse_args()

    root = args.root.expanduser().resolve()
    temp_root = args.temp_root.expanduser().resolve()
    sessions_root = args.sessions_root.expanduser().resolve()
    after = parse_local_datetime(args.after) if args.after else datetime.now() - timedelta(minutes=args.minutes)
    candidates = find_candidates(root, after, args.limit)
    clipboard_candidates = find_clipboard_candidates(temp_root, after, args.limit) if args.diagnose else []
    session_events = find_session_image_events(sessions_root, after, args.limit) if args.diagnose or args.copy_latest_session else []

    selected: Path | None = None
    selected_session_event: dict[str, object] | None = None
    if args.copy:
        selected = args.copy.expanduser().resolve()
    elif args.copy_latest:
        if not candidates:
            raise SystemExit(f"No ig_* image files found under {root} after {after.isoformat(timespec='seconds')}")
        selected = candidates[0]
    elif args.copy_latest_session:
        if not session_events:
            raise SystemExit(f"No session image_generation_end results found under {sessions_root} after {after.isoformat(timespec='seconds')}")
        selected_session_event = session_events[0]

    if selected or selected_session_event:
        if not args.to:
            raise SystemExit("--to is required when copying")

        destination = args.to.expanduser().resolve()
        if destination.exists() and not args.force:
            raise SystemExit(f"Destination exists; pass --force to overwrite: {destination}")

        if selected:
            if not selected.exists():
                raise SystemExit(f"Source does not exist: {selected}")
            if selected.suffix.lower() not in IMAGE_SUFFIXES:
                raise SystemExit(f"Source is not a supported image file: {selected}")

            result = {
                "source_kind": "generated_images_file",
                "source": record_for(selected, root),
                "destination": str(destination),
                "dry_run": args.dry_run,
            }
            if not args.dry_run:
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(selected, destination)
                result["copied"] = True
                result["destination_sha256"] = sha256(destination)
        else:
            encoded = selected_session_event.get("result_base64")
            if not isinstance(encoded, str):
                raise SystemExit("Selected session event has no result_base64")
            result = {
                "source_kind": "session_jsonl_image_generation_end",
                "source": public_session_record(selected_session_event),
                "destination": str(destination),
                "dry_run": args.dry_run,
            }
            if not args.dry_run:
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(base64.b64decode(encoded))
                result["copied"] = True
                result["destination_sha256"] = sha256(destination)

        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    records = [record_for(path, root) for path in candidates]
    clipboard_records = [record_for(path, temp_root) for path in clipboard_candidates]
    session_records = [public_session_record(event) for event in session_events]
    if args.json:
        print(json.dumps(
            {
                "root": str(root),
                "temp_root": str(temp_root),
                "sessions_root": str(sessions_root),
                "after": after.isoformat(timespec="seconds"),
                "images": records,
                "session_image_events": session_records,
                "codex_clipboard_captures": clipboard_records,
                "diagnostic_note": (
                    "session_image_events are native image_generation_end results from Codex session JSONL and can be decoded as native outputs. "
                    "codex-clipboard files are user/UI captures. They prove a preview was visible, but they are not accepted as native generated assets "
                    "unless the user explicitly provides the actual generated image file, not a screenshot of the conversation."
                ) if args.diagnose else None,
            },
            ensure_ascii=False,
            indent=2,
        ))
    else:
        print(f"root: {root}")
        print(f"after: {after.isoformat(timespec='seconds')}")
        for index, item in enumerate(records, 1):
            print(f"{index:02d} {item['modified']} {item['size']} {item['path']}")
        if args.diagnose:
            print(f"sessions_root: {sessions_root}")
            print("session_image_events:")
            for index, item in enumerate(session_records, 1):
                print(
                    f"{index:02d} {item['timestamp']} {item['estimated_bytes']} "
                    f"{item['call_id']} {item['session_path']}:{item['line_number']}"
                )
            print(f"temp_root: {temp_root}")
            print("codex_clipboard_captures:")
            for index, item in enumerate(clipboard_records, 1):
                print(f"{index:02d} {item['modified']} {item['size']} {item['path']}")
            print(
                "note: session_image_events can be decoded as native outputs; codex-clipboard files are user/UI captures, not accepted native output provenance by themselves."
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
