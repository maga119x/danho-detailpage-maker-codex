#!/usr/bin/env python3
"""
Placeholder Image Generator for Korean E-commerce Product Detail Pages

Generates professional placeholder images with:
- Rounded rectangle frame
- Centered description text (Korean/English)
- Optional dimensions display
- Base64 output for direct HTML embedding

Usage:
    python generate_placeholder.py "메인 제품 이미지" --width 860 --height 600
    python generate_placeholder.py "라이프스타일 컷" --width 860 --height 480 --theme dark
    python generate_placeholder.py "상세 이미지" --output file --filename placeholder.png

Requirements:
    pip install Pillow
"""

import argparse
import base64
import io
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: Pillow library required. Install with: pip install Pillow")
    sys.exit(1)


# Theme configurations
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


def hex_to_rgb(hex_color: str) -> tuple:
    """Convert hex color to RGB tuple."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def get_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    """Get a font, with fallback to default if custom fonts unavailable."""
    # Try common Korean fonts first
    font_candidates = [
        "malgun.ttf",           # Malgun Gothic (Windows)
        "NanumGothic.ttf",      # Nanum Gothic
        "AppleGothic.ttf",      # Apple Gothic (macOS)
        "NotoSansKR-Regular.otf",  # Noto Sans Korean
        "arial.ttf",            # Arial fallback
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

    # Final fallback to default
    try:
        return ImageFont.load_default()
    except:
        return None


def draw_rounded_rect(
    draw: ImageDraw.Draw,
    xy: tuple,
    radius: int,
    fill: str = None,
    outline: str = None,
    width: int = 1
):
    """Draw a rounded rectangle."""
    x1, y1, x2, y2 = xy
    fill_rgb = hex_to_rgb(fill) if fill else None
    outline_rgb = hex_to_rgb(outline) if outline else None

    # Use PIL's built-in rounded_rectangle if available (Pillow 8.2+)
    try:
        draw.rounded_rectangle(xy, radius=radius, fill=fill_rgb, outline=outline_rgb, width=width)
    except AttributeError:
        # Fallback for older Pillow versions
        # Draw corners
        draw.ellipse([x1, y1, x1 + 2*radius, y1 + 2*radius], fill=fill_rgb, outline=outline_rgb)
        draw.ellipse([x2 - 2*radius, y1, x2, y1 + 2*radius], fill=fill_rgb, outline=outline_rgb)
        draw.ellipse([x1, y2 - 2*radius, x1 + 2*radius, y2], fill=fill_rgb, outline=outline_rgb)
        draw.ellipse([x2 - 2*radius, y2 - 2*radius, x2, y2], fill=fill_rgb, outline=outline_rgb)
        # Draw rectangles
        draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill_rgb)
        draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill_rgb)
        if outline_rgb:
            draw.line([x1 + radius, y1, x2 - radius, y1], fill=outline_rgb, width=width)
            draw.line([x1 + radius, y2, x2 - radius, y2], fill=outline_rgb, width=width)
            draw.line([x1, y1 + radius, x1, y2 - radius], fill=outline_rgb, width=width)
            draw.line([x2, y1 + radius, x2, y2 - radius], fill=outline_rgb, width=width)


def draw_camera_icon(draw: ImageDraw.Draw, center: tuple, size: int, color: str):
    """Draw a simple camera icon."""
    cx, cy = center
    color_rgb = hex_to_rgb(color)

    # Camera body (rounded rectangle)
    body_width = size
    body_height = int(size * 0.7)
    body_radius = int(size * 0.15)

    draw_rounded_rect(
        draw,
        (cx - body_width//2, cy - body_height//2, cx + body_width//2, cy + body_height//2),
        radius=body_radius,
        fill=None,
        outline=color,
        width=3
    )

    # Lens (circle)
    lens_radius = int(size * 0.2)
    draw.ellipse(
        [cx - lens_radius, cy - lens_radius, cx + lens_radius, cy + lens_radius],
        fill=None,
        outline=color_rgb,
        width=3
    )

    # Flash/viewfinder bump
    bump_width = int(size * 0.25)
    bump_height = int(size * 0.12)
    bump_y = cy - body_height//2 - bump_height
    draw.rectangle(
        [cx - bump_width//2, bump_y, cx + bump_width//2, cy - body_height//2 + 2],
        fill=color_rgb
    )


def get_text_size(draw: ImageDraw.Draw, text: str, font: ImageFont.FreeTypeFont) -> tuple:
    """Get text dimensions compatible with different Pillow versions."""
    try:
        bbox = draw.textbbox((0, 0), text, font=font)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]
    except AttributeError:
        return draw.textsize(text, font=font)


def generate_placeholder(
    description: str,
    width: int = 860,
    height: int = 600,
    theme: str = "light",
    show_dimensions: bool = True,
) -> Image.Image:
    """
    Generate a placeholder image.

    Args:
        description: Text describing what image should be placed here
        width: Image width in pixels
        height: Image height in pixels
        theme: Color theme ('light', 'dark', 'warm')
        show_dimensions: Whether to show recommended dimensions

    Returns:
        PIL Image object
    """
    colors = THEMES.get(theme, THEMES["light"])

    # Create image
    img = Image.new("RGB", (width, height), hex_to_rgb(colors["bg"]))
    draw = ImageDraw.Draw(img)

    # Calculate dimensions
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

    # Draw inner dashed border effect (simple solid line for compatibility)
    inner_padding = padding + 15
    draw_rounded_rect(
        draw,
        (inner_padding, inner_padding, width - inner_padding, height - inner_padding),
        radius=int(frame_radius * 0.8),
        fill=None,
        outline=colors["frame"],
        width=1
    )

    # Calculate center
    center_x = width // 2
    center_y = height // 2

    # Draw camera icon
    icon_size = min(width, height) * 0.15
    draw_camera_icon(draw, (center_x, center_y - 40), int(icon_size), colors["icon"])

    # Draw description text
    font_size_main = max(18, min(28, width // 25))
    font_size_sub = max(14, min(20, width // 35))

    font_main = get_font(font_size_main, bold=True)
    font_sub = get_font(font_size_sub)

    # Main description
    text_y = center_y + 30
    if font_main:
        text_width, text_height = get_text_size(draw, description, font_main)
        draw.text(
            (center_x - text_width // 2, text_y),
            description,
            font=font_main,
            fill=hex_to_rgb(colors["text"])
        )
        text_y += text_height + 12

    # Dimension recommendation
    if show_dimensions and font_sub:
        dim_text = f"권장 크기: {width}px x {height}px"
        dim_width, dim_height = get_text_size(draw, dim_text, font_sub)
        draw.text(
            (center_x - dim_width // 2, text_y),
            dim_text,
            font=font_sub,
            fill=hex_to_rgb(colors["text_secondary"])
        )

    return img


def image_to_base64(img: Image.Image, format: str = "PNG") -> str:
    """Convert PIL Image to base64 string."""
    buffer = io.BytesIO()
    img.save(buffer, format=format, optimize=True)
    buffer.seek(0)
    encoded = base64.b64encode(buffer.getvalue()).decode("utf-8")
    mime = "png" if format.upper() == "PNG" else "jpeg"
    return f"data:image/{mime};base64,{encoded}"


def main():
    parser = argparse.ArgumentParser(
        description="Generate placeholder images for product detail pages"
    )
    parser.add_argument(
        "description",
        help="Description text for the placeholder (e.g., '메인 제품 이미지')"
    )
    parser.add_argument(
        "--width", "-w",
        type=int,
        default=860,
        help="Image width in pixels (default: 860)"
    )
    parser.add_argument(
        "--height", "-H",
        type=int,
        default=600,
        help="Image height in pixels (default: 600)"
    )
    parser.add_argument(
        "--theme", "-t",
        choices=["light", "dark", "warm"],
        default="light",
        help="Color theme (default: light)"
    )
    parser.add_argument(
        "--output", "-o",
        choices=["base64", "file", "both"],
        default="base64",
        help="Output format (default: base64)"
    )
    parser.add_argument(
        "--filename", "-f",
        default="placeholder.png",
        help="Output filename when using file output (default: placeholder.png)"
    )
    parser.add_argument(
        "--no-dimensions",
        action="store_true",
        help="Hide dimension recommendation text"
    )
    parser.add_argument(
        "--html",
        action="store_true",
        help="Wrap base64 output in HTML img tag"
    )

    args = parser.parse_args()

    # Generate image
    img = generate_placeholder(
        description=args.description,
        width=args.width,
        height=args.height,
        theme=args.theme,
        show_dimensions=not args.no_dimensions
    )

    # Output
    if args.output in ["base64", "both"]:
        base64_str = image_to_base64(img)
        if args.html:
            print(f'<img src="{base64_str}" alt="{args.description}">')
        else:
            print(base64_str)

    if args.output in ["file", "both"]:
        output_path = Path(args.filename)
        img.save(output_path, "PNG", optimize=True)
        if args.output == "both":
            print(f"\nSaved to: {output_path.absolute()}", file=sys.stderr)
        else:
            print(f"Saved to: {output_path.absolute()}")


if __name__ == "__main__":
    main()
