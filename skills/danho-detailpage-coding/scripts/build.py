#!/usr/bin/env python3
"""
통합 빌드 스크립트 - 상세페이지 HTML 빌드 (DESIGN.md 기반)

기존 하드코딩된 THEMES dict는 제거되고, 프로젝트 루트의 DESIGN.md를
단일 디자인 시스템 소스로 사용한다. DESIGN.md 형식은
`references/design-md-spec.md` 와 `references/design-md-presets/` 참조.

사용법:
    # 빈 템플릿 생성 (단일 HTML 코딩용)
    python build.py [project_dir] --init

    # 섹션 병합 빌드 (수정 및 재빌드용)
    python build.py [project_dir]

    # 다른 DESIGN.md 사용 (기본: <project_dir>/DESIGN.md)
    python build.py [project_dir] --design path/to/other.design.md
    python build.py [project_dir] --title "브랜드명 | 제품명"

예시:
    python build.py projects/01241530_lenovo-earphone --init
    python build.py projects/01241530_lenovo-earphone

프로젝트 구조:
    projects/MMDDHHmm_[프로젝트명]/
    ├── DESIGN.md           # 디자인 시스템 (필수)
    ├── config.json         # 메타데이터 (선택)
    ├── build/
    │   ├── sections/
    │   │   ├── styles.css  # 추가 커스텀 CSS (선택)
    │   │   └── 01_*.html   # 섹션 HTML
    │   └── [프로젝트명]-vN.html
    └── assets/             # 이미지

config.json 예시:
    {
        "title": "LENOVO | 수면 ASMR 이어폰"
    }

DESIGN.md 가 없으면:
    - --init 시: clean-minimal 프리셋이 자동 복사됨
    - build 시: 에러
"""
import argparse
import glob
import json
import os
import re
import shutil
import sys
from pathlib import Path

# 같은 디렉토리의 design_md.py 임포트
SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))
from design_md import DesignMD  # noqa: E402

PRESETS_DIR = SCRIPT_DIR.parent / "references" / "design-md-presets"
DEFAULT_PRESET = "clean-minimal"


# ============================================================
# BASE CSS (도메인 공통 — 디자인 시스템과 무관한 레이아웃·유틸리티)
# ============================================================

