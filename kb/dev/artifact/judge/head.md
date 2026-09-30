---
id: https://agentic-knowledge-base.dev/id/chunk/8be49e66-32e1-48fa-8df2-5e42684f3eea
type: artifact
level: executable
title_ko: 모듈 머리 agt (tools/judge.py)
title: module head agt in tools/judge.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-judge}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/d3023605-893e-42fb-a22a-3cd1241e45b0]
part_of: https://agentic-knowledge-base.dev/id/composite/9b099dc3-facc-4593-9927-5f2afdd09add
composite: {id: https://agentic-knowledge-base.dev/id/composite/9b099dc3-facc-4593-9927-5f2afdd09add, title_ko: 모듈 머리 복합체 agt (tools/judge.py), title: section composite agt in tools/judge.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/8be49e66-32e1-48fa-8df2-5e42684f3eea, https://agentic-knowledge-base.dev/id/chunk/35cf5136-8348-44b2-8fad-20002523764b, https://agentic-knowledge-base.dev/id/chunk/50114263-78e9-4af8-9078-cd158d3f76eb, https://agentic-knowledge-base.dev/id/chunk/81e5e72c-14de-43e1-ac54-19566c8df95e], part_of: https://agentic-knowledge-base.dev/id/composite/85cd0960-2c5b-4a4c-b5be-bcf71f036c54}
---
**모듈 머리** — `tools/judge.py` 의 모듈 머리 `agt` 다. 모듈 머리

**정의** — `JudgeError` · `at` · `slug` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # noqa: E402 — bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # noqa: E402 — 직접 실행
try:  # noqa: E402 — 대상의 IRI·수준은 frontmatter 파서가 읽는다. 값 어휘의 원본은 defs/kb.bzl 이다 (M1 단일 정의처)
    from tools.chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk
except ImportError:
    from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402
try:  # noqa: E402 — 본문 추출은 label_sample.py 하나가 원본이다(단일 정의처, 2026-09-30 vnv 결함 보고)
    from tools.label_sample import body_of as sample_body_of
except ImportError:
    from label_sample import body_of as sample_body_of  # noqa: E402

AGT = kb_lib.AGT
ID = kb_lib.ID
EXIT_OK, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP
TAG = kb_lib.JUDGE_GATE
GENERATOR = kb_lib.JUDGE_GENERATOR
PROFILE_DIR = kb_lib.JUDGE_PROFILE_DIR
SHAPES = kb_lib.JUDGE_QUESTION_SHAPES
ODD_IRI = str(ID["odd-agentic-knowledge-base"])
ASSUMPTIONS = [str(ID[a]) for a in kb_lib.JUDGE_ASSUMPTIONS]  # 청크 규약 — 판정 서비스 가정은 도입이 되돌려져 없다 (2026-09-30)
MAX_BODY_LINES = 42  # 청크 본문의 상한 (4.1절) — 로그도 청크라 같은 규칙을 받는다
MAX_ROWS = MAX_BODY_LINES - 12  # 로그 한 파일의 판정 행 상한 — 산문 1 + 빈 줄 2 + 표 머리 2 + 요약 1 과 여유를 뺀 나머지
_SLUG = re.compile(r"[^a-z0-9]+")
```
<!-- 인용 끝 -->
