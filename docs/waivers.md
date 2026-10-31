# waivers — 게이트 면제 선언 (원본)

면제는 게이트가 위반으로 판정한 대상을 집계에서 빼도록 선언한 것이고, 이 문서가 그 선언의 원본이다. 면제는 코드에
숨기지 않고 이 표에 선언한다. 근거는 "오탐은 침묵이 아니라 선언으로"라는 agrtls 공통 규칙이다(유저 채택 2026-09-12 C).
도구는 이 표를 `tools/kb_lib.py`의 `load_waivers`로 읽고, 면제 대상을 **집계에서 빼되 목록에는 남긴다**.

면제 대상을 고르는 축은 셋이다. `파일`은 경로이고, `stem`은 파일 이름의 줄기이며, `상태`는 `deprecated` 같은 지식
항목의 상태다. 게이트 id는 [`tools.md`](tools.md) 총람의 `id` 열에 있는 값을 쓴다. ODD의 `EXCLUSIONS_REVIEWED`가 같은
방식의 선례다.

면제는 검사를 약화하는 것이 아니다. 약화는 shape나 게이트 코드를 바꾸는 것만 가리킨다. 반면 면제는 orchestrator가
판정해 이 표에 선언으로 공개하는 것이다(Q7-b, 2026-10-03). 그래서 판정자 열은 비워 둘 수 없다.

| 게이트 id | 대상 | 축 | 사유 | 판정자 | 날짜 |
|---|---|---|---|---|---|
| prose | docs/references.md | 파일 | 도구 이름 "OOPS!"의 느낌표 — 고유명사 | orchestrator | 2026-09-13 |
| empty-value | kb/dev/decision/p9-uncertainty-as-link-uncertainty/conclusion.md | 파일 | 본문의 "값이 미정인 것처럼 보이는 경우"는 빈 값 표기가 아니라 낱말의 산문 용법이다 (⑧ 빈 값 이상 표기) | orchestrator | 2026-09-22 |
| term-drift | kb/dev/decision/p0-terms-from-glossary/conventions.md | 파일 | 옛 표기를 쓰지 않는다고 언급하는 규약 줄 — 쓰임이 아니다 (consistency ⑥, Q71-a) | orchestrator | 2026-10-06 |
| gendoc | bazel-bin/kg/revalidate.md | 파일 | `revalidate`는 리비전 대비 차이라 입력 해시값(G4)을 내지 않는다 — 두 리비전의 차이는 하나의 입력 집합이 아니다. 머리의 `입력` 줄이 그 사실을 `input_note`로 선언한다 | orchestrator | 2026-09-27 |
| chunk | kb/vv/run/judge-20260929T182311Z.md | 파일 | append-only 판정 로그(3,094토큰 > memory 상한 2,856)다 — 기록의 소급 수정은 기록을 다시 쓰는 일이라 분할하지 않는다(r-026, `p0-run-as-observation`). 새 로그는 `judge`가 토큰 상한 안에서 나눈다 | orchestrator | 2026-10-01 |
| shacl | kb/vv/run/judge-20260929T182311Z.md | 파일 | 같은 파일의 그래프 쪽 판정(`token-budget-shapes`, `agt:tokenCount` 3094 > 2856) — 위 `chunk` 면제와 같은 사유, append-only 기록은 소급 분할하지 않는다. shape는 그대로이고 선언된 면제가 적용된다 | orchestrator | 2026-10-01 |

