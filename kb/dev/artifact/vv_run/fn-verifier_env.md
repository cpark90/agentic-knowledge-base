---
id: https://agentic-knowledge-base.dev/id/chunk/1f07f858-5d83-4783-b792-6d5a462e0c7c
type: artifact
level: executable
title_ko: 함수 verifier_env (tools/vv_run.py)
title: function verifier_env in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/4b6ece88-9936-435d-b114-96c75670880e, https://agentic-knowledge-base.dev/id/chunk/8dd4f994-1cfe-41c8-a207-73df40d60c1e]
part_of: https://agentic-knowledge-base.dev/id/composite/38aa6392-7bfb-42b7-84e5-6278007e131f
---
**함수** — `verifier_env(vocab)` 다. `python3 tools/<검증기>.py` 로 직접 부르는 하위 프로세스의 환경 — `clean_env()` 에 둘을 더한다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def verifier_env(vocab: str | os.PathLike = "") -> dict[str, str]:
    """`python3 tools/<검증기>.py` 로 직접 부르는 하위 프로세스의 환경 — `clean_env()` 에 둘을 더한다.

    `PYTHONPATH` 는 `pip_closure_path()` 하나로 — runfiles 의 `tools/` 사본을 담지 않는다(결정
    `p8-verifier-env-isolation` 과 어긋나지 않는다: 그 결정이 걷어내라고 한 것은 실행기의 **도구 모듈** 문맥이고, 서드파티
    패키지는 애초에 그 결정의 대상이 아니다 — 대상을 넓히지 않고 bare `python3` 환경에 하네스가 이미 고정한 의존을 준다).
    `KB_TOKENIZER_VOCAB` 는 토큰 계수가 들어간 검증기(`chunk_lint.py` 등)가 `--vocab` 없이도 같은 고정 어휘를 찾게 한다
    (`tools/chunk2kg.py` 의 `tokenizer_vocab_path` 가 이 환경 변수를 명시 경로 다음으로 본다). 값은 **호출자가 이미
    해소한 절대 경로**다 — 해소와 실패는 `main()` 한 자리에서 일어나고 어휘가 없으면 케이스를 하나도 돌리지 않고
    `EXIT_CONFIG` 로 죽는다. 어휘를 못 찾은 것을 삼키고 계속 돌면 검증기가 자극에 닿기 전에 죽어 판정이 비는데,
    건너뜀은 판정이 아니라 판정의 공백이다 (p8-verifier-env-isolation · p8-reproducibility).
    """
    env = clean_env()
    closure = pip_closure_path()
    if closure:
        env["PYTHONPATH"] = closure
    else:
        env.pop("PYTHONPATH", None)
    if vocab:
        env[kb_lib.TOKENIZER_VOCAB_ENV] = str(Path(vocab).resolve())
    return env
```
<!-- 인용 끝 -->
