---
id: https://agentic-knowledge-base.dev/id/chunk/c4812ae0-4745-4e23-bcd2-a72f82d600fd
type: artifact
level: executable
title_ko: 함수 execute (tools/vv_run.py)
title: function execute in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
part_of: https://agentic-knowledge-base.dev/id/composite/9c609b2d-87cb-474b-9ee8-9a132ba26991
---
**함수** — `execute(cases, root)` 다. 케이스마다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def execute(cases: list[dict], root: Path) -> None:
    """케이스마다 자극을 쓰고 실행 대상 명령을 순서대로 돌린 뒤 기대와 대조한다 (제자리 갱신). 자극은 실행 뒤 지운다."""
    for case in cases:
        tmp, subs = materialize(case["spec"], case["slug"])
        try:
            for i, c in enumerate(case["commands"]):
                if c["skip"] is None:
                    c["run"] = substitute(c["cmd"], subs)
                    c.update(run_command(c["run"], root))
                    c["expect"] = expect_of(case["spec"], i)
                    c["mismatch"] = judge(c, c["expect"])
        finally:
            if tmp is not None:
                shutil.rmtree(tmp, ignore_errors=True)  # 커밋하지 않는다 — 자극은 실행 동안만 있다
        ran = [c for c in case["commands"] if c["skip"] is None]
        skipped = len(case["commands"]) - len(ran)
        # 건너뛴 명령이 하나라도 있으면 케이스는 pass 가 아니다 — 음성 자극이 건너뛰어진 케이스는 "게이트가 거부한다" 를
        # 보이는 절반이 빈 채로 남는다. 판정 어휘는 셋 그대로다(kb_lib.RUN_VERDICTS): 실행한 명령이 기대와 어긋나면 fail,
        # 명령 전부를 실행해 전부 기대와 맞으면 pass, 그 밖(건너뜀이 있거나 실행한 명령이 없음)은 skip 이다. SKIP 은 PASS 가 아니다.
        # 기대는 둘이다 — 종료 코드와 `contains` 의 문구. 둘 다 맞아야 pass 다 (p8-machine-readable-case)
        case["verdict"] = "fail" if any(c["mismatch"] for c in ran) else "pass" if ran and not skipped else "skip"
        case["secs"] = sum(c["secs"] for c in ran)
```
<!-- 인용 끝 -->
