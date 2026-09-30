---
id: https://agentic-knowledge-base.dev/id/chunk/38526768-723a-44ce-a114-eb98395d5c68
type: artifact
level: executable
title_ko: 함수 body_of (tools/label_sample.py)
title: function body_of in tools/label_sample.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-label-sample}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/f8d4f7c1-457b-4464-a913-96c62e1fcb28
---
**함수** — `body_of(path)` 다. 청크 본문 — frontmatter 제거 + 앞뒤 공백 제거.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def body_of(path: str) -> str:
    """청크 본문 — frontmatter 제거 + 앞뒤 공백 제거. `tools/judge.py`가 이 함수를 그대로 가져다 쓴다(단일 정의처,
    2026-09-30 vnv 결함 보고 ①) — 지문 대조가 성립하려면 두 도구가 같은 문자열을 내야 한다."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    end = lines[1:].index("---") + 1
    return "\n".join(lines[end + 1:]).strip()
```
<!-- 인용 끝 -->
