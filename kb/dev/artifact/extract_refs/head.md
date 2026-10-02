---
id: https://agentic-knowledge-base.dev/id/chunk/1a3482f6-0687-482a-848a-544cab7ed57b
type: artifact
level: executable
title_ko: 모듈 머리 exit-fail (tools/extract_refs.py)
title: module head exit-fail in tools/extract_refs.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-extract-refs}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-19T14:57:33Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
refines: [https://agentic-knowledge-base.dev/id/chunk/55535378-f5cd-4f01-a5ce-54d438529104, https://agentic-knowledge-base.dev/id/chunk/8d09b0e4-44b4-47b2-9ff6-5da9f3b22e12]
part_of: https://agentic-knowledge-base.dev/id/composite/1ddb8a02-e2d5-48e7-a66d-3c960e6a523a
---
**모듈 머리** — `tools/extract_refs.py` 의 모듈 머리 `exit-fail` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:  # 종료 코드 규약의 단일 정의처는 kb_lib — 없으면 같은 값의 폴백 (kb_lib 는 --ontology 때만 필수)
    from tools import kb_lib
except ImportError:
    try:
        import kb_lib
    except ImportError:
        kb_lib = None
try:  # 링크 IRI 규칙(뿌리 uuid · link_hash)과 specializationOf 키의 단일 정의처는 chunk2kg — rdflib 없이 돈다
    from tools.chunk2kg import ID_BASE, LINK_STATE_CANDIDATE, SPECIALIZATION_KEY, SpecializationError, link_hash, work_id
except ImportError:
    from chunk2kg import ID_BASE, LINK_STATE_CANDIDATE, SPECIALIZATION_KEY, SpecializationError, link_hash, work_id
EXIT_FAIL = getattr(kb_lib, "EXIT_FAIL", 1)
EXIT_CONFIG = getattr(kb_lib, "EXIT_CONFIG", 2)
SPECIALIZATION_GATE = getattr(kb_lib, "SPECIALIZATION_GATE", "specialization")

CITE =re.compile(r"\bd-(\d{4})\b")
CONCEPT = re.compile(r"\bagt:([A-Za-z][A-Za-z0-9]*)")
IRI = "https://agentic-knowledge-base.dev/id/chunk-d{}"
AGT = "https://agentic-knowledge-base.dev/agt/"
CANDIDATE_KIND = "cites"  # 후보 링크 개체로 나가는 추출 참조 — usesConcept 는 치역 밖 (모듈 docstring)
EVIDENCE = "agt:constructionRecord"  # 본문의 식별자는 구축 기록이다 (유저 결정 2026-09-12 (b), p10-link-by-construction)

PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 각 청크 본문의 인용·개념 표기다.
# 생성: tools/extract_refs.py (bazel build //kg:references_kg)
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix id: <https://agentic-knowledge-base.dev/id/> .
"""
```
<!-- 인용 끝 -->
