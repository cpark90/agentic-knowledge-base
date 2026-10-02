---
id: https://agentic-knowledge-base.dev/id/chunk/cd1dfd07-5449-47a5-93d2-39f46bcccf85
type: artifact
level: executable
title_ko: 절 comment-labels (tools/kb_lib.py)
title: section comment-labels in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/163f6311-4c7b-4d2d-983e-94afa5658211
---
**절** — `tools/kb_lib.py` 의 절 `comment-labels` 다. 주석의 형식 (STYLEGUIDE §4 annotation, 결정 p7-commentary-form — 게이트 id `blocking-comment`: chunk_lint)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 주석의 형식 (STYLEGUIDE §4 annotation, 결정 p7-commentary-form — 게이트 id `blocking-comment`: chunk_lint) ────────────
# annotation 청크는 주석이다. 첫 줄이 `<라벨> (<장식>): <요지>` 이고 이어서 줄 머리 슬롯 넷(대상·본문·제안·해소)이 온다.
# 라벨 일곱과 장식 셋의 표기 원천은 Conventional Comments 이고 해소 셋은 결정이 정했다 — 셋 다 닫힌 어휘다.
# **게이트 효과는 하나뿐이다.** `issue (blocking)` 이면서 `해소: 열림` 인 주석이 있으면 게이트가 막는다. 그 밖의 조합은
# 기록이고 막지 않는다. 형식(첫 줄 꼴·닫힌 어휘·본문 문장 상한)은 shape(review-comment-body-shapes.ttl)가 보고,
# 이 한 조건만 chunk_lint 가 본다 — 판정 도구는 해소 상태의 존재만 보고 이유의 내용을 보지 않는다 (p5-verification-tools-per-plane).
# 값 어휘의 정의처는 여기다. chunk2kg 는 rdflib 없이 타깃마다 돌므로 같은 문자열을 getattr 폴백으로 갖는다 (LINK_STATE_* 와 같은 형태)
COMMENT_LABELS = ("praise", "nitpick", "suggestion", "issue", "question", "thought", "chore")
COMMENT_DECORATIONS = ("blocking", "non-blocking", "if-minor")
COMMENT_RESOLUTIONS = ("열림", "해소", "기각")
COMMENT_SLOTS = ("대상", "본문", "제안", "해소")  # 줄 머리 `키워드: 값` 슬롯 — chunk2kg.BODY_SLOT_KEYWORDS 가 표지로 읽는다
COMMENT_OPEN = COMMENT_RESOLUTIONS[0]            # 아직 해소되지 않은 상태
COMMENT_BLOCKING = (COMMENT_LABELS[3], COMMENT_DECORATIONS[0])  # 막는 (라벨, 장식) 쌍 — issue (blocking)
COMMENT_MAX_SENTENCES = 4                        # 본문 슬롯의 문장 상한 — shape 의 sh:maxInclusive 와 같은 값
```
<!-- 인용 끝 -->
