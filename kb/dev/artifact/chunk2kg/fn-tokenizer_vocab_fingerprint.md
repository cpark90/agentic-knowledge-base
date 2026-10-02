---
id: https://agentic-knowledge-base.dev/id/chunk/8cbc7b96-a195-459d-89bb-a7d1e25755d2
type: artifact
level: executable
title_ko: 함수 tokenizer_vocab_fingerprint (tools/chunk2kg.py)
title: function tokenizer_vocab_fingerprint in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/5e2d37fd-1039-4929-8dbf-76c76777b467
---
**함수** — `tokenizer_vocab_fingerprint(path)` 다. 어휘 파일의 sha256 — ODD 조건 `id:cond-tokenizer-lock` 의 판정 값이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def tokenizer_vocab_fingerprint(path: str | os.PathLike) -> str:
    """어휘 파일의 sha256 — ODD 조건 `id:cond-tokenizer-lock` 의 판정 값이다."""
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()
```
<!-- 인용 끝 -->
