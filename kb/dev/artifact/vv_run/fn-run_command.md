---
id: https://agentic-knowledge-base.dev/id/chunk/72467e81-75de-4b48-92ac-2d429de91d8e
type: artifact
level: executable
title_ko: 함수 run_command (tools/vv_run.py)
title: function run_command in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/1f07f858-5d83-4783-b792-6d5a462e0c7c, https://agentic-knowledge-base.dev/id/chunk/4b6ece88-9936-435d-b114-96c75670880e]
part_of: https://agentic-knowledge-base.dev/id/composite/38aa6392-7bfb-42b7-84e5-6278007e131f
---
**함수** — `run_command(cmd, root, vocab)` 다. 셸로 실행 — 워크스페이스 루트에서.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def run_command(cmd: str, root: Path, vocab: str | os.PathLike = "") -> dict:
    """셸로 실행 — 워크스페이스 루트에서. 종료 코드·소요·출력 꼬리를 남긴다.

    `python3 ` 로 시작하는 명령은 인터프리터를 vv_run 자신의 것(`sys.executable` — 하네스의 pip 폐포가 보이는 쪽)으로
    바꾼다. bare `python3` 에는 `tiktoken` 같은 서드파티 의존이 없을 수 있어(이 저장소 실측, 2026-10-01) 토큰 계수가
    들어간 검증기가 `ModuleNotFoundError` 로 자극에 닿기 전에 죽는다 — 그 처리가 `verifier_env()` 다.
    `vocab` 은 `main()` 이 해소한 어휘 파일의 절대 경로이고 그 자리로 `KB_TOKENIZER_VOCAB` 가 간다.
    """
    exe = sys.executable
    if cmd.startswith(PYTHON_RUNNER) and exe:
        cmd, env = exe + cmd[len("python3"):], verifier_env(vocab)
    else:
        env = clean_env()
    t0 = time.monotonic()
    r = subprocess.run(cmd, shell=True, cwd=root, capture_output=True, text=True, env=env)
    out = r.stdout + r.stderr
    tail = "\n".join(out.strip().splitlines()[-6:])
    m = EXECUTED.search(out)
    tests = (int(m.group(2)), int(m.group(1))) if m else None  # (전체, 실행) — 없으면 요약 줄이 없는 실패
    return {"rc": r.returncode, "secs": time.monotonic() - t0, "tail": tail, "out": out, "tests": tests}
```
<!-- 인용 끝 -->
