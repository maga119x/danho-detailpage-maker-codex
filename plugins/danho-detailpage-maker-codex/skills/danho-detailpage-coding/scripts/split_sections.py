"""
HTML 파일을 섹션별로 분리하는 범용 스크립트

사용법:
    python split_sections.py <input.html> [output_dir]

예시:
    python split_sections.py 상세페이지.html
    python split_sections.py 상세페이지.html ./sections
"""
import os
import re
import sys
from pathlib import Path


def extract_sections(content: str) -> list[tuple[str, str]]:
    """
    HTML 콘텐츠에서 섹션들을 자동으로 추출합니다.

    섹션 인식 규칙:
    1. <!-- 주석 --> 바로 다음에 나오는 <section> 또는 <div>
    2. id 속성이 있는 section 또는 div 태그
    """
    sections = []

    # 패턴 1: 주석 + section/div 조합
    # <!-- Comment --> <section id="..." ...>...</section>
    # <!-- Comment --> <div id="..." ...>...</div>
    pattern = r'(<!--\s*(.+?)\s*-->\s*<(section|div)\s+[^>]*id=["\']([^"\']+)["\'][^>]*>.*?</\3>)'

    matches = re.finditer(pattern, content, re.DOTALL)

    for i, match in enumerate(matches):
        full_match = match.group(0)
        comment = match.group(2).strip()
        tag_type = match.group(3)
        section_id = match.group(4)

        # 파일명 생성: 순번_id
        filename = f"{str(i+1).zfill(2)}_{section_id}"
        sections.append((filename, full_match))

    return sections


def extract_css(content: str) -> str:
    """<style> 태그 내의 CSS를 추출합니다."""
    match = re.search(r'<style>(.*?)</style>', content, re.DOTALL)
    if match:
        return match.group(1).strip()
    return ""


def split_html(input_file: str, output_dir: str = "sections") -> dict:
    """
    HTML 파일을 섹션별로 분리합니다.

    Args:
        input_file: 입력 HTML 파일 경로
        output_dir: 출력 디렉토리 (기본값: sections)

    Returns:
        분리 결과 정보를 담은 딕셔너리
    """
    # 입력 파일 읽기
    input_path = Path(input_file)
    if not input_path.exists():
        raise FileNotFoundError(f"파일을 찾을 수 없습니다: {input_file}")

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 출력 디렉토리 생성
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    results = {
        "css_file": None,
        "sections": [],
        "warnings": []
    }

    # CSS 추출
    css_content = extract_css(content)
    if css_content:
        css_file = output_path / "styles.css"
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(css_content)
        results["css_file"] = str(css_file)
        print(f"Created: {css_file}")
    else:
        results["warnings"].append("CSS를 찾을 수 없습니다.")

    # body 콘텐츠 추출
    body_match = re.search(r'<body>(.*?)</body>', content, re.DOTALL)
    if not body_match:
        raise ValueError("HTML에서 <body> 태그를 찾을 수 없습니다.")

    body_content = body_match.group(1).strip()

    # detail-page div 내부 추출 (있는 경우)
    detail_match = re.search(r'<div class="detail-page">(.*?)</div>\s*$', body_content, re.DOTALL)
    if detail_match:
        inner_content = detail_match.group(1).strip()
    else:
        inner_content = body_content

    # 섹션 추출
    sections = extract_sections(inner_content)

    if not sections:
        results["warnings"].append("자동으로 인식된 섹션이 없습니다. 수동 패턴 정의가 필요할 수 있습니다.")

    # 섹션 파일 저장
    for name, section_content in sections:
        section_file = output_path / f"{name}.html"
        with open(section_file, 'w', encoding='utf-8') as f:
            f.write(section_content)
        results["sections"].append(str(section_file))
        print(f"Created: {section_file}")

    print(f"\nSection split completed!")
    print(f"   Total sections: {len(sections)}")
    print(f"   Output directory: {output_path.absolute()}")

    return results


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    input_file = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "sections"

    try:
        split_html(input_file, output_dir)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
