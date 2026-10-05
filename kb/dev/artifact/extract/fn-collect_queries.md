---
id: https://agentic-knowledge-base.dev/id/chunk/c60ce666-a684-4dc4-8022-ed23dbd14935
type: artifact
level: executable
title_ko: 함수 collect_queries (tools/extract.py)
title: function collect_queries in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/2734434f-58d6-4d30-884c-b79d2c51061b, https://agentic-knowledge-base.dev/id/chunk/5fef9048-0948-4bfe-ad98-9a6587163b44, https://agentic-knowledge-base.dev/id/chunk/8f365d81-2dc9-4f87-8f66-153ed897e871]
part_of: https://agentic-knowledge-base.dev/id/composite/ffce8a39-526e-459a-af7d-ed5cb6800166
---
**함수** — `collect_queries(src)` 다. 질의 디렉토리 → (한정 이름들, 정규화 해시, 이름 → 줄들).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def collect_queries(src: Path) -> tuple[list[str], dict[str, str], dict[str, list[str]]]:
    """질의 디렉토리 → (한정 이름들, 정규화 해시, 이름 → 줄들). 한정 이름은 `query:<stem>` 이고 해시는 개명 판정의 입력이다."""
    names, hashes, texts = [], {}, {}
    for f in sorted(src.glob("*" + kb_lib.EXTRACT_QUERY_SUFFIX)):
        q = qualified("query", f.stem)
        texts[q] = f.read_text(encoding="utf-8").splitlines()
        names.append(q)
        hashes[q] = normalized_hash(texts[q], f.stem)
    if not names:
        raise ExtractError(f"{src}: 질의 파일(*{kb_lib.EXTRACT_QUERY_SUFFIX})이 없다 — 빈 질의 디렉토리는 추출 대상이 아니다. "
                           f"EXTRACTED_QUERY_DIRS(defs/kb.bzl)에서 이름을 지운다")
    return names, hashes, texts
```
<!-- 인용 끝 -->
