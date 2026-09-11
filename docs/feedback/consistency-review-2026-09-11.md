---
from: hci
status: open
targets: [README.md, docs/roadmap.md, docs/tools.md, docs/risks-and-tensions.md, docs/open-questions.md, docs/decomposition-audit.md, docs/rules.md, INTENT.md]
---

# 진행 검토 — 전체 통일성·완결성 (2026-09-11, 인수 커밋 87a25d4 이후)

유저 요청: "진행사항 검토하고 전체적인 통일성 및 완결성 확인해줘." hci 는 읽고 보고만 한다 — 고칠 것은 담당 역할(orchestrator) 몫이다.

## 1. 진행 상태 (실측)

| 항목 | 값 |
|---|---|
| 게이트 | **15/15 PASS** — 코어 게이트 7 · 드리프트 · 동일성 · 채널 · 음성 시험 5 |
| 지식 | 요구 33 · 결정 185(복합체) · 옛 결정 153 · 살아 있는 청크 612(deprecated 129) · 온톨로지 TTL 34 · verify 질의 5 · 도구 21 |
| 인수 | hci 생성 청크 201 전부 orchestrator `verified` · 항목 `인수:` 8곳 · main = origin/main |
| 1단계 | 고아율 0% · 확정 문장 커버리지 148/148 · 앵커 작업 집합 예산 내 98.7~100% · **라벨 대표성 실험 미판정** |
| 2단계 | 판정 방법·명시 제외·스코프 파생·첫 모니터링 이탈 0 전부 ○ · 앵커별 작업 집합 ○ |
| 3단계 | 링크 개체 472, 증거 100% · 복원 비율 6% · plane×plane 매트릭스 8칸 중 2 · `refines` 건너뜀 333(구조적) · 하네스 읽기·쓰기 자동 기록 없음 |
| 남은 구조 | 연결 성분 5(목표 1) · `contract`·`schema`·`artifact` 0 · `kb/vv/` 비어 있음 · 사람 검토(`human:`) 0 |

## 2. 통일성 — 문서가 실측과 어긋난 곳 (담당 역할 수정 대상)

| 파일:줄 | 낡은 서술 | 지금 |
|---|---|---|
| `README.md:17` | "검사·생성 6개(3계층 컴파일러) · 활용 도구 0개" | 검사·생성 도구 12+, 활용 첫 형태 5(workset·metrics·impact·handoff·consistency). "컴파일러"는 용어집 밖 |
| `README.md:39,63`, `INTENT.md:19`, `decomposition-audit.md:277` | "결정 182건" | 185 (p14-stage-pass-conditions · p0-workset-anchor-neighbourhood · p4-redundancy-as-safety-margin 추가) |
| `README.md:64` | "옛 결정 126건이 deprecated" | 옛 126 + 대체된 새 결정 1(`p14-adoption-stages`) = deprecated 청크 129 |
| `roadmap.md:31` | "검사·생성 6개 …" | 위와 같음 |
| `roadmap.md:52` | "지식(요구 33 + 결정 182)이 조회·연결의 대상이 되지 못하고 있다" | workset·impact·링크 개체가 있다 — 문장 자체가 낡음 |
| `open-questions.md:12` vs `:15` | "Part XVI … 25건" vs "Part XVII의 30건" | 한 파일 안의 모순 — 12행을 XVII·30건으로 |
| `decomposition-audit.md:279,280` | "Part XVI 25건", "Part XIII 도입 순서 → 도입 7단계" | Part XVII 30건, Part XIV 8단계 |
| `rules.md:185` | "링크 데이터는 아직 0개다" | 링크 개체 472(구축 기록 증거). 후보 링크는 0 |
| `risks-and-tensions.md:17,18,21,23,28,45` | "해시 미구현" · "링크 붕괴 미착수 — 링크 0" · "역량 질문 목록 자체가 없다" · "해시가 없어 트리거 불가" · "기계화된 것은 셋뿐" · "검사 4개에 활용 0개" | contentHash 있음 · 링크 472 + verify 질의 · `competency-questions.md` 32문항 · 해시는 있고 라벨 재검토 트리거만 없음 · 기계화 10+(통제 어휘·ODD 참조·dangling·verify 5·writer·드리프트·수준 허용표·plane 방향·가시성) · 활용 첫 형태 5 |
| `tools.md:143` | "활용 도구 — 하나도 구현되어 있지 않다" | 바로 아래 표가 "첫 형태 있음"이라 문단과 표가 모순 |
| `tools.md` | 도구 표에 `channel_lint`·`consistency`·`endorse`·`label_sample`·`same_bytes` 없음; 게이트 트리에 `//docs/feedback:channel_lint_test` 없음 | 인수 커밋이 추가한 것들 |
| `glossary.md` | orchestrator 가 도입한 "안전율(중복)"이 없다 | 표준 공학 용어이나 용어집이 원본이므로 등재 |