BASE_CSS = """
    /* ===== RESET & BASE ===== */
    *, *::before, *::after {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    /* ===== WEB FONTS ===== */
    @font-face {
        font-family: 'Paperlogy';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/2408-3@1.0/Paperlogy-4Regular.woff2') format('woff2');
        font-weight: 400;
    }
    @font-face {
        font-family: 'Paperlogy';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/2408-3@1.0/Paperlogy-5Medium.woff2') format('woff2');
        font-weight: 500;
    }
    @font-face {
        font-family: 'Paperlogy';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/2408-3@1.0/Paperlogy-6SemiBold.woff2') format('woff2');
        font-weight: 600;
    }
    @font-face {
        font-family: 'Paperlogy';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/2408-3@1.0/Paperlogy-7Bold.woff2') format('woff2');
        font-weight: 700;
    }
    @font-face {
        font-family: 'Paperlogy';
        src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/2408-3@1.0/Paperlogy-8ExtraBold.woff2') format('woff2');
        font-weight: 800;
    }

    /* ===== LAYOUT BASE ===== */
    body {
        font-family: var(--font-body-md-family, 'Paperlogy'), -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
        font-weight: var(--font-body-md-weight, 500);
        font-size: var(--font-body-md-size, clamp(1rem, 3.7vw, 1.125rem));
        line-height: var(--font-body-md-line-height, 1.6);
        background: var(--color-bg);
        color: var(--color-text);
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
    }

    .detail-page {
        max-width: 860px;
        margin: 0 auto;
        overflow-x: hidden;
        background: var(--color-bg);
    }

    .detail-page * {
        max-width: 100%;
    }

    img {
        max-width: 100%;
        height: auto;
        display: block;
    }

    /* ===== CONTENT SECTIONS ===== */
    .content-section,
    .detail-section {
        padding: var(--space-section, clamp(56px, 14vw, 112px)) clamp(18px, 5vw, 44px);
        background: var(--color-bg);
    }

    .section-copy,
    .copy {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 12px;
        text-align: center;
        margin: 0 auto clamp(24px, 7vw, 40px);
    }

    .section-visual,
    .visual {
        width: 100%;
        margin: clamp(22px, 6vw, 36px) auto;
    }

    .section-visual img,
    .visual img {
        width: 100%;
        border-radius: var(--rounded-lg, 16px);
    }

    .lead {
        max-width: 34em;
        font-size: var(--font-body-lg-size, clamp(1.0625rem, 4vw, 1.375rem));
        line-height: 1.62;
        color: var(--color-text-secondary);
    }

    .section-var-1 { background: var(--color-bg-var-1); }
    .section-var-2 { background: var(--color-bg-var-2); }
    .section-var-3 { background: var(--color-bg-var-3); }

    .section-inverted {
        background: var(--color-bg-inverted);
        color: var(--color-text-inverted);
    }
    .section-inverted h2 { color: var(--color-text-inverted); }
    .section-inverted p { color: var(--color-text-inverted-secondary); }

    /* ===== FULL IMAGE ===== */
    .full-image {
        width: 100%;
        padding: 0;
        margin: 0;
    }
    .full-image img {
        width: 100%;
        height: auto;
        display: block;
    }

    /* ===== TYPOGRAPHY UTILITIES ===== */
    .section-title {
        font-family: var(--font-h2-family, 'Paperlogy');
        font-size: var(--font-h2-size, clamp(1.75rem, 7vw, 2.75rem));
        font-weight: var(--font-h2-weight, 800);
        line-height: var(--font-h2-line-height, 1.3);
        margin-bottom: var(--space-lg, clamp(20px, 6vw, 36px));
        text-align: center;
    }

    .section-subtitle {
        font-family: var(--font-h3-family, 'Paperlogy');
        font-size: var(--font-h3-size, clamp(1.25rem, 5vw, 1.875rem));
        font-weight: var(--font-h3-weight, 700);
        margin-bottom: var(--space-sm, 16px);
        text-align: center;
    }

    .section-desc {
        font-size: var(--font-body-lg-size, clamp(1.0625rem, 4vw, 1.375rem));
        color: var(--color-text-secondary);
        text-align: center;
        margin-bottom: var(--space-lg, clamp(22px, 6vw, 36px));
        line-height: 1.62;
    }

    .section-intro {
        font-size: var(--font-body-md-size, clamp(1rem, 3.7vw, 1.125rem));
        color: var(--color-text-secondary);
        text-align: center;
        margin-bottom: var(--space-lg, clamp(22px, 6vw, 36px));
        line-height: 1.7;
    }

    /* ===== TITLE EFFECTS ===== */
    .title-gradient {
        background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-secondary) 50%, var(--color-primary) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .title-shadow {
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1), 0 4px 8px rgba(0, 0, 0, 0.05);
    }
    .title-glow {
        text-shadow:
            0 0 5px var(--color-primary),
            0 0 15px var(--color-primary),
            0 0 30px var(--color-primary);
    }
    .title-neon-gradient {
        background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-tertiary) 30%, var(--color-primary) 60%, var(--color-secondary) 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        filter: drop-shadow(0 0 8px var(--color-primary))
                drop-shadow(0 0 16px var(--color-primary))
                drop-shadow(0 0 32px var(--color-primary));
    }

    /* ===== UTILITY CLASSES ===== */
    .gold, .accent {
        color: var(--color-primary);
        font-weight: 700;
    }
    .highlight {
        color: var(--color-text);
        font-weight: 700;
    }
    .block { display: block; }

    /* ===== CHECKLIST (도메인 공통 구조, 시각 스타일은 .checklist-item) ===== */
    .checklist {
        list-style: none;
        display: flex;
        flex-direction: column;
        gap: var(--space-sm, 20px);
    }
    .checklist li {
        display: flex;
        align-items: flex-start;
        gap: 16px;
    }
    .check-box {
        flex-shrink: 0;
        width: 28px;
        height: 28px;
        border: 2px solid var(--color-primary);
        border-radius: 6px;
        margin-top: 4px;
    }
    .check-text {
        font-size: var(--font-body-sm-size, clamp(1rem, 3.4vw, 1.0625rem));
        color: var(--color-text-secondary);
        line-height: 1.6;
    }

    /* ===== STACK CARDS (수직 스택, 본문이 2줄 이상이거나 카드 안 텍스트가 긴 경우 권장) ===== */
    .stack-cards {
        list-style: none;
        padding: 0;
        margin: 0;
        display: flex;
        flex-direction: column;
        gap: 24px;
    }
    .stack-cards > * {
        width: 100%;
        max-width: 100%;
    }
    .stack-card {
        padding: clamp(22px, 6vw, 34px) clamp(18px, 5vw, 34px);
        text-align: center;        /* 카드 내부 가운데 정렬 — 페이지 전체 정렬과 일관 */
    }
    /* 카드 내부 폰트는 본문 기본 사이즈보다 한 단계(0.5rem) 작게 — 본문과 카드의 시각 위계 */
    .stack-card .badge {
        display: inline-block;
        margin-bottom: 16px;
        font-size: var(--font-caption-size, clamp(1rem, 3.2vw, 1rem));
    }
    .stack-card .section-subtitle {
        margin-bottom: 12px;
        font-size: clamp(1.125rem, 4.4vw, 1.45rem);
    }
    .stack-card p {
        line-height: 1.7;
        margin: 0 auto;
        max-width: 60ch;           /* 본문이 너무 넓게 퍼지지 않게 가독성 보호 */
        font-size: clamp(.9375rem, 3.4vw, 1.0625rem);
    }
    /* 일반 .card 내부도 동일 위계로 0.5rem ↓ (grid-2/grid-3 안 카드 포함) */
    .card .section-subtitle {
        font-size: clamp(1.125rem, 4.4vw, 1.45rem);
    }
    .card p {
        font-size: clamp(.9375rem, 3.4vw, 1.0625rem);
        line-height: 1.7;
    }
    .card .badge {
        font-size: var(--font-caption-size, clamp(1rem, 3.2vw, 1rem));
    }
    /* 카드 상단 풀-블리드 이미지 (카드+이미지 결합 패턴) */
    .stack-card.has-image {
        padding: 0;
        overflow: hidden;
    }
    .stack-card.has-image .card-image {
        width: 100%;
        max-width: 100%;
        height: auto;
        display: block;
        margin: 0;
    }
    .stack-card.has-image .card-body {
        padding: 36px 40px;
        text-align: center;        /* card-body도 동일하게 가운데 */
    }

    /* ===== GRID SYSTEM (라벨/태그/한 줄 카드용. 본문이 2줄 넘으면 .stack-cards 사용) ===== */
    .grid-2 {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: center;
    }
    .grid-2 > * {
        flex: 1 1 calc(50% - 10px);
        max-width: calc(50% - 10px);
    }
    .grid-3 {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
        justify-content: center;
    }
    .grid-3 > * {
        flex: 1 1 calc(33.333% - 14px);
        max-width: calc(33.333% - 14px);
    }
    .full-width-grid {
        width: 100%;
        padding: 40px 5%;
    }
    .grid-inner {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
    }

    /* ===== STATS (도메인 공통 구조) ===== */
    .stats-grid {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 20px;
    }
    .stat-item {
        flex: 1 1 140px;
        max-width: 180px;
        min-width: 140px;
        padding: 32px 16px;
        text-align: center;
    }
    .stat-label {
        font-size: var(--font-body-sm-size, clamp(1rem, 3.4vw, 1.0625rem));
        color: var(--color-text-muted);
    }

    /* ===== CTA SECTION ===== */
    .cta-section {
        background: linear-gradient(180deg, var(--color-bg) 0%, var(--color-bg-var-2) 100%);
        padding: clamp(64px, 16vw, 112px) clamp(18px, 5vw, 44px);
        text-align: center;
    }
    .cta-section > * {
        margin-left: auto;
        margin-right: auto;
    }

    /* ===== STATIC CTA CUE (상세페이지는 버튼 UI를 만들지 않음) ===== */
    .cta-cue {
        display: block;
        text-decoration: none;
    }

    /* ===== CURRENT PRICE GUIDANCE (numeric prices must stay out of fixed detail-page UI) ===== */
    .price-display {
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 12px;
        margin: 40px auto;
        padding: 40px 32px;
    }
    .price-value {
        font-family: Paperlogy;
        font-size: clamp(2.75rem, 12vw, 4.75rem);
        font-weight: 800;
        line-height: 1.1;
        color: var(--color-text);
        letter-spacing: 0;
        white-space: nowrap;
    }
    .price-unit {
        font-size: 0.45em;
        font-weight: 700;
        margin-left: 0.1em;
        color: var(--color-text-secondary);
    }
    .price-meta {
        font-family: Paperlogy;
        font-size: var(--font-body-md-size, clamp(1rem, 3.7vw, 1.125rem));
        color: var(--color-text-secondary);
        text-align: center;
        white-space: nowrap;
    }

    /* ===== FOOTER ===== */
    .footer-section {
        background: var(--color-bg-var-2);
        padding: clamp(56px, 14vw, 88px) clamp(18px, 5vw, 44px);
        text-align: center;
    }
    .footer-brand {
        font-size: var(--font-h1-size, clamp(2rem, 8vw, 3.25rem));
        font-weight: 800;
        letter-spacing: 6px;
        color: var(--color-text-muted);
        margin-bottom: 20px;
    }
    .footer-tagline {
        font-size: var(--font-body-md-size, clamp(1rem, 3.7vw, 1.125rem));
        color: var(--color-text-dim);
    }

    @media (max-width: 540px) {
        .grid-2 > *,
        .grid-3 > * {
            flex-basis: 100%;
            max-width: 100%;
        }
        .price-meta {
            white-space: normal;
        }
        .footer-brand {
            letter-spacing: 3px;
        }
    }
"""


