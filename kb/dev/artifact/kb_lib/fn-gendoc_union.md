---
id: https://agentic-knowledge-base.dev/id/chunk/63c8b052-77ba-4c50-bc59-9b1fea9e598d
type: artifact
level: executable
title_ko: 함수 gendoc_union (tools/kb_lib.py)
title: function gendoc_union in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
uses: [https://agentic-knowledge-base.dev/id/chunk/dcdad310-25df-4a9e-8939-6ef8be6f1e20]
part_of: https://agentic-knowledge-base.dev/id/composite/ad8f9fc0-eedf-44e1-a93f-65f667e359ce
---
**함수** — `gendoc_union(paths)` 다. 머리 블록의 규모 자리에 붙는 union 구성 — `union: chunks·base·…` 꼴.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def gendoc_union(paths) -> str:
    """머리 블록의 규모 자리에 붙는 union 구성 — `union: chunks·base·…` 꼴. 그래프 파일(`.ttl`)만 센다."""
    names = [gendoc_input_name(p) for p in paths]
    graphs = [n for n in names if n.endswith(".ttl")]
    labels, matched = [], set()
    for frag, label in GENDOC_UNION_MEMBERS:
        hit = [n for n in graphs if frag in n]
        if hit:
            labels.append(label)
            matched.update(hit)
    labels += sorted({n.rsplit("/", 1)[-1][:-4] for n in graphs if n not in matched})
    return "union: " + ("\u00b7".join(labels) if labels else NONE_MARK)
```
<!-- 인용 끝 -->
