#!/usr/bin/env python3
"""
Placeholder Replacement Script for Korean E-commerce Product Detail Pages

Parses HTML files and replaces {{PLACEHOLDER:...}} keywords with base64 placeholder images.

Keyword Format:
    {{PLACEHOLDER:description:width:height:theme}}

    - description: Korean/English text describing the image
    - width: Image width in pixels (default: 860)
    - height: Image height in pixels (default: 600)
    - theme: light, dark, or warm (default: light)

Usage:
    python replace_placeholders.py input.html output.html
    python replace_placeholders.py input.html  # Overwrites input file
    python replace_placeholders.py input.html --dry-run  # Preview changes

Requirements:
    pip install Pillow
"""

import argparse
import re
import sys
from pathlib import Path

# Import the placeholder generator from the same directory
try:
    from generate_placeholder import generate_placeholder, image_to_base64
except ImportError:
    # Try relative import for when run as module
    try:
        from .generate_placeholder import generate_placeholder, image_to_base64
    except ImportError:
        print("Error: generate_placeholder.py must be in the same directory")
        sys.exit(1)


# Regex pattern for placeholder keywords
# Format: {{PLACEHOLDER:description:width:height:theme}}
# Only description is required; others have defaults
PLACEHOLDER_PATTERN = re.compile(
    r'\{\{PLACEHOLDER:([^:}]+)(?::(\d+))?(?::(\d+))?(?::(light|dark|warm))?\}\}'
)


def parse_placeholder(match: re.Match) -> dict:
    """Parse a placeholder match into parameters."""
    description = match.group(1).strip()
    width = int(match.group(2)) if match.group(2) else 860
    height = int(match.group(3)) if match.group(3) else 600
    theme = match.group(4) if match.group(4) else "light"

    return {
        "description": description,
        "width": width,
        "height": height,
        "theme": theme,
        "original": match.group(0)
    }


def generate_base64_placeholder(params: dict) -> str:
    """Generate a base64 placeholder image from parameters."""
    img = generate_placeholder(
        description=params["description"],
        width=params["width"],
        height=params["height"],
        theme=params["theme"],
        show_dimensions=True
    )
    return image_to_base64(img)


def replace_placeholders(html_content: str, dry_run: bool = False) -> tuple[str, list]:
    """
    Replace all placeholder keywords in HTML with base64 images.

    Args:
        html_content: HTML string to process
        dry_run: If True, don't actually replace, just report findings

    Returns:
        Tuple of (processed HTML, list of replacement info)
    """
    replacements = []

    # Find all placeholders
    matches = list(PLACEHOLDER_PATTERN.finditer(html_content))

    if not matches:
        return html_content, []

    # Process each placeholder
    result = html_content
    for match in reversed(matches):  # Reverse to maintain positions during replacement
        params = parse_placeholder(match)

        if dry_run:
            replacements.append({
                "original": params["original"],
                "description": params["description"],
                "size": f"{params['width']}x{params['height']}",
                "theme": params["theme"],
                "position": match.start()
            })
        else:
            base64_str = generate_base64_placeholder(params)
            result = result[:match.start()] + base64_str + result[match.end():]
            replacements.append({
                "original": params["original"],
                "description": params["description"],
                "size": f"{params['width']}x{params['height']}",
                "theme": params["theme"],
                "replaced": True
            })

    return result, replacements


def process_file(input_path: Path, output_path: Path = None, dry_run: bool = False) -> bool:
    """
    Process an HTML file and replace placeholders.

    Args:
        input_path: Path to input HTML file
        output_path: Path to output file (None = overwrite input)
        dry_run: If True, don't write, just report

    Returns:
        True if successful, False otherwise
    """
    try:
        # Read input file
        with open(input_path, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Process placeholders
        result, replacements = replace_placeholders(html_content, dry_run)

        # Report findings
        if replacements:
            print(f"\nFound {len(replacements)} placeholder(s):")
            for i, r in enumerate(replacements, 1):
                print(f"  {i}. {r['description']} ({r['size']}, {r['theme']})")
        else:
            print("\nNo placeholders found.")
            return True

        if dry_run:
            print("\n[Dry run] No changes written.")
            return True

        # Write output
        out_path = output_path or input_path
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(result)

        print(f"\nSuccessfully replaced {len(replacements)} placeholder(s).")
        print(f"Output written to: {out_path}")
        return True

    except FileNotFoundError:
        print(f"Error: File not found: {input_path}")
        return False
    except Exception as e:
        print(f"Error processing file: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Replace {{PLACEHOLDER:...}} keywords with base64 images"
    )
    parser.add_argument(
        "input",
        help="Input HTML file path"
    )
    parser.add_argument(
        "output",
        nargs="?",
        help="Output HTML file path (optional, defaults to overwriting input)"
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Preview changes without writing"
    )

    args = parser.parse_args()

    input_path = Path(args.input)
    output_path = Path(args.output) if args.output else None

    success = process_file(input_path, output_path, args.dry_run)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
