---
id: https://agentic-knowledge-base.dev/id/chunk/f6cfb6a4-3729-4b38-a2d0-0deab894be48
type: artifact
level: executable
title_ko: 앵커 없는 //kg:workset 이 펼침 0 이고 //kb/dev:index 가 청크 1982 의 라벨만 실어 두 뷰가 gendoc 을 통과한다
title: //kg:workset without an anchor expands zero bodies and //kb/dev:index carries only the labels of 1982 chunks, and both views pass gendoc
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/fcfb14cc-a00f-4407-84ca-faec437ae32a]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-05T12:48:58+09:00}
layer: process
---
**검증기** — 생성 뷰 둘과 그 게이트를 자극으로 쓴다.

**자극** — `//kb/dev:index`(`labels.py`, 입력 `//kb/dev:dev`)와 `//kg:workset`(기본 설정 `--//kb:role=developer`, 앵커 없음)이다. 2026-10-05 실측은 index 청크 1982 · workset 라벨 2010 이다.

```yaml
index:    {tool: tools/labels.py, chunks: 1982, body_lines: 0}
workset:  {role: developer, anchor: "", labels: 2010, expanded: 0, verdict: "예산 초과"}   # 앵커 없이는 라벨만 — 합계 59346토큰 / 예산 5418토큰
gate:     //:gendoc_test
```

**기대** — 세 타깃이 성공한다. `bazel-bin/kb/dev/index.md` 에 청크 본문 줄이 없고 라벨 행이 1982 이다. `bazel-bin/kg/workset-developer.md` 의 머리에 `펼침 0개` 와 `앵커를 주지 않았으므로 본문은 펼치지 않는다` 가 있다. 앵커 없는 전체 목록의 `예산 초과` 는 이 케이스의 판정 밖이다.

**실행 명령** — `bazel build //kb/dev:index //kg:workset && bazel test //:gendoc_test`

**판정 범위** — 라벨 목록 뷰는 둘뿐이라 표본이 전수다. 앵커 없는 workset 은 "본문을 펼치지 않는다" 의 경계값이고, 앵커 있는 쪽은 케이스 `dispatch-workset-budget-factor-1` 이 맡는다.

**검증 대응물** — 없음. 옮기기 전 케이스가 `verifies` 하던 결정 `p4-label-is-the-interface` 의 결론은 `concrete` 수준이라 `executable` 검증기가 `verifies` 할 수 없다.
