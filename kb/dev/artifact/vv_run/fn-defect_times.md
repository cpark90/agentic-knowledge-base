---
id: https://agentic-knowledge-base.dev/id/chunk/2393909a-601a-49e0-bc99-833dc33318cb
type: artifact
level: executable
title_ko: 함수 defect_times (tools/vv_run.py)
title: function defect_times in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/fae9d002-8656-4bb1-a04e-18a04452ff08]
part_of: https://agentic-knowledge-base.dev/id/composite/d4585999-3733-43ec-b6f4-d65181e989ce
---
**함수** — `defect_times(root)` 다. 신규 결함의 시각 — 살아 있는 판정 주석 중 판정 결과 주석(`process:judge`)이 아닌 것.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def defect_times(root: Path) -> list[datetime]:
    """신규 결함의 시각 — 살아 있는 판정 주석 중 판정 결과 주석(`process:judge`)이 아닌 것. 판정 결과는 리뷰가 찾은 결함이 아니다."""
    out = []
    for f in sorted((root / VERDICT_DIR).glob("*.md")):
        meta = parse_chunk(str(f))[0]
        if meta["type"] != "annotation" or meta["status"] == "deprecated" or meta["generated"]["by"] == kb_lib.JUDGE_GENERATOR:
            continue
        at = as_utc(meta["generated"]["at"])
        if at is not None:
            out.append(at)
    return out
```
<!-- 인용 끝 -->
