# tools — 검사 도구와 활용 도구, 세 층

도구는 [`rules.md`](rules.md)의 기계 형태(검사)와 [`method.md`](method.md)의 기계 형태(활용)다.
도구 하나가 규칙 하나 또는 절차 하나에 대응한다. 구조도 v5에 따라 **골격 / development / V&V**
세 층으로 적는다 — 골격 도구는 두 KB가 공유하고, 나머지는 각 KB의 규칙·절차를 수행한다.

## 하네스는 Bazel이다

지식 산출물은 데이터 타깃, 검사 게이트는 테스트 타깃이고 `bazel test //...` 한 번이 게이트
전체다. 근거와 기각된 대안은 [`id:chunk-d0001`](../chunks/decision/d-0001-bazel-harness.md),
plane별 규칙·deps=링크로의 전환은 [`pe-bazel-rules`](../kb/dev/decision/pe-bazel-rules/conclusion.md) (도입 3단계).

| 체계의 요구 | Bazel의 성질 |
|---|---|
| 바뀐 지식만 재판정 (d-0106 재판정 경계) | 입력 해시 기반 캐시 — 바뀐 파일의 게이트만 다시 돈다 |
| 산출물 간 의존을 명시 | BUILD 그래프가 의존을 선언으로 강제 |
| 판정 도구의 재현성 | hermetic 툴체인 + 해시 고정 lock |
| 게이트 우회 금지 | 테스트 타깃이라 우회하려면 BUILD를 고쳐야 한다 — 리뷰에 걸린다 |

**판정 가능한 것만 게이트로 만든다.** 기계가 판정할 수 없는 규칙은 게이트에 넣지 않고
`STYLEGUIDE.md`의 `[지킴]`으로 남기며, 게이트에 넣을 수 없다는 사실 자체를 §"게이트 밖"에
기록한다. shape은 **강화만** 한다 — 제약 완화는 유저 승인 사항이다.

## 게이트 총람 — 이 문서가 원본이다

노트 6.7절의 총람을 이 저장소의 실측과 함께 둔다 ([`p6-gate-catalogue`](../kb/dev/decision/p6-gate-catalogue/conclusion.md)).
실행 계층: **shape**(SHACL, 청크 단위, 즉시) / **verify**(SPARQL, 그래프 단위, 재판정 경계) /
**analysis**(Bazel 분석 시점, 빌드 실패) / **test**(실행, `bazel test`) / **human**(승인).
게이트에 걸린 청크는 `draft`에 머물고 하류로 전파되지 않는다.

| 게이트 | 무엇을 거부하는가 | 계층 | 절 | 이 저장소 |
|---|---|---|---|---|
| 청크 형식 | 42줄 초과, 라벨 누락, plane·level 유일성 위반, `type`이 온톨로지 밖 | shape | 4.4 | **있음** — `chunk_lint` + `chunk2kg` + `chunk-shapes` |
| 거주표 | plane에 허용되지 않는 level | shape | 6.4 | **있음** — `residency-shapes` |
| 구성체 | 부분의 plane·level 불일치, 직접 부분 > 9, 순환 | analysis | 4.5 | 부분 — `composite-shapes`(≤9)만. 동질성·순환은 없음 |
| 어휘 폐쇄 | 온톨로지에 없는 술어·개체 | verify | 0.0, 2.12 | **있음** — `validate` vocab |
| 출처 | `sources`가 빈 청크, 파생 연쇄 전체가 외부 유입인 확정 청크 | verify | 4.3, 2.12 | **있음** — `sources-empty.rq`·`imported-chain-confirmed.rq` |
| TIM | 링크 타입의 정의역·치역 밖 plane, 카디널리티 초과, 단방향 규칙 위반 | analysis | 10.1 | 없음 (도입 3단계, plane별 규칙) |
| ODD 참조 | ODD에 없는 조건을 참조하는 스코프·가정·시나리오 변수 | verify | 3.3 | **있음** — `validate` odd-ref |
| ODD 경계 | 후보 값·케이스 값이 ODD 범위 밖 | verify | 9.10 | 없음 (5단계 `space_check`) |
| 봉사 | `serves` 없는 abstract 결정 | verify | 6.8 | 없음 — abstract 결정 자체가 아직 없다 |
| 범위·제약 | 범위 없는 logical 변수, 실행 불가한 사후조건 | shape + test | 6.8 | 없음 (5단계) |
| 가로대 | 같은 높이의 V&V 대응물(목표·기준·verifier) 부재 | verify | 8.3 | 없음 (7단계; 그 전엔 **경고**) |
| 표본 근거 | `sampling` 없는 concrete 값·케이스 | shape | 6.8, 8.23 | 없음 (5·7단계) |
| 배정 근거 | 후보가 둘 이상인데 확정된 링크, 배제 근거 없는 기각 | verify | 9.10 | 부분 — 장부 규칙 2 질의(`confirmed-without-evidence`·`confirmed-with-refutation`), 링크 데이터 0 |
| 기준 바인딩 | 기준 없는 `verifies`, 판정식 없는 기준 | shape | 8.11 | **있음** — `verifies-without-criteria.rq` |
| 대안 기록 | 대안 청크 없는 결정 | shape | 7.4 | 규약 — 182/182 충족, shape은 없음 |
| 계약 선행 | 계약보다 먼저 확정된 구현 | verify | 7.5 | 없음 — `contract` plane 항목 0 |
| 판정 도구 | 컴파일·타입·스키마·린터 실패 | test | 5.4 | 없음 — `artifact` plane 항목 0 |
| 독립성 | 개발 역할이 V&V KB에 쓴 흔적 | verify | 8.5 | 없음 — `kb/vv/` 비어 있음 |
| 승인 | `requirement`·`decision`의 `stable` 전이, 온톨로지 확장, 학습 판정자 결과 | human | 5.4, 2.5, 8.14 | 규약 — `verified` 목록·`status: approved`. 사람 검토 실측 0 |
| 트러스트 | `generatedBy` 없음, 검증 뒤 수정 | shape | 2.12 | **있음** — `trust-shapes` |
| 참조 무결성 | 인용 대상·부분·가정·요구가 실재하지 않음 | verify + 생성 | 4.8 | **있음** — `extract_refs`·`validate` dangling |

