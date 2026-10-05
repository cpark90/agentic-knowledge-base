---
from: hci
status: approved
targets: [inquiries/bazel_suggestion.md, ../../kb/ontology/BUILD.bazel, ../../kg/BUILD.bazel, ../../defs/knowledge.bzl, ../tools.md]
---

# 검토 — 의존성을 Bazel로 관리하기

원문: `inquiries/bazel_suggestion.md` — *"현재는 온톨로지와 knowledge graph 둘 다
파일에 작성된 내용들만으로 연결이 되어 있음. bazel을 활용해서 의존성을 관리해줘."*

## 질문

지식 항목 사이의 의존(온톨로지 `owl:imports`, 청크의 `refines`/`part_of`/`sources`,
데이터→어휘 사용)을 **Bazel 타깃 의존으로 미러링**할 것인가, 한다면 어느 굵기로
할 것인가. 지금 Bazel은 이 의존을 전혀 모른다 — 모듈은 평평한 `filegroup`이고
게이트는 전체 union을 읽는다.

## 이미 정해진 것 — 이 제안을 당기는 결정과 미는 결정

당기는 쪽:

- **재판정 경계 = 커밋, Bazel 캐시가 그 실행기**다 (`docs/input.md`) — 의존이
  타깃에 있어야 "바뀐 입력의 게이트만" 재실행이 지식 단위로 내려간다. 지금의
  캐시 경계는 "지식 전체"라 청크 하나가 바뀌어도 union 게이트 전체가 다시 돈다.
- **툴 표면이 배정을 따라야 한다** (p5-tool-surface) — 타깃 의존이 생기면 Bazel
  `visibility`로 스코프(역할별 read 경계)를 빌드 수준에서 강제할 수 있다.
- **영향 분석** (p11-change-impact-analysis) — `bazel query rdeps`가 파일 수준
  근사를 공짜로 준다.

미는 쪽:

- **union을 검증한다** (d-0157, harness 승격분) — 어휘 폐쇄·SHACL 불변식은 union
  위에서만 성립한다. 게이트를 모듈별로 쪼개면 **좁은 게이트의 초록이 증거가 아닌
  상태**가 된다. 즉 어떤 안이든 union 게이트는 남아야 한다.
- **생성물 드리프트 가드** (d-0159) — 목록을 손으로 복제하다 부분 union이 검증을
  통과한 실제 사건이 있었다. 의존의 원본은 이미 그래프 안(`owl:imports`·frontmatter)에
  있으므로, BUILD의 deps를 **손으로 쓰는 순간 같은 드리프트**가 시작된다. 어떤
  안이든 BUILD/deps는 내용에서 **생성**되어야 하고 드리프트 검사가 붙어야 한다.
- **뷰는 질의 결과다** (p4-projection-as-query) — 의미적 의존 판정(무효화 전파,
  suspect 계산)은 그래프 질의의 일이다. Bazel 의존은 그 근사이지 대체가 아니다.

## 현재 상태 — 실측

- 의존이 사는 곳: `project-ontology.ttl`의 `owl:imports` 11건, 청크 frontmatter의
  `refines`/`supersedes`/`part_of`/`sources`(전체 ~750 청크), 데이터의 `agt:` 어휘 사용.
- Bazel이 아는 것: 모듈 = `filegroup(glob)` 11개, 게이트 7개가 각각 union을 소비.
  타깃 간 의존은 `//kg` 생성물 체인뿐이다.
- 전체 게이트 소요: 콜드 수십 초, 캐시 후 수 초. **분할 캐시의 이득이 아직 통증으로
  측정된 적 없다** — 1단계 통과 조건과 같은 상황("먼저 잰다", 유저 결정 Q7).

## 답이 가르는 것

- **굵기**: 청크 단위 타깃(~750개)이면 증분이 최대지만 BUILD 생성기·분석 오버헤드가
  크다. 모듈(디렉토리) 단위면 생성기가 단순하고 오버헤드가 작지만 증분은 모듈 굵기다.
- **판정의 위치**: Bazel deps를 판정(게이트 분할)에 쓸 것인가, 조회(query·visibility·
  캐시)에만 쓸 것인가. 전자는 d-0157과 정면 긴장이다.
