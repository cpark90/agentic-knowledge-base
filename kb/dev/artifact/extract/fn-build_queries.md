---
id: https://agentic-knowledge-base.dev/id/chunk/bea10200-8d45-4fa2-9999-bda8c1935253
type: artifact
level: executable
title_ko: 함수 build_queries (tools/extract.py)
title: function build_queries in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2734434f-58d6-4d30-884c-b79d2c51061b, https://agentic-knowledge-base.dev/id/chunk/8961c276-af1a-4b25-82aa-8ea7a53a20d0, https://agentic-knowledge-base.dev/id/chunk/cea6fcfc-b3e0-4dab-b8f5-e0727ee9c70d]
part_of: https://agentic-knowledge-base.dev/id/composite/ffce8a39-526e-459a-af7d-ed5cb6800166
---
**함수** — `build_queries(src_rel, texts, ids, reg)` 다. 질의 청크들 — 파일 전체가 인용 하나이고 링크는 청크마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def build_queries(src_rel: str, texts: dict[str, list[str]], ids, reg: dict) -> list[Chunk]:
    """질의 청크들 — 파일 전체가 인용 하나이고 링크는 청크마다 붙는다. 질의 파일이 곧 링크의 자리다."""
    per_query = reg.get(QUERY_REFINES_KEY) or {}
    unknown = sorted(set(per_query) - set(texts))
    if unknown:
        raise ExtractError(f"{src_rel}: 등록부 `{QUERY_REFINES_KEY}` 의 키 {', '.join(unknown)} 가 디렉토리의 질의가 아니다 — "
                           f"키는 `query:<질의 파일 stem>` 이다")
    out = []
    for q, lines in texts.items():
        stem = q.split(":", 1)[1]
        body = [f"**질의** — `{src_rel}/{stem}{kb_lib.EXTRACT_QUERY_SUFFIX}` 다. {len(lines)}줄이고 이 청크는 추출 생성물이다. "
                f"질의 파일 하나가 청크 하나이므로 링크와 가정의 자리가 이 청크다.", ""] + quote(lines, QUERY_LANG)
        c = Chunk(f"{stem}.md", q, ids.get(q, CHUNK_IRI), f"질의 {stem} ({src_rel})", f"query {stem} in {src_rel}", body)
        c.links = {"refines": list(dict.fromkeys(reg["refines"] + per_query.get(q, []))), "serves": reg["serves"]}
        out.append(c)
    return out
```
<!-- 인용 끝 -->
