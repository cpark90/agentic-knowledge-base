---
id: https://agentic-knowledge-base.dev/id/chunk/67eb756b-e7f0-4da2-af55-90f4bc3058e9
type: artifact
level: executable
title_ko: 함수 co_cover (tools/kb_lib.py)
title: function co_cover in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/33676d8e-31ee-4546-8550-deab439480eb]
part_of: https://agentic-knowledge-base.dev/id/composite/66e7a8ca-2ebd-4dc8-8cc0-23fa46a065fb
---
**함수** — `co_cover(refines, verifies, cases, verifiers, codes)` 다. 테스트 공동 커버 → {(검증기 W, 개발 항목 A): {테스트 케이스 C}} — `verifies` W→A 의 근거다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def co_cover(refines: dict, verifies: dict, cases, verifiers, codes) -> dict:
    """테스트 공동 커버 → {(검증기 W, 개발 항목 A): {테스트 케이스 C}} — `verifies` W→A 의 근거다 (결정 p10-link-judgement-evidence).

    테스트 케이스 C 가 개발 항목 D 를 `verifies` 하고, 같은 합격 기준의 검증기 W 가 C 를 돌리며, `codes` 의 항목 A 가 D 를 `refines` 하면
    테스트 C 가 W 의 대상과 A 를 함께 덮는다. 같은 V&V 항목이 함께 덮는 개발 항목 두 개의 쌍으로 읽지 않는다.
    """
    refined_by: dict = {}
    for a in codes:
        for d in refines.get(a, ()):
            refined_by.setdefault(d, set()).add(a)
    out: dict = {}
    for c, ws in case_verifiers(refines, cases, verifiers).items():
        for d in verifies.get(c, ()):
            for a in refined_by.get(d, ()):
                for w in ws:
                    out.setdefault((w, a), set()).add(c)
    return out
```
<!-- 인용 끝 -->