- **이중 관리**: 의존의 원본이 그래프인 채 BUILD가 생성물이 되는가(안전), BUILD가
  제2의 원본이 되는가(드리프트).

인수: orchestrator 2026-09-11 — 청크·도구·문서 변경을 검토했다(요구 7건 전문, 결정 표본, 온톨로지 폐기 표기, 게이트 구조 검사). endorse 로 verified 부여.

## 선택지

| 안 | 내용 | 얻는 것 | 비용·위험 |
|---|---|---|---|
| A. 전면 미러링 | 파일=타깃, 내용 의존=deps. BUILD 전부 생성 | 최대 증분, 청크 수준 rdeps, visibility 강제 | 생성기+드리프트 가드 필수, ~750 타깃 분석 비용, union 게이트와 이중 구조 |
| **B. 모듈 수준 미러링 (권고)** | `owl:imports`→모듈 deps 생성 + 모듈별 국소 게이트(구문·라벨·정의 경계), **union 게이트 유지**. 청크 의존은 생성물 `deps` 그래프로 노출해 query만 | 모듈 굵기 증분, 국소 실패의 빠른 신호, d-0157 보존 | 생성기 소형이지만 필요, 국소 초록 과신 위험(문서화로 완화) |
| C. 현상 유지 + 가드 | Bazel은 실행기·캐시로만. `modules` filegroup ↔ 디렉토리 일치 생성 검사만 추가 | 비용 0에 가까움 | 제안의 이득(증분·query) 없음 |

**권고: B**, 단 착수 전에 metrics에 게이트 소요(콜드/캐시) 측정을 추가해 "분할이
줄여줄 시간"을 먼저 잰다 — 수 초라면 C로 충분하고, 프로파일·V&V KB가 채워져
union이 커질 때 B로 간다. 어느 안이든 **deps 원본은 그래프, BUILD는 생성물**이
전제다(d-0159).

## 사용자 피드백
B, 추가적으로 의존성 뿐만이 아닌 연결성도 tightly coupled되게 bazel로 관리

## 재검토 (유저 답 수신 후) — B + 연결성까지 Bazel로

유저 답: **B**, 추가로 **의존성뿐 아니라 연결성(링크)도 Bazel로 긴밀 결합**.

이 답은 B의 "청크 의존은 query만"을 뒤집는다 — 링크는 청크 사이의 것이므로, 링크를
Bazel이 알려면 **청크(또는 결정 디렉토리)가 타깃**이어야 한다. 결론부터: 가능하고,
B의 원칙(deps 원본은 그래프·BUILD는 생성물·union 게이트 유지)을 지키면서 할 수 있다.

### "긴밀 결합"이 실제로 뜻하는 것 — Bazel이 맡을 수 있는 네 가지

| 연결의 성질 | 지금 (그래프만) | Bazel 결합 후 |
|---|---|---|
| 링크 끝점의 존재 | 게이트의 dangling 검사(테스트 시점) | **라벨 해석 실패 = 로드 시점 빌드 에러** — 끊긴 링크는 빌드가 안 된다 |
| 변경의 파급 | 그래프 역방향 질의(도구 미구현) | `bazel query rdeps(//..., X)` = suspect 후보 집합. 캐시 무효화가 곧 재판정 대상 |
| 방향 제약 | SHACL·verify 질의 | **`visibility`**: `kb/vv`→`kb/dev`만 허용(verifies 주어는 V&V 청크뿐), plane 단방향(requirement←decision←…)도 패키지 가시성으로 |
| head 그래프 생성 | `chunk2kg`가 전체를 한 번에 | 청크 타깃마다 head TTL 액션 → 바뀐 청크만 재생성, `//kg:chunks_kg`는 병합 |

Bazel이 **못 맡는 것**은 그대로 그래프의 일이다 — SHACL·어휘 폐쇄·수준 허용표(의미 판정),
`suspect`/`invalidated` 상태 전이, 링크의 판정 근거·신뢰도. 즉 링크의 **구조**(끝점·방향·
파급)는 Bazel, **의미**는 그래프. d-0157(union 검증)은 그대로 산다.

