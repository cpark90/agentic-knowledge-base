---
id: https://agentic-knowledge-base.dev/id/chunk/90f688eb-3f5a-4fec-bfc7-b1a2185f172d
type: artifact
level: executable
title_ko: 함수 render (tools/odd_check.py)
title: function render in tools/odd_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
uses: [https://agentic-knowledge-base.dev/id/chunk/22c8dd80-5cad-4f37-b706-ff35352ff074, https://agentic-knowledge-base.dev/id/chunk/62fad01f-2313-4072-9f22-128e8863be5c, https://agentic-knowledge-base.dev/id/chunk/9608411b-ed6c-441f-9662-2118cdb2a5e7]
part_of: https://agentic-knowledge-base.dev/id/composite/f0f7ba13-f15d-489f-80df-4c7ae50b0cdd
---
**함수** — `render(odd_label, rows)` 다. odd_check 보고 본문과 이탈 속성 목록.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def render(odd_label: str, rows: list[dict]) -> tuple[str, list[str]]:
    """odd_check 보고 본문과 이탈 속성 목록."""
    out_of = [r["name"] for r in rows if r["state"] == "out"]
    unverified = [r["name"] for r in rows if r["state"] == "unverified"]
    verdict = "**ODD 이탈**" if out_of else ("모니터링 불완전 (unverified 있음)" if unverified else "정상 — 모든 속성이 ODD 안")
    rep = kb_lib.gendoc_header(
        "odd_check", "ODD 모니터링 판정", "tools/odd_check.py",
        f"`{odd_label}` 의 속성마다 판정 방법(`CHECKS` 의 명령)을 실제로 돌려 실제 조건이 ODD 안인지 — 이탈이면 작업 중단과 유저 에스컬레이션이다 (3.5절)",
        f"bazel run //tools:odd_check -- --odd {odd_label}", [odd_label], f"속성 {len(rows)}개",
        kb_lib.gendoc_view_notice(f"`{odd_label}` 의 조건 정의"),
        extra=[f"- 결과: {verdict}"])
    body = ["| 속성 | 라벨 | 등급 | 판정 |", "|---|---|---|---|"]
    body += [f"| {r['name']} | {r['title_ko']} | {r['grade']} | {r['state']} |" for r in rows]
    body.append("")
    if out_of:
        body += ["이탈 속성: " + ", ".join(out_of) + " — 작업 중단 + 유저 에스컬레이션, 의존 항목 무효화 대상 (3.5절)"]
    if unverified:
        body += ["판정 불가: " + ", ".join(unverified) + " — 판정 방법(cmd) 보완 대상"]
    return kb_lib.gendoc_assemble(rep, body, [odd_label]), out_of
```
<!-- 인용 끝 -->
