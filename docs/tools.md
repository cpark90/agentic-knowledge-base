# tools — 검사 도구와 활용 도구, 세 층

검사 도구는 [`rules.md`](rules.md)의 기계 형태다. 활용 도구는 [`method.md`](method.md)의 기계 형태다.
도구 하나가 규칙 하나 또는 절차 하나에 대응한다. 구조도 v5에 따라 **코어 / development / V&V**
세 층으로 적는다. 코어 도구는 두 KB가 공유하고, 나머지는 각 KB의 규칙·절차를 수행한다.

## 하네스는 Bazel이다

지식 산출물은 데이터 타깃이고 검사 게이트는 테스트 타깃이다. `bazel test //...` 한 번이 게이트
전체다. 근거와 기각된 대안은 [`id:chunk-d0001`](../chunks/decision/d-0001-bazel-harness.md)에 있다.
plane별 규칙·deps=링크로의 전환은 [`pe-bazel-rules`](../kb/dev/decision/pe-bazel-rules/conclusion.md)에 있다 (도입 3단계).

| 체계의 요구 | Bazel의 성질 |
|---|---|
| 바뀐 지식만 재판정 (d-0106 재검증 시점) | 입력 해시 기반 캐시 — 바뀐 파일의 게이트만 다시 돈다 |
| 산출물 간 의존을 명시 | BUILD 그래프가 의존을 선언으로 강제 |
| 판정 도구의 재현성 | hermetic 툴체인 + 해시 고정 lock |
| 게이트 우회 금지 | 테스트 타깃이라 우회하려면 BUILD를 고쳐야 한다 — 리뷰에 걸린다 |

**판정 가능한 것만 게이트로 만든다.** 기계가 판정할 수 없는 규칙은 게이트에 넣지 않고
`STYLEGUIDE.md`의 `[지킴]`으로 남긴다. 게이트에 넣을 수 없다는 사실 자체는 §"게이트 밖"에
기록한다. shape은 **강화만** 한다. 제약 완화는 유저 승인 사항이다.

## 게이트 총람 — 이 문서가 원본이다

노트 6.7절의 총람을 이 저장소의 실측과 함께 둔다 ([`p6-gate-catalogue`](../kb/dev/decision/p6-gate-catalogue/conclusion.md)).
실행 계층: **shape**(SHACL, 청크 단위, 즉시) / **verify**(SPARQL, 그래프 단위, 재검증 시점) /
**analysis**(Bazel 분석 시점, 빌드 실패) / **test**(실행, `bazel test`) / **human**(승인).
게이트에 걸린 청크는 `draft`에 머물고 하류로 전파되지 않는다.

