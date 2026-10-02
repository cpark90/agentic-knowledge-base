---
id: https://agentic-knowledge-base.dev/id/chunk/c767c9b6-7391-4c5f-b482-89293d8895ee
type: artifact
level: executable
title_ko: 모듈 머리 grades (tools/assume_check.py)
title: module head grades in tools/assume_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-assume-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/9f79d119-83cf-46a7-89c0-680e8f203296, https://agentic-knowledge-base.dev/id/chunk/79bcc1dd-4036-43ef-b30d-f4dff07be513, https://agentic-knowledge-base.dev/id/chunk/b36581f8-2688-46dc-9b44-3e1019a37d66]
part_of: https://agentic-knowledge-base.dev/id/composite/169b7deb-a7ef-4d53-9f52-ad8abd5d4c3a
---
**모듈 머리** — `tools/assume_check.py` 의 모듈 머리 `grades` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
import kb_lib  # noqa: E402 — 네임스페이스·종료 코드의 단일 정의처
from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # noqa: E402 — 실제 의존 집합은 frontmatter 를 그래프와 독립적으로 읽는다
from odd_check import judge_all, load_odd  # noqa: E402 — 조건 판정은 odd_check 와 같은 함수

AGT, ID = kb_lib.AGT, kb_lib.ID
EXIT_OK, EXIT_FAIL, EXIT_CONFIG, EXIT_SKIP = kb_lib.EXIT_OK, kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG, kb_lib.EXIT_SKIP
GRADES = "ABCD"  # 판정 방법 등급 (3.9절) — 뒤로 갈수록 약하다. 연언의 등급은 최저 = 가장 뒤의 글자
# 전파에 쓰는 링크 — 청크 → 청크 (verifies 는 V&V 청크가 주어라 아직 없다). 방향: 주어가 목적어에 의존한다
PROPAGATE = [AGT.refines, AGT.serves, AGT.supersedes, AGT.cites, AGT.coUpdatesWith, AGT.overlapsWith]
# 기본 그래프 — `bazel run` 의 작업 디렉토리(runfiles)에 data 로 놓인다. 없으면 워크스페이스의 bazel-bin·소스에서 찾는다
DEFAULT_TTL = ["kg/chunks-kg.ttl", "kg/references-kg.ttl", "kg/base-kg.ttl", "kg/catalog-kg.ttl", "kg/composite-kg.ttl",
               "kb/odd/project-odd.ttl", "space/design-space.ttl"]  # 설계 공간의 후보 링크도 `when` 을 갖는다
CHUNK_DIRS = ("kb", "chunks")
MEMORY_DIR = "kb/dev/memory"
ODD_IRI = str(ID["odd-agentic-knowledge-base"])  # 관측의 출처 — ODD 개체 (base-kg 에 doc- 개체가 없다)
DEFAULT_ASSUMPTION = str(ID["asm-chunk-conventions"])
GENERATOR = kb_lib.ASSUME_CHECK_GENERATOR  # 관측의 generated.by — 정의처는 kb_lib (weave audit · metrics 가 같은 값으로 관측을 고른다)
```
<!-- 인용 끝 -->
