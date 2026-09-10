# 미해결 질문 — 인덱스

두 종류를 구분한다. **체계의 미해결**은 설계가 아직 답하지 못한 것이고, **구현의
미해결**은 답은 정해졌으나 아직 만들지 않은 것이다. 섞으면 "설계가 덜 됐다"와 "아직 안
만들었다"가 뒤엉킨다.

**항목은 한 줄로 쓰지 않는다.** 상세가 필요한 항목은 [`open-questions/`](open-questions/)에
파일 하나로 있고 **다섯 절**(질문 / 이미 정해진 것 / 현재 상태 / 답이 가르는 것 / 선택지)을
갖는다. 이 인덱스는 라벨 목록이다.

> **2026-09-10 재동기화 (유저 결정 C5 — 노트 우선).** 구조도 v4를 근거로 닫았던 13건은
> 그 근거가 노트 v3로 대체되면서 **다시 열렸다**. 번호는 노트 Part XVI를 따른다(25건).
> 아직 파일이 없는 재개 항목은 작업이 닿을 때 다섯 절 파일을 만든다.

## 1. 체계의 미해결 — 노트 Part XVII의 30건

| # | 질문 | 상세 파일 |
|---|---|---|
| 1 | 상위 온톨로지의 continuant/occurrent 구분 적용 (2.2) | [`upper-ontology-alignment`](open-questions/upper-ontology-alignment.md) |
| 2 | `contract`·`schema`의 logical 내용 (6.4) — v3에서 artifact→schema로 바뀜 | [`contract-artifact-logical`](open-questions/contract-artifact-logical.md) (파일명은 v1 기준 — 갱신 대상) |
| 3 | 설계 논증의 형식화 가능 여부 (6.6) | [`design-argument-formalization`](open-questions/design-argument-formalization.md) |
| 4 | 구성체 수준 가정의 필요 여부 (6.5) | **재개** (C5) |
| 5 | 리팩터링 시 시간 정체성 (2.6) | [`temporal-identity`](open-questions/temporal-identity.md) |
| 6 | 상승의 트리거 (6.3) | **재개** (C5) |
| 7 | `annotation`의 plane 순서 (5.2) | **재개** (C5) |
| 8 | 링크 판정 근거 (10.8) — v5 9.11 증거 장부가 규칙을 정함, 확정 규칙의 수는 #29 | [`link-judgement-basis`](open-questions/link-judgement-basis.md) |
| 9 | plane 수 상한 (5.3) | **재개** (C5) |
| 10 | logical 공간 커버의 계산 — 조합·경계값 가중 (8.7) | [`coverage-computation`](open-questions/coverage-computation.md) |
| 11 | 기존에 없는 모듈화 구현 (1.2) | **재개** (C5) |
| 12 | 영구 보관 정보와 실시간 정보 구분 (11.4) | **재개** (C5) |
| 13 | metric 선택 (12.3) — v4가 "낮으면 무엇을 고치는가"로 셋으로 제한 | [`evaluation-metrics`](open-questions/evaluation-metrics.md) |
| 14 | 미명명·미검출 오류 — 미지 요인 vs 미지 조합 (Part VIII) | [`failure-cause-statistics`](open-questions/failure-cause-statistics.md) |
| 15 | ODD의 적정 크기 (3.7) | [`odd-right-size`](open-questions/odd-right-size.md) |
| 16 | 42줄 상한의 plane별 적정성 (4.9) | **재개** (C5) |
| 17 | 컨텍스트 예산의 실측 (1.4) | [`context-budget`](open-questions/context-budget.md) |
| 18 | 하위 ODD가 상위에 없는 속성을 필요로 할 때 (3.11) | **재개** (C5) |
| 19 | `memory` plane의 42줄 단위 (4.12) | **재개** (C5) |
| 20 | 상승 트리거 임계값 N·M·K (6.11) | **재개** (C5) |
| 21 | 단계별 소요 기간 (Part XIV) | **재개** (C5) |
| 22 | 시뮬레이션 프로젝트의 최소 구성 (8.9) | **재개** (C5) |
| 23 | 6단계 관측을 커버리지에서 배제하는 것이 과도한가 (8.10) | **재개** (C5) |
| 24 | `decision`의 concrete가 `schema`·`artifact`의 concrete와 중복되는가 (6.4) | **신규** (v3) |
| 25 | 변이 주입 표본 검사의 표본 크기 (8.6) | **신규** (v3) |
| 26 | 시나리오 부류(G5) 라이브러리의 도메인 간 재사용 범위 (8.21) | **신규** (v4) |
| 27 | `-space` 제약이 CEL 필터로 감당되지 않는 규모 — 솔버 전환 시점 (9.10) | **신규** (v4) |
| 28 | ~~OKF `trust` 값 집합과 근거 유형의 사상~~ (부록 E) | **해소** (2026-09-10) — 판정 이력은 `verified` 목록, 근거 유형은 링크 장부 |
| 29 | 증거 장부의 확정 규칙 — 실행(+) 몇 건이면 구축 없이 확정 가능한가 (9.11) | **신규** (v5) |
| 30 | 조건부 링크의 `when` 평가 비용 — 재판정 경계마다 전 링크를 평가할 수 있는가 (9.11) | **신규** (v5) |

