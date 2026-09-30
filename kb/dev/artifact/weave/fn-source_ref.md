---
id: https://agentic-knowledge-base.dev/id/chunk/4b9d03d4-f126-455e-9e3d-533c84b76f26
type: artifact
level: executable
title_ko: 함수 source_ref (tools/weave.py)
title: function source_ref in tools/weave.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-weave}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/ec24ef39-7e27-4fff-bba3-6fdb1829b342
---
**함수** — `source_ref(m, s)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def source_ref(m: Model, s) -> str:
    loc = next(m.g.objects(s, PROV.atLocation), None)
    return f"{m.ko(s)} (`{kb_lib.compact_iri(str(s))}`" + (f", `{loc}`)" if loc else ")")
```
<!-- 인용 끝 -->
