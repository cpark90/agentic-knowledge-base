# rules — 무엇이 유효한 지식 구조인가

원본은 노트 v5([`agent-knowledge-system-notes.md`](agent-knowledge-system-notes.md))
Part II·IV·V·VII·VIII·IX·X와 그 재도출 결정(`kb/dev/decision/`)이다. 구조도 v5에 따라
**코어(§1~§6, 두 KB 공통) / development(§7) / V&V(§8)** 세 층으로 적는다. **규칙은 여기, 규칙을 수행하는 절차는
[`method.md`](method.md), 규칙을 기계로 강제하는 것은 [`tools.md`](tools.md)의 검사 도구다.**
기계가 판정할 수 없는 규칙은 [`../STYLEGUIDE.md`](../STYLEGUIDE.md)의 `[지킴]`으로 남는다.

# 코어 — 두 KB가 공유하는 규칙

## 1. chunk — 자립적 최소 지식 단위

**chunk는 포맷이 아니라 구조 규칙이다.** 마크다운 본문에만 적용되는 것이 아니라
온톨로지·ODD·설계 공간·지식그래프 파일에도 같이 적용된다 (유저 결정 2026-09-04).

| 규칙 | 내용 | 근거 |
|---|---|---|
| 크기 | 본문 42줄 이하. 컨텍스트 한계 약 200줄의 1/5 — 한 번에 4~5개를 조망한다 | d-0002 |
| 단위 | 한 chunk = 한 plane · 한 level · 한 주제 · **한 파일** | d-0002 · d-0071 |
| 라벨 | 한/영 각 하나. 라벨만 보고 본문을 예측할 수 있어야 한다(검사 불가, 규약) | d-0082 |
| 상태 | `draft` → `stable` → `suspect` → `invalidated` → `deprecated`. OKF `status` 어휘(draft·stable·deprecated) + 무효화 확장 둘. `stable`이 d-0078의 `valid`다 | d-0078 |
| 앵커 | chunk IRI가 앵커다. 산문 계열은 파일 경로, 코드 계열은 심볼로 해석한다 | d-0077 · d-0105 |
| 신뢰 등급 | `generated.by` 필수, `verified`가 없으면 미검증. `human:` 접두어가 사람 검토 등급 | §1.1 |
| 네 그래프 | head(타입·plane·level·라벨) · assertion(본문, 42줄은 여기만) · provenance · pubinfo | d-0011 |

**지식의 종류는 "X 청크"라 부르지 않는다.** 조건·개념·변수·후보·결정·가정·시그니처·
함수·주석·관측처럼 고유 용어로 부르고, "청크"는 그것들이 따르는 구조 규칙을 가리킬 때만
쓴다 (유저 결정 2026-09-04). 온톨로지 클래스 이름(`agt:DecisionChunk` 등)과 그래프 라벨을
인용할 때는 그대로 쓴다 — 그것은 구조 타입의 식별자다.

**본문 중복은 안전율로 용인한다** (유저 결정 2026-09-11,
[`p4-redundancy-as-safety-margin`](../kb/dev/decision/p4-redundancy-as-safety-margin/conclusion.md)).
자립성이 맥락의 반복을 요구하므로 같은 서술이 여러 청크에 있는 것은 결함이 아니다. 단
경계가 있다 — **개념·용어·라벨·요구의 중복은 용인하지 않는다**(어휘 드리프트·인터페이스
충돌·추적 커버리지 왜곡). 알고 둔 중복은 `coUpdatesWith`로 묶어 한쪽의 변경이 다른 쪽을
`suspect`로 만들게 한다 — 링크 없는 중복이 드리프트다. 정리는 재검증 시점에서 일괄로:
`consistency` 보고(중복·라벨 형식·용어)는 커밋마다, 병합·묶기·유지 판정은 도입 단계 끝마다.

### 신뢰 등급 — 누가 만들고 누가 검증했는가 {#11}

OKF의 행위자 규약을 그대로 쓴다: 도구는 `<생성기>/<버전>`, 사람은 `human:<id>`, 프로세스는
`process:<id>`. 등급은 저장하지 않고 질의로 얻는다 — `verified`가 없으면 **미검증**,
`human:` 없는 검증만 있으면 **기계 확인**, `human:`이 있으면 **사람 검토**다.

