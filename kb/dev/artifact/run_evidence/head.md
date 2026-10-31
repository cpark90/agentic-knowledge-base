---
id: https://agentic-knowledge-base.dev/id/chunk/06ff52f5-9406-4ead-8685-51db4f0cb144
type: artifact
level: executable
title_ko: 모듈 머리 kind (tools/run_evidence.py)
title: module head kind in tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
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
    from tools.chunk2kg import (ID_BASE, LINK_KEYS, LINK_STATE_CANDIDATE, SPECIALIZATION_KEY, SpecializationError, apply_plane_level_state,
                                body_slots, link_hash, load_plane_level_state, parse_chunk, work_id)
except ImportError:
    import kb_lib
    from chunk2kg import (ID_BASE, LINK_KEYS, LINK_STATE_CANDIDATE, SPECIALIZATION_KEY, SpecializationError, apply_plane_level_state,
                          body_slots, link_hash, load_plane_level_state, parse_chunk, work_id)

KIND = "satisfies"                           # p10-link-types — artifact → decision 의 수평 링크
EVIDENCE_KIND = "agt:runResult"              # evidence-ontology — 검증기·판정 도구의 통과(+) 또는 실패(−)
CONCLUSION_SLOT = "결론"                      # 결정 결론의 본문 표지 (STYLEGUIDE §4)
CASE_DIR = kb_lib.KB_VV + "/case"            # 테스트 케이스의 자리 — vv_run.CASE_DIR 와 같은 값
VERIFIER_DIR = kb_lib.KB_VV + "/verifier"    # 검증기의 자리 — vv_run.VERIFIER_DIR 와 같은 값
# 실행 사슬의 적용 경계 — generated.at 이 이 시각 이후인 실행 기록만 읽는다. 값은 유저 답 Q96-a 가 전달된 시각(answer 0216)이고, 그 앞의 5건은 소급하지 않는다
CHAIN_SINCE = "2026-10-23T17:33:01Z"
POLARITY = {"pass": "+", "fail": "-"}        # 테스트 케이스 판정 → 극성. skip 은 증거가 아니다
_SKIPPED = re.compile(r"(\d+)\s*건너뜀")
_SLUG = re.compile(r"^`([^`]+)`$")

PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 실행 기록(kb/vv/run/)·테스트 케이스·검증기와 코드 파일 단위 지식의 도장이다.
# 생성: tools/run_evidence.py (bazel build //kg:references_kg) — satisfies 후보와 실행 증거 (p9-evidence-ledger-with-belief),
# 확정 링크의 동시 편집·공동 커버 증거 (p10-co-edit-evidence-from-small-commits · p10-link-judgement-evidence),
# 판정 로그의 쌍 행 → 판정 증거와 후보 링크 (p8-judge-session-agreement) — 판정은 반박만 있어도 invalid 가 아니고 낡은 판정은 내지 않는다
# 실행 사슬(테스트 케이스 verifies 결정 × 같은 합격 기준의 검증기 verifies 코드)은 generated.at ≥ {since} 인 실행 기록에만 적용한다 — 그 앞은 소급하지 않는다.
# verify 질의의 실패는 증거로 쓰지 않는다. 동시 편집은 관측 {coedit} 만 읽고 git 을 읽지 않는다
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
"""
```
<!-- 인용 끝 -->
