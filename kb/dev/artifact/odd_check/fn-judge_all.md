---
id: https://agentic-knowledge-base.dev/id/chunk/0644b925-2088-4a6a-bc60-18ffa1808aa1
type: artifact
level: executable
title_ko: 함수 judge_all (tools/odd_check.py)
title: function judge_all in tools/odd_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/bdc32d15-06d9-439b-a3b2-0d3dab05225f
---
**함수** — `judge_all(doc, root, forced)` 다. CHECKS 의 모든 속성을 판정한다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judge_all(doc: dict, root: Path, forced: dict | None = None) -> list[dict]:
    """CHECKS 의 모든 속성을 판정한다 → [{name, iri, title_ko, grade, cmd, state}] (문서 순).

    forced 는 {속성명: 상태} — 그 속성은 cmd 를 돌리지 않고 주어진 상태로 둔다 (assume_check --break 의 인위 파괴).
    """
    checks, attrs = doc.get("CHECKS") or {}, doc.get("ATTRIBUTES") or {}
    forced = forced or {}
    rows = []
    for name, c in checks.items():
        c = c or {}
        attr = attrs.get(name) or {}
        state = forced[name] if name in forced else judge_condition(c, root)
        rows.append({"name": name, "iri": condition_iri(attr), "title_ko": attr.get("title_ko", ""),
                     "grade": str(c.get("grade", "")), "cmd": bool(c.get("cmd")), "state": state})
    return rows
```
<!-- 인용 끝 -->
