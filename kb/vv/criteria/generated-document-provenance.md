---
id: https://agentic-knowledge-base.dev/id/chunk/adc6879f-8333-4dcd-8ada-fed795f81f1b
type: contract
level: logical
title_ko: 생성 문서 전부의 머리가 G1~G7 을 만족하고 머리가 빠진 문서는 gendoc 이 G1 로 거부한다
title: The head of every generated document satisfies G1 to G7, and a document without the head is rejected by gendoc under G1
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:35:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/525a923d-3ef4-4cc7-979d-891306f083c0]
---
**합격 기준** — 기준 종류는 **산출물 품질**이다. 뷰마다 `head(doc) = [h1, 생성기, 생성 시각, 입력, 질의, 재현, 성격 경고]` 이고 `생성기 ∋ gendoc/1`, `생성 시각 ~ ^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$`, `입력 ∋ 지문 sha256:`, `재현 ∋ 백틱 명령` 이다. 생성 트리 파일은 생성 시각·지문을 제외한다.

**판정식**

- 양성: `bazel test //:gendoc_test` 가 PASS 다. 대상은 `defs/kb.bzl` 의 `VIEWS` 가 가리키는 Bazel 뷰 전부와 `.claude/skills/*/SKILL.md` 다.
- 음성(머리 없음): h1 만 있고 머리 블록이 없는 문서를 `python3 tools/gendoc.py --root <루트> <파일>` 에 넣으면 ``FAIL [gendoc] <파일>:1: G1 첫 줄이 `# <이름> — <목적> (생성 파일)` 가 아니다 — kb_lib.gendoc_header 로 낸다`` 로 끝나고 종료 코드가 1 이다.
- 음성(지문 없음): `생성 시각` 은 있고 `입력` 에 지문이 없으면 ``FAIL [gendoc] <파일>:5: G4 입력 줄에 지문(`sha256:<앞 12자>`)이 없다 — kb_lib.input_fingerprint 를 쓴다`` 로 끝난다.
- 음성(순서): 머리 항목의 순서가 다르면 ``G2~G6 머리 블록 i번째 항목은 `- <키>:` 다`` 로 끝난다.

**등급** — A 다. 판정은 게이트 하나이고 사람 판단이 없다.

판정의 원본은 `tools/kb_lib.py` 의 `check_gendoc`(G1~G7 절)과 `GENDOC_HEAD_KEYS`·`GENDOC_TIME_RE` 다. 루트 밖 파일은 게이트가 `EXIT_CONFIG` 로 거부하므로 음성 표본은 `--root` 를 표본 디렉토리로 준다.
