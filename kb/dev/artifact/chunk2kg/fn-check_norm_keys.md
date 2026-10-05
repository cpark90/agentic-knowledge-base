---
id: https://agentic-knowledge-base.dev/id/chunk/0771e060-41a6-434b-bb56-61bcf3e3b7ec
type: artifact
level: executable
title_ko: 함수 check_norm_keys (tools/chunk2kg.py)
title: function check_norm_keys in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/4eb70032-9c6d-47dc-a0b0-34e02f426e80, https://agentic-knowledge-base.dev/id/chunk/cc796185-bb2d-4940-a069-48a9334eecc8]
part_of: https://agentic-knowledge-base.dev/id/composite/679fc45f-a074-446c-aa6b-755cb0329d4f
---
**함수** — `check_norm_keys(path, meta)` 다. 절 키의 형식 — plane 제한과 값의 꼴.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_norm_keys(path: str, meta: dict) -> None:
    """절 키의 형식 — plane 제한과 값의 꼴. 머리 청크·절 청크의 구분(선언 여부)은 묶음 전체를 아는 main 이 본다."""
    keys = [k for k in NORM_SECTION_KEYS + NORM_HEAD_KEYS if k in meta]
    if meta["type"] != NORM_TYPE:
        if keys:
            raise ValueError(f"{path}: {', '.join(keys)} 는 type: {NORM_TYPE} 에서만 쓴다 — 실제 type {meta['type']!r} "
                             f"(절 키, p12-norm-documents-from-section-chunks)")
        return
    if NORM_HEADING_KEY in meta:
        h = meta[NORM_HEADING_KEY]
        if not isinstance(h, str) or not h.strip():
            raise ValueError(f"{path}: {NORM_HEADING_KEY} 는 비지 않은 절 제목 문자열이다")
        if NORM_HEADING_NUMBERED.match(h.strip()):
            raise ValueError(f"{path}: {NORM_HEADING_KEY} {h!r} 에 번호가 있다 — 절 번호는 생성기가 순서로 붙이고 소스에 두지 않는다")
    if NORM_DEPTH_KEY in meta and meta[NORM_DEPTH_KEY] not in NORM_DEPTHS:
        raise ValueError(f"{path}: {NORM_DEPTH_KEY} 는 {' 또는 '.join(NORM_DEPTHS)} 이다 — 실제 {meta[NORM_DEPTH_KEY]!r}")
    if NORM_NUMBERED_KEY in meta:
        if meta[NORM_NUMBERED_KEY] not in NORM_NUMBERED_VALUES:
            raise ValueError(f"{path}: {NORM_NUMBERED_KEY} 는 {' | '.join(NORM_NUMBERED_VALUES)} 중 하나다(기본 true) — "
                             f"실제 {meta[NORM_NUMBERED_KEY]!r}")
        if meta.get(NORM_DEPTH_KEY) != "2":
            raise ValueError(f"{path}: {NORM_NUMBERED_KEY} 는 depth 2 절에서만 쓴다 — 번호는 depth 2 절에만 붙는다 "
                             f"(실제 depth {meta.get(NORM_DEPTH_KEY)!r})")
    if NORM_ITEMS_KEY in meta:
        meta["_norm_items"] = parse_norm_items(path, meta[NORM_ITEMS_KEY])
    check_norm_bundle_form(path, meta)
    if NORM_NUMBERING_KEY in meta and not NORM_NUMBERING.match(str(meta[NORM_NUMBERING_KEY])):
        raise ValueError(f"{path}: {NORM_NUMBERING_KEY} 는 첫 절 번호의 꼴(`§0.` · `1.` · `0.`)이다 — 실제 {meta[NORM_NUMBERING_KEY]!r}")
    if NORM_STRENGTH_KEY in meta and meta[NORM_STRENGTH_KEY] not in NORM_STRENGTHS:
        raise ValueError(f"{path}: {NORM_STRENGTH_KEY} 는 {' | '.join(NORM_STRENGTHS)} 중 하나다 — 실제 {meta[NORM_STRENGTH_KEY]!r}")
```
<!-- 인용 끝 -->
