#!/usr/bin/env python3
"""
Placeholder Image Generator - Asset File Version

HTML 파일에서 플레이스홀더 키워드를 찾아 실제 PNG 파일로 생성하고
assets/placeholders/ 디렉토리에 저장한 후 HTML 경로를 업데이트합니다.

키워드 형식:
    {{PLACEHOLDER:description:width:height:theme}}

사용법:
    python generate_placeholders_to_assets.py <project_dir>
    python generate_placeholders_to_assets.py projects/01251245_sleep-asmr-earphone
    python generate_placeholders_to_assets.py projects/my-product --dry-run

Requirements:
    pip install Pillow
"""

import argparse
import re
import sys
import hashlib
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: Pillow library required. Install with: pip install Pillow")
    sys.exit(1)


# ============================================================
# THEME CONFIGURATIONS
# ============================================================

THEMES = {
    "light": {
        "bg": "#F5F5F5",
        "frame": "#E0E0E0",
        "frame_inner": "#EEEEEE",
        "text": "#757575",
        "text_secondary": "#9E9E9E",
        "icon": "#BDBDBD",
    },
    "dark": {
        "bg": "#1E1E1E",
        "frame": "#333333",
        "frame_inner": "#2A2A2A",
        "text": "#9E9E9E",
        "text_secondary": "#757575",
        "icon": "#4A4A4A",
    },
    "warm": {
        "bg": "#F5EFE6",
        "frame": "#D9CFC2",
        "frame_inner": "#EBE3D6",
        "text": "#8A7A68",
        "text_secondary": "#A99B8A",
        "icon": "#C4B5A5",
    },
}


# ============================================================
# IMAGE GENERATION FUNCTIONS
# ============================================================

def hex_to_rgb(hex_color: str) -> tuple:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def get_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    """Get a font with fallback."""
    font_candidates = [
        "malgun.ttf",           # Malgun Gothic (Windows)
        "NanumGothic.ttf",      # Nanum Gothic
        "AppleGothic.ttf",      # Apple Gothic (macOS)
        "NotoSansKR-Regular.otf",
        "arial.ttf",
    ]

    if bold:
        font_candidates = [
            "malgunbd.ttf",
            "NanumGothicBold.ttf",
            "NotoSansKR-Bold.otf",
            "arialbd.ttf",
        ] + font_candidates

    for font_name in font_candidates:
        try:
            return ImageFont.truetype(font_name, size)
        except (OSError, IOError):
            continue

    try:
        return ImageFont.load_default()
    except:
        return None


def draw_rounded_rect(draw: ImageDraw.Draw, xy: tuple, radius: int,
                      fill: str = None, outline: str = None, width: int = 1):
    """Draw a rounded rectangle."""
    x1, y1, x2, y2 = xy
    fill_rgb = hex_to_rgb(fill) if fill else None
    outline_rgb = hex_to_rgb(outline) if outline else None

    try:
        draw.rounded_rectangle(xy, radius=radius, fill=fill_rgb,
                              outline=outline_rgb, width=width)
    except AttributeError:
        # Fallback for older Pillow versions
        draw.ellipse([x1, y1, x1 + 2*radius, y1 + 2*radius],
                    fill=fill_rgb, outline=outline_rgb)
        draw.ellipse([x2 - 2*radius, y1, x2, y1 + 2*radius],
                    fill=fill_rgb, outline=outline_rgb)
        draw.ellipse([x1, y2 - 2*radius, x1 + 2*radius, y2],
                    fill=fill_rgb, outline=outline_rgb)
        draw.ellipse([x2 - 2*radius, y2 - 2*radius, x2, y2],
                    fill=fill_rgb, outline=outline_rgb)
        draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill_rgb)
        draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill_rgb)


