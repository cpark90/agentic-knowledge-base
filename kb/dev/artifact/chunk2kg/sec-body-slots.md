---
id: https://agentic-knowledge-base.dev/id/chunk/1fbf627e-a9f9-445e-aab2-a4206bdf72ee
type: artifact
level: executable
title_ko: 절 body-slots (tools/chunk2kg.py)
title: section body-slots in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/ab66f02d-6126-4507-b73a-c29429769f11, https://agentic-knowledge-base.dev/id/chunk/01f6a247-ed75-405f-b286-3d59b8acc9d2, https://agentic-knowledge-base.dev/id/chunk/28655d6b-d000-4f43-8d68-9e0ce042c39c]
part_of: https://agentic-knowledge-base.dev/id/composite/992d5e5a-5efc-4108-a5c8-1e75dd96807a
composite: {id: https://agentic-knowledge-base.dev/id/composite/992d5e5a-5efc-4108-a5c8-1e75dd96807a, title_ko: 절 복합체 body-slots (tools/chunk2kg.py), title: section composite body-slots in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/1fbf627e-a9f9-445e-aab2-a4206bdf72ee, https://agentic-knowledge-base.dev/id/chunk/848f96db-27ef-4fda-84af-e59077e7dc0c, https://agentic-knowledge-base.dev/id/chunk/b7ffd04b-bbcb-41aa-a69d-0b651364d2db, https://agentic-knowledge-base.dev/id/chunk/a3fa56bc-c50d-4d10-98ed-d101ae5102ce, https://agentic-knowledge-base.dev/id/chunk/41b351ab-939c-41ad-ab8f-bf2396bb0114], part_of: https://agentic-knowledge-base.dev/id/composite/f7d6eec7-bef4-4e94-ac55-36e7dda654ce}
---
**절** — `tools/chunk2kg.py` 의 절 `body-slots` 다. 본문 슬롯과 논평 형식

**정의** — `body_slots` · `_alt` · `count_sentences` · `comment_form` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 본문 슬롯과 논평 형식 ────────────────────





COMMENT_HEAD = re.compile(r"^(" + _alt(COMMENT_LABELS) + r")\s*\((" + _alt(COMMENT_DECORATIONS) + r")\)\s*:\s*(\S.*)$")
COMMENT_RESOLUTION = re.compile(r"^(" + _alt(COMMENT_RESOLUTIONS) + r")(?=$|[\s—.,])")  # 해소 슬롯의 첫 낱말 — 뒤는 한 줄 이유다
COMMENT_SLOT_HEAD = re.compile(r"^(" + _alt(COMMENT_SLOTS) + r")\s*:\s*(.*)$")
COMMENT_IRI = re.compile(r"https?://\S+?(?=[\s,)\]`]|$)")
COMMENT_CODE_SPAN = re.compile(r"`[^`]*`")
COMMENT_SENTENCE_END = re.compile(r"[.!?](?=\s|$)")  # 문장 끝 — 코드 스팬·IRI 를 지운 뒤 센다 (`4.1절` 의 마침표는 세지 않는다)
```
<!-- 인용 끝 -->
