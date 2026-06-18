#!/usr/bin/env python3
"""Prepare user-provided reference detail-page design files for analysis."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

from PIL import Image


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".webp"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy reference design files into a project and slice tall images."
    )
    parser.add_argument(
        "--project",
        required=True,
        help="Project directory containing PLANNING.md/DESIGN.md or where they will be created.",
    )
    parser.add_argument(
        "--slice-height",
        type=int,
        default=1400,
        help="Pixel height for tall-image slices. Defaults to 1400.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing copied originals and slices.",
    )
    parser.add_argument("files", nargs="+", help="Reference design files to prepare.")
    return parser.parse_args()


def unique_destination(path: Path, force: bool) -> Path:
    if force or not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    index = 2
    while True:
        candidate = parent / f"{stem}-{index}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def slice_image(source: Path, slices_dir: Path, slice_height: int, force: bool) -> list[Path]:
    slices_dir.mkdir(parents=True, exist_ok=True)
    if force:
        for old in slices_dir.glob("slice_*.png"):
            old.unlink()

    output_paths: list[Path] = []
    with Image.open(source) as image:
        width, height = image.size
        if height <= slice_height:
            return output_paths
        for idx, top in enumerate(range(0, height, slice_height), start=1):
            bottom = min(top + slice_height, height)
            crop = image.crop((0, top, width, bottom))
            output = slices_dir / f"slice_{idx:02d}.png"
            crop.save(output)
            output_paths.append(output)
    return output_paths


def image_size(path: Path) -> tuple[int | None, int | None]:
    if path.suffix.lower() not in IMAGE_EXTENSIONS:
        return None, None
    with Image.open(path) as image:
        return image.size


def main() -> int:
    args = parse_args()
    project = Path(args.project).expanduser().resolve()
    original_dir = project / "assets" / "reference-designs" / "originals"
    slices_root = project / "assets" / "reference-designs" / "slices"
    manifest = project / "assets" / "reference-designs" / "manifest.md"

    original_dir.mkdir(parents=True, exist_ok=True)
    slices_root.mkdir(parents=True, exist_ok=True)

    rows = [
        "# Reference Design Files",
        "",
        "| original | type | width | height | slices |",
        "|---|---|---:|---:|---|",
    ]

    for raw_file in args.files:
        source = Path(raw_file).expanduser().resolve()
        if not source.exists():
            raise SystemExit(f"Reference file not found: {source}")

        destination = unique_destination(original_dir / source.name, args.force)
        shutil.copy2(source, destination)

        ext = destination.suffix.lower()
        file_type = "REFERENCE_DETAILPAGE_IMAGE" if ext in IMAGE_EXTENSIONS else "REFERENCE_DETAILPAGE_FILE"
        width, height = image_size(destination)
        slice_paths: list[Path] = []
        if ext in IMAGE_EXTENSIONS:
            slice_paths = slice_image(
                destination,
                slices_root / destination.stem,
                args.slice_height,
                args.force,
            )

        rel_slices = ", ".join(str(p.relative_to(project)).replace("\\", "/") for p in slice_paths)
        if not rel_slices:
            rel_slices = "-"
        rows.append(
            "| {original} | {file_type} | {width} | {height} | {slices} |".format(
                original=str(destination.relative_to(project)).replace("\\", "/"),
                file_type=file_type,
                width=width if width is not None else "",
                height=height if height is not None else "",
                slices=rel_slices,
            )
        )

    manifest.write_text("\n".join(rows) + "\n", encoding="utf-8", newline="\n")
    print(f"prepared: {manifest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
