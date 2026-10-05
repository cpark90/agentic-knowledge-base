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

## 게이트 총람 — 원본은 `GATES` 리터럴이고 이 표는 그 투영이다

게이트 id의 단일 정의처는 [`defs/kb.bzl`](../defs/kb.bzl)의 `GATES`·`TOOL_TAGS`다(2026-10-02 — 그 전에는 같은 목록이 넷으로 갈려
있었다: 상수 25 · 코드의 태그 · 이 표의 `id` 열 · 아래 하네스 문단). 이 표는 노트 6.7절의 규칙 단위로 묶은 손 투영이고 `id` 열에
등록부 밖의 id가 있으면 `doccheck --gates`가 거부한다. 총람에 없는 등록 게이트는 같은 검사가 보고로 낸다. 표 자체를 생성 뷰로
바꾸는 것은 통일 기획 3단계다.

노트 6.7절의 총람을 이 저장소의 실측과 함께 둔다 ([`p6-gate-catalogue`](../kb/dev/decision/p6-gate-catalogue/conclusion.md)).
실행 계층: **shape**(SHACL, 청크 단위, 즉시) / **verify**(SPARQL, 그래프 단위, 재검증 시점) /
**analysis**(Bazel 분석 시점, 빌드 실패) / **test**(실행, `bazel test`) / **human**(승인).
게이트에 걸린 청크는 `draft`에 머물고 하류로 전파되지 않는다.

