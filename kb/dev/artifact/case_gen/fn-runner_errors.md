---
id: https://agentic-knowledge-base.dev/id/chunk/2ac44f3c-c4f0-43b6-a92b-686fa3406caf
type: artifact
level: executable
title_ko: 함수 runner_errors (tools/case_gen.py)
title: function runner_errors in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/cdaa7848-3ca1-4cc0-a72c-836fd556f15e]
part_of: https://agentic-knowledge-base.dev/id/composite/d35350bd-7f95-4059-82b7-88108831c060
---
**함수** — `runner_errors(text)` 다. 생성 케이스를 vv_run 의 파서로 되읽는다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def runner_errors(text: str) -> list[str]:
    """생성 케이스를 vv_run 의 파서로 되읽는다 — 실행기가 케이스를 읽는 꼴이 생성 케이스의 출력 꼴이다."""
    body = kb_lib.chunk_body(text)
    line = next((m for ln in body.splitlines() if (m := vv_run.COMMAND_LINE.match(ln.strip()))), None)
    if line is None:
        return ["`**실행 명령**` 줄이 없다 — 실행기가 명령을 찾지 못한다"]
    cmds = [c for c in vv_run.SPLIT.split(line.group(1).strip()) if c]
    spec, errs = vv_run.case_spec(body)
    return errs + vv_run.check_case(spec, cmds)
```
<!-- 인용 끝 -->