### 타깃 굵기 — 파일이 아니라 "항목"

- **요구**: 파일 하나 = 타깃 하나 (`//kb/dev/requirement:r-008`).
- **결정**: 디렉토리(복합체) 하나 = 타깃 하나 (`//kb/dev/decision:p6-refinement-ladder`),
  부분 셋은 `srcs`. `refines`·`supersedes`는 deps, `part_of`는 타깃 안에서 소화.
- **옛 결정** `chunks/decision`: 파일 = 타깃. deprecated라도 `supersedes`의 끝점이므로 필요.
- **온톨로지 모듈**: `owl:imports` → 모듈 deps (B 그대로).
- **본문 인용**(`cites`, extract_refs가 뽑는 것): 1차에서는 **deps에 넣지 않는다** —
  frontmatter 링크(의미 의존·시간축)만. 인용까지 넣으면 거의 모든 청크가 서로 얽혀
  rdeps가 전체가 된다. 필요하면 2차에서 별도 속성(`cites =`)으로.

굵기가 "항목"이라 타깃 수는 ~400(요구 33 + 결정 182 + 옛 153 + 모듈 11 + shape)이며
Bazel에 부담이 아니다.

### 이중 관리를 막는 방법 — 생성 + 드리프트 가드 (d-0159)

- `tools/gen_build.py`: frontmatter·`owl:imports`를 읽어 패키지별 `BUILD.bazel`을
  **생성**한다. IRI→라벨 사상은 파일 위치에서 결정적으로 나온다(uuid IRI는 불투명하지만
  파일이 유일하므로). 생성된 BUILD는 **커밋한다** — `bazel query`가 생성기 없이도 돌아야
  하고, 리뷰에서 diff가 보여야 한다.
- `//:build_drift_test`: 생성기를 다시 돌려 커밋본과 비교. 어긋나면 FAIL — frontmatter를
  고치고 BUILD를 안 돌린 경우를 잡는다. **frontmatter가 원본, BUILD는 뷰**라는 순서가
  이 테스트로 강제된다.

### 실행 순서 (제안)

| 순서 | 무엇 | 게이트 |
|---|---|---|
| 1 | `kb_chunk`·`kb_decision`·`kb_ontology_module` 규칙/매크로 (`defs/knowledge.bzl`) — 지금은 filegroup 위 얇은 층 | 기존 7 게이트 PASS 유지 |
| 2 | `gen_build.py` + 생성 BUILD 커밋 + `build_drift_test` | 드리프트 음성 시험 |
| 3 | 링크 → deps (refines·supersedes·verifies·모듈 imports). 끊긴 링크가 빌드 에러가 되는지 음성 시험 | dangling 게이트와 결과 일치 확인 |
| 4 | visibility 정책 — `kb/vv`→`kb/dev` 단방향, plane 단방향 | 역방향 의존을 넣어 빌드 실패 확인 |
| 5 | 청크별 head 생성 액션으로 `chunk2kg` 분해, `//kg:chunks_kg`는 병합 | 생성 TTL이 기존과 바이트 동일(정규화 후) |
| 6 | `impact` 도구를 `bazel query rdeps` 위에 얹기 (p11-change-impact-analysis의 1단계) | — |

### 확인이 필요한 것 (셋)

1. **옛 `chunks/decision` 153건도 타깃으로 올리는가** — 권고 예(supersedes 끝점이라 필요, 비용 미미).
2. **본문 인용(`cites`)을 1차 deps에서 제외**하는 데 동의하는가 — 위 이유.
3. **plane 단방향을 visibility로 강제**하는가 — 지금은 결정→요구만 있어 실효가 없지만,
   정책은 지금 넣어야 나중에 예외가 안 생긴다. 권고 예.

## 사용자 피드백
전부 예, 추가적으로 bazel의 rules 기능 활용방안도 조사해서 추가해줘.

## 재검토 2 — 확인 셋 전부 예 + Bazel rules 기능 활용 조사

