---
id: https://agentic-knowledge-base.dev/id/chunk/298c1a9e-71db-4862-a115-b67614e6e864
type: contract
level: logical
title_ko: 승격은 관측에서 낸 제안이 큐를 거쳐 확장 모듈에 병합되고 출처 링크를 갖는지 사람이 확인한다
title: Promotion is confirmed by a person checking that a proposal from an observation passed the queue, merged into an extension module and carries a provenance link
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-22T19:06:46+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/1ef46f34-e0ff-4996-bad4-ee3340ec290a]
---
**합격 기준** — 기준 종류는 **사람 확인**이다. 어떤 관측 `o` 에 대해 `proposal(o) ∈ kb/ontology/proposals/` 였다가 승인 뒤 `term ∈ 확장 모듈 ∧ (term prov:wasDerivedFrom o)` 인 사례가 하나 이상 있는지를 사람이 본다.

**확인 절차**

1. `bazel run //tools:term_propose -- --id <slug> --kind class --parent agt:<상위> --label-ko … --label-en … --definition … --cq CQ-NN --derived-from <관측 IRI>` 로 제안을 낸다. 검사 실패는 비영 종료다.
1. `kb/ontology/proposals/<slug>-proposal.ttl` 이 생겼고 `bazel query 'labels(srcs, //kb/ontology:modules)'` 에 없는지 본다.
1. 유저 승인 뒤 제안을 확장 모듈로 옮기고 `bazel test //kb/ontology:gate_test` 가 PASS 인지 본다.
1. 병합된 용어의 `prov:wasDerivedFrom` 이 관측 IRI 를 가리키는지 본다.

**등급** — C 다. 도구 실행은 기계이지만 반복 패턴의 인정과 승인은 사람이다.

케이스를 두지 않는다. `term_propose` 는 `bazel run` 이라 vv_run 의 허용 목록 밖이고, 2026-09-21 기준 승인 큐에 제안이 없어 양성 표본이 없다. 판정의 원본은 `tools/term_propose.py` 와 이 절차다.
