#!/usr/bin/env python3
"""
LEGACY FALLBACK: GPT Image 2 (gpt-image-2) API로 배너 이미지 일괄 생성

이 스크립트는 더 이상 danho-imageprompt-helper의 기본 생성 경로가 아니다.
기본 이미지 생성은 Codex 네이티브 이미지 생성 기능을 사용한다.
사용자가 명시적으로 API fallback을 요청하고 OPENAI_API_KEY를 제공한 경우에만
이 스크립트를 사용한다.

prompts/banners.md (또는 직접 지정한 마크다운)을 파싱해 각 항목을
gpt-image-2 API로 생성하여 assets/generated/ 에 저장한다.

의존성: curl 만 사용 (Python 표준 라이브러리 외 추가 패키지 불필요).

사용법:
    # 프로젝트 단위 일괄 생성
    python generate_banner.py projects/01241530_my-product

    # 직접 프롬프트 파일/출력 지정
    python generate_banner.py --prompts prompts/banners.md --out assets/generated/

    # 특정 항목만 생성 (id 기준)
    python generate_banner.py projects/01241530_my-product --only hero-main,section-1

    # 강제 재생성 (기본은 기존 파일 스킵)
    python generate_banner.py projects/01241530_my-product --force

환경변수:
    OPENAI_API_KEY (필수): OpenAI API 키
    OPENAI_BASE_URL (선택): 기본 https://api.openai.com
    OPENAI_IMAGE_MODEL (선택): 기본 gpt-image-2

.env 파일 자동 로드 (의존성 0, 직접 파싱):
    아래 위치를 순서대로 찾아 처음 발견한 .env 를 로드한다 (cascade).
    이미 셸에 export 된 변수가 있으면 그게 우선 (덮어쓰지 않음).
      1. --env-file <path>  (CLI)
      2. <project_dir>/.env  (project_dir 인자 지정 시)
      3. <cwd>/.env
      4. <cwd> 부터 위로 거슬러 올라가며 최초로 만나는 .env
         (저장소 루트의 .env 가 일반적으로 여기서 잡힘)
    템플릿: 저장소 루트의 .env.example 참조.

prompts/banners.md 형식 (imageprompt 스킬이 생성):

    # 이미지 프롬프트 - 배너

    ## 공통사항
    - 브랜드 컬러: <DESIGN.md에서 자동 주입>
    - 무드: <DESIGN.md mood.keywords>
    - 비율: 3:4
    - 제외: <DESIGN.md mood.negative>

    ---

    ## 1. hero-main
    **유형**: 디자인
    **용도**: 히어로 배너
    **size**: 1024x1536
    **quality**: high

    ```
    Modern luxury skincare hero design, ...
    ```

    ---

    ## 2. section-1
    ...

각 ## 항목의 첫 단어 또는 명시된 id가 출력 파일명(.png)이 된다.

DESIGN.md 연동:
    --design <path> 또는 프로젝트 루트 DESIGN.md 가 있으면
    공통사항에 colors/mood 를 자동 주입한다.
"""
import argparse
import base64
import json
import os
import re
import subprocess
import sys
from pathlib import Path

# coding 스킬의 design_md.py 재사용 (sibling 스킬에 있음)
SCRIPT_DIR = Path(__file__).resolve().parent
# skills/danho-imageprompt-helper/scripts -> two levels up is the plugin skills root.
SKILLS_ROOT = SCRIPT_DIR.parent.parent
CODING_SCRIPTS = SKILLS_ROOT / "danho-detailpage-coding" / "scripts"
if CODING_SCRIPTS.exists():
    sys.path.insert(0, str(CODING_SCRIPTS))
try:
    from design_md import DesignMD  # noqa: E402
except ImportError:
    DesignMD = None

DEFAULT_MODEL = "gpt-image-2"
DEFAULT_BASE_URL = "https://api.openai.com"
DEFAULT_SIZE = "1024x1536"
DEFAULT_QUALITY = "medium"


# ============================================================
# .env 로더 (의존성 0)
# ============================================================
# KEY=VALUE 형식만 지원. 따옴표 제거, # 주석 무시, 'export KEY=' 허용.

_ENV_LINE_RE = re.compile(r"""
    ^\s*
    (?:export\s+)?               # 'export ' 옵션
    ([A-Za-z_][A-Za-z0-9_]*)     # KEY
    \s*=\s*
    (.*?)                        # VALUE (raw)
    \s*$
""", re.VERBOSE)


