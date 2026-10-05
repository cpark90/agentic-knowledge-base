---
id: https://agentic-knowledge-base.dev/id/chunk/5964aabd-e71d-45eb-95eb-19a32020f049
type: artifact
level: executable
title_ko: 모듈 머리 norm-docs-name (tools/gen_norms.py)
title: module head norm-docs-name in tools/gen_norms.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-norms}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-03T18:12:00Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/aebd48bd-5503-44d2-a028-ca367564d9a2
composite: {id: https://agentic-knowledge-base.dev/id/composite/aebd48bd-5503-44d2-a028-ca367564d9a2, title_ko: 모듈 머리 복합체 norm-docs-name (tools/gen_norms.py), title: section composite norm-docs-name in tools/gen_norms.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/5964aabd-e71d-45eb-95eb-19a32020f049, https://agentic-knowledge-base.dev/id/chunk/e30fe78f-85fa-447c-8ec3-df25166cee41], part_of: https://agentic-knowledge-base.dev/id/composite/29a3a21d-a74b-4fc0-8764-46de4751e58a}
---
**모듈 머리** — `tools/gen_norms.py` 의 모듈 머리 `norm-docs-name` 다. 모듈 머리

**정의** — `GenNormsError` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
    from tools.chunk2kg import (BODY_FENCE, NORM_COLUMNS_KEY, NORM_CONTINUES_KEY, NORM_FORM_DEFAULT, NORM_FORM_KEY,
                                NORM_FORM_TABLE, NORM_LINK_COLUMN_KEY, NORM_DEPTH_KEY, NORM_HEADING_KEY, NORM_ITEMS_KEY, NORM_NUMBERING,
                                NORM_NUMBERED_KEY, NORM_NUMBERING_KEY, NORM_STRENGTH_KEY, NORM_TYPE, ORDERED_KEY, PART_OF_KEY,
                                apply_plane_level_state, load_plane_level_state, norm_bundle_errors, parse_chunk)
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
    from chunk2kg import (BODY_FENCE, NORM_COLUMNS_KEY, NORM_CONTINUES_KEY, NORM_FORM_DEFAULT, NORM_FORM_KEY,
                          NORM_FORM_TABLE, NORM_LINK_COLUMN_KEY, NORM_DEPTH_KEY, NORM_HEADING_KEY, NORM_ITEMS_KEY, NORM_NUMBERING,
                          NORM_NUMBERED_KEY, NORM_NUMBERING_KEY, NORM_STRENGTH_KEY, NORM_TYPE, ORDERED_KEY, PART_OF_KEY,
                          apply_plane_level_state, load_plane_level_state, norm_bundle_errors, parse_chunk)

EXIT_OK, EXIT_FAIL, EXIT_CONFIG = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG
GEN, DRIFT = kb_lib.GEN_NORMS_GATE, kb_lib.NORMS_DRIFT_GATE
NORM_DOCS_NAME = "NORM_DOCS"
NORM_ROOT = "kb/dev/norm"
DECISION_ROOT = "kb/dev/decision"
CONVENTIONS_FILE = kb_lib.DECISION_PART_FILES["conventions"]
CONCLUSION_FILE = kb_lib.DECISION_PART_FILES["conclusion"]
CONVENTION_LINE = re.compile(r"^규약:\s+(.*\S)\s*$")      # 줄 머리 `규약:` — chunk2kg.BODY_SLOT_KEYWORDS 의 같은 표지
STRENGTH = re.compile(r"^\[(지킴|권장)\]\s+(\S.*)$")       # 강도 — 문장의 성질이라 줄 머리에 둔다 (p4-convention-slot)
STRENGTH_DEFAULT = "required"
NORM_NUMBERED_DEFAULT = "true"  # 절 청크의 `numbered` — false 인 depth 2 절(부록)은 번호 없이 낸다
MD_LINK = re.compile(r"(!?\[[^\]\n]*\]\()([^)\s]+)(\))")  # 인라인 링크·그림 — 대상만 다시 계산한다. 텍스트는 코드 스팬을 담을 수 있다
URL_SCHEME = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
NOTICE_TARGET = "//:norms_drift_test"
```
<!-- 인용 끝 -->
