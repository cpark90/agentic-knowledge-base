---
id: https://agentic-knowledge-base.dev/id/chunk/6767c763-0377-4daf-9048-c63ddf3cd853
type: annotation
level: concrete
title_ko: 어휘 케이스의 음성 자극은 미정의 술어가 없어도 종료 1 을 내므로 종료 코드가 분기를 가르지 않는다
title: The vocabulary case's negative stimulus exits 1 even without the undefined predicate, so the exit code does not discriminate the branch
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/odd-agentic-knowledge-base}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/90e003d5-92eb-5220-b85d-cdb05fc96ece]
generated: {by: vnv/claude-opus-5, at: 2026-10-04T22:47:50+09:00}
---
nitpick (non-blocking): 이 케이스의 음성 자극은 통제 어휘 분기 하나만을 자극하지 않는다.

대상: https://agentic-knowledge-base.dev/id/chunk/90e003d5-92eb-5220-b85d-cdb05fc96ece

본문: 2026-09-23 측정에서 자극의 `agt:unknownPredicate` 만 뺀 그래프도 같은 명령에서 `FAIL [shacl]` 로 종료 1 을 냈다. 자극의 개체가 수준·한영 라벨을 갖지 않아 `agt:ChunkShape` 를 함께 어기기 때문이다. 따라서 이 케이스에서 vocab 분기를 고정하는 것은 종료 코드가 아니라 `contains` 의 문구 둘뿐이다.

제안: 자극에 수준과 한영 라벨을 더해 shape 를 만족시키면 종료 코드도 통제 어휘 분기만을 가리킨다.

해소: 해소 — 자극에 수준·한영 라벨·상태·생성자·슬롯을 더해 shape 와 writer 검사를 만족시켰고, 미정의 술어 한 줄만 뺀 통제가 같은 명령에서 종료 0 으로 PASS 임을 실험으로 확인해 종료 코드가 통제 어휘 분기만을 가리킨다.
