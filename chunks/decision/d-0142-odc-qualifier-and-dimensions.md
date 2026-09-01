---
iri: https://agentic-knowledge-base.dev/id/chunk-d0142
plane: decision
level: concrete
label_ko: ODC 한정자·차원과 분포 진단
label_en: ODC qualifier, dimensions, and distribution as diagnosis
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 각 결함에 ODC **한정자**(`missing` 있어야 할 것이 없음 /
`incorrect` 있으나 틀림)를 붙이고, **트리거·영향·발견 단계** 세 차원을 결함
청크의 속성으로 둔다. **유형 분포 자체가 진단**이며 그 추론 규칙을
`defect-rules`에 둔다.

**근거** (노트 10.1절)
- 인지 요인의 "누락"과 실행 요인의 `missing`은 다르다 — 전자는 **입력**의
  부재, 후자는 **산출물**의 부재. 한정자를 따로 두어야 둘이 구분된다.
- **트리거**(무엇이 드러냈는가: 검사 게이트 / 테스트 / 리뷰 / 실행 시 /
  ODD 이탈 대조) — 검사 체계의 효과 측정. 실행 시에만 드러나는 요인이
  많으면 게이트가 약한 것이다.
- **영향**(기능 / 성능 / 추적성 / 가정 건전성 / 커버리지) — 우선순위.
- **발견 단계**(functional ~ executable) — 하강 단절 지점 측정. concrete
  에서만 발견되면 상위 게이트가 약한 것이다.
- 진단의 예 — 실행 요인의 `function`·`missing`이 많으면 설계가 불완전한
  것이고, 인지 요인의 `누락`이 많으면 스코프가 좁은 것이다.
