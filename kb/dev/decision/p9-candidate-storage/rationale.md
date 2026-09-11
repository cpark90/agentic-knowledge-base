---
id: https://agentic-knowledge-base.dev/id/chunk/284d98e4-ea66-4433-a722-20cb9f3b5a5c
type: decision
level: logical
title_ko: 후보가 deps에 섞이면 빌드 그래프가 가능성을 사실로 만든다
title: Candidates in deps would let the build graph turn possibility into fact
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
generated: {by: hci/claude-opus-5, at: 2026-09-10T20:00:00+09:00}
verified: [{by: orchestrator/claude-fable-5, at: 2026-09-11T18:20:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/b4561dfb-19ea-4f34-b57e-c241cae4b9da
---
**근거** (노트 9.10절, 9.4절, 부록 E.6) — Bazel deps는 확정 의존이고 분석 시점 검사(TIM·수준 허용표)와 증분 재판정의 단위다. 후보가 deps에 들어가면 미확정 가능성이 빌드 의존이 되어 재판정 범위를 부풀리고 영향 분석(`rdeps`)이 틀린다. 자리를 나누면 확정이 한 줄 diff로 리뷰되고, `wasDerivedFrom`이 있어 확정을 되돌릴 때 옛 후보 집합이 복구된다. 변수 하나 = 파일 하나는 42줄 청크 규칙과 체크박스 뷰의 단위를 일치시킨다.
