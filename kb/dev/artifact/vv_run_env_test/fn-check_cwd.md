---
id: https://agentic-knowledge-base.dev/id/chunk/75a41a5b-41f9-406e-a6e7-ef2d50a688ec
type: artifact
level: executable
title_ko: 함수 check_cwd (tools/vv_run_env_test.py)
title: function check_cwd in tools/vv_run_env_test.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run-env-test}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/78211421-fa91-4809-8250-0a840db49298
---
**함수** — `check_cwd(root)` 다. ③ 하위 프로세스의 작업 디렉토리가 건넨 루트다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_cwd(root: Path) -> list[str]:
    """③ 하위 프로세스의 작업 디렉토리가 건넨 루트다 — 테스트 프로세스의 cwd 를 딴 곳에 두고 잰다."""
    here = Path.cwd()
    with tempfile.TemporaryDirectory(prefix="vv-env-") as elsewhere:
        os.chdir(elsewhere)
        try:
            r = vv_run.run_command(CWD_PROBE, root)
        finally:
            os.chdir(here)
    got = Path(r["out"].strip()).resolve()
    if r["rc"] != 0 or got != root.resolve():
        return [f"FAIL [{GATE}] {CWD_PROBE}: 작업 디렉토리가 {got} 다 — 워크스페이스 루트 {root.resolve()} 여야 "
                "케이스가 적은 상대 경로가 자극에 닿는다"]
    return []
```
<!-- 인용 끝 -->
