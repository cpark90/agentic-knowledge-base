---
id: https://agentic-knowledge-base.dev/id/chunk/db7470cb-ff9c-45b3-8817-27bf77a30aaf
type: requirement
level: functional
pattern: ubiquitous
title_ko: 감사 보고서는 선언된 입력만으로 생성되어야 한다
title: The audit report must be generated from declared inputs alone
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:40:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/ba638521-e9b0-4c38-b073-44230ac22785]
---
**검증 목표** — 감사와 온보딩이 체계의 출력만으로 동작한다는 결정이 샌드박스 빌드로 강제된다는 것이 보여져야 한다. 감사 보고서의 입력은 그래프 union과 관측 청크 본문뿐이고 체계 밖 정보는 0이다.

- **이해관계자**: 업체 · 감사 역할 · **관심사**: 자족성

**무엇을 관측하면 성립하는가**

- `//kg:audit`이 `genrule`이고 `srcs`가 그래프 라벨과 본문 filegroup뿐이다. 샌드박스에는 선언된 입력만 있어 선언되지 않은 파일을 읽으면 생성이 실패한다.
- 생성기 `tools/weave.py`는 git·네트워크를 부르지 않는다. 리비전은 실행 기록의 본문에서 읽는다.
- 보고서의 머리에 `체계 밖 정보 0`이 있고 끝의 자족성 선언이 재생성 명령 `bazel build //kg:audit`을 적는다.
- 같은 입력으로 다시 생성하면 수치가 같다.

판정의 원본은 `kg/BUILD.bazel`의 `audit` 타깃과 `defs/knowledge.bzl`의 `kb_weave`, `tools/weave.py`의 `render_audit`이다.
