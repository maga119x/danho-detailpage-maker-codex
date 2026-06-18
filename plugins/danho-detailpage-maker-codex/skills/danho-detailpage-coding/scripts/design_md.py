#!/usr/bin/env python3
"""
DESIGN.md 파서 + CSS 생성기

DESIGN.md (Google Stitch alpha 스펙 확장)를 파싱해 CSS variables와
컴포넌트 클래스를 생성한다. Python 표준 라이브러리만 사용 (PyYAML 불필요).

사용법 (모듈):
    from design_md import DesignMD
    d = DesignMD.from_file("projects/foo/DESIGN.md")
    css = d.to_css()           # CSS variables + 컴포넌트 클래스
    name = d.name              # 디자인 시스템 이름
    desc = d.description       # 한 줄 설명
    colors = d.tokens["colors"]  # 컬러 토큰 dict

사용법 (CLI):
    python design_md.py path/to/DESIGN.md            # CSS 출력
    python design_md.py path/to/DESIGN.md --validate # 검증만
"""
import argparse
import re
import sys
from pathlib import Path

# ============================================================
# Minimal YAML parser (DESIGN.md frontmatter용 한정 지원)
# ============================================================
# 지원: 들여쓰기 기반 dict, scalar (string/number/bool/null),
#       list (- item 형태), 따옴표 문자열, 멀티라인 plain scalar 미지원.
# 미지원: 앵커/별칭, 복합 키, 흐름 스타일 ({a: b}, [a, b]).

def parse_yaml(text):
    """간이 YAML 파서. dict/list/scalar만 지원."""
    lines = []
    for raw in text.splitlines():
        # 빈 줄 또는 주석 줄 스킵
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        # 라인 내 inline comment 제거 (단, 따옴표 안은 보호)
        line = _strip_inline_comment(raw)
        lines.append(line)
    result, _ = _parse_block(lines, 0, 0)
    return result


def _strip_inline_comment(line):
    in_single = False
    in_double = False
    for i, c in enumerate(line):
        if c == "'" and not in_double:
            in_single = not in_single
        elif c == '"' and not in_single:
            in_double = not in_double
        elif c == "#" and not in_single and not in_double:
            # # 앞에 공백이 있어야 inline comment로 간주
            if i == 0 or line[i - 1] in (" ", "\t"):
                return line[:i].rstrip()
    return line.rstrip()


def _indent_of(line):
    return len(line) - len(line.lstrip(" "))


def _parse_scalar(s):
    s = s.strip()
    if not s:
        return None
    # 따옴표 문자열
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        return s[1:-1]
    # null
    if s in ("null", "~", "Null", "NULL"):
        return None
    # bool
    if s in ("true", "True", "TRUE"):
        return True
    if s in ("false", "False", "FALSE"):
        return False
    # number
    try:
        if "." in s or "e" in s or "E" in s:
            return float(s)
        return int(s)
    except ValueError:
        pass
    return s


def _parse_block(lines, start, indent):
    """블록 파싱. dict 또는 list 반환. 끝난 라인 인덱스도 함께."""
    i = start
    # 첫 비 빈 줄로 구조 판별
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i >= len(lines):
        return None, i
    first = lines[i]
    if _indent_of(first) < indent:
        return None, i

    # list 항목 시작?
    stripped = first.lstrip()
    if stripped.startswith("- "):
        return _parse_list(lines, i, indent)
    return _parse_dict(lines, i, indent)


def _parse_dict(lines, start, indent):
    result = {}
    i = start
    while i < len(lines):
        line = lines[i]
        cur_indent = _indent_of(line)
        if cur_indent < indent:
            break
        if cur_indent > indent:
            # 이전 키의 자식이 깊은 경우인데 흐름이 어그러진 경우, 종료
            i += 1
            continue

        stripped = line.strip()
        if ":" not in stripped:
            # 잘못된 라인 — 스킵
            i += 1
            continue

        # 키:값 분리 (값에 콜론 있을 수 있으므로 첫 콜론만)
        key_part, _, value_part = stripped.partition(":")
        key = key_part.strip()
        value_part = value_part.strip()

        if value_part:
            # 인라인 스칼라
            result[key] = _parse_scalar(value_part)
            i += 1
        else:
            # 자식 블록
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j >= len(lines) or _indent_of(lines[j]) <= cur_indent:
                # 자식 없음 → None
                result[key] = None
                i = j
            else:
                child, ni = _parse_block(lines, j, _indent_of(lines[j]))
                result[key] = child
                i = ni
    return result, i