def parse_dotenv(text):
    """미니멀 .env 파서. dict 반환."""
    result = {}
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        m = _ENV_LINE_RE.match(line)
        if not m:
            continue
        key = m.group(1)
        val = m.group(2)
        # 인라인 주석 처리 (따옴표 밖의 # 만)
        val = _strip_inline_comment(val)
        # 따옴표 처리
        if len(val) >= 2 and val[0] == val[-1] and val[0] in ("'", '"'):
            val = val[1:-1]
            # 큰따옴표면 간단한 이스케이프
            if raw.strip().endswith('"') or raw.strip()[:-1].rstrip().endswith('"'):
                val = val.replace("\\n", "\n").replace("\\t", "\t").replace("\\\"", "\"")
        result[key] = val
    return result


def _strip_inline_comment(val):
    in_single = False
    in_double = False
    for i, c in enumerate(val):
        if c == "'" and not in_double:
            in_single = not in_single
        elif c == '"' and not in_single:
            in_double = not in_double
        elif c == "#" and not in_single and not in_double:
            if i == 0 or val[i - 1] in (" ", "\t"):
                return val[:i].rstrip()
    return val


def find_dotenv(start_dir=None):
    """현재 디렉토리부터 위로 거슬러 올라가며 .env 찾기. Path 또는 None."""
    cur = Path(start_dir or Path.cwd()).resolve()
    while True:
        candidate = cur / ".env"
        if candidate.is_file():
            return candidate
        if cur.parent == cur:
            return None
        cur = cur.parent


def load_dotenv_cascade(explicit_path=None, project_dir=None):
    """.env 를 cascade 로 로드하고 os.environ 에 주입.

    이미 환경변수가 설정된 키는 덮어쓰지 않는다 (셸 export 가 우선).
    어떤 파일을 로드했는지 Path 반환 (없으면 None).
    """
    paths_to_try = []
    if explicit_path:
        paths_to_try.append(Path(explicit_path))
    if project_dir:
        paths_to_try.append(Path(project_dir) / ".env")
    paths_to_try.append(Path.cwd() / ".env")
    # 위로 거슬러 찾기 (cwd/.env 가 이미 위에 있으니 거기서 또 잡혀도 무해)
    ascended = find_dotenv()
    if ascended:
        paths_to_try.append(ascended)

    for p in paths_to_try:
        try:
            if p.is_file():
                kvs = parse_dotenv(p.read_text(encoding="utf-8"))
                for k, v in kvs.items():
                    os.environ.setdefault(k, v)  # 기존 값 보호
                return p
        except OSError:
            continue
    return None


# ============================================================
# prompts/banners.md 파서
# ============================================================

# ## 1. hero-main  → id="hero-main", title="1. hero-main"
# ## hero-main    → id="hero-main"
HEADER_RE = re.compile(r"^##\s+(?:\d+\.\s*)?(\S[^\n]*?)\s*$", re.MULTILINE)
META_RE = re.compile(r"^\*\*(\w+)\*\*\s*:\s*(.+?)\s*$", re.MULTILINE)
CODE_BLOCK_RE = re.compile(r"```(?:[a-zA-Z]*)?\n(.*?)\n```", re.DOTALL)


