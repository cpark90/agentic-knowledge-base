---
id: https://agentic-knowledge-base.dev/id/chunk/5680c0bc-347b-47f1-a8ad-5b4ef768702f
type: contract
level: logical
title_ko: assumes와 refersTo의 대상이 전부 실재하고 ODD 조건은 판정 방법을 갖고 전제 없는 살아 있는 청크는 0이다
title: Every assumes and refersTo target exists, every ODD condition has a judgement method, and no living chunk lacks a premise
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/7e9efd2b-38fd-41d4-8e6a-a98dfc7f24bb]
---
**합격 기준** — 기준 종류는 **불변식**이다. 병합 그래프에서 `?item agt:assumes ?a`의 `?a`는 주어로 실재하고, `?a agt:refersTo ?cond`의 `?cond`는 ODD 그래프에 있으며, 살아 있는 청크 중 `agt:assumes`가 없는 것은 0이다.

**판정식**

- 음성(가정 부재): 그래프에 없는 `id:asm-…`을 `assumes`에 적으면 `//kg:gate_test`가 `FAIL [dangling] <파일>: <청크> 의 agt:assumes 대상이 없다: <IRI> (참조 무결성 8.2절)`로 끝난다.
- 음성(ODD 밖): 가정의 `agt:refersTo`가 ODD에 없는 속성이면 `FAIL [odd-ref] <파일>: <가정> 가 ODD에 없는 속성을 참조: <IRI> (0.4절 — ODD를 먼저 확장하라)`로 끝난다.
- 양성: `bazel test //kg:gate_test //kb/odd:gate_test`가 PASS이고 `bazel build //kg:cq`의 CQ-09 행 수가 **0**이다.

**등급** — B다. 판정은 기계가 하되 그래프 병합과 질의의 실행 비용이 있다.

기준의 대상은 head 그래프·시드 그래프의 모든 `agt:assumes`와 `agt:refersTo`이고 판정의 원본은 `tools/validate.py`의 `check_dangling`과 `check_odd_refs`다. 기본 가정 `asm-chunk-conventions`만 가진 청크의 수는 이 기준 밖이고 `//kg:metrics`가 센다.