기계화 9 · 부분 2 · 규약 2 · 없음 8. 없음의 대부분이 도입 3·5·7단계의 산출에 걸려 있다.

## 골격 층 — 두 KB가 공유하는 도구

### 검사 (있음)

```bash
bazel test //...                 # 게이트 전체 (커밋 전 필수)
bazel run //tools:validate -- --ontology <files> --shapes <files> --odd <files> --data <files>
bazel run //tools:chunk_lint -- --chunks <files> --ttl <files>
bazel run //tools:canonicalize -- --write <files>    # 커밋 전 정규화
bazel run //tools:term_propose -- --id <slug> --kind class --parent agt:… \
    --label-ko … --label-en … --definition … --cq CQ#   # 용어 제안 → 승인 큐
bazel build //kb/odd:odd //kb/dev:index              # 생성물: ODD 그래프·택소노미, 라벨 목록
tools/relock.sh                                      # 파이썬 의존성 재고정
```

#### 검사 3계층 (노트 2.5절 — 온톨로지 컴파일러)

| 계층 | 정의 | 이 저장소 |
|---|---|---|
| 구문·스타일 (report) | 라벨·정의 누락, 참조 구문, 폐기 규약 | `validate.py`의 labels·boundary + `chunk_lint` |
| **안티패턴** (verify) | "이런 트리플이 존재하면 실패"를 SPARQL로 명세 | `validate.py --verify-queries` — `tools/verify-queries/*.rq` 하나가 안티패턴 하나. 현재 5종: 출처 빈 청크 · 외부 유입 연쇄 · 기준 없는 verifies · 지지 없는 확정 · 반박된 확정 |
| 논리 정합성 (reason) | OWL 추론기 (RL 프로파일 안) | SHACL + `--reason`(OWL-RL). shape로 자연스러운 것(거주표·카디널리티)은 shape에 남긴다 |

**용어 제안 워크플로**(`term_propose`) — 상승이 온톨로지에 닿을 때: 에이전트는 신뢰할 수
없는 센서이므로 제안만 하고, 검사(상위 실재·라벨 중복·정의 형식)를 통과한 것만
`kb/ontology/proposals/` 승인 큐에 오른다. 큐는 `//kb/ontology:modules` 밖이라 승인 전에는
그래프에 들어가지 않는다.

#### `validate.py` — 그래프 게이트

