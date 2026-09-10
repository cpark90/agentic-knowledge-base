---
id: https://agentic-knowledge-base.dev/id/chunk/36ad6f0f-c619-4487-8ce0-b4a41aa16ed9
type: decision
level: logical
title_ko: 낮은 단계가 위 단계를 예측한다는 전제도 판정 방법을 동반해야 한다
title: The premise that lower steps predict higher ones must itself be checkable
status: stable
sources: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/962ef704-4544-41b5-8b6d-bea52f11c595
---
**근거** (노트 8.13절) — 3~4단계 통과가 실환경 통과를 예측한다는 근거가 없으면 환경 계층 자체가 무의미하다. 낮은 단계에서 거른다는 설계는 낮은 단계의 판정이 위 단계의 판정과 상관한다는 전제 위에 서 있고, 그 전제는 가정이므로 판정 방법을 동반해야 한다 (6.5절·6.9절).

- 요인별로 쪼개는 이유는 신뢰도가 단일 수치가 아니기 때문이다. 하나의 수치로 두면 잘 잡는 요인의 성적이 못 잡는 요인을 가리고, 할당표를 고칠 근거가 나오지 않는다.
- 네 근거의 성격이 다르다. 상관과 이탈 관측은 사후 측정이고 mock 계약과 합성 데이터 분포는 사전 검사다 — 사전 검사만으로는 못 잡는 요인이 남으므로 둘 다 필요하다.
