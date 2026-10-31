---
id: https://agentic-knowledge-base.dev/id/chunk/908a996f-e2c4-43ce-a43f-63ff651548af
type: artifact
level: executable
title_ko: 함수 space_link_ends (tools/kb_lib.py)
title: function space_link_ends in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d7f34b4e-71f9-47c7-8540-4f10c1a663db
---
**함수** — `space_link_ends(var_from, kind, from_plane, candidate)` 다. 설계 변수의 후보 하나 → 후보 링크의 (출발, 끝).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def space_link_ends(var_from: str, kind: str, from_plane: str, candidate: str) -> tuple:
    """설계 변수의 후보 하나 → 후보 링크의 (출발, 끝). 방향은 `SPACE_CANDIDATE_DIRECTION` 이 정하고 표 밖이면 KeyError 다."""
    if SPACE_CANDIDATE_DIRECTION[(kind, from_plane)] == "candidate":
        return candidate, var_from
    return var_from, candidate
```
<!-- 인용 끝 -->