# ============================================================
# I/O 헬퍼
# ============================================================

def get_next_version(output_dir: Path, base_filename: str) -> int:
    existing = list(output_dir.glob(f"{base_filename}-v*.html"))
    versions = []
    for f in existing:
        m = re.search(r"-v(\d+)\.html$", f.name)
        if m:
            versions.append(int(m.group(1)))
    return max(versions) + 1 if versions else 1


def load_config(project_dir: Path) -> dict:
    """프로젝트 메타데이터 (title 등) 로드. 위치: <project>/config.json (신규) 또는 <project>/build/config.json (구버전)."""
    for candidate in (project_dir / "config.json", project_dir / "build" / "config.json"):
        if candidate.exists():
            return json.loads(candidate.read_text(encoding="utf-8"))
    return {}


def load_design(project_dir: Path, design_arg: str = None) -> DesignMD:
    """DESIGN.md 로드. --design 인자 우선, 다음 <project>/DESIGN.md."""
    if design_arg:
        path = Path(design_arg)
    else:
        path = project_dir / "DESIGN.md"
    if not path.exists():
        raise FileNotFoundError(
            f"DESIGN.md 파일을 찾을 수 없습니다: {path}\n"
            f"  → 프리셋을 복사하세요: cp {PRESETS_DIR}/{DEFAULT_PRESET}.design.md {project_dir}/DESIGN.md"
        )
    d = DesignMD.from_file(path)
    errors = d.validate()
    if errors:
        msg = "\n".join(f"   - {e}" for e in errors)
        raise ValueError(f"DESIGN.md 검증 실패 ({path}):\n{msg}")
    return d


