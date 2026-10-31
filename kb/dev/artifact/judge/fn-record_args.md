---
id: https://agentic-knowledge-base.dev/id/chunk/f7d7344d-7095-485f-976f-8de7b92e5e4d
type: artifact
level: executable
title_ko: 함수 record_args (tools/judge.py)
title: function record_args in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-10T00:35:55Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/35cf5136-8348-44b2-8fad-20002523764b, https://agentic-knowledge-base.dev/id/chunk/50114263-78e9-4af8-9078-cd158d3f76eb]
part_of: https://agentic-knowledge-base.dev/id/composite/d3829a12-5161-4435-a412-0e94e23dc6ac
---
**함수** — `record_args(a, root)` 다. `--record` 의 공통 입력 — (기록의 뿌리, 계수기, 일치율 shape 경로).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def record_args(a, root: Path):
    """`--record` 의 공통 입력 — (기록의 뿌리, 계수기, 일치율 shape 경로)."""
    try:  # 로그를 가르는 상한이 토큰이므로 계수기가 기록의 입력이다 (ODD id:cond-tokenizer-lock)
        enc = kb_lib.load_tokenizer(a.vocab or None)
    except (FileNotFoundError, ValueError) as e:
        raise JudgeError(f"어휘 파일 — {e}") from e
    return (at(root, a.into) if a.into else root), enc, root / kb_lib.JUDGE_LOG_SHAPES
```
<!-- 인용 끝 -->
