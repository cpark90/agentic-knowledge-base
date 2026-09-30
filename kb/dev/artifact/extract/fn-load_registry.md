---
id: https://agentic-knowledge-base.dev/id/chunk/4333655e-49b9-4be9-b2f1-8c28243d8390
type: artifact
level: executable
title_ko: 함수 load_registry (tools/extract.py)
title: function load_registry in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T07:35:51Z}
part_of: https://agentic-knowledge-base.dev/id/composite/094c3193-2fdb-4341-b151-9ecda0fefd53
---
**함수** — `load_registry(path)` 다. 등록부 → {source, resource, package, at, source_hash, refines[], serves[], ids{}}.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_registry(path: Path) -> dict:
    """등록부 → {source, resource, package, at, source_hash, refines[], serves[], ids{}}. 없으면 빈 등록부다."""
    reg = {"source": "", "resource": "", "package": "", "at": "", "source_hash": "",
           "refines": [], "serves": [], kb_lib.STAMP_KEY: {}, "ids": {}}
    if not path.exists():
        return reg
    section = ""
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].rstrip() if raw.lstrip().startswith("#") else raw.rstrip()
        if not line.strip():
            continue
        if line.startswith("  "):
            body = line.strip()
            if section in ("refines", "serves"):
                reg[section].append(body.lstrip("- ").strip())
            elif section in ("ids", kb_lib.STAMP_KEY):  # 한정 이름에 `:` 가 있으므로 마지막 `: ` 에서 가른다 — IRI 에는 `: ` 가 없다
                k, sep, v = body.rpartition(": ")
                if sep:
                    reg[section][k.strip()] = v.strip()
            continue
        key, _, val = line.partition(":")
        key, val = key.strip(), val.strip()
        section = key if key in ("refines", "serves", "ids", kb_lib.STAMP_KEY) else ""
        if key in reg and not section:
            reg[key] = val
    return reg
```
<!-- 인용 끝 -->
