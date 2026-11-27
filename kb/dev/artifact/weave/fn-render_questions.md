---
id: https://agentic-knowledge-base.dev/id/chunk/4650cc1b-20d3-4c11-8858-478478d8b2c2
type: artifact
level: executable
title_ko: 함수 render_questions (tools/weave.py)
title: function render_questions in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T02:39:25Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2ed81f6f-d352-4431-9436-bf12e6534721, https://agentic-knowledge-base.dev/id/chunk/75937272-b60e-4d9d-8919-5253ef837ff4, https://agentic-knowledge-base.dev/id/chunk/7a42dec5-1fd8-42b8-b484-cc1380047b67, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7, https://agentic-knowledge-base.dev/id/chunk/d5be3602-e40e-4447-a03c-0d626399f32a, https://agentic-knowledge-base.dev/id/chunk/daf683a0-9d84-4163-9eb0-2ea99d87494d, https://agentic-knowledge-base.dev/id/chunk/ef9472b8-59c4-47b6-91eb-b0532f4403de, https://agentic-knowledge-base.dev/id/chunk/f608a299-e952-4c87-88d2-f11dd286bc42, https://agentic-knowledge-base.dev/id/chunk/f6cf75ba-7624-4742-a6f9-b56a69f540b1]
part_of: https://agentic-knowledge-base.dev/id/composite/17bed729-be8b-4186-8432-0a0e0f1b5673
---
**함수** — `render_questions(m, citing, sheet_paths, legacy_paths, inputs)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render_questions(m: Model, citing: list, sheet_paths: list[str], legacy_paths: list[str], inputs: list[str]) -> str:
    ix = QuestionIndex(sheet_paths, legacy_paths, citing, user_decision_evidence(m.g))
    open_n = sum(1 for v in ix.sheets.values() if v)
    answered = sum(1 for q in ix.questions.values() if q["answer"])
    bare_places = sum(ix.bare.values())
    h = head("questions", "질문 반영처",
             "질문지(`harness/user/Q-*.md` · `archive/Q-*.md`)의 `## Qn.` 절마다 제목 · 질문지 `created` · 첫 `답:` 줄, 단위 지식·설계 공간 본문의 "
             "긴 꼴 `Q-NNNN#Qn`(`Q-NNNN Qn`)과 짧은 꼴 `Qn-x` 인용, 설계 공간 그래프의 `agt:evidenceKind agt:userDecision` 증거의 `agt:evidenceRef`, "
             "옛 질문지(`archive/legacy/*.md`)의 제목 · `status` · 본문의 `legacy/<파일 이름>.md` 인용", m.g, inputs,
             [f"- 질문지 {len(ix.sheets)} (열림 {open_n} · 보관 {len(ix.sheets) - open_n}) · 질문 {len(ix.questions)} · 답 줄이 있는 질문 {answered} · "
              f"인용된 질문 {len(ix.cited())} · 유저 결정 증거가 가리키는 질문 {sum(1 for k in ix.evidence if isinstance(k, int))} · "
              f"풀리지 않는 인용 {len(set(ix.unresolved)) + len(ix.dups)} · 뒤집힘 묶음 {len(ix.reversals())} · 옛 질문지 {len(ix.legacy)}",
              f"- 답 문자 없는 꼴 `Qn` 은 질문 인용으로 세지 않는다 — {bare_places}곳 · 번호 {len(ix.bare)}개. 질문지 번호 체계보다 앞선 "
              "2026-09-10 세션의 유저 결정이 같은 꼴이라 질문지로 풀 수 없다"],
             source="질문지와 단위 지식 본문")
    body = _questions_table(ix) + _questions_unresolved(ix) + _questions_reversals(ix) + _questions_legacy(ix)
    return kb_lib.gendoc_assemble(h, body, inputs)
```
<!-- 인용 끝 -->