| 게이트 | 무엇을 거부하는가 | 계층 | 절 | 이 저장소 | id | 해소 (누가·어디서) |
|---|---|---|---|---|---|---|
| 청크 형식 | 본문 토큰 상한 초과(저작 산문 1,092 = 42×26 · `artifact`·`memory` 2,856 = 42×68), 라벨 누락, plane·level 유일성 위반, `type`이 온톨로지 밖 | shape | 4.4 | **있음** — `chunk_lint` + `chunk2kg` + `chunk-shapes` + `token-budget-shapes`. 크기의 단위는 줄이 아니라 **토큰**이고 계수기는 `o200k_base`(어휘 파일 sha256 고정) 하나다 — 줄 상한 42·200은 폐지됐다([`p1-chunk-unit-is-tokens`](../kb/dev/decision/p1-chunk-unit-is-tokens/conclusion.md), 2026-10-01) | `chunk` · `chunk2kg` · `token-budget` | 청크를 고친다 — plane의 write 역할(요구·결정 orchestrator, 산출물 developer). `chunk_lint`의 토큰 상한 위반은 `waivers.md`(축 `파일`)로 면제한다 — append-only 기록처럼 소급 분할이 기록을 다시 쓰는 일인 경우다(2026-10-01). SHACL(`token-budget-shapes`)쪽도 같은 선언을 받는다(2026-10-01) — `validate`의 `--waivers`가 위반의 focus node를 `agt:assertionLocation`으로 파일에 사상해 게이트 id `shacl`(축 `파일`)의 면제를 가른다. shape는 약화하지 않는다 |
| 수준 허용표 | plane에 허용되지 않는 level | shape | 6.4 | **있음** — `residency-shapes` | `shacl`(residency) | level 또는 plane을 고친다 — 저작자 |
| 복합체 | 부분의 plane·level 불일치, 직접 부분 > 9, 순환 | analysis + verify | 4.5 | **있음** — `composite-shapes`(≤9) · `kb_decision`(결정의 세 부분·수준·`ordered`가 부분 집합과 일치, 분석 시점) · verify 질의 `composite-heterogeneous`·`composite-cycle`(전체 복합체, 2026-09-13; 수준 동질성은 결정 복합체 제외) · `kb_composite`(부분 2~9 · plane·level 한 쌍, 분석 시점, 2026-09-29) · `gen_build._check_bundle`(묶음 = 패키지 × `composite.id`, 생성 시점 — 패키지 밖 부분·중복 선언·이질·상한·`ordered`와 부분 집합의 불일치) · `composite-order-shapes`(순서 있는 복합체의 색인 1..n 연속·중복 없음·부분 집합과 일치, 2026-09-29) | `shacl`·`gen-build`·`verify` | 복합체 선언·세 청크를 고친다 — 저작자 |
| 통제 어휘 | 온톨로지에 없는 술어·개체, 표준 어휘 원문에 없는 prov·skos 용어 | verify | 0.0, 2.12 | **있음** — `validate` vocab (+ `--standard-vocab`, 2026-09-12) | `vocab` | 온톨로지에 개념을 먼저 더하거나(`term_propose` → 승인) 술어를 정정한다 — developer(T-Box) |
| 출처 | `sources`가 빈 청크, 파생 연쇄 전체가 외부 유입인 확정 청크 | verify | 4.3, 2.12 | **있음** — `sources-empty.rq`·`imported-chain-confirmed.rq` | `verify` | `sources`를 보강한다 — 저작자 |
| TIM | 링크 타입의 정의역·치역 밖 plane, 카디널리티 초과, 단방향 규칙 위반 | analysis | 10.1 | **부분** — `defs/kb.bzl` 규칙이 `refines`(상위 수준·plane 단방향)·`serves`(요구만)·`supersedes`(같은 plane)·`verifies`(V&V 주어·같은 수준)를 분석 시점 `fail()`로, 끊긴 링크는 로드 에러, 방향은 `package_group` 가시성 (2026-09-11) | `tim`(`defs/kb.bzl` 분석 시점) | 링크의 방향·수준을 고친다 — 저작자. 규칙 변경은 유저 승인 사항이다 |
| KB 가로지름 링크 | `verifies` 밖의 저작 링크(frontmatter 링크 키 `chunk2kg.LINK_KEYS` — `satisfies`·`derivesFrom`·`overlapsWith` 포함)가 두 KB(`kb/dev` ↔ `kb/vv`)를 가로지름. 예외는 검증 목표(`kb/vv` requirement, functional) → 개발 요구 `derivesFrom` 하나다([`p8-scenario-ladder-rungs`](../kb/dev/decision/p8-scenario-ladder-rungs/conclusion.md)) | verify | 8.5 | **있음** — `validate` `check_cross_kb_link`(2026-10-04). `defs/kb.bzl` 의 `_check_links` 는 Bazel deps(`refines`·`serves`·`supersedes`·`verifies`)만 받고 판정에 두 끝점의 KB·plane·수준이 필요해 병합 그래프를 보는 `validate` 가 자리다. 판정 함수는 `kb_lib.cross_kb_link` 하나이고 복원 후보 생성기(`link`)가 같은 함수로 후보를 거른다. 실측 2026-10-04: 가로지름 46 전부 예외, 위반 0 | `cross-kb-link` | 케이스·검증기가 개발 항목을 가리키는 링크는 `verifies` 로 바꾸고 그 밖은 지운다 — 저작자 |
| 코드 부분 링크 | 추출 트리(`kb/dev/artifact/`) 안에서 복합체의 부분인 청크(정의 청크·절·장·모듈 머리의 구역 청크)가 `refines`·`serves`·`verifies` 의 주어 또는 대상이다. 코드의 링크는 파일 복합체의 선언 청크인 파일 청크(`module.md`) 하나가 갖는다([`p7-code-links-on-file-composite`](../kb/dev/decision/p7-code-links-on-file-composite/conclusion.md)) | verify | Q47-b | **있음** — `validate` `check_code_part_link`(2026-10-05). 판정에 부분 관계(`agt:hasDirectPart`)와 청크 위치가 함께 필요해 병합 그래프를 보는 `validate` 가 자리다. 판정 함수는 `kb_lib.code_part` 하나이고 복원 후보 생성기(`link`)가 같은 함수로 코드 부분 끝점의 후보를 거른다. 추출기는 구역 청크에 링크를 복사하지 않고 연결은 선언 청크 = 복합체 합침(Q49-a)과 `part_of` 로 선다 | `code-part-link` | 링크를 등록부의 `refines`·`serves` 로 옮기고 재추출한다 — developer |
| ODD 참조 | ODD에 없는 조건을 참조하는 스코프·가정·시나리오 변수 | verify | 3.3 | **있음** — `validate` odd-ref | `odd-ref` | ODD를 먼저 확장하거나(developer, design 겸임) 참조를 정정한다 |
| ODD 경계 | 후보 값·케이스 값이 ODD 범위 밖 | verify | 9.10 | 없음 (5단계 `space_check`) | — | 5단계 |
| 기여 | `serves` 없는 abstract 결정 | verify | 6.8 | 없음 — abstract 결정 자체가 아직 없다 | — | — |
| 범위·제약 | 범위 없는 logical 변수, 실행 불가한 사후조건 | shape + test | 6.8 | 없음 (5단계) | — | 5단계 |
| 검증 대응물 | 같은 높이의 V&V 대응물([`p8-scenario-ladder-rungs`](../kb/dev/decision/p8-scenario-ladder-rungs/conclusion.md)가 높이마다 정한 대응물) 없이 다음 높이로 내려간 하강(요구 `r-023-rung-before-descent`). 판정식은 R1 사다리 사슬이다 — functional→abstract 는 결정 결론(concrete)이 `refines`·`serves` 하는 요구에 그것을 `derivesFrom` 하는 검증 목표, logical→concrete 는 logical·concrete 부분을 함께 가진 결정 복합체가 닿는 요구의 목표에 합격 기준, concrete→executable 은 executable 이 `refines` 하는 concrete 의 복합체가 닿는 요구의 기준 가운데 검증기가 바인딩한 것(검증기 → 기준 또는 검증기 → 케이스 → 기준 `refines`)이다. 사람 확인 기준만 가진 요구는 면제다(Q26-a) | verify | Q51-a | **있음** — `validate` `check_rung_before_descent`(2026-10-05). 판정에 두 KB 의 청크·복합체 부분·링크가 함께 필요해 병합 그래프를 보는 `validate` 가 자리다. 판정 함수는 `kb_lib.rung_violations` 이고 대응물 집합 `kb_lib.vv_counterparts`·사람 확인 판정 `kb_lib.human_check_criteria` 를 `metrics` 7단계 절·전방 추적과 공유한다. 사슬 8(2026-09-19)의 concrete `verifies` 는 그대로다 | `rung-before-descent` | 빠진 높이의 대응물(목표·기준·검증기)을 저작한다 — vnv |
| 표본 근거 | `sampling` 없는 concrete 값·케이스 — 근거 규칙 없는 `cover` 항목, 손으로 적은 값(`cases` · 관측 재현 밖의 `values`), 생성 결과와 어긋난 케이스 | analysis + test | 6.8, 8.23 | **부분** — `tools/case_gen.py`(2026-10-04, [`p8-case-generation`](../kb/dev/decision/p8-case-generation/conclusion.md), 유저 답 Q27-a)가 생성 시점에 거부하고 `//:case_drift_test`가 트리의 케이스를 재생성과 비교한다. **대상은 0이다** — 현행 케이스는 수기이고 logical 시나리오가 없다. concrete 값(케이스 밖)의 표본 근거는 없음(5단계) | `case-gen` · `case-drift` | logical 시나리오의 `keep`·`cover`를 고쳐 `python3 tools/case_gen.py --out kb/vv/case`로 반영하고 그 시나리오를 `//:case_drift_test`의 `scenarios`에 더한다 — vnv |
| 할당 근거 | 후보가 둘 이상인데 확정된 링크, 배제 근거 없는 기각 | verify | 9.10 | 부분 — 증거 기록 규칙 2 질의(`confirmed-without-evidence`·`confirmed-with-refutation`); 확정·구축·복원·후보 링크 수는 `bazel build //kg:metrics` 링크 절과 `//kg:link_candidates`가 낸다(여기 적지 않는다 — 2026-10-01 실측에서 넷이 전부 낡아 있었다); 상태·클래스 불일치 질의 `link-state-class-mismatch` | `verify` | 증거 항목을 더하거나 확정을 후보로 되돌린다 — 저작자 |
| 기준 바인딩 | 기준 없는 `verifies`, 판정식 없는 기준 | shape | 8.11 | **있음** — `verifies-without-criteria.rq` | `verify` | vnv가 기준 청크를 만들고 `verifies`를 바인딩한다 |
| 대안 기록 | 대안 청크 없는 결정 | shape | 7.4 | **있음** — `kb_decision` 의 `alternatives` 가 필수 속성이고, `gen_build` 가 세 청크 없는 디렉토리를 거부한다 (로드 시점) | `gen-build` | `alternatives.md`를 쓴다 — orchestrator |
| 계약 선행 | 계약보다 먼저 확정된 구현 | verify | 7.5 | 없음 — `contract` plane 항목 0 | — | — |
| 판정 도구 | 컴파일·타입·스키마·린터 실패 | test | 5.4 | 없음 — `artifact` plane 항목 0 | — | — |
| 독립성 | 개발 역할이 V&V KB에 쓴 흔적 | verify | 8.5 | 부분 — 의존 방향(개발 → V&V 금지)은 `//kb:vv_readers` 가시성으로 분석 시점에 차단한다. 쓰기 흔적 검사는 없다 | `visibility`(`//kb:*_readers`) | 의존 방향을 되돌린다 — developer |
| 승인 | `requirement`·`decision`의 `stable` 전이, 온톨로지 확장, 학습 판정자 결과 | human | 5.4, 2.5, 8.14 | 규약 — `verified` 목록·질문지의 `status: answered`. 사람 검토 실측 10(2026-09-11 라벨 재판정) | `writer` | 쓰기 권한 역할이 검토 뒤 `endorse` — orchestrator·vnv |
| 신뢰 등급 | `generatedBy` 없음, 검증 뒤 수정 | shape | 2.12 | **있음** — `trust-shapes` | `shacl`(trust) | `generated.at` ≤ `verified.at`가 되게 검증 표시를 물리거나 다시 찍는다 |
| 참조 무결성 | 인용 대상·부분·가정·요구가 실재하지 않음 | verify + 생성 | 4.8 | **있음** — `extract_refs`·`validate` dangling. 정의의 호출 대상(`agt:usesDefinition` — 추출기가 낸 frontmatter `uses`)도 본다(2026-09-30) — 링크 개체가 없는 references 족이라 여기가 유일한 실재 검사다 | `dangling` · `extract-refs` | 인용 대상을 정정한다 — 저작자 |
| 산문 문체 | 경어체 종결(`습니다`·`세요`·`해요` 등), 산문의 느낌표 | test | STYLEGUIDE §0 | **있음** — `chunk_lint`·`doccheck`의 `prose` (2026-09-13). 추측·구어·대시 밀도는 `consistency` ⑦이 보고한다 | `prose` | 문장을 고친다 — 저작자. 고유명사의 느낌표는 `waivers.md` |
| 수준 허용표 단일 정의처 | `residency-shapes.ttl` 의 구간이 `defs/kb.bzl` 의 `RESIDENCY` 와 갈림 | verify | 6.4 | **있음** — `validate check_residency` (2026-09-26). 원본은 `defs/kb.bzl`(Starlark 는 파일을 읽지 못해 분석 시점 판정을 지키려면 표가 거기 있어야 한다)이고 `kb_lib.load_residency` 가 리터럴로 읽어 파생한다. `metrics` 의 사본은 제거됐다 | `residency` | shape 를 원본에 맞춘다 — developer |
| 링크 비순환 | `refines`·`supersedes`·`hasDirectPart` 의 반사·순환 | verify | 6.2·7.4·4.5 | **있음** — 질의 `refines-cycle`·`supersedes-cycle`(2026-09-26 신설)·`composite-cycle`. 공리(`owl:IrreflexiveProperty`·`TransitiveProperty`)는 선언이고 판정은 질의다 — pySHACL 의 rdfs·owlrl 추론이 비반사성 위반을 보고하지 않는다(고정물로 실측) | `verify` | 순환을 끊는다 — 저작자 |
| 주석의 수준 상속 | 주석의 `hasLevel` 이 `targets` 대상 어느 것의 수준과도 다름 | verify | 7.7 | **있음** — 질의 `comment-level-not-inherited`(2026-09-26). 대상이 여럿이면 그중 하나와 같으면 통과 | `verify` | 주석의 수준을 대상에 맞춘다 — vnv |
| 태그 값 | `taggedWith` 값이 온톨로지 개념이 아니거나 범주에 미등록 | shape | 0.5 | **있음** — `tag-shapes.ttl`(2026-09-26). 결함 요인 범주 값 22개 등록(2026-10-01, defect 현상 개체). `taggedWith` 실사용은 여전히 0 이라 위반 0 | `shacl`(tag) | 값을 개념으로 바꾼다 — 저작자 |
| 실행기 환경 격리 | 케이스의 명령이 실행기의 파이썬·runfiles 문맥을 물려받음 — 걷어내는 변수가 다섯과 다르거나, `clean_env()` 뒤에 남거나, 작업 디렉토리가 워크스페이스 루트가 아님 | test | 8.15 | **있음** — `//tools:vv_run_env_test` (2026-09-23). 판정 대상을 실행기 전체가 아니라 격리의 동작으로 좁혀 **중첩 bazel 을 피했다**. **선언된 예외 하나** — `//tools:vv_run_env_test` 자신이 `env_inherit = ["HOME"]`(실측 일치를 위해 호스트 `HOME`을 물려받는다). 그 수(≤1)는 ODD 조건 [`id:cond-host-env-inherit`](../kb/odd/project-odd.yml)가 `bazel query 'attr(env_inherit, "HOME", tests(//...))'` 의 행 수로 판정한다(2026-09-29) | `vv-run-env` | 걷어낼 변수를 바꾸려면 결정 [`p8-verifier-env-isolation`](../kb/dev/decision/p8-verifier-env-isolation/conclusion.md)과 검사의 기대를 같은 커밋에서 고친다 — developer |
| 작업 집합 예산 | 앵커가 있는 작업 집합 뷰(라벨 목록 + 펼친 본문)가 문서 전체로 예산(5,418토큰 = 42×129)을 넘음 — **앵커가 있을 때만** 판정한다. 앵커 없는 뷰(스코프 전체 라벨 목록)는 구조적으로 예산을 넘어 판정 밖이다 | analysis | 5.6, 11.3 | **있음** — `tools/workset.py`(2026-09-29). `bazel build //kg:workset --//kb:anchor=…`가 종료 코드로 판정한다 | `workset-budget` | 앵커의 이웃 구성이나 청크 크기를 줄인다 — 저작자. 예산 값(5,418토큰)은 결정 `p1-chunk-unit-is-tokens`가 정하고 단일 정의처는 `kb_lib.CONTEXT_TOKEN_BUDGET`이다 |
| V&V 케이스 형식 | 기계가 읽는 자극·기대의 규약 위반 — `files`·`expect` 밖의 키, `expect` 수가 명령 수와 다름, 이름에 경로, 명령이 가리키지 않는 자극, 미해결 `{{이름}}`, 검증기를 `bazel run`으로 부르는 명령 | analysis | 8.20 | **있음** — `vv_run` (2026-09-23). `bazel test //...` 밖이고 `bazel run //tools:vv_run` 이 판정한다 — 케이스가 `bazel test` 를 부르므로 실행기 전체는 테스트 타깃이 될 수 없다. 다만 **환경 격리는 `//tools:vv_run_env_test` 로 테스트 안에 있다** — 그 검사는 케이스를 하나도 돌리지 않는다 | `vv-case` | 케이스의 `yaml` 펜스를 규약(`files`·`expect`)에 맞춘다 — vnv. 면제는 `waivers.md`(축 `파일`·`stem`) |
| 해소되지 않은 차단 주석 | `issue (blocking)` 이면서 `해소: 열림` 인 살아 있는 주석 | test | 7.7 | **있음** — `chunk_lint` (2026-09-22). 대상은 살아 있는 `type: annotation` 청크이고 `deprecated`·`invalidated` 는 기록이라 막지 않는다 | `blocking-comment` | 대상을 고친 뒤 `해소: 해소 — <이유>`로, 받지 않기로 했으면 `해소: 기각 — <이유>`로 바꾼다 — 저작자. 면제는 `waivers.md`(축 `파일`) |
| 설계 공간 | 근거 없는 배제(`eliminated` 인데 `eliminated_by` 없음), 확정 후보가 정확히 하나가 아닌 `resolved`, 후보의 출발점·링크 타입이 변수와 불일치, 실재하지 않는 IRI, 같은 변수를 두 파일이 선언 | analysis + verify | 9.10 | **있음** — `space2kg`(생성 시점) · `validate` `check_space`(그래프 시점) (2026-09-22). `space/*-space.md` 는 `kb_chunk` 타깃이 아니라 A-Box 그래프 `//space:design_space` 로 나간다 | `space` | 후보에 근거를 붙이거나 변수를 고친다 — 저작자. 후보는 결코 `deps` 가 되지 않는다 (`p9-candidate-storage`) |
| 첨가 | 슬롯의 질문에 답하지 않는 문장 — 메타 문장(`다음과 같다`·`이 절에서는`·`아래에서 설명한다`·`앞서 말했듯`)과 채움 문구(`특이사항 없음`·`일반적인 방식을 따른다`·`추후 결정한다`) | test | STYLEGUIDE §0 | **있음** — `chunk_lint` (2026-09-22 승격, `consistency` ⑧ 수치 0). 대상은 살아 있는 청크이고 `deprecated`는 기록이라 제외한다 | `addition` | 슬롯의 질문에 답하는 문장으로 바꾸거나 지운다. 채움 자리에는 세 빈 값 — 저작자 |
| 빈 값 표기 | 세 빈 값(`없음`·`해당 없음`·`미확정`) 밖의 `N/A`·`TBD`·`미정`과 표의 단독 대시 셀 | test | STYLEGUIDE §0 | **있음** — `chunk_lint` (2026-09-22 승격) | `empty-value` | 세 값 중 하나로 바꾼다. 낱말의 산문 용법이면 `waivers.md`에 선언한다 — 저작자 |
| 목록 규칙 | 손 번호 `2.` 이상 · 항목 9개 초과 · 중첩 3단계 이상 · 항목당 240자 초과 · 빈 목록 항목 | test | STYLEGUIDE §0 | **있음** — `chunk_lint` (2026-09-22 승격). 길이는 이어지는 들여쓴 줄을 합치고 공백을 정규화한 뒤 센다 | `list-rules` | 번호를 전부 `1.`로 바꾸고, 항목 수·중첩·길이는 블록을 나누며, 빈 목록은 `없음`으로 적는다 — 저작자 |
| 본문 슬롯 | 틀이 요구하는 슬롯 표지 누락 — 요구·검증 목표·결정 세 청크·합격 기준·케이스의 일곱 틀 | shape | STYLEGUIDE §0 | **있음** — `*-body-shapes.ttl` 넷 (2026-09-22). `chunk2kg`가 본문에서 표지를 찾아 `agt:bodySlot`으로 내고 shape가 판정한다. 슬롯마다 등록 질문이 `sh:description`에 있다. V&V 시나리오의 **자극**·**요인**·**배제 자극**은 새 틀이 아니라 결정 틀의 세 슬롯에 사상된 표지다 (2026-09-29). **표지는 자리로 판정한다**(2026-09-29 실측 — 본문 중간의 굵은 강조가 표지로 잘못 잡힌 오탐 4건). 굵은 span 이 그 줄의 필드 자리(줄 머리·불릿 다음·앞선 필드의 ` · ` 다음)에 있고 표지 뒤 한정어가 짧을 때(마침표 없음, `BODY_SLOT_QUALIFIER_MAX` 이하)만 슬롯이다 — `chunk_lint`의 `decision-role`이 이미 쓰는 "본문 첫 산문 줄이 굵은 표지로 시작"과 같은 판정이다. 표지 집합 자체의 중복·접두 겹침은 `kb_lib.validate_body_slot_markers`가 로드 시점에 본다 | `shacl`(body-slot) | 빠진 슬롯을 채운다 — plane의 write 역할 |
| 생성 문서 형태 | 생성 마크다운의 머리 블록 누락(생성기·시각·입력·질의·재현·성격), 제목 계층 건너뜀, h1 복수, 표의 헤더 행·열 수·앞뒤 빈 줄, 언어 없는 펜스, 120줄 초과인데 목차 없음, 깨진 링크, 빈 표 셀, 분모 없는 백분율, `(목표 <값>)` 표기 불일치(G16) | test | STYLEGUIDE §9 | **있음** — `gendoc`(`//:gendoc_test`, 2026-09-21 · G16 표기 통일성 2026-09-29 추가). 입력은 생성 뷰와 생성 SKILL.md 이고 뷰 목록의 단일 정의처는 `defs/kb.bzl` 의 `VIEWS` 다(2026-10-03 — 손 목록이 넷으로 갈려 개수가 어긋났다). 검사 함수는 `kb_lib.check_gendoc` 이고 생성기가 같은 함수를 쓴다. G16 은 표기 통일성만 게이트다 — "목표를 붙여야 하는가"는 사람 판단이다. G17(시점 의존 표현)은 오탐률 실측(후보 7건 전부 오탐)으로 게이트로 올리지 않고 `check_gendoc`의 둘째 반환값(보고 전용)으로만 낸다 | `gendoc` | 생성기(`tools/*.py`)의 출력 문자열을 고친다 — developer. 면제는 `waivers.md` |
| 카탈로그 정합성 | 스코프 없는 역할, 미부여 스코프, read plane 0, write plane 공유, `maxConcurrent` 합 > ODD 상한 | verify | 10.2 | **있음** — `validate` `check_catalog`(2026-09-13) | `catalog` | `kg/catalog-kg.ttl`·ODD를 고친다 — orchestrator(문서·그래프 같은 커밋) |
| 결정 역할 표지 | 결론·근거·대안 청크의 첫 산문 줄에 `**결론**`·`**근거**`·`**대안**`("대안 없음" 변형 허용) 없음, 선택 넷째 규약 청크(`conventions.md`)의 첫 산문 줄에 `**규약**` 없음 | test | 7.4 | **있음** — `chunk_lint` `decision-role`(2026-09-13, 규약 청크 2026-10-04 — [`p4-convention-slot`](../kb/dev/decision/p4-convention-slot/conclusion.md)) | `decision-role` | 본문 첫 줄을 고친다 — orchestrator |
| 규범 문서 | 어느 문서도 싣지 않는 `규약:` 줄(고아 줄), 두 번 실린 줄(이중 소비), 없는 결정·줄을 가리키는 항목, 강도를 요구하는 문서의 강도 없는 줄, `NORM_DOCS`와 `kb/dev/norm/` 디렉토리 집합의 불일치, 절 청크의 구조 위반(선언·순서·머리 청크의 키·첫 절의 깊이), 재생성과 바이트가 다른 생성 문서 | analysis + test | Q19-b | **있음** — `tools/gen_norms.py`(2026-10-04, [`p12-norm-documents-from-section-chunks`](../kb/dev/decision/p12-norm-documents-from-section-chunks/conclusion.md)). 생성 트리 파일이고 `//:norms_drift_test`가 재생성과 비교한다. 문서 목록의 단일 정의처는 `defs/kb.bzl`의 `NORM_DOCS`이고 비어 있어도 고아 줄 검사는 돈다. 절 키의 형식은 `chunk2kg`(`chunk2kg`)와 `norm-section-shapes`(`shacl`)가 본다 | `gen-norms` · `norms-drift` | 절 청크의 `items`나 결정의 `conventions.md`를 고친 뒤 `python3 tools/gen_norms.py --root .`를 돌린다 — orchestrator(청크)·developer(생성기) |
| 요소 탈락 | 소스 요소가 어휘에 슬롯이 없어 조용히 빠짐 — 청크 frontmatter 의 최상위 키 중 `chunk2kg` 가 소비하지 않는 것, 프로파일이 선언한 plane 실체 클래스와 `chunk2kg.PROFILE_SUBSTANCE` 치역의 대칭차 | verify | 8.21 G1 | **있음** — `validate` `element-drop`(2026-09-29). 현상 [`agt:elementWithoutVocabularyDropped`](../kb/ontology/related/defect/function-phenomenon-ontology.ttl)(P19)의 관측 수단이고 vnv 가 설계했다. 실체 대칭차는 `--ontology` 만으로 돌아 `//kb/ontology:gate_test`·`//kg:gate_test` 안에 있고, 키 전수 대조는 `//kg:gate_test` 가 `chunk_files`(`//chunks`·`//kb/dev`·`//kb/vv`·`//space`)로 청크 본문을 넘겨 돈다. 실측 2026-10-01: 키 25 대 30 차 공집합 · 실체 7 대 7 대칭차 공집합 | `element-drop` | 어휘를 넓힌다(키를 `chunk2kg` 가 읽고 `kb_lib.CHUNK_OPTIONAL_KEYS` 에 등재, 실체 클래스를 프로파일에 선언) — 요소를 버리지 않는다(가정 `asm-missing-vocabulary-is-signal`). developer |
| 판정 로그 | 판정 로그의 형식·필수 필드 위반 — 판정 표의 헤더가 규약(`kb_lib.JUDGE_LOG_TABLE_HEADER`)과 다름, 행의 질문 id·값·확신도·**판정자 식별자**(세션·모델, 2026-09-30)·입력 지문·시각 중 하나가 빔, 지문이 sha256(소문자 16진 64자)이 아님, 시각이 ISO 8601 UTC 초 해상도가 아님, 처리가 임계의 세 값 밖, **일치 열이 일치·불일치·해당 없음 밖**(2026-09-30), 판정 행 0건 | test | 8.14 | **있음** — `chunk_lint` `judge-log`(2026-09-29, 필드 개정 2026-09-30). 대상은 `generated.by` 가 `process:judge` 이고 `type: memory` 인 청크다. **판정 자체는 게이트 밖 도구**(`bazel run //tools:judge`)가 하고 게이트는 로그만 본다 — 판정자는 세션마다 다시 여는 **세션 판정자**이지 외부 서비스가 아니고(유저 답 2026-09-30), 확신도가 자기 보고라 같은 리비전도 판정자마다 다른 값을 낼 수 있어 여전히 게이트 밖이다 ([`p8-judge-calibration-binding`](../kb/dev/decision/p8-judge-calibration-binding/conclusion.md)). **PASS 조건은 "위반 0건"이고 판정 로그가 0건이면 거부할 것이 없어 그대로 PASS 다** — 로그의 존재를 요구하는 것은 이 게이트의 몫이 아니라서 SKIP 으로 내리지 않는다 | `judge-log` | 로그를 다시 낸다(`bazel run //tools:judge -- --record`) 또는 빠진 필수 필드를 채운다 — developer(도구)·vnv(판정). 면제는 `waivers.md`(축 `파일`) |
| 게이트 id 단일 정의처 | 코드의 게이트 태그가 `GATES` 리터럴 밖, `kb_lib` 에 손으로 둔 `*_GATE` 상수, `getattr` 폴백의 값 드리프트, 등록됐으나 코드에 닿지 않는 id | verify | 6.7 | **있음** — `validate` `check_gate_registry`(2026-10-02). 원본은 `defs/kb.bzl` 의 `GATES`(id → 계층·판정 도구·한글 라벨·설명)와 `TOOL_TAGS`(게이트가 아닌 입력 문제·보고 태그)이고 `kb_lib` 이 리터럴 읽기로 `*_GATE`·`*_TAG` 를 파생한다 — `RESIDENCY`·`EXTRACTED_SOURCES` 와 같은 해법이다. 리터럴의 자기 정합성(네 키·계층 어휘·두 목록의 서로소)은 `tools/BUILD.bazel` 의 `check_gates` 가 로드 시점에 본다. 그래프 개체는 `//kg:gates_kg`(`id:gate-<id>`)이고 총람 `id` 열과의 동일성은 `doccheck --gates` 가 본다 | `gate-registry` | 태그를 상수로 바꾸거나 리터럴에 등재한다 — developer |
| 요약 지지 참조 | 요약 블록의 `핵심:` 항목에 본문의 지지 블록을 가리키는 참조(`[#id]`·`d-NNNN`·IRI·마크다운 링크)가 없음 | test | judge-without-service 기계 환원 ① | **있음** — `chunk_lint` `summary-support`(2026-09-30). 대상은 살아 있는 `.md` 청크의 선택 슬롯 `핵심:`이고 슬롯이 없으면 대상이 아니다. 오탐 실측(2026-09-30): 0/0 — 이 저장소는 아직 이 슬롯을 쓰지 않는다. 보고 모드를 거치지 않고 즉시 게이트로 올린 근거는 그 실측이다(usage 0 이라 오탐이 원천적으로 0) | `summary-support` | `핵심:` 항목마다 지지 참조를 더한다 — 저작자. 면제는 `waivers.md`(축 `파일`) |
| 동결 문서 | 동결 문서(설계 노트)의 내용이 `kb_lib.FROZEN_DOCS`의 sha256과 다름 | test | Q15-c | **있음** — `doccheck --frozen`(`//:frozen_docs_test`, 2026-10-03). 노트는 기획 원본으로 동결됐고 미결은 청크의 `미확정:`으로 옮겼다 | `frozen` | 노트를 고치지 않는다. 고쳐야 하면 그 변경을 결정으로 세우고 상수를 바꾸는 것이 의도한 변경의 표시다 — orchestrator |

