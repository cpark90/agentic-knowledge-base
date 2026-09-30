---
id: https://agentic-knowledge-base.dev/id/chunk/d4ad9c8b-b1ad-417c-8d8e-bd440024008e
type: artifact
level: executable
title_ko: 함수 load_odd (tools/odd_check.py)
title: function load_odd in tools/odd_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
part_of: https://agentic-knowledge-base.dev/id/composite/bdc32d15-06d9-439b-a3b2-0d3dab05225f
---
**함수** — `load_odd(path)` 다. OpenODD 문서 하나를 읽는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_odd(path: Path) -> dict:
    """OpenODD 문서 하나를 읽는다. CHECKS·ATTRIBUTES 가 없으면 빈 맵으로 본다."""
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
```
<!-- 인용 끝 -->
