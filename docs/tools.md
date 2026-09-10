# tools — 검사 도구와 활용 도구

도구는 두 갈래다. **검사 도구는 [`rules.md`](rules.md)의 기계 형태**이고, **활용 도구는
[`method.md`](method.md)의 기계 형태**다. 도구 하나가 규칙 하나 또는 절차 하나에 대응한다 —
method 목록이 도구 목록을 낳는다.

## 하네스는 Bazel이다

지식 산출물은 데이터 타깃, 검사 게이트는 테스트 타깃이고 `bazel test //...` 한 번이 게이트
전체다. 근거와 기각된 대안은 [`id:chunk-d0001`](../chunks/decision/d-0001-bazel-harness.md).

| 체계의 요구 | Bazel의 성질 |
|---|---|
| 바뀐 지식만 재판정 (d-0106 재판정 경계) | 입력 해시 기반 캐시 — 바뀐 파일의 게이트만 다시 돈다 |
| 산출물 간 의존을 명시 | BUILD 그래프가 의존을 선언으로 강제 |
| 판정 도구의 재현성 | hermetic 툴체인 + 해시 고정 lock |
| 게이트 우회 금지 | 테스트 타깃이라 우회하려면 BUILD를 고쳐야 한다 — 리뷰에 걸린다 |

**판정 가능한 것만 게이트로 만든다.** 기계가 판정할 수 없는 규칙은 게이트에 넣지 않고
`STYLEGUIDE.md`의 `[지킴]`으로 남기며, 게이트에 넣을 수 없다는 사실 자체를 §"게이트 밖"에
기록한다. shape은 **강화만** 한다 — 제약 완화는 유저 승인 사항이다.

## 검사 도구 (있음)

```bash
bazel test //...                 # 게이트 전체 (커밋 전 필수)
bazel test //:gate               # 같은 것 (test_suite)

bazel run //tools:validate -- --ontology <files> --shapes <files> --odd <files> --data <files>
bazel run //tools:chunk_lint -- --chunks <files> --ttl <files>
bazel run //tools:canonicalize -- --write <files>    # 커밋 전 정규화
bazel run //tools:term_propose -- --id <slug> --kind class --parent agt:… \
    --label-ko … --label-en … --definition … --cq CQ#   # 용어 제안 → 승인 큐
tools/relock.sh                                      # 파이썬 의존성 재고정
```

### 검사 3계층 (노트 v3 2.5절 — 온톨로지 컴파일러)

v3가 검사를 세 계층으로 재편했고, 이 저장소의 대응은 다음과 같다.

| 계층 | v3의 정의 | 이 저장소 |
|---|---|---|
| 구문·스타일 | 라벨·정의 누락, 참조 구문, 폐기 규약 | `validate.py`의 labels·boundary + `chunk_lint` |
| **안티패턴** | "이런 트리플이 존재하면 실패"를 SPARQL로 명세 | `validate.py --verify-queries` — `tools/verify-queries/*.rq` 하나가 안티패턴 하나. 현재 4종: 출처 빈 청크 · 기준 없는 verifies · 근거 없는 확정 링크 · 신뢰 전파 위반 |
| 논리 정합성 | OWL 추론기 (RL 프로파일 안) | SHACL + `--reason`(OWL-RL). shape로 자연스러운 것(거주표·카디널리티)은 shape에 남긴다 |

**용어 제안 워크플로**(`term_propose`) — 상승이 온톨로지에 닿을 때: 에이전트는
신뢰할 수 없는 센서이므로 제안만 하고, 검사(상위 실재·라벨 중복·정의 형식)를
통과한 것만 `kb/ontology/proposals/` 승인 큐에 오른다. 큐는 `//kb/ontology:modules`
밖이라 승인 전에는 그래프에 들어가지 않는다.

### `validate.py` — 그래프 게이트