유저 답: 확인 1·2·3 **전부 예**(옛 결정도 타깃, `cites`는 1차 제외, plane 단방향 visibility).
추가 요청: **Bazel의 rules 기능 활용 방안 조사.**

### 현재 위치

`defs/knowledge.bzl`의 매크로 10개는 전부 `native.genrule`·`py_test` 위의 얇은 포장이다 —
`rule()`·`provider()`·`aspect()`가 하나도 없다. 즉 Bazel은 지금 "파일 묶음을 스크립트에
넘기는 실행기"이고, 타깃이 **무엇인지**(plane·level·IRI·링크)는 Bazel 밖에 있다. rules
기능을 쓴다는 것은 그 정보를 **분석 시점의 타입 있는 데이터(provider)**로 올린다는 뜻이다.

### 기능별 활용 방안 (Bazel 9.2 기준)

| 기능 | 무엇인가 | 이 체계에서의 쓰임 | 단계 |
|---|---|---|---|
| **`provider()`** | 타깃이 의존자에게 내보내는 타입 있는 구조체 | `ChunkInfo(iri, plane, level, status, content_hash, links)` · `CompositeInfo(parts)` · `OntologyModuleInfo(iri, imports)` · `KgInfo(ttl 조각 depset)`. 링크의 끝점이 "파일"이 아니라 **plane·level을 아는 타깃**이 된다 | 1 |
| **`rule()` + `attr.label_list(providers=[...])`** | 속성이 특정 provider를 요구 | `kb_decision(refines=)`는 `ChunkInfo`이면서 plane=requirement인 것만 받는다 — **수준 허용표·plane 단방향·verifies 주어 제약을 분석 시점 `fail()`로** 강제. SHACL보다 앞선, 파일을 읽지 않는 구조 판정 | 1·4 |
| **`depset`** | 전이 폐포를 중복 없이 병합 | `//kg:chunks_kg` = 청크별 head TTL 조각의 depset 병합 → 바뀐 청크만 재생성. `refines` 전이 폐포도 depset — CQ19/20(전방·후방 추적 커버리지)이 분석 시점 계산 | 5 |
| **validation actions** (`OutputGroupInfo(_validation=)`) | 빌드의 부수 검사. 실패하면 산출물이 있어도 빌드 FAIL | 청크 lint·frontmatter 검사·42줄 상한을 **`bazel build`만으로** 강제 — "편집은 게이트가 판정한다"가 test 단계가 아니라 build 단계로 당겨진다 | 1 |
| **`rule(test=True)`** | 테스트를 규칙으로 | 게이트를 `py_test` 포장이 아니라 provider를 읽는 테스트 규칙으로. 청크별 국소 게이트(증분) + union 게이트(d-0157) 두 층 | 3 |
| **`aspect()`** | 규칙을 고치지 않고 의존 그래프를 따라 계산을 얹음 | `labels`/`workset`/`metrics`를 **aspect**로 — `bazel build //kb/dev/... --aspects //defs:kb.bzl%workset_aspect --define role=developer`. 규칙 하나에 뷰를 여러 개 붙일 수 있고 뷰가 저장되지 않는다(4.6절) | 5·6 |
| **symbolic macro** + `finalizer` (Bazel 8+) | 패키지의 모든 타깃을 본 뒤 도는 매크로 | 패키지별 집계 타깃(`:all_decisions`, 패키지 union 게이트)을 **자동 생성** — 생성 BUILD에 목록을 적지 않아도 된다. 속성 타입·visibility 상속도 얻는다 | 2 |
| **`visibility` / `package_group`** | 의존 허용 범위 | `package_group(vv_editors, packages=["//kb/vv/..."])`; plane별 기본 visibility를 생성기가 부여. 역방향 의존 = 분석 에러 | 4 |
| **`analysistest`** (skylib) | "이 타깃은 분석에 실패해야 한다"를 테스트로 | 3·4단계의 음성 시험(끊긴 링크·역방향 verifies·수준 허용표 위반)을 **영구 테스트**로 남긴다 | 3·4 |
| **build settings / transition** | 명령줄 플래그를 Starlark로 정의, 의존에 따라 구성 전환 | `--//kb:role=developer`(작업 집합 시점), `--//kb:reason`(OWL-RL 켜기), `--//kb:budget=200`. `select()`로 게이트 강도 전환 | 6 |
| **`cquery --output=starlark`** | provider 필드를 그대로 출력 | 라벨 목록·IRI 표를 파이썬 없이 — `bazel cquery 'kind(kb_chunk, //kb/dev/...)' --output=starlark --starlark:expr='providers(target)["ChunkInfo"].iri'` | 6 |
| **`query rdeps/somepath/allpaths --output=graph`** | 의존 그래프 질의·시각화 | `impact` 1단계, 추적 매트릭스 초안(plane×plane 격자는 `--output=graph`를 plane으로 접으면 됨) | 6 |
| **output groups** | 한 타깃의 여러 산출 묶음 | `bazel build //kg:kg --output_groups=metrics,index,taxonomy` — 뷰가 별도 genrule이 아니라 그래프 타깃의 출력 그룹 | 5 |
| **module extension / repo rule** | 로딩 전에 파일을 읽어 외부 저장소를 합성 | **(a)** 외부 표준 어휘(PROV-O·SKOS·BFO)를 해시 고정으로 가져오기 — `upper` 정렬의 입력. **(b)** frontmatter를 읽어 링크 타깃을 `@kb_links//...`로 합성 — 생성 BUILD를 커밋하지 않는 대안(`repository_ctx.watch`로 파일 변경 추적) | (a) 후속, (b) 대안 |
| toolchain / exec group | 도구 해석을 규칙에서 분리 | `kb_toolchain`(rdflib·pyshacl 버전)을 규칙이 요구 — 매크로마다 requirement 나열 제거. 이득 소폭 | 보류 |