| 게이트 | 무엇을 거부하는가 | 계층 | 절 | 이 저장소 | id | 해소 (누가·어디서) |
|---|---|---|---|---|---|---|
| 청크 형식 | 42줄 초과, 라벨 누락, plane·level 유일성 위반, `type`이 온톨로지 밖 | shape | 4.4 | **있음** — `chunk_lint` + `chunk2kg` + `chunk-shapes` | `chunk` · `chunk2kg` | 청크를 고친다 — plane의 write 역할(요구·결정 orchestrator, 산출물 developer) |
| 수준 허용표 | plane에 허용되지 않는 level | shape | 6.4 | **있음** — `residency-shapes` | `shacl`(residency) | level 또는 plane을 고친다 — 저작자 |
| 복합체 | 부분의 plane·level 불일치, 직접 부분 > 9, 순환 | analysis + verify | 4.5 | **있음** — `composite-shapes`(≤9) · `kb_decision`(결정의 세 부분·수준·`ordered`가 부분 집합과 일치, 분석 시점) · verify 질의 `composite-heterogeneous`·`composite-cycle`(전체 복합체, 2026-09-13; 수준 동질성은 결정 복합체 제외) · `kb_composite`(부분 2~9 · plane·level 한 쌍, 분석 시점, 2026-09-29) · `gen_build._check_bundle`(묶음 = 패키지 × `composite.id`, 생성 시점 — 패키지 밖 부분·중복 선언·이질·상한·`ordered`와 부분 집합의 불일치) · `composite-order-shapes`(순서 있는 복합체의 색인 1..n 연속·중복 없음·부분 집합과 일치, 2026-09-29) | `shacl`·`gen-build`·`verify` | 복합체 선언·세 청크를 고친다 — 저작자 |
| 통제 어휘 | 온톨로지에 없는 술어·개체, 표준 어휘 원문에 없는 prov·skos 용어 | verify | 0.0, 2.12 | **있음** — `validate` vocab (+ `--standard-vocab`, 2026-09-12) | `vocab` | 온톨로지에 개념을 먼저 더하거나(`term_propose` → 승인) 술어를 정정한다 — developer(T-Box) |
| 출처 | `sources`가 빈 청크, 파생 연쇄 전체가 외부 유입인 확정 청크 | verify | 4.3, 2.12 | **있음** — `sources-empty.rq`·`imported-chain-confirmed.rq` | `verify` | `sources`를 보강한다 — 저작자 |
| TIM | 링크 타입의 정의역·치역 밖 plane, 카디널리티 초과, 단방향 규칙 위반 | analysis | 10.1 | **부분** — `defs/kb.bzl` 규칙이 `refines`(상위 수준·plane 단방향)·`serves`(요구만)·`supersedes`(같은 plane)·`verifies`(V&V 주어·같은 수준)를 분석 시점 `fail()`로, 끊긴 링크는 로드 에러, 방향은 `package_group` 가시성 (2026-09-11) | `tim`(`defs/kb.bzl` 분석 시점) | 링크의 방향·수준을 고친다 — 저작자. 규칙 변경은 유저 승인 사항이다 |
| ODD 참조 | ODD에 없는 조건을 참조하는 스코프·가정·시나리오 변수 | verify | 3.3 | **있음** — `validate` odd-ref | `odd-ref` | ODD를 먼저 확장하거나(developer, design 겸임) 참조를 정정한다 |
| ODD 경계 | 후보 값·케이스 값이 ODD 범위 밖 | verify | 9.10 | 없음 (5단계 `space_check`) | — | 5단계 |
| 기여 | `serves` 없는 abstract 결정 | verify | 6.8 | 없음 — abstract 결정 자체가 아직 없다 | — | — |
| 범위·제약 | 범위 없는 logical 변수, 실행 불가한 사후조건 | shape + test | 6.8 | 없음 (5단계) | — | 5단계 |
| 검증 대응물 | 같은 높이의 V&V 대응물(목표·기준·검증기) 부재 | verify | 8.3 | 부분 — 사슬 8(2026-09-19)이 concrete 높이에서 결정 결론을 `verifies`한다. 대응물 부재를 거부하는 게이트는 없음 — `metrics` 7단계 절이 비율을 잰다 | — | 7단계 |
| 표본 근거 | `sampling` 없는 concrete 값·케이스 | shape | 6.8, 8.23 | 없음 (5·7단계) | — | 5·7단계 |
| 할당 근거 | 후보가 둘 이상인데 확정된 링크, 배제 근거 없는 기각 | verify | 9.10 | 부분 — 증거 기록 규칙 2 질의(`confirmed-without-evidence`·`confirmed-with-refutation`); 확정 링크 577(구축 548 · 복원 29), 후보 링크 30(본문 추출, 2026-09-19); 상태·클래스 불일치 질의 `link-state-class-mismatch` | `verify` | 증거 항목을 더하거나 확정을 후보로 되돌린다 — 저작자 |
| 기준 바인딩 | 기준 없는 `verifies`, 판정식 없는 기준 | shape | 8.11 | **있음** — `verifies-without-criteria.rq` | `verify` | vnv가 기준 청크를 만들고 `verifies`를 바인딩한다 |
| 대안 기록 | 대안 청크 없는 결정 | shape | 7.4 | **있음** — `kb_decision` 의 `alternatives` 가 필수 속성이고, `gen_build` 가 세 청크 없는 디렉토리를 거부한다 (로드 시점) | `gen-build` | `alternatives.md`를 쓴다 — orchestrator |
| 계약 선행 | 계약보다 먼저 확정된 구현 | verify | 7.5 | 없음 — `contract` plane 항목 0 | — | — |
| 판정 도구 | 컴파일·타입·스키마·린터 실패 | test | 5.4 | 없음 — `artifact` plane 항목 0 | — | — |
| 독립성 | 개발 역할이 V&V KB에 쓴 흔적 | verify | 8.5 | 부분 — 의존 방향(개발 → V&V 금지)은 `//kb:vv_readers` 가시성으로 분석 시점에 차단한다. 쓰기 흔적 검사는 없다 | `visibility`(`//kb:*_readers`) | 의존 방향을 되돌린다 — developer |
| 승인 | `requirement`·`decision`의 `stable` 전이, 온톨로지 확장, 학습 판정자 결과 | human | 5.4, 2.5, 8.14 | 규약 — `verified` 목록·`status: approved`. 사람 검토 실측 10(2026-09-11 라벨 재판정) | `writer` | 쓰기 권한 역할이 검토 뒤 `endorse` — orchestrator·vnv |
| 신뢰 등급 | `generatedBy` 없음, 검증 뒤 수정 | shape | 2.12 | **있음** — `trust-shapes` | `shacl`(trust) | `generated.at` ≤ `verified.at`가 되게 검증 표시를 물리거나 다시 찍는다 |
| 참조 무결성 | 인용 대상·부분·가정·요구가 실재하지 않음 | verify + 생성 | 4.8 | **있음** — `extract_refs`·`validate` dangling | `dangling` · `extract-refs` | 인용 대상을 정정한다 — 저작자 |
| 산문 문체 | 경어체 종결(`습니다`·`세요`·`해요` 등), 산문의 느낌표 | test | STYLEGUIDE §0 | **있음** — `chunk_lint`·`doccheck`의 `prose` (2026-09-13). 추측·구어·대시 밀도는 `consistency` ⑦이 보고한다 | `prose` | 문장을 고친다 — 저작자. 고유명사의 느낌표는 `waivers.md` |
| 수준 허용표 단일 정의처 | `residency-shapes.ttl` 의 구간이 `defs/kb.bzl` 의 `RESIDENCY` 와 갈림 | verify | 6.4 | **있음** — `validate check_residency` (2026-09-26). 원본은 `defs/kb.bzl`(Starlark 는 파일을 읽지 못해 분석 시점 판정을 지키려면 표가 거기 있어야 한다)이고 `kb_lib.load_residency` 가 리터럴로 읽어 파생한다. `metrics` 의 사본은 제거됐다 | `residency` | shape 를 원본에 맞춘다 — developer |
| 링크 비순환 | `refines`·`supersedes`·`hasDirectPart` 의 반사·순환 | verify | 6.2·7.4·4.5 | **있음** — 질의 `refines-cycle`·`supersedes-cycle`(2026-09-26 신설)·`composite-cycle`. 공리(`owl:IrreflexiveProperty`·`TransitiveProperty`)는 선언이고 판정은 질의다 — pySHACL 의 rdfs·owlrl 추론이 비반사성 위반을 보고하지 않는다(고정물로 실측) | `verify` | 순환을 끊는다 — 저작자 |
| 주석의 수준 상속 | 주석의 `hasLevel` 이 `targets` 대상 어느 것의 수준과도 다름 | verify | 7.7 | **있음** — 질의 `comment-level-not-inherited`(2026-09-26). 대상이 여럿이면 그중 하나와 같으면 통과 | `verify` | 주석의 수준을 대상에 맞춘다 — vnv |
| 태그 값 | `taggedWith` 값이 온톨로지 개념이 아니거나 범주에 미등록 | shape | 0.5 | **있음** — `tag-shapes.ttl`(2026-09-26). 사용 0 이라 위반 0 | `shacl`(tag) | 값을 개념으로 바꾼다 — 저작자 |
| 실행기 환경 격리 | 케이스의 명령이 실행기의 파이썬·runfiles 문맥을 물려받음 — 걷어내는 변수가 다섯과 다르거나, `clean_env()` 뒤에 남거나, 작업 디렉토리가 워크스페이스 루트가 아님 | test | 8.15 | **있음** — `//tools:vv_run_env_test` (2026-09-23). 판정 대상을 실행기 전체가 아니라 격리의 동작으로 좁혀 **중첩 bazel 을 피했다**. **선언된 예외 하나** — `//tools:vv_run_env_test` 자신이 `env_inherit = ["HOME"]`(실측 일치를 위해 호스트 `HOME`을 물려받는다). 그 수(≤1)는 ODD 조건 [`id:cond-host-env-inherit`](../kb/odd/project-odd.yml)가 `bazel query 'attr(env_inherit, "HOME", tests(//...))'` 의 행 수로 판정한다(2026-09-29) | `vv-run-env` | 걷어낼 변수를 바꾸려면 결정 [`p8-verifier-env-isolation`](../kb/dev/decision/p8-verifier-env-isolation/conclusion.md)과 검사의 기대를 같은 커밋에서 고친다 — developer |
| 작업 집합 예산 | 앵커가 있는 작업 집합 뷰(라벨 목록 + 펼친 본문)가 문서 전체로 예산(200줄)을 넘음 — **앵커가 있을 때만** 판정한다. 앵커 없는 뷰(스코프 전체 라벨 목록)는 구조적으로 예산을 넘어 판정 밖이다 | analysis | 5.6, 11.3 | **있음** — `tools/workset.py`(2026-09-29). `bazel build //kg:workset --//kb:anchor=…`가 종료 코드로 판정한다 | `workset-budget` | 앵커의 이웃 구성이나 청크 크기를 줄인다 — 저작자. 예산 값(200줄)은 결정 `p1-context-budget-breakdown`이 정한다 |
| V&V 케이스 형식 | 기계가 읽는 자극·기대의 규약 위반 — `files`·`expect` 밖의 키, `expect` 수가 명령 수와 다름, 이름에 경로, 명령이 가리키지 않는 자극, 미해결 `{{이름}}`, 검증기를 `bazel run`으로 부르는 명령 | analysis | 8.20 | **있음** — `vv_run` (2026-09-23). `bazel test //...` 밖이고 `bazel run //tools:vv_run` 이 판정한다 — 케이스가 `bazel test` 를 부르므로 실행기 전체는 테스트 타깃이 될 수 없다. 다만 **환경 격리는 `//tools:vv_run_env_test` 로 테스트 안에 있다** — 그 검사는 케이스를 하나도 돌리지 않는다 | `vv-case` | 케이스의 `yaml` 펜스를 규약(`files`·`expect`)에 맞춘다 — vnv. 면제는 `waivers.md`(축 `파일`·`stem`) |
| 해소되지 않은 차단 주석 | `issue (blocking)` 이면서 `해소: 열림` 인 살아 있는 주석 | test | 7.7 | **있음** — `chunk_lint` (2026-09-22). 대상은 살아 있는 `type: annotation` 청크이고 `deprecated`·`invalidated` 는 기록이라 막지 않는다 | `blocking-comment` | 대상을 고친 뒤 `해소: 해소 — <이유>`로, 받지 않기로 했으면 `해소: 기각 — <이유>`로 바꾼다 — 저작자. 면제는 `waivers.md`(축 `파일`) |
| 설계 공간 | 근거 없는 배제(`eliminated` 인데 `eliminated_by` 없음), 확정 후보가 정확히 하나가 아닌 `resolved`, 후보의 출발점·링크 타입이 변수와 불일치, 실재하지 않는 IRI, 같은 변수를 두 파일이 선언 | analysis + verify | 9.10 | **있음** — `space2kg`(생성 시점) · `validate` `check_space`(그래프 시점) (2026-09-22). `space/*-space.md` 는 `kb_chunk` 타깃이 아니라 A-Box 그래프 `//space:design_space` 로 나간다 | `space` | 후보에 근거를 붙이거나 변수를 고친다 — 저작자. 후보는 결코 `deps` 가 되지 않는다 (`p9-candidate-storage`) |
| 첨가 | 슬롯의 질문에 답하지 않는 문장 — 메타 문장(`다음과 같다`·`이 절에서는`·`아래에서 설명한다`·`앞서 말했듯`)과 채움 문구(`특이사항 없음`·`일반적인 방식을 따른다`·`추후 결정한다`) | test | STYLEGUIDE §0 | **있음** — `chunk_lint` (2026-09-22 승격, `consistency` ⑧ 수치 0). 대상은 살아 있는 청크이고 `deprecated`는 기록이라 제외한다 | `addition` | 슬롯의 질문에 답하는 문장으로 바꾸거나 지운다. 채움 자리에는 세 빈 값 — 저작자 |
| 빈 값 표기 | 세 빈 값(`없음`·`해당 없음`·`미확정`) 밖의 `N/A`·`TBD`·`미정`과 표의 단독 대시 셀 | test | STYLEGUIDE §0 | **있음** — `chunk_lint` (2026-09-22 승격) | `empty-value` | 세 값 중 하나로 바꾼다. 낱말의 산문 용법이면 `waivers.md`에 선언한다 — 저작자 |
| 목록 규칙 | 손 번호 `2.` 이상 · 항목 9개 초과 · 중첩 3단계 이상 · 항목당 240자 초과 · 빈 목록 항목 | test | STYLEGUIDE §0 | **있음** — `chunk_lint` (2026-09-22 승격). 길이는 이어지는 들여쓴 줄을 합치고 공백을 정규화한 뒤 센다 | `list-rules` | 번호를 전부 `1.`로 바꾸고, 항목 수·중첩·길이는 블록을 나누며, 빈 목록은 `없음`으로 적는다 — 저작자 |
| 본문 슬롯 | 틀이 요구하는 슬롯 표지 누락 — 요구·검증 목표·결정 세 청크·합격 기준·케이스의 일곱 틀 | shape | STYLEGUIDE §0 | **있음** — `*-body-shapes.ttl` 넷 (2026-09-22). `chunk2kg`가 본문에서 표지를 찾아 `agt:bodySlot`으로 내고 shape가 판정한다. 슬롯마다 등록 질문이 `sh:description`에 있다. V&V 시나리오의 **자극**·**요인**·**배제 자극**은 새 틀이 아니라 결정 틀의 세 슬롯에 사상된 표지다 (2026-09-29). **표지는 자리로 판정한다**(2026-09-29 실측 — 본문 중간의 굵은 강조가 표지로 잘못 잡힌 오탐 4건). 굵은 span 이 그 줄의 필드 자리(줄 머리·불릿 다음·앞선 필드의 ` · ` 다음)에 있고 표지 뒤 한정어가 짧을 때(마침표 없음, `BODY_SLOT_QUALIFIER_MAX` 이하)만 슬롯이다 — `chunk_lint`의 `decision-role`이 이미 쓰는 "본문 첫 산문 줄이 굵은 표지로 시작"과 같은 판정이다. 표지 집합 자체의 중복·접두 겹침은 `kb_lib.validate_body_slot_markers`가 로드 시점에 본다 | `shacl`(body-slot) | 빠진 슬롯을 채운다 — plane의 write 역할 |
| 생성 문서 형태 | 생성 마크다운의 머리 블록 누락(생성기·시각·입력·질의·재현·성격), 제목 계층 건너뜀, h1 복수, 표의 헤더 행·열 수·앞뒤 빈 줄, 언어 없는 펜스, 120줄 초과인데 목차 없음, 깨진 링크, 빈 표 셀, 분모 없는 백분율, `(목표 <값>)` 표기 불일치(G16) | test | STYLEGUIDE §9 | **있음** — `gendoc`(`//:gendoc_test`, 2026-09-21 · G16 표기 통일성 2026-09-29 추가). 생성 뷰 14종(SKILL.md 19 포함)이 입력이다. 검사 함수는 `kb_lib.check_gendoc` 이고 생성기가 같은 함수를 쓴다. G16 은 표기 통일성만 게이트다 — "목표를 붙여야 하는가"는 사람 판단이다. G17(시점 의존 표현)은 오탐률 실측(후보 7건 전부 오탐)으로 게이트로 올리지 않고 `check_gendoc`의 둘째 반환값(보고 전용)으로만 낸다 | `gendoc` | 생성기(`tools/*.py`)의 출력 문자열을 고친다 — developer. 면제는 `waivers.md` |
| 카탈로그 정합성 | 스코프 없는 역할, 미부여 스코프, read plane 0, write plane 공유, `maxConcurrent` 합 > ODD 상한 | verify | 10.2 | **있음** — `validate` `check_catalog`(2026-09-13) | `catalog` | `kg/catalog-kg.ttl`·ODD를 고친다 — orchestrator(문서·그래프 같은 커밋) |
| 결정 역할 표지 | 결론·근거·대안 청크의 첫 산문 줄에 `**결론**`·`**근거**`·`**대안**`("대안 없음" 변형 허용) 없음 | test | 7.4 | **있음** — `chunk_lint` `decision-role`(2026-09-13) | `decision-role` | 본문 첫 줄을 고친다 — orchestrator |
| 요소 탈락 | 소스 요소가 어휘에 슬롯이 없어 조용히 빠짐 — 청크 frontmatter 의 최상위 키 중 `chunk2kg` 가 소비하지 않는 것, 프로파일이 선언한 plane 실체 클래스와 `chunk2kg.PROFILE_SUBSTANCE` 치역의 대칭차 | verify | 8.21 G1 | **있음** — `validate` `element-drop`(2026-09-29). 현상 [`agt:elementWithoutVocabularyDropped`](../kb/ontology/related/defect/function-phenomenon-ontology.ttl)(P19)의 관측 수단이고 vnv 가 설계했다. 실체 대칭차는 `--ontology` 만으로 돌아 `//kb/ontology:gate_test`·`//kg:gate_test` 안에 있고, 키 전수 대조는 `//kg:gate_test` 가 `chunk_files`(`//chunks:bodies`·`//kb/dev:bodies`·`//kb/vv:bodies`·`//space:bodies`)로 청크 본문을 넘겨 돈다. 실측 2026-09-29: 키 23 대 28 차 공집합 · 실체 7 대 7 대칭차 공집합 | `element-drop` | 어휘를 넓힌다(키를 `chunk2kg` 가 읽고 `kb_lib.CHUNK_OPTIONAL_KEYS` 에 등재, 실체 클래스를 프로파일에 선언) — 요소를 버리지 않는다(가정 `asm-missing-vocabulary-is-signal`). developer |
| 판정 로그 | 판정 로그의 형식·필수 필드 위반 — 판정 표의 헤더가 규약(`kb_lib.JUDGE_LOG_TABLE_HEADER`)과 다름, 행의 질문 id·값·확신도·모델 식별자·입력 지문·시각 중 하나가 빔, 지문이 sha256(소문자 16진 64자)이 아님, 시각이 ISO 8601 UTC 초 해상도가 아님, 처리가 임계의 세 값 밖, 판정 행 0건 | test | 8.14 | **있음** — `chunk_lint` `judge-log`(2026-09-29). 대상은 `generated.by` 가 `process:judge` 이고 `type: memory` 인 청크다. **판정 자체는 게이트 밖 도구**(`bazel run //tools:judge`)가 하고 게이트는 로그만 본다 — 외부 서비스가 `bazel test` 의 입력이 되면 같은 리비전이 네트워크 상태에 따라 다른 판정을 낸다 ([`p8-judge-calibration-binding`](../kb/dev/decision/p8-judge-calibration-binding/conclusion.md)). **PASS 조건은 "위반 0건"이고 판정 로그가 0건이면 거부할 것이 없어 그대로 PASS 다** — 로그의 존재를 요구하는 것은 이 게이트의 몫이 아니라서 SKIP 으로 내리지 않는다 | `judge-log` | 로그를 다시 낸다(`bazel run //tools:judge -- --record`) 또는 빠진 필수 필드를 채운다 — developer(도구)·vnv(판정). 면제는 `waivers.md`(축 `파일`) |

