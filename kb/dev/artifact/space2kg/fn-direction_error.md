---
id: https://agentic-knowledge-base.dev/id/chunk/afdf06df-8670-440e-8cd5-b5447c7d760a
type: artifact
level: executable
title_ko: 함수 direction_error (tools/space2kg.py)
title: function direction_error in tools/space2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-space2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/2716ece9-44f6-48ff-b2ab-1ad0ea6fa6c0
---
**함수** — `direction_error(space, plane_of)` 다. 변수 종류(링크 타입, 출발 항목의 지식 종류)가 방향 표에 있는가 — 없으면 오류 문장, 있으면 빈 문자열 (Q-0055 Q112-b).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def direction_error(space: dict, plane_of) -> str:
    """변수 종류(링크 타입, 출발 항목의 지식 종류)가 방향 표에 있는가 — 없으면 오류 문장, 있으면 빈 문자열 (Q-0055 Q112-b)."""
    frm, kind = space["var"]
    plane = plane_of(URIRef(frm)) or kb_lib.NONE_MARK
    space["from_plane"] = plane
    if (kind, plane) in kb_lib.SPACE_CANDIDATE_DIRECTION:
        return ""
    known = " · ".join(f"({k}, {p})" for k, p in kb_lib.SPACE_CANDIDATE_DIRECTION)
    return (f"{space['path']}: 변수 종류 ({kind}, {plane}) 의 후보 링크 방향이 정해지지 않았다 — 방향 표 "
            f"kb_lib.SPACE_CANDIDATE_DIRECTION 의 종류는 {known} 다. 출발 항목의 지식 종류는 head 그래프에서 읽는다 (Q-0055 Q112-b)")
```
<!-- 인용 끝 -->
