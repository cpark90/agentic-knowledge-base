---
id: https://agentic-knowledge-base.dev/id/chunk/42689d2d-de66-4143-bd55-21a97e71e57c
type: artifact
level: executable
title_ko: 함수 heading_index (tools/gen_skills.py)
title: function heading_index in tools/gen_skills.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-skills}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
part_of: https://agentic-knowledge-base.dev/id/composite/210e1533-9390-4961-914e-3e556e96fe3d
---
**함수** — `heading_index(doc)` 다. 문서의 제목 앵커 → 제목 텍스트 (doccheck 의 slug 규칙, 같은 slug 는 -1, -2 …).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def heading_index(doc: Path) -> dict[str, str]:
    """문서의 제목 앵커 → 제목 텍스트 (doccheck 의 slug 규칙, 같은 slug 는 -1, -2 …). 코드 펜스 안은 제목이 아니다."""
    out, seen, fence = {}, {}, False
    for line in doc.read_text(encoding="utf-8").splitlines():
        if re.match(r"^ {0,3}(`{3,}|~{3,})", line):
            fence = not fence
            continue
        if fence:
            continue
        m = HEADING.match(line)
        if not m:
            continue
        text = m.group(2).strip()
        s = slug(text)
        n = seen.get(s, 0)
        seen[s] = n + 1
        out[s if n == 0 else f"{s}-{n}"] = text
    return out
```
<!-- 인용 끝 -->
