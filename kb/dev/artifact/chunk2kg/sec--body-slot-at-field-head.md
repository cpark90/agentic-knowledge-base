---
id: https://agentic-knowledge-base.dev/id/chunk/5adbc7c4-4ac0-47f2-abf4-51a6e0cb3291
type: artifact
level: executable
title_ko: 절 -body-slot-at-field-head (tools/chunk2kg.py)
title: section -body-slot-at-field-head in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d2327845-e19c-432e-bef7-b5d429601fb6
composite: {id: https://agentic-knowledge-base.dev/id/composite/d2327845-e19c-432e-bef7-b5d429601fb6, title_ko: 절 복합체 -body-slot-at-field-head (tools/chunk2kg.py), title: section composite -body-slot-at-field-head in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/5adbc7c4-4ac0-47f2-abf4-51a6e0cb3291, https://agentic-knowledge-base.dev/id/chunk/a88529ad-7941-47a8-a7ae-eb1866d89efc], part_of: https://agentic-knowledge-base.dev/id/composite/28e52252-d603-4c96-b7ee-f85197b0d7da}
---
**절** — `tools/chunk2kg.py` 의 절 `-body-slot-at-field-head` 다. 본문 슬롯 표지의 자리

**정의** — `_body_slot_at_field_head` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 본문 슬롯 표지의 자리 ────────────────────

# 줄 머리 `키워드: 값` 형 슬롯 (제안 4.1절). 선택 슬롯 `미확정:` 은 미결을 문서가 아니라 항목 안에 두어 집계를 생성물로
# 만든다 (p4-three-empty-values) — //kg:open 이 이 표지로 미결을 모은다. 줄 `규약:` 은 결정의 선택 넷째 청크 `conventions.md`
# 가 규범 문서에 싣는 문장 하나다 (p4-convention-slot, 유저 답 Q13-a·Q22-b) — 그 청크 한정은 convention-slot-shapes 가 본다.
# 같은 청크의 역할 표지 `**규약**` 도 같은 값 "규약" 으로 나간다(BODY_SLOT_MARKERS). 줄 `규약:` 은 목록 항목이 아니라 슬롯이다.
# 나머지 넷은 주석의 슬롯이다 (p7-commentary-form).
# 첫 줄 `<라벨> (<장식>): <요지>` 는 표지가 아니라 형식 검사 대상이라 여기 없다 — comment_form 이 읽는다.
# **표지를 늘리면 shape(kb/ontology/shapes/*-body-shapes.ttl)의 틀도 같은 커밋에서 늘린다** — 표지만 늘리면 방출은
# 바뀌는데 강제하는 곳이 없어 틀이 거짓이 된다
BODY_SLOT_KEYWORDS = ("미확정", "규약", *COMMENT_SLOTS)
BODY_SLOT_KEYWORD = re.compile(r"^(" + "|".join(BODY_SLOT_KEYWORDS) + r"):\s")
BODY_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")  # 코드 펜스 안은 본문 형식이 아니다 — 예시 안의 표지를 슬롯으로 읽지 않는다
```
<!-- 인용 끝 -->
