---
id: https://agentic-knowledge-base.dev/id/chunk/6189466b-4ba2-4b53-9a83-79dfbe146028
type: decision
level: logical
title_ko: 관측과 명세를 같은 이름으로 부르면 일반화 단계가 사라진다
title: Naming observation and specification alike erases the generalization step
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/696b52ee-952f-478e-9af1-cd83c82c9b88
---
**근거** (노트 0.5절)

- 처방적 명세(시나리오)와 관측(`agt:Run`)을 같은 이름으로 부르면 **관측을
  명세로 올리는 일반화 단계가 사라진다.** 0.0절 동음 충돌 회피가 이 자리에
  적용된 결과다.
- 관측에 level을 주지 않는 이유는 정제 수준이 요구에서 산출물로 내려가는
  거리인데(0.1절) 관측은 그 계층을 타고 만들어진 것이 아니기 때문이다.
  이미 일어난 사실은 정제되지 않는다.
- append-only여야 실행 기록이 판정의 증거로 남는다. 덮어쓸 수 있으면 어떤
  가정이 언제 깨졌는지를 뒤에서 확인할 수 없다.
- 일반화의 목적지가 KB마다 다른 것은 두 KB의 판정 주체가 다르기 때문이다 —
  개발 쪽은 규칙으로, 검증 쪽은 시나리오와 합격 기준으로 올라간다.
