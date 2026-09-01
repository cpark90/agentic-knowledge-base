---
iri: https://agentic-knowledge-base.dev/id/chunk-d0056
plane: decision
level: concrete
label_ko: 도메인 중립 골격과 도메인 프로파일로 나눈다
label_en: Split the system into a domain-neutral skeleton and domain profiles
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 체계를 작업 종류와 무관한 **도메인 중립 골격**과, 그것을 특정 작업
종류에 맞게 채우는 **도메인 프로파일**로 나눈다.

**근거** (노트 2.11절)
- 골격이 정하는 것은 작업 종류가 바뀌어도 같다: plane 여섯 개와 각각의 판정
  방식, 추상화 수준 다섯 단계, 경계 조건 3갈래와 둘째 수준, 결함 요인 3갈래,
  링크 타입, 청크 상한 42줄, 앵커 해석 방식.
- 프로파일이 채우는 것은 작업 종류마다 다르다: 각 plane의 청크가 구체적으로
  무엇이고 판정 도구가 무엇인가, 각 단계의 assertion 형식, 셋째 수준 이하의
  조건 개념, 도메인 고유의 결함 하위 유형, 링크 양 끝에 올 수 있는 프로파일
  청크 클래스, plane별 42줄 오버라이드와 "줄"의 단위, 실제 앵커 해석기
  (심볼·문단·절차 단계).
- 이 노트의 예시는 대부분 개발 프로파일이며, 개발 프로파일의 결정을 모아 둔
  부록 D가 다른 프로파일을 만들 때의 템플릿이 된다.
