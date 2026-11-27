---
id: https://agentic-knowledge-base.dev/id/chunk/5690d157-cae5-4d04-8a72-b47782cadf6b
type: artifact
level: executable
title_ko: 함수 core_path (tools/kb_lib.py)
title: function core_path in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/5bbe9743-feb1-4ec4-8678-c5b66eb40f83, https://agentic-knowledge-base.dev/id/chunk/8ed1af77-96cb-4d77-ae1e-028946b9ebb8]
part_of: https://agentic-knowledge-base.dev/id/composite/be71ea80-0460-47d3-b2be-8acda0b879fb
---
**함수** — `core_path(rel, root)` 다. 코어 파일의 경로 — 이 모듈의 뿌리(`core_root`)에 있으면 그것, 없으면 호출 저장소의 뿌리 아래다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def core_path(rel: str, root: Path | None = None) -> Path:
    """코어 파일의 경로 — 이 모듈의 뿌리(`core_root`)에 있으면 그것, 없으면 호출 저장소의 뿌리 아래다 (task 0327 손질 5).

    판정 프로파일·shape 처럼 이 모듈이 원본인 T-Box 파일의 자리다. 뒤의 자리는 소스에서 직접 돌리는 경우의 것이다.
    """
    cand = core_root() / rel
    if cand.exists():
        return cand
    return (root if root is not None else workspace_root()) / rel
```
<!-- 인용 끝 -->
