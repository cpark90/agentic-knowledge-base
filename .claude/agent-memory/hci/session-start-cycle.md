# hci 세션 시작 사이클 — 명령 / 정상 (기준선 2026-09-12, base 10c75e6)

정상 칸이 수치라 초록이 반증 가능하다. 기준선이 바뀌면 이 표를 고친다 — 게이트 목록·비-초록 기준선의 **원본은
`docs/tools.md` §게이트를 추가할 때**이고 여기는 hci 의 실행 순서다.

| # | 명령 | 정상 |
|---|---|---|
| 1 | `git status -sb` · `git log --oneline -3` | 작업 트리에 **남의 변경**이 있을 수 있다(다른 세션이 같은 트리) — 있으면 커밋 전 `commit-lane-procedure.md` |
| 2 | `bazel test //...` | **17/17 PASS** (코어 게이트 7 · 드리프트 · 동일성 · 채널 · doccheck · consistency_build · 음성 시험 5). FAIL 이면 지식 산출물을 고치는 것은 담당 역할 — hci 는 항목으로 보고 |
| 3 | `bazel test //docs/feedback:channel_lint_test --test_output=all` | `OK channel` · WAIT 는 담당 역할 대기 목록(정상) · FAIL 은 hci 규약 위반 |
| 4 | `bazel build //kg:metrics && sed -n 3p bazel-bin/kg/metrics.md` | 청크 750(살아 있는 621 · deprecated 129) · 링크 개체 475, 증거 100% · 고아 0% · 연결 성분 **5 (목표 1 — 계약·스키마·구현 plane 이 0 이라 구조적)** |
| 5 | `bazel build //kb:consistency` → ⑥ | tier 1 위반 **0** (잔존 2건은 tier 3/waiver 목록 — 보고에 보이는 것이 정상) |
| 6 | 채널 스캔 — 유저 lane `open`/`approved`/`rejected` · `agents/` `open` · `inquiries/` `answered` · `handoff/` 짝 없는 것 | 기준선: 유저 11(실험 4 · 설계 자료 3 · 원장 · 태깅 대기 1 · 검토 2) · agents 1 · handoff 0~1 · inquiries 2 |

## 없는 것 — 없는 것이 정상이다 (다음 세션이 고치러 오지 않게)

- `kb/vv/` 비어 있음, `kb/ontology/vv` 없음 — 도입 4단계 전. V&V 설계 입력은 `agrtls-practices-review-2026-09-12` V&V 절.
- `.claude/agents/` 에 `hci.md` 뿐 — vnv·developer·inspection 정의 파일 없음(AGENTS 표가 원본). V&V 착수 시 신설.
- `contract`·`schema`·`artifact` plane 0 — plane×plane 매트릭스 8칸 중 2, `refines` 한 단계씩 건너뜀 339. 사례 프로젝트 관통 전까지 그대로.
- `handoff/` 항목 0 = 인수 대기 없음. 짝 없는 handoff = 되돌아오지 않은 것.
- 사람 검토(`human:`) 도장 10건 — 라벨 실험 표본. 기록지 30행 사람 판정은 아직 비어 있음(유저).

## 되돌아오지 않은 것을 보는 법
`channel_lint` 의 WAIT 줄 + `handoff/` 에서 `agents/` 짝(`ref: handoff/…`)이 없는 파일.
