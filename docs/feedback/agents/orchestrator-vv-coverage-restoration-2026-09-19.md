---
from: orchestrator
kind: notice
status: open
targets: [kb/vv/, kb/dev/decision/p10-restored-link-marking/, chunks/decision/, tools/link.py, tools/chunk2kg.py, tools/kb_lib.py, STYLEGUIDE.md, docs/method.md, docs/roadmap.md, docs/tools.md]
---

# 검증 대응물 18/33과 복원 첫 형태 — 사슬 8 추가, `link` 후보 생성기, `restored` 표시 (2026-09-19)

유저 "계속해서 진행해줘"에 따라 같은 날 두 번째 라운드를 돌렸다. 7단계의 검증 범위를 넓히고 8단계의 복원 쪽을 열었다.

- **V&V 사슬 8 추가**(vnv, 청크 24): 기계적 검증기가 이미 있는 요구 8건 — `r-024`(기준 없는 verifies 거부) · `r-026`(관측 append-only) · `reproducible-runs`(`--runs_per_test=2`) · `r-006`(가정 명시) · `explicit-versioned-inputs`(표준 어휘 해시 고정) · `documents-are-generated`(드리프트 시험) · `r-016`(음성 시험 5) · `audit-self-sufficiency`(샌드박스 생성 + `bazel query`). 실행 명령은 전부 허용 목록이라 SKIP 0. verifies 대상은 후보 대신 실제로 그 검증기를 정한 결정으로 골랐다(`p0-odd-scope-assumption`·`p11-inputs-as-versioned-vocabulary`·`p6-gate-catalogue`). 감사 보고서: 검증 대응물 있는 요구 **10 → 18/33**, verifies 대상 결정 16/198, 기준 없는 verifies 0. 두 번째 실행 기록 `kb/vv/run/run-20260919T065358Z.md` — 케이스 16 pass · 명령 28 중 26 실행. 남은 15건은 검증기가 없는 요구다(r-001~005·007·009·010·013·015·019·020·023·025·`verification-means-trust`).
- **결정 `p10-restored-link-marking`**(orchestrator, `refines` r-011): 복원 링크는 링크 키에 적고 같은 청크의 선택 키 `restored: [<대상 IRI>…]`에 한 번 더 적는다. 목록의 IRI가 링크 대상에 없으면 `chunk2kg`가 `FAIL [restored]`. 그 링크 개체의 증거는 `constructionRecord`(사람의 확정 기록) + `proposal`(후보 출처) 두 줄이다 — developer가 실측으로 잡은 대로 `proposal` 한 줄이면 verify 질의 `confirmed-without-evidence`가 29건을 거부한다. 결정 본문을 두 줄 형태로 고쳤다(게이트 약화 없음). 복원 링크 = 구축 기록 아닌 증거를 하나라도 가진 링크, 비율은 `kb_lib.link_origins` 하나로 `metrics`·`audit`가 센다.
- **사후 링크 28건을 복원으로 표시**: 2026-09-13에 이은 옛 결정 27건 + `p12-documents-are-generated`의 `refines`에 `restored`를 넣었다(메타데이터만, `verified` 없음). 복원 29 / (구축 731 + 29) = **3.8%** < 20%. 로드맵의 "알려진 한계"를 지웠다.
- **`link` 후보 생성기**(developer): `bazel build //kg:link_candidates` → 그래프 union만으로 본문 식별자(`cites`)·테스트 공동 커버(`verifies`)·개념 공유(`usesConcept` ≥ 3)에서 후보, TIM 허용 칸·plane 단방향·수준·복합체 형제로 탈락, 앵커당 k ≤ 7. 첫 결과: 후보 11(구축 기록 9 · proposal 2), 탈락 21(deprecated 19 · 형제 2). 전부 `relatedTo`다 — 인용 30건이 모두 결정↔결정이고 TIM의 결정→결정 칸이 `supersedes`뿐이라서다. `relatedTo`는 링크 키가 없어(`coUpdatesWith`뿐) 채택해도 복원 비율에 들지 않는다 — 결정 본문에 적었다.
- **문서**: STYLEGUIDE §4 선택 키에 `restored`, method §6·§9, tools(활용 첫 형태 10, `link` 행, 배선), roadmap(입력표 후보 상한 "있음", 8단계 행, 다음 산출 8), 경쟁 질문 문서의 앵커. skill 15(`link` 추가).
- 남긴 것: 후보 11의 채택 판정(전부 `relatedTo`라 실익이 작다), 거짓 빈 칸 판정, 동시 편집 이력 근거, 검증기 없는 요구 15의 검증 수단, V&V 프로파일(위험 분석 G1~G6 — 유저 입력 필요)·`defect`, 시나리오·검증기·판정 주석 항목.

## hci에 전달
- 원장에 "검증 대응물 18/33 · 복원 첫 형태 · 결정 p10-restored-link-marking(2026-09-19)" 한 줄. 재판정 대상 없음.
- `restored`를 넣은 옛 결정 27건은 `verified`가 없어 재검토 표시 대상이 아니다. `kb/dev/decision/BUILD.bazel`은 생성기가 갱신했다(`p10-restored-link-marking` 타깃).
- 커밋 대기 파일이 많다(09-14 이후 전부 미커밋). 유저 요청 시 커밋.

## 답
(hci가 채움)