### 생성 BUILD 커밋 vs 모듈 확장 합성 — 하나만 고른다

| | 생성 BUILD + 드리프트 가드 (재검토 1 제안) | 모듈 확장이 `@kb_links` 합성 |
|---|---|---|
| 원본 | frontmatter. BUILD는 커밋된 뷰 | frontmatter. BUILD는 캐시에만 |
| 드리프트 | 테스트가 잡음 (커밋 잊음 가능) | 구조적으로 없음 |
| 리뷰 가시성 | PR diff에 링크 변화가 보임 | 안 보임 |
| 라벨 | `//kb/dev/decision:p6-...` | `@kb_links//kb/dev/decision:p6-...` — 주 저장소와 이원화 |
| query·visibility | 그대로 | 저장소 경계 넘는 visibility 필요 |

**권고: 생성 BUILD + 드리프트 가드로 시작**한다 — 링크 변화가 diff에 보이는 것이
"연결의 구축(편집 부산물)" 원칙과 맞고, 라벨이 한 저장소 안에 있어야 visibility가
단순하다. 모듈 확장은 청크 수가 수천이 되어 BUILD diff가 소음이 될 때 재검토.

### 실행 순서 (rules 반영판)

| 순서 | 무엇 | 검증 |
|---|---|---|
| 1 | `provider()` 3종 + `kb_chunk`·`kb_decision`·`kb_ontology_module` **규칙**(매크로 아님). 규칙 impl에서 plane·level·방향 검사 → `fail()`. 청크 lint를 validation action으로 | 기존 7 게이트 PASS + `bazel build`만으로 lint 실패 재현 |
| 2 | `gen_build.py` → 패키지 BUILD 생성(symbolic macro로 목록 최소화) + 커밋 + `build_drift_test` | 드리프트 음성 시험 |
| 3 | 링크 → deps(refines·supersedes·verifies·part_of·imports). `analysistest`로 끊긴 링크 영구 음성 시험 | dangling 게이트와 일치 |
| 4 | `package_group` + plane별 visibility. `analysistest`로 역방향 verifies·plane 위반 | 역방향 의존 빌드 실패 |
| 5 | `chunk2kg`를 규칙 액션으로 분해, `KgInfo` depset 병합 → `//kg:chunks_kg`. `metrics`·`index`를 output group으로 | 생성 TTL 바이트 동일(정규화 후) |
| 6 | `workset`을 aspect + `--//kb:role` 플래그로. `impact`를 `query rdeps` 위에 | 역할별 작업 집합 크기 = 2단계 통과 조건 측정 |

