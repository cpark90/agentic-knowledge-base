---
id: https://agentic-knowledge-base.dev/id/chunk/544c73da-ad3f-4d03-a0ac-8561fc696df1
type: norm
level: logical
title_ko: docs/method.md 절 — 영향 분석은 변경 전에 계산한다
title: docs/method.md section — impact analysis is computed before the change
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/ec6a4bb0-67a3-435c-bdab-850ae50240c4
heading: 영향 분석
depth: 2
---
`revalidate`의 `호출부` 열은 본문 해시가 바뀐 정의를 `uses`(`agt:usesDefinition`)로 가리키는 출발점의 수이고 **코드 호출부
파손의 상한**이다(2026-09-30). 상한의 범위는 같은 모듈과 치역 경계(`defs/kb.bzl`의 `USES_TARGETS`) 안의 모듈이다 — 경계 밖 모듈·간접 호출·상수 참조는
세지 않으므로 값이 저장소 전체의 호출부와 같지 않다. **단위는 정의 청크**다 — 호출 표현식 수가 아니다(실측 2026-10-02: `pct`는
호출부 13 = 호출 모듈 8 전부, 호출 표현식 38 중 직접 16·인자로 받는 쪽 22; 승인 문구의 "36 안팎"은 표현식 단위라 같은 자로
재지 않는다 — vnv 판정 부분 성공, 해소 자체는 20/20·오탐 0). 수치를 churn의 크기로 인용할 때 이 경계를 함께 적는다.

"X를 바꾸면 무엇이 영향받는가"를 **변경 전에** 계산한다 (d-0148).

```
1. X의 IRI에서 satisfies / refines / constrains 역방향 질의 → 직접 의존 집합
2. 직접 의존 집합의 assumes 가정 중 X에 관한 것       → 무효화 후보
3. 단방향 규칙으로 하위 plane까지 반복
4. 결과: 청크 수 · plane 분포 · suspect가 될 링크 수 · 유저 승인이 필요한 결정 수
```

새 질의를 만들지 않는다. 이미 있는 역방향 질의와 단방향 규칙의 조합이다. 구조 근사는
`bazel run //tools:impact -- <타깃>`(링크 = deps, `rdeps`)이 낸다. 이 도구는 네 수치 중 셋과
직접 의존자 수를 낸다 (2026-09-11). 셋은 항목 수·plane 분포·승인 필요 결정 수다. 네 수치로
나오므로 변경의 크기가 비교 가능해진다. 유저 승인이 필요한 수가 0이 아니면 자율 진행 범위를
벗어난다.
