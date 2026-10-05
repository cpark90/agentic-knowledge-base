---
id: https://agentic-knowledge-base.dev/id/chunk/81d7f703-027b-4647-8dce-e966f4f594c2
type: agt:Space
level: logical
title_ko: ODD의 적정 크기를 무엇으로 판정하는가
title: What judges the right size of the ODD
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T00:17:40+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — ODD가 작으면 파생물(스코프·가정·시나리오)이 참조할 속성이 부족해 지식을 만들 수 없다. 크면 커버리지 분모가 커져 같은 시나리오 집합의 커버리지가 떨어지고 대조·유지 비용이 는다. 몇 개의 조건이 적정한가, 그리고 적정성을 무엇으로 판정하는가가 변수다. 요구 `r-005`(ODD 문서 하나)에서 이 판정 규칙으로 가는 `refines`가 열려 있다.

이미 정해진 것 — 필수 절 6개와 조건 3분류, 값·판정 방법·등급은 `p3-odd-required-sections`가 정했다. 판정 등급 D는 넣지 않고 크기의 하한 필터는 있다(`p3-measurement-method-grades`). 변경은 확장·축소·정밀화 셋이고 온톨로지가 선행하며 줄이는 절차가 있다(`p3-odd-maintenance`). ODD가 커지면 커버리지가 떨어진다는 크기의 비용은 `p8-coverage-metrics`에 정의되어 있다. 명시 제외 절이 검토했으나 밖에 둔 것을 담아 크기를 키우지 않고 검토 흔적을 남긴다.

현재 상태(2026-10-05 실측) — 조건은 9개이고 등급 A 7 · B 2다. 명시 제외는 4건이다. 가정은 5개이고 가정이 참조하는 조건은 9개 중 3개(빌드 체계·저장소 구조·언어 정책)다. 스코프 4개는 조건 7개를 참조한다(포함 6 · 제외 1). 가정과 스코프 어느 쪽도 참조하지 않는 조건은 토크나이저 고정과 호스트 환경 상속 둘이다. 참조되지 않는 조건이 과대의 신호이고 가정을 못 적는 항목이 과소의 신호다. 후자는 지금 확인할 수 없다.

답이 가르는 것 — ODD를 언제 늘리고 언제 줄이는지가 갈린다. 판정 기준이 없으면 ODD는 한 방향으로만 자란다.

선택지 — A는 수치 상한 없이 참조율과 기각률 두 지표로 조정하는 안이다(`p3-odd-size-two-indicators`). B는 조건 수 상한 7±2다(`p3-odd-size-condition-cap`). C는 프로파일 입력으로 두고 코어는 정하지 않는 안이다(`p3-odd-size-profile-input`). 세 후보 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/fd0d3d18-4aab-4c4c-8f72-41702860b68c
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/63cd97c9-d7f5-4771-af07-1bc63e42ceff
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/ccf8a107-b013-40d7-87f6-8da6303bacbc
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/5b6829fd-ea97-4e9a-b2e4-8edb5ae55267
    state: open
```
