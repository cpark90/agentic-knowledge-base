---
id: https://agentic-knowledge-base.dev/id/chunk/db4948aa-0374-4100-8ea3-fcc9111717da
type: artifact
level: executable
title_ko: 함수 check_judge_log (tools/chunk_lint.py)
title: function check_judge_log in tools/chunk_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/7b250e22-fd3e-4d64-9b95-214bd55ce9d3
---
**함수** — `check_judge_log(text)` 다. 판정 로그의 형식과 필수 필드 (게이트 id `judge-log`) → [(줄 번호, 이유)].

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_judge_log(text: str) -> list[tuple[int, str]]:
    """판정 로그의 형식과 필수 필드 (게이트 id `judge-log`) → [(줄 번호, 이유)].

    게이트는 판정을 부르지 않고 로그만 본다 (결정 p8-judge-calibration-binding). 판정 표의 열이 곧 필수 필드이므로
    헤더가 `kb_lib.JUDGE_LOG_TABLE_HEADER` 와 글자까지 같아야 하고, 행마다 질문 id·값·확신도·판정자 식별자(세션·모델,
    2026-09-30)·입력 지문·시각이 비어 있지 않아야 한다. 확신도는 0 이상 1 이하, 입력 지문은 sha256 64자, 시각은
    ISO 8601 UTC, 처리는 임계가 가르는 세 값 중 하나, `일치`는 일치·불일치·해당 없음 중 하나다. **판정 로그가 0건이면
    이 검사는 아무 것도 거부하지 않는다** — 검사 대상 없음은 SKIP 이 아니라 PASS 다 (로그의 존재를 강제하는 것은
    이 게이트의 몫이 아니다).
    """
    fields, body, start = split_frontmatter(text)
    if not is_judge_log(fields):
        return []
    header = kb_lib.JUDGE_LOG_TABLE_HEADER
    cols = [c.strip() for c in header.split("|")[1:-1]]
    idx = next((i for i, l in enumerate(body) if l.strip().startswith("| ")), None)
    if idx is None or body[idx].strip() != header:
        found = body[idx].strip() if idx is not None else "표 없음"
        return [(start + (idx or 0), f"판정 표의 헤더가 `{header}` 여야 한다 — 열이 곧 필수 필드다"
                                     f"(필수 {' · '.join(kb_lib.JUDGE_LOG_FIELDS)}). 실제 `{found}` "
                                     "(p8-judge-calibration-binding)")]
    errors, rows = [], 0
    for offset, line in enumerate(body[idx + 2 :], start=idx + 2):
        s = line.strip()
        if not s.startswith("|"):
            break
        cells = [c.strip() for c in s.split("|")[1:-1]]
        ln = start + offset
        if len(cells) != len(cols):
            errors.append((ln, f"판정 행의 칸이 {len(cells)}개다 — 헤더와 같은 {len(cols)}개여야 한다"))
            continue
        row = dict(zip(cols, cells))
        rows += 1
        for field in kb_lib.JUDGE_LOG_FIELDS:
            bare = _CELL_CODE.sub(r"\1", row[field]).strip()
            if not bare or bare in kb_lib.EMPTY_VALUE:
                errors.append((ln, f"필수 필드 `{field}` 가 비어 있다 — 판정 로그는 여섯을 전부 적는다 "
                                   "(p8-judge-calibration-binding)"))
        conf = _CELL_CODE.sub(r"\1", row["확신도"]).strip()
        if not kb_lib.JUDGE_CONFIDENCE.match(conf):
            errors.append((ln, f"확신도 `{conf}` 가 0 이상 1 이하의 십진 표기가 아니다 — 확신도는 확률이다"))
        fp = _CELL_CODE.sub(r"\1", row["입력 지문"]).strip()
        if not kb_lib.JUDGE_FINGERPRINT.match(fp):
            errors.append((ln, f"입력 지문 `{fp[:20]}` 이 sha256(소문자 16진 64자)이 아니다 — 지문이 없으면 "
                               "같은 입력에 같은 답이 나왔는지 대조할 수 없다"))
        at = _CELL_CODE.sub(r"\1", row["시각"]).strip()
        if not kb_lib.GENDOC_TIME_RE.match(at):
            errors.append((ln, f"시각 `{at}` 이 ISO 8601 UTC 초 해상도(`{kb_lib.GENDOC_TIME_FORMAT}`)가 아니다"))
        if row["처리"] not in kb_lib.JUDGE_ROUTES:
            errors.append((ln, f"처리 `{row['처리']}` 가 {' · '.join(kb_lib.JUDGE_ROUTES)} 밖이다 — "
                               "구간별 정확도를 재기 전에는 전부 사람 확인 큐다 (규칙 ②)"))
        if row["일치"] not in kb_lib.JUDGE_AGREEMENT:
            errors.append((ln, f"일치 `{row['일치']}` 가 {' · '.join(kb_lib.JUDGE_AGREEMENT)} 밖이다 — "
                               "판정자 둘 이상이 같은 (질문·지문)에 답했을 때만 일치·불일치이고 단독이면 해당 없음이다"))
    if not rows:
        errors.append((start + idx, "판정 표에 행이 없다 — 판정 하나도 없는 로그는 로그가 아니다"))
    return errors
```
<!-- 인용 끝 -->
