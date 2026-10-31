---
id: https://agentic-knowledge-base.dev/id/chunk/d822fdc1-b484-44a5-b885-a8d3b3549d1f
type: norm
level: logical
title_ko: docs/method.md 절 갱신의 이어짐 — 링크 상태는 평가 결과이고 무효화는 삭제가 아니다
title: docs/method.md update section continued — link state is an evaluation result and invalidation is not deletion
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/c4e92186-f234-481e-b847-7b3b32d283c0
continues: true
---
**링크 상태는 저장값이 아니라 평가 결과다**(유저 승인 2026-09-23, 링크 견고성 D). 링크의 `when`은 `in(<조건>)`과
`!`, `&&`, `||`를 쓰는 3값 논리의 ODD 조건 참조로 평가되고, 그 값이 거짓이면 확정 링크는 `suspect`로, 후보는 `invalid`로
유도된다. 유도된 상태는 그래프에 쓰지 않고 `bazel run //tools:assume_check`의 보고와 `//kg:metrics`에서만 물질화된다.
전파는 `tools/kb_lib.py`의 `SUSPECT_TRIGGERS`에 선언된 링크 종류만 도는데, 지금은 `supersedes` 하나이고 선언에 없는
종류는 돌지 않는다. 추적 매트릭스가 `suspect`로 포화되는지는 `metrics`의 포화율 한 줄이 관측한다(경고선 20%).
**본문 해시가 바뀌면 링크를 재검증하는** 경로는 `bazel run //tools:revalidate -- --base <rev>`가 닫았다. 이 도구는
바뀐 단위 지식을 양 끝으로 갖는 `agt:Link` 개체를 그래프의 같은 IRI로 낸다.

무효화는 삭제가 아니다. 무효화 이력은 일반화의 입력이고, 어떤 가정이 자주 깨지는가는 그 자체로 일반화
대상이다.
