---
id: https://agentic-knowledge-base.dev/id/chunk/eccccc47-d3e9-4480-8b14-b2511afe1457
type: schema
level: concrete
title_ko: gendoc_test 가 PASS 이고 대시 셀과 분모 없는 백분율을 가진 표본 문서는 G14·G15 두 건으로 거부된다
title: gendoc_test passes, and a sample document with a dash cell and an undenominated percentage is rejected with two findings, G14 and G15
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:40:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/02fd5ecb-544d-434e-9146-96a0e3607851]
verifies: [https://agentic-knowledge-base.dev/id/chunk/160ca62a-0dd2-4b06-a5e5-21bb1fc54fbe, https://agentic-knowledge-base.dev/id/chunk/2314093a-f5e3-4fc0-96a0-6c5d35db03ee]
---
**케이스** — 게이트 하나와 임시 표본 하나를 자극으로 쓴다.

**자극** — `//:gendoc_test` 와 스크래치 디렉토리 `<S>` 의 `badform.md` 다. 표본은 규약에 맞는 머리 블록 뒤에 대시 셀 하나와 `50%` 한 곳을 둔다. `python3 tools/gendoc.py --root <S> <S>/badform.md` 로 넣는다.

```yaml
badform.md:
  head:  ["# form — 서식 표본 (생성 파일)", "- 생성기: `tools/x.py` · gendoc/1", "- 생성 시각: 2026-09-21T00:00:00Z", "- 입력: 입력 파일 1개: `a.md` · 지문 `sha256:000000000000`", "- 질의: 표본", "- 재현: `bazel build //x`", "- 이 파일은 뷰다. 저장하지 않고 인용한다."]
  body:  ["## 표", "| a | b |", "|---|---|", "| 1 | — |", "비율은 50% 다."]
```

**기대** — `gendoc_test` 가 PASS 다. 표본은 두 줄 ``FAIL [gendoc] badform.md:14: G14 빈 표 셀 — 비우거나 대시를 쓰지 않고 `없음` 으로 적는다 (Microsoft Writing Style Guide, Tables)`` 와 ``FAIL [gendoc] badform.md:16: G15 분모 없는 백분율 `50%` — `n/d = p.p%` 꼴로 적는다 (kb_lib.pct)`` 뒤에 요약 `FAIL [gendoc] — 2건 (생성 문서 1개)` 로 끝나고 종료 코드가 1 이다. 2026-09-21 실측과 같다.

**실행 명령** — `bazel test //:gendoc_test`

**표본 근거** — 양성은 게이트 대상 전부라 전수다. 음성은 2026-09-19 실측에서 갈래가 가장 많던 둘(빈 값 표기 네 갈래 · 백분율)을 고른다. 머리 블록 쪽 음성은 케이스 `generated-document-provenance` 가 맡는다.