### 이 저장소가 관찰한 추가 긴장 (노트 목록 밖)

| 질문 | 출처 |
|---|---|
| 4.5 동질성(부분의 plane·level = 전체)과 4.7 "결정 = 세 청크의 구성체"(결론 concrete·근거 logical)가 한 구성체 안에서 충돌한다 — 결정 구성체는 동질성의 예외인가, 결론→근거가 refines 링크여야 하는가 | v3 재도출 구현 중 발견 (2026-09-10). 관련: #24 |

## 2. 닫힌 질문 — 되묻지 않도록 남긴다

| 질문 | 무엇이 닫았나 |
|---|---|
| 결정의 역할 태그 중 무엇이 필수인가 | 노트 v3 4.7 — 결정 = 결론·근거·대안 세 청크의 구성체 (유저 결정 C2). [`decision-role-tags`](open-questions/decision-role-tags.md)는 기록으로 유지 |
| 프로파일 간 공유 개념 | v3가 목록에서 제거 — 골격/프로파일 두 층으로 흡수 |
| 42줄 강제가 손상시키는 plane이 있는가 | v3가 목록에서 제거 — #16(plane별 적정성)으로 흡수 |
| 역할 세분화 vs 오염 전파의 균형점 | v3가 목록에서 제거 — 실측 후 재검토 ([`risks-and-tensions.md`](risks-and-tensions.md)) |

## 3. 구현의 미해결 — 만들기만 하면 되는 것

답은 정해져 있고 막혀 있지 않다. 우선순위는 [`roadmap.md`](roadmap.md)의 "다음 산출".

| 항목 | 무엇이 없나 |
|---|---|
| 활용 도구 | workset/labels · link · query · impact · project · metrics — 하나도 없다. v3는 `propagate`·`revalidate`도 요구 |
| 읽기·쓰기 집합 기록 | 연결 단계의 입력이 없다 |
| `profile/` 디렉토리와 구축 절차 | 분야 프로파일이 하나도 없다 |
| 미구현 게이트 | 카탈로그 정합성 · 구성체 동질성 · 정규화 · **대안 청크 필수**(v4 7.4 — 현재 77/145 위반) · 장부 규칙(verify 질의 2개는 있음, 데이터 0) |
| 검사 도구 확장 | `odd_check`·`assume_check` (v3 도구 목록) |
| 이름 붙은 그래프 (TriG) | 네 그래프가 논리적 구분일 뿐 |
| V&V KB 내용 | `kb/vv/`가 비어 있다 — 이 저장소 자신의 검증 목표·시나리오·기준이 없다 |
| `artifact` plane 등록 | 도구 코드를 지식으로 등록할지 미결 |
| YAML 로더 | `tools/kb_yaml.py`는 부분집합 로더다. 잠금(`requirements_lock.txt`)이 순수 파이썬 휠만 두어 PyYAML(C 확장)을 못 넣었다 — 잠금 정책을 바꾸거나 순수 파이썬 YAML 구현을 넣으면 삭제 |

## 4. 이 목록을 쓰는 법

- **새 질문이 생기면** 노트 목록 밖 표에 넣고, 상세가 필요하면 `open-questions/`에 파일로.
- **질문이 풀리면** 결정을 만들고 닫힌 표에 한 줄을 남긴다 — 같은 질문이 다시 열리지
  않게. 단 닫은 **근거가 대체되면 다시 연다**(이번 C5가 그 사례다).
