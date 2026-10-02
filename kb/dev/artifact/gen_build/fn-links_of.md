---
id: https://agentic-knowledge-base.dev/id/chunk/e284beaa-0477-4715-ba21-44028b13bf3f
type: artifact
level: executable
title_ko: 함수 links_of (tools/gen_build.py)
title: function links_of in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/04bfcfb9-d96b-42ec-9555-a58bd09f1551]
part_of: https://agentic-knowledge-base.dev/id/composite/569c6e75-e264-4981-bf0b-bba156b541c8
---
**함수** — `links_of(meta, iri_to_label, where)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def links_of(meta, iri_to_label, where):
    out = {}
    for key in LINKS:
        labs = []
        for iri in meta.get(key, []) or []:
            if iri not in iri_to_label:
                raise GenBuildError(f"{where}: {key} 대상 {iri} 가 타깃이 아니다 — 끊긴 링크 (참조 무결성)")
            labs.append(iri_to_label[iri])
        if labs:
            out[key] = labs
    return out
```
<!-- 인용 끝 -->