게이트 둘이 이 위에 선다.

| 검사 | 강제하는 것 |
|---|---|
| `generatedBy` 필수 | 누가 만들었는지 없는 항목을 만들 수 없다 |
| `generatedAtTime ≤ verifiedAt` | **검증 뒤에 내용이 바뀌면 FAIL** — 사람이 검증한 항목을 에이전트가 고치고 재검증하지 않는 경우를 잡는다 |

둘째가 요점이다. "decision은 유저 승인이 `valid` 전이의 조건"(d-0003)이 지금까지 그래프에
기록되지 않았고 채널의 `status: approved`는 그래프 밖이었다 — `verified`가 그 둘을 잇고,
write plane 경계가 규약에서 기계 검사로 내려온다.

*현재 실측(2026-09-10): 생성자는 `claude/fable-5`·`claude/opus-5`뿐, **사람 검토 0건**.*

### 파일 형식과 head 생성

head 메타데이터는 파일 안(frontmatter)에 있고, `kg/chunks-kg.ttl`은 거기서 **생성**된다.
손으로 쓰지 않는다 — `lineCount`·`assertionLocation`이 파일에서 계산되므로 어긋날 수 없다.

```markdown
---
id: https://agentic-knowledge-base.dev/id/chunk/<uuid4>    # 필수 — uuid 영속 IRI (OKF 확장 키 id; 경로 = 주소, uuid = 정체성)
type: decision             # 필수 (OKF). requirement|decision|contract|schema|artifact|annotation|memory
level: concrete            # 필수. functional|abstract|logical|concrete|executable
title_ko: Bazel 하네스 채택  # 필수 (OKF 확장 키)
title: Adopt Bazel harness    # 필수 (OKF title)
status: stable             # 필수 (OKF). draft|stable|suspect|invalidated|deprecated
generated: {by: claude/fable-5, at: 2026-09-01T17:34:48+09:00}   # 필수 (OKF)
verified: [{by: human:cpark, at: 2026-09-07T10:00:00+09:00}]     # 선택 (OKF)
assumes: [<가정 IRI>, ...]      # 선택
sources: [{resource: <출처 IRI>}, ...]   # 선택 — OKF v0.2 sources: 객체 목록(resource 필수, id·title·author 선택) → prov:wasDerivedFrom. 도입 3단계부터 하네스가 읽기 집합으로 채움
refines: [<IRI>, ...]           # 선택 — 결정→요구 등
supersedes: [<IRI>, ...]        # 선택 — 시간축 대체
part_of: <복합체 IRI>            # 선택 — 복합체의 부분일 때
composite: {id: ..., title_ko: ..., title: ...}  # 복합체 선언 — 대표 부분에서 한 번만
---
본문 — 42줄 이하 (frontmatter와 앞뒤 빈 줄은 세지 않는다)
```

IRI는 uuid로 영속이고, 내용 버전은 `chunk2kg`가 본문의 sha256 앞 12자를
`agt:contentHash`로 계산해 붙인다 — 같은 IRI에서 내용이 바뀌었는지를 해시 비교로
안다 (노트 9.9절, 유저 결정 Q1).