def load_sections(sections_dir: Path) -> list:
    section_files = sorted(glob.glob(str(sections_dir / "*.html")))
    sections = []
    for sf in section_files:
        content = Path(sf).read_text(encoding="utf-8").strip()
        sections.append({"file": os.path.basename(sf), "content": content})
        print(f"  ✅ Loaded: {os.path.basename(sf)}")
    return sections


def load_custom_styles(sections_dir: Path) -> str:
    styles_file = sections_dir / "styles.css"
    if styles_file.exists():
        print("  ✅ Loaded: styles.css")
        return styles_file.read_text(encoding="utf-8").strip()
    return ""


# ============================================================
# HTML 생성
# ============================================================

def build_html(title: str, design_css: str, sections_html: str, custom_css: str = "") -> str:
    return f'''<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
{design_css}
{BASE_CSS}
{custom_css}
    </style>
</head>
<body>
    <div class="detail-page">
{sections_html}
    </div>
</body>
</html>'''


def ensure_design_exists(project_path: Path):
    """DESIGN.md 없으면 기본 프리셋 자동 복사."""
    target = project_path / "DESIGN.md"
    if target.exists():
        return
    preset = PRESETS_DIR / f"{DEFAULT_PRESET}.design.md"
    if not preset.exists():
        print(f"⚠️ 기본 프리셋을 찾을 수 없습니다: {preset}")
        return
    shutil.copy(preset, target)
    print(f"  ℹ️  DESIGN.md 자동 생성됨 (프리셋: {DEFAULT_PRESET})")
    print(f"     → {target}")


