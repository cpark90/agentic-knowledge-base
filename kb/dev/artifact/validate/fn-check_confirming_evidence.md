---
id: https://agentic-knowledge-base.dev/id/chunk/d44afb5e-6469-4c49-9b40-d3b2f01ae0a6
type: artifact
level: executable
title_ko: 함수 check_confirming_evidence (tools/validate.py)
title: function check_confirming_evidence in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d62da398-7c0d-493a-9514-8d3ccebe5ca7
---
**함수** — `check_confirming_evidence(query_dir)` 다. 확정 근거 증거 종류의 단일 정의 위치 — verify 질의 confirmed-without-evidence 의 FILTER 목록이 `kb_lib.SPACE_CONFIRMING_EVIDENCE` 와 같은 집합인가 (게이트 id `verify`, 2026-10-24).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_confirming_evidence(query_dir: str) -> list[str]:
    """확정 근거 증거 종류의 단일 정의 위치 — verify 질의 confirmed-without-evidence 의 FILTER 목록이
    `kb_lib.SPACE_CONFIRMING_EVIDENCE` 와 같은 집합인가 (게이트 id `verify`, 2026-10-24).

    SPARQL 파일은 파이썬 상수를 읽지 못하므로 같은 집합이 두 곳에 적힌다. 원본은 상수이고 질의는 그 사본이다 —
    space2kg·validate.check_space 가 상수를 읽고, 질의가 갈리면 여기서 FAIL 이다(유저 결정을 더한 개정 Q-0055 Q111-a).
    """
    from pathlib import Path
    rq = Path(query_dir) / "confirmed-without-evidence.rq"
    if not rq.is_file():
        return [f"[{VERIFY}] {rq.as_posix()}: 없다 — 확정 근거 없는 확정 링크를 잡는 질의가 있어야 한다 (9.11절)"]
    m = re.search(r"FILTER\s*\(\s*\?k\s+IN\s*\(([^)]*)\)", rq.read_text(encoding="utf-8"))
    found = {t.strip().split(":", 1)[-1] for t in m.group(1).split(",")} if m else set()
    want = set(kb_lib.SPACE_CONFIRMING_EVIDENCE)
    if found != want:
        return [f"[{VERIFY}] {rq.as_posix()}: 확정 근거 증거 종류 {sorted(found)} 가 kb_lib.SPACE_CONFIRMING_EVIDENCE "
                f"{sorted(want)} 와 다르다 — 원본은 상수다. 질의의 FILTER 목록을 상수에 맞춘다"]
    return []
```
<!-- 인용 끝 -->
