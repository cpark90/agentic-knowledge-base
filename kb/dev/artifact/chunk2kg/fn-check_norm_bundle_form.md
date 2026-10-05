---
id: https://agentic-knowledge-base.dev/id/chunk/cc796185-bb2d-4940-a069-48a9334eecc8
type: artifact
level: executable
title_ko: 함수 check_norm_bundle_form (tools/chunk2kg.py)
title: function check_norm_bundle_form in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/679fc45f-a074-446c-aa6b-755cb0329d4f
---
**함수** — `check_norm_bundle_form(path, meta)` 다. 묶음의 꼴(form·columns·link_column)과 이어짐(continues)의 형식 — 한 청크 안에서 판정되는 것만 본다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_norm_bundle_form(path: str, meta: dict) -> None:
    """묶음의 꼴(form·columns·link_column)과 이어짐(continues)의 형식 — 한 청크 안에서 판정되는 것만 본다.

    칸 수·표 줄의 강도·첫 절의 이어짐은 결정의 줄과 문서의 순서를 아는 생성기(tools/gen_norms.py)가 판정한다.
    """
    if NORM_CONTINUES_KEY in meta:
        if meta[NORM_CONTINUES_KEY] not in NORM_CONTINUES_VALUES:
            raise ValueError(f"{path}: {NORM_CONTINUES_KEY} 는 {' | '.join(NORM_CONTINUES_VALUES)} 중 하나다(기본 false) — "
                             f"실제 {meta[NORM_CONTINUES_KEY]!r}")
        if meta[NORM_CONTINUES_KEY] == "true":
            have = [k for k in (NORM_HEADING_KEY, NORM_DEPTH_KEY, NORM_NUMBERED_KEY) if k in meta]
            if have:
                raise ValueError(f"{path}: 이어짐 절 청크({NORM_CONTINUES_KEY}: true)는 {', '.join(have)} 를 갖지 않는다 — "
                                 f"제목이 없고 깊이는 앞 절을 잇는다")
    form = meta.get(NORM_FORM_KEY, NORM_FORM_DEFAULT)
    if form not in NORM_FORMS:
        raise ValueError(f"{path}: {NORM_FORM_KEY} 는 {' | '.join(NORM_FORMS)} 중 하나다(기본 {NORM_FORM_DEFAULT}) — 실제 {form!r}")
    if NORM_FORM_KEY in meta and NORM_ITEMS_KEY not in meta:
        raise ValueError(f"{path}: {NORM_FORM_KEY} 는 {NORM_ITEMS_KEY} 가 있는 절에서만 쓴다 — 꼴은 항목 묶음의 꼴이다")
    cols = meta.get(NORM_COLUMNS_KEY)
    if form != NORM_FORM_TABLE:
        bad = [k for k in (NORM_COLUMNS_KEY, NORM_LINK_COLUMN_KEY) if k in meta]
        if bad:
            raise ValueError(f"{path}: {', '.join(bad)} 는 {NORM_FORM_KEY}: {NORM_FORM_TABLE} 에서만 쓴다 — 실제 {NORM_FORM_KEY} {form!r}")
        return
    if not isinstance(cols, list) or not cols or not all(isinstance(c, str) and c.strip() for c in cols) \
            or len(set(cols)) != len(cols) or any("|" in c for c in cols):
        raise ValueError(f"{path}: {NORM_FORM_KEY}: {NORM_FORM_TABLE} 는 {NORM_COLUMNS_KEY}: [열 머리, …] 를 갖는다 — 비지 않고 서로 "
                         f"다르며 `|` 가 없는 문자열의 목록이다. 실제 {cols!r}")
    if NORM_LINK_COLUMN_KEY in meta:
        if meta[NORM_LINK_COLUMN_KEY] != cols[-1]:
            raise ValueError(f"{path}: {NORM_LINK_COLUMN_KEY} {meta[NORM_LINK_COLUMN_KEY]!r} 는 {NORM_COLUMNS_KEY} 의 마지막 원소 "
                             f"{cols[-1]!r} 여야 한다 — 링크 열은 표의 끝 열이다")
        if len(cols) < 2:
            raise ValueError(f"{path}: {NORM_LINK_COLUMN_KEY} 를 둔 표는 링크 열 밖의 열을 하나 이상 갖는다 — 실제 {cols!r}")
    for it in meta.get("_norm_items") or []:
        if it["sub"]:
            raise ValueError(f"{path}: 표 절({NORM_FORM_KEY}: {NORM_FORM_TABLE})의 항목은 하위를 갖지 않는다 — 행 하나가 줄 하나다")
```
<!-- 인용 끝 -->
