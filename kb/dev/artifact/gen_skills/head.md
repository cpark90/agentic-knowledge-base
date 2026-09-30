---
id: https://agentic-knowledge-base.dev/id/chunk/c29ecdfb-152c-44e9-b18d-b86fbe44d561
type: artifact
level: executable
title_ko: 모듈 머리 py-binary (tools/gen_skills.py)
title: module head py-binary in tools/gen_skills.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-skills}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
verified: [{by: process:bazel-test, at: 2026-09-30T10:45:28Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
part_of: https://agentic-knowledge-base.dev/id/composite/826eea39-5afc-41d4-a5cc-4afd24c0f0b2
---
**모듈 머리** — `tools/gen_skills.py` 의 모듈 머리 `py-binary` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
HEADING, slug = kb_lib.MD_HEADING, kb_lib.slug  # GitHub 제목 앵커 규칙의 단일 정의처는 kb_lib (STYLEGUIDE §7)

EXIT_OK, EXIT_FAIL, EXIT_CONFIG = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG
GEN, DRIFT = kb_lib.GEN_SKILLS_GATE, kb_lib.SKILLS_DRIFT_GATE
PY_BINARY = re.compile(r'py_binary\(\s*name\s*=\s*"([\w-]+)"')
# `사용:` 줄 — 줄머리(콜론 없어도 된다: "사용  doccheck.py …") 또는 줄 가운데의 "사용: …". 블록은 뒤따르는 들여쓴 줄까지다
USAGE = re.compile(r"^사용[:：]?(?=\s|$)|사용[:：]\s*")
NOTICE = kb_lib.gendoc_tree_notice("도구 docstring 과 `kb_lib.SKILLS`", "//:skills_drift_test")
DOCS_DIR = "docs"
TOOLS_DIR = "tools"
RESOLVE_ANCHOR = "게이트-총람--이-문서가-원본이다"  # docs/tools.md 의 총람 — `해소` 열이 FAIL [<id>] 의 해소다
```
<!-- 인용 끝 -->
