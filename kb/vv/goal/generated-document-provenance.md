---
id: https://agentic-knowledge-base.dev/id/chunk/525a923d-3ef4-4cc7-979d-891306f083c0
type: requirement
level: functional
pattern: ubiquitous
title_ko: 생성 문서는 생성기·생성 시각·입력 지문·질의·재현 명령을 머리에 담아야 한다
title: A generated document must carry its generator, generation time, input fingerprint, query and rebuild command in its head
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/4ae7ad6d-fabc-4925-bc6a-4aa518eeab55]
---
**검증 목표** — 생성 문서의 머리가 h1 한 줄과 여섯 줄의 고정 순서라는 결정이 생성기와 게이트가 공유하는 함수 하나로 강제된다는 것이 보여져야 한다. 생성기는 `kb_lib.gendoc_header` 로 머리를 내고 게이트 `gendoc` 은 `kb_lib.check_gendoc` 으로 같은 규약을 판정한다.

- **이해관계자**: 감사 역할 · 새로 들어오는 에이전트 · **관심사**: 사본이 원본으로 오인되지 않는 것

**무엇을 관측하면 성립하는가**

- 모든 생성 뷰의 첫 줄이 `# <이름> — <목적> (생성 파일)` 이고 그 아래 `생성기` → `생성 시각` → `입력` → `질의` → `재현` → 성격 경고의 순서다(G1~G7).
- `생성기` 줄에 규약 버전 `gendoc/1` 이, `생성 시각` 에 ISO 8601 UTC 초가, `입력` 에 파일 목록과 `sha256:` 지문이, `재현` 에 백틱 명령이 있다.
- 생성 트리 파일(`.claude/skills/*/SKILL.md`)은 생성 시각·지문이 없고 결정론이 그 자리를 대신한다.
- 머리가 빠지거나 순서가 다른 문서는 `FAIL [gendoc] <파일>:<줄>: G1 …` 로 거부된다.

판정의 원본은 `tools/kb_lib.py` 의 `gendoc_header`·`check_gendoc` 과 `BUILD.bazel` 의 `gendoc_test` 다.
