---
id: https://agentic-knowledge-base.dev/id/chunk/e1b40b31-0dc4-45a2-b4a1-345ee72df9df
type: artifact
level: executable
title_ko: 함수 norm_conventions (tools/gen_build.py)
title: function norm_conventions in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/04bfcfb9-d96b-42ec-9555-a58bd09f1551]
part_of: https://agentic-knowledge-base.dev/id/composite/6400a2c9-ed32-428b-bd76-5952553e5e04
---
**함수** — `norm_conventions(lab, it, decisions)` 다. 절 청크 묶음의 `items` 가 줄을 싣는 결정 slug → 결정 복합체 IRI.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def norm_conventions(lab, it, decisions) -> dict:
    """절 청크 묶음의 `items` 가 줄을 싣는 결정 slug → 결정 복합체 IRI. 결정 디렉토리가 없으면 GenBuildError 다.

    링크만 하는 결정(`slug#k + slug2` 의 둘째)은 agt:projectsConvention 의 대상이 아니라 여기 넣지 않는다 — 그 실재는
    생성기 gen_norms 가 본다. `decisions` 는 결정 디렉토리 이름 → 결정 복합체 IRI 다.
    """
    out = {}
    for m in it["metas"]:
        for slug in norm_item_slugs(m.get("_norm_items") or [], links=False):
            if slug not in decisions:
                raise GenBuildError(f"{it['pkg']}/{Path(m.get('_path', lab)).name}: items 가 가리키는 결정 {slug!r} 가 "
                                    f"kb/dev/decision/ 에 없다 — slug 는 결정 디렉토리 이름이다 (p12-norm-documents-from-section-chunks)")
            out[slug] = decisions[slug]
    return out
```
<!-- 인용 끝 -->