2026-09-11 Bazel 규칙 반영 후 기계화 10 · 부분 4 · 규약 1 · 없음 6이다. 없음의 대부분이 도입
5·7단계의 산출에 걸려 있다. `id`는 도구의 `FAIL [<id>]` 태그와 같다(agrtls A). 결정
`p6-gate-catalogue`가 같은 id를 적는다. 하네스 자체의 게이트 id(원본 `GATES`, 2026-10-02)는 `naming`(`//:naming_test`) ·
`build-drift`(`//:build_drift_test`) · `extract`·`extract-drift`(`//:extract_drift_test`) · `stamp`(`//tools:stamp`) · `token-budget`(`validate` — plane별 본문 토큰 상한의 표와 shape 의 동일성 + 어휘 파일 sha256) ·
`gate-registry`(`//tools:gate_registry_test` — 코드의 태그·상수·폴백이 `GATES`와 같은가) · `gates2kg`(생성=검사) · `labels`·`boundary`·`syntax`(`validate`의 온톨로지 품질 검사) · `restored`·`specialization`(`chunk2kg` 생성 시점) · `chunk2kg-merge`(`kb_kg_merge` — IRI 중복) · `gen-skills`·`skills-drift`(`gen_skills`) · `gen-norms`·`norms-drift`(`//:norms_drift_test`) · `case-gen`·`case-drift`(`//:case_drift_test`, 대상 0) ·
`channel`(`//harness:channel_lint_test`) · `doccheck`(`//:doccheck_test`) · `gendoc`(`//:gendoc_test`) · `addition`·`empty-value`·`list-rules`·`blocking-comment`·`judge-log`·`summary-support`(`chunk_lint`) · `space`(`space2kg` 생성=검사 — 게이트 id는 `space`다) ·
`odd2kg`·`taxonomy`(생성=검사) · `workset-budget`(`//kg:workset`, 앵커가 있을 때만) · `canon`(규약, 테스트 타깃 아님)이다. **게이트가 아닌 도구 태그** 아홉(`consistency`·`judge`·`link`·`open`·`propose`·`revalidate`·`tokens`·`validate`·`weave` — 입력 문제·보고)은 같은 대괄호 표기를 쓰되 `TOOL_TAGS`로 갈라 그래프 개체를 받지 않는다. 실패 종류(종료 코드 1·2·3)는
§게이트를 추가할 때에 적혀 있다.

## 코어 층 — 두 KB가 공유하는 도구

### 검사 (있음)

```bash
bazel test //...                 # 게이트 전체 (커밋 전 필수)
bazel run //tools:validate -- --ontology <files> --shapes <files> --odd <files> --data <files>
bazel run //tools:chunk_lint -- --chunks <files> --ttl <files>
bazel run //tools:canonicalize -- --write <files>    # 커밋 전 정규화
bazel run //tools:term_propose -- --id <slug> --kind class --parent agt:… \
    --label-ko … --label-en … --definition … --cq CQ# \
    --derived-from <관측 IRI> --derived-from <관측 IRI>   # 용어 제안 → 승인 큐
bazel build //kb/odd:odd //kb/dev:index              # 생성물: ODD 그래프·택소노미, 라벨 목록
tools/relock.sh                                      # 파이썬 의존성 재고정
```

#### 검사 3계층 (노트 2.5절 — 온톨로지 검사기)

| 계층 | 정의 | 이 저장소 |
|---|---|---|
| 구문·스타일 (report) | 라벨·정의 누락, 참조 구문, 폐기 규약 | `validate.py`의 labels·boundary + `chunk_lint` |
| **안티패턴** (verify) | "이런 트리플이 존재하면 실패"를 SPARQL로 명세 | `validate.py --verify-queries` — `tools/verify-queries/*.rq` 하나가 안티패턴 하나. 목록의 원본은 그 디렉토리이고 질의마다 `kb/dev/artifact/verify-queries/`의 청크다 |
| 논리 정합성 (reason) | OWL 추론기 (RL 프로파일 안) | SHACL + `--reason`(OWL-RL). shape로 자연스러운 것(수준 허용표·카디널리티)은 shape에 남긴다 |