def slugify(s):
    s = s.strip().lower()
    s = re.sub(r"[^a-z0-9가-힣\-_]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "item"


def parse_banners_md(text):
    """banners.md 파싱 → [{id, meta, prompt}, ...] 와 공통사항 dict 반환."""
    # 공통사항: '## 공통사항' 섹션의 - key: value 들
    common = {}
    common_match = re.search(r"##\s*공통사항\s*\n(.*?)(?=\n##\s|\Z)", text, re.DOTALL)
    if common_match:
        for line in common_match.group(1).splitlines():
            line = line.strip()
            if line.startswith("-") and ":" in line:
                k, _, v = line.lstrip("-").strip().partition(":")
                common[k.strip()] = v.strip()

    # 각 항목 분리: '## ' 헤더로 split (공통사항 제외)
    items = []
    # 위치 기준 분할
    header_positions = [(m.start(), m.end(), m.group(1).strip()) for m in HEADER_RE.finditer(text)]
    for idx, (start, end, raw_title) in enumerate(header_positions):
        title = raw_title
        if title.startswith("공통사항"):
            continue
        # 항목의 본문: 다음 헤더까지
        body_start = end
        body_end = header_positions[idx + 1][0] if idx + 1 < len(header_positions) else len(text)
        body = text[body_start:body_end]

        # id 추출: 첫 단어 (또는 명시된 **id**)
        id_match = re.search(r"^\*\*id\*\*\s*:\s*(\S+)", body, re.MULTILINE)
        if id_match:
            item_id = id_match.group(1).strip()
        else:
            # 헤더에서 첫 토큰
            first_token = title.split()[0]
            item_id = slugify(first_token)

        # 메타 추출
        meta = {}
        for m in META_RE.finditer(body):
            meta[m.group(1).lower()] = m.group(2).strip()

        # 프롬프트 (첫 번째 코드 블록)
        prompt_match = CODE_BLOCK_RE.search(body)
        if not prompt_match:
            print(f"⚠️  '{title}' 항목에 프롬프트 코드 블록이 없습니다. 스킵.", file=sys.stderr)
            continue
        prompt_text = prompt_match.group(1).strip()

        items.append({
            "id": item_id,
            "title": title,
            "meta": meta,
            "prompt": prompt_text,
        })

    return items, common


# ============================================================
# DESIGN.md → 공통사항 자동 주입
# ============================================================

def inject_design_context(prompt, design, common):
    """프롬프트 끝에 DESIGN.md의 컬러/무드/네거티브를 추가.

    이미 프롬프트나 공통사항에 컬러/무드가 명시되어 있다면 중복을 피하기 위해
    단순히 ', ' 로 이어 붙인다 (정밀한 dedup은 사용자가 프롬프트 수동 조정).
    """
    if design is None:
        return prompt

    colors = design.tokens.get("colors") or {}
    mood = design.mood or {}

    parts = [prompt]

    # 컬러 팔레트 — 핵심 3색만
    palette = []
    for key in ("primary", "secondary", "tertiary"):
        v = colors.get(key)
        if v:
            palette.append(f"{v}")
    if palette and "color" not in prompt.lower():
        parts.append(f"brand colors {', '.join(palette)}")

    # 무드
    keywords = mood.get("keywords")
    if isinstance(keywords, list) and keywords:
        kw = ", ".join(str(k) for k in keywords)
        parts.append(kw)

    # 네거티브
    negative = mood.get("negative")
    if isinstance(negative, list) and negative:
        neg = ", ".join(str(n) for n in negative)
        parts.append(neg)

    return ", ".join(parts)


# ============================================================
# API 호출 (curl)
# ============================================================

def _parse_api_response(stdout_text):
    """공통: API 응답 JSON → bytes."""
    try:
        resp = json.loads(stdout_text)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"응답 JSON 파싱 실패: {e}\n응답: {stdout_text[:500]}")

    if "error" in resp:
        raise RuntimeError(f"API 에러: {resp['error'].get('message', resp['error'])}")

    data = resp.get("data") or []
    if not data:
        raise RuntimeError(f"data 비어있음: {stdout_text[:500]}")

    item = data[0]
    if "b64_json" in item and item["b64_json"]:
        return base64.b64decode(item["b64_json"])
    if "url" in item:
        proc2 = subprocess.run(
            ["curl", "-sS", "-L", item["url"]], capture_output=True
        )
        if proc2.returncode != 0:
            raise RuntimeError(f"이미지 다운로드 실패: {proc2.stderr.decode(errors='ignore')[:200]}")
        return proc2.stdout
    raise RuntimeError(f"이미지 데이터 없음: {item}")


def call_gpt_image(prompt, size, quality, api_key, base_url, model):
    """gpt-image-2 /v1/images/generations 호출. PNG bytes 반환."""
    body = json.dumps({
        "model": model,
        "prompt": prompt,
        "size": size,
        "quality": quality,
        "n": 1,
    })
    url = f"{base_url.rstrip('/')}/v1/images/generations"

    cmd = [
        "curl",
        "-sS",
        "-X", "POST",
        url,
        "-H", f"Authorization: Bearer {api_key}",
        "-H", "Content-Type: application/json",
        "-d", body,
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"curl 실패: {proc.stderr.strip()}")
    return _parse_api_response(proc.stdout)


