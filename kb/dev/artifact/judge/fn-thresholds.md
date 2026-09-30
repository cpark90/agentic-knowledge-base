---
id: https://agentic-knowledge-base.dev/id/chunk/568c9c47-0d5f-4372-a395-b07605eaeedd
type: artifact
level: executable
title_ko: 함수 thresholds (tools/judge.py)
title: function thresholds in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/459184ba-3aec-453b-a423-9345d0975436
---
**함수** — `thresholds(g)` 다. 확신도 임계 셋 — 자동 적용·사람 확인 경계와 캘리브레이션 상태 (judge-threshold·judge-calibration 온톨로지).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def thresholds(g: Graph) -> dict:
    """확신도 임계 셋 — 자동 적용·사람 확인 경계와 캘리브레이션 상태 (judge-threshold·judge-calibration 온톨로지)."""
    node = AGT[kb_lib.JUDGE_THRESHOLDS]
    got = lambda p, d=None: next(g.objects(node, p), d)  # noqa: E731 — 한 줄 접근자
    if got(AGT.autoApplyThreshold) is None:
        raise JudgeError(f"{SHAPES}: 임계 셋 개체 `agt:{kb_lib.JUDGE_THRESHOLDS}` 가 없다 — 임계의 원본은 프로파일이다")
    return {"auto": float(got(AGT.autoApplyThreshold)), "human": float(got(AGT.humanReviewThreshold, 0)),
            "measured": bool(got(AGT.bandAccuracyMeasured, False)),
            "floor": int(got(AGT.calibrationSampleFloor, 0)), "model": str(got(AGT.calibratedFor, kb_lib.EMPTY_UNDECIDED))}
```
<!-- 인용 끝 -->
