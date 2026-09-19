# hci 세션 시작 사이클 — 명령 / 정상 (기준선 2026-09-19, base 7cfc61f)

정상 칸이 수치라 초록이 반증 가능하다. 기준선이 바뀌면 이 표를 고친다 — 게이트 목록·비-초록 기준선의 **원본은
`docs/tools.md` §게이트를 추가할 때**이고 여기는 hci 의 실행 순서다.

| # | 명령 | 정상 |
|---|---|---|
| 1 | `git status -sb` · `git log --oneline -3` | 작업 트리에 **남의 변경**이 있을 수 있다(다른 세션이 같은 트리) — 있으면 커밋 전 `commit-lane-procedure.md` |
| 2 | `bazel test //...` | **18/18 PASS** (코어 게이트 8 · 드리프트 2(BUILD·skills) · 채널 · doccheck · consistency_build · 음성 시험 5). FAIL 이면 지식 산출물을 고치는 것은 담당 역할 — hci 는 항목으로 보고 |
| 3 | `bazel test //docs/feedback:channel_lint_test --test_output=all` | `OK channel` · WAIT 는 담당 역할 대기 목록(정상) · 답 placeholder 가 남은 항목은 "처리 대상 아님"으로 집계된다(유저 답 대기 = 정상) |
| 4 | `bazel build //kg:metrics` → `bazel-bin/kg/metrics.md` | 청크 813(살아 684 — 개발 634 · V&V 50) · 링크 개체 607, 증거 100% · 고아 0% · 복원 5.0% · **연결 성분 4**(관측 3건이 링크가 없어 각각 성분 — 유저 판단 대기) |
| 5 | `bazel build //kg:audit` → `bazel-bin/kg/audit.md` | 검증 대응물 있는 요구 18/33 · 기준 없는 verifies 0 · 최근 실행 pass 16·fail 0 |
| 6 | `bazel build //kb:consistency` → ⑥ | tier 1 위반 0(면제 1건) · 근사 중복 후보 1(실행 기록 둘, 형식이 같아 구조적) |
| 7 | 조사 lane — `inquiries/` 의 열린 항목은 **hci 가 직접 조사**한다 |
| 8 | 채널 스캔 — 유저 lane `open`/`approved`/`rejected` · `agents/` `open` · `inquiries/` `answered` · `handoff/` 짝 없는 것 | 기준선 2026-09-19: 유저 8(답 대기 3 · 반영 완료 유지 1 · `docs/` 링크 잔존 4) · agents 6(전부 `answered` — 발신자가 닫는다) · handoff 0 · inquiries 1(`closed`, 링크 때문에 유지) |

## 없는 것 — 없는 것이 정상이다 (다음 세션이 고치러 오지 않게)

- `artifact`·`annotation` plane 0, `contract`·`schema` 는 V&V 사슬로만 16·16 — 사례 프로젝트 관통 전까지 그대로.
- V&V: 시나리오 0 · 검증기 청크 0 · 판정 주석 0 · `defect` 모듈 없음 · V&V 프로파일 없음(위험 분석 G1~G6 은 유저 입력 대기).
- `when` 실물 0 · `suspect` 실물 0 · selector 어휘 없음 — 링크 견고성 C·D·E 가 유저 판단 대기라 그렇다.
- `.claude/agents/` 에 `hci.md` 뿐 — vnv·developer 정의 파일 없음(AGENTS 표가 원본).
- `handoff/` 항목 0 = 인수 대기 없음. 짝 없는 handoff = 되돌아오지 않은 것.

## 되돌아오지 않은 것을 보는 법
`channel_lint` 의 WAIT 줄 + `handoff/` 에서 `agents/` 짝(`ref: handoff/…`)이 없는 파일.

## git 인증
`git push` 는 저장된 자격이 만료돼 실패한다. `gh` 는 로그인돼 있으므로
`git -c credential.helper='!gh auth git-credential' push origin main` 으로 민다(설정을 바꾸지 않는다).
