---
id: https://agentic-knowledge-base.dev/id/chunk/6fd0167b-9fe9-4a4f-96c0-08a4efc53eda
type: artifact
level: executable
title_ko: 함수 previous_query_hashes (tools/extract.py)
title: function previous_query_hashes in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/5fef9048-0948-4bfe-ad98-9a6587163b44, https://agentic-knowledge-base.dev/id/chunk/8f365d81-2dc9-4f87-8f66-153ed897e871]
part_of: https://agentic-knowledge-base.dev/id/composite/ffce8a39-526e-459a-af7d-ed5cb6800166
---
**함수** — `previous_query_hashes(pkg_dir)` 다. 트리에 있는 질의 청크 → {정규화 해시: 한정 이름}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def previous_query_hashes(pkg_dir: Path) -> dict[str, str]:
    """트리에 있는 질의 청크 → {정규화 해시: 한정 이름}. `previous_hashes` 의 질의판이다 — 펜스 언어만 다르다."""
    out = {}
    for f in sorted(pkg_dir.glob("*.md")) if pkg_dir.is_dir() else []:
        code = re.findall(r"^```" + QUERY_LANG + r"\n(.*?)^```$", f.read_text(encoding="utf-8"), re.M | re.S)
        if code:
            out[normalized_hash(code[0].splitlines(), f.stem)] = qualified("query", f.stem)
    return out
```
<!-- 인용 끝 -->
