---
id: https://agentic-knowledge-base.dev/id/chunk/f352bb8b-d59b-44f1-977e-83c29d9ccc64
type: artifact
level: executable
title_ko: 절 -code-fence (tools/validate.py)
title: section -code-fence in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/650f6771-cd62-485d-85c3-a08e4df10c41
composite: {id: https://agentic-knowledge-base.dev/id/composite/650f6771-cd62-485d-85c3-a08e4df10c41, title_ko: 절 복합체 -code-fence (tools/validate.py), title: section composite -code-fence in tools/validate.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/f352bb8b-d59b-44f1-977e-83c29d9ccc64, https://agentic-knowledge-base.dev/id/chunk/2a4b8195-f60c-4855-abcc-199681ca3549, https://agentic-knowledge-base.dev/id/chunk/b526b631-d6a6-4bd8-9e43-b754fabfae9b, https://agentic-knowledge-base.dev/id/chunk/6f429584-5f62-4039-9848-4d26e16a22ac], part_of: https://agentic-knowledge-base.dev/id/composite/4d158385-e139-4042-8477-a87c3deeefe2}
---
**절** — `tools/validate.py` 의 절 `-code-fence` 다. 믿음 정도 일관성

**정의** — `_code_words` · `_code_unit` · `check_belief_consistency` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 믿음 정도 일관성 ────────────────────
# 코드 단위 지식(추출 생성물 kb/dev/artifact/)의 인용 코드를 읽어, 믿음 정도가 상태 전이와 선호의 동률 깨기에 새지 않았는가를 본다
# (게이트 belief-consistency, 요구 r-032, 설계 공간 degree-of-belief-space 닫기 기준 3, Q90-a·Q137-a). 추출물은 소스와
# extract-drift 게이트로 묶여 있으므로 소스를 다시 읽지 않는다.
_CODE_FENCE = re.compile(r"^```(python|sparql)\s*$")
_AGT_TOKEN = re.compile(r"(?:\bagt:|<https://agentic-knowledge-base\.dev/agt/)([A-Za-z_][A-Za-z0-9_]*)")
# 상태의 어휘 — 링크 상태(link-state-ontology)·후보와 확정 링크 클래스(p10-candidate-and-confirmed-link)·설계 공간 상태와 그 파이썬 상수
_STATE_WORDS = re.compile(r"^(?:linkState|CandidateLink|ConfirmedLink|spaceStatus|LINK_STATE_[A-Z_]+)$")
_PREFERENCE_WORDS = re.compile(r"^preferredOver$")   # 선호의 부분순서 (space-ontology, p9-preference-partial-order)
_BELIEF_WORDS = re.compile(r"belief", re.IGNORECASE)  # 믿음 정도의 어휘(belief-ontology)와 그것을 계산하는 이름
# 상태 전이를 정한 결정(결론)과 선호의 부분순서를 정한 결정(결론) — 코드가 refines 로 이 결론을 구현한다고 선언한다
_TRANSITION_DECISIONS = (str(kb_lib.ID) + "chunk/9deed62a-70ad-4a87-99a2-73c11e1a4453",   # p9-evidence-ledger-with-belief
                         str(kb_lib.ID) + "chunk/5287133e-f7a3-4913-8aaf-062647cf5491")   # p10-candidate-and-confirmed-link
_TIE_BREAK_DECISIONS = (str(kb_lib.ID) + "chunk/c6c78803-bdb6-4ca2-9b07-bba7878f3a01",)    # p9-preference-partial-order
_CLOSED_RULES = """
PREFIX agt: <https://agentic-knowledge-base.dev/agt/>
SELECT DISTINCT ?rule WHERE {
  ?space a agt:Space ; agt:hasCandidate ?c .
  ?c agt:linkFrom ?rule ; agt:linkState "confirmed" .
  ?node agt:beliefRule ?rule .
}"""
```
<!-- 인용 끝 -->