2026-09-11 Bazel 규칙 반영 후 기계화 10 · 부분 4 · 규약 1 · 없음 6이다. 없음의 대부분이 도입
5·7단계의 산출에 걸려 있다. `id`는 도구의 `FAIL [<id>]` 태그와 같다(agrtls A). 결정
`p6-gate-catalogue`가 같은 id를 적는다. 하네스 자체의 게이트 id는 `naming`(`//:naming_test`) ·
`build-drift`(`//:build_drift_test`) ·
`channel`(`//docs/feedback:channel_lint_test`) · `doccheck`(`//:doccheck_test`) · `gendoc`(`//:gendoc_test`) · `addition`·`empty-value`·`list-rules`·`blocking-comment`·`judge-log`(`chunk_lint`) · `space`(`space2kg`·`validate`) · `vv-case`(`vv_run`) · `vv-run-env`(`//tools:vv_run_env_test`) · `residency`·`element-drop`(`validate`) · `chunk2kg-merge`(병합) ·
`odd2kg`·`taxonomy`(생성=검사) · `workset-budget`(`//kg:workset`, 앵커가 있을 때만) · `canon`(규약, 테스트 타깃 아님)이다. 실패 종류(종료 코드 1·2·3)는
§게이트를 추가할 때에 적혀 있다.

## 코어 층 — 두 KB가 공유하는 도구

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

#### 검사 3계층 (노트 2.5절 — 온톨로지 검사기)

| 계층 | 정의 | 이 저장소 |
|---|---|---|
| 구문·스타일 (report) | 라벨·정의 누락, 참조 구문, 폐기 규약 | `validate.py`의 labels·boundary + `chunk_lint` |
| **안티패턴** (verify) | "이런 트리플이 존재하면 실패"를 SPARQL로 명세 | `validate.py --verify-queries` — `tools/verify-queries/*.rq` 하나가 안티패턴 하나. 현재 5종: 출처 빈 청크 · 외부 유입 연쇄 · 기준 없는 verifies · 지지 없는 확정 · 반박된 확정 |
| 논리 정합성 (reason) | OWL 추론기 (RL 프로파일 안) | SHACL + `--reason`(OWL-RL). shape로 자연스러운 것(수준 허용표·카디널리티)은 shape에 남긴다 |

**용어 제안 워크플로**(`term_propose`)는 일반화가 온톨로지에 닿을 때의 절차다. 에이전트는
신뢰할 수 없는 센서이므로 제안만 한다. 상위 실재·라벨 중복·정의 형식 검사를 통과한 것만
`kb/ontology/proposals/` 승인 큐에 오른다. 큐는 `//kb/ontology:modules` 밖이라 승인 전에는
그래프에 들어가지 않는다.

#### `validate.py` — 그래프 게이트

