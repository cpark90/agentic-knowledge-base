---
id: https://agentic-knowledge-base.dev/id/chunk/ebff2353-68b1-432c-a716-d28a7943107f
type: decision
level: logical
title_ko: 관측과 명세를 같은 이름으로 부르면 일반화 단계가 사라지고 실행 기록의 실물은 2026-09-19부터 memory 청크다
title: Naming observation and specification alike erases the generalization step, and run records have been memory chunks since 2026-09-19
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-06T11:26:44+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-06T11:26:48+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/34f0e33e-c23d-42fe-bcb2-1a7d1e3ba33c
---
**근거** — 어휘를 가르는 근거는 옛 결정(노트 0.5절)에서 그대로 승계한다.

- 처방적 명세(시나리오)와 관측(`agt:Run`)을 같은 이름으로 부르면 **관측을 명세로 올리는 일반화 단계가 사라진다.** 0.0절 동음 충돌 회피가 이 자리에 적용된 결과다.
- 관측에 level을 주지 않는 이유는 정제 수준이 요구에서 산출물로 내려가는 거리인데(0.1절) 관측은 그 정제 계층을 타고 만들어진 것이 아니기 때문이다. 이미 일어난 사실은 정제되지 않는다.
- append-only여야 실행 기록이 판정의 증거로 남는다. 덮어쓸 수 있으면 어떤 가정이 언제 깨졌는지를 뒤에서 확인할 수 없다.
- 일반화의 목적지가 KB마다 다른 것은 두 KB의 판정 주체가 다르기 때문이다. 개발 쪽은 규칙으로, 검증 쪽은 시나리오와 합격 기준으로 올라간다.

저장 자리를 바로잡는 근거는 실물이다.

- 2026-09-19부터 `vv_run --record`가 실행 기록을 `kb/vv/run/run-<UTC 시각>.md`의 memory 청크로 쓴다(`tools/vv_run.py` docstring). 이미 있는 파일은 덮지 않는다. 판정 로그도 같은 디렉토리의 실행 기록이다(`docs/rules.md` 판정 로그 행).
- `memory` plane의 수준은 concrete 하나다(`defs/kb.bzl` `RESIDENCY`). `p8-vv-plane-instances`가 `memory`를 실행 기록 `agt:Run`으로 정한다.
- 저장소에 `run-kg` 파일은 없다(2026-10-03 실측). 실행 기록의 head는 다른 청크와 같이 `chunks-kg.ttl`에 생성된다.
- 대체를 택한 까닭은 Q8-a다. 통일 기획 3단계는 결정에서 규범 문서를 생성하므로 결정의 문장이 실물과 같아야 한다.

`agt:Runbook`의 개체는 2026-10-03 실측으로 0건이다. 그 저장 진술은 옛 결론의 문언을 그대로 둔다.
