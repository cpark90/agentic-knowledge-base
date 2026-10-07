---
id: https://agentic-knowledge-base.dev/id/chunk/40832ce8-b21d-4635-9f79-0212625c61fe
type: artifact
level: executable
title_ko: 함수 check_rung_before_descent (tools/validate.py)
title: function check_rung_before_descent in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/8a2be483-4fc8-411f-8f35-b7719552e4e4, https://agentic-knowledge-base.dev/id/chunk/a7d95ff4-ef90-4353-a266-826a544f37d8, https://agentic-knowledge-base.dev/id/chunk/b743d72c-4fe1-4898-bd6f-aeed9063b344]
part_of: https://agentic-knowledge-base.dev/id/composite/700062aa-fcac-4d30-8481-7021a666d072
---
**함수** — `check_rung_before_descent(merged)` 다. 같은 정제 수준의 V&V 대응물 없이 다음 정제 수준으로 내려간 정제를 거부한다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_rung_before_descent(merged: Graph) -> list[str]:
    """같은 정제 수준의 V&V 대응물 없이 다음 정제 수준으로 내려간 정제를 거부한다 (게이트 `rung-before-descent`, 요구 r-023, 유저 결정 Q51-a).

    판정식은 R1 정제 계층 사슬이다 — functional→abstract 는 정제 대상 요구의 검증 목표, logical→concrete 는 결정 복합체가 닿는
    요구의 목표에 달린 합격 기준, concrete→executable 은 그 기준 가운데 검증기가 바인딩한 것을 요구한다(사람 확인 기준만
    가진 요구는 면제, Q26-a). 판정에는 두 KB 의 청크·복합체 부분·링크가 함께 필요해 병합 그래프를 보는 여기가 자리다
    (`cross-kb-link`·`code-part-link` 와 같다). 판정 함수는 지표(metrics 7단계 절·전방 추적)와 같은 `kb_lib.rung_violations`
    · `kb_lib.vv_counterparts` 다.
    """
    gate = kb_lib.RUNG_BEFORE_DESCENT_GATE
    plane = kb_lib.chunk_planes(merged)
    level = {c: str(next(merged.objects(c, kb_lib.AGT.hasLevel), "")).split("/")[-1] for c in plane}
    live = {c for c in plane if str(next(merged.objects(c, kb_lib.AGT.status), "")) != "deprecated"}
    need = {kb_lib.RUNG_DESCENTS[0]: "요구를 derivesFrom 하는 검증 목표가 없다",
            kb_lib.RUNG_DESCENTS[1]: "요구의 검증 목표에 합격 기준이 없다",
            kb_lib.RUNG_DESCENTS[2]: "요구의 합격 기준(사람 확인 기준 제외)을 바인딩한 검증기가 없다"}
    return [f"[{gate}] {_chunk_location(merged, s)}: {rung} 정제(대상 {_chunk_location(merged, o)})이 닿는 요구 "
            f"{_chunk_location(merged, r)} — {need[rung]} (r-023-rung-before-descent, p8-scenario-ladder-rungs)"
            for rung, s, o, r in kb_lib.rung_violations(merged, plane, level, live)]
```
<!-- 인용 끝 -->