def call_gpt_image_edit(prompt, size, quality, reference_paths, api_key, base_url, model):
    """gpt-image-2 /v1/images/edits 호출 (reference 이미지 첨부, multipart/form-data).

    reference_paths: 하나 이상의 PNG 파일 경로. 단일이면 그것, 다중이면 모두 image[] 로 전송.
    제품 일관성 강화용. 마스크는 사용하지 않음 (제공하지 않으면 전체 자유 변형).
    """
    if not reference_paths:
        raise ValueError("call_gpt_image_edit: reference_paths가 비어있음")

    url = f"{base_url.rstrip('/')}/v1/images/edits"
    cmd = [
        "curl",
        "-sS",
        "-X", "POST",
        url,
        "-H", f"Authorization: Bearer {api_key}",
        "-F", f"model={model}",
        "-F", f"prompt={prompt}",
        "-F", f"size={size}",
        "-F", f"quality={quality}",
        "-F", "n=1",
    ]
    # reference 이미지 첨부 (다중일 경우 image[] 반복)
    field_name = "image[]" if len(reference_paths) > 1 else "image"
    for p in reference_paths:
        cmd.extend(["-F", f"{field_name}=@{p}"])

    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"curl 실패: {proc.stderr.strip()}")
    return _parse_api_response(proc.stdout)


# ============================================================
# 메인 흐름
# ============================================================

def resolve_paths(args):
    if args.project_dir:
        project = Path(args.project_dir)
        prompts = Path(args.prompts) if args.prompts else project / "prompts" / "banners.md"
        out = Path(args.out) if args.out else project / "assets" / "generated"
        design = args.design or (str(project / "DESIGN.md") if (project / "DESIGN.md").exists() else None)
    else:
        if not args.prompts or not args.out:
            print("❌ project_dir 미지정 시 --prompts 와 --out 둘 다 필요합니다.", file=sys.stderr)
            sys.exit(1)
        prompts = Path(args.prompts)
        out = Path(args.out)
        design = args.design
    return prompts, out, design