| 검사 | 강제하는 것 | 규칙 |
|---|---|---|
| `syntax` | 모든 TTL이 파싱된다 | — |
| `labels` | `agt:` 용어마다 한/영 `rdfs:label` + `skos:definition` | [ontology §확장 규칙](ontology.md#확장-규칙) |
| `boundary` | 한 용어는 한 모듈 파일에서만 정의된다 | 같음 |
| `vocab` | 데이터의 술어가 온톨로지 또는 등록된 표준 어휘 안 | [rules §어휘 폐쇄](rules.md#어휘-폐쇄) |
| `odd-ref` | `agt:refersTo`의 대상이 ODD에 존재한다 | [rules §가정](rules.md#가정) |
| `dangling` | `cites`·`hasDirectPart`·`assumes`·`refines`·`satisfies`가 가리키는 항목이 실재한다 | [rules §4](rules.md#4-traceability--인터페이스를-기준축으로-한-mapping) |
| `verify` | 안티패턴 질의 결과 행 = 위반 | 위 표 |
| `shacl` | shape 적합성 (아래) | [rules](rules.md) |

`vocab`이 핵심 방어선이다 — 어휘 우회를 막지 못하면 나머지 규칙이 전부 우회된다.

#### SHACL shape — `kb/ontology/shapes/`

| 파일 | 대상 | 주요 제약 |
|---|---|---|
| `chunk-shapes.ttl` | `agt:Chunk` | `lineCount` ≤ 42 · `hasLevel` 정확히 1 · 한/영 라벨 각 1 · `status` 값 |
| `composite-shapes.ttl` | `agt:Composite` | `hasDirectPart` ≤ 9 |
| `residency-shapes.ttl` | plane별 | plane×level 상주표 |
| `condition-shapes.ttl` | `agt:Condition`·`agt:ODD` | 조건마다 `checkMethod` 필수 · 등급 A–D · ODD는 조건 ≥ 1 |
| `assumption-shapes.ttl` | `agt:Assumption` | ODD 조건을 `refersTo` ≥ 1 · `proposition` 필수 |
| `scope-shapes.ttl` | `agt:Scope` | `mode` 고정 · `subsetOf`로 어느 ODD의 부분집합인지 |
| `trust-shapes.ttl` | `agt:Chunk` | `generatedBy` 필수 · `generatedAtTime ≤ verifiedAt`(검증 뒤 수정 금지) |

라벨 제약은 `sh:qualifiedValueShape` + `sh:qualifiedMinCount`로 쓴다 — `sh:languageIn`은
*모든* 값에 적용되어 "한글 하나 + 영어 하나"를 표현하지 못한다.

#### `chunk_lint.py` — 파일 게이트

`chunk`: 본문 42줄 이하(`.md`는 frontmatter 제외, `.ttl`은 `@prefix`·주석·빈 줄 제외).
`naming`: 파일명 접미사 규약(`-ontology`/`-rules`/`-shapes`/`-space`/`-kg`/`-odd`).
**온톨로지 파일도 42줄 규율을 받는다** — chunk는 포맷이 아니라 구조 규율이기 때문이다.

#### 생성기 = 검사기

| 도구 | 입력 → 산출 | 실패 조건 |
|---|---|---|
| `chunk2kg.py` | 청크 frontmatter → `kg/chunks-kg.ttl` (head·구성체·contentHash) | 필수 키 7개 누락, 값 어휘 밖, **IRI 중복**, 구성체 미선언 — "한 chunk는 한 파일"의 기계적 강제 |
| `extract_refs.py` | 본문의 `d-NNNN` 인용 → `references-kg.ttl`의 `agt:cites` | 인용 대상이 실재하지 않음 |
| `odd2kg.py` + `taxonomy.py` | OpenODD 문서 `kb/odd/project-odd.yml` → `project-odd.ttl`; `related/condition` → `taxonomy.yml` (부록 E.4) | 택소노미 밖 범주, 판정 방법·등급 없는 조건 |
| `labels.py` | 청크 head → OKF `index.md` (5.6절) | frontmatter 오류 |

`kb_yaml.py`는 YAML **부분집합** 로더 — 잠금이 순수 파이썬 휠만 허용해 PyYAML을 못 넣은
부채다 ([`open-questions.md`](open-questions.md) §3). 생성물은 `bazel-bin`에만 있고 소스 트리에
같은 이름의 파일을 두지 않는다 (`index.md`·`log.md` 포함).

### 검사 (없음) — `odd_check`(COD 대조·이탈 감지, 3.5절) · `assume_check`(가정 판정식 실행, 6.9절). 도입 2·4단계.

### 활용 (없음)

**하나도 구현되어 있지 않다.** 검사만 있고 활용이 없다는 것이 현재의 가장 큰 공백이며,
활용 도구가 없으면 "온톨로지를 활용하는 방법론"이 성립하지 않는다.

| 도구 | 대응 절차 | 하는 일 | 단계 |
|---|---|---|---|
| `workset` / `labels` | [method §8 조회](method.md#8-조회) | 스코프 × level 창 → 작업 집합. 라벨 목록 → 펼치기 → 예산 패킹 (`labels`의 첫 형태는 `index.md` 생성기) | 2 |
| `link` | [method §6 연결](method.md#6-연결) | 구축 기록 → 후보, 복원 파이프라인 k≤7 | 3·8 |
| `propagate` / `revalidate` | [method §7 갱신](method.md#7-갱신) | 무효화 전파 8단계 · 재판정 큐, 규칙 카탈로그 8종 | 4 |
| `query` | [competency-questions](competency-questions.md) | CQ1~20과 표준 추적 질의 | 3 |
| `impact` | [method §12 영향 분석](method.md#12-영향-분석) | 변경 전 의존 집합·승인 필요 수 | 3 |
| `project` | [method §9 투영](method.md#9-투영) | tangle·weave·매트릭스·보고. 저장하지 않고 질의 | 8 |
| `metrics` | [methodology 완료 판정](methodology.md#완료-판정) | 고아율·링크 밀도·suspect 비율·누락률·라벨 대표성·**CQ19·CQ20** | 1 |

`metrics`가 없어 지표를 손으로 세고 있다. 도구가 생기면 문서는 수치를 적지 않고 생성물을
인용한다 (d-0075).

## development 층 — 개발 KB의 도구 (노트 Part VII, 전부 미구현)

| 도구 | 하는 일 | 규칙·절차 |
|---|---|---|
| `gate` | 전이 게이트 4종 — 봉사 명시 / 범위·제약 / 표본 근거 / 기준 바인딩 (6.8) | [rules development](rules.md#development-규칙--개발-kb-노트-7277) |
| `space_check` | `-space` 호 일관성 · ODD 경계 · `when` 평가 · 장부 규칙 · 확정 제안 (9.10, 9.11) | [method §5](method.md#5-후보-관리) |
| `feedback` | `-space` → 체크박스 파일 · 되읽기 → 확정 (13.5) | [p9-candidate-storage](../kb/dev/decision/p9-candidate-storage/conclusion.md) |
| `contract_check` | 계약 선행 · 타입 · 사후조건 CEL 실행 가능성 (7.5) | [p7-contract-first](../kb/dev/decision/p7-contract-first/conclusion.md) |
| `schema_compat` | 하위 호환 판정, 비호환이면 새 IRI + `supersedes` (7.6) | [p7-schema-derivation](../kb/dev/decision/p7-schema-derivation/conclusion.md) |
| `adr` | 결정 구성체 투영 (7.4) | [p7-alternatives-mandatory](../kb/dev/decision/p7-alternatives-mandatory/conclusion.md) |
| `tangle` | 구현 청크 → 코드 파일 (4.6) | [method §9](method.md#9-투영) |
| `dev_metrics` | 하강 완주율 · 상향 귀속률 · 결정 완결률 · `-space` 체류 · 계약 선행률 · 대안 기록률 (7.8) | [p7-dev-kb-outputs-and-metrics](../kb/dev/decision/p7-dev-kb-outputs-and-metrics/conclusion.md) |

## V&V 층 — V&V KB의 도구 (노트 Part VIII, 도입 7단계, 전부 미구현)

| 도구 | 하는 일 | 절 |
|---|---|---|
| `goal_derive` | 요구 → 검증 목표 후보 | 8.19 |
| `scenario_lint` | 변수가 ODD 속성인가 · 부류 참조 · 배제 자극 존재 · 자극 ≠ 기준 | 8.22 |
| `case_gen` | `keep(범위)` + `cover()` → concrete 케이스. 규칙·seed를 provenance에 | 8.23 |
| `verifier_bind` | 기준 바인딩 검사. 기준 없는 `verifies` 거부 | 8.11 |
| `env_assign` | 결함 요인 → 환경 단계, 재현성 조건 | 8.10, 8.12 |
| `run` | 실행기. 리비전·seed·환경 버전 기록, 실행 기록 append | 8.15 |
| `judge` | 판정. 학습된 판정자면 3지표 검사, 결과를 head `verified` 목록에 | 8.14, 2.12 |
| `mutate` | 변이 주입 표본 검사 | 8.6 |
| `coverage` | 하강 완주 · 상향 귀속 · logical 공간 커버, 경계값 별도, 6단계 제외 | 8.7 |
| `defect_classify` | `defect-rules` 추론: 요인·한정자·트리거·발견 단계 | 8.16~8.18 |
| `sim_trust` | 시뮬레이션 신뢰도 요인별 상관 | 8.13 |
| `vv_report` | 검증 상태 · 커버리지 · 결함 · 가정 건전성 · 독립성 | 8.24 |
| `independence_audit` | 개발 역할의 V&V KB 쓰기 흔적 = 0 | 8.5 |
| `vv_metrics` | 목표 파생률 · 기준 바인딩률 · V&V 완주율 · 실행 통과율 · 변이 검출률 · 재현 실패율 · 가로대 지연 | 8.26 |
| `diagnose` | 불만족 핵 · 보간 · 최약 전제조건 · 명세 추론. 결과는 관측 청크 | [12.12](../kb/dev/decision/p12-symbolic-diagnosis/conclusion.md) |
| `guide` | 지도 청크 생성 — 귀속 후보 · 조치 · 배제된 전략 | [8.4](../kb/dev/decision/p8-mismatch-attribution/conclusion.md) |
| `proactive_vv` | 선제 트리거 감시(ODD 경계 · 커버리지 공백 · 외부 지식 · 증거 노화), 재실행 선택 | [8.27](../kb/dev/decision/p8-proactive-vv/conclusion.md) |

## Bazel 배선

```
//:gate  (test_suite)
├── //:naming_test                 TTL 접미사 규약
├── //chunks:lint_test             `chunks/` 항목 42줄
├── //kb/dev:lint_test             개발 KB 청크 42줄
├── //kb/ontology:gate_test        labels · boundary · SHACL
├── //kb/odd:gate_test             ODD shape  ← //kb/odd:odd (odd2kg) · :taxonomy
└── //kg:gate_test                 vocab · odd-ref · dangling · verify · SHACL
                                    ← //kg:chunks_kg · //kg:references_kg 를 입력으로
생성물: //kb/odd:odd · //kb/odd:taxonomy · //kb/dev:index
```

`//kb/ontology:chunk_lint_test`는 `bazel test //...`로는 돌고 `//:gate`로는 안 돈다. 배선은
`defs/knowledge.bzl`의 매크로(`kb_gate_test`·`kb_chunk_kg`·`kb_reference_kg`·`kb_chunk_lint_test`·
`kb_odd_kg`·`kb_taxonomy`·`kb_index`)로만 선언하며 `py_test`를 직접 쓰지 않는다.

## 게이트 밖 — 규약으로 남은 것

**여기 적히지 않은 채 게이트도 없는 규칙은 사실상 없는 규칙이다.**

| 규칙 | 왜 게이트가 아닌가 | 어디에 |
|---|---|---|
| 라벨이 본문을 대표한다 | 판정 불가 | `STYLEGUIDE.md` §4 |
| 한 chunk는 한 주제 | 판정 불가. 42줄과 분할 신호가 대리 지표 | `STYLEGUIDE.md` §0 |
| 구성체 동질성·순환 | 분석 시점 검사 — plane별 규칙 전환(3단계)까지 미구현 | [rules §2](rules.md#2-구성체--통합이-필요한-것만) |
| 대안 청크 필수 | shape로 가능하나 미구현 (구성체 멤버 역할이 그래프에 없다) | [rules development](rules.md#development-규칙--개발-kb-노트-7277) |
| 카탈로그 정합성 (역할별 read plane ≥ 1, write plane 비공유, `maxConcurrent` 합 ≤ ODD 동적 요소) | 기계화 가능하나 미구현 | `AGENTS.md` 역할 절 |
| 정규화 직렬화 | `canonicalize.py --check`가 있으나 테스트 타깃이 아니다 | [rules §정규화](rules.md#정규화-직렬화) |

카탈로그 정합성 검사가 없어 ODD의 동시 에이전트 한도와 카탈로그의 합이 한동안 어긋난 채
지나간 적이 있다 — 규약만으로는 지켜지지 않는다는 증거다.

## 도구 작성 규칙

- 실패 시 비영 종료 + `FAIL [검사명]` 접두사 + 근거 인용 — 메시지가 곧 수정 안내다.
- 새 검사는 독립 함수 `check_*() -> list[str]`로 추가하고 `main`에서 합류한다.
- 규약 상수(접미사·네임스페이스)의 단일 정의처는 `tools/kb_lib.py`다.
- 생성기는 검사기다 — 생성 실패가 곧 게이트 실패이고, 생성물은 소스 트리에 두지 않는다.
- 검사를 약화하는 변경(삭제·예외 추가)은 유저 승인 사항이다.
