---
id: https://agentic-knowledge-base.dev/id/chunk/2fa82a3a-2e47-4bf8-8d59-2e02da4270dd
type: decision
level: concrete
title_ko: 케이스의 명령은 실행기의 파이썬 문맥을 물려받지 않는다
title: A case command does not inherit the runner's Python context
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/2b1e5103-9b9d-43da-9231-6b4027bc370e]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-29T01:22:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/2a051063-7217-4597-b03f-4a4346e85b0e
composite: {id: https://agentic-knowledge-base.dev/id/composite/2a051063-7217-4597-b03f-4a4346e85b0e, title_ko: 검증기 실행 환경의 격리, title: Isolating the verifier execution environment}
---
**결론** — 검증기는 워크스페이스 루트를 작업 디렉토리로, **실행기의 파이썬·runfiles 변수를 걷어낸 환경**에서 돈다. 걷어내는 것은 `PYTHONSAFEPATH`·`PYTHONPATH`·`PYTHONHOME`·`RUNFILES_DIR`·`RUNFILES_MANIFEST_FILE`이다.

실행기를 어떻게 불렀는가가 케이스의 판정을 바꾸면 그것은 재현이 아니다. 같은 리비전·같은 케이스·같은 자극인데 `bazel run`과 `python3`이 다른 답을 내면 어느 쪽이 참인지 말할 수 없다.

`PYTHONPATH`를 함께 걷어내는 까닭은 따로 있다. 남겨 두면 검증기가 runfiles 사본의 모듈을 읽어 **케이스가 검사하는 대상이 소스 트리가 아니게 된다.** 검증의 대상이 바뀌는 것은 환경 문제가 아니라 판정의 오류다.

같은 이유로 검증기를 `bazel run //tools:<검증기>`로 부르는 명령은 허용 목록 밖이고 게이트 `vv-case`가 실행 전에 거부한다. 그 형태는 작업 디렉토리가 runfiles 트리라 워크스페이스 상대 경로가 자극에 닿지 못하고, 그때 나오는 입력 단계 오류가 **기대한 거부와 같은 종료 코드·문구를 낸다.** 건너뜀은 판정의 공백이지만 거짓 통과는 틀린 판정이다.

**밀폐 예외 하나를 받는다**(유저 승인 2026-09-29). 이 격리를 검사하는 게이트 `vv-run-env`는 실측 일치를 위해 호스트의 `HOME`을 물려받는다(`env_inherit`) — 합성 자극으로 바꾸면 실제 검증기가 죽는 재현이 아니다. 예외의 수는 문서가 아니라 ODD 조건 `cond-host-env-inherit`(≤ 1)이 판정하므로 다음 세션이 같은 판단을 다시 하지 않는다.
