---
id: https://agentic-knowledge-base.dev/id/chunk/b93fb4b9-164c-4311-b61e-f0c87ace4e3e
type: artifact
level: executable
title_ko: 절 round-prefix (tools/vv_run.py)
title: section round-prefix in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/d4585999-3733-43ec-b6f4-d65181e989ce
composite: {id: https://agentic-knowledge-base.dev/id/composite/d4585999-3733-43ec-b6f4-d65181e989ce, title_ko: 절 복합체 round-prefix (tools/vv_run.py), title: section composite round-prefix in tools/vv_run.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/b93fb4b9-164c-4311-b61e-f0c87ace4e3e, https://agentic-knowledge-base.dev/id/chunk/fae9d002-8656-4bb1-a04e-18a04452ff08, https://agentic-knowledge-base.dev/id/chunk/cad21a57-2adb-46fe-b8c7-82cd106906ed, https://agentic-knowledge-base.dev/id/chunk/2393909a-601a-49e0-bc99-833dc33318cb, https://agentic-knowledge-base.dev/id/chunk/f0e6f002-4d5d-46c0-abba-ab242b4572e4, https://agentic-knowledge-base.dev/id/chunk/9cb93d1c-7ae3-49f8-8812-213367f8a3e4, https://agentic-knowledge-base.dev/id/chunk/d213b57a-b3ec-4271-aba1-114f98f7a4c7, https://agentic-knowledge-base.dev/id/chunk/9f97f1c4-3974-4cf9-a2d7-d09597311cae], part_of: https://agentic-knowledge-base.dev/id/composite/5fc8dfb1-4583-4c27-8266-44c34557e4c1}
---
**절** — `tools/vv_run.py` 의 절 `round-prefix` 다. 라운드 경계 기록 (유저 답 Q39-c)

**정의** — `as_utc` · `round_records` · `defect_times` · `round_counts` · `round_observation` · `record_round` · `main` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 라운드 경계 기록 (유저 답 Q39-c) ────────────────────
# 라운드 경계는 날짜가 아니라 명시 기록이다. `--round <사유>` 가 라운드 하나를 닫으며 실행 기록과 같은 자리(memory, append-only)에
# `round-<UTC>.md` 를 남긴다 — 라운드 번호 · 구간 안 신규 결함 수 · 종료 사유. 종료 사유의 어휘는 온톨로지
# `kb/ontology/related/state/round-end-reason-ontology.ttl` 의 개체 셋이고 기록 본문이 그중 하나를 인용한다(agt:usesConcept 로 그래프에 선다).
# 정지 규칙의 판정은 verify 질의 `round-stop-rule-violated` 가 그래프에서 하고, `weave` audit 의 라운드 절이 이 기록으로 구간을 자른다
ROUND_PREFIX = "round-"  # 파일명 round-<UTC>.md — run-·judge- 와 한 디렉토리에서 갈린다 (kb_lib 로 옮길 후보)
VERDICT_DIR = kb_lib.KB_VV + "/verdict"  # 신규 결함 = 이 자리의 판정 주석 (weave audit 판정 주석 절과 같은 대상)
ROUND_REASONS = {  # --round 값 → (종료 사유 개체, 라벨 ko, 라벨 en). 라벨의 정의처는 온톨로지다 — 여기는 기록 제목에 옮겨 적을 뿐이다
    "stop-rule": ("agt:roundEndedByStopRule", "정지 규칙", "stop rule"),
    "budget": ("agt:roundEndedByBudget", "예산 소진", "budget exhaustion"),
    "complete": ("agt:roundEndedByCompletion", "완료", "completion"),
}
ROUND_TABLE_HEADER = "| 라운드 | 구간 시작 | 구간 끝 | 신규 결함 | 종료 사유 |"
STOP_RULE_QUERY = "round-stop-rule-violated"  # tools/verify-queries/ 의 정지 규칙 질의 이름
















if __name__ == "__main__":
    raise SystemExit(main())
```
<!-- 인용 끝 -->
