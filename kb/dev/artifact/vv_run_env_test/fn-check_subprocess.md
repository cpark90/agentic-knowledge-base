---
id: https://agentic-knowledge-base.dev/id/chunk/4ec05239-7f7f-4a11-93fb-cc78958546b5
type: artifact
level: executable
title_ko: 함수 check_subprocess (tools/vv_run_env_test.py)
title: function check_subprocess in tools/vv_run_env_test.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run-env-test}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/34277117-5c2c-4fcc-9a6d-fa0bb51bac85]
part_of: https://agentic-knowledge-base.dev/id/composite/78211421-fa91-4809-8250-0a840db49298
---
**함수** — `check_subprocess(root, probe)` 다. ② PYTHONSAFEPATH=1 을 둔 부모에서 실제 하위 프로세스를 띄워 검증기가 종료 0 을 낸다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_subprocess(root: Path, probe: str) -> list[str]:
    """② PYTHONSAFEPATH=1 을 둔 부모에서 실제 하위 프로세스를 띄워 검증기가 종료 0 을 낸다."""
    poison(EXPECTED_ENV)
    cmd = f"python3 tools/{probe}.py --help"
    r = vv_run.run_command(cmd, root)
    if r["rc"] != 0:
        return [f"FAIL [{GATE}] {cmd}: 종료 {r['rc']} — 부모의 파이썬 문맥이 하위 프로세스로 샌다. "
                f"격리가 없으면 검증기는 자극에 닿기 전에 죽는다:\n{r['tail']}"]
    return []
```
<!-- 인용 끝 -->
