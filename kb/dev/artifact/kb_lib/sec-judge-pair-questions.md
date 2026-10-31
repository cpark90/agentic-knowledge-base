---
id: https://agentic-knowledge-base.dev/id/chunk/fcb30a31-da2f-4bba-9dab-90c28d339362
type: artifact
level: executable
title_ko: 절 judge-pair-questions (tools/kb_lib.py)
title: section judge-pair-questions in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6309baee-3513-4835-affe-e76a4382e7d5
composite: {id: https://agentic-knowledge-base.dev/id/composite/6309baee-3513-4835-affe-e76a4382e7d5, title_ko: 절 복합체 judge-pair-questions (tools/kb_lib.py), title: section composite judge-pair-questions in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/fcb30a31-da2f-4bba-9dab-90c28d339362, https://agentic-knowledge-base.dev/id/chunk/674eca0b-5a5b-45f5-b382-4fa958bafcdc, https://agentic-knowledge-base.dev/id/chunk/df43fa6f-d424-49d0-aec2-0aea8545572a, https://agentic-knowledge-base.dev/id/chunk/d536eb83-d269-4b4d-a6ed-281a4a2f54c2], part_of: https://agentic-knowledge-base.dev/id/composite/3e4f98b8-3c0f-42e8-91f7-7868662123ed}
---
**절** — `tools/kb_lib.py` 의 절 `judge-pair-questions` 다. 쌍 판정의 질문과 대상 꼴

**정의** — `pair_question` · `pair_target` · `parse_pair_target` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 쌍 판정의 질문과 대상 꼴 ────────────────────
# 동시 편집이 첫 근거인 링크 후보를 판정자 둘이 쌍 단위로 판정한다. 질문은 종류가 겹침이면 `overlapsHolds`, 그 밖이면
# `proposedLinkHolds` 이고 둘 다 noul 형이다. 판정 로그의 `대상` 열은 `<앵커 IRI> ↔ <대상 IRI> · <링크 종류>` 의 고정 꼴이다 —
# 링크 종류를 함께 적는 까닭은 `proposedLinkHolds` 의 답이 종류마다 다르고 증거를 붙일 후보 링크 개체의 IRI 가 종류를 담기 때문이다.
JUDGE_PAIR_QUESTIONS = {"overlapsWith": "overlapsHolds"}   # 링크 종류 → 질문. 표에 없는 종류는 JUDGE_PAIR_DEFAULT 다
JUDGE_PAIR_DEFAULT = "proposedLinkHolds"
JUDGE_PAIR_SEP, JUDGE_PAIR_KIND_SEP = " ↔ ", " · "
JUDGE_PAIR_TARGET = re.compile(r"^(\S+) ↔ (\S+) · ([A-Za-z]+)$")
JUDGE_NOUL_POLARITY = {"yes": "+", "no": "-"}              # noul 값 → 증거 극성. 그 밖의 값은 증거가 아니다
POLARITY_MARK = {"+": "+", "-": "−"}                  # 증거 극성 → 생성 뷰의 표기. 반박은 U+2212 다 — 단독 하이픈은 G14 의 빈 칸 표기와 겹친다 (agt:polarity 정의 "지지(+) 또는 반박(−)")
```
<!-- 인용 끝 -->