def init_template(project_dir: str, design_arg: str = None, title: str = None):
    project_path = Path(project_dir)
    if not project_path.exists():
        print(f"❌ 프로젝트 디렉토리를 찾을 수 없습니다: {project_dir}")
        sys.exit(1)

    build_dir = project_path / "build"
    sections_dir = build_dir / "sections"
    build_dir.mkdir(exist_ok=True)
    sections_dir.mkdir(exist_ok=True)

    # DESIGN.md 없으면 기본 프리셋 복사
    if not design_arg:
        ensure_design_exists(project_path)

    config = load_config(project_path)
    design = load_design(project_path, design_arg)

    final_title = title or config.get("title", project_path.name)

    custom_css = load_custom_styles(sections_dir)
    config_css = config.get("custom_css", "")
    if config_css:
        custom_css = (custom_css + "\n" + config_css).strip()

    design_css = design.to_css()

    html = build_html(
        title=final_title,
        design_css=design_css,
        sections_html="        <!-- CONTENT_START -->\n\n        <!-- CONTENT_END -->",
        custom_css=custom_css,
    )

    version = get_next_version(build_dir, project_path.name)
    output_file = build_dir / f"{project_path.name}-v{version}.html"
    output_file.write_text(html, encoding="utf-8")

    print(f"\n{'='*50}")
    print("✅ Template created!")
    print(f"   Output: {output_file}")
    print(f"   Design: {design.name} — {design.description}")
    print(f"   Title:  {final_title}")
    print(f"{'='*50}\n")
    return str(output_file)


def build(project_dir: str, design_arg: str = None, title: str = None):
    project_path = Path(project_dir)
    if not project_path.exists():
        print(f"❌ 프로젝트 디렉토리를 찾을 수 없습니다: {project_dir}")
        sys.exit(1)

    build_dir = project_path / "build"
    sections_dir = build_dir / "sections"
    if not sections_dir.exists():
        print(f"❌ 섹션 디렉토리를 찾을 수 없습니다: {sections_dir}")
        sys.exit(1)

    config = load_config(project_path)
    design = load_design(project_path, design_arg)

    final_title = title or config.get("title", project_path.name)

    custom_css = load_custom_styles(sections_dir)
    config_css = config.get("custom_css", "")
    if config_css:
        custom_css = (custom_css + "\n" + config_css).strip()

    print(f"\n{'='*50}")
    print(f"Building: {project_path.name}")
    print(f"Design:   {design.name}")
    print(f"Title:    {final_title}")
    print(f"{'='*50}\n")

    print("Loading sections...")
    sections = load_sections(sections_dir)
    if not sections:
        print("❌ 섹션 파일을 찾을 수 없습니다!")
        sys.exit(1)

    sections_html = "\n\n".join(f"        {s['content']}" for s in sections)
    design_css = design.to_css()
    html_output = build_html(final_title, design_css, sections_html, custom_css)

    version = get_next_version(build_dir, project_path.name)
    output_file = build_dir / f"{project_path.name}-v{version}.html"
    output_file.write_text(html_output, encoding="utf-8")

    print(f"\n{'='*50}")
    print("✅ Build complete!")
    print(f"   Output:   {output_file}")
    print(f"   Version:  v{version}")
    print(f"   Sections: {len(sections)}")
    print(f"{'='*50}\n")
    return str(output_file)


def main():
    parser = argparse.ArgumentParser(
        description="상세페이지 HTML 빌드 (DESIGN.md 기반)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
예시:
    # 빈 템플릿 생성 (DESIGN.md 없으면 clean-minimal 자동 생성)
    python build.py projects/01241530_lenovo-earphone --init

    # 섹션 병합 빌드
    python build.py projects/01241530_lenovo-earphone

    # 다른 DESIGN.md 사용
    python build.py projects/foo --design path/to/other.design.md

사용 가능한 프리셋:
    - clean-minimal (기본값)
    - dark-luxury
    - warm-natural
    - soft-modern
    - fresh-vibrant
    - heritage

  프리셋 위치: <danho-detailpage-coding-skill-dir>/references/design-md-presets/
        """,
    )
    parser.add_argument("project_dir", help="프로젝트 디렉토리 (예: projects/01241530_my-product)")
    parser.add_argument("--init", action="store_true", help="빈 템플릿 HTML 생성 (단일 HTML 코딩용)")
    parser.add_argument("--design", help="DESIGN.md 경로 (기본: <project>/DESIGN.md)")
    parser.add_argument("--title", help="페이지 제목 (기본: config.json 또는 프로젝트명)")
    args = parser.parse_args()

    try:
        if args.init:
            init_template(args.project_dir, args.design, args.title)
        else:
            build(args.project_dir, args.design, args.title)
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
