---
id: https://agentic-knowledge-base.dev/id/chunk/431d34c4-d7da-4861-97ba-a3802a193bac
type: norm
level: logical
title_ko: docs/method.md 절 — 운용 순환의 여덟 단계와 각 단계가 다음의 전제가 되는 이유
title: docs/method.md section — the eight steps of the operating cycle and why each is a premise of the next
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T03:43:47+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/61ca9d74-d16e-46ad-8e75-46954e9f27f0
composite: {id: https://agentic-knowledge-base.dev/id/composite/61ca9d74-d16e-46ad-8e75-46954e9f27f0, title_ko: docs/method.md의 순서와 완료 판정 절 묶음, title: docs/method.md order and completion section group, part_of: https://agentic-knowledge-base.dev/id/composite/c040ba95-dc6c-4c10-af69-8d0d4c0cf6ec, ordered: [https://agentic-knowledge-base.dev/id/chunk/431d34c4-d7da-4861-97ba-a3802a193bac, https://agentic-knowledge-base.dev/id/chunk/a40ae293-0c0f-42f5-8dbb-abbb49b49ad3, https://agentic-knowledge-base.dev/id/chunk/ed0bb1c6-2a61-46a8-b082-40ae2eafe2ed, https://agentic-knowledge-base.dev/id/chunk/28864ba1-0509-420d-bd9a-c7784ea5920e]}
heading: 순서와 완료 판정
depth: 2
form: table
columns: [#, 단계, 산출, 다음 단계의 전제가 되는 이유, 방법]
items: [p2-skeleton-and-domain-profile#1 + p3-odd-first-project-start, p3-odd-first-project-start#1, p6-refinement-ladder#1, p0-workset-anchor-neighbourhood#1, p10-link-by-construction#1, p6-assumption-invalidation#1, p4-projection-as-query#1, p6-ascent-generalization#1]
---
운용 순환이라 부르는 전체 순서는 여덟 단계다. 이 문서의 각 절은 그 단계를 수행하는 방법을 적고, [`rules.md`](../../../../docs/rules.md)는
결과가 유효한지를 가르는 규칙을 적는다. 원본은 노트 Part VI·XI과 운용 지도다. 반면 이 저장소가 어디까지 왔는가를 재는 도입 8단계는
결정 [`p14-adoption-stages`](../../decision/p14-adoption-stages/conclusion.md)에 있고, 운용 순환과는 다른 축이다. 각 단계의 통과 여부는 `bazel build //kg:metrics`가 낸다.

```
프로파일 구축 → ODD 작성 → 정제(저작) → 조회 → 연결 → 갱신 → 뷰 → 일반화
                                                                    │
                     (교훈이 다시 프로파일·ODD·결정으로) ←──────────┘
```
