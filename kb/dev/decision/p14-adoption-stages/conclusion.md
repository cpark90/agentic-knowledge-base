---
id: https://agentic-knowledge-base.dev/id/chunk/7ffcce18-39d0-45b3-90f7-6ac8d1528254
type: decision
level: concrete
title_ko: 도입은 여덟 단계이고 단계마다 통과 조건이 있으며 사례 프로젝트 하나에서 끝까지 한 뒤 다음으로 간다
title: Adoption has eight stages with pass conditions, each completed end-to-end on one case project before the next
status: deprecated
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/opus-5, at: 2026-09-10T20:00:00+09:00}
composite: {id: https://agentic-knowledge-base.dev/id/composite/4e1e176d-aa8d-4ab5-aade-db3aca0f68fc, title_ko: 도입 8단계와 통과 조건, title: Eight adoption stages and their pass conditions}
part_of: https://agentic-knowledge-base.dev/id/composite/4e1e176d-aa8d-4ab5-aade-db3aca0f68fc
---
**결론** — 도입 단계와 통과 조건 (노트 14.1절). 각 단계는 사례 프로젝트(부록 B) 하나에서 끝까지 수행한 뒤 다음으로 간다. **여러 프로젝트에 동시 도입하지 않는다.**

1. 청크와 plane — 통과: 같은 작업의 토큰이 줄어듦이 측정됨, 고아율 < 10% / 실패: 체계 중단
2. ODD·카탈로그·스코프·작업 집합 — 첫 모니터링 이탈 0, 역할별 작업 집합 200줄 안 / ODD 재작성
3. 읽기·쓰기 기록, `sources` 자동, 링크 구축 — 링크 밀도 하한, 복원 비율 < 20% / 인수인계 수정
4. 가정·판정식·무효화 전파 — 가정 하나를 인위로 깨뜨려 무효 범위가 전수조사 없이 계산됨 / **설계 재검토**
5. abstract·logical, `-space`, 체크박스, 게이트 4종 — `refines` 연쇄의 functional 도달률 상승 / 원인 분석
6. 실행 기록, 일반화 트리거, 용어 제안 — 온톨로지 확장 ≥ 1건, 사후분석마다 산출 / 트리거 재설계
7. V&V 프로파일·`vv/`·검증 대응물·독립 스코프 — 기준 바인딩률 100%, 독립성 0건, 검증 대응물 지연 측정 / 검증 대응물를 경고로
8. 복원·감사·매트릭스 화면 — 감사 보고서가 체계 밖 정보 없이 생성 / 어휘 확장

이 저장소(2026-09-10): 1단계 **미통과** — 토큰 감소가 측정된 적 없다 (유저 결정 Q7: 먼저 잰다).