**이 형식은 [OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
번들이다** — 마크다운 + YAML 프론트매터, `type`만 필수, 소비자는 알 수 없는 키를 견딘다.
`id`·`title_ko`·`level`·`assumes` 등은 확장 키로 남고 외부 도구도 이 저장소를 읽을 수 있다
(필드 사상은 [`pe-three-layer-binding`](../kb/dev/decision/pe-three-layer-binding/conclusion.md)).
예약 파일명 `index.md`·`log.md`는 **생성물로만** 둔다 — `bazel build //kb/dev:index` (유저 결정 Q4).

값 어휘의 원본은 `tools/chunk2kg.py`의 상수(`PLANE_CLASS`·`LEVELS`·`STATES`·`REQUIRED`)다.
생성 경로: 청크 타깃(`kb_chunk`·`kb_decision`)마다 head 조각 → 패키지 `:kg` 묶음 → `//kg:chunks_kg`(`kb_kg_merge`)
→ `bazel-out/.../kg/chunks-kg.ttl` → `//kg:gate_test`의 입력. union 생성(`chunks_kg_union`)과 바이트 동일해야 한다. 생성물은
`bazel-out`에만 존재하며 소스 트리에 같은 이름의 파일을 두지 않는다.

**지식은 두 KB로 갈려 산다** — 개발 KB `kb/dev/`(요구·결정·계약·스키마·구현), V&V KB
`kb/vv/`(검증 목표·시나리오·판정 기준). 두 KB를 잇는 링크는 `verifies` 하나뿐이고 주어는
항상 V&V 쪽, `kb/vv/`의 편집 주체는 vnv 역할뿐이다 (노트 Part VII, 유저 결정 저장 분리).
`chunks/`는 v1 유래 결정의 잔류 위치로, 재도출로 대체된 것은 `deprecated`가 된다.

**네 그래프는 현재 논리적 구분이다** — 저장 형식이 Turtle이라 물리적으로는 기본 그래프
하나다. TriG 전환은 `annotation`이 생겨 "어느 그래프에 대한 주석인가"를 말해야 할 때
재검토한다.

## 2. 복합체 — 통합이 필요한 것만

복합체(`agt:Composite`)는 **chunk의 part-of 묶음**이다. 본문이 없고, 라벨과 순서 있는 부분
목록이 전부다. `agt:Chunk`와 disjoint하며 둘 다 `agt:KnowledgeItem`의 하위다.

| 규칙 | 내용 | 근거 |
|---|---|---|
| 동질성 | 부분의 plane·level이 전체와 같다. plane·level을 넘는 관계는 전부 링크다 | d-0074 |
| 크기 | 직접 부분 최대 9개(7±2) | d-0074 |
| 순서 | 순서가 뜻을 갖는 복합체만 `co:List` + `co:index`. 순서를 요구하지 않는 것에 순서를 붙이면 거짓 정보다 | d-0073 |
| 비순환 | `part-of`의 반대칭 공리로 추론된다 | d-0074 |
| 상태 | 부분에서 추론된다 — 부분 하나가 `invalidated`면 복합체는 `suspect` | d-0074 |

**모든 chunk가 복합체에 속할 필요는 없다** (유저 결정 2026-09-02). 통합이 필요한 것만
묶고 나머지는 개별로 둔다. 통합의 기준은 둘이다 — **함께 읽혀야 이해되는가**(병합 신호,
d-0002), **순서가 뜻을 갖는가**(d-0073). 셋째 기준인 "무효화가 함께 번져야 하는가"는
복합체가 아니라 링크(`relatedTo`)로 표현한다
([`feedback/dependency-graph-design.md`](feedback/dependency-graph-design.md) §2.4).

**결정은 세 청크의 복합체다** (노트 4.7절·7.4절, 유저 결정 C2) — 결론(concrete)·근거(logical)·
대안(logical, **필수** — "대안 없었음"도 기록)이 `kb/dev/decision/<파트>-<슬러그>/` 디렉토리 하나에 살고,
복합체 개체는 conclusion의 frontmatter 선언에서 `chunk2kg`가 생성한다. 이 복합체는
level이 섞이므로 동질성 규칙과 긴장한다 — 등록된 미해결이다
([`open-questions.md`](open-questions.md) "이 저장소가 관찰한 추가 긴장").

## 3. plane — 판정 방식으로 나뉜 종류

plane의 분류 기준은 저장 위치나 파일 형식이 아니라 **"맞다"고 판정되는 메커니즘**이다
([`id:chunk-d0003`](../chunks/decision/d-0003-plane-by-verification.md)).

plane은 **일곱**이다 (v3에서 `requirement` 추가).

| plane | 판정 방식 | 변경률 | 개발 프로파일의 실체 |
|---|---|---|---|
| `requirement` | 이해관계자 확인 (EARS 형식 + 유저 승인) | 매우 낮음 | 요구사항 문장 |
| `decision` | 논증의 타당성 (논박 가능, 기계 판정 불가 → 유저 승인) | 낮음 | 설계 결정·아키텍처 문서 |
| `schema` | 스키마·호환성 검사 | 낮음 | 데이터 프로토콜·스키마 |
| `contract` | 형식 검사 (결정론적) | 중간 | 인터페이스·타입 시그니처 |
| `artifact` | 실행·실측 | 빠름 | 소스코드 |
| `annotation` | 사회적 합의 (해소/승인) | 매우 높음 | 주석·리뷰 코멘트 |
| `memory` | 없음 (휘발성) | 매우 빠름 | 에이전트 작업 메모리 |

plane은 `agt:Chunk`의 **하위 클래스**이고 level은 **속성**(`agt:hasLevel`)이다 — plane마다
다른 shape을 붙이기 위해서이고, 같은 항목이 level을 바꾸는 일은 없기 때문이다(전이는 새
chunk + `refines`) ([`id:chunk-d0071`](../chunks/decision/d-0071-plane-class-level-property.md)).

**plane 추가의 유일한 근거는 판정 방식이 기존 어디와도 다를 때다.** 같으면 하위 클래스로
둔다. 영향은 단방향이며 순서 기준은 변화 속도다 —
`requirement → decision → contract/schema → artifact → annotation → memory`. 무효화도 이
순서로만 전파되므로 파급이 유계가 된다 (노트 5.2절).

## 4. traceability — 인터페이스를 기준축으로 한 mapping

각 종류의 **인터페이스를 기준축**으로 plane 간 항목을 잇는다. 링크의 양 끝은 파일이 아니라
chunk·복합체의 IRI이고, 링크는 산출물 밖(`-kg`)에 한 방향만 저장한다(역방향은 질의)
(d-0010 · d-0105).

링크 타입은 네 족으로 정렬된다 (`kb/ontology/related/trace/`).

| 족 | 뜻 | 잎 | 전파 |
|---|---|---|---|
| `agt:references` | 본문이 식별자로 가리킴 | `cites` · `targets` | 대상 변경 → 출발점 `suspect` |
| `agt:semanticallyDependsOn` | 빼면 의미상 불완전 | `refines` · `satisfies` · `constrains` · `verifies` · `derivesFrom` · `usesConcept` · `assumes` · `generates` · `allocates` | 같음. plane 단방향 안에서만 |
| `agt:relatedTo` | 함께 갱신되어야 함 | `coUpdatesWith` · `conflictsWith` | 대칭 — 양쪽 `suspect` |
| (구성 관계) | 함께 읽힘·순서 | `hasDirectPart` | 부분이 무효면 전체 `suspect` |

`allocates`(요구→구성요소 할당)와 `generates`(산출 의존)는 v3 9장에서 추가됐다 (유저 결정
C7). `serves ⊑ refines`(결정 → 요구·관심사)는 v4 6.8·7.3의 기여 명시다. `supersedes`는 시간축이라
세 족 밖이다. **링크는 개체다**(`agt:Link`) — 양 끝·타입·**조건**(`when`: ODD 속성·가정 위의 CEL)·
**증거 기록**(`agt:Evidence` — 종류·참조·극성 ± 항목 목록)를 갖고, 확정 전 후보는 `agt:CandidateLink`,
판정된 것은 `agt:ConfirmedLink`다. 상태(`candidate`/`confirmed`/`suspect`/`invalid`)는 저장값이
아니라 **조건 평가와 증거 기록 규칙의 결과**다. **수치 신뢰도는 없다** — 선호는 지지 증거의 종류 서열
(구축 > 실행 > 동시 편집 > 공동 커버 > 임베딩 > 세션 > 제안)에서 파생된다. `assumes`와 스코프
conditional은 `when`의 특수형이다. 증거 기록 규칙 둘은 verify 질의다 — 구축(+)·실행(+) 없는 확정,
(−)가 있는 확정 (`tools/verify-queries/`). (노트 9.11절, 2026-09-10)

상세 설계(LEDGER·LARGER를 참고한 조회 알고리즘, 복원 계획)는
[`feedback/dependency-graph-design.md`](feedback/dependency-graph-design.md).
**어휘는 갖춰졌고 링크 데이터는 아직 0개다.**

## 5. knowledge graph — 무엇을 담는가

| 담는 것 | 위치 | 손/생성 |
|---|---|---|
| chunk head | `kg/chunks-kg.ttl` | **생성** |
| 복합체 | `kg/composite-kg.ttl` | 손 |
| 가정·출처 문서 | `kg/base-kg.ttl` | 손 |
| 역할·스코프·채널·하네스 (입력) | `kg/catalog-kg.ttl` | 손 |
| 조건과 ODD | `kb/odd/project-odd.yml` (OpenODD YAML 매핑: `TAXONOMY`·`MODULES`·`INCLUDE_AND`…; 확장 키 `ATTRIBUTES`·`LITERALS`·`CHECKS`·`EXCLUSIONS_REVIEWED`) → 생성 `project-odd.ttl`·`taxonomy.yml` | YAML 손, TTL 생성 |
| 후보 링크 | `kb/dev/**/*.space.md` (`type: agt:Space`, 변수 하나 = 파일 하나) | 미구현 — [p9-candidate-storage](../kb/dev/decision/p9-candidate-storage/conclusion.md) |

### ODD

프로젝트당 하나이며, 스코프·가정·시나리오·커버리지의 **분모**다. 조건은 정적 요소·환경
조건·동적 요소 3분류이고 각각 값 또는 범위, 객관적 판정 방법, 등급 A~D를 갖는다. 판정
불가(D)는 ODD에 넣지 않는다 (d-0008 · d-0059 · d-0064).

### 가정

모든 chunk는 ODD 조건 위의 가정 위에 선다. **ODD에 없는 조건을 참조하는 파생물은 게이트가
거부한다** — 대응은 ODD 확장 또는 파생물 기각뿐이다. 가정이 깨지면 그 가정에 의존하는
항목이 자동으로 무효화 표시되므로 전수조사가 필요 없다 (d-0007 · d-0008 · d-0087).

### level — 정제 수준과 수준 허용표

v3가 level을 **정제 수준**로 재정의했다 (노트 6.4절): `functional`(요구만 있는 높이) ·
`abstract`(형식 문장, 도메인 없음) · `logical`(후보와 제약) · `concrete`(확정된 개체) ·
`executable`(동작만 남은 높이). 다섯 단계를 유지하며 건너뛰지 않는다.

**모든 plane이 모든 level에 살지 않는다** — plane×level 수준 허용표가 SHACL로 강제된다
(`kb/ontology/shapes/residency-shapes.ttl`):

| plane | 허용 level |
|---|---|
| `requirement` | functional |
| `decision` | abstract · logical · concrete |
| `contract` | abstract · logical |
| `schema` | logical · concrete |
| `artifact` | concrete · executable |
| `memory` | concrete |
| `annotation` | (제약 없음 — 모든 level의 항목에 대해 주석한다) |

### 통제 어휘

데이터의 술어는 `agt:` 온톨로지 또는 등록된 표준 어휘(rdf·rdfs·owl·xsd·skos·sh·prov·
dcterms·co·obo) 안이어야 한다. `agt:` 접두어인데 온톨로지에 없으면 오타 또는 무단 어휘
생성이고, 등록되지 않은 네임스페이스면 어휘 우회다 — 둘을 다른 메시지로 구분해 보고한다
(d-0028, `tools/kb_lib.py`가 목록의 단일 정의처).

### 개체 IRI 접두사

| 종류 | 형식 | 사는 곳 |
|---|---|---|
| chunk (v3 이후) | `id/chunk/<uuid4>` — 불투명 영속 IRI | (생성) `chunks-kg.ttl` |
| chunk (v1 잔류) | `id:chunk-d0001` 등 — deprecated 예정 | (생성) `chunks-kg.ttl` |
| 복합체 (v3 이후) | `id/composite/<uuid4>` | (생성) 또는 `composite-kg.ttl` |
| 가정 · 출처 문서 | `asm-` · `doc-` | `base-kg.ttl` |
| 복합체 (손) | `comp-` | `composite-kg.ttl` |
| ODD · 조건 | `odd-` · `cond-` | `project-odd.ttl` |
| 하네스 · 역할 · 스코프 · 채널 | `h-` · `role-` · `scope-` · `chan-` | `catalog-kg.ttl` |
| 시나리오 · 실행 기록 | `scn-` · `run-` | (아직 없음) |

IRI는 불투명하게 유지한다 — 라벨이나 경로가 바뀌어도 IRI가 유지되어야 시간 정체성이
성립한다 (그래서 v3부터 uuid다, 유저 결정 Q1). 사람이 읽는 이름은 IRI가 아니라
`rdfs:label`이고, 내용 버전은 `agt:contentHash`다.

### 정규화 직렬화

기계가 만든 TTL은 커밋 전 정규형으로 바꾼다 — 정렬된 `@prefix` + 주어·술어·목적어 정렬.
직렬화 순서가 불안정하면 git diff가 의미 없는 변경으로 오염되고, 그것이 무효화 판정의
입력을 더럽힌다 (d-0050).

```bash
bazel run //tools:canonicalize -- --write <files>
```

## 6. 그래프 안과 밖

검사 대상인 지식(`kb/{ontology,odd,dev,vv}/`·`kg/`·`chunks/`)과, 대상이 아닌 문서
(`docs/`·`.claude/`)를 가른다. 소통 기록과 지식을 섞으면 통제 어휘 검사가 무의미해진다.
문서는 결정을 복사하지 않고 **IRI로 인용**한다 — 복사하면 이중 관리가 되고 둘이 어긋나는
순간 어느 쪽이 원본인지 알 수 없어진다 (d-0075).

# development 규칙 — 개발 KB (노트 7.2~7.7)

개발 KB는 요구 명세에서 실산출물을 생산하기 위한 지식이다
([`p7-dev-kb-purpose`](../kb/dev/decision/p7-dev-kb-purpose/conclusion.md)). 코어 규칙 위에 다음이 더해진다.

| 규칙 | 내용 | 결정 |
|---|---|---|
| `requirement` | functional 전용. EARS 다섯 패턴, 이해관계자·관심사 필수 | [p7-dev-plane-substance](../kb/dev/decision/p7-dev-plane-substance/conclusion.md) |
| 결정 복합체 | 항상 결론·근거·대안 세 청크. **대안 청크 없는 결정 = shape 위반**, "대안 없었음"도 기록 | [p7-alternatives-mandatory](../kb/dev/decision/p7-alternatives-mandatory/conclusion.md) |
| 결정의 수준 | abstract(변수)·logical(후보·제약·배제)·concrete(값)는 별개 청크, `refines`로 연결. concrete가 생겨야 확정. abstract 청크는 `-space`가 있을 때만 | [p7-decision-spans-three-levels](../kb/dev/decision/p7-decision-spans-three-levels/conclusion.md) |
| 기여 | abstract 결정은 `serves`(⊑ `refines`)로 어느 요구의 어느 관심사에 기여하는지 명시. 없으면 거부 | [p6-transition-gates](../kb/dev/decision/p6-transition-gates/conclusion.md) |
| 계약 우선 | `contract` abstract가 구현보다 먼저. 계약 없는 구현 = 정제 단절. 계약 logical(사후조건)이 V&V 기준의 재료 | [p7-contract-first](../kb/dev/decision/p7-contract-first/conclusion.md) |
| 스키마 | `decision`에서 `derives-from`, `contract`를 `constrains`. 비호환 변경 = 새 IRI + `supersedes` | [p7-schema-derivation](../kb/dev/decision/p7-schema-derivation/conclusion.md) |
| `artifact` | 구현만. verifier는 V&V KB | [p6-executable-splits-by-kb](../kb/dev/decision/p6-executable-splits-by-kb/conclusion.md) |
| 구현 착수 | developer는 concrete 결정·확정 스키마 없이 구현 불가(스코프 conditional). developer 작업 집합에 `-space` 없음 | [p7-developer-requires-concrete](../kb/dev/decision/p7-developer-requires-concrete/conclusion.md) |
| 대체 | 결정 대체는 `supersedes`. 옛 결정은 `deprecated`, 그 `satisfies` 전부 `suspect` | [p7-decision-supersession](../kb/dev/decision/p7-decision-supersession/conclusion.md) |
| 완료 | 연쇄 완주 · 계약 선행 · 대안 존재 · 가정 `stable` · **V&V `verifies` 유효** — 개발 KB만으로 완료 선언 불가 | [p7-dev-kb-completion](../kb/dev/decision/p7-dev-kb-completion/conclusion.md) |
| 역할 | design(요구·결정·계약·스키마·ODD) / developer(`artifact`) / orchestrator(dispatch 결정) / V&V(`annotation`만) | [p7-dev-roles-and-scopes](../kb/dev/decision/p7-dev-roles-and-scopes/conclusion.md) |

이 저장소의 실측(2026-09-10): `requirement` 33 · `decision` 182(대안 182/182) · `contract`·`schema`·`artifact` 0.

# V&V 규칙 — V&V KB (노트 8.2~8.5, 8.11~8.15, 8.4, 9.11)

V&V KB는 코어의 두 번째 인스턴스다 — 새 plane을 만들지 않고 실체만 다르다
([`p8-vv-plane-instances`](../kb/dev/decision/p8-vv-plane-instances/conclusion.md)).

| 규칙 | 내용 | 결정 |
|---|---|---|
| 독립성 | 개발 역할은 V&V KB 쓰기 불가. 기준 수정은 요구 수정으로만. 저장 분리(`kb/vv/`), V&V → 개발 단방향 의존 | [p8-vv-independence-scope](../kb/dev/decision/p8-vv-independence-scope/conclusion.md) |
| 검증 대응물 필수 | f→a에 검증 목표 / l→c에 합격 기준 / c→e에 검증기. 없으면 개발 게이트 실패(7단계 전엔 경고) | [p8-scenario-ladder-rungs](../kb/dev/decision/p8-scenario-ladder-rungs/conclusion.md) |
| `verifies` | KB를 가로지르는 유일한 링크. 방향은 V&V → 개발, 같은 level끼리 | [p6-executable-splits-by-kb](../kb/dev/decision/p6-executable-splits-by-kb/conclusion.md) |
| 시나리오 | `decision`(vv) 복합체 — 자극·요인·배제 자극. 변수는 ODD 속성만, ODD 밖은 `odd:outside`로 커버리지 제외 | [p8-scenario-authoring](../kb/dev/decision/p8-scenario-authoring/conclusion.md) |
| 기준 ≠ 자극 | 기준은 `contract`(vv) 별도 청크, `verifies` 속성으로 바인딩. 판정식 없는 기준은 abstract로 강등 | [p8-pass-criteria](../kb/dev/decision/p8-pass-criteria/conclusion.md) |
| 케이스 | concrete 케이스는 사람이 쓰지 않는다 — `keep`+`cover`에서 생성. 표본 근거 없는 케이스 거부 | [p8-case-generation](../kb/dev/decision/p8-case-generation/conclusion.md) |
| 역할 | 검증기 저자 ≠ V&V engineer (또는 다른 세션). audit은 쓰기 없음 | [p8-vv-roles](../kb/dev/decision/p8-vv-roles/conclusion.md) |
| 재현성 | 재현 불가 → 5~6단계 강등. 6단계 관측은 커버리지에 넣지 않음 | [p8-reproducibility](../kb/dev/decision/p8-reproducibility/conclusion.md) |
| 학습된 판정자 | 정확도·판별력·캘리브레이션 3지표 + 사람 승인. 결과는 head `verified` 목록에 | [p8-learned-environment-and-judge](../kb/dev/decision/p8-learned-environment-and-judge/conclusion.md) |
| 평가의 목적지 | 확인 결과는 `requirement`로 — 요구가 바뀌는 유일한 정규 경로 | [p8-verification-and-validation](../kb/dev/decision/p8-verification-and-validation/conclusion.md) |
| 불일치의 귀속 | 산출물 / 지식(요구 과도·제약 부족·가정 누락) / 둘 다는 **결정**이며 V&V `decision`의 지침. 진단은 기호 도구 먼저 | [p8-mismatch-attribution](../kb/dev/decision/p8-mismatch-attribution/conclusion.md) |
| 실행 증거 | 검증기 결과는 개발 KB `satisfies` 후보의 증거 기록에 (+)(−)로 — 링크가 아니라 증거 기록 항목이라 방향 규칙 유지 | [p9-evidence-ledger](../kb/dev/decision/p9-evidence-ledger/conclusion.md) |

이 저장소의 실측(2026-09-10): `kb/vv/`는 비어 있다 — 이 저장소 자신의 검증 목표·시나리오·기준이 없다 (도입 7단계).