| 검사 | 강제하는 것 | 규칙 |
|---|---|---|
| `syntax` | 모든 TTL이 파싱된다 | — |
| `labels` | `agt:` 용어마다 한/영 `rdfs:label` + `skos:definition` | [ontology §확장 규칙](ontology.md#확장-규칙) |
| `boundary` | 한 용어는 한 모듈 파일에서만 정의된다 | 같음 |
| `vocab` | 데이터의 술어가 온톨로지 또는 등록된 표준 어휘 안 | [rules §어휘 폐쇄](rules.md#어휘-폐쇄) |
| `odd-ref` | `agt:refersTo`의 대상이 ODD에 존재한다 | [rules §가정](rules.md#가정) |
| `dangling` | `cites`·`hasDirectPart`·`assumes`가 가리키는 항목이 실재한다 (참조 무결성) | [rules §4](rules.md#4-traceability--인터페이스를-기준축으로-한-mapping) |
| `shacl` | shape 적합성 (아래) | [rules](rules.md) |

`vocab`이 핵심 방어선이다 — 어휘 우회를 막지 못하면 나머지 규칙이 전부 우회된다.

### SHACL shape — `kb/ontology/shapes/`

| 파일 | 대상 | 주요 제약 |
|---|---|---|
| `chunk-shapes.ttl` | `agt:Chunk` | `lineCount` ≤ 42 · `hasLevel` 정확히 1 · 한/영 라벨 각 1 · `state` 값 |
| `composite-shapes.ttl` | `agt:Composite` | `hasDirectPart` ≤ 9 |
| `condition-shapes.ttl` | `agt:Condition`·`agt:ODD` | 조건마다 `checkMethod` 필수 · 등급 A–D · ODD는 조건 ≥ 1 |
| `assumption-shapes.ttl` | `agt:Assumption` | ODD 조건을 `refersTo` ≥ 1 · `proposition` 필수 |
| `scope-shapes.ttl` | `agt:Scope` | `mode` 고정 · `subsetOf`로 어느 ODD의 부분집합인지 |
| `trust-shapes.ttl` | `agt:Chunk` | `generatedBy` 필수 · `generatedAtTime ≤ verifiedAt`(검증 뒤 수정 금지) |

라벨 제약은 `sh:qualifiedValueShape` + `sh:qualifiedMinCount`로 쓴다 — `sh:languageIn`은
*모든* 값에 적용되어 "한글 하나 + 영어 하나"를 표현하지 못한다.

### `chunk_lint.py` — 파일 게이트

| 검사 | 규칙 |
|---|---|
| `chunk` | 본문 42줄 이하. `.md`는 frontmatter 제외, `.ttl`은 `@prefix`·주석·빈 줄 제외 |
| `naming` | 파일명이 접미사 규약(`-ontology`/`-rules`/`-shapes`/`-space`/`-kg`/`-odd`)을 따른다 |

**온톨로지 파일도 42줄 규율을 받는다** — chunk는 포맷이 아니라 구조 규율이기 때문이다.

### `extract_refs.py` — 생성 겸 검사

본문의 `d-NNNN` 인용을 뽑아 `agt:cites` 링크를 방출한다. **인용 대상이 실재하지 않으면 비영
종료**하므로 "인용한 타깃이 존재하는가"가 생성 시점에 강제된다. 목록을 손으로 복제하지 않는
것이 요점이다 — 본문이 원본이고 그래프는 생성물이다.

*현재 실측: 항목 20개가 27개의 인용 링크를 만든다.*

### `odd2kg.py` · `taxonomy.py` · `kb_yaml.py` — ODD 생성 겸 검사

ODD 원본은 OpenODD 문서 `kb/odd/project-odd.yml`이다 (부록 E.4). `taxonomy.py`가 `related/condition`
온톨로지에서 속성 범주 택소노미를 생성하고, `odd2kg.py`가 문서를 `-odd.ttl`로 올리며 **택소노미 밖 범주·판정
방법 없는 조건이면 생성이 실패한다** (0.4절). `kb_yaml.py`는 YAML **부분집합** 로더 — 잠금이 순수 파이썬
휠만 허용해 PyYAML을 못 넣은 부채다 ([`open-questions.md`](open-questions.md) §3).

### `labels.py` — 라벨 목록 투영

OKF 예약 파일 `index.md`를 청크 head에서 생성한다 (5.6절, 부록 E.2). `bazel build //kb/dev:index` →
`bazel-bin/kb/dev/index.md`. 손으로 쓰지 않는다 (유저 결정 2026-09-10 Q4). 도입 1단계 도구 `labels`의 첫 형태.

### `chunk2kg.py` — 생성 겸 검사

생성기가 곧 검사기다. frontmatter 필수 키 6개, 값 어휘, **IRI 중복**을 보고 어기면 비영
종료하므로 `//kg:chunks_kg` 빌드가 실패한다. IRI 중복 검사가 "한 chunk는 한 파일"의 기계적
강제다.

### Bazel 배선

```
//:gate  (test_suite)
├── //:naming_test              TTL 접미사 규약
├── //chunks:lint_test          `chunks/` 항목 42줄
├── //kb/ontology:gate_test        labels · boundary · SHACL
├── //kb/odd:gate_test             ODD shape
└── //kg:gate_test              vocab · odd-ref · dangling · SHACL
                                 ← //kg:chunks_kg · //kg:references_kg 를 입력으로
```

`//kb/ontology:chunk_lint_test`는 정의되어 있으나 `//:gate` suite에는 들어 있지 않다 —
`bazel test //...`로는 돌고 `//:gate`로는 안 돈다. 배선은 `defs/knowledge.bzl`의 매크로
(`kb_gate_test`·`kb_chunk_kg`·`kb_chunk_lint_test`)로만 선언하며 `py_test`를 직접 쓰지 않는다.

### 게이트 밖 — 규약으로 남은 것

**여기 적히지 않은 채 게이트도 없는 규칙은 사실상 없는 규칙이다.**

| 규칙 | 왜 게이트가 아닌가 | 어디에 |
|---|---|---|
| 라벨이 본문을 대표한다 | 판정 불가 | `STYLEGUIDE.md` §4 |
| 한 chunk는 한 주제 | 판정 불가. 42줄과 분할 신호가 대리 지표 | `STYLEGUIDE.md` §0 |
| 구성체 동질성(부분의 plane·level = 전체) | 기계화 가능하나 미구현 | [rules §2](rules.md#2-구성체--통합이-필요한-것만) |
| 카탈로그 정합성 (역할별 read plane ≥ 1, 설계/구현/운영의 write plane 비공유, `maxConcurrent` 합 ≤ ODD 동적 요소) | 기계화 가능하나 미구현 | `AGENTS.md` 역할 절 |
| 정규화 직렬화 | `canonicalize.py --check`가 있으나 테스트 타깃이 아니다 | [rules §정규화](rules.md#정규화-직렬화) |

(결정 역할 태그 검사는 v3 재도출로 소멸했다 — 결정이 결론·근거·대안 세 파일의
구성체가 되면서 역할이 파일 구조 자체가 되었다.)

카탈로그 정합성 검사가 없어 ODD의 동시 에이전트 한도와 카탈로그의 합이 한동안 어긋난 채
지나간 적이 있다 — 규약만으로는 지켜지지 않는다는 증거다.

## 활용 도구 (없음)

**하나도 구현되어 있지 않다.** 검사만 있고 활용이 없다는 것이 현재의 가장 큰 공백이며,
활용 도구가 없으면 "온톨로지를 활용하는 방법론"이 성립하지 않는다.

| 도구 | 대응 절차 | 하는 일 |
|---|---|---|
| `workset` / `labels` | [method §8 조회](method.md#8-조회) | 스코프 × level 창으로 거른 작업 집합 조립. 라벨 목록 → 펼치기 → 예산 패킹 |
| `link` | [method §6 연결](method.md#6-연결) | 의미 의존·관련성 **후보** 제안. 본문 인용 추출은 `extract_refs`가 이미 한다 |
| `query` | [ontology 경쟁 질문](ontology.md#경쟁-질문--온톨로지의-요구사항이자-완료-판정) | 경쟁 질문과 표준 추적 질의 실행 |
| `impact` | [method §12 영향 분석](method.md#12-영향-분석) | 변경 전 의존 집합·무효화 후보·승인 필요 수 산출 |
| `project` | [method §9 투영](method.md#9-투영) | tangle·weave·문서·추적 매트릭스 |
| `metrics` | [methodology 완료 판정](methodology.md#완료-판정) | 청크 수·고아율·크기 분포·링크 밀도·가정 건전성·**하강 완주율(CQ19)·상향 귀속률(CQ20)** 산출 |
| `propagate` / `revalidate` | method §갱신 | 무효화 전파와 재판정 큐 처리 — v3 도구 목록의 추가분 |
| `odd_check` / `assume_check` | method §갱신 | ODD 이탈 대조·가정 판정식 실행 — v3 검사 추가분 |

`metrics`가 없어 지표를 손으로 세고 있다. **문서에 수치를 적으면 반드시 낡으므로**, 도구가
생기면 문서는 수치를 적지 않고 생성물을 인용한다 (d-0075의 투영 원칙).

### V&V 층 도구 (도입 7단계, 구조도 v5)

`goal_derive` · `scenario_lint` · `case_gen` · `verifier_bind` · `env_assign` · `run` · `judge` ·
`mutate` · `coverage` · `defect_classify` · `sim_trust` · `vv_report` · `independence_audit` ·
`vv_metrics` · **`diagnose`**(불만족 핵·보간·최약 전제조건·명세 추론, 12.12절) · **`guide`**(귀속·조치·대안의
지도 청크, 8.4절) · **`proactive_vv`**(선제 트리거 감시, 8.27절). 전부 미구현. 검사 층의 verify 질의에는
장부 규칙 둘이 이미 있다 — `confirmed-without-evidence.rq`·`confirmed-with-refutation.rq`.

## 도구 작성 규칙

- 실패 시 비영 종료 + `FAIL [검사명]` 접두사 + 근거 인용 — 메시지가 곧 수정 안내다.
- 새 검사는 독립 함수 `check_*() -> list[str]`로 추가하고 `main`에서 합류한다.
- 규약 상수(접미사·네임스페이스)의 단일 정의처는 `tools/kb_lib.py`다.
- 검사를 약화하는 변경(삭제·예외 추가)은 유저 승인 사항이다.
