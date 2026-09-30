---
id: https://agentic-knowledge-base.dev/id/chunk/fad9cc7c-a705-42d5-adcc-e124bff2c57c
type: artifact
level: executable
title_ko: 함수 check_case (tools/vv_run.py)
title: function check_case in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/d941f238-14e0-4a1b-8d8f-918968b9587f
---
**함수** — `check_case(spec, cmds)` 다. 케이스 형식 검사 — 펜스와 실행 명령의 대조.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_case(spec: dict, cmds: list[str]) -> list[str]:
    """케이스 형식 검사 — 펜스와 실행 명령의 대조. 메시지가 곧 수정 안내다 (STYLEGUIDE §7)."""
    errs = []
    expect = spec.get("expect")
    if expect is not None and len(expect) != len(cmds):
        errs.append(f"`expect` 항목 {len(expect)}개가 실행 명령 {len(cmds)}개와 다르다 — 명령 순서마다 하나를 적는다")
    for c in cmds:
        m = BAZEL_RUN_VERIFIER.match(c.strip())
        if m and m.group(1) in READ_ONLY_VERIFIERS:
            errs.append(f"`bazel run //tools:{m.group(1)}` 는 runfiles 트리에서 돌아 워크스페이스 상대 경로 인자를 자극이 아닌 "
                        f"runfiles 의 없는 파일로 푼다 — `python3 tools/{m.group(1)}.py` 로 바꾼다 (실행의 cwd 가 워크스페이스 루트다)")
    names = set(spec.get("files") or {})
    used = {m for c in cmds for m in PLACEHOLDER.findall(c)}
    for ph in sorted(used - names):
        errs.append(f"명령의 `{{{{{ph}}}}}` 가 `files` 에 없다 — 자극의 이름과 같아야 한다")
    for name in sorted(names - used):
        errs.append(f"`files` 의 `{name}` 을 명령이 가리키지 않는다 — 쓰이지 않는 자극은 케이스의 절반이 빈 것이다")
    return errs
```
<!-- 인용 끝 -->