def _parse_list(lines, start, indent):
    result = []
    i = start
    while i < len(lines):
        line = lines[i]
        cur_indent = _indent_of(line)
        if cur_indent < indent:
            break
        if cur_indent > indent:
            i += 1
            continue
        stripped = line.lstrip()
        if not stripped.startswith("- "):
            break
        item_value = stripped[2:].strip()
        if item_value:
            # 인라인 스칼라
            result.append(_parse_scalar(item_value))
            i += 1
        else:
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j >= len(lines) or _indent_of(lines[j]) <= cur_indent:
                result.append(None)
                i = j
            else:
                child, ni = _parse_block(lines, j, _indent_of(lines[j]))
                result.append(child)
                i = ni
    return result, i


# ============================================================
# Frontmatter 추출
# ============================================================

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def extract_frontmatter(text):
    """DESIGN.md의 YAML frontmatter와 본문 분리."""
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValueError("DESIGN.md에 YAML frontmatter (--- ... ---) 가 없습니다.")
    yaml_text = m.group(1)
    body = text[m.end():]
    return yaml_text, body


# ============================================================
# 토큰 참조 해석
# ============================================================

TOKEN_REF_RE = re.compile(r"\{([a-zA-Z0-9_\-\.]+)\}")


def resolve_token(value, tokens, path="<root>", seen=None):
    """문자열 값 안의 {a.b.c} 참조를 실제 값으로 치환.

    Args:
        value: 치환 대상 (str 외 타입이면 그대로 반환)
        tokens: 전체 토큰 dict (frontmatter)
        path: 에러 메시지용 경로
        seen: 순환 참조 감지용 set
    """
    if not isinstance(value, str):
        return value
    seen = seen or set()

    def replace(m):
        ref = m.group(1)
        if ref in seen:
            raise ValueError(f"토큰 순환 참조: {ref} (at {path})")
        seen2 = seen | {ref}
        resolved = _lookup(ref, tokens)
        if resolved is None:
            raise ValueError(f"정의되지 않은 토큰 참조: {{{ref}}} (at {path})")
        # 재귀 치환
        return str(resolve_token(resolved, tokens, path=f"{path} -> {ref}", seen=seen2))

    return TOKEN_REF_RE.sub(replace, value)


def _lookup(dotted, tokens):
    """'colors.primary' 형태 경로로 토큰값 조회."""
    parts = dotted.split(".")
    cur = tokens
    for p in parts:
        if not isinstance(cur, dict) or p not in cur:
            return None
        cur = cur[p]
    return cur


# ============================================================
# CSS 생성
# ============================================================

# typography 토큰의 어떤 속성을 어떤 CSS variable로 매핑할지
TYPOGRAPHY_PROPS = {
    "fontFamily": "family",
    "fontSize": "size",
    "fontWeight": "weight",
    "lineHeight": "line-height",
    "letterSpacing": "letter-spacing",
}

# components 토큰의 속성 → CSS 속성 매핑
COMPONENT_PROP_MAP = {
    "backgroundColor": "background",
    "textColor": "color",
    "rounded": "border-radius",
    "elevation": "box-shadow",
    "padding": "padding",
    "margin": "margin",
    "width": "width",
    "height": "height",
    "size": None,  # size는 width/height 둘 다로 펼침
    "border": "border",
}


