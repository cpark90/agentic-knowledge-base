---
id: https://agentic-knowledge-base.dev/id/chunk/3ff5bc7a-3ad4-4f8b-a855-bb3b80d2034a
type: annotation
level: concrete
title_ko: usesDefinition 모듈 간 치역 관측 — 재측정과 pct 자극이 성공 조건의 단위 불일치를 드러낸다
title: Cross-module usesDefinition range observation — remeasurement and the pct stimulus expose a unit mismatch in the success condition
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
generated: {by: vnv/claude-sonnet-5, at: 2026-10-02T10:20:00+09:00}
---
thought (non-blocking): usesDefinition 재측정은 667/183에서 737/195로 늘었고 pct 자극의 revalidate 호출부(13)는 handoff의 "36 안팎"과 단위가 달라 성공 여부를 액면으로 대조할 수 없다.

대상: https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23

본문: `agt:usesDefinition`을 재측정하면 737건(모듈 간 195건, 전부 `kb_lib` 치역)으로 2026-10-01 인수 당시의 667/183보다 늘었고, 무작위 20간선 손 확인은 20/20 참·오탐 0이며 `//kg:gate_test --nocache_test_results` 단독 실행은 61.4초다. 소스의 `kb_lib.<이름>` 호출 표현식 225건 중 18건이 해소 실패다 — 17건은 `kb_lib`가 `chunk2kg`의 함수 다섯(`load_tokenizer` 등)을 재수출하는 간접 호출이고 1건은 함수 바깥(모듈 최상위)의 호출이며, 별도로 `getattr(kb_lib, "이름", 기본값)` 꼴의 동적 상수 참조 33건은 설계상 제외된 상수 참조다. `pct` 본문을 고친 스크래치 사본(현재 워킹트리를 임시 커밋해 base로 삼았다)에서 `revalidate --base HEAD`의 호출부는 13(developer 보고 12에서 1 증가, 호출 모듈 8 전부 포함)이고 내가 다시 센 호출 표현식은 38(직접 16 · 매개변수로 받는 쪽 22)로 승인된 "36 안팎"에 근접한다. 호출부는 정의 청크 단위이고 36은 호출 표현식 단위라 두 수를 같은 자로 잴 수 없으므로, 교차 모듈 해소 자체는 정확해도(모듈 8 전부 포착·오탐 0) "36 안팎"과 revalidate 출력을 액면으로 대조하는 판정은 부분 성공이다.

제안: orchestrator가 handoff 3번 과제(`revalidate`의 "호출부" 경계 문서화)를 이 단위 차이까지 반영해 마무리한다.

해소: 열림 — 성공 조건의 단위 불일치가 문서에 아직 반영되지 않았다.
