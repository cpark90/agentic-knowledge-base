---
id: https://agentic-knowledge-base.dev/id/chunk/7e6ee13b-33d6-454c-80a4-0153fd8aeb90
type: artifact
level: executable
title_ko: 모듈 머리 actor (tools/case_gen.py)
title: module head actor in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T14:43:34Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/1a0a0d9e-abcb-46ca-bf5b-d530a350816e
composite: {id: https://agentic-knowledge-base.dev/id/composite/1a0a0d9e-abcb-46ca-bf5b-d530a350816e, title_ko: 모듈 머리 복합체 actor (tools/case_gen.py), title: section composite actor in tools/case_gen.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/7e6ee13b-33d6-454c-80a4-0153fd8aeb90, https://agentic-knowledge-base.dev/id/chunk/b23dee78-99ba-49f8-bcde-88ea157cbe7a], part_of: https://agentic-knowledge-base.dev/id/composite/6038262a-0bc8-4f38-bb62-357c9eaeece2}
---
**모듈 머리** — `tools/case_gen.py` 의 모듈 머리 `actor` 다. 모듈 머리

**정의** — `CaseGenError` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib, vv_run  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
    from tools.chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
    import vv_run
    from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk

EXIT_OK, EXIT_FAIL, EXIT_CONFIG = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG
GEN, DRIFT = kb_lib.CASE_GEN_GATE, kb_lib.CASE_DRIFT_GATE
ACTOR = kb_lib.CASE_GEN_ACTOR  # 케이스의 generated.by — 역할이 아니라 프로세스다. writer 검사 밖이다 (validate check_writer)
SCENARIO_DIR = kb_lib.KB_VV + "/scenario"
CASE_DIR = kb_lib.KB_VV + "/case"
RUN_DIR = kb_lib.VV_RUN_DIR
ODD_FILE = "kb/odd/project-odd.yml"
CHUNK_NS = str(kb_lib.ID) + "chunk/"
STIMULUS_SUFFIX = "-stimulus"
INPUT_HEAD = (re.compile(r"^keep\s*:", re.M), re.compile(r"^cover\s*:", re.M))  # 두 키가 다 있는 펜스만 입력이다
INPUT_KEYS = ("keep", "cover", "seed", "case")
VAR_NAME = re.compile(r"[a-z][a-z0-9_]*")
VAR_KEYS = ("odd", "range", "values", "reject", "domain")
ODD_OUTSIDE = "outside"
RULE_TAGS = {"equivalence": "sampling:equivalence", "boundary": "sampling:boundary", "pairwise": "sampling:pairwise",
             "factor": "sampling:factor", "observed": "sampling:observed"}  # 결정 p8-case-generation 의 근거 태그
RULE_KEYS = {"equivalence": ("vars",), "boundary": ("vars",), "pairwise": ("vars",), "factor": ("var", "factors"),
             "observed": ("run", "values")}
ORIGIN_OBSERVED = "origin:observed"
ODD_OUTSIDE_TAG = "odd:outside"
FACTOR_TAG = re.compile(r"agt:[A-Za-z][A-Za-z0-9]*")
CASE_KEYS = ("criteria", "verifies", "derivesFrom", "title_ko", "title", "summary", "stimulus", "files", "command", "accept", "reject")
CASE_REQUIRED = ("criteria", "title_ko", "title", "summary", "stimulus", "command")
CLASS_KEYS = ("prose", "expect")
CLASSES = ("accept", "reject")
TEMPLATE = re.compile(r"\$\{([^{}\s]*)\}")  # `${변수}` — 셸의 `$(…)`·`$VAR` 와 vv_run 의 `{{이름}}` 은 건드리지 않는다
UNSAMPLED = "표본 근거 없는 케이스다"
```
<!-- 인용 끝 -->
