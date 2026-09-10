---
id: https://agentic-knowledge-base.dev/id/chunk-d0153
type: decision
level: concrete
title_ko: 인시던트 사후분석은 상승을 실행하는 자리
title: Incident postmortem is where ascent is executed
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 사후분석은 이 체계의 상승(6.3절)을 실행하는 자리다. 아래 여섯
단계를 밟고, **3~5 중 하나도 산출하지 않은 사후분석은 실패로 본다.**

**근거** (노트 10.12절)

```
1. 실행 기록에서 인시던트 구간의 관측 청크를 뽑는다
2. defect-rules로 요인을 추론한다
   (10.1절 하위 유형·한정자·트리거)
3. 요인이 어휘에 없으면 — 새 요인 청크 → defect 어휘 확장 후보
4. 요인이 어휘에 있으나 조합이 시나리오에 없으면
   — 새 시나리오 후보 (origin:observed)
5. 깨진 가정이 있으면 — ODD 속성 재검토 후보 (3.6절)
6. 결론을 design 청크로, 관측을 memory 청크로.
   둘의 구성체가 사후분석 문서
```

- 3·4는 10.1절 "알려지지 않은 것"의 두 원인에 그대로 대응한다 — 어휘 문제와
  커버리지 문제.
- 3~5가 비면 지식이 축적되지 않았다는 뜻이다. 사후분석 문서가 나왔다는 것은
  성공의 증거가 아니다.
