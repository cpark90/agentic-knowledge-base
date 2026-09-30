---
id: https://agentic-knowledge-base.dev/id/chunk/f02955db-e9e3-4d4e-956f-148581ed6984
type: artifact
level: executable
title_ko: 함수 analyse_cohesion (tools/consistency.py)
title: function analyse_cohesion in tools/consistency.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-consistency}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/980ff6a4-1f10-4e39-bd06-73c6c65e5d37
---
**함수** — `analyse_cohesion(items, by_id, sh, theta_c)` 다. ④ 묶임과 응집 — coUpdatesWith 로 묶인 쌍(살아 있는 입력 안의 것만)의 현재 본문 Jaccard 가 θ_cohesion 미만이면 응집 저하 후보.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def analyse_cohesion(items, by_id, sh, theta_c):
    """④ 묶임과 응집 — coUpdatesWith 로 묶인 쌍(살아 있는 입력 안의 것만)의 현재 본문 Jaccard 가 θ_cohesion 미만이면
    응집 저하 후보. 이전 값과 비교하지 않는다 — 뷰는 저장하지 않으므로 캐시가 없다 (4.6절). 절대 임계
    """
    bound = sorted({tuple(sorted((x["id"], c))) for x in items for c in x["co"] if c in by_id and c != x["id"]})
    cohesion = [(jaccard(sh[xi], sh[yi]), by_id[xi], by_id[yi]) for xi, yi in bound]
    cohesion_low = sorted((t for t in cohesion if t[0] < theta_c), key=lambda t: t[0])
    return bound, cohesion_low
```
<!-- 인용 끝 -->
