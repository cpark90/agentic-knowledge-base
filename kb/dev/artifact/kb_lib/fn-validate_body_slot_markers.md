---
id: https://agentic-knowledge-base.dev/id/chunk/a09e5ab7-1cd6-4c2b-b4e4-88c84095631d
type: artifact
level: executable
title_ko: 함수 validate_body_slot_markers (tools/kb_lib.py)
title: function validate_body_slot_markers in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/efdfa170-bf07-4ef8-9d31-b554c7e26f8c
---
**함수** — `validate_body_slot_markers(markers)` 다. 표지 집합의 중복·접두 겹침을 검사한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def validate_body_slot_markers(markers: tuple[str, ...]) -> None:
    """표지 집합의 중복·접두 겹침을 검사한다. 위반이면 ValueError로 죽는다(로드 시점, 폴백 없음)."""
    seen: dict[str, int] = {}
    for i, m in enumerate(markers):
        if m in seen:
            raise ValueError(f"BODY_SLOT_MARKERS 에 표지 {m!r} 가 중복 등록됐다 (자리 {seen[m]}·{i})")
        seen[m] = i
    for a in markers:
        for b in markers:
            if a != b and b.startswith(a):
                raise ValueError(
                    f"BODY_SLOT_MARKERS 의 표지 {a!r} 가 다른 표지 {b!r} 의 접두다 — "
                    f"줄 머리 매칭이 등록 순서에 기대게 된다. 표지를 다시 고른다"
                )
```
<!-- 인용 끝 -->
