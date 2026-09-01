---
iri: https://agentic-knowledge-base.dev/id/chunk-d0003
plane: decision
level: concrete
label_ko: plane은 판정 방식으로 정의된다
label_en: Planes are defined by verification mechanism
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 종류가 다른 지식을 하나의 컨텍스트에 섞지 않는다. plane의 분류
기준은 저장 위치나 파일 형식이 아니라 **"맞다"고 판정되는 메커니즘**이다.

**근거** (노트 5.1절) — 판정 방식이 다르면 판정 도구·갱신 주기·책임 주체가
전부 다르다. 판정 방식으로 정의하므로 plane은 도메인 중립이고, 도메인
프로파일이 각 plane의 실체와 판정 도구를 정한다.

| plane | 판정 방식 | 변경률 |
|---|---|---|
| annotation | 사회적 합의 (해소/승인) | 매우 높음 |
| decision | 논증의 타당성 (논박 가능) | 낮음 |
| schema | 스키마·호환성 검사 | 낮음 |
| contract | 형식 검사 (결정론적) | 중간 |
| artifact | 실행·실측 | 빠름 |
| memory | 없음 (휘발성) | 매우 빠름 |

**plane 추가의 유일한 근거** (5.5절) — 판정 방식이 기존 어디와도 다를 때.
같으면 하위 클래스로 둔다. decision의 판정이 가장 약하므로(논증 타당성은
기계가 판정 못 함) decision 청크는 유저 승인이 valid 전이의 조건이다.
