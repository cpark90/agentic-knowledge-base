---
id: https://agentic-knowledge-base.dev/id/chunk/769e8138-5647-40e0-8626-1ff77d838b92
type: artifact
level: executable
title_ko: 함수 provenance (tools/case_gen.py)
title: function provenance in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d35350bd-7f95-4059-82b7-88108831c060
---
**함수** — `provenance(sc, a, cls)` 다. `**표본 근거**` 한 줄 — 근거 태그·seed·시나리오·값·부류.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def provenance(sc: dict, a: dict, cls: str) -> str:
    """`**표본 근거**` 한 줄 — 근거 태그·seed·시나리오·값·부류. 재생성의 근거가 이 줄과 derivesFrom 이다 (p8-case-generation)."""
    keep = sc["spec"]["keep"]
    tags = list(a["tags"])
    if any(keep[k]["odd"] == ODD_OUTSIDE for k in keep):
        tags.append(ODD_OUTSIDE_TAG)
    vals = " · ".join(f"`{k}={v}`" for k, v in a["values"].items())
    extra = "".join(f" · 요인 `{f}`" for f in a.get("factors", []))
    extra += "".join(f" · 실행 기록 `{r}`" for r in a.get("runs", []))
    side = "keep 안" if cls == "accept" else "keep 밖"
    return (f"**표본 근거** — {' · '.join(f'`{t}`' for t in tags)} · seed `{sc['spec']['seed']}` · 시나리오 `{sc['slug']}`"
            f"{extra}. 값은 {vals}이고 판정 부류는 `{cls}`({side})다.")
```
<!-- 인용 끝 -->
