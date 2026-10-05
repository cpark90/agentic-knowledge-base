---
id: https://agentic-knowledge-base.dev/id/chunk/cad21a57-2adb-46fe-b8c7-82cd106906ed
type: artifact
level: executable
title_ko: 함수 round_records (tools/vv_run.py)
title: function round_records in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/fae9d002-8656-4bb1-a04e-18a04452ff08]
part_of: https://agentic-knowledge-base.dev/id/composite/d4585999-3733-43ec-b6f4-d65181e989ce
---
**함수** — `round_records(root)` 다. 이미 있는 라운드 기록의 시각 — 오름차순.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def round_records(root: Path) -> list[datetime]:
    """이미 있는 라운드 기록의 시각 — 오름차순. 기록의 시각이 라운드의 끝(경계)이다."""
    out = []
    for f in sorted((root / RUN_DIR).glob(f"{ROUND_PREFIX}*.md")):
        at = as_utc(parse_chunk(str(f))[0]["generated"]["at"])
        if at is None:
            raise ValueError(f"{f}: generated.at 을 읽을 수 없다 — 라운드 경계가 서지 않는다")
        out.append(at)
    return sorted(out)
```
<!-- 인용 끝 -->
