---
iri: https://agentic-knowledge-base.dev/id/chunk-d0010
plane: decision
level: concrete
label_ko: 추적성 정보 모델과 링크 타입
label_en: Traceability information model and link types
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 링크가 무엇을 무엇에 어떻게 이을 수 있는지를 추적성 정보
모델(TIM)로 고정한다. TIM은 온톨로지의 일부(related/trace 모듈)이며,
TIM에 없는 링크는 게이트가 거부한다. 링크의 양 끝은 파일이 아니라
청크·구성체이고, 한 방향만 저장한다 (역방향은 질의).

**링크 타입** (노트 8.2절) — 수직은 refines 하나(사다리 전이의 기록),
수평은 satisfies(산출물→결정), constrains(schema→contract),
derives-from(→결정), verifies(시나리오→결정·계약), supersedes(결정 대체),
targets(annotation→임의), assumes(→가정), prov:wasRevisionOf(시간 정체성).
확장분: allocates, depends-on, generates, conflicts-with.

**근거** (8.1절)
- TIM은 한 번 정해지면 바꾸기 어렵다 — 타입 변경은 기존 링크 전부의
  재검토다. 그래서 타입을 소수로 고정하고 확장은 빈 범주를 채우는
  타입 추가로만 한다.
- 특수한 셋: refines만 사다리를 따라 잇고, assumes만 plane을 가로질러
  무효화를 전파하며, prov:wasRevisionOf만 시간을 가로질러 잇는다.
- 파일 단위 링크는 무효화가 파일 전체로 번지므로 기각.
