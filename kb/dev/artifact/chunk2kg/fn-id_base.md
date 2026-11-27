---
id: https://agentic-knowledge-base.dev/id/chunk/16348364-cc1d-4c34-9b3f-ca27ea8e9ad4
type: artifact
level: executable
title_ko: 함수 id_base (tools/chunk2kg.py)
title: function id_base in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/094f7e14-ed5b-4c40-83f8-782d9f4161b0
---
**함수** — `id_base()` 다. 단위 지식 IRI 이름공간 — `KB_ID_BASE` 가 비었으면 `ID_BASE_DEFAULT` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def id_base() -> str:
    """단위 지식 IRI 이름공간 — `KB_ID_BASE` 가 비었으면 `ID_BASE_DEFAULT` 다. `/` 로 끝나는 http(s) IRI 가 아니면 ValueError 다."""
    v = os.environ.get(ID_BASE_ENV, "").strip()
    if not v:
        return ID_BASE_DEFAULT
    if not re.fullmatch(r"https?://[^\s<>\"{}|\\^`]+/", v):
        raise ValueError(f"{ID_BASE_ENV}={v!r}: 단위 지식 IRI 이름공간은 `/` 로 끝나는 http(s) IRI 여야 한다")
    return v
```
<!-- 인용 끝 -->