def draw_camera_icon(draw: ImageDraw.Draw, center: tuple, size: int, color: str):
    """Draw a simple camera icon."""
    cx, cy = center
    color_rgb = hex_to_rgb(color)

    body_width = size
    body_height = int(size * 0.7)
    body_radius = int(size * 0.15)

    draw_rounded_rect(
        draw,
        (cx - body_width//2, cy - body_height//2,
         cx + body_width//2, cy + body_height//2),
        radius=body_radius,
        fill=None,
        outline=color,
        width=3
    )

    lens_radius = int(size * 0.2)
    draw.ellipse(
        [cx - lens_radius, cy - lens_radius, cx + lens_radius, cy + lens_radius],
        fill=None,
        outline=color_rgb,
        width=3
    )

    bump_width = int(size * 0.25)
    bump_height = int(size * 0.12)
    bump_y = cy - body_height//2 - bump_height
    draw.rectangle(
        [cx - bump_width//2, bump_y, cx + bump_width//2, cy - body_height//2 + 2],
        fill=color_rgb
    )


def get_text_size(draw: ImageDraw.Draw, text: str, font) -> tuple:
    """Get text dimensions."""
    try:
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]
    except AttributeError:
        return draw.textsize(text, font=font)


def wrap_text(draw: ImageDraw.Draw, text: str, font, max_width: int) -> list:
    """
    Wrap text to fit within max_width.
    Returns list of lines.
    """
    # Split by comma or space for natural breaks
    words = []
    for segment in text.split(','):
        segment = segment.strip()
        if segment:
            words.append(segment + ',')
    # Remove trailing comma from last word
    if words and words[-1].endswith(','):
        words[-1] = words[-1][:-1]

    # If no commas, split by spaces
    if len(words) <= 1:
        words = text.split()

    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        test_width, _ = get_text_size(draw, test_line, font)

        if test_width <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    # Limit to 3 lines max
    if len(lines) > 3:
        lines = lines[:3]
        lines[2] = lines[2][:20] + '...' if len(lines[2]) > 20 else lines[2] + '...'

    return lines


def generate_placeholder_image(
    description: str,
    width: int = 860,
    height: int = 600,
    theme: str = "light",
    show_dimensions: bool = True,
) -> Image.Image:
    """Generate a placeholder image."""
    colors = THEMES.get(theme, THEMES["light"])

    img = Image.new("RGB", (width, height), hex_to_rgb(colors["bg"]))
    draw = ImageDraw.Draw(img)

    padding = min(width, height) * 0.06
    frame_radius = min(width, height) * 0.03

    # Draw outer frame
    draw_rounded_rect(
        draw,
        (padding, padding, width - padding, height - padding),
        radius=int(frame_radius),
        fill=colors["frame_inner"],
        outline=colors["frame"],
        width=2
    )

    # Draw inner border
    inner_padding = padding + 15
    draw_rounded_rect(
        draw,
        (inner_padding, inner_padding, width - inner_padding, height - inner_padding),
        radius=int(frame_radius * 0.8),
        fill=None,
        outline=colors["frame"],
        width=1
    )

    center_x = width // 2
    center_y = height // 2

    # Camera icon - adjust position based on expected text lines
    icon_size = min(width, height) * 0.12
    draw_camera_icon(draw, (center_x, center_y - 60), int(icon_size), colors["icon"])

    # Description text
    font_size_main = max(16, min(24, width // 30))
    font_size_sub = max(14, min(18, width // 40))

    font_main = get_font(font_size_main, bold=True)
    font_sub = get_font(font_size_sub)

    # Calculate max text width (with padding)
    max_text_width = int((width - padding * 2) * 0.85)

    # Wrap text to multiple lines
    if font_main:
        lines = wrap_text(draw, description, font_main, max_text_width)
        line_height = font_size_main + 8

        # Calculate starting Y position to center text block
        total_text_height = len(lines) * line_height
        text_y = center_y + 10 - (total_text_height // 4)

        # Draw each line centered
        for line in lines:
            line_width, _ = get_text_size(draw, line, font_main)
            draw.text(
                (center_x - line_width // 2, text_y),
                line,
                font=font_main,
                fill=hex_to_rgb(colors["text"])
            )
            text_y += line_height

        text_y += 8  # Extra spacing before dimension

    # Dimension text
    if show_dimensions and font_sub:
        dim_text = f"{width}px x {height}px"
        dim_width, _ = get_text_size(draw, dim_text, font_sub)
        draw.text(
            (center_x - dim_width // 2, text_y),
            dim_text,
            font=font_sub,
            fill=hex_to_rgb(colors["text_secondary"])
        )

    return img


# ============================================================
# PLACEHOLDER PROCESSING
# ============================================================

# Regex pattern 1: {{PLACEHOLDER:description:width:height:theme}}
PLACEHOLDER_PATTERN_KEYWORD = re.compile(
    r'\{\{PLACEHOLDER:([^:}]+)(?::(\d+))?(?::(\d+))?(?::(light|dark|warm))?\}\}'
)

# Regex pattern 2: <div class="placeholder-img">PLACEHOLDER: description</div>
PLACEHOLDER_PATTERN_DIV = re.compile(
    r'<div class="placeholder-img"[^>]*>PLACEHOLDER:\s*([^<]+)</div>',
    re.IGNORECASE
)


def parse_placeholder_keyword(match: re.Match) -> dict:
    """Parse a {{PLACEHOLDER:...}} match into parameters."""
    description = match.group(1).strip()
    width = int(match.group(2)) if match.group(2) else 860
    height = int(match.group(3)) if match.group(3) else 600
    theme = match.group(4) if match.group(4) else "light"

    return {
        "description": description,
        "width": width,
        "height": height,
        "theme": theme,
        "original": match.group(0),
        "type": "keyword"
    }


def parse_placeholder_div(match: re.Match) -> dict:
    """Parse a <div class="placeholder-img"> match into parameters."""
    description = match.group(1).strip()

    return {
        "description": description,
        "width": 860,   # Default width
        "height": 600,  # Default height
        "theme": "light",
        "original": match.group(0),
        "type": "div"
    }


def generate_filename(params: dict, index: int) -> str:
    """Generate a unique filename for the placeholder."""
    desc = params["description"]
    # Sanitize description for filename
    safe_desc = re.sub(r'[^\w\s가-힣]', '', desc)
    safe_desc = re.sub(r'\s+', '_', safe_desc)
    safe_desc = safe_desc[:30]  # Limit length

    # Create short hash for uniqueness
    hash_input = f"{params['description']}_{params['width']}_{params['height']}_{params['theme']}"
    short_hash = hashlib.md5(hash_input.encode()).hexdigest()[:6]

    return f"placeholder_{index:02d}_{safe_desc}_{short_hash}.png"


def process_project(project_dir: Path, dry_run: bool = False) -> bool:
    """Process a project directory and generate placeholder images."""

    build_dir = project_dir / "build"
    assets_dir = project_dir / "assets"
    placeholders_dir = assets_dir / "placeholders"

    # Find HTML files in build directory
    html_files = list(build_dir.glob("*.html"))
    if not html_files:
        print(f"No HTML files found in {build_dir}")
        return False

    # Use the first (or main) HTML file
    html_file = html_files[0]
    print(f"\nProcessing: {html_file.name}")

    # Read HTML content
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Find all placeholders (both formats)
    keyword_matches = list(PLACEHOLDER_PATTERN_KEYWORD.finditer(html_content))
    div_matches = list(PLACEHOLDER_PATTERN_DIV.finditer(html_content))

    all_placeholders = []

    # Parse keyword format: {{PLACEHOLDER:...}}
    for match in keyword_matches:
        all_placeholders.append(parse_placeholder_keyword(match))

    # Parse div format: <div class="placeholder-img">
    for match in div_matches:
        all_placeholders.append(parse_placeholder_div(match))

    if not all_placeholders:
        print("No placeholder keywords found.")
        return True

    print(f"Found {len(all_placeholders)} placeholder(s):")
    if keyword_matches:
        print(f"  - {{{{PLACEHOLDER:...}}}} format: {len(keyword_matches)}")
    if div_matches:
        print(f"  - <div class=\"placeholder-img\"> format: {len(div_matches)}")
    print()

    # Create placeholders directory
    if not dry_run:
        placeholders_dir.mkdir(parents=True, exist_ok=True)

    # Process each placeholder
    replacements = []
    for i, params in enumerate(all_placeholders, 1):
        filename = generate_filename(params, i)
        relative_path = f"../assets/placeholders/{filename}"

        print(f"  {i}. {params['description']}")
        print(f"     Size: {params['width']}x{params['height']}, Theme: {params['theme']}")
        print(f"     File: {filename}")

        if not dry_run:
            # Generate image
            img = generate_placeholder_image(
                description=params["description"],
                width=params["width"],
                height=params["height"],
                theme=params["theme"]
            )

            # Save image
            output_path = placeholders_dir / filename
            img.save(output_path, "PNG", optimize=True)
            print(f"     Saved to: {output_path}")

        # Create replacement based on type
        if params["type"] == "keyword":
            # Replace {{PLACEHOLDER:...}} with path directly
            replacement = relative_path
        else:
            # Replace <div class="placeholder-img">...</div> with <img> tag
            alt_text = params["description"][:50]  # Limit alt text length
            replacement = f'<div class="full-image">\n            <img src="{relative_path}" alt="{alt_text}">\n        </div>'

        replacements.append({
            "original": params["original"],
            "replacement": replacement
        })
        print()

    if dry_run:
        print("[Dry run] No files created or modified.")
        return True

    # Replace placeholders in HTML
    result = html_content
    for r in replacements:
        result = result.replace(r["original"], r["replacement"])

    # Write updated HTML
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(result)

    print(f"\n{'='*50}")
    print(f"Successfully generated {len(replacements)} placeholder image(s)!")
    print(f"Images saved to: {placeholders_dir}")
    print(f"HTML updated: {html_file}")
    print(f"{'='*50}\n")

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Generate placeholder images as asset files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python generate_placeholders_to_assets.py projects/01251245_sleep-asmr-earphone
    python generate_placeholders_to_assets.py projects/my-product --dry-run

This script will:
1. Scan HTML files in build/ directory for {{PLACEHOLDER:...}} keywords
2. Generate PNG images for each placeholder
3. Save images to assets/placeholders/ directory
4. Update HTML to use relative paths to the generated images
        """
    )
    parser.add_argument(
        "project_dir",
        help="Project directory path (e.g., projects/01251245_sleep-asmr-earphone)"
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Preview changes without creating files"
    )

    args = parser.parse_args()

    project_path = Path(args.project_dir)

    if not project_path.exists():
        print(f"Error: Project directory not found: {project_path}")
        sys.exit(1)

    success = process_project(project_path, args.dry_run)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
