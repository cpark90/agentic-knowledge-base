---
id: https://agentic-knowledge-base.dev/id/chunk/f178c885-f133-4f49-a296-18b123272948
type: artifact
level: executable
title_ko: 함수 parse_chunk (tools/chunk2kg.py)
title: function parse_chunk in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/ee14f038-7ba4-416d-8e2c-3314fe17ab94
---
**함수** — `parse_chunk(path)` 다. frontmatter dict와 본문 줄 수를 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def parse_chunk(path: str) -> tuple[dict, int]:
    """frontmatter dict와 본문 줄 수를 돌려준다."""
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError(f"{path}: frontmatter가 없다 — 한 청크는 한 파일이고 head는 frontmatter다")
    try:
        end = lines[1:].index("---") + 1
    except ValueError:
        raise ValueError(f"{path}: frontmatter가 닫히지 않았다")

    meta: dict = {}
    for i, raw in enumerate(lines[1:end], start=2):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if ":" not in raw:
            raise ValueError(f"{path}:{i}: 'key: value' 형식이 아니다: {raw!r}")
        key, _, val = raw.partition(":")
        key, val = key.strip(), val.strip()
        meta[key] = parse_value(val)

    body = lines[end + 1 :]
    while body and not body[-1].strip():
        body.pop()
    while body and not body[0].strip():
        body.pop(0)
    meta["_content_hash"] = hashlib.sha256("\n".join(body).encode("utf-8")).hexdigest()[:12]
    meta["_body_slots"] = body_slots(body)  # 본문이 쓴 슬롯 표지 (결정 p4-slot-answers-one-question)

    for k in REQUIRED:
        if not meta.get(k):
            raise ValueError(f"{path}: frontmatter에 {k} 가 없다")
    if meta["type"] == SPACE_TYPE:  # 설계 공간 — plane 이 아니라 클래스다. 본문(후보·제약)은 space2kg 가 읽는다 (p9-candidate-storage)
        if meta["level"] != SPACE_LEVEL:
            raise ValueError(f"{path}: `-space` 청크의 level 은 {SPACE_LEVEL} 이다 — 후보·제약·배제 근거가 사는 수준이다 "
                             f"(p9-candidate-storage). 실제 {meta['level']!r}")
    elif meta["type"] not in PLANE_CLASS:
        raise ValueError(f"{path}: 알 수 없는 type {meta['type']!r} — plane 이름이거나 `{SPACE_TYPE}` 여야 한다")
    if meta["level"] not in LEVELS:
        raise ValueError(f"{path}: 알 수 없는 level {meta['level']!r}")
    if meta["status"] not in STATES:
        raise ValueError(f"{path}: 알 수 없는 status {meta['status']!r}")
    if "pattern" in meta:  # EARS 패턴 — 요구 문장의 형식이지 다른 plane 의 속성이 아니다 (p7-dev-plane-substance)
        if meta["type"] != "requirement":
            raise ValueError(f"{path}: pattern 은 type: requirement 에서만 쓴다 — 실제 type {meta['type']!r} (EARS 패턴은 요구 문장의 형식이다)")
        if meta["pattern"] not in EARS_PATTERNS:
            raise ValueError(f"{path}: 알 수 없는 pattern {meta['pattern']!r} — {' | '.join(EARS_PATTERNS)} 중 하나다 (EARS, Mavin RE'09)")
    declared = meta.get(TARGETS_KEY) or []
    if declared and meta["type"] != "annotation":  # agt:targets 의 정의역은 agt:AnnotationChunk 다 — 주석만 대상을 가리킨다
        raise ValueError(f"{path}: {TARGETS_KEY} 는 type: annotation 에서만 쓴다 — 실제 type {meta['type']!r} "
                         f"(agt:targets 의 정의역은 agt:AnnotationChunk 다)")
    if meta["type"] == "annotation":  # 주석 — 첫 줄과 슬롯을 읽는다 (p7-commentary-form). 형식 판정은 shape 가 한다
        meta["_comment"] = comment_form(body)
        in_body = meta["_comment"].get("targets")
        if in_body is not None and sorted(in_body) != sorted(declared):
            raise ValueError(f"{path}: 주석의 `대상:` 과 frontmatter {TARGETS_KEY} 가 다르다 — 본문 {sorted(in_body)} · "
                             f"frontmatter {sorted(declared)} (p7-commentary-form: 대상은 둘이 일치해야 한다)")
    if meta["status"] != "deprecated":
        fence = None  # 코드 펜스 안은 인용 구역이다 — 생성기는 원문을 고쳐 쓰지 않으므로(p7-code-extraction-direction)
        for i, raw in enumerate(lines[end + 1 :], start=end + 2):  # 인용원 규칙은 **저작된 본문**의 규칙이다
            m = BODY_FENCE.match(raw)
            if fence:
                if m and m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                    fence = None
                continue
            if m:
                fence = m.group(1)
                continue
            if EPHEMERAL_PATH in raw:
                raise ValueError(f"{path}:{i}: 소멸성 채널 경로를 인용원으로 쓰지 않는다 — 규칙·근거는 영속 지식(노트·결정)에 둔다 "
                                 f"(agrtls-practices-review P): {raw.strip()[:80]}")
    if HANGUL.search(meta["title"]):
        raise ValueError(f"{path}: title {meta['title']!r} 에 한글이 있다 — 영문 라벨에 한글을 섞지 않는다(0.6절)")
    if not HANGUL.search(meta["title_ko"]):
        raise ValueError(f"{path}: title_ko {meta['title_ko']!r} 에 한글이 없다 — 라벨은 한/영 1:1, 한글 라벨은 한글로 쓴다(0.6절)")
    comp = meta.get("composite")
    if isinstance(comp, dict):  # 구조({id, title_ko, title})는 main 이 검사한다 — 여기서는 청크 라벨과 같은 언어 규칙만
        if comp.get("title") and HANGUL.search(comp["title"]):
            raise ValueError(f"{path}: composite.title {comp['title']!r} 에 한글이 있다 — 복합체 라벨도 한/영 1:1(0.6절)")
        if comp.get("title_ko") and not HANGUL.search(comp["title_ko"]):
            raise ValueError(f"{path}: composite.title_ko {comp['title_ko']!r} 에 한글이 없다 — 복합체 라벨도 한/영 1:1(0.6절)")
        if ORDERED_KEY in comp:  # 순서의 선언 — 부분 집합과의 일치는 묶음 전체를 아는 main 이 본다 (p4-composite-order-is-declared)
            for e in order_errors(path, comp[ORDERED_KEY], f"composite.{ORDERED_KEY}"):
                raise ValueError(e)
    gen = meta["generated"]
    if not isinstance(gen, dict) or not gen.get("by") or not gen.get("at"):
        raise ValueError(f"{path}: generated 는 {{by: …, at: …}} 여야 한다 (OKF 행위자 표기)")
    for v in meta.get("verified", []):
        if not isinstance(v, dict) or not v.get("by") or not v.get("at"):
            raise ValueError(f"{path}: verified 항목은 {{by: …, at: …}} 여야 한다")
    if SPECIALIZATION_KEY in meta:  # 분할 조각 → 원 청크 (단일 IRI). 같은 plane·실재·비순환은 묶음 전체를 아는 곳(validate·merge)이 본다
        spec = meta[SPECIALIZATION_KEY]
        if not isinstance(spec, str) or not spec:
            raise SpecializationError(f"{path}: {SPECIALIZATION_KEY} 는 원 청크 IRI 하나여야 한다 — 실제 {spec!r} (p10-split-keeps-work-identity)")
        if spec == meta["id"]:
            raise SpecializationError(f"{path}: {SPECIALIZATION_KEY} 가 자기 자신 {spec} 이다 — 조각은 다른 청크(원본)를 특수화한다")

    return meta, len(body)
```
<!-- 인용 끝 -->
