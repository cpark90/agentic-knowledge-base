---
id: https://agentic-knowledge-base.dev/id/chunk/ba904590-9eda-4d49-8f05-18e8d160388d
type: artifact
level: executable
title_ko: gendoc_test 가 등록된 뷰 전부와 skill 을 통과하고 머리 블록 없는 표본 문서는 G1 로, 지문 없는 표본은 G4 로 거부된다
title: gendoc_test passes over every registered view and the skills, and a sample without the head block is rejected under G1 and one without a fingerprint under G4
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/adc6879f-8333-4dcd-8ada-fed795f81f1b]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-06T10:55:32+09:00}
layer: process
---
**검증기** — 게이트 하나와 임시 표본 둘을 자극으로 쓴다.

**자극** — `//:gendoc_test` 다. `docs` 는 `:skills` 와 `defs/kb.bzl` 의 `VIEWS` 다(뷰 목록의 단일 정의처). 음성 표본은 스크래치 디렉토리 `<S>` 의 파일 둘이고 `python3 tools/gendoc.py --root <S> <S>/<파일>` 로 넣는다.

```yaml
nohead.md:   ["# nohead", "", "본문만 있는 문서다."]                                                       # 머리 블록 없음 — G1
nofinger.md: ["# x — y (생성 파일)", "", "- 생성기: `tools/x.py` · gendoc/1", "- 생성 시각: 2026-09-21T00:00:00Z", "- 입력: 입력 파일 1개: `a.md`", "- 질의: 표본", "- 재현: `bazel build //x`", "- 이 파일은 뷰다. 저장하지 않고 인용한다."]   # 지문 없음 — G4
```

**기대** — `gendoc_test` 가 PASS 다. 표본 하나는 ``FAIL [gendoc] nohead.md:1: G1 첫 줄이 `# <이름> — <목적> (생성 파일)` 가 아니다 — kb_lib.gendoc_header 로 낸다`` 와 요약 `FAIL [gendoc] — 1건 (생성 문서 1개)` 로 끝나고 종료 코드가 1 이다. 표본 둘은 ``FAIL [gendoc] nofinger.md:5: G4 입력 줄에 지문(`sha256:<앞 12자>`)이 없다 — kb_lib.input_fingerprint 를 쓴다`` 로 끝난다. 음성 표본 둘의 문구는 2026-09-21 실측과 같고 뷰 목록은 `VIEWS` 가 정한다.

**실행 명령** — `bazel test //:gendoc_test`

**판정 범위** — 양성은 게이트의 대상 전부라 전수다. 음성은 머리의 유무(G1)와 머리 안 필수 값의 유무(G4)로 두 경우를 하나씩 덮는다. 임시 파일 자극은 vv_run 이 실행하지 않으므로 서술로 둔다.

**검증 대응물** — 없음. 옮기기 전 케이스가 `verifies` 하던 결정 `p12-generated-document-header` 의 결론은 `concrete` 수준이라 `executable` 검증기가 `verifies` 할 수 없다.
