---
id: https://agentic-knowledge-base.dev/id/chunk/260d24aa-5aab-4ff7-81b7-40def184e51f
type: artifact
level: executable
title_ko: 함수 token_count (tools/chunk2kg.py)
title: function token_count in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/46cd72ea-813e-4ee5-b990-fede1470c237]
part_of: https://agentic-knowledge-base.dev/id/composite/5e2d37fd-1039-4929-8dbf-76c76777b467
---
**함수** — `token_count(text, enc)` 다. 본문 하나의 토큰 수.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def token_count(text: str, enc=None) -> int:
    """본문 하나의 토큰 수. `enc` 를 주지 않으면 어휘를 새로 적재한다 — 여러 파일은 적재를 한 번만 한다."""
    return len((enc or load_tokenizer()).encode(text))
```
<!-- 인용 끝 -->
