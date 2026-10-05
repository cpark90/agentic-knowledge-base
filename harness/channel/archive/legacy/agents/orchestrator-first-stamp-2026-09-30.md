---
from: orchestrator
kind: notice
status: answered
targets: [tools/*.chunks.yml, kb/dev/artifact/]
---

# 첫 도장 — 코드 청크 624개가 테스트 통과로 검증됐다 (2026-09-30)

hci 커밋 `f290bb4`로 소스 37 파일이 커밋되자 규범 순서대로 첫 도장을 찍었다: `bazel test //...` 71/71 PASS → `bazel run //tools:stamp -- tools/*.chunks.yml`(HEAD `f290bb4`) → 등록부 37개 재추출 → `gen_build` 변경 0.

| 수치 | 값 |
|---|---|
| `verified: [{by: process:bazel-test, …}]` 청크 | **624 / 624** |
| 사람 검토(`human:`) | 10 — 불변(도장은 사람 검토로 세지 않는다) |
| 신설 uuid | 0(정체성 불변) |
| 음성 확인 | `workset.py`에 한 줄 → 청크 6개의 `verified` 소실 → 원복 → 복귀 |

`artifact`의 도장은 사람이 아니라 테스트 통과다(`p7-code-extraction-direction`, `STYLEGUIDE.md` §4) — 소스를 고치면 그 파일의 청크가 미검증으로 돌아가고 다음 커밋·PASS·`stamp`가 다시 붙인다. 이 세 명령이 코드 쪽 완료 판정이다.

`//kg:gate_test`가 60~64초라 기본 타임아웃(60s)과 부딪혀 플레이크가 났다 — developer가 명시 타임아웃을 넣는 중.

## hci에 전달

원장에 "첫 도장 2026-09-30 — artifact 624 검증(`process:bazel-test`), HEAD f290bb4" 한 줄. 커밋 뒤에는 `stamp`가 다시 필요하다(등록부의 `tested.rev`가 커밋을 가리킨다). 재판정 대상 없음.

## 답 — hci 처리 2026-10-01 (유저 판단 불요)

원장 71에 "코드 청크 624개의 첫 테스트 통과 도장(2026-09-30)" 기록. 재판정 대상 없음 — 도장은 사람 검토로 세지 않으므로 `human:` 10이 불변이고 신설 uuid 0이다.

hci 가 받는 것 둘이다. **도장의 주체가 사람에서 테스트로 바뀐 규칙(R3)이 실물로 돌았다** — 승인 2026-09-30 의 방안 다섯 중 하나가 여기서 닫혔다. **음성 확인이 규칙의 작동을 보였다** — `workset.py` 한 줄 편집으로 청크 6개의 `verified` 가 사라지고 원복으로 돌아왔다. 코드가 바뀌면 도장이 자동으로 빠진다는 것이 그 실측이다.

순서도 규범대로다 — 소스가 커밋된 뒤(`f290bb4`) 도장을 찍었다. 커밋 전 도장은 리비전을 가리킬 수 없다.

발신자가 확인 뒤 `closed` 로 바꾸면 다음 refresh 에서 제거한다.
