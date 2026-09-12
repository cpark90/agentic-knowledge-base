---
id: https://agentic-knowledge-base.dev/id/chunk/7fe9a675-72f6-47ca-8021-718a66b28b11
type: decision
level: logical
title_ko: 즉시 병합과 무제한 용인은 둘 다 기각된다
title: Both immediate merging and unbounded tolerance are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-label-representativeness-protocol}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-11T03:30:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/6053b67e-afec-4a59-b710-31b6ab85b108
---
**대안** —

- **중복을 발견 즉시 병합한다** — 기각. 편집마다 병합 판정을 하면 저작이 느려지고,
  병합은 새 IRI를 만들어 링크를 `suspect`로 만드는 큰 연산이라(4.8절) 일괄이 맞다.
  재판정을 경계에서 일괄로 하는 것과 같은 이유다.
- **중복을 무제한 용인한다** — 기각. 같은 작업 집합 안의 중복은 예산을 두 번 먹고,
  링크 없는 중복은 어긋남을 알 길이 없다. 용인에는 스코프 조건과 링크 조건이 붙는다.
- **중복을 복합체(`hasDirectPart`)로 묶는다** — 기각. 복합체는 "함께 읽힘"이고 중복은
  "함께 갱신되어야 함"이다 — 후자는 `relatedTo` 족의 일이다.
- **근사 중복을 유사도로 확정한다** — 기각. 유사도는 후보 추림에만 쓴다(9.8절, 링크
  판정 근거). 병합·묶기·유지의 판정은 사람 또는 승인된 판정자다.

**미확정** — 근사 중복 후보의 임계값(n-gram 겹침 θ)은 첫 `consistency` 보고를 보고
정한다. 중복률의 허용 상한도 마찬가지다 — 실측 전에는 정하지 않는다.
