---
id: https://agentic-knowledge-base.dev/id/chunk/378dc204-7474-4a47-ab11-c9fc4cb5c778
type: artifact
level: executable
title_ko: 함수 _convention_stops (tools/consistency.py)
title: function _convention_stops in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6a994e18-dde7-48bd-9ce5-98a5b38caa45
---
**함수** — `_convention_stops(pieces)` 다. `규약:` 줄의 문장 끝 위치 → {이은 글의 위치}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _convention_stops(pieces: list[tuple[int, str]]) -> set[int]:
    """`규약:` 줄의 문장 끝 위치 → {이은 글의 위치}. _joined 와 같은 셈으로 위치를 낸다.

    규약 줄은 줄마다 항목 하나이므로 줄 끝이 문장 끝이다. 표 절의 줄 `규약: a | b | c` 는 gen_norms 가 칸으로 나누는
    경계(TABLE_CELL_SEP)마다 칸이 끝나므로 그 경계도 문장 끝이다. 단위가 손 줄바꿈으로 이은 규약 줄 여럿이어도 줄마다 센다.
    """
    stops, pos = set(), 0
    for i, (_, seg) in enumerate(pieces):
        piece = seg.strip()
        pos += 1 if i else 0
        if CONVENTION_LINE.match(piece):
            stops.add(pos + len(piece))
            stops.update(pos + m.start() for m in TABLE_CELL_SEP.finditer(piece))
        pos += len(piece)
    return stops
```
<!-- 인용 끝 -->
