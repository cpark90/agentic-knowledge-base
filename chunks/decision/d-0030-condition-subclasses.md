---
id: https://agentic-knowledge-base.dev/id/chunk-d0030
type: decision
level: concrete
title_ko: 조건의 둘째 수준 하위 분류와 판정 등급 요건
title: Second-level condition subclasses and decidability grade
status: deprecated
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-01T20:43:47+09:00}
---
**결론** — 조건 3갈래(정적 요소·환경 조건·동적 요소) 아래 **둘째 수준까지를
온톨로지 `related/condition`에 고정**하고, ODD의 모든 속성이 그중 하나에
속하게 한다. 셋째 수준 이하는 프로젝트별로 둔다.

**둘째 수준 목록** (노트 0.4절)
- **정적 요소** — 언어·런타임 / 빌드·패키징 체계 / 저장소 구조 /
  아키텍처 스타일 / 코딩 규약 / 라이선스·규제 정책
- **환경 조건** — 의존성 버전 / 인프라 자원 / 외부 서비스 / 연결성 /
  자원 예산 / 시간 / 규제·컴플라이언스 상태
- **동적 요소** — 활성 에이전트 / 유저 / 동시 변경 / 미해소 스레드 /
  데이터 볼륨·트래픽 / 외부 행위자

**근거** (노트 0.4절, 3.9절)
- 둘째 수준을 고정하면 ODD 속성이 빠짐없이 분류되어 갈래별 커버리지를 셀
  수 있다. 셋째 수준까지 고정하면 프로젝트마다 맞지 않는다.
- 각 하위 분류는 **판정 등급**을 갖고, **등급 C 이상이 대부분이어야 ODD
  이탈 감지가 실효적이다.** 대부분의 분류는 A(기계 판정)지만 아키텍처
  스타일은 C, 코딩 규약은 B(린터), 외부 행위자는 C다.
- C·D가 많은 갈래는 두 선택뿐이다 — 판정 방법을 개선하거나, ODD에서 빼고
  가정으로 내린다. 판정 불가능한 조건을 ODD에 두면 이탈이 감지되지 않는다.