**용어 제안 워크플로**(`term_propose`)는 일반화가 온톨로지에 닿을 때의 절차다. 에이전트는
신뢰할 수 없는 센서이므로 제안만 한다. 상위 실재·라벨 중복·정의 형식·근거 실재(관측·판정 주석 둘 이상, `prov:wasDerivedFrom`) 검사를 통과한 것만
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
| `cross-kb-link` | frontmatter 링크 키의 링크가 `verifies` 밖이면서 두 KB를 가로지르지 않는다. 예외는 검증 목표(functional) → 개발 요구 `derivesFrom` 하나다. 판정 함수 `kb_lib.cross_kb_link` 는 복원 후보 생성기와 공유한다 | [rules §8](rules.md#8-vv-규칙--vv-kb-노트-8285-811815-84-911) |
| `code-part-link` | 추출 트리 안에서 복합체의 부분인 청크(정의·구역 청크)는 `refines`·`serves`·`verifies` 의 끝점이 아니다 — 링크는 파일 청크 하나가 갖는다. 판정 함수 `kb_lib.code_part` 는 복원 후보 생성기와 공유한다 | [rules §7](rules.md#7-development-규칙--개발-kb-노트-7277) |
| `rung-before-descent` | 같은 높이의 V&V 대응물 없이 다음 높이로 내려간 하강이 없다 — R1 사다리 사슬(functional→abstract 목표 · logical→concrete 기준 · concrete→executable 검증기가 바인딩한 기준, 사람 확인 기준만 가진 요구는 면제). 판정 함수 `kb_lib.rung_violations` 는 `metrics` 와 대응물 집합(`kb_lib.vv_counterparts`)을 공유한다 | [rules §8](rules.md#8-vv-규칙--vv-kb-노트-8285-811815-84-911) |
| `verify` | 안티패턴 질의 결과 행 = 위반 | 위 표 |
| `shacl` | shape 적합성 (아래). `--waivers <waivers.md>`를 주면 위반의 focus node를 `agt:assertionLocation`으로 파일에 사상해 게이트 id `shacl`(축 `파일`)로 선언된 면제를 집계에서 빼고 `WAIVED [shacl] <파일>: <sh:resultMessage>` 줄로 남긴다 (2026-10-01) | [rules](rules.md) |

`vocab`이 핵심 방어선이다. 어휘 우회를 막지 못하면 나머지 규칙이 전부 우회된다.

#### SHACL shape — `kb/ontology/shapes/`

| 파일 | 대상 | 주요 제약 |
|---|---|---|
| `chunk-shapes.ttl` | `agt:Chunk` | `tokenCount` 0 이상 정수 하나 · `hasLevel` 정확히 1 · 한/영 라벨 각 1 · `status` 값. 크기의 **상한**은 여기 없다 — plane별 프로파일 파라미터라 `token-budget-shapes.ttl` 이 본다 |
| `token-budget-shapes.ttl` | plane별 `…Chunk` | 본문 `tokenCount` 상한 — 저작 산문 1,092(42×26) · `artifact`·`memory` 2,856(42×68). 값의 단일 정의처는 `tools/kb_lib.py` 의 `BODY_TOKEN_LIMITS` 이고 게이트 `token-budget` 이 둘의 동일성과 어휘 파일 지문을 본다 ([`p1-chunk-unit-is-tokens`](../kb/dev/decision/p1-chunk-unit-is-tokens/conclusion.md), 2026-10-01) |
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
| `layer-shapes.ttl` | `agt:inLayer` 주어 | 항목의 서비스 층이 정확히 하나이고 값이 `knowledge`·`methodology`·`process` 셋 중 하나다. 층 개체 자체는 층에 속하지 않는다 (2026-10-01) |
| `exposes-factor-shapes.ttl` | `agt:exposesFactor` 주어 | frontmatter `exposes`의 대상이 `defect` 모듈이 선언한 현상 개체다. 없는 개체와 요인 아닌 개체를 둘 다 거부한다 — 링크 개체도 deps도 아니라 여기가 유일한 실재 검사다 (2026-09-29) |

라벨 제약은 `sh:qualifiedValueShape` + `sh:qualifiedMinCount`로 쓴다. `sh:languageIn`은
모든 값에 적용되어 "한글 하나 + 영어 하나"를 표현하지 못한다.

shape의 면제도 `waivers.md` 하나에 선언한다(2026-10-01). `//kg:gate_test`가 `waivers = "//docs:waivers"`로
그 표를 넘기고 `validate`가 위반마다 focus node를 `agt:assertionLocation`으로 파일에 사상해 게이트 id
`shacl`(축 `파일`)의 선언과 대조한다. 면제된 위반은 집계에서 빠지고 `WAIVED [shacl]` 줄로 남는다 —
`chunk_lint`의 `chunk` 면제와 같은 규약이고 같은 파일이 두 게이트에 두 행으로 선언된다. **shape는 고치지
않는다** — 상한을 낮추면 면제 대상이 아닌 파일의 판정까지 약해진다.

#### `chunk_lint.py` — 파일 게이트

`chunk`는 본문 토큰 상한을 강제한다 — 저작 산문 1,092(42×26) · `artifact`·`memory` 2,856(42×68)이다.
단위는 줄이 아니라 토큰이고 계수기는 `o200k_base`(`MODULE.bazel` 의 `http_file` 이 sha256 으로 고정, 네트워크
없이 runfiles 에서 읽는다) 하나다. 본문을 떼는 판정처는 `kb_lib.body_text` 하나이고 `.md`는 frontmatter를
제외하고 `.ttl`은 `@prefix`·주석·빈 줄을 제외한다. 어휘 파일이 없거나 해시가 고정값과 다르면 판정하지 않고
죽는다(`EXIT_CONFIG`·`FAIL [chunk]`). `naming`은 파일명 접미사
규약(`-ontology`/`-rules`/`-shapes`/`-space`/`-kg`/`-odd`)을 강제한다.
**온톨로지 파일도 토큰 상한을 받는다.** chunk는 포맷이 아니라 구조 규칙이기 때문이다.
`chunk`도 `--waivers`가 받는 게이트 id다(2026-10-01) — `waivers.md`(축 `파일`)로 면제된 파일의 상한 초과는 집계에서
빼되 `WAIVED [chunk]` 줄로 남긴다. append-only 기록(판정 로그 등)의 소급 분할이 기록을 다시 쓰는 일이라 면제가
유일한 해소인 경우가 그 자리다 — 새로 쓰는 로그는 상한 안에서 나누므로 면제가 늘지 않는다.

`decision-role`의 표지는 파일 경로가 정한다. `conclusion`·`rationale`·`alternatives`가 **결론**·**근거**·**대안**이고, V&V 시나리오 패키지(`kb/vv/scenario/`)의 `<슬러그>-stimulus.md`·`<슬러그>-factors.md`·`<슬러그>-excluded.md`가 **자극**·**요인**·**배제 자극**이며(선언 청크 = `-stimulus`, 타깃 이름도 그것이다), 그 밖(단일 파일 옛 결정·단일 청크 시나리오)이 **결론**이다(2026-09-29, [`p8-scenario-authoring`](../kb/dev/decision/p8-scenario-authoring/conclusion.md)). 접미 판정을 시나리오 패키지로 한정한 것은 `chunks/decision/d-0140-three-defect-factors.md`처럼 stem이 `-factors`로 끝나는 옛 결정이 있기 때문이다.

청크를 파싱하는 도구는 전부 `--residency <defs/kb.bzl>` 를 받는다(2026-09-27 — `chunk2kg`·`consistency`·`weave`·`labels`·`space2kg`·`revalidate`·`vv_run`·`assume_check`·`label_sample`·`gen_build`). 인자가 없으면 `EXIT_CONFIG` 다. 직접 실행은 `--residency defs/kb.bzl` 을 명시한다.

#### 생성기 = 검사기

| 도구 | 입력 → 산출 | 실패 조건 |
|---|---|---|
| `chunk2kg.py` | 청크 frontmatter → head 그래프. plane을 개발 프로파일의 실체 클래스로 함께 타이핑하고 요구의 `pattern`을 방출한다(2026-09-18). **타깃별 조각**(`--fragment`, `kb_chunk`·`kb_decision` 액션) → `kb_kg_merge`(`--merge`) → `bazel-bin/kg/chunks-kg.ttl`. 바뀐 타깃의 조각만 다시 만든다. 묶음의 단위는 파일이 아니라 **액션의 입력 집합**이다 — `kb_decision`(셋 고정)·`kb_composite`(2~9 가변)가 그 집합을 만들고 `kb_chunk` 하나로는 복합체가 서지 않는다. 위험에서 파생된 항목의 선택 키 `exposes: [<agt: 현상 IRI>…]`를 `agt:exposesFactor`로 방출한다(2026-09-29) — 링크 키가 아니라 `targets`와 같은 자리이고 Bazel deps가 되지 않는다. 정의 청크의 선택 키 `uses: [<청크 IRI>…]`를 `agt:usesDefinition`으로 방출한다(2026-09-30, `type: artifact`에서만 — 정의역이 `agt:ArtifactChunk`다) — 같은 자리이고 값의 원본은 손이 아니라 `extract`다. 서비스 층의 선택 키 `layer: knowledge | methodology | process`를 `agt:inLayer`로 방출하고 **명시가 없으면 `agt:knowledgeLayer`를 방출한다**(2026-10-01, plane 제한 없음 — 층은 plane과 직교하는 역할 속성이다). 기본값을 그래프에 적는 이유는 표시 누락이 산발로 세어지지 않아야 하고 층별 집계(CQ-38)의 분모가 항목 전수여야 한다는 것이다 ([`p0-service-is-a-three-layer-wiki`](../kb/dev/decision/p0-service-is-a-three-layer-wiki/conclusion.md)). 값이 어휘 밖이면 거부한다. 복합체 선언의 선택 키 `composite: {…, ordered: [<부분 IRI>…]}`가 있으면 `agt:Composite , co:List`로 타이핑하고 부분마다 `co:item [ a co:ListItem ; co:index "<1..n>"^^xsd:positiveInteger ; co:itemContent <부분> ]`을 그 순서로 낸다(2026-09-29). 없으면 `hasDirectPart`만 낸다 — 순서를 요구하지 않는 것에 순서를 붙이면 거짓 정보다. **예외는 없다**(유저 승인 2026-09-29) — 결정 복합체도 선언으로만 순서를 갖고 그 선언은 생성 BUILD 의 명시 인자를 통해 `--ordered <IRI>`(부분마다 한 번)로 들어온다. 이 도구는 역할 이름·파일 stem 으로 순서를 추측하지 않는다. `--ordered`와 frontmatter `composite.ordered`가 함께 있으면 같아야 한다 — BUILD는 뷰이고 frontmatter가 원본이므로 불일치는 드리프트다 ([`p4-composite-order-is-declared`](../kb/dev/decision/p4-composite-order-is-declared/conclusion.md)). 본문 슬롯 표지(`agt:bodySlot`)는 굵은 span 이 그 줄의 필드 자리(줄 머리·불릿 `- ` 다음·앞선 필드의 ` · ` 다음)에 있고 표지 뒤 한정어가 짧을 때(마침표 없음, 길이 `BODY_SLOT_QUALIFIER_MAX` 이하)만 방출한다(`body_slots`, 2026-09-29) — 표 셀·산문 접속·목록 항목 전체를 감싼 굵은 강조는 자리가 아니라 표지로 방출하지 않는다. | 필수 키 7개 누락, 값 어휘 밖, 복합체 미선언(조각), `ordered`가 목록이 아님·부분 중복·**부분 집합과 불일치**, **IRI 중복**(병합) — "한 chunk는 한 파일"의 기계적 강제 |
| `extract_refs.py` | 본문의 `d-NNNN` 인용 → `references-kg.ttl`의 `agt:cites`; 본문의 `agt:<Term>` 표기 중 온톨로지가 정의한 용어 → `agt:usesConcept`(복원 경로, dependency-graph (f)). 온톨로지에 없는 표기는 `info`로 집계만 한다 | 인용 대상이 실재하지 않음 |
| `run_evidence.py` | 실행 기록의 케이스 판정(pass → 실행(+) · fail → 실행(−))과 코드 파일 청크의 테스트 통과 도장(`process:bazel-test`) → 코드 파일 청크 → 결정 결론의 `satisfies` 후보 링크와 증거 항목(`agt:runResult`). 출력은 `references-kg.ttl`에 이어 붙는다(p9-evidence-ledger) | 읽을 수 없는 청크·값 어휘 |
| `odd2kg.py` + `taxonomy.py` | OpenODD YAML 매핑 문서 `kb/odd/project-odd.yml`(`TAXONOMY`·`MODULES`·`INCLUDE_AND`…) → `project-odd.ttl`; `related/condition` → `taxonomy.yml` (부록 E.4) | 택소노미 밖 범주 · 미선언 속성 · 선언 밖 리터럴 · OpenODD 식이 아닌 값 · `ATTRIBUTES`/`CHECKS` 없는 조건 |
| `gates2kg.py` | 게이트 등록부 `defs/kb.bzl` 의 `GATES` 리터럴 + 등록부 사이드카(`tools/*.chunks.yml`) → `bazel-bin/kg/gates-kg.ttl` 의 `id:gate-<id>` 개체. 게이트는 프로세스 층의 **항목**이라 그래프에 개체가 서야 층별 집계(CQ-38)가 셀 자리를 갖는다 ([`p0-service-is-a-three-layer-wiki`](../kb/dev/decision/p0-service-is-a-three-layer-wiki/conclusion.md)). 개체마다 한/영 라벨·`skos:definition`·`agt:inLayer agt:processLayer`·`agt:gateTier`·`agt:enforcedBy`(판정 도구의 파일 복합체 — `agt:judgedBy` 는 정의역이 `agt:Chunk` 인 개발 프로파일의 술어라 쓸 수 없다)를 낸다 — 판정 도구가 파이썬 밖(`starlark`·`bazel`)인 게이트는 가리킬 코드 청크가 없어 마지막 술어를 갖지 않는다. 생성물이라 `kg/` 에 손으로 쓰지 않는다 | 항목의 네 키 누락 · 계층이 `GATE_TIERS` 밖 · 판정 도구의 파일 복합체 부재 |
| `labels.py` | 청크 head → OKF `index.md` (5.6절) | frontmatter 오류 |
| `metrics.py` | 그래프 → `metrics.md` (4.13절 지표, CQ19·CQ20, 14.1 통과 조건; 구축에는 frontmatter 링크 개체와 본문 식별자 추출(`cites`·`usesConcept`)이 들어가고 복원은 후보 파이프라인 산출만(유저 결정 2026-09-12 (b)), 가정 절에 "기본 가정만 가진 청크"). 연결 성분과 CQ20 후방 추적은 `prov:specializationOf` 를 **연결로 센다**(2026-10-01) — 분할 조각은 원 청크의 정체성을 나눠 가진 것이지 새 지식이 아니고 링크는 승계 청크가 가지므로([`p10-split-keeps-work-identity`](../kb/dev/decision/p10-split-keeps-work-identity/conclusion.md)) 조각이 그 키 하나만 가져도 고립이 아니다. 그 술어는 추적 링크 네 족 밖(PROV-O)이라 링크 밀도·TIM 에는 들지 않는다. 연결로 세는 술어의 단일 정의처는 `kb_lib` 의 `LINKAGE_PREDICATES`·`ASCRIPTION_PREDICATES`·`COMMUNITY_EDGE_KINDS` 셋이고 `metrics`·`community` 가 거기서 읽는다. 연결 성분은 `kb_lib.linkage_predicates` 로 세 족의 하위 속성을 T-Box(`//kb/ontology:modules`)에서 전이적으로 더하고 복합체를 경유 노드로 둔다(2026-10-04) — 절 청크의 `agt:projectsConvention`(치역 결정 복합체)과 중첩 복합체(문서 → 묶음)가 그 경로로 이어진다. 성분이 1보다 크면 「주 성분 밖 청크」 절이 성분마다 라벨·plane·경로를 낸다 — 수만으로는 무엇이 떨어졌는지 보고서로 알 수 없다 | 그래프 파싱 실패 |
| `stamp.py` | 등록부의 `tested: {rev, at, source_hash}` 를 갱신한다 — `artifact` 의 `verified` 는 사람 검토가 아니라 **테스트 통과** 도장이고 판정 주체가 바뀐 것이지 검사가 약해진 것이 아니다 ([`p7-code-extraction-direction`](../kb/dev/decision/p7-code-extraction-direction/conclusion.md) "도장"). **`bazel test //...` 가 종료 0 으로 끝난 뒤에만 돌린다** — 중첩 Bazel 호출을 피하려고 도구가 스스로 테스트를 부르지 않으므로 그 순서는 규범이다. 도구가 지키는 것은 리비전이 실재를 가리키는가 하나다: `--rev` 가 없으면 소스가 커밋되어 있어야 한다. 추출기가 `tested.source_hash` 가 지금 소스와 같을 때만 `verified: [{by: process:bazel-test, at: …}]` 를 낸다 — 소스가 도장 뒤에 바뀌면 `verified` 가 빠져 수정 뒤 미검증이 되고 재판정이 자동이다 | 커밋되지 않은 소스에 `--rev` 없는 도장 · `source` 없는 등록부 |
| `extract.py` | 소스 파일 하나(`tools/*.py`) + 등록부 사이드카(`<소스>.chunks.yml`) → `kb/dev/artifact/<모듈>/`의 청크 트리 (`artifact`×`executable`). 코드가 원본이고 청크는 생성물이다 ([`p7-code-extraction-direction`](../kb/dev/decision/p7-code-extraction-direction/conclusion.md)). 구조는 파일 복합체 → 절 복합체(소스의 절 주석 `# ══ 장` · `# ── 절`) → 정의 청크 셋이고, 링크(`refines`)는 등록부가 주어 파일 청크와 절 청크(복합체의 선언 청크)에만 붙는다 — 정의 청크는 `part_of`로만 존재해 함수 churn이 링크를 움직이지 않는다 ([`p7-code-links-on-file-composite`](../kb/dev/decision/p7-code-links-on-file-composite/conclusion.md)). 한정 이름 → uuid의 원본은 등록부이고 신설만 자동이다 — 개명·삭제는 사람의 편집이다. 등록부의 손 필드 `layer`는 소스 하나의 서비스 층이고 추출기가 생성 청크 전부(정의·절·파일)의 frontmatter로 옮긴다(2026-10-01) — 도구는 프로세스 층의 실행 표면이라 값은 `process`이고 실측 37 등록부·청크 642다. 정의 청크는 선택 키 `uses: [<청크 IRI>…]`를 갖는다(2026-09-30) — 최상위 정의를 이름으로 쓰는 관계이고 해소는 AST 의 이름 참조뿐이다. 모듈 안 해소(`used_defs`)의 제외는 다섯이다(자기 자신·섀도잉된 이름·최상위 정의가 아닌 이름·`ast.Attribute`의 뒤쪽 이름·다른 모듈의 이름). 경계는 둘이고 둘 다 `--residency`(기본 `<루트>/defs/kb.bzl`)의 리터럴이 단일 정의처다. **방출 경계** `EXTRACTED_SOURCES` 안의 소스에서만 내고 — 추출기가 하나라 경계가 없으면 37 파일이 한꺼번에 든다(유저 답 2026-09-30) — 표본 하나에서 시작해 37 파일 전부로 넓혔다(2026-10-01, 유저 답 1). **치역 경계** `USES_TARGETS` 안의 모듈만 모듈 밖 대상으로 삼는다(2026-10-01, 유저 답 1 — 표본 쌍 `kb_lib` 하나부터, 넓히기는 그 리터럴에 이름을 더하는 것이다). 모듈 밖 해소(`import_bindings`·`used_foreign_defs`)는 최상위 import 와 정의 안의 늦은 import 가 묶은 이름을 보고 `kb_lib.<이름>`(별칭 포함)과 `from kb_lib import <이름>`의 `Load` 참조를 대상 모듈 등록부의 `fn:`·`cls:` uuid 로 푼다 — 제외는 넷이다(`as` 별칭으로 철자가 바뀐 이름·섀도잉된 뿌리·등록부에 없는 이름(상수·모듈 변수)·치역 경계 밖의 모듈). 실측 `agt:usesDefinition` **667** 트리플(모듈 안 484 · 모듈 간 183, 치역은 전부 `kb_lib`), 오탐 0·누락 0(독립 정규식 대조 186 중 3은 docstring 인용). `EXTRACTED_SOURCES`의 단일 정의처는 `defs/kb.bzl`이다(M1, 2026-10-01 — `BUILD.bazel`은 그 리터럴을 load 하고, `kb_lib.load_extracted_sources`가 `ast.literal_eval`로 읽어 파생한다. 전에는 둘로 적혀 있었다). `tools/BUILD.bazel`의 `check_extracted_sources`가 등록부 사이드카의 존재와 그 목록이 같은 집합인지 로드 시점에 강제한다 — 갈리면 bazel 명령이 바로 FAIL 한다. **질의 디렉토리**(2026-10-03, 2단계 편입)도 같은 방향으로 추출한다 — 목록의 단일 정의처는 `defs/kb.bzl`의 `EXTRACTED_QUERY_DIRS`이고 소스는 디렉토리 `tools/<이름>`, 그 안의 `*.rq` 질의 파일 하나가 청크 하나(`kb/dev/artifact/<이름>/<stem>.md`)다. 질의는 정의로 나뉘지 않으므로 파일 전체가 인용 하나이고 복합체를 세우지 않으며 링크는 청크마다 붙는다. 등록부는 `tools/<이름>.chunks.yml`(키 `query:<stem>`)이고 `source_hash`는 디렉토리 안 질의 파일 전부의 해시다(`source_digest` — 도장도 같은 함수를 쓴다). 드리프트 테스트는 `//:extract_drift_<이름>`(`-`는 `_`)이고 게이트 id는 같은 `extract-drift`다. 커밋한다 | 직접 부분 9개 초과(절 주석을 요구한다) · 개명 안내(본문 해시가 같고 이름만 다름) · 등록부에 있는데 소스에 없는 이름 · `--check`의 어긋남 |
| `gen_build.py` | 청크 frontmatter → `BUILD.bazel`(`kb_chunk`·`kb_decision`·`kb_composite` 타깃, 링크 = deps; `kb/vv/{goal,scenario,criteria,case,verifier}/`는 디렉토리 = plane). `kb_composite`의 `ordered`·`part_iris`는 선언 청크의 `composite.ordered`를 옮긴 뷰이고, 선언이 없으면 `ordered` 인자도 없고 `part_iris`는 `srcs` 순서로 뜻을 갖지 않는다. **결정 묶음의 `ordered`는 생성기가 넣는다**(필수, 결론·근거·대안 — 유저 승인 2026-09-29: 결정도 예외 없이 선언한다. 205개 `conclusion.md`를 손으로 고치는 것이 첨가이므로 선언의 자리를 생성 BUILD의 명시 인자로 둔다). 커밋한다 | 세 청크 없는 결정 디렉토리 · 끊긴 링크 · `_check_bundle`(패키지 밖 부분·부분 수·이질·`ordered`가 부분 집합과 불일치·**시나리오 묶음(`kb/vv/scenario/`의 `-stimulus`·`-factors`·`-excluded`)에 `ordered` 없음** — 자극 → 요인 → 배제 자극의 읽기 순서가 정해져 있어 선언 없는 묶음은 거짓 무순서다) |
| `consistency.py` | 청크 본문 + 용어집 → `consistency.md` (`bazel build //kb:consistency`): 정확·근사 중복, 묶인 쌍(`coUpdatesWith`)의 응집 저하(본문 5-gram Jaccard < θ/2 — 의미 응집 검사의 첫 형태, 학습 모델 임베딩은 ODD 명시 제외), 라벨 중복, 결론 라벨 형식(결론만 — 근거·대안 라벨은 명사구 관례), 용어집 옛 표기, 중복률, ⑧ 첨가(메타 문장·채움 문구·빈 값 이상 표기 — `p4-three-empty-values`), ⑨ 목록 규칙(손 번호·항목 수·중첩·항목 길이 — `p4-slot-answers-one-question`), ⑩ 중복 확정 후보(①·③의 미묶음 쌍을 판정자 질문 "이 두 블록은 같은 주장을 담는가?"의 입력으로 다시 낸다), ⑪ 자리 후보(둘 이상의 본문 슬롯을 가진 청크에서 다른 슬롯의 표지 낱말이 자리 밖으로 등장하는 문장을 판정자 질문 "이 문장이 그 슬롯에 있어야 하는가?"의 입력으로 낸다). ⑧·⑨는 2026-09-22에 더했고 **게이트가 아니라 보고**다. 수치가 0이 된 뒤 `chunk_lint`로 올린다. ⑩·⑪은 2026-09-30에 더했고(judge-without-service 기계 환원 ②) **후보 생성까지이며 게이트로 올리지 않는다** — 확정은 판정자(사람 또는 세션 판정자, `tools/judge.py`) 몫이다. 보고 뷰이며 게이트가 아니지만 `//kb:consistency_build_test`가 `bazel test //...`마다 생성한다(rules.md "커밋마다") ([`p4-redundancy-as-safety-margin`](../kb/dev/decision/p4-redundancy-as-safety-margin/conclusion.md)) | 파싱 실패 |

#### 하네스 도구 — 역할 규약과 인수

| 도구 | 하는 일 | 게이트 |
|---|---|---|
| `channel_lint.py` | 하네스 채널(`harness/channel/` 메시지 · `harness/user/` 질문지) 규약 — 어휘, 단일 작성자, type별 방향, `task` 필수 절, `re`·`source` 실재, `result` 없는 `task`의 완료 거부, hci 반영 흔적 | `//harness:channel_lint_test` |
| `endorse.py` | 인수 — plane 쓰기 권한이 있는 역할이 검토한 청크에 `verified`를 붙인다. `//kg:gate_test`의 writer 검사(`generated.by` 역할 × 카탈로그 쓰기 권한)를 해소하는 수단이다 | `bazel run //tools:endorse -- --by <역할>/<모델> --at <시각> <청크…>` |
| `label_sample.py` | 라벨 대표성 실험 표본 — 층화 표본 + 미끼, seed 고정 ([`label-representativeness-protocol`](../harness/user/archive/legacy/label-representativeness-protocol.md)). `sheet.md`의 척도 문구는 프로파일(`kb_lib.judge_load_profile`·`judge_questions`)에서 그대로 읽는다(단일 정의처, 2026-09-30). `--judge-sheet <dir>`(선택)을 주면 세션 판정자에게 줄 `labels.md`(라벨+`kb_lib.label_fingerprint` 대조 지문)·`bodies.md`(본문)를 낸다 — 생성 머리·경로·seed 없이, **워크스페이스 밖**에만 쓴다(안이면 거부) | 게이트 아님 — 실험 |

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

`bazel run //tools:vv_run -- [--record] [--case <슬러그>…] [--verifier <슬러그>…]` — 케이스(`kb/vv/case/*.md`)와 검증기(`kb/vv/verifier/*.md`) 본문의 `**실행 명령**`을 읽어 읽기 전용
검증기(`bazel test`·`bazel build`·`bazel query`·`gen_build --check`)만 실행하고 그 밖(임시 파일 자극·`bazel run`)은 SKIP으로
적는다. 검증기는 케이스와 같은 줄 꼴·허용 목록·기대 대조·판정 규칙으로 돈다(2026-10-04, 유저 답 Q29-a — 비표본 판정을 검증기로 옮긴 뒤에도 그 명령이 실행 경로에 남는다). 선택이 없으면 둘 다 돌고, `--case` 만 주면 케이스만의 보고·기록 꼴 그대로다. 실행 기록은 검증기 행을 케이스 표와 따로 둔 검증기 표(`kb_lib.RUN_VERIFIER_TABLE_HEADER`)에 적는다 — 실행 증거(`run_evidence`)는 케이스 표만 읽고, 검증기는 `verifies` 가 없어 증거 쌍이 서지 않는다. 실행 명령 줄이 없는 검증기는 실행 대상 밖으로 따로 센다. 고정물 시험은 `//defs/tests:vv_run_fixture_all_test` 와 같은 꼴의 셋(`all`·`case`·`verifier`)이다. 케이스 판정은 **명령 전부를 실행해** 전부 0이면 `pass`, 실행분에 실패가 있으면 `fail`, **건너뛴 명령이 하나라도 있으면** `skip`이다(2026-09-22 정정). 건너뛴 쪽이 게이트가 거부한다는 것을 보이는 절반이므로 절반만 실행한 케이스는 기준을 보이지 못한다 — SKIP은 PASS가 아니다(실패 종류 3). 보고는 명령 단위 집계(`실행`·`건너뜀`·`명령`)를 따로 낸다. 리비전(**변경된 추적 파일 수** — `git status --porcelain --untracked-files=no` 의 줄 수)·UTC 시각·bazel·python 버전·명령별 종료 코드·소요를 적는다. 변경된 추적 파일이 있으면 그 실행의 케이스 판정을 `재현 불가 후보 n/N = p.p%` 로 보고와 실행 기록의 판정 요약에 함께 센다(2026-10-01) — 같은 리비전을 다시 체크아웃해도 같은 입력이 아니기 때문이고, 이것이 현상 `agt:concurrentSessionState`(P22)의 관측 수단이다. `--record`는 실행 기록(`kb/vv/run/run-<시각>.md`, memory
plane, concrete, `generated.by: process:vv_run`)을 append-only로 남긴다 — 도구가 executor 하위 역할을 맡는 첫 형태라 writer
검사 밖이다. 종료 코드는 fail 1 · pass 0 · skip만 3이다. **기대 대조와 자극 생성이 2026-09-23에 들어왔다**([`p8-machine-readable-case`](../kb/dev/decision/p8-machine-readable-case/conclusion.md)). 케이스가 `**자극**`·`**기대**` 산문 옆에 `yaml` 펜스로 `files`(이름 → 내용)와 `expect`(명령마다 `exit`·`contains`)를 적으면, 검증기가 자극을 임시 디렉토리에 쓰고 명령의 `{{이름}}`을 실제 경로로 바꾼 뒤 실행하고 지운다. 판정은 종료 코드와 문구가 **둘 다** 맞아야 통과다 — 종료 코드만 보면 기대한 사유로 실패했는지 모른다. 펜스가 있는 케이스에 한해 저장소 자신의 읽기 전용 검증기(`python3 tools/<v>.py`, 닫힌 집합 열 — 2026-09-26에 `assume_check` 가 들었다)를 더 실행하되 **허용 목록은 그대로 보안 경계다** — 위험은 자극의 유무가 아니라 명령이 무엇을 할 수 있는가에 있다. 리다이렉션·파이프·백틱이 있으면 실행하지 않는다. **쓰기 인자도 막는다** — `--record`(관측을 쓴다)와 저장소 안 경로의 `--out`(`{{이름}}` 자극이 아닌 값)은 SKIP 이고 사유가 수정 방향이다. `--break <조건>` 은 읽기만 하므로 실행된다. 이 검사는 `assume_check` 전용이 아니라 허용 목록 전체에 걸린다. `--out /dev/null` 같은 예외는 열지 않았다 — 허용 목록은 보안 경계라 넓히는 판단은 승인 사항이다. **`bazel run //tools:<v>` 형태는 허용 목록 밖이고 `FAIL [vv-case]`로 실행 전에 거부한다** — 그 형태는 작업 디렉토리가 runfiles 트리라 상대 경로가 자극에 닿지 못하고, 그때 나오는 입력 단계 오류가 기대한 거부와 같은 종료 코드·문구를 내 거짓 통과를 만든다([`p8-verifier-env-isolation`](../kb/dev/decision/p8-verifier-env-isolation/conclusion.md)). 명령은 워크스페이스 루트를 작업 디렉토리로, 실행기의 파이썬·runfiles 변수(`PYTHONSAFEPATH`·`PYTHONPATH`·`PYTHONHOME`·`RUNFILES_*`)를 걷어낸 환경에서 돈다 — 실행기를 부르는 방식이 판정을 바꾸면 재현이 아니다. `python3 `로 시작하는 명령(검증기를 직접 부른다)은 예외 하나를 받는다(2026-10-01) — 인터프리터를 vv_run 자신의 `sys.executable`로, `PYTHONPATH`를 vv_run 자신의 `sys.path` 중 하네스의 pip 폐포(site-packages) 항목만으로 바꾼다(`verifier_env`). 걷어내는 대상은 실행기의 **도구 모듈** 문맥(runfiles 사본의 `tools/`)이지 서드파티 패키지가 아니므로 [`p8-verifier-env-isolation`](../kb/dev/decision/p8-verifier-env-isolation/conclusion.md)과 어긋나지 않는다 — bare `python3`에 `tiktoken` 같은 하네스 전용 패키지가 없어 토큰 계수가 들어간 검증기가 자극에 닿기 전에 `ModuleNotFoundError`로 죽는 문제(이 저장소 실측, 2026-10-01)의 해소다. vv_run의 BUILD 의존에 `tiktoken`·`pyshacl`·`owlrl`을 더해 그 폐포에 READ_ONLY_VERIFIERS 전체가 쓰는 서드파티 패키지를 올렸다. 토큰 계수기 어휘 경로는 실행기가 `--vocab`으로 받아 `KB_TOKENIZER_VOCAB` 환경 변수로 넘긴다 — 값의 원본은 `tools/BUILD.bazel`의 `args = ["--vocab=$(rootpath @tiktoken_o200k_base//file)"]`이고 다른 도구와 같은 꼴이다(2026-10-01). **runfiles 탐색을 배선의 원본으로 쓰지 않는다** — `use_repo_rule`로 만든 저장소의 runfiles 디렉토리 이름은 canonical 이름 `+http_file+tiktoken_o200k_base`이고 apparent 이름만 찾던 `chunk2kg.tokenizer_vocab_path`의 후보는 전부 빗나갔다(이 저장소 실측 2026-10-01 — 환경 변수가 비어 가 케이스 `token-budget`·`chunk-42-lines`가 자극에 닿기 전에 죽었다). 그 후보에 canonical 이름도 더했고 명시 경로가 우선이다. 어휘를 못 찾으면 `vv_run`은 케이스를 하나도 돌리지 않고 `EXIT_CONFIG`로 죽는다 — 건너뜀은 판정이 아니라 판정의 공백이므로 `FileNotFoundError`를 삼키지 않는다. 펜스가 없는 케이스는 지금처럼 양성 명령만 돈다(점진 도입). 형식 위반은 `FAIL [vv-case]`로 실행 전에 멈춘다. 임시 파일 자극의 자동 생성은 이로써 갖춰졌고 seed 고정은 후속이다.

**2026-10-04** — 허용 목록의 읽기 전용 검증기에 `revalidate` 의 **스냅숏 꼴**(`--base-dir`·`--head-dir` 또는 `--base-files`·`--head-files`)이 들어왔다(유저 답 Q38-c). 기본 꼴(`--base <rev>`)은 git·`bazel query` 를 불러 SKIP 이다. `--round stop-rule|budget|complete` 는 케이스를 돌리지 않고 검증 라운드 하나를 닫는 라운드 기록 `kb/vv/run/round-<UTC>.md`(memory, append-only)를 남긴다(유저 답 Q39-c) — 라운드 번호 · 구간 안 신규 결함 수 · 종료 사유. 종료 사유는 온톨로지 `round-end-reason-ontology.ttl` 의 개체 셋이고 정지 규칙은 verify 질의 `round-stop-rule-violated` 가 판정한다.

#### `odd_check.py` — ODD 모니터링 (3.5절, 도입 2단계)

`bazel run //tools:odd_check`는 ODD 문서 `CHECKS.<속성>.cmd`를 실행해 속성마다 in / out / unverified를
판정하고 이탈을 보고한다. 종료 1은 이탈이다. 네트워크·호스트 상태를 보므로 테스트 타깃이 아니다.
첫 모니터링(2026-09-11)은 7속성 전부 in, 이탈 0이었다.

### 활용 (첫 형태 11)

**첫 형태가 있는 것은 `workset`·`metrics`·`impact`·`handoff`·`consistency`(2026-09-11)와
`query`·`propagate`/`revalidate`(2026-09-14)·`weave`·`gen_skills`(2026-09-19)다.** `link`(복원 후보 생성)도 2026-09-19에 생겼다.
`gendoc`(2026-09-21)은 활용 도구가 아니라 생성 문서 전부의 형태 게이트이고, 생성기가 쓰는 머리 블록·검사 함수의 정의처는
`kb_lib`다([`STYLEGUIDE.md` §9](../STYLEGUIDE.md#9-생성-문서-bazel-binmd--생성-트리-파일)). 없는 것은
tangle이다. 구축 쪽 공백의 공통 원인은 하네스의 도구가 읽기·쓰기 집합을 기록하지 않는 것이다. 활용 도구가 없으면 "온톨로지를 활용하는 방법론"이 성립하지 않는다.

| 도구 | 대응 절차 | 하는 일 | 단계 |
|---|---|---|---|
| `workset` / `labels` | [method §8 조회](method.md#8-조회) | **첫 형태 있음** — `bazel build //kg:workset --//kb:role=<role> --//kb:anchor=<라벨|IRI> --//kb:levels=<창> --//kb:hops=1 --//kb:budget=200` → `bazel-bin/kg/workset-<role>.md`: 역할 스코프(plane) × 수준 창 × 앵커 이웃(상류 ∪ 하류), 족별 우선순위(앵커 ≫ references ≫ semanticallyDependsOn ≫ 구성 관계 ≫ relatedTo ≫ 시간축) 뒤 예산 패킹, 초과분은 라벨만(dependency-graph §4, 2026-09-12). 선택자는 빌드 설정이라 BUILD를 고치지 않는다. 정의(0.5절 정정본)대로 앵커가 양을 거른다 — 앵커 없이 573줄, 앵커를 주면 14줄이다 | 2 |
| `link` | [method §6 연결](method.md#6-연결) | **첫 형태 있음**(2026-09-19) — 복원 후보 생성기 `bazel build //kg:link_candidates` → `bazel-bin/kg/link-candidates.md`: 그래프 union만으로 본문 식별자(`cites`, 구축 기록)·테스트 공동 커버(`verifies`)·개념 공유(`usesConcept` ≥ 3, `proposal`)에서 후보를 내고 TIM 허용 칸·plane 단방향·수준·복합체 형제로 탈락시키며 앵커당 k ≤ 7이다. 채택은 사람이 링크 키와 `restored` 목록에 적는다([`p10-restored-link-marking`](../kb/dev/decision/p10-restored-link-marking/conclusion.md)) — 복원 비율은 `metrics`·`audit`가 `kb_lib.link_origins`로 센다. 구축 쪽: frontmatter 링크마다 `agt:Link` + 구축 기록 증거를 `chunk2kg`가 방출, `handoff`가 workset 뷰의 펼친 청크를 `sources`로 옮긴다 (`bazel run //tools:handoff -- --workset bazel-bin/kg/workset-<role>.md <청크>`). 없는 것: 동시 편집 이력 근거, `relatedTo` 후보의 복원 표시 | 3·8 |
| `propagate` / `revalidate` | [method §7 갱신](method.md#7-갱신) | **첫 형태 있음** — `propagate`는 `assume_check`의 전파 절(깨진 가정 → 직접 영향 집합 → 하류 suspect 후보). `revalidate` — `bazel run //tools:revalidate -- --base <rev>`(또는 git 없이 스냅숏 둘 — `--base-dir`·`--head-dir`·`--base-files`·`--head-files`, 2026-10-04 유저 답 Q38-c, 하류 의존자 열은 빈다): base 리비전 대비 본문 해시가 바뀐 청크와 그 링크 양 끝·`part_of` 형제·`rdeps` 하류를 재판정 대상 표로 낸다(종료 1 = 대상 있음). head만 바뀐 청크는 제외한다. **2026-09-26** — `## 재판정 대상 링크 개체` 절이 본문 해시가 바뀐 청크를 양 끝으로 갖는 `agt:Link`(head 그래프와 같은 IRI)를 낸다. **2026-10-01** — 요약과 머리에 **바뀐 끝이 결정 결론(`conclusion.md`)인 재판정 링크 수**를 함께 낸다: 결정의 본문과 구현이 어긋나는 현상(`agt:reasoningActionMismatch`, P16)의 판정 대상 행이고 0 이면 공허 합격이다. **2026-09-30** — 표에 `호출부` 열이 붙는다: 본문 해시가 바뀐 정의를 `uses`(`agt:usesDefinition`)로 가리키는 출발점의 수이고 **코드 호출부 파손의 상한**이다. 모듈 안 호출과 치역 경계(`defs/kb.bzl`의 `USES_TARGETS` — 2026-10-01 표본 쌍은 `kb_lib` 하나다) 안의 모듈 간 호출을 세므로, 경계 밖을 치역으로 하는 호출은 빠지고 실제 파손은 그 수보다 크다. `assume_check`는 링크의 `when`을 ODD 판정으로 평가해 거짓이면 `suspect`를 보고하고(종료 1) `kb_lib.SUSPECT_TRIGGERS`의 켜진 종류(`supersedes`)를 전파한다 — **상태는 저장하지 않는다**. 무효화 전파 8단계·규칙 카탈로그 전체는 없다 | 4 |
| `query` | [competency-questions](competency-questions.md) | **첫 형태 있음** — `bazel run //tools:query -- <CQ> [--labels] [--bind ?v=…]`가 역량 질문 질의 27개(`tools/cq-queries/*.rq`, 하나가 CQ 하나)를 그래프 union 위에서 돌린다. 결과는 라벨 목록이다. 뷰 `bazel build //kg:cq` → `bazel-bin/kg/cq.md`가 CQ마다 행 수와 상위 5행을 낸다(2026-09-14) | 3 |
| `impact` | [method §12 영향 분석](method.md#12-영향-분석) | **첫 형태 있음** — `bazel run //tools:impact -- <타깃>`: `rdeps`로 영향 항목 수·plane 분포·suspect가 될 링크 수·승인 필요 결정 수. 구조 근사이며 가정·무효화 전파는 그래프 질의 몫이다 | 3 |
| `project` / `weave` | [method §9 뷰](method.md#9-뷰) | **첫 형태 있음** — `weave`(2026-09-19): `bazel build //kb/dev:adr`(결정 복합체의 ADR 뷰) · `//kb/dev:requirements`(요구 색인 — EARS 패턴·정제 수·도달 수준) · `//kb/dev:changelog`(`supersedes` 이력) · `//kg:audit`(감사 보고서 — 검증 현황·최근 실행·**판정 주석**·가정·추적 매트릭스·검증 표시·링크 근거를 그래프 union과 관측 본문만으로, 8단계 첫 형태). 판정 주석 절이 **라운드(날짜)별 신규 주석 수**를 표로 낸다(2026-10-01, `round_section`) — 라운드 경계는 주석의 `prov:generatedAtTime` 날짜이고 `generated.by` 가 `process:judge` 인 판정 결과는 판정자의 응답 기록이라 집계에서 뺀다. 연속한 두 라운드의 신규 수가 줄지 않으면 다음 라운드를 열지 않는 것이 정지 규칙이고 현상 `agt:unknownStopCondition`(P15)의 관측 수단이다. **2026-10-04** — 라운드 기록(`vv_run --round`)이 있으면 경계를 날짜 대신 그 기록으로 자르고(`round_record_section`) 없으면 날짜 대리로 떨어진다(유저 답 Q39-c). 생성물마다 생성 시각과 질의를 적는다(`p12-documents-are-generated`). `communities` — `bazel build //kg:communities`: 결정론적 Louvain으로 복합체 후보(같은 plane·level, 2~9)와 `relatedTo` 링크 후보(plane·level을 넘음)를 제안, 판정은 사람이 한다([`p4-community-detection-proposes-composites`](../kb/dev/decision/p4-community-detection-proposes-composites/conclusion.md)). tangle은 없다 | 8 |
| `gen_skills` | [method](method.md) 정형 절차 | **첫 형태 있음**(2026-09-19) — `python3 tools/gen_skills.py --root .`가 도구 docstring과 `kb_lib.SKILLS`(도구·절 앵커·대표 명령)에서 `.claude/skills/<도구>/SKILL.md`를 생성한다. 트리에 두고 커밋하며 `//:skills_drift_test`가 재생성과 비교한다. BUILD와 같은 생성 트리 파일이며 손으로 고치면 다음 생성이 덮어쓴다 | 6 |
| `open_questions` | [method §9 뷰](method.md#9-뷰) | **첫 형태 있음**(2026-09-22) — `bazel build //kg:open` → `bazel-bin/kg/open.md`: 설계 공간(`--spaces` = `//space:design_space`)을 공간마다 한 행(제목·status·변수 from/kind·후보 state별 수·그 공간을 가리키는 슬롯)으로 내고, 공간을 가리키지 않는 선택 슬롯 `미확정:`을 head(`agt:bodySlot`)로 골라 질문·청크·plane/level·상세 문서로 낸다. 슬롯의 상세 값이 공간 IRI이면 그 공간의 행에 붙는다. **미결 목록의 유일한 자리다** — 상세 다섯 절은 설계 공간 청크에 있고(Q54-a) 손 색인 `docs/open-questions.md`의 목록을 대체했다(2026-10-06, 지시 0095; [`p4-three-empty-values`](../kb/dev/decision/p4-three-empty-values/conclusion.md)) | 6 |
| `space2kg` / `choices` | [method §5 후보 관리](method.md#5-후보-관리) | **첫 형태 있음**(2026-09-22) — `space/*-space.md`(변수 하나 = 파일 하나)를 A-Box `//space:design_space`로 올리고 체크박스 뷰 `//space:choices`를 낸다. 후보는 `kb_chunk` 타깃이 아니므로 **구조적으로 `deps`가 되지 못한다**. 근거 없는 배제와 확정 후보 수를 게이트 `space`가 거부한다 — `r-011`의 실물이다. 없는 것: CEL 평가기(`when`·양립 제약이 문자열) | 5 |
| `tokens` | [rules §1 chunk](rules.md#1-chunk--자립적-최소-지식-단위) | **있음**(2026-10-01) — `bazel run //tools:tokens -- [청크…] [--out <경로>]`: 청크 본문의 토큰 수를 고정된 공개 토크나이저로 세어 plane별 분포(최소·분위수·중앙·최대·줄당 토큰)·**42의 배수마다 초과 청크 수와 비율**(42×1 … 42×20)·컨텍스트 예산의 환산·상위 20 청크를 낸다. 청크의 단위가 줄이 아니라 토큰이라는 유저 결정(2026-10-01)의 실측 수단이고 상한의 숫자(1,092 = 42×26 · 2,856 = 42×68)를 이 분포가 정했다. 계수기는 `tiktoken 0.12.0` + 어휘 `o200k_base`이며 어휘 파일은 `MODULE.bazel`의 `http_file(tiktoken_o200k_base)`가 sha256으로 고정해 네트워크 없이 runfiles에서 읽는다 — 해시가 다르면 로더가 거부하고 ODD 조건 `id:cond-tokenizer-lock`이 이탈한다. 생성 시각을 적지 않아 같은 입력에서 같은 바이트가 나온다. 본문을 떼는 판정처는 `kb_lib.body_text` 하나라 게이트·방출·이 뷰가 같은 문자열을 센다. **게이트가 아니라 뷰다** — 상한의 강제는 `chunk_lint`(`chunk`)와 shape(`token-budget`)의 몫이고 이 도구는 분할 대상을 고르는 자리다 | 1 |
| `metrics` | [methodology 완료 판정](method.md#완료-판정) | **첫 형태 있음** — `bazel build //kg:metrics` → `bazel-bin/kg/metrics.md`: 청크 수·고아율·크기 분포·링크 밀도·CQ19·CQ20·신뢰 등급. **연결 성분과 CQ20 후방 추적은 관측(`memory` plane) 제외다**(유저 승인 2026-09-23) — 관측은 실행의 부산물이고 append-only라 사후에 링크를 이을 길이 없으며 추적 매트릭스에 `memory` 칸이 0개다. 관측을 세면 실행할수록 지표가 나빠지는데 그것은 고립이 아니라 기록의 축적이다. 없는 것은 suspect 비율·누락률·라벨 대표성이다. 분할 조각의 `prov:specializationOf` 는 그 두 지표에서 연결로 센다(2026-10-01, [`p10-split-keeps-work-identity`](../kb/dev/decision/p10-split-keeps-work-identity/conclusion.md)) — 조각은 링크를 승계 청크에 두므로 원 청크를 거쳐 요구에 닿는다. 성분이 1보다 크면 「주 성분 밖 청크」 절이 성분마다 라벨·plane·경로를 낸다. 2026-10-04 유저 결정으로 건너뜀을 결정 복합체 몫·V&V 사다리 몫(V&V KB 안의 합격 기준 → 검증 목표 `refines`, Q30-b · 검증기 → 합격 기준 `refines`, Q41-a)·남는 몫으로 가르고, 5단계 절(결정 완결률·사람 확인 요구를 뺀 전방 추적)과 7단계 행(독립성·음성 고정물의 변이 검출률)을 더했다 | 1 |

`metrics`(1·2단계 대리 포함)·`workset`·`odd_check`의 첫 형태가 생겼으므로 문서는 수치를 적지 않고 생성물을 인용한다 (d-0075). 문서에 남아
있는 수치는 스냅샷 표기가 붙어야 한다.

## development 층 — 개발 KB의 도구 (노트 Part VII, 전부 미구현)

| 도구 | 하는 일 | 규칙·절차 |
|---|---|---|
| `gate` | 전이 게이트 4종 — 기여 명시 / 범위·제약 / 표본 근거 / 기준 바인딩 (6.8) | [rules development](rules.md#7-development-규칙--개발-kb-노트-7277) |
| `space_check` | `-space` 호 일관성 · ODD 경계 · `when` 평가 · 증거 기록 규칙 · 확정 제안 (9.10, 9.11) | [method §5](method.md#5-후보-관리) |
| `feedback` | `-space` → 체크박스 파일 · 되읽기 → 확정 (13.5) | [p9-candidate-storage](../kb/dev/decision/p9-candidate-storage/conclusion.md) |
| `contract_check` | 계약 선행 · 타입 · 사후조건 CEL 실행 가능성 (7.5) | [p7-contract-first](../kb/dev/decision/p7-contract-first/conclusion.md) |
| `schema_compat` | 하위 호환 판정, 비호환이면 새 IRI + `supersedes` (7.6) | [p7-schema-derivation](../kb/dev/decision/p7-schema-derivation/conclusion.md) |
| `adr` | 결정 복합체 뷰 (7.4) — **있음**: `weave --kind adr`, `//kb/dev:adr` (2026-09-19) | [p7-alternatives-mandatory](../kb/dev/decision/p7-alternatives-mandatory/conclusion.md) |
| `tangle` | 구현 청크 → 코드 파일 (4.6) | [method §9](method.md#9-뷰) |
| `dev_metrics` | 전방 추적 커버리지 · 후방 추적 커버리지 · 결정 완결률 · `-space` 체류 · 계약 선행률 · 대안 기록률 (7.8) | [p7-dev-kb-outputs-and-metrics](../kb/dev/decision/p7-dev-kb-outputs-and-metrics/conclusion.md) |

## V&V 층 — V&V KB의 도구 (노트 Part VIII, 도입 7단계, `run`·`case_gen` 첫 형태 외 미구현)

| 도구 | 하는 일 | 절 |
|---|---|---|
| `goal_derive` | 요구 → 검증 목표 후보 | 8.19 |
| `scenario_lint` | 변수가 ODD 속성인가 · 부류 참조 · 배제 자극 존재 · 자극 ≠ 기준 | 8.22 |
| `case_gen` | **첫 형태 있음** — `tools/case_gen.py`(2026-10-04, 유저 답 Q27-a): logical 시나리오 자극 청크의 `yaml` 펜스 하나(`keep` · `cover` · `seed` · `case`)에서 concrete 케이스 청크(`kb/vv/case/*.md` 꼴)를 결정론적으로 낸다. 규칙은 다섯(`sampling:equivalence`·`boundary`·`pairwise`·`factor`·`observed`)이고 규칙·seed·값·부류가 `**표본 근거**`에, 시나리오가 `derivesFrom`에 남는다. 생성 케이스는 `vv_run`의 파서로 되읽어 실행기가 읽는 꼴인지 본다. 출력은 `--out` 디렉토리이고 저장소 반영은 vnv가 한다. 드리프트 가드 `//:case_drift_test`는 대상 0으로 서 있다 | 8.23 |
| `verifier_bind` | 기준 바인딩 검사. 기준 없는 `verifies` 거부 | 8.11 |
| `env_assign` | 결함 요인 → 환경 단계, 재현성 조건 | 8.10, 8.12 |
| `run` | **첫 형태 있음** — `vv_run`(2026-09-19): 리비전·환경 버전 기록, 실행 기록 append(`kb/vv/run/`). **기대 문구 대조 있음**(2026-09-23, `contains`) · **환경 격리 상시 판정 있음**(`//tools:vv_run_env_test`) · seed 고정은 없다 | 8.15 |
| `judge` | **첫 형태 있음, 외부 서비스 없이 개정**(2026-09-30) — `bazel run //tools:judge -- --question <질문 id> --responses <json> [--responses <json> …] [--decoys <json>] [--record] [--into <디렉토리>] <청크 파일…>`: **게이트 밖 도구다.** 판정자는 외부 서비스가 아니라 **세션 판정자**(다른 세션·다른 역할의 에이전트)다 — `call_service`·`urllib` 호출과 자격 환경 변수(`AKB_JUDGE_*`)를 뺐다(유저 답 2026-09-30). `--fixture`(오프라인 고정물)를 정식 입력 `--responses`로 승격했다 — 세션 판정자가 낸 `{judge: <역할/모델 또는 세션 식별자>, responses: [{question, fingerprint, value, confidence}]}`를 받아 같은 형 검사(noul·choice·score, choice ≤ 255)·라우팅·로그·주석 생성을 돈다. 질문·척도·임계는 프로파일(`kb/ontology/profile/development/judge-question-ontology.ttl`·`judge-question-set-ontology.ttl`·`judge-threshold-ontology.ttl`·`judge-calibration-ontology.ttl` + `kb/ontology/shapes/judge-question-shapes.ttl`)에서 읽는다. 확신도는 자기 보고라 **단독 응답으로는 자동 적용이 없다** — `--responses`를 둘 이상(판정자마다 하나) 주면 같은 (질문·입력 지문)의 값 일치 여부를 계산해 로그의 `일치` 열(일치·불일치·해당 없음)에 낸다. 일치율 임계와 자동 적용은 결정 [`p8-judge-session-agreement`](../kb/dev/decision/p8-judge-session-agreement/conclusion.md)가 정확도·판별력 재측정 뒤 정한다 — 지금은 전부 사람 확인 큐다. **대조 지문은 항상 세션 판정자가 실제로 본 라벨+본문**(`kb_lib.label_fingerprint`)이지 청크 파일 바이트가 아니다(2026-09-30 vnv 결함 보고 ① — 파일 바이트로 대조하면 판정자의 응답이 전부 안 잡힌다) — 파일 바이트 지문은 로그의 `입력 지문` 열에 추적용으로만 남는다. `--decoys <json>`(`label_sample.py`가 낸 key.json — 실표본·미끼를 다 담는다)을 주면 그 항목의 라벨+본문으로 실표본까지 스스로 대조하고, 미끼 검출률(**검출 = 척도의 최고값(적합)이 아니다**, orchestrator 결정 2026-09-30 — 판별력은 "미끼를 적합으로 통과시키지 않는가")을 보고 요약에 낸다. 결과 주석의 파일명은 `<파트 디렉토리>-<파일 stem>-<판정자>`다(2026-09-30 결함 보고 ② — 결정 세 청크는 stem이 conclusion·rationale·alternatives뿐이라 그것만으로는 부딪힌다). 판정 로그(`kb/vv/run/judge-<시각>.md`, memory plane, append-only — 필수 필드 질문 id·값·확신도·**판정자 식별자**·입력 지문(sha256)·시각, 읽기 열 대상·처리·일치, `관측` 문장은 응답 파일의 **basename만** 싣는다)와 결과 주석(`kb/vv/verdict/`, 논평 형식 — `본문:` 은 판정자가 쓰지 못해 `해당 없음`)을 낸다. 선택 집합 255 초과는 `FAIL [judge]` 로 거부하며 점수 → 선택 2단계를 안내한다. 없는 것: 3지표(정확도·판별력·캘리브레이션) 측정과 head `verified` 반영, 일치율 임계 자체(`p8-judge-session-agreement`) | 8.14, 2.12 |
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

**지식 항목은 타깃이다** (2026-09-11, [`bazel-dependency-review`](../harness/user/archive/legacy/bazel-dependency-review.md) B + 연결성).
`defs/kb.bzl`의 규칙 `kb_chunk`(청크 = 타깃)·`kb_decision`(결정 복합체 = 타깃, 대안 필수)·`kb_composite`(결정 밖 복합체 = 타깃, 부분 2~9 동질)·
`kb_ontology_module`(모듈 = 타깃, `owl:imports` = deps)이 `ChunkInfo`·`OntologyModuleInfo` provider를
내보낸다. frontmatter의 `refines`·`serves`·`supersedes`·`verifies`가 **deps**다. BUILD는
`tools/gen_build.py`가 frontmatter에서 **생성**하고 커밋한다. `//:build_drift_test`가 원본과 비교한다
(d-0159). Bazel이 맡는 것은 링크의 **구조**다. 끊긴 링크 = 로드 에러, 방향 = 분석 시점 `fail()` +
`//kb:*_readers` 가시성, 파급 = `bazel query rdeps`, 토큰 상한·frontmatter = 검증 액션(`bazel build`만으로)이다.
의미, 곧 SHACL·통제 어휘·상태는 그대로 union 게이트다(d-0157). 음성 시험은 `//defs/tests`에 있다.
skylib analysistest를 쓴다.

```bash
bazel run //tools:impact -- //kb/dev/requirement:r-008-descend-to-executable   # 영향 집합 = rdeps (12.6절 네 수치)
bazel build //kg:workset --//kb:role=developer --//kb:anchor="두 KB" --//kb:levels=concrete   # 작업 집합 뷰, 선택자는 플래그
bazel build //kb/dev/decision:all                                                       # 검증 액션 = 토큰 상한·frontmatter
bazel run //tools:revalidate -- --base HEAD~1                                            # 본문 해시 변경 → 재판정 대상 링크·항목
bazel run //tools:extract -- tools/kb_lib.py                                             # 소스를 고쳤으면 코드 청크 재추출
tools/gen_build.py                                                                       # frontmatter 를 고쳤으면 BUILD 재생성
```

```
bazel test //...  (게이트 전체 — test_suite 없음, 패키지의 test 타깃 전부)
├── //:build_drift_test            생성 BUILD = frontmatter (드리프트 가드)
├── //defs/tests:*                 음성 시험 5 — plane 단방향·수준 허용표·supersedes plane·verifies 주어·결정 수준
├── //:naming_test                 TTL 접미사 규약
├── //harness:channel_lint_test    채널 규약 — 메시지·질문지 어휘 · 단일 작성자 · task↔result 쌍 · hci 반영 흔적 · waivers
├── //harness:scripts_test         채널 스크립트 동작 — send → inbox → mark 흐름과 거부 규칙 (게이트 id 없음, 호스트 bash)
├── //:doccheck_test               문서 현행성 — 깨진 링크·앵커·백틱 경로 (루트 md + docs/** + 하네스 문서, 채널 메시지·질문지 제외)
├── //space:design_space           설계 공간 A-Box — 열린 변수와 후보 링크 (게이트 `space`)
├── //space:choices                후보 체크박스 뷰 (생성 뷰, 게이트 아님)
├── //kg:open                      미결 집계 — 청크의 `미확정:` 슬롯 (생성 뷰, 게이트 아님)
├── //:gendoc_test                 생성 문서 형태 — 머리 블록·제목 계층·표·목차·링크·비율 표기 (생성 뷰 = `defs/kb.bzl` 의 `VIEWS` + SKILL.md)
├── //:skills_drift_test           생성 skill(.claude/skills) = 도구 docstring·kb_lib.SKILLS (드리프트 가드)
├── //:extract_drift_test          생성 코드 청크(kb/dev/artifact/**) + 등록부 = 소스 (드리프트 가드, 게이트 `extract-drift`).
│                                  `//:extract_drift_<이름>` 의 test_suite — 판정 단위가 소스 하나다(목록은 `defs/kb.bzl` 의
│                                  `EXTRACTED_SOURCES`·`EXTRACTED_QUERY_DIRS`)
├── //:case_drift_test             생성 케이스(kb/vv/case) = logical 시나리오의 keep·cover (드리프트 가드, 게이트 `case-drift`, 대상 0)
├── //kb:consistency_build_test    정합성 보고 생성 (build_test — 보고는 게이트 실행마다)
├── //chunks:lint_test             `chunks/` 항목 토큰 상한 · 산문 문체(prose) · 첨가·빈 값·목록
├── //kb/dev:lint_test             개발 KB 청크 토큰 상한 · 산문 문체(prose) · 첨가·빈 값·목록
├── //kb/vv:lint_test              V&V KB 청크 토큰 상한 · 산문 문체 · 첨가·빈 값·목록 (2026-09-19)
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
| 라벨이 본문을 대표한다 | 판정 불가 — 게이트로 만들지 않는다 | `STYLEGUIDE.md` §4. 보고 기구는 **세션 판정자**(외부 서비스가 아니다, 2026-09-30) — 질문 `agt:labelRepresentsBody`(score)를 `tools/judge.py --responses`로 묻는다(2026-09-29·2026-09-30) |
| 한 chunk는 한 주제 | 판정 불가. 토큰 상한과 분할 신호가 대리 지표 | `STYLEGUIDE.md` §0. 보고 기구는 **세션 판정자** — 질문 `agt:bodyHasOneClaim`(noul)을 `tools/judge.py --responses`로 묻는다(2026-09-29·2026-09-30) |
| 문서의 수치가 생성물의 수치와 같다 | 이름의 짝짓기가 사람의 대조다 — 문서가 수치 옆에 생성 타깃의 이름을 적는 규약이 서면 게이트로 올린다 | V&V 기준 [`document-table-matches-generated`](../kb/vv/criteria/document-table-matches-generated.md). 보고 기구는 `bazel run //tools:doccheck -- --report`(2026-10-01) — 진입점 문서 넷(위치 인자를 주면 그 목록으로 바뀐다, 2026-10-01 vnv 요청 — 이 모드만 루트 밖 절대 경로를 허용해 `vv_run` 케이스의 워크스페이스 밖 자극도 대조 대상이 될 수 있다) × 이름 열넷을 생성물(`//kg:metrics`·`//kg:audit`·`//kg:link_candidates`)과 쌍으로 대조해 어긋난 쌍을 센다. 판정이 아니라 보고이므로 종료 0 이고, 이름과 값이 산문으로 떨어져 있으면 쌍이 서지 않는다. 현상 `agt:documentLag`(P18)의 관측 수단이다 |

카탈로그 정합성 검사가 없어 ODD의 동시 에이전트 한도와 카탈로그의 합이 한동안 어긋난 채
지나간 적이 있다. 규약만으로는 지켜지지 않는다는 증거다.

## 도구 작성 규칙

- 실패 시 비영 종료 + `FAIL [검사명]` 접두사 + 근거 인용을 낸다. 메시지가 곧 수정 안내다.
- 새 검사는 독립 함수 `check_*() -> list[str]`로 추가하고 `main`에서 합류한다.
- 규약 상수(접미사·네임스페이스)의 단일 정의처는 `tools/kb_lib.py`다.
- 생성기는 검사기다. 생성 실패가 곧 게이트 실패이고, 생성물은 소스 트리에 두지 않는다.
- 검사를 약화하는 변경(삭제·예외 추가)은 유저 승인 사항이다.
