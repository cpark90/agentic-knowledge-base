---
id: https://agentic-knowledge-base.dev/id/chunk/6fcb9067-8131-4868-8b29-752ae0babca5
type: artifact
level: executable
title_ko: 절 decision-role-gate (tools/kb_lib.py)
title: section decision-role-gate in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/163f6311-4c7b-4d2d-983e-94afa5658211
---
**절** — `tools/kb_lib.py` 의 절 `decision-role-gate` 다. 결정의 역할 표지 (STYLEGUIDE §4, 게이트 id `decision-role` — chunk_lint)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 결정의 역할 표지 (STYLEGUIDE §4, 게이트 id `decision-role` — chunk_lint) ────────────────────────────────
# type: decision 인 .md 의 본문 첫 산문 줄은 굵은 역할 표지로 시작한다. 세 파일 결정은 파일 stem 이 표지를 정하고, 단일 파일 옛 결정
# (chunks/decision/d-*.md)은 결론 표지만 요구한다. 표지 안의 한정어("**대안 없음**"·"**대안 — 미확정**"·"**대안(미해결)**")는 같은 역할
# 표지로 본다 — 첫 실행(2026-09-13) 결론 187/187·근거 187/187 은 맨 표지, 대안 21/187 이 한정어 형태였고 그것은 "대안 없음"을 기록하라는
# 규칙(노트 7.4절)의 이행이지 표지 누락이 아니다 (p6-mass-fail-suspects-the-rule). 굵은 span 이 역할 낱말로 시작하지 않으면 위반이다
DECISION_ROLE_GATE = "decision-role"
DECISION_ROLE_MARKERS = {"conclusion": "결론", "rationale": "근거", "alternatives": "대안"}
DECISION_SINGLE_FILE_MARKER = "결론"
# V&V 시나리오의 역할 표지 (결정 p8-scenario-authoring) — 시나리오는 `decision`(vv) 복합체이고 결론·근거·대안이 각각
# 자극·요인·배제 자극이다. 표지 낱말만 갈리고 슬롯은 결정의 셋 그대로다(SCENARIO_ROLE_TO_DECISION_SLOT) — 그래서
# shape 는 결정의 본문 틀(decision-body-shapes.ttl)에 대안 셋을 더한 것이고 새 틀이 아니다.
# 파일명 규약은 `<슬러그>-stimulus.md`·`<슬러그>-factors.md`·`<슬러그>-excluded.md` 이고 선언 청크(타깃 이름)는 stimulus 다.
# **규약이 걸리는 자리를 V&V 시나리오 패키지로 한정한다** — 접미만 보면 옛 결정 `chunks/decision/d-0140-three-defect-factors.md`
# 의 stem 이 `-factors` 로 끝나 표지가 결론에서 요인으로 뒤바뀐다(실측). 시나리오 실체의 패키지는 kb/vv/scenario 다.
SCENARIO_DIR = "scenario"  # gen_build.VV_PKGS 의 키 — V&V 시나리오 실체의 패키지 이름
SCENARIO_ROLE_MARKERS = {"stimulus": "자극", "factors": "요인", "excluded": "배제 자극"}
SCENARIO_ROLE_TO_DECISION_SLOT = {"자극": "결론", "요인": "근거", "배제 자극": "대안"}
# 단일 청크 시나리오(부류 셋을 한 파일에 담은 이행기의 형태)는 stem 이 세 접미 밖이므로 결론 표지로 계속 통과한다 —
# 기존 허용의 유지이고 약화가 아니다. 세 청크로 다시 쓰면 그때부터 세 표지가 강제된다.
DECISION_ROLE_MARKER = re.compile(
    r"^\s*\*\*(" + "|".join(sorted(set(DECISION_ROLE_MARKERS.values()) | set(SCENARIO_ROLE_MARKERS.values()),
                                  key=len, reverse=True)) + r")[^*\n]*\*\*")
```
<!-- 인용 끝 -->
