---
id: https://agentic-knowledge-base.dev/id/chunk/53335074-67d7-45c8-b564-78065ea96eb8
type: artifact
level: executable
title_ko: 함수 emit_chunk (tools/chunk2kg.py)
title: function emit_chunk in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/094f7e14-ed5b-4c40-83f8-782d9f4161b0
---
**함수** — `emit_chunk(path, meta, line_count)` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def emit_chunk(path: str, meta: dict, line_count: int) -> str:
    stmts = [
        f"a {PLANE_CLASS[meta['type']]} , {PROFILE_SUBSTANCE[meta['type']]}",
        f'rdfs:label "{esc(meta["title"])}"@en',
        f'rdfs:label "{esc(meta["title_ko"])}"@ko',
        f"agt:hasLevel agt:{meta['level']}",
    ]
    if "pattern" in meta:
        stmts.append(f"agt:pattern {EARS_PATTERNS[meta['pattern']]}")
    stmts += [
        f"agt:lineCount {line_count}",
        *(f'agt:bodySlot "{esc(s)}"' for s in meta.get("_body_slots", [])),  # 본문 형태 — 틀의 필수 슬롯은 *-body-shapes.ttl 이 본다
        f'agt:status "{meta["status"]}"',
        f'agt:contentHash "{meta["_content_hash"]}"',
        f'agt:generatedBy "{esc(meta["generated"]["by"])}"',
        f'prov:generatedAtTime "{meta["generated"]["at"]}"^^xsd:dateTime',
        f'agt:assertionLocation "{esc(path)}"',
    ]
    for a in meta.get("assumes", []):
        stmts.append(f"agt:assumes <{a}>")
    for d in meta.get("sources", []):
        res = d.get("resource") if isinstance(d, dict) else d  # OKF: 객체 목록. 옛 문자열 목록도 읽는다
        if not res:
            raise ValueError(f"{path}: sources 항목에 resource 가 없다 (OKF v0.2 §5.1)")
        stmts.append(f"prov:wasDerivedFrom <{res}>")
    if SPECIALIZATION_KEY in meta:  # 같은 것의 다른 입도 — 출처(wasDerivedFrom)와 다르다 (p10-split-keeps-work-identity)
        stmts.append(f"prov:specializationOf <{meta[SPECIALIZATION_KEY]}>")
    # 주석 → 대상 (agt:targets). **링크 키가 아니다**: 주석이 대상의 deps 가 되면 리뷰가 빌드 그래프를 오염시켜 주석 하나가
    # 대상의 재빌드를 유발한다. 주석은 대상을 관찰하지 대상을 구성하지 않으므로 agt:cites 처럼 그래프에만 트리플로 남는다 —
    # LINK_KEYS(링크 개체)에도 gen_build.LINKS(Bazel deps)에도 넣지 않는다. 대상 실재는 validate check_dangling 이 본다
    for t in meta.get(TARGETS_KEY, []) or []:
        stmts.append(f"agt:targets <{t}>")
    # 위험에서 파생된 항목 → 그것이 노출하려는 결함 요인 (agt:exposesFactor, 위험 분석 G5). 대상은 청크가 아니라 온톨로지 개체이므로
    # LINK_KEYS 도 gen_build.LINKS 도 아니다 — 링크 개체의 치역 밖이고 deps 가 되면 T-Box 가 청크의 빌드 입력이 된다.
    # 대상이 agt:DefectFactor 하위 개체인지는 shape 가 본다 (exposes-factor-shapes.ttl)
    for f in meta.get(EXPOSES_KEY, []) or []:
        stmts.append(f"{EXPOSES_PREDICATE} <{f}>")
    c = meta.get("_comment") or {}  # 주석의 본문 파생 사실 (p7-commentary-form) — 닫힌 어휘와 상한은 shape 가 판정한다
    for key, pred in (("label", "agt:commentLabel"), ("decoration", "agt:commentDecoration"), ("resolution", "agt:resolutionState")):
        if key in c:
            stmts.append(f'{pred} "{esc(c[key])}"')
    if "sentences" in c:
        stmts.append(f"agt:commentSentenceCount {c['sentences']}")
    for key in LINK_KEYS:  # 링크는 직접 트리플로도 낸다 — CQ-04·16·17·34 와 verify 질의(verifies-without-criteria)·metrics 가 agt:<key> 술어를 본다. 링크 개체는 emit_links
        for to in meta.get(key, []) or []:
            stmts.append(f"agt:{key} <{to}>")
    for c in meta.get("coUpdatesWith", []):  # 알고 둔 중복 — 안전율 (p4-redundancy-as-safety-margin). 대칭·relatedTo 족
        stmts.append(f"agt:coUpdatesWith <{c}>")
    for v in meta.get("verified", []):
        stmts.append(f'agt:verifiedBy "{esc(v["by"])}"')
        stmts.append(f'agt:verifiedAt "{v["at"]}"^^xsd:dateTime')

    lines = [f"<{meta['id']}>"]
    for i, s in enumerate(stmts):
        sep = " ." if i == len(stmts) - 1 else " ;"
        lines.append(f"    {s}{sep}")
    return "\n".join(lines)
```
<!-- 인용 끝 -->
