---
id: https://agentic-knowledge-base.dev/id/chunk/8013f604-8091-4bcf-aa5e-9a4a96aa15f1
type: artifact
level: executable
title_ko: 모듈 머리 chunk-dirs (tools/revalidate.py)
title: module head chunk-dirs in tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/974f7eff-3756-4a18-af98-04c75441cd70
---
**모듈 머리** — `tools/revalidate.py` 의 모듈 머리 `chunk-dirs` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib  # noqa: E402
except ImportError:
    import kb_lib  # noqa: E402 — 생성 문서 규약(머리 블록·빈 값 표기)의 단일 정의처
from chunk2kg import (ID_BASE, SPECIALIZATION_KEY, SpecializationError, apply_plane_level_state,  # noqa: E402
                      link_hash, load_plane_level_state, parse_chunk, work_id)
from chunk2kg import LINK_KEYS as OBJECT_LINK_KEYS  # noqa: E402 — 링크 개체(agt:Link)를 내는 키. assumes·part_of 는 개체가 없다

CHUNK_DIRS = ("kb", "chunks")
USES_KEY = kb_lib.USES_KEY  # 정의 → 정의 (agt:usesDefinition, 치역은 같은 모듈 + USES_TARGETS). `호출부` 열의 입력이다
# frontmatter 의 링크 키 — 목록 값. part_of 는 스칼라
LINK_KEYS = ("refines", "serves", "supersedes", "verifies", "assumes", "satisfies", "constrains", "derivesFrom", "allocates",
             "coUpdatesWith", "overlapsWith")
# 하류 조회가 세는 타깃 종류 — 복합체 묶음(kb_composite)이 빠지면 추출된 코드 청크의 rdeps 가 늘 0 이다
ITEM_KINDS = "kb_chunk|kb_decision|kb_composite"
```
<!-- 인용 끝 -->
