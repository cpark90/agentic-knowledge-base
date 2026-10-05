---
id: https://agentic-knowledge-base.dev/id/chunk/09968ec4-e794-44fe-ac33-d50471cd12a1
type: decision
level: concrete
title_ko: 규범 문서 규약 — 복원 링크는 frontmatter의 restored 목록으로 표시하고 증거에 proposal을 더한다
title: Normative-document conventions — Restored links are marked by the frontmatter restored list and add proposal evidence
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T03:54:56+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/66d847e5-4837-43ea-8498-da00a8fb92f3
---
**규약** — `p10-restored-link-marking`의 결론을 규범 문서에 싣는 문장이다.

규약: 복원 후보는 `bazel build //kg:link_candidates`(본문 식별자·테스트 공동 커버·개념 공유, TIM 제약 검사, 앵커당 k ≤ 7)가 낸다. 사람이 채택하면 링크 키에 적고 같은 청크의 `restored` 목록에 대상을 한 번 더 적는다 — 그 링크의 증거는 `proposal`이고 복원 비율은 `metrics`·`audit`가 센다.
