---
id: https://agentic-knowledge-base.dev/id/chunk/ee10ae76-e59e-44e2-87ad-d798ab4c0311
type: artifact
level: executable
title_ko: 함수 tombstones (tools/chunk2kg.py)
title: function tombstones in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/583a95ea-746e-4243-a6d9-108c18a3c9d8]
part_of: https://agentic-knowledge-base.dev/id/composite/7efb5476-c231-4b0e-9e6c-a2389a12409e
---
**함수** — `tombstones(path, meta)` 다. frontmatter `sources` 의 묘비 선언 → [{id, title_ko, title, location}].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def tombstones(path: str, meta: dict) -> list:
    """frontmatter `sources` 의 묘비 선언 → [{id, title_ko, title, location}]. 선언의 형식 위반은 ValueError 다.

    선언은 resource 가 git 영구 위치이고 id 가 있는 항목이다. 라벨 둘은 필수이고 한/영 규칙(0.6절)은 단위 지식 라벨과 같다.
    id 는 이 항목의 링크 키 대상이어야 한다 — 묘비는 대체 링크의 끝점을 지키는 자리이므로 아무도 가리키지 않는 묘비는 만들지 않는다.
    """
    out = []
    for d in meta.get("sources", []) or []:
        if not (isinstance(d, dict) and d.get("id") and GIT_PERMALINK.match(d.get("resource", ""))):
            continue
        iri, ko, en = d["id"], d.get("title_ko", ""), d.get("title", "")
        if not ko or not en:
            raise ValueError(f"{path}: 묘비 선언 {iri} 에 title_ko·title 이 없다 — 지운 항목의 옛 라벨 둘을 적는다 (Q-0061#Q146)")
        if HANGUL.search(en) or not HANGUL.search(ko):
            raise ValueError(f"{path}: 묘비 선언 {iri} 의 라벨이 한/영 규칙을 어긴다 — title {en!r} · title_ko {ko!r} (0.6절)")
        if iri not in link_targets(meta):
            raise ValueError(f"{path}: 묘비 선언 {iri} 가 이 항목의 링크 대상이 아니다 — 묘비는 대체 링크의 끝점을 지키는 자리다. "
                             f"supersedes 에 그 IRI 를 적는다 (Q-0061#Q146)")
        out.append({"id": iri, "title_ko": ko, "title": en, "location": d["resource"]})
    return out
```
<!-- 인용 끝 -->
