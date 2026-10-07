---
id: https://agentic-knowledge-base.dev/id/chunk/f3fcb094-a1c5-414e-ab93-287b0bec0449
type: artifact
level: executable
title_ko: 함수 cross_kb_link (tools/kb_lib.py)
title: function cross_kb_link in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d6533f17-7314-4ac1-a34c-ab4e73160294
---
**함수** — `cross_kb_link(kind, src, dst)` 다. 링크가 KB 를 가로지르는 금지 링크인가 — 끝점은 `(KB, plane, 수준)` 이다(KB 는 `kb_of` 의 값).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def cross_kb_link(kind: str, src: tuple, dst: tuple) -> bool:
    """링크가 KB 를 가로지르는 금지 링크인가 — 끝점은 `(KB, plane, 수준)` 이다(KB 는 `kb_of` 의 값).

    KB 사이 링크는 `verifies` 하나다 (p6-executable-splits-by-kb, docs/rules.md §8). 예외는 정제 계층의 functional 행
    하나다 — V&V 검증 목표(kb/vv requirement, functional) → 개발 요구 `derivesFrom` (p8-scenario-ladder-rungs 결론
    "functional 검증 목표 ↔ 요구 — derives-from 필수", TIM 칸 `("derivesFrom", "requirement", "requirement")`).
    판정의 단일 정의처다 — 소비자는 복원 후보 생성기 `tools/link.py` 의 `violation`(후보 탈락)과 게이트
    `cross-kb-link`(`tools/validate.py` 의 `check_cross_kb_link`, 저작된 링크의 거부)다.
    """
    (kb_a, plane_a, level_a), (kb_b, plane_b, _) = src, dst
    if kind == "verifies" or kb_a == kb_b:
        return False
    ladder_goal = (kind == "derivesFrom" and kb_a == KB_VV and kb_b == KB_DEV
                   and plane_a == "requirement" and plane_b == "requirement" and level_a == "functional")
    return not ladder_goal
```
<!-- 인용 끝 -->
