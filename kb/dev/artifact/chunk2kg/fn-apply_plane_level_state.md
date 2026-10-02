---
id: https://agentic-knowledge-base.dev/id/chunk/abf3ca16-b991-4326-8c10-b4581d03a6d2
type: artifact
level: executable
title_ko: 함수 apply_plane_level_state (tools/chunk2kg.py)
title: function apply_plane_level_state in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/b1903be2-0bdb-4f11-9c2b-cc59cc7e9a24
---
**함수** — `apply_plane_level_state(planes, levels, states)` 다. 전역 PLANES·LEVELS·STATES 를 교체하고 PLANE_CLASS 의 키 집합과 즉시 대조한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def apply_plane_level_state(planes: list[str], levels: list[str], states: list[str]) -> None:
    """전역 PLANES·LEVELS·STATES 를 교체하고 PLANE_CLASS 의 키 집합과 즉시 대조한다.

    이 도구가 아는 plane 이름(PLANE_CLASS 의 키)과 defs/kb.bzl 의 PLANES 가 갈리면 이 자리에서 죽는다 — 두 곳이
    말없이 갈라지는 것(anti-drift)이 판정 불가지 통과보다 나쁘다. `load_plane_level_state` 는 값을 읽기만 하므로
    반영은 항상 이 함수를 거친다 — `main()`이 `--residency` 를 받았을 때, 또는 `parse_chunk` 를 직접 부르는 다른
    도구가 자기 진입점에서 부른다(defs/knowledge.bzl 의 매크로·각 도구의 --residency 인자).
    """
    global PLANES, LEVELS, STATES
    assert set(PLANE_CLASS) == set(planes), (
        f"PLANE_CLASS 의 키 {sorted(PLANE_CLASS)} 가 defs/kb.bzl 의 PLANES {sorted(planes)} 와 다르다 — "
        f"두 곳을 같은 집합으로 맞춘다(STYLEGUIDE §7 단일 정의처)"
    )
    PLANES, LEVELS, STATES = planes, levels, states
```
<!-- 인용 끝 -->
