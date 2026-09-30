---
id: https://agentic-knowledge-base.dev/id/chunk/0fa7a40a-c96a-4ddd-956f-2d07695d77a4
type: artifact
level: executable
title_ko: 함수 evidence (tools/choices.py)
title: function evidence in tools/choices.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-choices}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T16:38:13Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/6c9da832-fd4f-4fba-a0f6-33561303de46
---
**함수** — `evidence(g, link, polarity)` 다. 링크의 증거 기록 중 극성이 맞는 것 — "<종류 라벨> `<참조>`" 목록.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def evidence(g: Graph, link, polarity: str) -> list[str]:
    """링크의 증거 기록 중 극성이 맞는 것 — "<종류 라벨> `<참조>`" 목록."""
    out = []
    for e in sorted(g.objects(link, AGT.hasEvidence), key=str):
        if str(next(g.objects(e, AGT.polarity), "")) != polarity:
            continue
        kind = next(g.objects(e, AGT.evidenceKind), None)
        ref = next(g.objects(e, AGT.evidenceRef), None)
        label = kb_lib.label_of(g, kind, "ko") if kind is not None else kb_lib.NONE_MARK
        out.append(f"{label} `{kb_lib.compact_iri(str(ref))}`" if ref is not None else label)
    return sorted(out)
```
<!-- 인용 끝 -->
