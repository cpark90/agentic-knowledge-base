---
id: https://agentic-knowledge-base.dev/id/chunk/4787cbe7-b43d-4db2-b609-c25540fe1afc
type: artifact
level: executable
title_ko: 함수 citing_ref (tools/weave.py)
title: function citing_ref in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/0a90a335-aba9-44bf-b3c0-2b57ec12feaa
---
**함수** — `citing_ref(rel, kind)` 다. 인용처 → (무리, 표기).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def citing_ref(rel: str, kind: str) -> tuple[str, str]:
    """인용처 → (무리, 표기). 결정 기록은 결정 디렉토리(slug)가 단위이고 그 밖의 결정(V&V 시나리오)은 파일 하나가 단위다.
    설계 공간은 파일 stem, 그 밖의 단위 지식은 경로다."""
    if kind == "decision":
        parts = rel.split("/")
        return "decision", (parts[3] if rel.startswith(kb_lib.DECISION_DIR + "/") and len(parts) >= 5 else rel[:-3])
    if kind == kb_lib.SPACE_TYPE:
        return "space", Path(rel).stem
    return "other", rel
```
<!-- 인용 끝 -->
