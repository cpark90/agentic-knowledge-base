---
id: https://agentic-knowledge-base.dev/id/chunk/bfe7f63e-7fc3-4a1b-bb7a-b40041fd189e
type: artifact
level: executable
title_ko: 함수 assumption_facts (tools/metrics.py)
title: function assumption_facts in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ed87942d-df5e-46e6-9d80-37dcb250574c
---
**함수** — `assumption_facts(g, live, plane)` 다. 기본 가정만 가진 청크 수와 가정 개체·판정식 등급 분포·관측 수를 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def assumption_facts(g, live, plane):
    """기본 가정만 가진 청크 수와 가정 개체·판정식 등급 분포·관측 수를 돌려준다."""
    # 가정 — 기본 가정만 가진 청크 (좁힘 진행률의 역수, docs/rules.md 가정 절)
    default_only = sum(1 for c in live if set(g.objects(c, AGT.assumes)) == {DEFAULT_ASSUMPTION})
    # 4단계 대리 (14.1 정정본: 무효화 이력 · 판정식 등급 · 인위 파괴 실험) — 판정식은 참조 조건 판정의 연언이라 등급은 참조 조건
    # 등급(ODD agt:verificationGrade)의 최저다 (tools/assume_check.py 와 같은 정의). 무효화 이력은 memory plane 의 관측 수다
    assumptions = sorted(g.subjects(RDF.type, AGT.Assumption), key=str)
    def asm_grade(asm):
        grades = [str(next(g.objects(c, AGT.verificationGrade), "?")) for c in g.objects(asm, AGT.refersTo)]
        return max(grades, key=lambda x: GRADES.index(x) if x in GRADES else len(GRADES)) if grades else "?"
    grade_dist = Counter(asm_grade(a_) for a_ in assumptions)
    grade_ab = sum(v for k, v in grade_dist.items() if k in "AB")
    observations = [c for c in live if plane[c] == "memory"]
    obs_recorded = sum(1 for c in observations if str(next(g.objects(c, AGT.generatedBy), "")) == kb_lib.ASSUME_CHECK_GENERATOR)
    return default_only, assumptions, grade_dist, grade_ab, observations, obs_recorded
```
<!-- 인용 끝 -->
