---
id: https://agentic-knowledge-base.dev/id/chunk/1d31fc8d-2de8-4f7d-8e58-8a0252739342
type: artifact
level: executable
title_ko: 함수 body_text (tools/chunk2kg.py)
title: function body_text in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/5e2d37fd-1039-4929-8dbf-76c76777b467
---
**함수** — `body_text(path, text)` 다. 청크 본문만 — frontmatter 와 앞뒤 빈 줄을 뗀 나머지다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def body_text(path: str | os.PathLike, text: str) -> str:
    """청크 본문만 — frontmatter 와 앞뒤 빈 줄을 뗀 나머지다. 토큰은 이 문자열에서 센다.

    본문을 떼는 **단일 판정처**다 (결정 p1-chunk-unit-is-tokens 의 게이트 교체, 2026-10-01). 게이트
    (`chunk_lint`)·방출(`parse_chunk`)·실측(`tokens`)이 모두 이 문자열을 보므로 세 자리의 크기 판정이 갈리지 않는다.
    """
    lines = text.splitlines()
    if Path(path).suffix == ".ttl":
        return "\n".join(l for l in lines
                         if l.strip() and not l.lstrip().startswith(("#", "@prefix", "@base")))
    if lines and lines[0].strip() == "---":
        try:
            lines = lines[lines[1:].index("---") + 2:]
        except ValueError:
            pass
    while lines and not lines[-1].strip():
        lines.pop()
    while lines and not lines[0].strip():
        lines.pop(0)
    return "\n".join(lines)
```
<!-- 인용 끝 -->
