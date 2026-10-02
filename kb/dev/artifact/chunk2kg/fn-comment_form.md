---
id: https://agentic-knowledge-base.dev/id/chunk/41b351ab-939c-41ad-ab8f-bf2396bb0114
type: artifact
level: executable
title_ko: 함수 comment_form (tools/chunk2kg.py)
title: function comment_form in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/a3fa56bc-c50d-4d10-98ed-d101ae5102ce]
part_of: https://agentic-knowledge-base.dev/id/composite/992d5e5a-5efc-4108-a5c8-1e75dd96807a
---
**함수** — `comment_form(body)` 다. 주석 본문 → {label, decoration, gist, resolution, sentences, targets} (찾은 것만) — 결정 p7-commentary-form.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def comment_form(body: list[str]) -> dict:
    """주석 본문 → {label, decoration, gist, resolution, sentences, targets} (찾은 것만) — 결정 p7-commentary-form.

    첫 산문 줄이 `<라벨> (<장식>): <요지>` 이고 이어서 줄 머리 슬롯이 온다. 없는 것은 넣지 않는다 — 방출이 비면
    shape(review-comment-body-shapes.ttl)의 sh:minCount 가 무엇이 빠졌는지 말한다. 여기서 형식을 두 번 판정하지 않는다.
    """
    form: dict = {}
    slots: dict[str, list[str]] = {}
    cur = None
    for line in body:
        s = line.strip()
        if not s:
            continue
        if not form and (m := COMMENT_HEAD.match(s)):
            form.update(label=m.group(1), decoration=m.group(2), gist=m.group(3))
            continue
        if m := COMMENT_SLOT_HEAD.match(s):
            cur = m.group(1)
            slots.setdefault(cur, []).append(m.group(2))
            continue
        if cur:
            slots[cur].append(s)
    if "본문" in slots:
        form["sentences"] = count_sentences(" ".join(slots["본문"]))
    if "대상" in slots:
        form["targets"] = COMMENT_IRI.findall(" ".join(slots["대상"]))
    if "해소" in slots and (m := COMMENT_RESOLUTION.match(" ".join(slots["해소"]).strip())):
        form["resolution"] = m.group(1)
    return form
```
<!-- 인용 끝 -->
