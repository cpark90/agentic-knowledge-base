---
id: https://agentic-knowledge-base.dev/id/chunk/f6cfb6a4-3729-4b38-a2d0-0deab894be48
type: artifact
level: executable
title_ko: 앵커 없는 //kg:workset 이 펼침 0 이고 //kb/dev:index 가 단위 지식 1982 의 라벨만 실어 두 뷰가 gendoc 을 통과한다
former_title_ko: ["앵커 없는 //kg:workset 이 펼침 0 이고 //kb/dev:index 가 청크 1982 의 라벨만 실어 두 뷰가 gendoc 을 통과한다", "앵커 없는 //kg:workset 이 펼침 0 이고 //kb/dev:index 가 지식 항목 1982 의 라벨만 실어 두 뷰가 gendoc 을 통과한다"]
title: //kg:workset without an anchor expands zero bodies and //kb/dev:index carries only the labels of 1982 chunks, and both views pass gendoc
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/fcfb14cc-a00f-4407-84ca-faec437ae32a]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-25T13:46:23+09:00}
layer: process
verifies: [https://agentic-knowledge-base.dev/id/chunk/1c0459c2-171f-4194-9719-75449a207951, https://agentic-knowledge-base.dev/id/chunk/ea192023-b5a0-4dbe-bb2f-8b507575633c, https://agentic-knowledge-base.dev/id/chunk/0a421535-c9ff-40ab-a04f-cd96deb799a9]
restored: [https://agentic-knowledge-base.dev/id/chunk/1c0459c2-171f-4194-9719-75449a207951, https://agentic-knowledge-base.dev/id/chunk/ea192023-b5a0-4dbe-bb2f-8b507575633c, https://agentic-knowledge-base.dev/id/chunk/0a421535-c9ff-40ab-a04f-cd96deb799a9]
---
**검증기** — 생성 뷰 둘과 그 게이트를 자극으로 쓴다.

**자극** — `//kb/dev:index`(`labels.py`, 입력 `//kb/dev:dev`)와 `//kg:workset`(기본 설정 `--//kb:role=developer`, 앵커 없음)이다. 2026-10-05 측정은 index 단위 지식 1982 · workset 라벨 2010 이다.

```yaml
index:    {tool: tools/labels.py, chunks: 1982, body_lines: 0}
workset:  {role: developer, anchor: "", labels: 2010, expanded: 0, verdict: "예산 초과"}   # 앵커 없이는 라벨만 — 합계 59346토큰 / 예산 5418토큰
gate:     //:gendoc_test
```

**기대** — 세 타깃이 성공한다. `bazel-bin/kb/dev/index.md` 에 단위 지식 본문 줄이 없고 라벨 행이 1982 이다. `bazel-bin/kg/workset-developer.md` 의 머리에 `펼침 0개` 와 `앵커를 주지 않았으므로 본문은 펼치지 않는다` 가 있다. 앵커 없는 전체 목록의 `예산 초과` 는 이 테스트 케이스의 판정 밖이다.

**실행 명령** — `bazel build //kb/dev:index //kg:workset && bazel test //:gendoc_test`

**판정 범위** — 라벨 목록 뷰는 둘뿐이라 표본이 전수다. 앵커 없는 workset 은 "본문을 펼치지 않는다" 의 경계값이고, 앵커 있는 쪽은 테스트 케이스 `dispatch-workset-budget-factor-1` 이 맡는다.

**검증 대응물** — 이 검증기는 `tools/labels.py`, `tools/workset.py`와 `tools/gendoc.py`의 항목을 `verifies` 한다. 끝은 파일 복합체의 선언 항목(`module.md`)이고, 판정 함수 같은 부분 항목은 게이트 `code-part-link` 가 끝으로 받지 않는다. 반면 옮기기 전 테스트 케이스가 `verifies` 하던 결정 `p4-label-is-the-interface`의 결론은 `concrete` 수준이라, 같은 수준끼리만 잇는 규칙에 따라 이 검증기의 끝이 되지 않는다.
