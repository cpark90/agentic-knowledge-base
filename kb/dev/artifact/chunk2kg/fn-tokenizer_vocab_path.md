---
id: https://agentic-knowledge-base.dev/id/chunk/6b251b77-d183-4d67-973b-146eb11735d6
type: artifact
level: executable
title_ko: 함수 tokenizer_vocab_path (tools/chunk2kg.py)
title: function tokenizer_vocab_path in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/5e2d37fd-1039-4929-8dbf-76c76777b467
---
**함수** — `tokenizer_vocab_path(explicit)` 다. 고정된 어휘 파일의 경로.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def tokenizer_vocab_path(explicit: str | os.PathLike | None = None) -> Path:
    """고정된 어휘 파일의 경로. 명시 경로 → 환경 변수 → runfiles 순으로 찾고 없으면 `FileNotFoundError` 다.

    **명시가 우선이다** — 타깃이 `--vocab=$(rootpath @tiktoken_o200k_base//file)` 로 주는 경로가 그 자리다.
    runfiles 자리는 `bazel run` 의 것이다 — `http_file` 의 산출물은 외부 저장소에 살아
    `<runfiles>/{repo}/file/{name}` 이고, cwd 가 `_main` 인 부트스트랩에서는 `../{repo}/file/{name}` 이다.
    `{repo}` 는 canonical 이름(`+http_file+…`)과 apparent 이름 둘을 다 본다 — bzlmod 의 실측 디렉토리는
    앞의 것이고 뒤의 것만 보면 인자 없이 부른 경로가 전부 빗나간다.
    """
    if explicit:
        p = Path(explicit)
        if not p.is_file():
            raise FileNotFoundError(f"어휘 파일 {p} 가 없다")
        return p
    env = os.environ.get(TOKENIZER_VOCAB_ENV)
    if env:
        return tokenizer_vocab_path(env)
    rels = [f"{repo}/file/{TOKENIZER_VOCAB_FILE}"
            for repo in (TOKENIZER_VOCAB_REPO_CANONICAL, TOKENIZER_VOCAB_REPO)]
    runfiles = os.environ.get("RUNFILES_DIR", "")
    bases = ([Path(runfiles)] if runfiles else []) + [Path(".."), Path("external")]
    for base in bases:
        for rel in rels:
            if (base / rel).is_file():
                return base / rel
    raise FileNotFoundError(
        f"어휘 파일 {TOKENIZER_VOCAB_FILE} 을 찾지 못했다 — `bazel run //tools:tokens` 로 돌리거나 "
        f"{TOKENIZER_VOCAB_ENV} 에 경로를 준다 (고정처는 MODULE.bazel 의 http_file {TOKENIZER_VOCAB_REPO}, "
        f"runfiles 의 이름은 {TOKENIZER_VOCAB_REPO_CANONICAL} 다)")
```
<!-- 인용 끝 -->
