---
id: https://agentic-knowledge-base.dev/id/chunk/d456c76a-43ad-49f5-b73e-ca32721dd5ec
type: artifact
level: executable
title_ko: 모듈 머리 tag (tools/link.py)
title: module head tag in tools/link.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-link}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/b28a66c9-4140-4beb-bb95-69e12a91e607
---
**모듈 머리** — `tools/link.py` 의 모듈 머리 `tag` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # bazel runfiles: 워크스페이스 루트가 sys.path 에 있다
except ImportError:
    import kb_lib  # 직접 실행: 스크립트 디렉토리 기준
from chunk2kg import LINK_KEYS, RESTORED_KEY  # noqa: E402 — frontmatter 링크 키의 단일 정의처

AGT, PROV = kb_lib.AGT, kb_lib.PROV
EXIT_OK, EXIT_CONFIG = kb_lib.EXIT_OK, kb_lib.EXIT_CONFIG
TAG = kb_lib.LINK_TAG
LEVELS = ["functional", "abstract", "logical", "concrete", "executable"]  # defs/kb.bzl 와 같은 순서 (6.2절 정제 계층)
PLANES = ["requirement", "decision", "contract", "schema", "artifact", "annotation", "memory"]  # 5.2절 단방향 순서
RELATED_KEYS = ("coUpdatesWith", "conflictsWith", "relatedTo", "overlapsWith")  # relatedTo 족 — 이미 이어진 쌍을 가리는 데 쓴다
RELATED = "overlapsWith"  # 칸이 없을 때의 종류 — relatedTo 자신이 아니라 그 아래 약한 잎이다 (overlap-ontology)
# 증거 종류의 강도 — 검사 가능성 순 (evidence-ontology, p10-link-judgement-evidence). 작을수록 강하다
EVIDENCE_RANK = {"constructionRecord": 0, "testCoverage": 1, "proposal": 2}
# 한 TIM 칸에 종류가 여럿일 때의 우선순위 — 정제가 먼저, 다음 의미 의존, serves 는 refines 의 약한 형태, verifies 는 vnv 가 적는다
KIND_PREFERENCE = ("refines", "derivesFrom", "satisfies", "constrains", "serves", "verifies", "allocates", "generates")
# 탈락 사유 — 요약의 분포 열쇠
R_SELF, R_DEPRECATED, R_SIBLING, R_LINKED = "자기 자신(같은 단위)", "deprecated", "복합체 형제", "이미 링크됨"
R_DIRECTION, R_CROSS_KB, R_CAP = "TIM 칸은 있으나 단방향·수준 규칙 위반", "KB 가로지름 (overlapsWith 불가 — verifies 뿐)", "상한 k 초과"
# 구조상 채택될 수 없는 후보 — 위반 사유가 곧 탈락 사유다 (docstring 제약 (가)~(다))
R_CROSS_LINK = "KB 가로지름 링크 (KB 사이 링크는 verifies 뿐 — 목표 → 요구 derivesFrom 만 예외)"
R_CODE_PART = "코드 부분 청크가 끝점 (링크는 파일 복합체에)"
R_CASE_DERIVES = "케이스의 derivesFrom (생성기가 자기 시나리오로 쓴다)"
STRUCTURAL = (R_CROSS_LINK, R_CASE_DERIVES)
```
<!-- 인용 끝 -->
