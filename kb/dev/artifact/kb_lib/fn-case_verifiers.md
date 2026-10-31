---
id: https://agentic-knowledge-base.dev/id/chunk/33676d8e-31ee-4546-8550-deab439480eb
type: artifact
level: executable
title_ko: 함수 case_verifiers (tools/kb_lib.py)
title: function case_verifiers in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/66e7a8ca-2ebd-4dc8-8cc0-23fa46a065fb
---
**함수** — `case_verifiers(refines, cases, verifiers)` 다. 테스트 케이스 → 그 테스트 케이스를 돌린 검증기들.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def case_verifiers(refines: dict, cases, verifiers) -> dict:
    """테스트 케이스 → 그 테스트 케이스를 돌린 검증기들. 둘이 같은 합격 기준을 `refines` 하면 그 검증기가 테스트 케이스를 돌린 것이다.

    지금의 V&V 구조에서 테스트 케이스와 검증기는 둘 다 합격 기준을 정제한다 — 테스트 케이스가 검증기를 직접 가리키지 않는다. 실행 증거의 사슬
    (run_evidence)과 테스트 공동 커버(`co_cover`)가 이 한 정의를 쓴다. `refines` 는 IRI → 정제 대상 IRI 목록이다.
    """
    by_criteria: dict = {}
    for w in verifiers:
        for k in refines.get(w, ()):
            by_criteria.setdefault(k, set()).add(w)
    return {c: set().union(*(by_criteria.get(k, set()) for k in refines.get(c, ()))) for c in cases}
```
<!-- 인용 끝 -->
