---
id: https://agentic-knowledge-base.dev/id/chunk/06ff52f5-9406-4ead-8685-51db4f0cb144
type: artifact
level: executable
title_ko: 모듈 머리 kind (tools/run_evidence.py)
title: module head kind in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T05:47:19Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/27628b6a-73ec-4466-bb12-a1a1ae970dd7
---
**모듈 머리** — `tools/run_evidence.py` 의 모듈 머리 `kind` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib
    from tools.chunk2kg import (ID_BASE, LINK_STATE_CANDIDATE, SPECIALIZATION_KEY, SpecializationError, apply_plane_level_state,
                                body_slots, link_hash, load_plane_level_state, parse_chunk, work_id)
except ImportError:
    import kb_lib
    from chunk2kg import (ID_BASE, LINK_STATE_CANDIDATE, SPECIALIZATION_KEY, SpecializationError, apply_plane_level_state,
                          body_slots, link_hash, load_plane_level_state, parse_chunk, work_id)

KIND = "satisfies"                           # p10-link-types — artifact → decision 의 수평 링크
EVIDENCE_KIND = "agt:runResult"              # evidence-ontology — 검증기·판정 도구의 통과(+) 또는 실패(−)
CONCLUSION_SLOT = "결론"                      # 결정 결론의 본문 표지 (STYLEGUIDE §4)
CASE_DIR = kb_lib.KB_VV + "/case"            # 케이스의 자리 — vv_run.CASE_DIR 와 같은 값
POLARITY = {"pass": "+", "fail": "-"}        # 케이스 판정 → 극성. skip 은 증거가 아니다
_SKIPPED = re.compile(r"(\d+)\s*건너뜀")
_SLUG = re.compile(r"^`([^`]+)`$")

PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 실행 기록(kb/vv/run/)·케이스·검증기와 코드 파일 청크의 도장이다.
# 생성: tools/run_evidence.py (bazel build //kg:references_kg) — satisfies 후보와 실행 증거 (p9-evidence-ledger)
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
"""
```
<!-- 인용 끝 -->
