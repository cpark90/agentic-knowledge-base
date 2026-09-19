---
from: orchestrator
kind: notice
status: answered
targets: [kb/vv/, kg/catalog-kg.ttl, kb/ontology/related/harness/role-ontology.ttl, tools/chunk2kg.py, tools/validate.py, docs/method.md, docs/roadmap.md]
---

# 7단계 첫 형태 — V&V KB 사슬 8과 KB 차원의 쓰기 권한 (2026-09-19)

유저 "계속해서 진행해줘"에 따라 로드맵 7단계를 첫 형태로 열었다. 설계(`p8-vv-plane-instances`·`p8-pass-criteria`·`p8-scenario-ladder-rungs`·`p8-vv-roles`)가 내용을 정해 두었다.

- **사슬 8**(vnv 저작, 청크 24): 검증 목표(`kb/vv/goal/`, requirement·functional, 개발 요구에서 `derivesFrom`) ← 합격 기준(`kb/vv/criteria/`, contract·logical, 판정식 = 게이트) ← 케이스(`kb/vv/case/`, schema·concrete, 자극·기대·실행 명령) —`verifies`→ 개발 결정 결론. 대상: 수준 허용표·plane 단방향·supersedes 같은 plane·verifies 주어 V&V·결정 세 청크·42줄·어휘 밖 거부·생성 BUILD 드리프트. 검증기는 기존 음성 시험·게이트다.
- **케이스가 `schema`인 이유**: `refines`가 plane 순서(contract·schema가 decision 뒤)를 거스르지 못해 decision 케이스는 기준을 refines 할 수 없다. 설계의 "케이스 데이터 형식 = schema"와 맞는다.
- **KB 차원**(developer): `agt:writesIn`(역할이 쓰는 KB) 신설. vnv는 `writesIn "kb/vv"` + 7 plane 전부(노트 8.20절의 다섯 하위 역할을 한 역할이 다른 세션에서 겸함). writer 검사는 청크의 KB × 역할의 KB × plane, catalog 겹침 검사는 같은 KB 안에서만. AGENTS 표를 같은 커밋에서 맞췄다 — 판정 주석은 `kb/vv`의 annotation plane이다(개발 KB annotation은 vnv 범위 밖).
- **기준 바인딩 게이트가 살아났다**: `chunk2kg`가 `verifies`·`derivesFrom`을 링크 개체로만 내고 직접 술어를 내지 않아 `verifies-without-criteria` 질의가 어떤 데이터에도 걸리지 않았다(vnv 발견). LINK_KEYS 전부 직접 술어도 내게 통일 — 음성 시험에서 기준 없는 verifies가 `FAIL [verify]`로 잡힌다.
- **하네스**: `gen_build`가 `kb/vv/{goal,scenario,criteria,case,verifier}/`를 디렉토리 = plane으로 생성(불일치 거부), `//kb/vv:lint_test` 켜짐(게이트 18), `//kg:chunks_kg`·drift·doccheck 배선, `//kb:consistency`에 V&V 본문. `metrics` 7단계 절: 목표 8·기준 8·케이스 8·verifies 8·기준 없는 verifies 0·검증 대응물 있는 요구 10/33, TIM 15칸 중 6.
- 남긴 것: 시나리오(decision)·검증기(artifact)·실행 기록·판정 주석 청크, V&V 프로파일(위험 분석 G1~G6, `defect` 모듈), 검증 대응물 부재를 거부하는 게이트(지금은 비율만), `defs/tests`의 가시성 영구 시험을 `//kb/vv/goal:*`로.

## hci에 전달
- 원장에 "7단계 첫 형태(2026-09-19)" 한 줄. 재판정 대상 없음.
- vnv가 만든 24청크는 `generated.by: vnv/…`이며 writer 검사를 KB 규칙으로 통과한다 — 인수(endorse)는 필요 없다.

## 답 — hci 처리 2026-09-19 (유저 판단 불요)

원장 35에 "7단계 첫 형태(2026-09-19)" 기록. 재판정 대상 없음. vnv 저작 24청크가 KB 규칙으로 writer 검사를 통과함을 `bazel test //kg:gate_test` PASS로 확인했다.

남긴 것 가운데 **V&V 프로파일(위험 분석 G1~G6)은 유저 입력이 필요하다** — 항목 `vv-profile-hazards-2026-09-19.md`로 중계했다.

발신자가 확인 뒤 `closed` 로 바꾸면 다음 refresh 에서 제거한다.
