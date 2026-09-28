# waivers — 게이트 면제 선언 (원본)

면제는 코드에 숨기지 않고 여기에 선언한다 — "오탐은 침묵이 아니라 선언으로"(agrtls 공통 규칙, 유저 채택 2026-09-12 C).
도구는 이 표를 읽어(`tools/kb_lib.py` `load_waivers`) 면제 대상을 **집계에서 빼되 목록에는 남긴다**. 축은 셋 — `파일`(경로),
`stem`(파일 이름 줄기), `상태`(예: `deprecated`). 게이트 id는 [`tools.md`](tools.md) 총람의 `id` 열. ODD의 `EXCLUSIONS_REVIEWED`가
같은 패턴의 선례다. 면제를 더하는 것은 검사 약화이므로 판정자 열이 비어 있으면 안 된다.

| 게이트 id | 대상 | 축 | 사유 | 판정자 | 날짜 |
|---|---|---|---|---|---|
| channel | docs/feedback/README.md · docs/feedback/TEMPLATE.md · docs/feedback/purpose-statement.md · docs/feedback/agents/README.md · docs/feedback/inquiries/README.md · docs/feedback/handoff/README.md | 파일 | 규약 문서·양식·원장은 반영 항목이 아니다 (옛 `channel_lint.EXEMPT`) | orchestrator | 2026-09-12 |
| term-drift | kb/dev/decision/pe-storage-layout/conclusion.md | 파일 | 본문의 `verifier/`는 디렉토리명 — 옛 표기가 아니다 (consistency ⑥) | orchestrator | 2026-09-12 |
| prose | docs/references.md | 파일 | 도구 이름 "OOPS!"의 느낌표 — 고유명사 | orchestrator | 2026-09-13 |
| empty-value | kb/dev/decision/p9-uncertainty-as-link-uncertainty/conclusion.md | 파일 | 본문의 "값이 미정인 것처럼 보이는 경우"는 빈 값 표기가 아니라 낱말의 산문 용법이다 (⑧ 빈 값 이상 표기) | orchestrator | 2026-09-22 |
| term-drift | kb/vv/verifier/vv-run-executor.md | 파일 | 본문의 `verifier`는 결정 슬러그 `p8-verifier-env-isolation`(식별자)와 영문 `title:`뿐이다 — 옛 표기의 산문 용법이 아니라 부분 문자열 오탐이다 (consistency ⑥) | orchestrator | 2026-09-26 |
| gendoc | bazel-bin/kg/revalidate.md | 파일 | `revalidate`는 리비전 대비 차이라 입력 지문(G4)을 내지 않는다 — 두 리비전의 차이는 하나의 입력 집합이 아니다. 머리의 `입력` 줄이 그 사실을 `input_note`로 선언한다 | orchestrator | 2026-09-27 |
