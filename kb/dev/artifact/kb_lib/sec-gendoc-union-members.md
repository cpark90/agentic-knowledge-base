---
id: https://agentic-knowledge-base.dev/id/chunk/e3781341-dacf-4bdc-a798-ec3dcfb231a7
type: artifact
level: executable
title_ko: 절 gendoc-union-members (tools/kb_lib.py)
title: section gendoc-union-members in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6b2ef1c0-06f1-44c5-9b0f-6ba8a1fedb8d
composite: {id: https://agentic-knowledge-base.dev/id/composite/6b2ef1c0-06f1-44c5-9b0f-6ba8a1fedb8d, title_ko: 절 복합체 gendoc-union-members (tools/kb_lib.py), title: section composite gendoc-union-members in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/e3781341-dacf-4bdc-a798-ec3dcfb231a7, https://agentic-knowledge-base.dev/id/chunk/0b2c0543-8f0e-4ad8-a18a-eb3da5ff4767, https://agentic-knowledge-base.dev/id/chunk/63c8b052-77ba-4c50-bc59-9b1fea9e598d, https://agentic-knowledge-base.dev/id/chunk/d5a80e19-21cd-4de4-b68c-641a875cd7de, https://agentic-knowledge-base.dev/id/chunk/aac10f80-c526-4fab-ad8f-e93b193438f3], part_of: https://agentic-knowledge-base.dev/id/composite/9b61f2e4-e29d-4fe0-8a4f-f1be5708e79a}
---
**절** — `tools/kb_lib.py` 의 절 `gendoc-union-members` 다. union 구성과 증분 — 머리 `입력` 줄의 트리플 수를 구성원별 몫으로 가른다 (G4, 유저 답 Q40-a)

**정의** — `_gendoc_graph_triples` · `gendoc_union` · `gendoc_union_errors` · `input_fingerprint` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── union 구성과 증분 — 머리 `입력` 줄의 트리플 수를 구성원별 몫으로 가른다 (G4, 유저 답 Q40-a) ─────────────

# union 구성의 이름 — 같은 이름의 수치가 도구마다 갈리는 이유를 머리 블록 안에 남긴다 (현상 P21 의 관측 수단, vnv 설계 2026-09-29).
# 구성을 밝히지 않으면 트리플 수가 다른 것이 결함인지 구성 차이인지 문서만 보고 가릴 수 없다 — 참조 저장소 R5 가 그 형태다.
# 순서는 선언 순서이고(경로 정렬이 아니다) 표에 없는 그래프 파일은 stem 으로 뒤에 붙는다 — 구성원을 숨기지 않는다.
# 구성원마다 **증분**을 붙인다 (유저 답 Q40-a, 2026-10-04): 선언 순서대로 앞 구성원들의 합집합에 더한 트리플 수다. 구성원 단독
# 크기가 아니다 — 구성원끼리 트리플이 겹치므로 단독 크기의 합은 총수가 아니다. 증분의 합은 총수와 같고 G4 가 그것을 판정한다.
GENDOC_UNION_MEMBERS = (
    ("kg/chunks-kg.ttl", "chunks"),
    ("kg/base-kg.ttl", "base"),
    ("kg/catalog-kg.ttl", "catalog"),
    ("kg/composite-kg.ttl", "composite"),
    ("kg/references-kg.ttl", "references"),
    ("kb/odd/", "odd"),
    ("kb/ontology/", "ontology"),
    ("space/", "space"),
    ("kg/gates-kg.ttl", "gates"),
)
GENDOC_UNION_UNREAD = "?"  # 읽지 못한 구성원의 증분 자리 — 합이 총수와 갈려 G4 가 FAIL 로 드러낸다
GENDOC_UNION_RE = re.compile(r"트리플 (\d+) \(union: ([^)]*)\)")
GENDOC_UNION_PART_RE = re.compile(r"(\S+) \+(\d+)")
_GENDOC_TRIPLES: dict[str, frozenset] = {}  # 그래프 파일 → 트리플 집합. 한 프로세스에서 같은 파일을 두 번 파싱하지 않는다
```
<!-- 인용 끝 -->
