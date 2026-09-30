---
id: https://agentic-knowledge-base.dev/id/chunk/9dc7489b-268b-4ce2-9f99-fdb748499729
type: artifact
level: executable
title_ko: 함수 expect_note (tools/vv_run.py)
title: function expect_note in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/e9c6807f-239f-4a44-beed-743506b59164
---
**함수** — `expect_note(exp)` 다. 보고의 `기대` 칸 — 기대를 적지 않은 명령은 종료 0 만 본다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def expect_note(exp: dict | None) -> str:
    """보고의 `기대` 칸 — 기대를 적지 않은 명령은 종료 0 만 본다 (점진 도입)."""
    if not exp:
        return "종료 0 (기대 없음)"
    bits = [f"종료 {exp['exit']}"] if exp.get("exit") is not None else ["종료 0"]
    if phrases(exp.get("contains")):
        bits.append("문구 " + " · ".join(f"`{ph}`" for ph in phrases(exp["contains"])))
    return " · ".join(bits)
```
<!-- 인용 끝 -->
