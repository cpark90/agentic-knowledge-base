---
id: https://agentic-knowledge-base.dev/id/chunk/6fcb9067-8131-4868-8b29-752ae0babca5
type: artifact
level: executable
title_ko: 절 decision-role-markers (tools/kb_lib.py)
title: section decision-role-markers in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/163f6311-4c7b-4d2d-983e-94afa5658211
---
**절** — `tools/kb_lib.py` 의 절 `decision-role-markers` 다. 결정의 역할 표지 (STYLEGUIDE §4, 게이트 id `decision-role` — chunk_lint)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 결정의 역할 표지 (STYLEGUIDE §4, 게이트 id `decision-role` — chunk_lint) ────────────────────────────────
# type: decision 인 .md 의 본문 첫 산문 줄은 굵은 역할 표지로 시작한다. 파일 stem 이 표지를 정하고, stem 이 역할 이름이
# 아닌 결정 파일은 받지 않는다 — 단일 파일 꼴은 마지막 시나리오가 세 항목으로 나뉘어 0건이 됐다(유저 답 Q-0061 Q147-a). 표지와 한정어("**대안 없음**"·"**대안 — 미확정**"·"**대안(미해결)**")의
# 판정은 방출과 같은 `body_slot_mark`(chunk2kg) 하나다 (p4-slot-marker-by-position) — 첫 실행(2026-09-13) 대안 21/187 이 한정어
# 형태였고 그것은 "대안 없음"을 기록하라는 규칙(노트 7.4절)의 이행이지 표지 누락이 아니다 (p6-mass-fail-suspects-the-rule).
# 넷째 `conventions` 는 선택 규약이다 (p4-convention-slot, 유저 답 Q22-b) — 있으면 첫 산문 줄이 **규약** 이고 셋의 검사는 그대로다
DECISION_ROLE_MARKERS = {"conclusion": "결론", "rationale": "근거", "alternatives": "대안", "conventions": "규약"}
# V&V 시나리오의 역할 표지 (결정 p8-scenario-authoring) — 시나리오는 `decision`(vv) 복합체이고 결론·근거·대안이 각각
# 자극·요인·배제 자극이다. 표지 낱말만 갈리고 슬롯은 결정의 셋 그대로다(SCENARIO_ROLE_TO_DECISION_SLOT) — 그래서
# shape 는 결정의 본문 틀(decision-body-shapes.ttl)에 대안 셋을 더한 것이고 새 틀이 아니다.
# 파일명 규약은 `<슬러그>-stimulus.md`·`<슬러그>-factors.md`·`<슬러그>-excluded.md` 이고 선언 단위 지식(타깃 이름)은 stimulus 다.
# **규약이 걸리는 자리를 V&V 시나리오 패키지로 한정한다** — 접미만 보면 옛 결정 트리에 있던 결정(후속은 p8-defect-factor-taxonomy)
# 의 stem 이 `-factors` 로 끝나 표지가 결론에서 요인으로 뒤바뀐다(측정). 시나리오 실체의 패키지는 kb/vv/scenario 다.
SCENARIO_DIR = "scenario"  # gen_build.VV_PKGS 의 키 — V&V 시나리오 실체의 패키지 이름
SCENARIO_ROLE_MARKERS = {"stimulus": "자극", "factors": "요인", "excluded": "배제 자극"}
SCENARIO_ROLE_TO_DECISION_SLOT = {"자극": "결론", "요인": "근거", "배제 자극": "대안"}
# 부류 셋을 한 파일에 담은 단일 파일 시나리오(이행기의 꼴)는 받지 않는다. 그 꼴의 마지막 항목 risk-grade-scale 이 2026-10-24
# 세 항목으로 나뉜 뒤 결론 표지로 떨어지는 기본값을 지웠다(유저 답 Q-0061 Q147-a) — 받아들이는 꼴이 줄었고 검사는 좁아졌다.
```
<!-- 인용 끝 -->
