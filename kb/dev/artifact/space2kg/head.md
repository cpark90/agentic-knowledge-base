---
id: https://agentic-knowledge-base.dev/id/chunk/06619efb-02eb-4124-9d89-7e2245f5d90c
type: artifact
level: executable
title_ko: 모듈 머리 gate (tools/space2kg.py)
title: module head gate in tools/space2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-space2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/89a47e26-d93e-47e7-ae74-ba6e801d1d5a
---
**모듈 머리** — `tools/space2kg.py` 의 모듈 머리 `gate` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
import chunk2kg  # noqa: E402 — frontmatter 파서·링크 IRI 규칙의 정의처

try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # noqa: E402 — 직접 실행: 스크립트 디렉토리 기준

GATE = kb_lib.SPACE_GATE
EXIT_FAIL, EXIT_CONFIG = kb_lib.EXIT_FAIL, kb_lib.EXIT_CONFIG
BODY_KEYS = ("variable", "status", "candidates", "constraints", "preferences")
CANDIDATE_KEYS = ("to", "state", "when", "evidence", "eliminated_by")
EVIDENCE_KEYS = ("kind", "ref")
# 증거 종류 — evidence-ontology 의 살아 있는 개체 (폐기된 counterfactualTest 는 뺀다)
EVIDENCE_KINDS = ("constructionRecord", "coEditHistory", "testCoverage", "runResult", "proposal",
                  "embeddingSimilarity", "coRead")
PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 각 `-space` 청크의 frontmatter 와 본문이다.
# 생성: tools/space2kg.py (bazel build //space:design_space)
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
"""
```
<!-- 인용 끝 -->
