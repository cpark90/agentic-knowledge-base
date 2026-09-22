---
id: https://agentic-knowledge-base.dev/id/chunk/fcfb14cc-a00f-4407-84ca-faec437ae32a
type: contract
level: logical
title_ko: index 뷰는 라벨과 메타만 싣고 workset 뷰는 앵커 없이 펼침 0 이다
title: The index view carries labels and metadata only, and the workset view expands zero bodies without an anchor
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:35:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/d84aae5a-3190-44d7-9b27-02013b6b70b1]
---
**합격 기준** — 기준 종류는 **산출물 품질**이다. `body_lines(index.md) = 0` 이고 `expanded(workset, anchor = ∅) = 0` 이다. 라벨 목록의 행 수는 입력 청크 수와 같다.

**판정식**

- 양성(index): `bazel build //kb/dev:index` 가 성공하고 `bazel-bin/kb/dev/index.md` 의 머리에 `청크 N개` 가, 본문에 plane 디렉토리(h2)·항목 디렉토리(h3) 아래 라벨 행만 있다. 청크 본문의 산문 줄은 없다.
- 양성(workset): `bazel build //kg:workset` 이 성공하고 `bazel-bin/kg/workset-<role>.md` 의 머리에 `펼침 0개` 와 `앵커를 주지 않았으므로 본문은 펼치지 않는다` 가 있다.
- 양성(형태): `bazel test //:gendoc_test` 가 두 뷰를 포함해 PASS 다.
- 음성: 라벨이 본문을 대표하지 못하는 경우는 분할 신호이고 이 기준 밖이다(`label_sample` 실험).

**등급** — A 다. 판정은 생성 뷰의 형태이고 사람 판단이 없다.

판정의 원본은 `tools/labels.py`(head 만 읽는다), `tools/workset.py`(`--anchor` 없으면 `expanded = []`), `kb_lib.check_gendoc` 이다. 라벨 대표성의 측정은 `label_sample` 실험의 몫이다.
