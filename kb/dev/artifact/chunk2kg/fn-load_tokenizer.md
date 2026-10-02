---
id: https://agentic-knowledge-base.dev/id/chunk/46cd72ea-813e-4ee5-b990-fede1470c237
type: artifact
level: executable
title_ko: 함수 load_tokenizer (tools/chunk2kg.py)
title: function load_tokenizer in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/6b251b77-d183-4d67-973b-146eb11735d6, https://agentic-knowledge-base.dev/id/chunk/8cbc7b96-a195-459d-89bb-a7d1e25755d2]
part_of: https://agentic-knowledge-base.dev/id/composite/5e2d37fd-1039-4929-8dbf-76c76777b467
---
**함수** — `load_tokenizer(vocab)` 다. 고정된 어휘로 `tiktoken.Encoding` 을 만든다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def load_tokenizer(vocab: str | os.PathLike | None = None):
    """고정된 어휘로 `tiktoken.Encoding` 을 만든다. 해시가 다르면 `ValueError` 로 거부한다.

    네트워크를 쓰지 않는다 — `tiktoken` 의 내려받기 경로(`load_tiktoken_bpe`)를 거치지 않고 고정된 파일을
    직접 해독한다. 파일 형식은 줄마다 `<base64 토큰> <순위>` 다. 특수 토큰은 두지 않는다 — 청크 본문에
    `<|endoftext|>` 같은 문자열이 있어도 보통 텍스트로 센다.
    `import tiktoken` 은 함수 안에 둔다. `kb_lib` 를 import 하는 도구 대부분은 계수기를 의존하지 않고
    그 BUILD 타깃에 패키지가 없다 (`chunk2kg` · `doccheck` 가 그렇다).
    """
    import base64

    import tiktoken
    from tiktoken_ext import openai_public

    path = tokenizer_vocab_path(vocab)
    got = tokenizer_vocab_fingerprint(path)
    if got != TOKENIZER_VOCAB_SHA256:
        raise ValueError(
            f"어휘 파일 {Path(path).as_posix()} 의 sha256 {got} 가 고정값 {TOKENIZER_VOCAB_SHA256} 과 다르다 — "
            f"계수기가 재현되지 않는다 (ODD id:cond-tokenizer-lock 이탈)")
    ranks = {}
    for line in Path(path).read_bytes().splitlines():
        if not line:
            continue
        token, rank = line.split()
        ranks[base64.b64decode(token)] = int(rank)
    pat = getattr(openai_public, TOKENIZER_NAME)()["pat_str"]
    return tiktoken.Encoding(name=TOKENIZER_NAME, pat_str=pat, mergeable_ranks=ranks, special_tokens={})
```
<!-- 인용 끝 -->
