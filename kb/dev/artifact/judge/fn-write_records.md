---
id: https://agentic-knowledge-base.dev/id/chunk/0b44a7ed-753e-4f76-bfba-efd520b3c3f1
type: artifact
level: executable
title_ko: 함수 write_records (tools/judge.py)
title: function write_records in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/29c0f765-ca46-4758-8671-e2013c8c7e8a, https://agentic-knowledge-base.dev/id/chunk/35cf5136-8348-44b2-8fad-20002523764b, https://agentic-knowledge-base.dev/id/chunk/5e8f0410-5a7f-4fe4-848c-4414e21924d0, https://agentic-knowledge-base.dev/id/chunk/81e5e72c-14de-43e1-ac54-19566c8df95e, https://agentic-knowledge-base.dev/id/chunk/942e32e9-5c96-4432-8b79-c82af3a44f4f, https://agentic-knowledge-base.dev/id/chunk/a720999d-da2c-4b54-9c40-b64df9c9a74a]
part_of: https://agentic-knowledge-base.dev/id/composite/40ebb229-865e-4943-872b-b8b168710b83
---
**함수** — `write_records(root, rows, q, name, decoy, source, now, enc, shapes, first)` 다. 판정 로그와 결과 주석을 쓴다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def write_records(root: Path, rows: list[dict], q: dict, name: str, decoy: str, source: str, now: datetime,
                  enc, shapes: Path, first: int = 0) -> list[Path]:
    """판정 로그와 결과 주석을 쓴다 — 이미 있는 파일을 덮지 않는다 (append-only, r-026). 쓰기 전에 로그 글을 일치율
    shape(`shapes`)로 검사하고 위반이 있으면 아무 것도 쓰지 않는다 (Q-0056 Q119-a).

    결과 주석의 파일명은 `<파트 디렉토리>-<파일 stem>`(`verdict_stem`)을 쓴다(2026-09-30 vnv 결함 보고 ②) —
    결정 기록은 파일 stem이 전부 `conclusion`·`rationale`·`alternatives`뿐이라 파일명이 그대로 부딪힌다
    (측정: 실표본 60 중 50건이 그 충돌로 로그에 못 들어갔다). 부모 디렉토리 이름(결정 슬러그)을 더하면 유일하다.
    """
    stamp = kb_lib.utc_stamp(now)
    log_dir, verdict_dir = root / kb_lib.JUDGE_LOG_DIR, root / kb_lib.JUDGE_VERDICT_DIR
    chunks, texts = log_texts(rows, q, name, decoy, source, stamp, enc, shapes)  # 위반이 하나라도 있으면 아무 것도 쓰지 않는다
    log_dir.mkdir(parents=True, exist_ok=True)
    verdict_dir.mkdir(parents=True, exist_ok=True)
    written = []
    for i, part in enumerate(chunks, start=first):   # `first` — 한 실행이 질문 여럿의 로그를 쓸 때 파일 번호를 잇는다(쌍 모드)
        suffix = "" if i == 0 else f"-{i + 1}"
        target = log_dir / f"{kb_lib.JUDGE_LOG_PREFIX}{now.strftime('%Y%m%dT%H%M%SZ')}{suffix}.md"
        if target.exists():
            raise JudgeError(f"{target}: 이미 있다 — 판정 로그는 append-only 다 (r-026)")
        target.write_text(texts[i - first], encoding="utf-8")
        written.append(target)
    if rows and rows[0].get("pair"):   # 쌍 모드 — 결과 주석은 쌍마다 하나다
        groups: dict = defaultdict(list)
        for r in rows:
            groups[r["iri"]].append(r)
        for grp in groups.values():
            target = verdict_dir / f"{kb_lib.JUDGE_LOG_PREFIX}{name.lower()}-pair-{grp[0]['pair_fp'][:8]}.md"
            if target.exists():
                raise JudgeError(f"{target}: 이미 있다 — 같은 질문·쌍의 앞 판정이 있다. 그 주석의 `해소:` 를 먼저 닫는다")
            target.write_text(verdict_pair_chunk(grp, q, name, stamp), encoding="utf-8")
            written.append(target)
        return written
    for r in rows:
        target = verdict_dir / f"{kb_lib.JUDGE_LOG_PREFIX}{name.lower()}-{r['verdict_stem']}-{slug(r['judge'])}.md"
        if target.exists():
            raise JudgeError(f"{target}: 이미 있다 — 같은 질문·판정자의 앞 판정이 있다. 그 주석의 `해소:` 를 먼저 닫는다")
        target.write_text(verdict_chunk(r, q, name, stamp), encoding="utf-8")
        written.append(target)
    return written
```
<!-- 인용 끝 -->
