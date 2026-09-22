---
id: https://agentic-knowledge-base.dev/id/chunk/8eb561b7-3127-4b38-bf4c-da672e972b3f
type: schema
level: concrete
title_ko: vnv 역할에 결정 p11-execution-mode-and-workset 을 앵커로 준 작업 집합 뷰가 이웃 본문만 펼쳐 예산 200줄 안이다
title: The vnv workset anchored on the decision p11-execution-mode-and-workset expands only the neighbour bodies and fits within the 200-line budget
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:40:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/7db997bc-4f86-4b0c-aa3f-e941657a94a7]
verifies: [https://agentic-knowledge-base.dev/id/chunk/82e341ba-c47f-4677-8013-491082b24b6c]
---
**케이스** — 앵커를 준 작업 집합 뷰 하나를 자극으로 쓴다.

**자극** — `//kg:workset` 을 `--//kb:role=vnv --//kb:anchor=<결정 결론 IRI>` 로 빌드한다. 앵커는 결정 `p11-execution-mode-and-workset` 의 결론(`id:chunk/965f738a-db50-4729-a551-e58a90cd6320`, "dispatch에는 스코프로 거른 작업 집합만 전달한다")이다. 수준 창은 기본(다섯 수준 전부), 홉은 1, 예산은 200 이다.

```yaml
role:     vnv                                   # reads: requirement·artifact·decision, writes: kb/vv 의 일곱 plane
anchor:   id:chunk/965f738a-db50-4729-a551-e58a90cd6320   # 결정 결론 — 이웃은 r-015·r-020·context-budget 과 복합체 형제
observed: {list_lines: 16, expanded: 6, lines: 78, budget: 200, verdict: "예산 안"}   # 2026-09-21 실측
```

**기대** — 빌드가 성공하고 `bazel-bin/kg/workset-vnv.md` 의 머리에 `예산 판정: 이 문서 전체(라벨 목록 16줄 + 펼친 본문)의 합계 **78줄 / 예산 200줄 → 예산 안**` 이 있다. 라벨 목록 첫 줄이 `scope: vnv` 로 시작하고 `[anchor]`·`[dep]`·`[part]` 표시가 이웃마다 붙는다. 이웃 수는 앵커를 `refines` 하는 청크가 늘면 함께 는다.

**실행 명령** — `bazel build //kg:workset --//kb:role=vnv --//kb:anchor=https://agentic-knowledge-base.dev/id/chunk/965f738a-db50-4729-a551-e58a90cd6320`

**표본 근거** — vnv 는 읽기 plane 이 셋뿐이라 스코프 거름이 가장 눈에 띄는 역할이다. 앵커를 요구 `r-015` 자체로 잡는 것이 자연스러우나 그 이웃에 V&V 검증 목표가 있고 `//kg:workset` 의 `data` 에 `//kb/vv:bodies` 가 없어 본문 펼침이 샌드박스에서 실패한다. 그래서 이웃이 전부 개발 KB 인 결정 결론을 앵커로 잡는다. 앵커 없는 경계값은 케이스 `labels-before-bodies` 가 맡는다.