def main():
    parser = argparse.ArgumentParser(
        description="LEGACY FALLBACK: gpt-image-2 API로 배너 이미지 일괄 생성",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("project_dir", nargs="?", help="프로젝트 디렉토리 (예: projects/01241530_foo)")
    parser.add_argument("--prompts", help="banners.md 경로 (기본: <project>/prompts/banners.md)")
    parser.add_argument("--out", help="출력 디렉토리 (기본: <project>/assets/generated)")
    parser.add_argument("--design", help="DESIGN.md 경로 (기본: <project>/DESIGN.md)")
    parser.add_argument("--only", help="생성할 id 쉼표 구분 (예: hero-main,section-1)")
    parser.add_argument("--force", action="store_true", help="기존 파일 덮어쓰기 (기본: 스킵)")
    parser.add_argument("--model", help=f"모델 (기본: $OPENAI_IMAGE_MODEL 또는 {DEFAULT_MODEL})")
    parser.add_argument("--env-file", help=".env 경로 (기본: cascade 자동 탐색)")
    parser.add_argument("--dry-run", action="store_true", help="API 호출 없이 무엇을 만들지만 출력")
    parser.add_argument(
        "--reference-image",
        help="모든 항목에 기본 reference 이미지 (PNG 경로). 항목별 **reference** 메타가 우선. "
             "지정 시 /v1/images/edits 엔드포인트 호출하여 제품 일관성 강화."
    )
    args = parser.parse_args()

    # .env 자동 로드 (셸 env 우선, 그 다음 .env)
    loaded_env = load_dotenv_cascade(
        explicit_path=args.env_file,
        project_dir=args.project_dir,
    )
    if loaded_env:
        print(f"📄 .env 로드: {loaded_env}")

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key and not args.dry_run:
        print("❌ OPENAI_API_KEY 가 필요합니다. 다음 중 하나로 설정:", file=sys.stderr)
        print("   1. export OPENAI_API_KEY=sk-...", file=sys.stderr)
        print("   2. <repo-root>/.env 또는 <project>/.env 파일에 OPENAI_API_KEY=sk-...", file=sys.stderr)
        print("   3. --env-file <path> 로 명시", file=sys.stderr)
        sys.exit(2)
    base_url = os.environ.get("OPENAI_BASE_URL", DEFAULT_BASE_URL)
    model = args.model or os.environ.get("OPENAI_IMAGE_MODEL", DEFAULT_MODEL)

    prompts_path, out_dir, design_path = resolve_paths(args)
    if not prompts_path.exists():
        print(f"❌ 프롬프트 파일 없음: {prompts_path}", file=sys.stderr)
        sys.exit(1)
    out_dir.mkdir(parents=True, exist_ok=True)

    text = prompts_path.read_text(encoding="utf-8")
    items, common = parse_banners_md(text)
    if not items:
        print("❌ 생성할 항목이 없습니다.", file=sys.stderr)
        sys.exit(1)

    # DESIGN.md 로드 (있을 때만)
    design = None
    if design_path and DesignMD is not None:
        try:
            design = DesignMD.from_file(design_path)
        except Exception as e:
            print(f"⚠️  DESIGN.md 로드 실패 ({design_path}): {e}", file=sys.stderr)

    only_ids = set(s.strip() for s in (args.only or "").split(",") if s.strip())

    manifest = {"items": []}
    success = 0
    skipped = 0
    failed = 0

    for item in items:
        if only_ids and item["id"] not in only_ids:
            continue

        size = item["meta"].get("size", DEFAULT_SIZE)
        quality = item["meta"].get("quality", common.get("품질", DEFAULT_QUALITY)) or DEFAULT_QUALITY
        # 한글 품질 표기 매핑
        quality = {"고": "high", "중": "medium", "저": "low", "높음": "high", "중간": "medium", "낮음": "low"}.get(quality, quality)

        out_path = out_dir / f"{item['id']}.png"
        if out_path.exists() and not args.force:
            print(f"⏭️  {item['id']}: 이미 존재 (스킵). --force 로 재생성.")
            skipped += 1
            manifest["items"].append({"id": item["id"], "path": str(out_path), "status": "skipped"})
            continue

        # 프롬프트 합성
        merged_prompt = inject_design_context(item["prompt"], design, common)

        # reference 해석: 항목별 **reference** 메타 > 글로벌 --reference-image
        # **reference**는 쉼표 구분 다중 가능. 각 값은 (1) 절대/상대 경로, (2) 동일 out_dir 안의 다른 항목 id, (3) "skip"
        reference_meta = item["meta"].get("reference", "").strip()
        reference_paths = []
        if reference_meta and reference_meta.lower() != "skip":
            for raw in [s.strip() for s in reference_meta.split(",") if s.strip()]:
                # 경로처럼 보이면 그대로, 아니면 out_dir 안의 <id>.png로 해석
                candidate = Path(raw)
                if not candidate.exists():
                    candidate = out_dir / f"{raw}.png"
                if candidate.exists():
                    reference_paths.append(str(candidate))
                else:
                    print(f"   ⚠️  reference 해석 실패 (없음): {raw}", file=sys.stderr)
        elif args.reference_image and reference_meta.lower() != "skip":
            ref_p = Path(args.reference_image)
            if ref_p.exists():
                reference_paths.append(str(ref_p))
            else:
                print(f"   ⚠️  --reference-image 파일 없음: {args.reference_image}", file=sys.stderr)

        # reference 이미지가 자기 자신이면 무한 루프 방지로 제거
        reference_paths = [p for p in reference_paths if Path(p).resolve() != out_path.resolve()]

        mode_label = f"edit (ref={len(reference_paths)})" if reference_paths else "gen"
        print(f"🎨 {item['id']} ({size}, {quality}, {mode_label})...")
        if args.dry_run:
            print(f"   prompt: {merged_prompt[:200]}{'...' if len(merged_prompt) > 200 else ''}")
            if reference_paths:
                print(f"   reference: {reference_paths}")
            manifest["items"].append({
                "id": item["id"], "path": str(out_path), "status": "dry-run",
                "size": size, "quality": quality, "prompt": merged_prompt,
                "reference": reference_paths,
            })
            continue

        try:
            if reference_paths:
                img_bytes = call_gpt_image_edit(
                    prompt=merged_prompt,
                    size=size,
                    quality=quality,
                    reference_paths=reference_paths,
                    api_key=api_key,
                    base_url=base_url,
                    model=model,
                )
            else:
                img_bytes = call_gpt_image(
                    prompt=merged_prompt,
                    size=size,
                    quality=quality,
                    api_key=api_key,
                    base_url=base_url,
                    model=model,
                )
            out_path.write_bytes(img_bytes)
            print(f"   ✅ {out_path} ({len(img_bytes)} bytes)")
            success += 1
            manifest["items"].append({
                "id": item["id"], "path": str(out_path), "status": "generated",
                "size": size, "quality": quality,
                "reference": reference_paths,
            })
        except Exception as e:
            print(f"   ❌ 실패: {e}", file=sys.stderr)
            failed += 1
            manifest["items"].append({"id": item["id"], "status": "failed", "error": str(e)})

    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"\n{'='*50}")
    print(f"완료: 성공 {success} / 스킵 {skipped} / 실패 {failed}")
    print(f"manifest: {manifest_path}")
    print(f"{'='*50}\n")

    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
