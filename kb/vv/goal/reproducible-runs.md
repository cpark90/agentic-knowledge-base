---
id: https://agentic-knowledge-base.dev/id/chunk/27096663-5ee0-4958-b91f-db0f394c595a
type: requirement
level: functional
pattern: ubiquitous
title_ko: 같은 리비전과 환경에서 검증기 재실행은 같은 판정을 내야 한다
title: Re-running a verifier at the same revision and environment must yield the same verdict
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T15:40:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/2b1e5103-9b9d-43da-9231-6b4027bc370e]
---
**검증 목표** — 재현성이 검증 청크의 속성이 아니라 환경 할당의 조건이라는 결정이 실행기와 hermetic 테스트로 뒷받침된다는 것이 보여져야 한다. 같은 리비전·환경에서 검증기를 다시 돌리면 같은 결과가 나온다.

- **이해관계자**: 업체 · 검증 역할 · **관심사**: 재현성

**무엇을 관측하면 성립하는가**

- 같은 입력으로 게이트 테스트를 캐시 없이 두 번 돌리면 두 번 다 같은 판정이다.
- 실행 기록에 리비전·워킹트리 변경 여부·bazel·python 버전·OS·seed 유무가 적힌다. 명령은 결정적이라 seed는 없다.
- 테스트는 `--incompatible_strict_action_env`의 샌드박스에서 돌아 환경 변수가 결과에 섞이지 않는다.

판정의 원본은 `.bazelrc`와 `tools/vv_run.py`의 `revision`·`environment`이고 재현의 단위는 케이스의 실행 명령이다.
