---
id: https://agentic-knowledge-base.dev/id/chunk/a83e5a5d-15ff-4e18-80b5-2c88dead1cfc
type: artifact
level: executable
title_ko: 함수 dump_registry (tools/extract.py)
title: function dump_registry in tools/extract.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/094c3193-2fdb-4341-b151-9ecda0fefd53
---
**함수** — `dump_registry(reg)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def dump_registry(reg: dict) -> str:
    out = [REGISTRY_HEAD.format(package=reg["package"])]
    for k in ("source", "resource", "package", kb_lib.LAYER_KEY, "at", "source_hash"):
        out.append(f"{k}: {reg[k]}")
    for k in ("refines", "serves"):
        out.append(f"{k}:" + ("" if reg[k] else " []"))
        out += [f"  - {v}" for v in reg[k]]
    tested = reg.get(kb_lib.STAMP_KEY) or {}
    out.append(f"{kb_lib.STAMP_KEY}:" + ("" if tested else " {}"))
    out += [f"  {k}: {tested[k]}" for k in ("rev", "at", "source_hash") if tested.get(k)]
    out.append("ids:")
    out += [f"  {k}: {reg['ids'][k]}" for k in sorted(reg["ids"])]
    return "\n".join(out) + "\n"
```
<!-- 인용 끝 -->
