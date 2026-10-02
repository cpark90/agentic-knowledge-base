---
id: https://agentic-knowledge-base.dev/id/chunk/7aa3c343-6435-4646-8f2b-a0a45fc33d8b
type: decision
level: logical
title_ko: 자극이 여럿을 어기면 종료 코드가 무엇을 가리키는지 말하지 못한다
title: A stimulus violating several rules leaves the exit code pointing at nothing in particular
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-23T13:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/6eea0a91-2e8d-400c-a830-ea653fa104f0
---
**근거** — 2026-09-23 실측이 문제를 드러냈다. 케이스 `foreign-vocabulary-rejected`의 자극에서 어휘 밖 술어만 빼도 같은 명령이 `FAIL [shacl]`로 종료 1을 냈다. 자극 개체가 수준과 한영 라벨을 갖지 않아 shape 검사를 함께 어기기 때문이다. 판정 주석 `vocab-stimulus-not-minimal`이 그것을 `nitpick`으로 적었다.

그 케이스에서 통제 어휘 분기를 고정하는 것은 종료 코드가 아니라 `contains` 문구 둘뿐이다. 문구 대조가 없었다면 케이스는 **다른 이유로 실패한 것을 통과로 읽었을 것이다.** `p8-machine-readable-case`가 문구 대조를 들여온 까닭이 여기서 실물로 확인된다.

최소성을 요구하는 근거는 게이트 메시지의 수명에 있다. 게이트 메시지는 수정 방향이라 개선되고 바뀐다. 문구가 바뀌면 케이스는 실패하고 사람이 고치는데, 그때 **자극이 여전히 무엇을 어기는지**가 종료 코드로 받쳐지지 않으면 고치는 사람이 새 문구를 무엇에 맞출지 알 수 없다.

표본 근거에 어기는 규칙을 적게 하는 근거는 검사 가능성이다. 최소성은 자극을 하나씩 빼 보는 실험으로만 확인되고 그 실험은 사람이 한다. 주장을 적어 두면 다음 사람이 그것을 재검사할 수 있다.
