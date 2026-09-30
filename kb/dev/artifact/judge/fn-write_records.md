---
id: https://agentic-knowledge-base.dev/id/chunk/0b44a7ed-753e-4f76-bfba-efd520b3c3f1
type: artifact
level: executable
title_ko: 함수 write_records (tools/judge.py)
title: function write_records in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/3723c1d5-0d22-4da6-86ca-1b408cdc80dc
---
**함수** — `write_records(root, rows, q, name, th, source, now)` 다. 판정 로그와 결과 주석을 쓴다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def write_records(root: Path, rows: list[dict], q: dict, name: str, th: dict, source: str, now: datetime) -> list[Path]:
    """판정 로그와 결과 주석을 쓴다 — 이미 있는 파일을 덮지 않는다 (append-only, r-026).

    결과 주석의 파일명은 `<파트 디렉토리>-<파일 stem>`(`verdict_stem`)을 쓴다(2026-09-30 vnv 결함 보고 ②) —
    결정 복합체는 파일 stem이 전부 `conclusion`·`rationale`·`alternatives`뿐이라 파일명이 그대로 부딪힌다
    (실측: 실표본 60 중 50건이 그 충돌로 로그에 못 들어갔다). 부모 디렉토리 이름(결정 슬러그)을 더하면 유일하다.
    """
    stamp = kb_lib.utc_stamp(now)
    log_dir, verdict_dir = root / kb_lib.JUDGE_LOG_DIR, root / kb_lib.JUDGE_VERDICT_DIR
    log_dir.mkdir(parents=True, exist_ok=True)
    verdict_dir.mkdir(parents=True, exist_ok=True)
    written = []
    chunks = [rows[i:i + MAX_ROWS] for i in range(0, len(rows), MAX_ROWS)]
    for i, part in enumerate(chunks):
        suffix = "" if i == 0 else f"-{i + 1}"
        target = log_dir / f"{kb_lib.JUDGE_LOG_PREFIX}{now.strftime('%Y%m%dT%H%M%SZ')}{suffix}.md"
        if target.exists():
            raise JudgeError(f"{target}: 이미 있다 — 판정 로그는 append-only 다 (r-026)")
        target.write_text(log_chunk(part, q, name, th, source, stamp), encoding="utf-8")
        written.append(target)
    for r in rows:
        target = verdict_dir / f"{kb_lib.JUDGE_LOG_PREFIX}{name.lower()}-{r['verdict_stem']}-{slug(r['judge'])}.md"
        if target.exists():
            raise JudgeError(f"{target}: 이미 있다 — 같은 질문·판정자의 앞 판정이 있다. 그 주석의 `해소:` 를 먼저 닫는다")
        target.write_text(verdict_chunk(r, q, name, stamp), encoding="utf-8")
        written.append(target)
    return written
```
<!-- 인용 끝 -->
