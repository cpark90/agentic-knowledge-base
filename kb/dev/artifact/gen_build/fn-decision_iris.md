---
id: https://agentic-knowledge-base.dev/id/chunk/32315be1-6edc-4ecd-8cb0-fa9a30fc7efc
type: artifact
level: executable
title_ko: 함수 decision_iris (tools/gen_build.py)
title: function decision_iris in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6400a2c9-ed32-428b-bd76-5952553e5e04
---
**함수** — `decision_iris(items)` 다. 결정 디렉토리 이름 → 결정 복합체 IRI — 절 청크의 `items` 가 slug 로 가리키는 대상이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def decision_iris(items) -> dict:
    """결정 디렉토리 이름 → 결정 복합체 IRI — 절 청크의 `items` 가 slug 로 가리키는 대상이다."""
    return {it["dir"]: it["comp_iri"] for it in items.values() if it["kind"] == "decision" and it.get("comp_iri")}
```
<!-- 인용 끝 -->
