---
id: https://agentic-knowledge-base.dev/id/chunk/486c23bf-6f0f-434d-9f68-98eac5f9e46e
type: schema
level: concrete
title_ko: 앵커 없는 //kg:workset 이 펼침 0 이고 //kb/dev:index 가 청크 621 의 라벨만 실어 두 뷰가 gendoc 을 통과한다
title: //kg:workset without an anchor expands zero bodies and //kb/dev:index carries only the labels of 621 chunks, and both views pass gendoc
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:40:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/fcfb14cc-a00f-4407-84ca-faec437ae32a]
verifies: [https://agentic-knowledge-base.dev/id/chunk/8d962172-f5b0-4fe3-8c9c-8598334847e4]
---
**케이스** — 생성 뷰 둘과 그 게이트를 자극으로 쓴다.

**자극** — `//kb/dev:index`(`labels.py`, 입력 `//kb/dev:bodies`)와 `//kg:workset`(기본 설정 `--//kb:role=developer`, 앵커 없음)이다. 2026-09-21 실측은 index 청크 621 · workset 라벨 641 이다.

```yaml
index:    {tool: tools/labels.py, chunks: 621, body_lines: 0}
workset:  {role: developer, anchor: "", labels: 641, expanded: 0, verdict: "예산 초과"}   # 앵커 없이는 라벨만 — 646줄 / 200줄
gate:     //:gendoc_test
```

**기대** — 세 타깃이 성공한다. `bazel-bin/kb/dev/index.md` 에 청크 본문 줄이 없고 라벨 행이 621 이다. `bazel-bin/kg/workset-developer.md` 의 머리에 `펼침 0개` 와 `앵커를 주지 않았으므로 본문은 펼치지 않는다` 가 있다. 앵커 없는 전체 목록의 `예산 초과` 는 이 케이스의 판정 밖이다.

**실행 명령** — `bazel build //kb/dev:index //kg:workset && bazel test //:gendoc_test`

**표본 근거** — 라벨 목록 뷰는 둘뿐이라 표본이 전수다. 앵커 없는 workset 은 "본문을 펼치지 않는다" 의 경계값이고, 앵커 있는 쪽은 케이스 `dispatch-workset-budget` 이 맡는다.
