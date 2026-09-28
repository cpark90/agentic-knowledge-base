---
id: https://agentic-knowledge-base.dev/id/chunk/c386ece1-e7ab-4e4b-9c0d-74f04335e7ad
type: annotation
level: concrete
title_ko: 현상 22 중 결함 건수를 가진 것은 여덟이고 일곱은 데이터가 전혀 없다
title: Eight of the 22 phenomena carry a defect count and seven have no data at all
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-vv-profile-hazards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-finite-factor-types, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/688dd654-9493-4ff5-a3bc-1fe4906776ce]
generated: {by: vnv/claude-opus-5, at: 2026-09-29T02:45:00+09:00}
---
thought (non-blocking): G3 데이터 검토에서 결함 건수를 가진 현상은 여덟이고 0건인 것이 일곱, 데이터가 전혀 없는 것이 일곱이다.

대상: https://agentic-knowledge-base.dev/id/chunk/688dd654-9493-4ff5-a3bc-1fe4906776ce

본문: 실행 기록 2건·케이스 31·관측 2건과 `//kg:audit`·`//kg:metrics`·`//kb:consistency`·`//kg:link_candidates`에서 P번호별로 세면 결함 건수를 가진 여덟은 P4·P5·P6·P11·P12·P13·P18·P22이고 0건인 일곱은 P1·P2·P3·P7·P8·P9·P10이다. P3은 관측 수단이 근사 중복 1쌍을 내되 그 쌍이 append-only 실행 기록 둘이라 병합 대상이 아니므로 결함 건수가 0이다. 데이터가 전혀 없는 일곱은 P14·P15·P16·P17·P19·P20·P21이며 그 자리가 초기엔 전문가라는 규칙의 자리이므로 노출은 전문가 판단으로 매기고 탐지가능성은 D3으로 적는다. P12는 실행 기록 둘이 건너뛴 명령을 가진 케이스 둘을 `pass`로 판정한 형태로 실재했고 P18은 지금도 실재해 `docs/roadmap.md`의 8단계 행이 복원 링크 29·비율 3.8%·후보 11을 적는데 생성물은 66·9.4%·32를 낸다.

제안: P번호별 건수·트리거·발견 수준의 표는 저장하지 않고 생성물에서 인용한다. 등급과 트리거 트리플은 developer가 `defect-rules`에 옮긴다.

해소: 해소 — 건수를 세고 데이터 없는 일곱을 없다고 적었다.