def to_css(tokens):
    """전체 토큰 dict → CSS 문자열 생성."""
    lines = []

    name = tokens.get("name", "Untitled")
    lines.append(f"    /* ===== DESIGN: {name} ===== */")
    lines.append("    :root {")

    # colors
    colors = tokens.get("colors") or {}
    if colors:
        lines.append("        /* Colors */")
        for k, v in colors.items():
            resolved = resolve_token(v, tokens, path=f"colors.{k}")
            lines.append(f"        --color-{k}: {resolved};")

    # typography
    typography = tokens.get("typography") or {}
    if typography:
        lines.append("        /* Typography */")
        for tname, tdef in typography.items():
            if not isinstance(tdef, dict):
                continue
            for prop, suffix in TYPOGRAPHY_PROPS.items():
                if prop in tdef and tdef[prop] is not None:
                    v = resolve_token(tdef[prop], tokens, path=f"typography.{tname}.{prop}")
                    lines.append(f"        --font-{tname}-{suffix}: {v};")

    # rounded
    rounded = tokens.get("rounded") or {}
    if rounded:
        lines.append("        /* Rounded */")
        for k, v in rounded.items():
            resolved = resolve_token(v, tokens, path=f"rounded.{k}")
            lines.append(f"        --rounded-{k}: {resolved};")

    # spacing
    spacing = tokens.get("spacing") or {}
    if spacing:
        lines.append("        /* Spacing */")
        for k, v in spacing.items():
            resolved = resolve_token(v, tokens, path=f"spacing.{k}")
            lines.append(f"        --space-{k}: {resolved};")

    # elevation
    elevation = tokens.get("elevation") or {}
    if elevation:
        lines.append("        /* Elevation (shadows) */")
        for k, v in elevation.items():
            resolved = resolve_token(v, tokens, path=f"elevation.{k}")
            lines.append(f"        --shadow-{k}: {resolved};")

    lines.append("    }")
    lines.append("")

    # components → CSS classes
    components = tokens.get("components") or {}
    if components:
        lines.append("    /* ===== Components (from DESIGN.md) ===== */")
        for cname, cdef in components.items():
            if not isinstance(cdef, dict):
                continue
            lines.append(f"    .{cname} {{")
            for prop, val in cdef.items():
                if val is None:
                    continue
                # typography 참조: 전체 폰트 속성 펼치기
                if prop == "typography" and isinstance(val, str):
                    m = TOKEN_REF_RE.fullmatch(val.strip())
                    if m:
                        tname = m.group(1).split(".")[-1]
                        tdef = (tokens.get("typography") or {}).get(tname) or {}
                        if "fontFamily" in tdef:
                            lines.append(f"        font-family: {resolve_token(tdef['fontFamily'], tokens)};")
                        if "fontSize" in tdef:
                            lines.append(f"        font-size: {resolve_token(tdef['fontSize'], tokens)};")
                        if "fontWeight" in tdef:
                            lines.append(f"        font-weight: {resolve_token(tdef['fontWeight'], tokens)};")
                        if "lineHeight" in tdef:
                            lines.append(f"        line-height: {resolve_token(tdef['lineHeight'], tokens)};")
                        if "letterSpacing" in tdef:
                            lines.append(f"        letter-spacing: {resolve_token(tdef['letterSpacing'], tokens)};")
                        continue
                # size: width/height
                if prop == "size":
                    v = resolve_token(val, tokens, path=f"components.{cname}.size")
                    lines.append(f"        width: {v};")
                    lines.append(f"        height: {v};")
                    continue
                css_prop = COMPONENT_PROP_MAP.get(prop)
                if css_prop is None:
                    continue
                v = resolve_token(val, tokens, path=f"components.{cname}.{prop}")
                lines.append(f"        {css_prop}: {v};")
            lines.append("    }")
            lines.append("")

    return "\n".join(lines)


# ============================================================
# 검증
# ============================================================

REQUIRED_TOKENS = [
    "colors.primary",
    "colors.bg",
    "colors.text",
    "typography.body-md",
]


def validate(tokens):
    """필수 토큰 존재 여부 검증. 에러 메시지 리스트 반환."""
    errors = []
    for path in REQUIRED_TOKENS:
        if _lookup(path, tokens) is None:
            errors.append(f"필수 토큰 누락: {path}")

    # 토큰 참조 무결성 검사
    def walk(node, prefix=""):
        if isinstance(node, dict):
            for k, v in node.items():
                walk(v, f"{prefix}.{k}" if prefix else k)
        elif isinstance(node, list):
            for i, v in enumerate(node):
                walk(v, f"{prefix}[{i}]")
        elif isinstance(node, str):
            for m in TOKEN_REF_RE.finditer(node):
                ref = m.group(1)
                if _lookup(ref, tokens) is None:
                    errors.append(f"정의되지 않은 토큰 참조: {{{ref}}} (at {prefix})")

    walk(tokens)
    return errors


# ============================================================
# 메인 클래스
# ============================================================

class DesignMD:
    def __init__(self, tokens, body=""):
        self.tokens = tokens
        self.body = body

    @classmethod
    def from_text(cls, text):
        yaml_text, body = extract_frontmatter(text)
        tokens = parse_yaml(yaml_text)
        if not isinstance(tokens, dict):
            raise ValueError("frontmatter가 dict 형태가 아닙니다.")
        return cls(tokens, body)

    @classmethod
    def from_file(cls, path):
        text = Path(path).read_text(encoding="utf-8")
        return cls.from_text(text)

    @property
    def name(self):
        return self.tokens.get("name", "Untitled")

    @property
    def description(self):
        return self.tokens.get("description", "")

    @property
    def mood(self):
        return self.tokens.get("mood") or {}

    def validate(self):
        return validate(self.tokens)

    def to_css(self):
        return to_css(self.tokens)


# ============================================================
# CLI
# ============================================================

def main():
    parser = argparse.ArgumentParser(description="DESIGN.md → CSS 변환/검증")
    parser.add_argument("path", help="DESIGN.md 파일 경로")
    parser.add_argument("--validate", action="store_true", help="검증만 수행")
    args = parser.parse_args()

    try:
        d = DesignMD.from_file(args.path)
    except Exception as e:
        print(f"❌ 파싱 실패: {e}", file=sys.stderr)
        sys.exit(1)

    errors = d.validate()
    if errors:
        print(f"❌ 검증 실패 ({len(errors)}건):", file=sys.stderr)
        for e in errors:
            print(f"   - {e}", file=sys.stderr)
        sys.exit(1)

    if args.validate:
        print(f"✅ {args.path} 검증 통과 ({d.name})")
        return

    print(d.to_css())


if __name__ == "__main__":
    main()
