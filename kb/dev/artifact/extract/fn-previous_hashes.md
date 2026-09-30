---
id: https://agentic-knowledge-base.dev/id/chunk/66148879-b856-4716-aa7c-9e2273143711
type: artifact
level: executable
title_ko: 함수 previous_hashes (tools/extract.py)
title: function previous_hashes in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
part_of: https://agentic-knowledge-base.dev/id/composite/afe5a31d-455c-4ff6-8986-80ad97804df0
---
**함수** — `previous_hashes(pkg_dir)` 다. 트리에 있는 생성 청크 → {정규화 해시: 한정 이름}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def previous_hashes(pkg_dir: Path) -> dict[str, str]:
    """트리에 있는 생성 청크 → {정규화 해시: 한정 이름}. 개명은 이름을 뺀 본문이 같은 것으로 판정한다."""
    out = {}
    for f in sorted(pkg_dir.glob("*.md")):
        stem = f.stem
        if not stem.startswith(("fn-", "cls-", "sec-", "ch-")):
            continue
        qname = stem.replace("-", ":", 1)
        text = f.read_text(encoding="utf-8")
        code = re.findall(r"^```python\n(.*?)^```$", text, re.M | re.S)
        if code:
            out[normalized_hash(trim(code[0].splitlines()), qname.split(":", 1)[1])] = qname
    return out
```
<!-- 인용 끝 -->
