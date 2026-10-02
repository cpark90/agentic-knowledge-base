---
id: https://agentic-knowledge-base.dev/id/chunk/1cfb1c75-6407-431a-96f9-0e38abd07445
type: artifact
level: executable
title_ko: 절 tokenizer-name (tools/chunk2kg.py)
title: section tokenizer-name in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/ab66f02d-6126-4507-b73a-c29429769f11, https://agentic-knowledge-base.dev/id/chunk/01f6a247-ed75-405f-b286-3d59b8acc9d2, https://agentic-knowledge-base.dev/id/chunk/28655d6b-d000-4f43-8d68-9e0ce042c39c]
part_of: https://agentic-knowledge-base.dev/id/composite/5e2d37fd-1039-4929-8dbf-76c76777b467
composite: {id: https://agentic-knowledge-base.dev/id/composite/5e2d37fd-1039-4929-8dbf-76c76777b467, title_ko: 절 복합체 tokenizer-name (tools/chunk2kg.py), title: section composite tokenizer-name in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/1cfb1c75-6407-431a-96f9-0e38abd07445, https://agentic-knowledge-base.dev/id/chunk/6b251b77-d183-4d67-973b-146eb11735d6, https://agentic-knowledge-base.dev/id/chunk/8cbc7b96-a195-459d-89bb-a7d1e25755d2, https://agentic-knowledge-base.dev/id/chunk/46cd72ea-813e-4ee5-b990-fede1470c237, https://agentic-knowledge-base.dev/id/chunk/1d31fc8d-2de8-4f7d-8e58-8a0252739342, https://agentic-knowledge-base.dev/id/chunk/260d24aa-5aab-4ff7-81b7-40def184e51f], part_of: https://agentic-knowledge-base.dev/id/composite/f7d6eec7-bef4-4e94-ac55-36e7dda654ce}
---
**절** — `tools/chunk2kg.py` 의 절 `tokenizer-name` 다. 본문과 토큰 계수기 — 크기의 단위는 토큰이다 (결정 p1-chunk-unit-is-tokens)

**정의** — `tokenizer_vocab_path` · `tokenizer_vocab_fingerprint` · `load_tokenizer` · `body_text` · `token_count` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 본문과 토큰 계수기 — 크기의 단위는 토큰이다 (결정 p1-chunk-unit-is-tokens) ────────────────────
# 본문을 떼는 규칙과 계수기가 이 모듈에 사는 까닭은 **head 액션**이다 — 청크 타깃마다 한 번 돌고 rdflib 를
# 싣지 않는다(`py_binary //tools:chunk2kg` 의 deps 가 비어 있다). `kb_lib` 에 두면 액션마다 rdflib 적재를
# 문다. `kb_lib` 는 이 이름들을 다시 내보내고 호출자는 `kb_lib.body_text`·`kb_lib.token_count` 를 쓴다.
# 크기의 단위가 줄에서 토큰으로 바뀌면 계수기가 빌드 입력이 된다. 재현의 조건은 둘이다 — 어휘 파일이
# 같은 바이트로 읽히고, 그것을 읽는 패키지의 버전이 같아야 한다. 어휘는 `MODULE.bazel` 의
# `http_file(@tiktoken_o200k_base//file)` 이 sha256 으로 고정하고 패키지는 `tools/requirements_lock.txt`
# 가 고정한다. 그 짝이 ODD 조건 `id:cond-tokenizer-lock` 이고 판정은 파일 해시 대조다.
# 어휘를 `o200k_base` 로 고른 근거는 이 저장소 청크 100개의 실측이다 — 문자/토큰 2.30 으로 `cl100k_base`
# 1.78 · `p50k_base` 0.97 · XLM-R SentencePiece 2.14 를 앞선다. 한글 산문의 토큰 수가 가장 적은 어휘가
# 같은 예산에 가장 많은 지식을 담는다.
# 아래 sha256 은 `MODULE.bazel` 의 http_file 과 같은 값이다. 사본이 둘이므로 동일성은 사람이 아니라
# ODD `CHECKS.tokenizer_lock` 의 명령이 보고, `load_tokenizer` 는 읽은 파일을 이 값으로 대조해 거부한다.
TOKENIZER_NAME = "o200k_base"                 # tiktoken 등록 어휘의 이름 — 패턴도 이 이름의 것을 쓴다
TOKENIZER_PACKAGE = "tiktoken"                # 계수기 패키지 (lock 의 직접 의존)
TOKENIZER_PACKAGE_VERSION = "0.12.0"
TOKENIZER_VOCAB_REPO = "tiktoken_o200k_base"  # MODULE.bazel 의 http_file 이름 (apparent 이름)
# runfiles 디렉토리의 이름은 **canonical 저장소 이름**이다 — `use_repo_rule` 로 만든 저장소는 bzlmod 에서
# `+<규칙 이름>+<저장소 이름>` 이 되고 실측 디렉토리가 `+http_file+tiktoken_o200k_base` 다. apparent 이름만
# 찾으면 인자 없이 부른 runfiles 탐색이 전부 빗나간다 (이 저장소 실측 2026-10-01 — vv_run 이 KB_TOKENIZER_VOCAB
# 를 못 채워 케이스 token-budget·chunk-42-lines 가 자극에 닿기 전에 죽었다). 둘 다 본다.
TOKENIZER_VOCAB_REPO_CANONICAL = f"+http_file+{TOKENIZER_VOCAB_REPO}"
TOKENIZER_VOCAB_FILE = "o200k_base.tiktoken"  # http_file 의 downloaded_file_path
TOKENIZER_VOCAB_SHA256 = "446a9538cb6c348e3516120d7c08b09f57c36495e2acfffe59a5bf8b0cfb1a2d"
TOKENIZER_VOCAB_ENV = "KB_TOKENIZER_VOCAB"    # 어휘 파일 경로의 환경 변수 — bazel 밖 실행의 자리
# o200k_base 의 사전 분할 패턴 — tiktoken 의 등록부(`tiktoken_ext.openai_public`)에서 읽는다. 여기 복제하면
# 정의처가 둘이 되고 패키지 갱신에서 갈린다 (STYLEGUIDE §7 단일 정의처).
```
<!-- 인용 끝 -->
