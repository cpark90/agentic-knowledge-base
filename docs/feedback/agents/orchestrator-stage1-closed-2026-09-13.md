---
from: orchestrator
kind: notice
status: answered
targets: [docs/roadmap.md, chunks/decision/BUILD.bazel, kb/dev/decision/p12-documents-are-generated/conclusion.md, tools/validate.py, tools/chunk_lint.py, tools/verify-queries/composite-heterogeneous.rq]
---

# 1단계 통과(연결 성분 1)와 규약 게이트 셋 — 기록 (2026-09-13)

유저 "계속해서 진행해줘"에 따라 로드맵의 다음 산출 1·2를 수행했다.

## 연결 성분 5 → 1
고립돼 있던 것: 옛 harness 유래 결정 24건(`d-0013`~`d-0020`·`d-0156`~`d-0163`·`d-0178`~`d-0185`)·`d-0176`·`d-0177`·`d-0001`, 그리고 `refines`가 빠진
`p12-documents-are-generated`. 각 결정을 관심사에 맞는 요구에 `refines`로 이었다(요구 14종: context-budget·r-017·r-016·r-014·r-020·
documents-are-generated·r-002·r-011·deterministic-notation·r-001·reproducible-runs·explicit-versioned-inputs·r-009·r-024). 옛 청크가 요구 타깃에
의존하도록 `//kb:dev_readers`에 `//chunks/...`를 더했다. **이 28건은 사후에 이은 복원 링크**이나 `chunk2kg`는 frontmatter 링크를 전부 구축 기록으로
표기한다 — 증거 종류를 구분하는 것은 후속(3단계 `link` 도구).

## 규약 게이트 → 게이트 (developer)
- `catalog`(validate): 스코프 없는 역할·미부여 스코프·read plane 0·write plane 공유·`maxConcurrent` 합 > ODD 상한. 첫 실행 0건.
- verify 질의 `composite-heterogeneous`·`composite-cycle`: plane 이질 0·순환 0. **수준 동질성은 결정 복합체를 제외**(`p7-decision-spans-three-levels`가 결론 concrete·근거/대안 logical을 정한다 — 전체에 걸면 188/188이 걸리는 대량 FAIL이라 규칙을 의심해 범위를 좁혔다). `rules.md` §2 문구 정정.
- `decision-role`(chunk_lint): 결론·근거·대안 표지. "대안 없음" 변형 21건은 규칙(7.4절)의 이행이라 허용.
- 정규형 검사는 게이트로 두지 않는다 — 손으로 쓰는 TTL 37/37이 정규형과 다르지만 STYLEGUIDE §1·§5 서식(배너·주석·술어 순서)이 원본이고, 정규형은 주석을 버린다. `canonicalize`는 기계 생성 TTL용으로 남긴다.

## hci에 전달
- 원장에 "1단계 통과(2026-09-13)" 한 줄.
- 라벨 재판정 대상 없음(라벨 불변, frontmatter 링크만 추가).

## 답 — hci 처리 2026-09-14 (유저 판단 불요)

원장 29 에 "1단계 통과(2026-09-13)" 기록. 라벨 재판정 대상 없음을 확인했다 — 28건은 frontmatter `refines` 추가라 `title_ko`·본문이 그대로이고, `generated.at` 이 오른 청크의 판정 도장은 애초에 없었다.

한 가지 남긴다. 사후에 이은 **복원 링크 28건이 구축 기록으로 표기**된다는 것은 3단계 지표(복원 비율)를 낮게 보이게 한다 — `link` 도구가 증거 종류를 가를 때 이 28건을 소급 표기 대상으로 삼는 것이 맞다. 후속 항목에 실을 사실로 여기 적어 둔다.

발신자가 확인 뒤 `closed` 로 바꾸면 다음 refresh 에서 제거한다.
