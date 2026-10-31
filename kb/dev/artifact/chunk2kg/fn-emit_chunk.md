---
id: https://agentic-knowledge-base.dev/id/chunk/53335074-67d7-45c8-b564-78065ea96eb8
type: artifact
level: executable
title_ko: 함수 emit_chunk (tools/chunk2kg.py)
title: function emit_chunk in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/578f22f5-4d9d-43ef-8b3a-1459989cf6e9, https://agentic-knowledge-base.dev/id/chunk/8c16b743-c8b1-4799-9c5b-5b003686ac07, https://agentic-knowledge-base.dev/id/chunk/d75bcbfe-969b-45d4-81f9-fc42145f892b]
part_of: https://agentic-knowledge-base.dev/id/composite/094f7e14-ed5b-4c40-83f8-782d9f4161b0
---
**함수** — `emit_chunk(path, meta, tokens, conventions)` 다. 단위 지식 하나의 head 블록.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def emit_chunk(path: str, meta: dict, tokens: int, conventions: dict | None = None) -> str:
    """단위 지식 하나의 head 블록. `conventions` 는 결정 slug → 결정 기록 IRI — 절 항목의 `items` 를 agt:projectsConvention 으로 낸다.

    사상에 없는 slug 는 호출자(main)가 먼저 거부한다 — 여기 오면 전부 풀린다.
    """
    substance = PROFILE_SUBSTANCE.get(meta["type"])  # norm 은 실체 클래스가 없다 — 지식 종류 클래스 하나로 타이핑한다
    stmts = [
        f"a {PLANE_CLASS[meta['type']]}" + (f" , {substance}" if substance else ""),
        *label_stmts(meta["title"], meta["title_ko"], meta.get(FORMER_TITLE_KEY)),
        f"agt:hasLevel agt:{meta['level']}",
        # 서비스 층 — plane·level 과 나란한 직교 축이다. **명시가 없어도 기본값을 방출한다**: 표시 누락을 산발로
        # 세지 않으려면 지식 층 배정이 그래프에 있어야 하고, 그래야 층별 집계(CQ-38)의 분모가 항목 전수가 된다
        # (p0-service-is-a-three-layer-wiki). 값의 닫힌 집합은 shape layer-shapes.ttl 이 판정한다
        f"{LAYER_PREDICATE} {LAYERS[meta.get(LAYER_KEY, LAYER_DEFAULT)]}",
    ]
    if "pattern" in meta:
        stmts.append(f"agt:pattern {EARS_PATTERNS[meta['pattern']]}")
    if NORM_HEADING_KEY in meta:  # 절 제목·깊이 — 절 항목의 shape(norm-section-shapes.ttl)가 짝과 값을 본다
        stmts.append(f'agt:sectionHeading "{esc(meta[NORM_HEADING_KEY])}"')
    if NORM_DEPTH_KEY in meta:
        stmts.append(f"agt:sectionDepth {int(meta[NORM_DEPTH_KEY])}")
    if meta.get(NORM_CONTINUES_KEY) == "true":  # 이어짐 절 항목 — 제목·깊이 없이 규약 줄을 싣는 자리를 shape 가 머리 단위 지식과 가른다
        stmts.append("agt:sectionContinues true")
    for slug in norm_item_slugs(meta.get("_norm_items") or [], links=False):  # 절이 싣는 줄의 결정
        stmts.append(f"{PROJECTS_CONVENTION_PREDICATE} <{(conventions or {})[slug]}>")
    stmts += [
        f"agt:tokenCount {tokens}",  # 본문의 크기 — 단위는 토큰이고 계수기는 o200k_base 다 (p1-chunk-unit-is-tokens)
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
    # 위험에서 파생된 항목 → 그것이 노출하려는 결함 요인 (agt:exposesFactor, 위험 분석 G5). 대상은 지식이 아니라 온톨로지 개체이므로
    # LINK_KEYS 도 gen_build.LINKS 도 아니다 — 링크 개체의 치역 밖이고 deps 가 되면 T-Box 가 단위 지식의 빌드 입력이 된다.
    # 대상이 agt:DefectFactor 하위 개체인지는 shape 가 본다 (exposes-factor-shapes.ttl)
    for f in meta.get(EXPOSES_KEY, []) or []:
        stmts.append(f"{EXPOSES_PREDICATE} <{f}>")
    # 정의 → 같은 모듈의 정의 (agt:usesDefinition, references 족의 잎). 추출기가 AST 에서 낸 값이고 손으로 쓰지 않는다.
    # LINK_KEYS 도 gen_build.LINKS 도 아니다 — 링크는 파일 복합체의 것이고(p7-code-links-on-file-composite) 함수 churn 이
    # 빌드 그래프를 움직이면 안 된다. 대상 실재는 validate check_dangling 이 본다
    for u in meta.get(USES_KEY, []) or []:
        stmts.append(f"{USES_PREDICATE} <{u}>")
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
    # verified 는 판정 이력이라 누적된다 (p2-judgement-history-in-verified). 시각은 항목마다 낸다 — trust shape 가 그 최댓값을
    # 생성 시각과 비교한다. 주체는 지금 내용의 판정(at ≥ generated.at)만 낸다 — 신뢰 등급과 writer 의 인수는 agt:verifiedBy 를
    # 읽으므로, 옛 내용에 찍힌 human: 승인이 지금 내용의 등급이 되지 않는다 (유저 답 Q-0064#Q159-a, p2-trust-tier-from-generated-and-verified)
    for v in meta.get("verified", []):
        try:
            current = datetime.fromisoformat(str(v["at"])) >= datetime.fromisoformat(str(meta["generated"]["at"]))
        except (TypeError, ValueError):  # 읽을 수 없거나 비교할 수 없는 시각은 지금 판정으로 세지 않는다
            current = False
        if current:
            stmts.append(f'agt:verifiedBy "{esc(v["by"])}"')
        stmts.append(f'agt:verifiedAt "{v["at"]}"^^xsd:dateTime')

    lines = [f"<{meta['id']}>"]
    for i, s in enumerate(stmts):
        sep = " ." if i == len(stmts) - 1 else " ;"
        lines.append(f"    {s}{sep}")
    return "\n".join(lines)
```
<!-- 인용 끝 -->
