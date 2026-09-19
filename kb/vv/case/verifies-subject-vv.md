---
id: https://agentic-knowledge-base.dev/id/chunk/3a93bc97-0661-4051-877b-55ffd4669809
type: schema
level: concrete
title_ko: 개발 패키지에서 verifies를 가진 고정물 bad_verifies의 분석이 주어 제한으로 실패한다
title: Analysis of the fixture bad_verifies carrying verifies from a development package fails with the subject restriction
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/2a7d49b7-e29a-4609-acc5-81608e38324a]
verifies: [https://agentic-knowledge-base.dev/id/chunk/ee51de32-a48b-4ade-a147-4953bce27364]
---
**케이스** — `kb/vv` 밖의 `verifies` 하나와 이 파일 자신을 자극으로 쓴다.

**자극** — `defs/tests/BUILD.bazel`의 고정물 `fx_dec`와 `bad_verifies`다. 패키지 `defs/tests`는 `kb/vv` 접두어가 없다.

```yaml
fx_dec:        {src: fx_dec.md, plane: decision, level: concrete}
bad_verifies:  {src: fx_dec.md, plane: decision, level: concrete, verifies: [fx_dec]}   # 주어가 개발 패키지
```

양성 표본은 이 케이스 자신이다. 패키지 `kb/vv/case`의 `schema`·`concrete` 타깃이 `kb/dev/decision`의 결정 복합체(결론 수준 concrete)를 `verifies` 한다.

**기대** — `bad_verifies`의 분석이 실패하고 메시지에 `verifies 의 주어는 V&V KB 청크뿐이다 (8.5절)`가 있다. `verifies_subject_test`는 그 실패를 기대하므로 PASS다. 양성 실행 `bazel build //kb/vv/...`는 성공한다.

**실행 명령** — `bazel test //defs/tests:verifies_subject_test && bazel build //kb/vv/...`

**표본 근거** — 음성 표본은 대상·수준을 전부 맞추고 주어의 위치만 틀리게 하여 실패 원인을 패키지 접두어 하나로 좁힌다. 양성 표본을 이 파일로 두면 케이스가 자기 실행으로 판정되어 별도 고정물이 필요 없다.
