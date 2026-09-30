---
id: https://agentic-knowledge-base.dev/id/chunk/e95cd557-a497-404a-9265-5ebfe0776084
type: artifact
level: executable
title_ko: 함수 check_gendoc (tools/kb_lib.py)
title: function check_gendoc in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
uses: [https://agentic-knowledge-base.dev/id/chunk/078b2808-e9ad-4d17-b2a5-9ab6a30d04f0, https://agentic-knowledge-base.dev/id/chunk/07b69002-1dea-4097-9ab5-18b1bc332898, https://agentic-knowledge-base.dev/id/chunk/15e8fdb5-4855-45e7-a8da-d43faba52099, https://agentic-knowledge-base.dev/id/chunk/46b79267-2ae4-4c11-9208-401a5ac9ab53, https://agentic-knowledge-base.dev/id/chunk/68b9e471-9de9-45d6-8c8c-4d7b5b1609b2, https://agentic-knowledge-base.dev/id/chunk/76e74bc8-5ade-4a57-8804-6270a72fd693, https://agentic-knowledge-base.dev/id/chunk/a0841084-48a1-45f6-842a-57f5b8cbf0c9, https://agentic-knowledge-base.dev/id/chunk/a9138ecc-8714-414e-a8f3-69d0c646e65d, https://agentic-knowledge-base.dev/id/chunk/df94eed1-fa2e-4203-9b68-c415799b6b9a, https://agentic-knowledge-base.dev/id/chunk/ecb06437-81f9-480c-90ba-0b78a8fde56b]
part_of: https://agentic-knowledge-base.dev/id/composite/ce172a2a-c2c5-4b33-b5f6-71a19a8c5bd7
---
**함수** — `check_gendoc(path, text, exists)` 다. 생성 마크다운 규약 G1~G16·G18 중 기계 판정이 되는 것과 G17 후보 → (errors, g17_candidates).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_gendoc(path, text: str, exists=None) -> tuple[list[tuple[int, str]], list[tuple[int, str]]]:
    """생성 마크다운 규약 G1~G16·G18 중 기계 판정이 되는 것과 G17 후보 → (errors, g17_candidates).

    check_prose 와 같은 모양(게이트/보고 분리)으로 낸다 — errors 는 게이트가 `FAIL [gendoc] <파일>:<줄>: <근거>` 로
    찍는다. g17_candidates 는 보고 전용이고 게이트는 보지 않는다 — "값 대신 쓰였는가"를 기계로 못 가르기 때문이다
    (2026-09-29 오탐률 실측, GENDOC_TIME_WORD_RE 주석). exists 는 `경로 → bool` 로 링크 대상의 실재를 판정한다
    (G13). 없으면 문서 안 앵커만 본다.
    """
    errors: list[tuple[int, str]] = []
    lines = text.split("\n")
    start = frontmatter_end(lines)
    while start < len(lines) and not lines[start].strip():  # frontmatter 뒤의 빈 줄은 본문 앞이다
        start += 1
    body = lines[start:]
    while body and not body[-1].strip():
        body.pop()
    rows = list(md_lines(lines))
    quoted = gendoc_quoted_lines(lines)

    # G1 · G2~G7 — 머리 블록. h1 한 줄이 첫 줄이고 순서가 고정이다
    first = start + 1
    if not body or not re.fullmatch(r"# \S.*" + re.escape(GENDOC_H1_SUFFIX), body[0]):
        errors.append((first, f"G1 첫 줄이 `# <이름> — <목적> {GENDOC_H1_SUFFIX}` 가 아니다 — kb_lib.gendoc_header 로 낸다"))
    else:
        if len(body) < 2 or body[1].strip():
            errors.append((first + 1, "G1 h1 다음 줄은 빈 줄이다 — kb_lib.gendoc_header 로 낸다"))
        head = []
        for i, line in enumerate(body[2:], start=2):
            if not line.startswith("- "):
                break
            head.append((first + i, line))
        keys = [k for k in GENDOC_HEAD_KEYS]
        got = [(ln, line[2:].split(":", 1)[0]) for ln, line in head]
        want = [k for k in keys if k != "생성 시각" or any(g == "생성 시각" for _, g in got)]
        for i, k in enumerate(want):
            if i >= len(got) or got[i][1] != k:
                errors.append((head[i][0] if i < len(head) else first + 2,
                               f"G2~G6 머리 블록 {i + 1}번째 항목은 `- {k}:` 다 — 순서는 {' · '.join(want)} 이고 그 뒤가 성격 경고 한 줄이다"))
                break
        else:
            v = {k: head[i][1][2:].split(": ", 1)[-1] for i, k in enumerate(want)}
            if GENDOC_VERSION.split("/")[0] + "/" not in v["생성기"]:
                errors.append((head[0][0], f"G2 생성기 줄에 규약 버전 표기 `{GENDOC_VERSION}` 가 없다 — kb_lib.GENDOC_VERSION 이 단일 정의처다"))
            if "생성 시각" in v and not GENDOC_TIME_RE.fullmatch(v["생성 시각"].strip()):
                errors.append((head[want.index("생성 시각")][0],
                               f"G3 생성 시각이 `{GENDOC_TIME_FORMAT}` 가 아니다 (실제 {v['생성 시각'].strip()!r}) — kb_lib.now_utc 를 쓴다"))
            i_in = head[want.index("입력")][0]
            if "생성 시각" in v and "지문 `sha256:" not in v["입력"]:
                errors.append((i_in, "G4 입력 줄에 지문(`sha256:<앞 12자>`)이 없다 — kb_lib.input_fingerprint 를 쓴다"))
            if "개:" not in v["입력"] and f"#{slug(GENDOC_INPUTS_HEADING)}" not in v["입력"] and NONE_MARK not in v["입력"]:
                errors.append((i_in, f"G4 입력 줄에 파일 목록이 없다 — 개수만 적지 않는다. 많으면 `{GENDOC_INPUTS_HEADING}` 절로 접는다"))
            if f"#{slug(GENDOC_INPUTS_HEADING)}" in v["입력"] and not any(
                    (m := MD_HEADING.match(line)) and m.group(2).strip() == GENDOC_INPUTS_HEADING for _, line in rows):
                errors.append((i_in, f"G4 입력 줄이 `{GENDOC_INPUTS_HEADING}` 절을 가리키는데 그 절이 없다 — kb_lib.gendoc_inputs_section 을 붙인다"))
            if "`" not in v["재현"]:
                errors.append((head[want.index("재현")][0], "G6 재현 줄의 명령은 백틱 안에 적는다 — 자기 자신을 다시 만드는 명령이다"))
            notice = head[len(want)][1] if len(head) > len(want) else ""
            if GENDOC_VIEW_MARK not in notice and GENDOC_TREE_MARK not in notice:
                errors.append((head[len(want) - 1][0] + 1,
                               "G7 머리 블록 끝에 성격 경고 한 줄이 없다 — kb_lib.gendoc_view_notice · gendoc_tree_notice"))

    # G8 · G9 — 제목 계층은 한 단계씩, h1 은 문서당 하나 (MD001 · MD025 · MD041)
    prev_level = 0
    for ln, line in rows:
        m = MD_HEADING.match(line)
        if not m:
            continue
        level = len(m.group(1))
        if level == 1 and prev_level:
            errors.append((ln, f"G9 문서당 h1 은 하나다 (MD025) — `{m.group(2).strip()[:40]}`"))
        elif prev_level and level > prev_level + 1:
            errors.append((ln, f"G8 제목 계층은 한 단계씩 내려간다 (MD001) — h{prev_level} 다음에 h{level} 이 왔다"))
        prev_level = level

    # G10 — 표는 헤더 행을 갖고 열 수가 같고 앞뒤에 빈 줄이 있다 (MD055 · MD056 · MD058)
    by_ln = dict(rows)
    for block in _gendoc_tables(rows):
        ln0, first_line = block[0]
        if ln0 in quoted:
            continue
        if len(block) < 2 or not re.fullmatch(r"\|[\s:|-]+\|", block[1][1].strip()):
            errors.append((ln0, "G10 표에 헤더 행과 구분 행(`|---|`)이 없다 (MD055)"))
            continue
        width = len(_gendoc_cells(first_line))
        for ln, line in block[1:]:
            if len(_gendoc_cells(line)) != width:
                errors.append((ln, f"G10 표의 열 수가 헤더와 다르다 (MD056) — 헤더 {width}, 이 행 {len(_gendoc_cells(line))}"))
        before, after = by_ln.get(ln0 - 1), by_ln.get(block[-1][0] + 1)
        if before is not None and before.strip():
            errors.append((ln0, "G10 표 앞에 빈 줄이 있어야 한다 (MD058)"))
        if after is not None and after.strip():
            errors.append((block[-1][0] + 1, "G10 표 뒤에 빈 줄이 있어야 한다 (MD058)"))
        # G14 — 빈 셀은 없음으로 적는다
        for ln, line in block[2:]:
            for c in _gendoc_cells(line):
                if _GENDOC_EMPTY_CELL.fullmatch(c):
                    errors.append((ln, f"G14 빈 표 셀 — 비우거나 대시를 쓰지 않고 `{NONE_MARK}` 으로 적는다 (Microsoft Writing Style Guide, Tables)"))
                    break

    # G11 — 펜스 코드 블록에 언어를 명시한다 (MD040)
    fence = None
    for i, line in enumerate(lines[start:], start=start + 1):
        m = MD_FENCE.match(line)
        if not m:
            continue
        if fence:
            if m.group(1)[0] == fence[0] and len(m.group(1)) >= len(fence):
                fence = None
            continue
        fence = m.group(1)
        if i not in quoted and not line.strip()[len(m.group(1)):].strip():
            errors.append((i, "G11 펜스 코드 블록에 언어를 명시한다 (MD040) — 예 ```text"))

    # G12 — 긴 문서는 목차 절을 둔다
    headings = [(ln, MD_HEADING.match(line).group(2).strip()) for ln, line in rows if MD_HEADING.match(line)]
    if len(body) > GENDOC_TOC_MIN and not any(h == GENDOC_TOC_HEADING for _, h in headings):
        errors.append((first, f"G12 본문 {len(body)}줄이 {GENDOC_TOC_MIN}줄을 넘는데 `{GENDOC_TOC_HEADING}` 절이 없다 "
                              "(ISO/IEC/IEEE 26514:2022 9.10.5) — kb_lib.gendoc_toc 를 쓴다"))

    # G13 — 링크의 경로와 앵커가 생성물이 놓이는 위치 기준으로 실재한다
    anchors = {a for _, h in headings for a in [slug(h)]} | md_anchors(lines)
    doc_dir = os.path.dirname(str(path))
    for ln, line in rows:
        for dest in find_links(MD_CODE_SPAN.sub(" ", line)):
            if not dest or MD_SCHEME.match(dest):
                continue
            target, _, frag = dest.partition("#")
            if not target:
                if frag and frag not in anchors:
                    errors.append((ln, f"G13 없는 앵커 ({dest}) — 이 문서의 제목 slug 에 #{frag} 가 없다"))
                continue
            if exists is None:
                continue
            rel = os.path.normpath(target[1:] if target.startswith("/") else os.path.join(doc_dir, target))
            if not exists(rel):
                errors.append((ln, f"G13 깨진 링크 ({dest}) — {rel} 가 없다. 생성물은 전 패키지를 한 파일로 합치므로 "
                                   "파일명 상대 링크가 성립하지 않는다. 문서 안 앵커나 저장소 루트 기준 경로(`/`로 시작)로 적는다"))

    # G15 — 비율은 n/d = p.p%. 분모 없는 백분율을 쓰지 않는다. 목표 표기(G16)는 값이 아니라 기준이므로 뺀다
    heading_lines = {ln for ln, line in rows if MD_HEADING.match(line)}
    for ln, seg in prose_segments(text):
        if ln in quoted or ln in heading_lines:  # 제목은 이름이지 측정이 아니다
            continue
        seg = MD_LINK_TEXT.sub(" ", seg)  # 링크 텍스트도 이름이다 — 목차의 라벨이 백분율을 담을 수 있다
        for m in _GENDOC_PCT.finditer(seg):
            before = seg[:m.start()]
            if "목표" in before[-24:]:
                continue
            if not _GENDOC_PCT_OK.search(before):
                errors.append((ln, f"G15 분모 없는 백분율 `{m.group(0)}` — `n/d = p.p%` 꼴로 적는다 (kb_lib.pct)"))
            elif "." not in m.group(1) or len(m.group(1).split(".")[1]) != RATIO_DIGITS:
                errors.append((ln, f"G15 백분율의 소수 자릿수는 {RATIO_DIGITS} 이다 — `{m.group(0)}` (kb_lib.pct)"))

    # G16 — 목표 표기는 `(목표 <값>)` 한 꼴로 통일한다. "이 수치에 목표를 붙여야 하는가"는 사람 판단으로 남기고
    # 이미 쓰인 표기가 갈렸는지만 기계 판정한다 — 콜론 변형 `(목표: …)`은 그 밖의 전부와 다른 표기다
    for ln, seg in prose_segments(text):
        if ln in quoted:
            continue
        if GENDOC_TARGET_BAD_RE.search(seg):
            errors.append((ln, f"G16 목표 표기가 `(목표 <값>)` 꼴이 아니다 — 콜론 없이 값을 바로 잇는다 (STYLEGUIDE §9): "
                                f"{seg.strip()[:80]}"))

    # G18 — 산문은 단정 서술형이다 (STYLEGUIDE §0). 인용해 옮긴 청크 본문은 원본이 같은 게이트를 이미 통과했다
    errors += [(ln, why) for ln, why in check_prose(path, text)[0] if ln not in quoted]

    # G17(보고 전용) — 시점 의존 표현 후보. 제목·표 헤더 행·인용 구역은 이름/원문이지 측정이 아니라서 뺀다
    # (G15 의 제목·링크 텍스트 제외와 같은 근거). 게이트는 이 목록을 보지 않는다
    header_row_lines = {block[0][0] for block in _gendoc_tables(rows)
                        if len(block) >= 2 and re.fullmatch(r"\|[\s:|-]+\|", block[1][1].strip())}
    g17: list[tuple[int, str]] = []
    for ln, seg in prose_segments(text):
        if ln in quoted or ln in heading_lines or ln in header_row_lines:
            continue
        seg2 = MD_LINK_TEXT.sub(" ", seg)
        for m in GENDOC_TIME_WORD_RE.finditer(seg2):
            g17.append((ln, f"G17 시점 의존 표현 후보 `{m.group(0)}` — 값 대신 쓰였는지 사람이 판단한다 (STYLEGUIDE §9): "
                            f"{seg2.strip()[:80]}"))

    return sorted(errors), sorted(g17)
```
<!-- 인용 끝 -->
