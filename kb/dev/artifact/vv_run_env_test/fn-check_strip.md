---
id: https://agentic-knowledge-base.dev/id/chunk/890796e2-4d86-47b3-8963-ccab2ab97d40
type: artifact
level: executable
title_ko: 함수 check_strip (tools/vv_run_env_test.py)
title: function check_strip in tools/vv_run_env_test.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run-env-test}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
part_of: https://agentic-knowledge-base.dev/id/composite/78211421-fa91-4809-8250-0a840db49298
---
**함수** — `check_strip()` 다. ① 걷어내는 목록이 규약의 다섯과 같고 clean_env 가 그 다섯을 전부 지운다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def check_strip() -> list[str]:
    """① 걷어내는 목록이 규약의 다섯과 같고 clean_env 가 그 다섯을 전부 지운다."""
    msgs, declared = [], tuple(vv_run.BAZEL_PY_ENV)
    missing = [n for n in EXPECTED_ENV if n not in declared]
    extra = [n for n in declared if n not in EXPECTED_ENV]
    if missing:
        msgs.append(f"FAIL [{GATE}] vv_run.BAZEL_PY_ENV: {', '.join(missing)} 이 없다 — "
                    "결정 p8-verifier-env-isolation 은 다섯을 전부 걷어낸다. 목록을 줄이려면 결정을 먼저 고친다")
    if extra:
        msgs.append(f"FAIL [{GATE}] vv_run.BAZEL_PY_ENV: {', '.join(extra)} 은 결정에 없다 — "
                    "걷어낼 변수를 늘리려면 결정 p8-verifier-env-isolation 과 이 검사의 기대를 같은 커밋에서 고친다")
    poison(EXPECTED_ENV)
    env = vv_run.clean_env()
    left = [n for n in EXPECTED_ENV if n in env]
    if left:
        msgs.append(f"FAIL [{GATE}] clean_env(): {', '.join(left)} 이 남았다 — "
                    "케이스의 명령이 실행기의 파이썬 문맥을 물려받는다")
    if env.get(SENTINEL) != "keep":
        msgs.append(f"FAIL [{GATE}] clean_env(): 다섯 밖의 변수 {SENTINEL} 까지 사라졌다 — "
                    "격리는 환경을 비우는 것이 아니라 다섯을 걷어내는 것이다")
    return msgs
```
<!-- 인용 끝 -->
