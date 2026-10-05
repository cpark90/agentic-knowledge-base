---
id: https://agentic-knowledge-base.dev/id/chunk/47cbe988-791e-493e-b71c-1671f649b23a
type: artifact
level: executable
title_ko: 모듈 머리 gate (tools/tokens.py)
title: module head gate in tools/tokens.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-tokens}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-01T16:05:21Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/4fe35c96-c167-4a3e-b640-a888f6bcefe5
---
**모듈 머리** — `tools/tokens.py` 의 모듈 머리 `gate` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import chunk_lint, kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import chunk_lint  # 직접 실행: 스크립트 디렉토리 기준
    import kb_lib

EXIT_OK, EXIT_FAIL, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP
GATE = kb_lib.TOKENS_TAG  # 보고 접두 — 이 도구는 게이트 타깃이 아니다 (상한의 강제는 chunk_lint·token-budget 이다)
CHUNK_ROOTS = ("chunks", "kb/dev", "kb/vv", "kb/ontology", "space")  # 인자가 없을 때 훑는 자리 — 청크가 사는 디렉토리
# 온톨로지 모듈과 shape 은 `.ttl` 청크다 — 같은 크기 규칙을 받으므로(chunk_lint 가 `--chunks` 로 받는다)
# 실측의 분모도 그것을 담아야 한다 (2026-10-01 정정: `.md` 만 훑어 TTL 청크 78개가 분모에서 빠져 있었다).
# TTL 청크의 판별은 접미사 규약이고 정의처는 `kb_lib.ALLOWED_TTL_SUFFIXES` 의 저작 접미 둘이다 — `-kg`·`-odd`·
# `-space` 는 생성물이라 청크가 아니다.
TTL_CHUNK_SUFFIXES = ("-ontology", "-rules", "-shapes")
MULTIPLES = 20          # 42의 배수를 몇 개까지 보는가 — 42×1 … 42×20
LINE_BUDGET_LINES = 200  # 환산의 분모가 된 옛 예산의 줄 수 (d-0002 "42줄은 200줄의 1/5") — 지금 예산은 토큰이다
BUDGET_PLANES = ("requirement", "decision")  # 줄당 토큰의 표본 — 저작된 산문의 plane 이다
VIEW_PLANES = 5  # 조망 단위 — 한 번에 4~5개를 조망한다 (노트 949행). 예산 ÷ 이 수가 상한의 한 근거다
TOP_N = 20
```
<!-- 인용 끝 -->
