---
id: https://agentic-knowledge-base.dev/id/chunk/5a9fe231-83f7-42c0-8949-35d799fe8b82
type: decision
level: logical
title_ko: 손 문서는 두 번째 원본이 되고 plane 하나에 형식 하나인 골격 청크가 단순하고 확고하다
title: A hand-written document becomes a second source, and a skeleton chunk with one form per plane is simple and firm
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:13:51+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/5c148128-480b-40d0-a8ff-76bcd4884244
---
**근거** — 요구 "문서는 저장하지 않고 생성한다"는 저장된 문서가 청크와 별개의 원본이 되어 갱신 단절이 재발한다고 적는다. 규범 문서도 그 대상이다.

- 유저가 Q19에서 (b)를 골랐다. 문서 넷을 전부 생성하고 `AGENTS.md`를 마지막에 옮긴다. 기준은 구조의 단순·확고다. 그 선택지의 문언에서 `AGENTS.md`는 결정 신설과 승인이 가장 많은 문서다.
- 유저가 Q21에서 (a)를 골랐다. 그 선택지의 문언이 "plane 하나에 형식 하나"다. 이 답이 새 개념 `agt:DocumentSectionChunk`의 승인을 겸한다.
- 유저가 Q22에서 (b)를 골랐다. 문장의 자리가 결정마다 `conventions.md` 하나라 골격이 가리키는 꼴도 하나(`slug#k`)다.
- orchestrator 실측(2026-10-03)에서 `STYLEGUIDE.md`의 항목 89는 결정 56을 인용하고 결정 20은 다른 규범 문서와 공유된다. 골격이 결정이 아니라 줄을 가리켜야 공유 결정의 줄을 문서마다 나눠 싣는다.
- 순서를 복합체의 `ordered`로 두는 까닭은 순서 선언이 이미 복합체의 규칙이기 때문이다(`p4-composite-order-is-declared`). 순서가 그래프 안에 있어 `chunk2kg`가 읽는다.
- 검사는 고아 줄과 한 문서 안의 이중 소비를 함께 잡는다. 고아 줄은 문서에 실리지 않는 규약이고, 이중 소비는 한 문서 안의 같은 문장 두 벌이다. 서로 다른 문서가 같은 줄을 싣는 것을 허용하는 까닭은 두 규범 문서에 같은 문장을 실으려고 결정에 사본 줄을 두지 않게 하는 것이다(`tools/gen_norms.py` docstring).
- 생성 트리 파일과 바이트 드리프트 검사는 `.claude/skills/*/SKILL.md`(`tools/gen_skills.py`, `//:skills_drift_test`)의 선례다. 도구가 없어도 문서가 읽히고, 손 편집은 드리프트로 거부된다.
- 이 결정은 하네스가 지식에서 생성된다는 요구(`r-029`)의 한 사례다. 결정이 바뀌면 규범 문서가 재생성으로 따라온다.

표 꼴의 선택 키(`form`·`columns`·`link_column`·`continues`)는 `docs/rules.md`를 옮길 때 정했다. 절 청크 하나를 항목 묶음 하나로 두면 본문의 문법이 산문 하나로 남고, 묶음 뒤의 산문과 다음 묶음은 이어짐 절 청크가 받는다. 그래서 `docs/method.md`처럼 한 절에 묶음이 여럿인 문서도 같은 꼴로 풀린다. 표의 모든 행이 `규약:` 줄이라 근거 열이 없는 표도 고아 줄·이중 소비 검사 안에 든다. 근거 열이 없는 표의 출처는 생성기가 표 앞 한 줄로 내므로 손 문장이 둘째 원본이 되지 않는다.