### 진행 기록 (hci, 2026-09-11)

| 순서 | 상태 | 산출 |
|---|---|---|
| 1 규칙·provider | **완료** | `defs/kb.bzl`: `ChunkInfo`·`OntologyModuleInfo`, `kb_chunk`·`kb_decision`·`kb_ontology_module`, 수준 허용표·plane 단방향·serves·supersedes·verifies 분석 시점 `fail()`, 42줄 lint 검증 액션(`bazel build` 411 액션 PASS) |
| 2 생성기·드리프트 | **완료** | `tools/gen_build.py` → BUILD 14개(요구 33·결정 184·옛 결정 153 타깃, 모듈 10, `modules.bzl`) 커밋, `//:build_drift_test`(음성: 손 편집 시 FAIL 확인). `project-ontology.ttl`의 `owl:imports`에 빠져 있던 channel·state·tag 보강 |
| 3 링크 → deps | **완료** | `refines` 335·`supersedes` 134 → deps. 끊긴 링크 = 로드 에러 확인. `cites`·`assumes` 제외(확인 2) |
| 4 가시성 | **완료** | `//kb:dev_readers`·`vv_readers`·`requirement_readers`·`decision_readers`. 역방향 의존 → "not visible" 확인. `//defs/tests` analysistest 5종(skylib 1.7.1) |
| 5 chunk2kg 분해 | **완료** | `KgInfo` 조각(`chunk2kg --fragment`, 타깃당 액션) → 패키지 `kb_bundle(:kg)` → `kb_kg_merge`(`--merge`, IRI 중복 검사) = `//kg:chunks_kg`. 옛 union은 `chunks_kg_union`으로 남겨 `kg_equivalence_test`가 바이트 동일(629,457 B)을 검사. 청크 하나 수정 → 조각 1 + 병합 1만 재실행. 정규 순서(IRI 정렬)를 양쪽에 적용 |
| 6 플래그 뷰·impact | **완료(변형)** | `kb_workset_view` + 빌드 설정 `//kb:role·anchor·levels·hops·budget`(skylib `string_flag`·`int_flag`) — `bazel build //kg:workset --//kb:role=… --//kb:anchor=…`. `tools/impact.py`가 `rdeps` 위에서 12.6절 네 수치(예: `r-008-descend-to-executable` → 영향 항목·직접 의존자·plane 분포·승인 필요 결정). **aspect는 쓰지 않았다** — aspect는 deps 방향(상류)만 따라가 rdeps(하류 이웃)를 못 보고, 역할→plane 사상을 카탈로그와 중복하게 된다. 뷰는 규칙 + 플래그로 같은 효과 |

### 하지 않는 것

- transition으로 plane마다 구성 분기 — 지금 실효 없음.
- toolchain화 — 이득 소폭, 보류.
- 본문 인용 `cites`의 deps화 — 유저 확인 2대로 1차 제외.

인수: orchestrator 2026-09-12 — 유저 "전부 수용으로 진행". 권고 B와 실행 순서 6단계는 2026-09-11에 구현 완료(진행 기록 표). 이번에 기능 표의 남은 "후속" (a)를 반영했다: 외부 표준 어휘 PROV-O·SKOS를 `MODULE.bazel`의 `http_file`로 sha256 고정해 가져오고(`@prov_o//file`·`@skos//file`), `validate.py` `vocab`이 `--standard-vocab`로 그 네임스페이스의 용어가 원문에 실재하는지까지 검사한다 — 세 게이트(`//kg`·`//kb/ontology`·`//kb/odd`)에 연결. (b) `@kb_links` 합성은 권고대로 생성 BUILD 방식을 유지해 하지 않는다. 표의 나머지(rule(test=True) 게이트·symbolic macro·output group·toolchain·transition·aspect)는 진행 기록의 변형 결정대로 — 기능상 얻는 것이 없는 재구성이라 채택하지 않는다.