용어 잔재는 사실상 없다 — 문서·KB·온톨로지에서 옛 표기 0(증가 의미의 "상승", 판정 도구 의미의 "컴파일러"는 정상), 조사 오류 0. 원장 1~23 연속, 미해결 1~30 연속, docs 색인 완결.

## 3. 완결성 — 계획 대비 남은 것

- **라벨 대표성 실험이 둘로 갈라졌다.** hci 는 선택지 1(사람 판정, 표본 30, 미끼 없음)의 기록지를 만들었고, orchestrator 는 `tools/label_sample.py`(에이전트 판정, 표본 60, 미끼 10, `key.json`)를 만들었다. 프로토콜 항목은 `approved`인데 **어느 안인지 답이 없다.** 둘 다 판정은 비어 있다. → 유저가 하나를 고르거나(또는 둘 다: 에이전트 판정 + 사람 표본 검증), 고른 뒤 다른 쪽을 닫아야 한다.
- 3단계에서 기계화 못 한 것: 하네스의 읽기·쓰기 집합 자동 기록(`handoff`는 수동), `refines` 한 단계씩(abstract·logical 결정이 생겨야), 매트릭스 6칸(contract·schema·artifact·V&V 항목).
- 4단계 이후: 가정 1건뿐·판정식 없음(`assume_check`), `-space` 0, 상승 0, V&V KB 비어 있음.
- `consistency` 보고가 어디에도 배선되지 않았다 — `kb_consistency` 매크로는 있으나 `kg/BUILD`에 타깃이 없어 `bazel build`로 만들 수 없다(문서만 `docs/BUILD.bazel` 주석). 규칙(rules.md)은 "커밋마다 생성"이라 한다.

## 4. 판단 요청 (유저)

1. 라벨 대표성 실험 — 사람 판정(기록지) / 에이전트 판정(`label_sample`, 미끼) / 둘 다 중 무엇으로 1단계를 판정할지.
2. §2 의 문서 정정을 orchestrator 에게 맡길지(권고 — 한 커밋 분량).

## 답
**유저(2026-09-11): "문서 정정은 orchestrator에 맡기고, 라벨 실험은 둘 다 진행해줘"** — §2 문서 정정과 §3 `consistency` 배선은 orchestrator 담당(hci 는 손대지 않음). 라벨 실험은 사람 판정(기록지)과 에이전트 판정(`label_sample`, 미끼) 둘 다 — 에이전트 판정은 hci 세션이 판정자로 수행하고 결과를 `label-experiment-agent-2026-09-11.md` 에 남긴다.

인수: orchestrator 2026-09-11 — §2 문서 정정 전부 반영(`README.md`·`INTENT.md`·`roadmap.md`·`open-questions.md`·`decomposition-audit.md`·`rules.md`·`risks-and-tensions.md`·`tools.md`·`glossary.md` 안전율 등재). §3 `consistency` 배선은 `kb/BUILD.bazel:70`의 `kb_consistency(name = "consistency")`로 이미 있어 `bazel build //kb:consistency`가 성립한다(검토 시점의 "kg/BUILD에 없음"은 위치 착오) — `tools.md` 생성물 목록에 추가. "커밋마다 자동 생성"은 하네스 훅이 없어 규약으로 남는다. 라벨 실험 반영분(`verified` 60 + `human:cpark` 10, roadmap)은 워킹트리에 있고 게이트 15/15 PASS — 커밋은 유저·inspection 몫.