| 검사 | 강제하는 것 | 규칙 |
|---|---|---|
| `syntax` | 모든 TTL이 파싱된다 | — |
| `labels` | `agt:` 용어마다 한/영 `rdfs:label` + `skos:definition` | [ontology §확장 규칙](ontology.md#확장-규칙) |
| `boundary` | 한 용어는 한 모듈 파일에서만 정의된다 | 같음 |
| `vocab` | 데이터의 술어가 온톨로지 또는 등록된 표준 어휘 안. `--standard-vocab`(PROV-O·SKOS 원문, `MODULE.bazel` `http_file` 해시 고정)를 주면 그 네임스페이스의 용어가 **원문에 실재**하는지까지 — 접두사만 맞는 오타를 잡는다 | [rules §통제 어휘](rules.md#통제-어휘) |
| `odd-ref` | `agt:refersTo`의 대상이 ODD에 존재한다 | [rules §가정](rules.md#가정) |
| `dangling` | `cites`·`usesConcept`·`hasDirectPart`·`assumes`·`refines`·`satisfies`가 가리키는 항목이 실재한다. `usesConcept`의 대상이 폐기 용어(`owl:deprecated`)면 `warn [usesConcept-deprecated]`(FAIL 아님 — LEDGER 용어 일관성 검사) | [rules §4](rules.md#4-traceability--인터페이스를-기준축으로-한-mapping) |
| `verify` | 안티패턴 질의 결과 행 = 위반 | 위 표 |
| `shacl` | shape 적합성 (아래) | [rules](rules.md) |

`vocab`이 핵심 방어선이다. 어휘 우회를 막지 못하면 나머지 규칙이 전부 우회된다.

#### SHACL shape — `kb/ontology/shapes/`

| 파일 | 대상 | 주요 제약 |
|---|---|---|
| `chunk-shapes.ttl` | `agt:Chunk` | `lineCount` ≤ 42 · `hasLevel` 정확히 1 · 한/영 라벨 각 1 · `status` 값 |
| `composite-shapes.ttl` | `agt:Composite` | `hasDirectPart` ≤ 9 |
| `composite-order-shapes.ttl` | `co:List` | 순서 있는 복합체의 색인 1..n 연속·중복 없음, `co:itemContent` 집합이 `hasDirectPart`와 일치 (2026-09-29) |
| `residency-shapes.ttl` | plane별 | plane×level 수준 허용표 |
| `condition-shapes.ttl` | `agt:Condition`·`agt:ODD` | 조건마다 `checkMethod` 필수 · 등급 A–D · ODD는 조건 ≥ 1 |
| `assumption-shapes.ttl` | `agt:Assumption` | ODD 조건을 `refersTo` ≥ 1 · `proposition` 필수 |
| `scope-shapes.ttl` | `agt:Scope` | `mode` 고정 · `subsetOf`로 어느 ODD의 부분집합인지 |
| `trust-shapes.ttl` | `agt:Chunk` | `generatedBy` 필수 · `generatedAtTime ≤ verifiedAt`(검증 뒤 수정 금지) |
| `tag-shapes.ttl` | `agt:taggedWith` 대상 | 태그 값은 온톨로지 개념이고 범주에 등록돼 있다 (2026-09-26) |
| `requirement-body-shapes.ttl` | `agt:RequirementChunk` | 요구·검증 목표의 본문 슬롯과 순서 (2026-09-22) |
| `decision-body-shapes.ttl` | `agt:DecisionChunk` | 결론·근거·대안의 본문 슬롯. V&V 시나리오의 **자극**·**요인**·**배제 자극**이 그 세 슬롯에 사상된 대안 셋이다 (2026-09-29) |
| `acceptance-criteria-body-shapes.ttl` | `agt:ContractChunk` | 합격 기준 · 판정식 또는 확인 절차 · 등급 |
| `verification-case-body-shapes.ttl` | `agt:SchemaChunk` | 케이스 · 자극 · 기대 · 실행 명령 · 표본 근거 |
| `review-comment-body-shapes.ttl` | `agt:ReviewComment` | 라벨 일곱·장식 셋·해소 셋의 닫힌 어휘, `대상`·`본문`·`해소` 슬롯, 본문 4문장 상한 |
| `defect-factor-shapes.ttl` | `agt:DefectFactor` 인스턴스 | 현상 개체의 정의·표기·관측 수단·출처 (2026-09-29) |
| `risk-grade-shapes.ttl` | 같음 | 위험 등급 셋의 형·개수와 닫힌 값 어휘 `S0~S3`·`E1~E4`·`D1~D3`. 단계의 판정 조건은 [`risk-grade-scale`](../kb/vv/scenario/risk-grade-scale.md)이 정의한다 (2026-09-29) |
| `exposes-factor-shapes.ttl` | `agt:exposesFactor` 주어 | frontmatter `exposes`의 대상이 `defect` 모듈이 선언한 현상 개체다. 없는 개체와 요인 아닌 개체를 둘 다 거부한다 — 링크 개체도 deps도 아니라 여기가 유일한 실재 검사다 (2026-09-29) |

라벨 제약은 `sh:qualifiedValueShape` + `sh:qualifiedMinCount`로 쓴다. `sh:languageIn`은
모든 값에 적용되어 "한글 하나 + 영어 하나"를 표현하지 못한다.

#### `chunk_lint.py` — 파일 게이트

`chunk`는 본문 42줄 이하를 강제한다. `.md`는 frontmatter를 제외하고 `.ttl`은 `@prefix`·주석·빈 줄을
제외한다. `naming`은 파일명 접미사 규약(`-ontology`/`-rules`/`-shapes`/`-space`/`-kg`/`-odd`)을 강제한다.
**온톨로지 파일도 42줄 규칙을 받는다.** chunk는 포맷이 아니라 구조 규칙이기 때문이다.

`decision-role`의 표지는 파일 경로가 정한다. `conclusion`·`rationale`·`alternatives`가 **결론**·**근거**·**대안**이고, V&V 시나리오 패키지(`kb/vv/scenario/`)의 `<슬러그>-stimulus.md`·`<슬러그>-factors.md`·`<슬러그>-excluded.md`가 **자극**·**요인**·**배제 자극**이며(선언 청크 = `-stimulus`, 타깃 이름도 그것이다), 그 밖(단일 파일 옛 결정·단일 청크 시나리오)이 **결론**이다(2026-09-29, [`p8-scenario-authoring`](../kb/dev/decision/p8-scenario-authoring/conclusion.md)). 접미 판정을 시나리오 패키지로 한정한 것은 `chunks/decision/d-0140-three-defect-factors.md`처럼 stem이 `-factors`로 끝나는 옛 결정이 있기 때문이다.

청크를 파싱하는 도구는 전부 `--residency <defs/kb.bzl>` 를 받는다(2026-09-27 — `chunk2kg`·`consistency`·`weave`·`labels`·`space2kg`·`revalidate`·`vv_run`·`assume_check`·`label_sample`·`gen_build`). 인자가 없으면 `EXIT_CONFIG` 다. 직접 실행은 `--residency defs/kb.bzl` 을 명시한다.

#### 생성기 = 검사기

| 도구 | 입력 → 산출 | 실패 조건 |
|---|---|---|
| `chunk2kg.py` | 청크 frontmatter → head 그래프. plane을 개발 프로파일의 실체 클래스로 함께 타이핑하고 요구의 `pattern`을 방출한다(2026-09-18). **타깃별 조각**(`--fragment`, `kb_chunk`·`kb_decision` 액션) → `kb_kg_merge`(`--merge`) → `bazel-bin/kg/chunks-kg.ttl`. 바뀐 타깃의 조각만 다시 만든다. 묶음의 단위는 파일이 아니라 **액션의 입력 집합**이다 — `kb_decision`(셋 고정)·`kb_composite`(2~9 가변)가 그 집합을 만들고 `kb_chunk` 하나로는 복합체가 서지 않는다. 위험에서 파생된 항목의 선택 키 `exposes: [<agt: 현상 IRI>…]`를 `agt:exposesFactor`로 방출한다(2026-09-29) — 링크 키가 아니라 `targets`와 같은 자리이고 Bazel deps가 되지 않는다. 복합체 선언의 선택 키 `composite: {…, ordered: [<부분 IRI>…]}`가 있으면 `agt:Composite , co:List`로 타이핑하고 부분마다 `co:item [ a co:ListItem ; co:index "<1..n>"^^xsd:positiveInteger ; co:itemContent <부분> ]`을 그 순서로 낸다(2026-09-29). 없으면 `hasDirectPart`만 낸다 — 순서를 요구하지 않는 것에 순서를 붙이면 거짓 정보다. **예외는 없다**(유저 승인 2026-09-29) — 결정 복합체도 선언으로만 순서를 갖고 그 선언은 생성 BUILD 의 명시 인자를 통해 `--ordered <IRI>`(부분마다 한 번)로 들어온다. 이 도구는 역할 이름·파일 stem 으로 순서를 추측하지 않는다. `--ordered`와 frontmatter `composite.ordered`가 함께 있으면 같아야 한다 — BUILD는 뷰이고 frontmatter가 원본이므로 불일치는 드리프트다 ([`p4-composite-order-is-declared`](../kb/dev/decision/p4-composite-order-is-declared/conclusion.md)). 본문 슬롯 표지(`agt:bodySlot`)는 굵은 span 이 그 줄의 필드 자리(줄 머리·불릿 `- ` 다음·앞선 필드의 ` · ` 다음)에 있고 표지 뒤 한정어가 짧을 때(마침표 없음, 길이 `BODY_SLOT_QUALIFIER_MAX` 이하)만 방출한다(`body_slots`, 2026-09-29) — 표 셀·산문 접속·목록 항목 전체를 감싼 굵은 강조는 자리가 아니라 표지로 방출하지 않는다. | 필수 키 7개 누락, 값 어휘 밖, 복합체 미선언(조각), `ordered`가 목록이 아님·부분 중복·**부분 집합과 불일치**, **IRI 중복**(병합) — "한 chunk는 한 파일"의 기계적 강제 |
| `extract_refs.py` | 본문의 `d-NNNN` 인용 → `references-kg.ttl`의 `agt:cites`; 본문의 `agt:<Term>` 표기 중 온톨로지가 정의한 용어 → `agt:usesConcept`(복원 경로, dependency-graph (f)). 온톨로지에 없는 표기는 `info`로 집계만 한다 | 인용 대상이 실재하지 않음 |
| `odd2kg.py` + `taxonomy.py` | OpenODD YAML 매핑 문서 `kb/odd/project-odd.yml`(`TAXONOMY`·`MODULES`·`INCLUDE_AND`…) → `project-odd.ttl`; `related/condition` → `taxonomy.yml` (부록 E.4) | 택소노미 밖 범주 · 미선언 속성 · 선언 밖 리터럴 · OpenODD 식이 아닌 값 · `ATTRIBUTES`/`CHECKS` 없는 조건 |
| `labels.py` | 청크 head → OKF `index.md` (5.6절) | frontmatter 오류 |
| `metrics.py` | 그래프 → `metrics.md` (4.13절 지표, CQ19·CQ20, 14.1 통과 조건; 구축에는 frontmatter 링크 개체와 본문 식별자 추출(`cites`·`usesConcept`)이 들어가고 복원은 후보 파이프라인 산출만(유저 결정 2026-09-12 (b)), 가정 절에 "기본 가정만 가진 청크") | 그래프 파싱 실패 |
| `gen_build.py` | 청크 frontmatter → `BUILD.bazel`(`kb_chunk`·`kb_decision`·`kb_composite` 타깃, 링크 = deps; `kb/vv/{goal,scenario,criteria,case,verifier}/`는 디렉토리 = plane). `kb_composite`의 `ordered`·`part_iris`는 선언 청크의 `composite.ordered`를 옮긴 뷰이고, 선언이 없으면 `ordered` 인자도 없고 `part_iris`는 `srcs` 순서로 뜻을 갖지 않는다. **결정 묶음의 `ordered`는 생성기가 넣는다**(필수, 결론·근거·대안 — 유저 승인 2026-09-29: 결정도 예외 없이 선언한다. 205개 `conclusion.md`를 손으로 고치는 것이 첨가이므로 선언의 자리를 생성 BUILD의 명시 인자로 둔다). 커밋한다 | 세 청크 없는 결정 디렉토리 · 끊긴 링크 · `_check_bundle`(패키지 밖 부분·부분 수·이질·`ordered`가 부분 집합과 불일치·**시나리오 묶음(`kb/vv/scenario/`의 `-stimulus`·`-factors`·`-excluded`)에 `ordered` 없음** — 자극 → 요인 → 배제 자극의 읽기 순서가 정해져 있어 선언 없는 묶음은 거짓 무순서다) |
| `consistency.py` | 청크 본문 + 용어집 → `consistency.md` (`bazel build //kb:consistency`): 정확·근사 중복, 묶인 쌍(`coUpdatesWith`)의 응집 저하(본문 5-gram Jaccard < θ/2 — 의미 응집 검사의 첫 형태, 학습 모델 임베딩은 ODD 명시 제외), 라벨 중복, 결론 라벨 형식(결론만 — 근거·대안 라벨은 명사구 관례), 용어집 옛 표기, 중복률, ⑧ 첨가(메타 문장·채움 문구·빈 값 이상 표기 — `p4-three-empty-values`), ⑨ 목록 규칙(손 번호·항목 수·중첩·항목 길이 — `p4-slot-answers-one-question`). ⑧·⑨는 2026-09-22에 더했고 **게이트가 아니라 보고**다. 수치가 0이 된 뒤 `chunk_lint`로 올린다. 보고 뷰이며 게이트가 아니지만 `//kb:consistency_build_test`가 `bazel test //...`마다 생성한다(rules.md "커밋마다") ([`p4-redundancy-as-safety-margin`](../kb/dev/decision/p4-redundancy-as-safety-margin/conclusion.md)) | 파싱 실패 |

#### 하네스 도구 — 역할 규약과 인수

| 도구 | 하는 일 | 게이트 |
|---|---|---|
| `channel_lint.py` | 채널(`docs/feedback/`) 규약 — lane별 `status` 어휘, hci 반영 흔적은 담당 역할의 `인수:` 줄이 있어야 통과한다 | `//docs/feedback:channel_lint_test` |
| `endorse.py` | 인수 — plane 쓰기 권한이 있는 역할이 검토한 청크에 `verified`를 붙인다. `//kg:gate_test`의 writer 검사(`generated.by` 역할 × 카탈로그 쓰기 권한)를 해소하는 수단이다 | `bazel run //tools:endorse -- --by <역할>/<모델> --at <시각> <청크…>` |
| `label_sample.py` | 라벨 대표성 실험 표본 — 층화 표본 + 미끼, seed 고정 ([`label-representativeness-protocol`](feedback/label-representativeness-protocol.md)) | 게이트 아님 — 실험 |

YAML은 PyYAML로 읽는다. 잠금은 `pyyaml==6.0.2`이고 해시는 호스트 휠 + sdist 둘이다. 부분집합 로더
`kb_yaml.py`는 2026-09-11에 삭제했다. 생성물은 `bazel-bin`에만 있고 소스 트리에 같은 이름의 파일을
두지 않는다. `index.md`·`log.md`도 마찬가지다.

#### `assume_check.py` — 가정 판정과 전파 (6.9절, 도입 4단계 첫 형태, 2026-09-14)

`bazel run //tools:assume_check -- [--break <cond-id>…] [--record]` — 가정마다 `refersTo`한 ODD 조건의 판정(`odd_check`와 같은
`CHECKS.cmd`)을 연언으로 평가해 `valid`·`invalidated`·`unverified`를 낸다. 판정식 등급은 참조 조건 등급의 최저다. 깨진 가정을
`assumes`하는 살아 있는 청크가 직접 영향 집합이고, 링크·복합체 형제로 닿는 하류를 더한 것이 suspect 후보 집합이다 — 전파
(`propagate`)의 첫 형태다. `--break`는 조건 하나를 이탈로 가정해 계산된 영향 집합이 실제 의존 집합과 같은지 보는 인위 파괴
실험이다. `--record`는 실행 결과를 관측 청크(`kb/dev/memory/obs-<시각>.md`, memory plane, append-only)로 남긴다 — 무효화 이력의
자리다. 새 어휘는 없다. 가정 자체의 `when` 판정식은 후속이다.

#### `vv_run.py` — V&V 실행기 (8.15절, 도입 7단계 첫 형태, 2026-09-19)

`bazel run //tools:vv_run -- [--record] [--case <슬러그>…]` — 케이스(`kb/vv/case/*.md`) 본문의 `**실행 명령**`을 읽어 읽기 전용
검증기(`bazel test`·`bazel build`·`bazel query`·`gen_build --check`)만 실행하고 그 밖(임시 파일 자극·`bazel run`)은 SKIP으로
적는다. 케이스 판정은 **명령 전부를 실행해** 전부 0이면 `pass`, 실행분에 실패가 있으면 `fail`, **건너뛴 명령이 하나라도 있으면** `skip`이다(2026-09-22 정정). 건너뛴 쪽이 게이트가 거부한다는 것을 보이는 절반이므로 절반만 실행한 케이스는 기준을 보이지 못한다 — SKIP은 PASS가 아니다(실패 종류 3). 보고는 명령 단위 집계(`실행`·`건너뜀`·`명령`)를 따로 낸다. 리비전(워킹트리
변경 여부)·UTC 시각·bazel·python 버전·명령별 종료 코드·소요를 적는다. `--record`는 실행 기록(`kb/vv/run/run-<시각>.md`, memory
plane, concrete, `generated.by: process:vv_run`)을 append-only로 남긴다 — 도구가 executor 하위 역할을 맡는 첫 형태라 writer
검사 밖이다. 종료 코드는 fail 1 · pass 0 · skip만 3이다. **기대 대조와 자극 생성이 2026-09-23에 들어왔다**([`p8-machine-readable-case`](../kb/dev/decision/p8-machine-readable-case/conclusion.md)). 케이스가 `**자극**`·`**기대**` 산문 옆에 `yaml` 펜스로 `files`(이름 → 내용)와 `expect`(명령마다 `exit`·`contains`)를 적으면, 검증기가 자극을 임시 디렉토리에 쓰고 명령의 `{{이름}}`을 실제 경로로 바꾼 뒤 실행하고 지운다. 판정은 종료 코드와 문구가 **둘 다** 맞아야 통과다 — 종료 코드만 보면 기대한 사유로 실패했는지 모른다. 펜스가 있는 케이스에 한해 저장소 자신의 읽기 전용 검증기(`python3 tools/<v>.py`, 닫힌 집합 열 — 2026-09-26에 `assume_check` 가 들었다)를 더 실행하되 **허용 목록은 그대로 보안 경계다** — 위험은 자극의 유무가 아니라 명령이 무엇을 할 수 있는가에 있다. 리다이렉션·파이프·백틱이 있으면 실행하지 않는다. **쓰기 인자도 막는다** — `--record`(관측을 쓴다)와 저장소 안 경로의 `--out`(`{{이름}}` 자극이 아닌 값)은 SKIP 이고 사유가 수정 방향이다. `--break <조건>` 은 읽기만 하므로 실행된다. 이 검사는 `assume_check` 전용이 아니라 허용 목록 전체에 걸린다. `--out /dev/null` 같은 예외는 열지 않았다 — 허용 목록은 보안 경계라 넓히는 판단은 승인 사항이다. **`bazel run //tools:<v>` 형태는 허용 목록 밖이고 `FAIL [vv-case]`로 실행 전에 거부한다** — 그 형태는 작업 디렉토리가 runfiles 트리라 상대 경로가 자극에 닿지 못하고, 그때 나오는 입력 단계 오류가 기대한 거부와 같은 종료 코드·문구를 내 거짓 통과를 만든다([`p8-verifier-env-isolation`](../kb/dev/decision/p8-verifier-env-isolation/conclusion.md)). 명령은 워크스페이스 루트를 작업 디렉토리로, 실행기의 파이썬·runfiles 변수(`PYTHONSAFEPATH`·`PYTHONPATH`·`PYTHONHOME`·`RUNFILES_*`)를 걷어낸 환경에서 돈다 — 실행기를 부르는 방식이 판정을 바꾸면 재현이 아니다. 펜스가 없는 케이스는 지금처럼 양성 명령만 돈다(점진 도입). 형식 위반은 `FAIL [vv-case]`로 실행 전에 멈춘다. 임시 파일 자극의 자동 생성은 이로써 갖춰졌고 seed 고정은 후속이다.

#### `odd_check.py` — ODD 모니터링 (3.5절, 도입 2단계)

`bazel run //tools:odd_check`는 ODD 문서 `CHECKS.<속성>.cmd`를 실행해 속성마다 in / out / unverified를
판정하고 이탈을 보고한다. 종료 1은 이탈이다. 네트워크·호스트 상태를 보므로 테스트 타깃이 아니다.
첫 모니터링(2026-09-11)은 7속성 전부 in, 이탈 0이었다.

### 활용 (첫 형태 10)

**첫 형태가 있는 것은 `workset`·`metrics`·`impact`·`handoff`·`consistency`(2026-09-11)와
`query`·`propagate`/`revalidate`(2026-09-14)·`weave`·`gen_skills`(2026-09-19)다.** `link`(복원 후보 생성)도 2026-09-19에 생겼다.
`gendoc`(2026-09-21)은 활용 도구가 아니라 생성 문서 전부의 형태 게이트이고, 생성기가 쓰는 머리 블록·검사 함수의 정의처는
`kb_lib`다([`STYLEGUIDE.md` §9](../STYLEGUIDE.md#9-생성-문서-bazel-binmd--생성-트리-파일)). 없는 것은
tangle이다. 구축 쪽 공백의 공통 원인은 하네스가 읽기·쓰기 집합을 기록하지 않는 것이다. 활용 도구가 없으면 "온톨로지를 활용하는 방법론"이 성립하지 않는다.

| 도구 | 대응 절차 | 하는 일 | 단계 |
|---|---|---|---|
| `workset` / `labels` | [method §8 조회](method.md#8-조회) | **첫 형태 있음** — `bazel build //kg:workset --//kb:role=<role> --//kb:anchor=<라벨|IRI> --//kb:levels=<창> --//kb:hops=1 --//kb:budget=200` → `bazel-bin/kg/workset-<role>.md`: 역할 스코프(plane) × 수준 창 × 앵커 이웃(상류 ∪ 하류), 족별 우선순위(앵커 ≫ references ≫ semanticallyDependsOn ≫ 구성 관계 ≫ relatedTo ≫ 시간축) 뒤 예산 패킹, 초과분은 라벨만(dependency-graph §4, 2026-09-12). 선택자는 빌드 설정이라 BUILD를 고치지 않는다. 정의(0.5절 정정본)대로 앵커가 양을 거른다 — 앵커 없이 573줄, 앵커를 주면 14줄이다 | 2 |
| `link` | [method §6 연결](method.md#6-연결) | **첫 형태 있음**(2026-09-19) — 복원 후보 생성기 `bazel build //kg:link_candidates` → `bazel-bin/kg/link-candidates.md`: 그래프 union만으로 본문 식별자(`cites`, 구축 기록)·테스트 공동 커버(`verifies`)·개념 공유(`usesConcept` ≥ 3, `proposal`)에서 후보를 내고 TIM 허용 칸·plane 단방향·수준·복합체 형제로 탈락시키며 앵커당 k ≤ 7이다. 채택은 사람이 링크 키와 `restored` 목록에 적는다([`p10-restored-link-marking`](../kb/dev/decision/p10-restored-link-marking/conclusion.md)) — 복원 비율은 `metrics`·`audit`가 `kb_lib.link_origins`로 센다. 구축 쪽: frontmatter 링크마다 `agt:Link` + 구축 기록 증거를 `chunk2kg`가 방출, `handoff`가 workset 뷰의 펼친 청크를 `sources`로 옮긴다 (`bazel run //tools:handoff -- --workset bazel-bin/kg/workset-<role>.md <청크>`). 없는 것: 동시 편집 이력 근거, `relatedTo` 후보의 복원 표시 | 3·8 |
| `propagate` / `revalidate` | [method §7 갱신](method.md#7-갱신) | **첫 형태 있음** — `propagate`는 `assume_check`의 전파 절(깨진 가정 → 직접 영향 집합 → 하류 suspect 후보). `revalidate` — `bazel run //tools:revalidate -- --base <rev>`: base 리비전 대비 본문 해시가 바뀐 청크와 그 링크 양 끝·`part_of` 형제·`rdeps` 하류를 재판정 대상 표로 낸다(종료 1 = 대상 있음). head만 바뀐 청크는 제외한다. **2026-09-26** — `## 재판정 대상 링크 개체` 절이 본문 해시가 바뀐 청크를 양 끝으로 갖는 `agt:Link`(head 그래프와 같은 IRI)를 낸다. `assume_check`는 링크의 `when`을 ODD 판정으로 평가해 거짓이면 `suspect`를 보고하고(종료 1) `kb_lib.SUSPECT_TRIGGERS`의 켜진 종류(`supersedes`)를 전파한다 — **상태는 저장하지 않는다**. 무효화 전파 8단계·규칙 카탈로그 전체는 없다 | 4 |
| `query` | [competency-questions](competency-questions.md) | **첫 형태 있음** — `bazel run //tools:query -- <CQ> [--labels] [--bind ?v=…]`가 역량 질문 질의 27개(`tools/cq-queries/*.rq`, 하나가 CQ 하나)를 그래프 union 위에서 돌린다. 결과는 라벨 목록이다. 뷰 `bazel build //kg:cq` → `bazel-bin/kg/cq.md`가 CQ마다 행 수와 상위 5행을 낸다(2026-09-14) | 3 |
| `impact` | [method §12 영향 분석](method.md#12-영향-분석) | **첫 형태 있음** — `bazel run //tools:impact -- <타깃>`: `rdeps`로 영향 항목 수·plane 분포·suspect가 될 링크 수·승인 필요 결정 수. 구조 근사이며 가정·무효화 전파는 그래프 질의 몫이다 | 3 |
| `project` / `weave` | [method §9 뷰](method.md#9-뷰) | **첫 형태 있음** — `weave`(2026-09-19): `bazel build //kb/dev:adr`(결정 복합체의 ADR 뷰) · `//kb/dev:requirements`(요구 색인 — EARS 패턴·정제 수·도달 수준) · `//kb/dev:changelog`(`supersedes` 이력) · `//kg:audit`(감사 보고서 — 검증 현황·최근 실행·**판정 주석**·가정·추적 매트릭스·검증 표시·링크 근거를 그래프 union과 관측 본문만으로, 8단계 첫 형태). 생성물마다 생성 시각과 질의를 적는다(`p12-documents-are-generated`). `communities` — `bazel build //kg:communities`: 결정론적 Louvain으로 복합체 후보(같은 plane·level, 2~9)와 `relatedTo` 링크 후보(plane·level을 넘음)를 제안, 판정은 사람이 한다([`p4-community-detection-proposes-composites`](../kb/dev/decision/p4-community-detection-proposes-composites/conclusion.md)). tangle은 없다 | 8 |
| `gen_skills` | [method](method.md) 정형 절차 | **첫 형태 있음**(2026-09-19) — `python3 tools/gen_skills.py --root .`가 도구 docstring과 `kb_lib.SKILLS`(도구·절 앵커·대표 명령)에서 `.claude/skills/<도구>/SKILL.md`를 생성한다. 트리에 두고 커밋하며 `//:skills_drift_test`가 재생성과 비교한다. BUILD와 같은 생성 트리 파일이며 손으로 고치면 다음 생성이 덮어쓴다 | 6 |
| `open_questions` | [method §9 뷰](method.md#9-뷰) | **첫 형태 있음**(2026-09-22) — `bazel build //kg:open` → `bazel-bin/kg/open.md`: 청크의 선택 슬롯 `미확정:`을 head(`agt:bodySlot`)로 골라 질문·청크·plane/level·상세 문서로 집계한다. **집계만 맡는다** — 상세 다섯 절은 42줄 청크에 들어가지 않아 `docs/open-questions.md` 색인과 그 아래 문서로 남는다 ([`p4-three-empty-values`](../kb/dev/decision/p4-three-empty-values/conclusion.md)) | 6 |
| `space2kg` / `choices` | [method §5 후보 관리](method.md#5-후보-관리) | **첫 형태 있음**(2026-09-22) — `space/*-space.md`(변수 하나 = 파일 하나)를 A-Box `//space:design_space`로 올리고 체크박스 뷰 `//space:choices`를 낸다. 후보는 `kb_chunk` 타깃이 아니므로 **구조적으로 `deps`가 되지 못한다**. 근거 없는 배제와 확정 후보 수를 게이트 `space`가 거부한다 — `r-011`의 실물이다. 없는 것: CEL 평가기(`when`·양립 제약이 문자열) | 5 |
| `metrics` | [methodology 완료 판정](method.md#완료-판정) | **첫 형태 있음** — `bazel build //kg:metrics` → `bazel-bin/kg/metrics.md`: 청크 수·고아율·크기 분포·링크 밀도·CQ19·CQ20·신뢰 등급. **연결 성분과 CQ20 후방 추적은 관측(`memory` plane) 제외다**(유저 승인 2026-09-23) — 관측은 실행의 부산물이고 append-only라 사후에 링크를 이을 길이 없으며 추적 매트릭스에 `memory` 칸이 0개다. 관측을 세면 실행할수록 지표가 나빠지는데 그것은 고립이 아니라 기록의 축적이다. 없는 것은 suspect 비율·누락률·라벨 대표성이다 | 1 |

`metrics`(1·2단계 대리 포함)·`workset`·`odd_check`의 첫 형태가 생겼으므로 문서는 수치를 적지 않고 생성물을 인용한다 (d-0075). 문서에 남아
있는 수치는 스냅샷 표기가 붙어야 한다.

## development 층 — 개발 KB의 도구 (노트 Part VII, 전부 미구현)

| 도구 | 하는 일 | 규칙·절차 |
|---|---|---|
| `gate` | 전이 게이트 4종 — 기여 명시 / 범위·제약 / 표본 근거 / 기준 바인딩 (6.8) | [rules development](rules.md#development-규칙--개발-kb-노트-7277) |
| `space_check` | `-space` 호 일관성 · ODD 경계 · `when` 평가 · 증거 기록 규칙 · 확정 제안 (9.10, 9.11) | [method §5](method.md#5-후보-관리) |
| `feedback` | `-space` → 체크박스 파일 · 되읽기 → 확정 (13.5) | [p9-candidate-storage](../kb/dev/decision/p9-candidate-storage/conclusion.md) |
| `contract_check` | 계약 선행 · 타입 · 사후조건 CEL 실행 가능성 (7.5) | [p7-contract-first](../kb/dev/decision/p7-contract-first/conclusion.md) |
| `schema_compat` | 하위 호환 판정, 비호환이면 새 IRI + `supersedes` (7.6) | [p7-schema-derivation](../kb/dev/decision/p7-schema-derivation/conclusion.md) |
| `adr` | 결정 복합체 뷰 (7.4) — **있음**: `weave --kind adr`, `//kb/dev:adr` (2026-09-19) | [p7-alternatives-mandatory](../kb/dev/decision/p7-alternatives-mandatory/conclusion.md) |
| `tangle` | 구현 청크 → 코드 파일 (4.6) | [method §9](method.md#9-뷰) |
| `dev_metrics` | 전방 추적 커버리지 · 후방 추적 커버리지 · 결정 완결률 · `-space` 체류 · 계약 선행률 · 대안 기록률 (7.8) | [p7-dev-kb-outputs-and-metrics](../kb/dev/decision/p7-dev-kb-outputs-and-metrics/conclusion.md) |

## V&V 층 — V&V KB의 도구 (노트 Part VIII, 도입 7단계, `run` 첫 형태 외 미구현)

| 도구 | 하는 일 | 절 |
|---|---|---|
| `goal_derive` | 요구 → 검증 목표 후보 | 8.19 |
| `scenario_lint` | 변수가 ODD 속성인가 · 부류 참조 · 배제 자극 존재 · 자극 ≠ 기준 | 8.22 |
| `case_gen` | `keep(범위)` + `cover()` → concrete 케이스. 규칙·seed를 provenance에 | 8.23 |
| `verifier_bind` | 기준 바인딩 검사. 기준 없는 `verifies` 거부 | 8.11 |
| `env_assign` | 결함 요인 → 환경 단계, 재현성 조건 | 8.10, 8.12 |
| `run` | **첫 형태 있음** — `vv_run`(2026-09-19): 리비전·환경 버전 기록, 실행 기록 append(`kb/vv/run/`). **기대 문구 대조 있음**(2026-09-23, `contains`) · **환경 격리 상시 판정 있음**(`//tools:vv_run_env_test`) · seed 고정은 없다 | 8.15 |
| `judge` | **첫 형태 있음** — `bazel run //tools:judge -- --question <질문 id> [--fixture <json>] [--record] [--into <디렉토리>]`(2026-09-29): **게이트 밖 도구다.** 질문·척도·임계를 프로파일(`kb/ontology/profile/development/judge-question-ontology.ttl`·`judge-question-set-ontology.ttl`·`judge-threshold-ontology.ttl`·`judge-calibration-ontology.ttl` + `kb/ontology/shapes/judge-question-shapes.ttl`)에서 읽어 청크에 묻고, 판정 로그(`kb/vv/run/judge-<시각>.md`, memory plane, append-only — 필수 필드 질문 id·값·확신도·모델 식별자·입력 지문(sha256)·시각)와 결과 주석(`kb/vv/verdict/`, 논평 형식 — `본문:` 은 판정자가 쓰지 못해 `해당 없음`)을 낸다. 형은 noul·choice·score 셋이고 선택 집합 255 초과는 `FAIL [judge]` 로 거부하며 점수 → 선택 2단계를 안내한다. 외부 호출은 함수 하나(`call_service`)에 갇혀 있고 자격은 환경 변수 `AKB_JUDGE_ENDPOINT`·`AKB_JUDGE_API_KEY`·`AKB_JUDGE_MODEL` 로만 받는다 — 없으면 호출하지 않고 `EXIT_CONFIG` 로 멈춘다. `--fixture` 는 기록된 응답으로 같은 경로를 도는 오프라인 모드다. 구간별 정확도를 재기 전이라 처리는 전부 사람 확인 큐다 ([`p8-judge-calibration-binding`](../kb/dev/decision/p8-judge-calibration-binding/conclusion.md), ODD 조건 `id:cond-judge-service`). 로그·주석은 가정 `id:asm-judge-service` 를 `assumes` 하므로 조건이 이탈하면 `assume_check` 가 그 모델로 낸 판정을 직접 영향 집합으로 낸다. 없는 것: 3지표(정확도·판별력·캘리브레이션) 측정과 head `verified` 반영 | 8.14, 2.12 |
| `mutate` | 변이 주입 표본 검사 | 8.6 |
| `coverage` | 정제 완주 · 후방 추적 귀속 · logical 공간 커버, 경계값 별도, 6단계 제외 | 8.7 |
| `defect_classify` | `defect-rules` 추론: 요인·한정자·트리거·발견 단계 | 8.16~8.18 |
| `sim_trust` | 시뮬레이션 신뢰도 요인별 상관 | 8.13 |
| `vv_report` | 검증 상태 · 커버리지 · 결함 · 가정 건전성 · 독립성 — 검증 상태·가정 건전성은 `//kg:audit`(2026-09-19)이 낸다. 결함·독립성은 없다 | 8.24 |
| `independence_audit` | 개발 역할의 V&V KB 쓰기 흔적 = 0 | 8.5 |
| `vv_metrics` | 목표 파생률 · 기준 바인딩률 · V&V 완주율 · 실행 통과율 · 변이 검출률 · 재현 실패율 · 검증 대응물 지연 | 8.26 |
| `diagnose` | 불만족 핵 · 보간 · 최약 전제조건 · 명세 추론. 결과는 관측 청크 | [12.12](../kb/dev/decision/p12-symbolic-diagnosis/conclusion.md) |
| `guide` | 지침 생성 — 귀속 후보 · 조치 · 배제된 전략 | [8.4](../kb/dev/decision/p8-mismatch-attribution/conclusion.md) |
| `proactive_vv` | 선제 트리거 감시(ODD 경계 · 커버리지 공백 · 외부 지식 · 증거 노화), 재실행 선택 | [8.27](../kb/dev/decision/p8-proactive-vv/conclusion.md) |

## Bazel 배선

**지식 항목은 타깃이다** (2026-09-11, [`bazel-dependency-review`](feedback/bazel-dependency-review.md) B + 연결성).
`defs/kb.bzl`의 규칙 `kb_chunk`(청크 = 타깃)·`kb_decision`(결정 복합체 = 타깃, 대안 필수)·`kb_composite`(결정 밖 복합체 = 타깃, 부분 2~9 동질)·
`kb_ontology_module`(모듈 = 타깃, `owl:imports` = deps)이 `ChunkInfo`·`OntologyModuleInfo` provider를
내보낸다. frontmatter의 `refines`·`serves`·`supersedes`·`verifies`가 **deps**다. BUILD는
`tools/gen_build.py`가 frontmatter에서 **생성**하고 커밋한다. `//:build_drift_test`가 원본과 비교한다
(d-0159). Bazel이 맡는 것은 링크의 **구조**다. 끊긴 링크 = 로드 에러, 방향 = 분석 시점 `fail()` +
`//kb:*_readers` 가시성, 파급 = `bazel query rdeps`, 42줄·frontmatter = 검증 액션(`bazel build`만으로)이다.
의미, 곧 SHACL·통제 어휘·상태는 그대로 union 게이트다(d-0157). 음성 시험은 `//defs/tests`에 있다.
skylib analysistest를 쓴다.

```bash
bazel run //tools:impact -- //kb/dev/requirement:r-008-descend-to-executable   # 영향 집합 = rdeps (12.6절 네 수치)
bazel build //kg:workset --//kb:role=developer --//kb:anchor="두 KB" --//kb:levels=concrete   # 작업 집합 뷰, 선택자는 플래그
bazel build //kb/dev/decision:all                                                       # 검증 액션 = 42줄·frontmatter
bazel run //tools:revalidate -- --base HEAD~1                                            # 본문 해시 변경 → 재판정 대상 링크·항목
tools/gen_build.py                                                                       # frontmatter 를 고쳤으면 BUILD 재생성
```

```
bazel test //...  (게이트 전체 — test_suite 없음, 패키지의 test 타깃 전부)
├── //:build_drift_test            생성 BUILD = frontmatter (드리프트 가드)
├── //defs/tests:*                 음성 시험 5 — plane 단방향·수준 허용표·supersedes plane·verifies 주어·결정 수준
├── //:naming_test                 TTL 접미사 규약
├── //docs/feedback:channel_lint_test  채널 규약 — lane status 어휘 · handoff↔agents 쌍 · hci 반영 흔적 · waivers
├── //:doccheck_test               문서 현행성 — 깨진 링크·앵커·백틱 경로 (루트 md + docs/**, 채널 제외)
├── //space:design_space           설계 공간 A-Box — 열린 변수와 후보 링크 (게이트 `space`)
├── //space:choices                후보 체크박스 뷰 (생성 뷰, 게이트 아님)
├── //kg:open                      미결 집계 — 청크의 `미확정:` 슬롯 (생성 뷰, 게이트 아님)
├── //:gendoc_test                 생성 문서 형태 — 머리 블록·제목 계층·표·목차·링크·비율 표기 (생성 뷰 11종 + SKILL.md)
├── //:skills_drift_test           생성 skill(.claude/skills) = 도구 docstring·kb_lib.SKILLS (드리프트 가드)
├── //kb:consistency_build_test    정합성 보고 생성 (build_test — 보고는 게이트 실행마다)
├── //chunks:lint_test             `chunks/` 항목 42줄 · 산문 문체(prose) · 첨가·빈 값·목록
├── //kb/dev:lint_test             개발 KB 청크 42줄 · 산문 문체(prose) · 첨가·빈 값·목록
├── //kb/vv:lint_test              V&V KB 청크 42줄 · 산문 문체 · 첨가·빈 값·목록 (2026-09-19)
├── //kb/ontology:gate_test        labels · boundary · SHACL
├── //kb/odd:gate_test             ODD shape  ← //kb/odd:odd (odd2kg) · :taxonomy
└── //kg:gate_test                 vocab · odd-ref · dangling · verify · SHACL
                                    ← //kg:chunks_kg · //kg:references_kg 를 입력으로
생성물: //kb/odd:odd · //kb/odd:taxonomy · //kb/dev:index · //kg:metrics · //kg:workset_<role> · //kb:consistency · //kg:communities · //kg:cq · //kb/dev:adr · //kb/dev:requirements · //kb/dev:changelog · //kg:audit · //kg:link_candidates
```

배선은
`defs/knowledge.bzl`의 매크로(`kb_gate_test`·`kb_reference_kg`·`kb_chunk_lint_test`·
`kb_odd_kg`·`kb_taxonomy`·`kb_index`·`kb_metrics`·`kb_gendoc_test`) 또는 `defs/kb.bzl`의
규칙(`kb_chunk`·`kb_decision`·`kb_ontology_module`·`kb_bundle`·`kb_kg_merge`·`kb_workset_view`)으로만 선언한다.
`py_test`를 직접 쓰지 않는다.

## 게이트를 추가할 때 — 절차·판단 기준·기준선 (agrtls A·C·E, 2026-09-12)

절차는 결정 [`p6-mass-fail-suspects-the-rule`](../kb/dev/decision/p6-mass-fail-suspects-the-rule/conclusion.md)에 있다.
순서는 **이름(id)** → **총람 행**(무엇을 거부·계층·id·해소 절차) → **도구**(`FAIL [<id>] <경로>: <메시지>`) →
**첫 실행 실태 기록** → **판정**이다. 첫 실행에서 대량 FAIL이면 산출물이 아니라 규칙을 먼저 의심한다.
실례로 결론 라벨 형식 197건은 규칙 원문("결론 문장형")대로 범위를 결론으로 좁혀 25건이 되었다.

| 구분 | 기준 | 자리 |
|---|---|---|
| **게이트** | 기계적으로 참·거짓이 갈리고 재현되며 오탐이 없다 | test 타깃 — `bazel test //...` |
| **보고** | 판정에 사람(또는 승인된 판정자)이 필요하다 | build 뷰 — `consistency`·`communities`·`metrics` |

**실패 종류**는 도구 종료 코드이며 `tools/kb_lib.py` 상수다. `1`은 판정 실패, `2`는 설정·입력
문제(파일 없음·인자·파싱 불가), `3`은 미실행이다. 미실행은 검사 대상이 0건인 경우다.
**SKIP은 PASS가 아니다.** 비영 종료라 게이트는 빨갛다.

**면제는 선언한다.** 선언처는 [`waivers.md`](waivers.md)이고 항목은 게이트 id·대상·축·사유·판정자·날짜다.
도구는 면제를 집계에서 빼되 목록에 남긴다. 코드 속 예외 목록을 두지 않는다.

**비-초록 기준선**은 아래와 같다. 알려진 상태이며 결함이 아니다. 고치러 오지 말고, 바뀌면 이 표를 고친다.

| 신호 | 상태 | 왜 정상인가 |
|---|---|---|
| `//kg:gate_test` 로그 `warn [usesConcept-deprecated]` 4건 | 정상 | `p9-evidence-ledger`·`p9-language-model-place`가 폐기(`confidence`·`counterfactualTest`)를 **서술**한다 |
| `consistency` ⑥ 옛 표기 잔존 1건 | 정상(면제) | `pe-storage-layout`의 `verifier/`는 디렉토리명 — `waivers.md` |
| `metrics` "기본 가정만 가진 청크 614/615" | 정상(진행 지표) | 기본 가정 후 좁힘 — 목표 0은 도입 4단계 |
| `communities` 복합체 후보 0 | 정상 | 링크가 구축 기록뿐인 동안은 선언된 복합체와 같은 군집만 나온다 |
| `consistency` ⑦ 단정성 — 추측 표현·구어 후보·대시 밀도 목록 | 정상(보고) | 판정은 사람이 한다. 청크는 문체만을 이유로 재작성하지 않는다(검증 표시 보존, 유저 결정 2026-09-13) — 신규·수정 문장부터 규칙을 적용한다 |

## 게이트 밖 — 규약으로 남은 것

**여기 적히지 않은 채 게이트도 없는 규칙은 사실상 없는 규칙이다.**

| 규칙 | 왜 게이트가 아닌가 | 어디에 |
|---|---|---|
| 라벨이 본문을 대표한다 | 판정 불가 — 게이트로 만들지 않는다 | `STYLEGUIDE.md` §4. 보고는 게이트 밖 판정자의 질문 `agt:labelRepresentsBody`(score)다(2026-09-29) |
| 한 chunk는 한 주제 | 판정 불가. 42줄과 분할 신호가 대리 지표 | `STYLEGUIDE.md` §0. 보고는 게이트 밖 판정자의 질문 `agt:bodyHasOneClaim`(noul)다(2026-09-29) |

카탈로그 정합성 검사가 없어 ODD의 동시 에이전트 한도와 카탈로그의 합이 한동안 어긋난 채
지나간 적이 있다. 규약만으로는 지켜지지 않는다는 증거다.

## 도구 작성 규칙

- 실패 시 비영 종료 + `FAIL [검사명]` 접두사 + 근거 인용을 낸다. 메시지가 곧 수정 안내다.
- 새 검사는 독립 함수 `check_*() -> list[str]`로 추가하고 `main`에서 합류한다.
- 규약 상수(접미사·네임스페이스)의 단일 정의처는 `tools/kb_lib.py`다.
- 생성기는 검사기다. 생성 실패가 곧 게이트 실패이고, 생성물은 소스 트리에 두지 않는다.
- 검사를 약화하는 변경(삭제·예외 추가)은 유저 승인 사항이다.
