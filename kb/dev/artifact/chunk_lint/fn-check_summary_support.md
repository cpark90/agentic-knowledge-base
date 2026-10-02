---
id: https://agentic-knowledge-base.dev/id/chunk/4978379c-7c15-4dc1-9832-9ada51fe6cf0
type: artifact
level: executable
title_ko: 함수 check_summary_support (tools/chunk_lint.py)
title: function check_summary_support in tools/chunk_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/b61b3d07-041e-43c2-bb5d-cf3239db7602]
part_of: https://agentic-knowledge-base.dev/id/composite/ea7476e7-b990-4825-a271-6356855d2118
---
**함수** — `check_summary_support(text)` 다. `핵심:` 항목마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_summary_support(text: str) -> list[tuple[int, str]]:
    """`핵심:` 항목마다 지지 참조가 있는가 (게이트 id `summary-support`) → [(줄 번호, 이유)].

    슬롯은 선택이다 — `미확정:`과 같은 자리 규약(줄 머리 `핵심:`)으로 열리고, 그 뒤 이어지는 목록 항목이 대상이다.
    항목이 다른 슬롯 표지·산문으로 넘어가면 블록이 끝난다. 참조가 하나도 없는 항목만 위반이다.
    """
    fields, body, start = split_frontmatter(text)
    out: list[tuple[int, str]] = []
    in_block = False
    for i, line in enumerate(body):
        s = line.strip()
        if s == SUMMARY_KEY_MARKER or s.startswith(SUMMARY_KEY_MARKER + " "):
            in_block = True
            continue
        if not in_block:
            continue
        if not s:
            continue
        if s.startswith("- "):
            item = s[2:].strip()
            if not SUMMARY_REF_RE.search(item):
                out.append((start + i, f'`핵심:` 항목이 지지 참조가 없다 — "{item}". `[#id]`·`d-NNNN`·IRI(백틱)·'
                                       '마크다운 링크 중 하나로 본문의 지지 블록을 가리킨다 (요약은 집계다, judge-without-service-2026-09-30)'))
            continue
        in_block = False
    return out
```
<!-- 인용 끝 -->
