# rules.md — 무엇이 유효한 지식 구조인가 (생성 파일)

- 생성기: `tools/gen_norms.py` · gendoc/1
- 입력: 원본 파일 71개 · 절 30 · 규약 줄 76 · 전체 목록은 [입력 파일](#입력-파일)
- 질의: `kb/dev/norm/rules/` 의 절 청크를 선언 순서로 펼치고 항목마다 결정의 `규약:` 줄을 싣는다
- 재현: `python3 tools/gen_norms.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 `kb/dev/norm/rules/` 의 절 청크와 결정의 `conventions.md`이다. 검사: `//:norms_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

## 목차

- [§1. chunk — 자립적 최소 지식 단위](#1-chunk--자립적-최소-지식-단위)
- [§2. 복합체 — 통합이 필요한 것만](#2-복합체--통합이-필요한-것만)
- [§3. plane — 판정 방식으로 나뉜 종류](#3-plane--판정-방식으로-나뉜-종류)
- [§4. traceability — 인터페이스를 기준축으로 한 mapping](#4-traceability--인터페이스를-기준축으로-한-mapping)
- [§5. knowledge graph — 무엇을 담는가](#5-knowledge-graph--무엇을-담는가)
- [§6. 그래프 안과 밖](#6-그래프-안과-밖)
- [§7. development 규칙 — 개발 KB (노트 7.2~7.7)](#7-development-규칙--개발-kb-노트-7277)
- [§8. V&V 규칙 — V&V KB (노트 8.2~8.5, 8.11~8.15, 8.4, 9.11)](#8-vv-규칙--vv-kb-노트-8285-811815-84-911)
- [입력 파일](#입력-파일)

<!-- 인용 시작: 청크에서 그대로 옮긴 값 — 원본이 자기 게이트를 통과했다 -->

원본은 노트 v5([`agent-knowledge-system-notes.md`](agent-knowledge-system-notes.md))
Part II·IV·V·VII·VIII·IX·X와 그 재도출 결정(`kb/dev/decision/`)이다. 구조도 v5에 따라
**코어(§1~§6, 두 KB 공통) / development(§7) / V&V(§8)** 셋으로 적는다. **규칙은 여기, 규칙을 수행하는 절차는
[`method.md`](method.md), 규칙을 기계로 강제하는 것은 [`tools.md`](tools.md)의 검사 도구다.**
기계가 판정할 수 없는 규칙은 [`../STYLEGUIDE.md`](../STYLEGUIDE.md)의 `[지킴]`으로 남는다.

## §1. chunk — 자립적 최소 지식 단위

**chunk는 포맷이 아니라 구조 규칙이다.** 마크다운 본문에만 적용되는 것이 아니라
온톨로지·ODD·설계 공간·지식그래프 파일에도 같이 적용된다 (유저 결정 2026-09-04).

| 규칙 | 내용 | 근거 |
|---|---|---|
| 크기 | 본문은 **토큰 상한** 이하다 — 저작 산문 **1,092**(42×26 = 예산 5,418의 1/5, 한 번에 4~5개를 조망), 인용(`artifact`·`memory`) **2,856**(42×68 = 한 창). 계수기는 고정된 `o200k_base`(ODD `cond-tokenizer-lock`)이고 단일 정의처는 `tools/kb_lib.py`의 `BODY_TOKEN_LIMITS`, 그래프 쪽은 `token-budget-shapes.ttl`(2026-10-01 — 그 전에는 42줄·200줄. 줄은 내용에 따라 토큰이 1.9배 갈린다) | [`p4-chunk-as-ontology-class`](../kb/dev/decision/p4-chunk-as-ontology-class/conclusion.md) · [`p1-chunk-unit-is-tokens`](../kb/dev/decision/p1-chunk-unit-is-tokens/conclusion.md) |
| 층 | 선택 키 `layer: knowledge \| methodology \| process`는 항목이 서비스의 어느 층에서 역할을 갖는가다([p0-service-is-a-three-layer-wiki](../kb/dev/decision/p0-service-is-a-three-layer-wiki/conclusion.md), 2026-10-01). 층은 plane과 직교하므로 type 제한이 없고, 명시가 없으면 `chunk2kg`가 `agt:inLayer agt:knowledgeLayer`를 방출한다 — 표시 누락이 산발로 세어지지 않아야 하고 층별 집계(CQ-38)의 분모가 항목 전수여야 한다. 코드 청크는 등록부의 `layer`가 원본이다. 값 어휘·개수는 `layer-shapes` | [`p0-service-is-a-three-layer-wiki`](../kb/dev/decision/p0-service-is-a-three-layer-wiki/conclusion.md) |
| 단위 | 한 chunk = 한 plane · 한 level · 한 주제 · **한 파일** | [`p4-chunk-as-ontology-class`](../kb/dev/decision/p4-chunk-as-ontology-class/conclusion.md) · [`p4-plane-subclass-level-property`](../kb/dev/decision/p4-plane-subclass-level-property/conclusion.md) |
| 라벨 | 한/영 각 하나. 라벨만 보고 본문을 예측할 수 있어야 한다(검사 불가, 규약) | [`p4-label-is-the-interface`](../kb/dev/decision/p4-label-is-the-interface/conclusion.md) |
| 상태 | `draft` → `stable` → `suspect` → `invalidated` → `deprecated`. OKF `status` 어휘(draft·stable·deprecated) + 무효화 확장 둘. `stable`이 d-0078의 `valid`다 | [`p4-chunk-state-machine`](../kb/dev/decision/p4-chunk-state-machine/conclusion.md) |
| 앵커 | chunk IRI가 앵커다. 산문 계열은 파일 경로, 코드 계열은 심볼로 해석한다 | [`p4-chunk-iri-is-the-anchor`](../kb/dev/decision/p4-chunk-iri-is-the-anchor/conclusion.md) · [`p10-link-storage-and-anchors`](../kb/dev/decision/p10-link-storage-and-anchors/conclusion.md) |
| 신뢰 등급 | `generated.by` 필수, `verified`가 없으면 미검증. `human:` 접두어가 사람 검토 등급. 상세는 §1의 신뢰 등급 절이다 | [`p2-trust-tier-from-generated-and-verified`](../kb/dev/decision/p2-trust-tier-from-generated-and-verified/conclusion.md) |
| 네 그래프 | head(타입·plane·level·라벨) · assertion(본문, 토큰 상한은 여기만) · provenance · pubinfo | [`p4-chunk-as-four-named-graphs`](../kb/dev/decision/p4-chunk-as-four-named-graphs/conclusion.md) |

**지식의 종류는 "X 청크"라 부르지 않는다.** 조건·개념·변수·후보·결정·가정·시그니처·
함수·주석·관측처럼 고유 용어로 부르고, "청크"는 그것들이 따르는 구조 규칙을 가리킬 때만
쓴다 (유저 결정 2026-09-04). 온톨로지 클래스 이름(`agt:DecisionChunk` 등)과 그래프 라벨을
인용할 때는 그대로 쓴다. 그것은 구조 타입의 식별자다.

**본문 중복은 안전율로 용인한다** (유저 결정 2026-09-11,
[`p4-redundancy-as-safety-margin`](../kb/dev/decision/p4-redundancy-as-safety-margin/conclusion.md)).
자립성이 맥락의 반복을 요구하므로 같은 서술이 여러 청크에 있는 것은 결함이 아니다. 단
경계가 있다. **개념·용어·라벨·요구의 중복은 용인하지 않는다.** 그 이유는 어휘 드리프트·
인터페이스 충돌·추적 커버리지 왜곡이다. 알고 둔 중복은 `coUpdatesWith`로 묶어 한쪽의 변경이
다른 쪽을 `suspect`로 만들게 한다. 링크 없는 중복이 드리프트다. 정리는 재검증 시점에서 일괄로
한다. `consistency` 보고는 커밋마다 내며 중복·라벨 형식·용어를 다룬다. 병합·묶기·유지 판정은
도입 단계 끝마다 한다.

### 신뢰 등급 — 누가 만들고 누가 검증했는가

OKF의 행위자 규약을 그대로 쓴다. 도구는 `<생성기>/<버전>`, 사람은 `human:<id>`, 프로세스는
`process:<id>`다. 등급은 저장하지 않고 질의로 얻는다. `verified`가 없으면 **미검증**,
`human:` 없는 검증만 있으면 **기계 확인**, `human:`이 있으면 **사람 검토**다.

게이트 둘이 이 위에 선다.

원본: [`p2-trust-tier-from-generated-and-verified`](../kb/dev/decision/p2-trust-tier-from-generated-and-verified/conclusion.md).

| 검사 | 강제하는 것 |
|---|---|
| `generatedBy` 필수 | 누가 만들었는지 없는 항목을 만들 수 없다 |
| `generatedAtTime ≤ verifiedAt` | **검증 뒤에 내용이 바뀌면 FAIL** — 사람이 검증한 항목을 에이전트가 고치고 재검증하지 않는 경우를 잡는다 |

둘째가 요점이다. "decision은 유저 승인이 `valid` 전이의 조건"(d-0003)이 지금까지 그래프에
기록되지 않았고 채널의 `status: approved`는 그래프 밖이었다. `verified`가 그 둘을 잇고,
write plane 경계가 규약에서 기계 검사로 내려온다.

*현재 실측(2026-09-10): 생성자는 `claude/fable-5`·`claude/opus-5`뿐이고 **사람 검토는 0건**이다.*

### 파일 형식과 head 생성

head 메타데이터는 파일 안의 frontmatter에 있고, `bazel-bin/kg/chunks-kg.ttl`은 거기서 **생성**된다.
손으로 쓰지 않는다. `tokenCount`·`assertionLocation`이 파일에서 계산되므로 어긋날 수 없다.

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
restored: [<IRI>, ...]          # 선택 — 위 링크 키의 대상 중 사후에 이은(복원) 것. 증거에 proposal 이 더해진다
specializationOf: <IRI>         # 선택 — 분할로 생긴 조각이 원 청크(같은 plane)를 가리킨다. 링크 IRI 는 뿌리 uuid 로 계산
part_of: <복합체 IRI>            # 선택 — 복합체의 부분일 때
composite: {id: ..., title_ko: ..., title: ..., ordered: [...], part_of: <상위 복합체 IRI>}  # 복합체 선언 — 대표 부분에서 한 번만.
                                # `part_of`는 선언된 **복합체**가 다른 복합체의 부분임을 적는다 (중첩, p4-composite-as-part-of)
---
본문 — 토큰 상한 이하(저작 산문 1,092 · 인용 2,856; frontmatter와 앞뒤 빈 줄은 세지 않는다)
```

IRI는 uuid로 영속이고, 내용 버전은 `chunk2kg`가 본문의 sha256 앞 12자를
`agt:contentHash`로 계산해 붙인다. 같은 IRI에서 내용이 바뀌었는지를 해시 비교로
안다 (노트 9.9절, 유저 결정 Q1).

**이 형식은 [OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
번들이다.** 번들은 마크다운 + YAML 프론트매터이고, `type`만 필수이며, 소비자는 알 수 없는 키를 견딘다.
`id`·`title_ko`·`level`·`assumes` 등은 확장 키로 남고 외부 도구도 이 저장소를 읽을 수 있다
(필드 사상은 [`pe-three-layer-binding`](../kb/dev/decision/pe-three-layer-binding/conclusion.md)).
예약 파일명 `index.md`·`log.md`는 **생성물로만** 둔다. 생성 명령은 `bazel build //kb/dev:index`다 (유저 결정 Q4).

**본문의 빈 자리는 세 값으로만 적는다**(유저 승인 2026-09-22 — [`p4-three-empty-values`](../kb/dev/decision/p4-three-empty-values/conclusion.md)).
`없음`은 찾아봤고 없다, `해당 없음`은 적용되지 않는다, `미확정`은 아직 모른다는 뜻이고 셋만 행동이 갈린다.
`N/A`·`TBD`·`미정`·단독 대시를 쓰지 않는다. 아직 모르는 것은 선택 슬롯 `미확정:`에 적고, 미결 집계는
문서가 아니라 그 슬롯에서 생성된다. 슬롯에는 그 슬롯의 질문에 답하는 문장만 쓴다
([`p4-slot-answers-one-question`](../kb/dev/decision/p4-slot-answers-one-question/conclusion.md)) — 다른 슬롯의 답·메타
문장·채움은 첨가다. 순서 목록의 모든 항목은 `1.`로 적고 항목 9개·중첩 2단계·항목당 2줄을 넘지 않는다.
검사는 `consistency` ⑧·⑨ 보고에서 시작해 수치가 0이 된 뒤 `chunk_lint`로 올린다. 슬롯 표지는 **자리**로 판정한다 —
그 줄의 필드 머리(줄 시작·`- ` 다음·` · ` 다음)에 있는 굵은 span만 슬롯이고 표 셀·문장 중간의 굵은 span은 강조다; 한정어는
12자 이하·마침표 없음일 때만 같은 표지다(2026-09-29 — 시나리오 표지를 더하자 옛 청크 32파일 60건의 강조가 슬롯으로
방출됐고 이 규칙으로 0이 됐다). 표지 낱말의 접두 겹침은 `kb_lib.validate_body_slot_markers`가 로드 시점에 거부한다.

**게이트 id의 단일 정의처는 `defs/kb.bzl`의 `GATES`**(id → 실행 계층·판정 도구·한글 라벨·설명 한 줄)**와 `TOOL_TAGS`**(게이트가 아닌 입력
문제·보고 태그)**다**(2026-10-02 — 통일 기획 2단계의 첫 조각; 그 전에는 같은 목록이 넷으로 갈려 있었다). `kb_lib`이 리터럴 읽기로
`*_GATE`·`*_TAG`를 파생하므로 상수를 손으로 두지 않는다. 게이트는 프로세스 층의 **항목**이고 개체는 `//kg:gates_kg`의
`id:gate-<id>`(`agt:Gate`, `agt:gateTier`, `agt:enforcedBy` → 판정 도구의 파일 복합체)다 — `kg/`에 손으로 쓰지 않는다. 갈림은
게이트 `gate-registry`(코드의 태그 ⊆ 등록부 · 손 상수 없음 · 폴백 값 일치 · 등록 id가 코드에 닿음)가 거부한다.

**값 어휘와 수준 허용표의 단일 정의처는 `defs/kb.bzl`이다**(2026-09-26·27). `PLANES`·`LEVELS`·`STATES`·`RESIDENCY`를 거기에만
적고, 파이썬 쪽(`chunk2kg`·`kb_lib`)은 그 리터럴을 읽어 파생한다. 청크를 파싱하는 모든 액션이 `//defs:kb.bzl`을 입력으로
받는다 — `kb_chunk`·`kb_decision`의 head 액션, `kb_consistency`·`kb_weave`·`kb_index`, `//space:design_space`,
`//:build_drift_test`이고, `bazel run` 도구는 `BUILD_WORKSPACE_DIRECTORY`로 푼다. 폴백값은 두지 않는다 — 값이 같아도
정의처가 둘이면 어느 날 하나만 고쳐진다. shape(`residency-shapes.ttl`)는 소스로 남되 게이트 `residency`가 원본과의
동일성을 강제한다.

값 어휘의 원본은 `tools/chunk2kg.py`의 상수(`PLANE_CLASS`·`LEVELS`·`STATES`·`REQUIRED`)다.
생성 경로는 청크 타깃(`kb_chunk`·`kb_decision`)마다 head 조각 → 패키지 `:kg` 묶음 → `//kg:chunks_kg`(`kb_kg_merge`)
→ `bazel-out/.../kg/chunks-kg.ttl` → `//kg:gate_test`의 입력이다.
생성물은 `bazel-out`에만 존재하며 소스 트리에 같은 이름의 파일을 두지 않는다.

**지식은 두 KB로 갈려 산다.** 개발 KB `kb/dev/`는 요구·결정·계약·스키마·구현을 담고, V&V KB
`kb/vv/`는 검증 목표·시나리오·판정 기준을 담는다. 두 KB를 잇는 링크는 `verifies` 하나뿐이고 주어는
항상 V&V 쪽이며, `kb/vv/`의 편집 주체는 vnv 역할뿐이다 (노트 Part VII, 유저 결정 저장 분리).
`chunks/`는 v1 유래 결정의 잔류 위치로, 재도출로 대체된 것은 `deprecated`가 된다.

**네 그래프는 현재 논리적 구분이다.** 저장 형식이 Turtle이라 물리적으로는 기본 그래프
하나다. TriG 전환은 `annotation`이 생겨 "어느 그래프에 대한 주석인가"를 말해야 할 때
재검토한다.

## §2. 복합체 — 통합이 필요한 것만

복합체(`agt:Composite`)는 **chunk의 part-of 묶음**이다. 본문이 없고, 라벨과 순서 있는 부분
목록이 전부다. `agt:Chunk`와 disjoint하며 둘 다 `agt:KnowledgeItem`의 하위다.

| 규칙 | 내용 | 근거 |
|---|---|---|
| 동질성 | 부분의 plane 클래스가 전체와 같다. level도 같되 결정 복합체는 예외다 — 결론 concrete·근거/대안 logical(`p7-decision-spans-three-levels`). plane·level을 넘는 관계는 전부 링크다. verify 질의 `composite-heterogeneous`가 검사한다 (2026-09-13) | [`p4-composition-rules`](../kb/dev/decision/p4-composition-rules/conclusion.md) |
| 크기 | 직접 부분 최대 9개(7±2). 넘는 묶음은 **중첩**으로 담는다 — 선언 청크의 `composite.part_of`가 그 복합체를 상위 복합체의 직접 부분으로 만들고(`p4-composite-as-part-of`), 중첩된 복합체 전부는 한 액션(= 한 Bazel 타깃)이 뿌리부터 잎까지 받는다. 코드의 추출이 이 자리를 처음 쓴다 — 파일 → 장·절 복합체 → 정의 청크이고 소스의 절 주석(`# ══ 장` · `# ── 절`)이 구조의 원본이다. 절 주석이 없어 9를 넘는 파일은 `FAIL [extract]`로 절 주석을 요구한다 — 9개씩 자르지 않는다(순서에 뜻이 없는 묶음) | [`p4-composition-rules`](../kb/dev/decision/p4-composition-rules/conclusion.md) · [`p7-code-links-on-file-composite`](../kb/dev/decision/p7-code-links-on-file-composite/conclusion.md) |
| 순서 | 순서가 뜻을 갖는 복합체만 `co:List` + `co:index`. 순서의 원본은 **선언**이다 — 선언 청크의 `composite:`에 선택 키 `ordered: [<부분 IRI>…]`(부분 전부를 빠짐없이 한 번씩)가 있을 때만 생성기가 낸다. 결정 복합체도 예외가 아니다 — 생성기가 결론·근거·대안 순서를 `ordered` 인자로 선언한다(유저 답 2026-09-29). 시나리오 복합체는 `ordered`가 필수다. 순서를 요구하지 않는 것에 순서를 붙이면 거짓 정보다 | [`p4-composite-as-part-of`](../kb/dev/decision/p4-composite-as-part-of/conclusion.md) · [`p4-composite-order-is-declared`](../kb/dev/decision/p4-composite-order-is-declared/conclusion.md) |
| 비순환 | `part-of`의 반대칭 공리로 추론된다 | [`p4-composition-rules`](../kb/dev/decision/p4-composition-rules/conclusion.md) |
| 상태 | 부분에서 추론된다 — 부분 하나가 `invalidated`면 복합체는 `suspect` | [`p4-composition-rules`](../kb/dev/decision/p4-composition-rules/conclusion.md) |

**모든 chunk가 복합체에 속할 필요는 없다** (유저 결정 2026-09-02). 통합이 필요한 것만
묶고 나머지는 개별로 둔다. 통합의 기준은 둘이다. 첫째는 **함께 읽혀야 이해되는가**(병합 신호,
[p4-chunk-split-and-merge](../kb/dev/decision/p4-chunk-split-and-merge/conclusion.md))이고, 둘째는 **순서가 뜻을 갖는가**([p4-composite-as-part-of](../kb/dev/decision/p4-composite-as-part-of/conclusion.md))다. 셋째 기준인 "무효화가 함께 번져야 하는가"는
복합체가 아니라 링크(`relatedTo`)로 표현한다 (§4 링크 타입 표). 복합체 **후보**는 커뮤니티 탐지가
제안하고 채택은 사람이 한다 ([`p4-community-detection-proposes-composites`](../kb/dev/decision/p4-community-detection-proposes-composites/conclusion.md)).

**결정은 세 청크의 복합체다** (노트 4.7절·7.4절, 유저 결정 C2). 결론은 concrete, 근거는 logical,
대안은 logical이다. 대안은 **필수**이며 "대안 없었음"도 기록한다. 세 청크는
`kb/dev/decision/<파트>-<슬러그>/` 디렉토리 하나에 살고, 복합체 개체는 conclusion의 frontmatter
선언에서 `chunk2kg`가 생성한다. 이 복합체는 level이 섞이므로 동질성 규칙과 긴장했다. 그 긴장은
[`p4-composition-rules`](../kb/dev/decision/p4-composition-rules/conventions.md)의 규약이 결정 복합체를 동질성의 level 예외로 정해 닫혔다(2026-09-13).

**결정 밖의 복합체는 `kb_composite`로 선다** (유저 답 2026-09-26, 도구를 고친다). 묶음의 단위는 파일이 아니라
**액션의 입력 집합**이다 — 같은 패키지에서 `composite.id`를 공유하는 청크 2~9개가 타깃 하나가 되고 부분 청크의
개별 `kb_chunk` 타깃은 사라진다. 타깃 이름은 `composite:`를 선언한 청크의 파일 이름이다. 부분과 선언은 같은
패키지에 있어야 하고 부분의 plane·level은 서로 같아야 한다. 판정은 세 시점이다 — 생성 시점 `tools/gen_build.py`의
`_check_bundle`, 분석 시점 `kb_composite`(`plane`·`level`을 한 쌍만 받으므로 이질 복합체를 표현할 수 없다), 그래프
verify 질의 `composite-heterogeneous`. 수준 혼합은 결정 복합체의 예외뿐이다. 손으로 쓴 `kg/composite-kg.ttl`의
복합체는 이 경로로 옮기고, 부분이 하나인 것은 복합체가 아니므로 남기지 않는다. 복합체 IRI는 지속 IRI 원칙대로
기존 `id:comp-*`를 유지한다.

**순서는 선언에서만 나온다** ([`p4-composite-order-is-declared`](../kb/dev/decision/p4-composite-order-is-declared/conclusion.md) —
유저 승인 2026-09-29 — 결정도 예외 없이, 도구 반영 같은 날). 선언 청크의 `composite:`에 `ordered: [<부분 IRI>…]`가 있으면 `kb_composite`·`gen_build`가
`part_iris`를 그 순서로 내고 `chunk2kg`가 `<복합체> a agt:Composite, co:List ; co:item [ a co:ListItem ; co:index
"<1..n>"^^xsd:positiveInteger ; co:itemContent <부분> ] …`을 방출한다. 없으면 `hasDirectPart`만 낸다 — `hasDirectPart`는 순서와
무관하게 남으므로 순서 트리플은 추가일 뿐이다. 목록이 부분 집합과 어긋나면 생성 시점 `gen-build`와 실행 시점 `chunk2kg`가
거부하고, 색인 1..n 연속·중복 없음·부분 집합과의 일치는 shape `composite-order-shapes`(`sh:sparql` — 이 저장소의 첫
사용)가 판정한다. 판정 단위가 복합체 노드 하나라 verify 실행 계층이 아니라 shape 실행 계층이다. `ordered`는 frontmatter의 메타데이터이므로
더하거나 고쳐도 `generated.at`·`verified`를 건드리지 않는다.

## §3. plane — 판정 방식으로 나뉜 종류

plane의 분류 기준은 저장 위치나 파일 형식이 아니라 **"맞다"고 판정되는 메커니즘**이다
([`id:chunk-d0003`](../chunks/decision/d-0003-plane-by-verification.md)).

plane은 **일곱**이다. v3에서 `requirement`가 추가됐다.

원본: [`p5-plane-by-verification`](../kb/dev/decision/p5-plane-by-verification/conclusion.md) · [`p7-dev-plane-substance`](../kb/dev/decision/p7-dev-plane-substance/conclusion.md).

| plane | 판정 방식 | 변경률 | 개발 프로파일의 실체 |
|---|---|---|---|
| `requirement` | 이해관계자 확인 (EARS 형식 + 유저 승인) | 매우 낮음 | 요구사항 문장 |
| `decision` | 논증의 타당성 (논박 가능, 기계 판정 불가 → 유저 승인) | 낮음 | 설계 결정·아키텍처 문서 |
| `schema` | 스키마·호환성 검사 | 낮음 | 데이터 프로토콜·스키마 |
| `contract` | 형식 검사 (결정론적) | 중간 | 인터페이스·타입 시그니처 |
| `artifact` | 실행·실측 | 빠름 | 소스코드 |
| `annotation` | 사회적 합의 (해소/승인) | 매우 높음 | 주석·리뷰 코멘트 |
| `memory` | 없음 (휘발성) | 매우 빠름 | 에이전트 작업 메모리 |

plane은 `agt:Chunk`의 **하위 클래스**이고 level은 **속성**(`agt:hasLevel`)이다. plane마다
다른 shape을 붙이기 위해서이고, 같은 항목이 level을 바꾸는 일은 없기 때문이다. 전이는 새
chunk + `refines`로 한다 ([`id:chunk-d0071`](../chunks/decision/d-0071-plane-class-level-property.md)).

**plane 추가의 유일한 근거는 판정 방식이 기존 어디와도 다를 때다.** 같으면 하위 클래스로
둔다. 영향은 단방향이며 순서 기준은 변화 속도다. 순서는
`requirement → decision → contract/schema → artifact → annotation → memory`다. 무효화도 이
순서로만 전파되므로 파급이 유계가 된다 (노트 5.2절).

## §4. traceability — 인터페이스를 기준축으로 한 mapping

각 종류의 **인터페이스를 기준축**으로 plane 간 항목을 잇는다. 링크의 양 끝은 파일이 아니라
chunk·복합체의 IRI이고, 링크는 산출물 밖(`-kg`)에 한 방향만 저장한다. 역방향은 질의로 얻는다
([p10-link-types](../kb/dev/decision/p10-link-types/conclusion.md) · [p10-link-storage-and-anchors](../kb/dev/decision/p10-link-storage-and-anchors/conclusion.md)).

링크 타입은 세 족과 구성 관계로 정렬된다 (`kb/ontology/related/trace/`).

원본: [`p10-link-families`](../kb/dev/decision/p10-link-families/conclusion.md).

| 족 | 뜻 | 잎 | 전파 |
|---|---|---|---|
| `agt:references` | 본문이 식별자로 가리킴 | `cites` · `targets` · `usesDefinition`(2026-09-30 — 정의 → 같은 모듈의 정의, 추출기가 AST 의 최상위 이름 참조에서 낸다) | 대상 변경 → 출발점 `suspect` |
| `agt:semanticallyDependsOn` | 빼면 의미상 불완전 | `refines` · `satisfies` · `constrains` · `verifies` · `derivesFrom` · `usesConcept` · `assumes` · `generates` · `allocates` | 같음. plane 단방향 안에서만 |
| `agt:relatedTo` | 참조·의미 의존 어느 족에도 들지 않는 관련성 | `coUpdatesWith` · `conflictsWith` · `overlapsWith`(2026-09-26 — 가장 약한 잎, 이름 없는 관련성의 자리) | 대칭 — 양쪽 `suspect` |
| (구성 관계) | 함께 읽힘·순서 | `hasDirectPart` | 부분이 무효면 전체 `suspect` |

**링크 어휘의 확장 규칙**(유저 승인 2026-09-23, 링크 견고성 E). 새 관계는 위 세 족 가운데 하나의 **잎으로만** 더한다.
족을 새로 만들지 않는다. 잎은 `rdfs:subPropertyOf`로 족에 속하고, 게이트가 부모 트리플을 함께 생성하므로 족 단위 질의는
새 잎을 자동으로 본다. 잎의 이름은 추적성 관계 분류(`docs/references.md` §추적성)에서 가져오고 지어내지 않는다 —
`overlapsWith`가 그 예다. 후보 생성기가 추적 매트릭스에 칸이 없는 쌍을 만나면 `relatedTo`가 아니라 `overlapsWith`로
낸다. 인용은 겹침의 표지이고 칸 없는 참조는 참조 링크로 확정되지 않는다. 칸이 생기면 그 잎으로 올린다.

frontmatter 링크 키는 두 무리다. Bazel `deps`가 되는 넷(`refines`·`serves`·`supersedes`·`verifies`)과 그래프 트리플과
링크 개체만 되는 나머지(`satisfies`·`constrains`·`derivesFrom`·`allocates`·`generates`·`overlapsWith`)다. 대칭 속성은
`deps`가 되면 순환이 생기므로 둘째 무리에만 든다.

`allocates`는 요구→구성요소 할당이고 `generates`는 산출 의존이며, 둘은 v3 9장에서 추가됐다 (유저 결정
C7). `serves ⊑ refines`는 결정 → 요구·관심사의 링크이며 v4 6.8·7.3의 기여 명시다. `supersedes`는
시간축이라 세 족 밖이다. **링크는 개체다**(`agt:Link`). 링크는 양 끝·타입·**조건**·**증거 기록**을
갖는다. 조건은 `when`이며 ODD 속성·가정 위의 CEL이다. 증거 기록은 `agt:Evidence`이며 종류·참조·극성
±를 가진 항목 목록이다. 확정 전 후보는 `agt:CandidateLink`, 판정된 것은 `agt:ConfirmedLink`다.
상태(`candidate`/`confirmed`/`suspect`/`invalid`)는 저장값이 아니라 **조건 평가와 증거 기록 규칙의
결과**다. **수치 신뢰도는 없다.** 선호는 지지 증거의 종류 서열에서 파생된다. 서열은
구축 > 실행 > 동시 편집 > 공동 커버 > 임베딩 > 세션 > 제안이다. `assumes`와 스코프 conditional은
`when`의 특수형이다. 증거 기록 규칙 둘은 verify 질의다. 하나는 구축(+)·실행(+) 없는 확정이고, 다른
하나는 (−)가 있는 확정이다 (`tools/verify-queries/`). (노트 9.11절, 2026-09-10)

조회 알고리즘은 앵커 → 이웃 확장 → 우선순위 → 예산 패킹이며 [`p0-workset-anchor-neighbourhood`](../kb/dev/decision/p0-workset-anchor-neighbourhood/conclusion.md)에 있다.
복원 경로는 [`p10-link-by-construction`](../kb/dev/decision/p10-link-by-construction/conclusion.md)·[`p9-candidate-generation-limits`](../kb/dev/decision/p9-candidate-generation-limits/conclusion.md)에 있다.
LEDGER·LARGER 대응표 원안은 출처 문서 `id:doc-dependency-graph-design`(2026-09-04, 반영 완료 2026-09-12 — 위치는 `kg/base-kg.ttl`의 `prov:atLocation`)에 있다.
**어휘는 갖춰졌고 링크 개체는 전부 구축 기록 증거를 갖는다(수는 `bazel build //kg:metrics` 3단계 절이 낸다 — 2026-09-11의 472는 2026-10-01에 1,277이었다).**

## §5. knowledge graph — 무엇을 담는가

원본: [`pe-kg-hand-and-generated-files`](../kb/dev/decision/pe-kg-hand-and-generated-files/conclusion.md) · [`pe-odd-is-openodd`](../kb/dev/decision/pe-odd-is-openodd/conclusion.md) · [`p9-candidate-storage`](../kb/dev/decision/p9-candidate-storage/conclusion.md).

| 담는 것 | 위치 | 손/생성 |
|---|---|---|
| chunk head | `bazel-bin/kg/chunks-kg.ttl` | **생성** |
| 복합체 | `kg/composite-kg.ttl` | 손 |
| 가정·출처 문서 | `kg/base-kg.ttl` | 손 |
| 역할·스코프·채널·하네스 (입력) | `kg/catalog-kg.ttl` | 손 |
| 조건과 ODD | `kb/odd/project-odd.yml` (OpenODD YAML 매핑: `TAXONOMY`·`MODULES`·`INCLUDE_AND`…; 확장 키 `ATTRIBUTES`·`LITERALS`·`CHECKS`·`EXCLUSIONS_REVIEWED`) → 생성 `project-odd.ttl`·`taxonomy.yml` | YAML 손, TTL 생성 |
| 후보 링크 | `kb/dev/**/*.space.md` (`type: agt:Space`, 변수 하나 = 파일 하나) | 미구현 |

### ODD

프로젝트당 하나이며, 스코프·가정·시나리오·커버리지의 **분모**다. 조건은 정적 요소·환경
조건·동적 요소 3분류이고 각각 값 또는 범위, 객관적 판정 방법, 등급 A~D를 갖는다. 판정
불가(D)는 ODD에 넣지 않는다 ([p3-odd-derivations-and-gate](../kb/dev/decision/p3-odd-derivations-and-gate/conclusion.md) · [p3-odd-required-sections](../kb/dev/decision/p3-odd-required-sections/conclusion.md) · [p3-measurement-method-grades](../kb/dev/decision/p3-measurement-method-grades/conclusion.md)).

### 가정

모든 chunk는 ODD 조건 위의 가정 위에 선다. **ODD에 없는 조건을 참조하는 파생물은 게이트가
거부한다.** 대응은 ODD 확장 또는 파생물 기각뿐이다. 가정이 깨지면 그 가정에 의존하는
항목이 자동으로 무효화 표시되므로 전수조사가 필요 없다 ([p6-assumption-invalidation](../kb/dev/decision/p6-assumption-invalidation/conclusion.md) · [p0-odd-scope-assumption](../kb/dev/decision/p0-odd-scope-assumption/conclusion.md) · [p6-assumption-verification-methods](../kb/dev/decision/p6-assumption-verification-methods/conclusion.md)).

**기본 가정 후 좁힘**(2026-09-12)이 규칙이다. 항목 고유의 전제를 아직 적지 않은 청크는 기본 가정
`id:asm-chunk-conventions`를 `assumes`한다. 이 기본 가정은 저장소 구조 + 언어 정책 조건이다. 이것은
자리표시이며, 항목의 실제 전제가 드러나면 그 고유 가정을 **앞에 더한다**. 예를 들어 Bazel 하네스에 기대는
결정의 고유 전제는 `asm-bazel-toolchain`이다. 기본 가정은 항목이 청크 규약에도 기대는 한 남는다. 좁힘의 진행은
고유 가정을 가진 청크 수로 잰다 — `metrics`의 가정 절(2026-09-14 정정).

### level — 정제 수준과 수준 허용표

v3가 level을 **정제 수준**으로 재정의했다 (노트 6.4절). 다섯 수준은 `functional`(요구만 있는 높이) ·
`abstract`(형식 문장, 도메인 없음) · `logical`(후보와 제약) · `concrete`(확정된 개체) ·
`executable`(동작만 남은 높이)이다. 다섯 단계를 유지하며 건너뛰지 않는다.

**모든 plane이 모든 level에 살지 않는다.** plane×level 수준 허용표가 SHACL로 강제된다
(`kb/ontology/shapes/residency-shapes.ttl`).

원본: [`p6-plane-level-occupancy`](../kb/dev/decision/p6-plane-level-occupancy/conclusion.md).

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
dcterms·co·obo) 안이어야 한다. prov·skos 용어는 W3C 원문에 실재해야 한다. 원문은 `MODULE.bazel`의
`http_file`로 해시 고정한 `@prov_o`·`@skos`다. 게이트가 원문과 대조한다 (2026-09-12). `agt:` 접두어인데
온톨로지에 없으면 오타 또는 무단 어휘 생성이고, 등록되지 않은 네임스페이스면 어휘 우회다. 둘을 다른
메시지로 구분해 보고한다 ([p0-agt-namespace](../kb/dev/decision/p0-agt-namespace/conclusion.md)). 목록의 단일 정의처는 `tools/kb_lib.py`다.

### 개체 IRI 접두사

원본: [`p0-entity-iri-forms`](../kb/dev/decision/p0-entity-iri-forms/conclusion.md) · [`p0-iri-design`](../kb/dev/decision/p0-iri-design/conclusion.md).

| 종류 | 형식 | 사는 곳 |
|---|---|---|
| chunk (v3 이후) | `id/chunk/<uuid4>` — 불투명 영속 IRI | (생성) `chunks-kg.ttl` |
| chunk (v1 잔류) | `id:chunk-d<번호>`. 새로 만들지 않는다 | `supersedes` 대상으로만 남는다 |
| 복합체 (v3 이후) | `id/composite/<uuid4>` | (생성) 또는 `composite-kg.ttl` |
| 가정 · 출처 문서 | `asm-` · `doc-` | `base-kg.ttl` |
| 복합체 (손) | `comp-` | `composite-kg.ttl` |
| ODD · 조건 | `odd-` · `cond-` | `project-odd.ttl` |
| 하네스 · 역할 · 스코프 · 채널 | `h-` · `role-` · `scope-` · `chan-` | `catalog-kg.ttl` |
| 시나리오 | `scn-` | (아직 없음) |
| 게이트 | `gate-` | (생성) `bazel-bin/kg/gates-kg.ttl` — 원본은 `defs/kb.bzl`의 `GATES`, 손으로 쓰지 않는다 (2026-10-02) |
| 뷰 · skill (투영) | `view-` · `skill-` | (생성) `bazel-bin/kg/projections-kg.ttl` — 원본은 `defs/kb.bzl`의 `VIEWS`와 `tools/kb_lib.py`의 `SKILLS`, `prov:wasDerivedFrom`이 원본 코드 청크를 가리킨다. 층이 없다(Q9-a, 2026-10-03) |
| 실행 기록 | `id/chunk/<uuid4>` — memory 청크(`kb/vv/run/run-<시각>.md`, `process:vv_run`) | (생성) `chunks-kg.ttl` |

IRI는 불투명하게 유지한다. 라벨이나 경로가 바뀌어도 IRI가 유지되어야 시간 정체성이
성립한다. 그래서 v3부터 uuid다 (유저 결정 Q1). 사람이 읽는 이름은 IRI가 아니라
`rdfs:label`이고, 내용 버전은 `agt:contentHash`다.

### 정규화 직렬화

기계가 만든 TTL은 커밋 전 정규형으로 바꾼다. 손으로 쓰는 TTL(`kg/*-kg.ttl`·온톨로지·shape)은 STYLEGUIDE §1·§5의
서식(배너·주석·술어 순서)이 원본이라 정규형 검사 대상이 아니다(2026-09-13 판정). 정규형은 정렬된 `@prefix` + 주어·술어·목적어 정렬이다.
직렬화 순서가 불안정하면 git diff가 의미 없는 변경으로 오염되고, 그것이 무효화 판정의
입력을 더럽힌다 ([p2-ontology-compiler-three-tiers](../kb/dev/decision/p2-ontology-compiler-three-tiers/conclusion.md)).

```bash
bazel run //tools:canonicalize -- --write <files>
```

## §6. 그래프 안과 밖

검사 대상인 지식(`kb/{ontology,odd,dev,vv}/`·`kg/`·`chunks/`)과, 대상이 아닌 문서
(`docs/`·`.claude/`)를 가른다. 소통 기록과 지식을 섞으면 통제 어휘 검사가 무의미해진다.
문서는 결정을 복사하지 않고 **IRI로 인용**한다. 복사하면 이중 관리가 되고 둘이 어긋나는
순간 어느 쪽이 원본인지 알 수 없어진다 ([p4-projection-as-query](../kb/dev/decision/p4-projection-as-query/conclusion.md)).

## §7. development 규칙 — 개발 KB (노트 7.2~7.7)

개발 KB는 요구 명세에서 실산출물을 생산하기 위한 지식이다
([`p7-dev-kb-purpose`](../kb/dev/decision/p7-dev-kb-purpose/conclusion.md)). 코어 규칙 위에 다음이 더해진다.

**코드는 청크로 올라오고 방향은 추출이다**(유저 승인 2026-09-30, [`p7-code-extraction-direction`](../kb/dev/decision/p7-code-extraction-direction/conclusion.md)).
소스 파일 하나가 패키지 하나(`kb/dev/artifact/<모듈>/`)이고 청크 전부가 `bazel run //tools:extract -- <소스>`의 생성물이다 —
손으로 고치면 `//:extract_drift_test`가 거부한다. 정체성의 원본은 소스 옆 사이드카 등록부 `<소스>.chunks.yml`의 `한정 이름 →
uuid`이고 신설만 자동이다 — 개명·삭제는 등록부 편집이다([`p10-function-identity-registry`](../kb/dev/decision/p10-function-identity-registry/conclusion.md)).
링크는 파일 복합체가 갖는다([`p7-code-links-on-file-composite`](../kb/dev/decision/p7-code-links-on-file-composite/conclusion.md)) — 등록부의
`refines`를 추출기가 파일 청크와 절 청크로 옮기고 정의 청크는 `part_of`만 갖는다. `serves`는 정의역이 `agt:DecisionChunk`이므로
`artifact` 청크가 요구를 직접 `serves`하지 않는다 — 결정을 `refines`하고 그 결정이 요구에 닿는다. `artifact`의 `verified`는
테스트 통과 도장이다(`STYLEGUIDE.md` §4).

**정의 사이의 호출은 `usesDefinition`으로 올라온다**(유저 답 2026-09-30). 정의 청크의
선택 키 `uses`가 같은 모듈의 최상위 정의를 가리키고 추출기가 AST의 이름 참조에서 낸다 — `references` 족의 잎이라 Bazel `deps`도
링크 개체도 아니고 링크는 그대로 파일 복합체의 것이다. 방출의 경계는 `defs/kb.bzl`의 `EXTRACTED_SOURCES`(단일 정의처 — `RESIDENCY`와 같은 해법, 2026-10-01)이고 37 파일 전부이며
실측 트리플 476이다. `BUILD.bazel`은 그 리터럴을 load하고 `kb_lib.load_extracted_sources`가 `ast.literal_eval`로 읽어 `uses`
방출 경계를 파생한다 — 상수를 둘로 두지 않는다. `tools/BUILD.bazel`의 `check_extracted_sources`가 등록부 사이드카의 집합과
그 목록이 같은지 로드 시점에 강제해 갈리면 bazel 명령이 바로 fail한다. **치역 경계는 선언이다**(유저 답 1, 2026-10-01). `uses`의 치역은 같은 모듈의 최상위 정의와 `defs/kb.bzl`의 `USES_TARGETS`가 선언한
모듈의 최상위 정의다 — 표본 쌍은 `kb_lib` 하나이고 넓히기는 그 리터럴에 이름을 더하는 것이다. 모듈 밖 해소는 최상위 import와
정의 안의 늦은 import가 묶은 이름을 보고 `kb_lib.<이름>`(별칭 포함)과 `from kb_lib import <이름>`의 `Load` 참조를 대상 모듈
등록부의 uuid로 푼다. 실측 `agt:usesDefinition` 667(모듈 안 484 · 모듈 간 183, 치역은 전부 `kb_lib`), 오탐 0 · 누락 0(표본 30 +
독립 대조). 채널이 든 사례(`pct`)는 이제 **호출부 12**로 잡힌다. **남은 사각지대는 셋이다** — ① 치역 경계 밖의 모듈(전부로
넓히면 +52, 그 대부분이 `chunk2kg` 43) ② 함수를 인자로 넘기는 간접 호출(17 표현식 — 넘기는 쪽은 잡히고 받는 쪽은 아니다)
③ 정의가 아닌 이름(상수·모듈 변수)을 쓰는 관계 — 정의 청크가 없어 어느 경계에서도 올라오지 않는다. 표본 `tools/kb_lib.py`(청크 100·복합체 25)의 churn 실측(uuid 정체성 성립)을 근거로 같은 날 `tools/*.py` 전부로 넓혔다 — **37 파일 전부** · 청크 624 · 복합체 184, 파일마다 드리프트 테스트 `//:extract_drift_<모듈>`(묶음 `//:extract_drift_test`). 절 주석은 최소 하나다(파일 복합체의 부분이 둘 이상). 클래스는 정의 청크 하나이고 실측 최대 85줄이다. 200줄을 넘던 `main` 둘(`consistency`·`metrics`)은 상한을 올리지 않고 나눴다 — 산출물 바이트 동일.

| 규칙 | 내용 | 결정 |
|---|---|---|
| `requirement` | functional 전용. EARS 다섯 패턴, 이해관계자·관심사 필수 | [`p7-dev-plane-substance`](../kb/dev/decision/p7-dev-plane-substance/conclusion.md) |
| 결정 복합체 | 항상 결론·근거·대안 세 청크. **대안 청크 없는 결정 = shape 위반**, "대안 없었음"도 기록 | [`p7-alternatives-mandatory`](../kb/dev/decision/p7-alternatives-mandatory/conclusion.md) |
| 결정의 수준 | abstract(변수)·logical(후보·제약·배제)·concrete(값)는 별개 청크, `refines`로 연결. concrete가 생겨야 확정. abstract 청크는 `-space`가 있을 때만 | [`p7-decision-spans-three-levels`](../kb/dev/decision/p7-decision-spans-three-levels/conclusion.md) |
| 기여 | abstract 결정은 `serves`(⊑ `refines`)로 어느 요구의 어느 관심사에 기여하는지 명시. 없으면 거부 | [`p6-transition-gates`](../kb/dev/decision/p6-transition-gates/conclusion.md) |
| 계약 우선 | `contract` abstract가 구현보다 먼저. 계약 없는 구현 = 정제 단절. 계약 logical(사후조건)이 V&V 기준의 재료 | [`p7-contract-first`](../kb/dev/decision/p7-contract-first/conclusion.md) |
| 스키마 | `decision`에서 `derives-from`, `contract`를 `constrains`. 비호환 변경 = 새 IRI + `supersedes` | [`p7-schema-derivation`](../kb/dev/decision/p7-schema-derivation/conclusion.md) |
| `artifact` | 구현만. verifier는 V&V KB | [`p6-executable-splits-by-kb`](../kb/dev/decision/p6-executable-splits-by-kb/conclusion.md) |
| 구현 착수 | developer는 concrete 결정·확정 스키마 없이 구현 불가(스코프 conditional). developer 작업 집합에 `-space` 없음 | [`p7-developer-requires-concrete`](../kb/dev/decision/p7-developer-requires-concrete/conclusion.md) |
| 대체 | 결정 대체는 `supersedes`. 옛 결정은 `deprecated`, 그 `satisfies` 전부 `suspect` | [`p7-decision-supersession`](../kb/dev/decision/p7-decision-supersession/conclusion.md) |
| 완료 | 연쇄 완주 · 계약 선행 · 대안 존재 · 가정 `stable` · **V&V `verifies` 유효** — 개발 KB만으로 완료 선언 불가 | [`p7-dev-kb-completion`](../kb/dev/decision/p7-dev-kb-completion/conclusion.md) |
| 역할 | design(요구·결정·계약·스키마·ODD) / developer(`artifact`) / orchestrator(dispatch 결정) / V&V(`annotation`만) | [`p7-dev-roles-and-scopes`](../kb/dev/decision/p7-dev-roles-and-scopes/conclusion.md) |

이 저장소의 실측(2026-09-10)은 `requirement` 33 · `decision` 182(대안 182/182) · `contract`·`schema`·`artifact` 0이다.

## §8. V&V 규칙 — V&V KB (노트 8.2~8.5, 8.11~8.15, 8.4, 9.11)

V&V KB는 코어의 두 번째 인스턴스다. 새 plane을 만들지 않고 실체만 다르다
([`p8-vv-plane-instances`](../kb/dev/decision/p8-vv-plane-instances/conclusion.md)).

| 규칙 | 내용 | 결정 |
|---|---|---|
| 독립성 | 개발 역할은 V&V KB 쓰기 불가. 기준 수정은 요구 수정으로만. 저장 분리(`kb/vv/`), V&V → 개발 단방향 의존 | [`p8-vv-independence-scope`](../kb/dev/decision/p8-vv-independence-scope/conclusion.md) |
| 검증 대응물 필수 | f→a에 검증 목표 / l→c에 합격 기준 / c→e에 검증기. 없으면 개발 게이트 실패(7단계 전엔 경고) | [`p8-scenario-ladder-rungs`](../kb/dev/decision/p8-scenario-ladder-rungs/conclusion.md) |
| `verifies` | KB를 가로지르는 유일한 링크. 방향은 V&V → 개발, 같은 level끼리 | [`p6-executable-splits-by-kb`](../kb/dev/decision/p6-executable-splits-by-kb/conclusion.md) |
| 시나리오 | `decision`(vv) 복합체 — 자극·요인·배제 자극. 변수는 ODD 속성만, ODD 밖은 `odd:outside`로 커버리지 제외. 세 청크의 파일 이름은 `<슬러그>-stimulus.md`·`<슬러그>-factors.md`·`<슬러그>-excluded.md`이고 역할 표지 **자극**·**요인**·**배제 자극**이 결정의 결론·근거·대안 슬롯에 사상되며 선언 청크는 `-stimulus`, `ordered`는 필수다(게이트 `decision-role`·`shacl`, 2026-09-29). 접미 판정은 `kb/vv/scenario/`에서만 걸린다 — 옛 결정에 stem이 `-factors`로 끝나는 것이 있다. 단일 청크 시나리오는 이행 기간 동안 **결론** 표지로 통과한다 | [`p8-scenario-authoring`](../kb/dev/decision/p8-scenario-authoring/conclusion.md) |
| 판정 로그 | 판정 로그는 실행 기록이다 — `kb/vv/run/judge-<시각>.md`에 append-only로 쌓이고 생성자는 `process:judge`다(역할이 아니므로 writer 검사 밖). 판정 표의 열이 곧 필수 필드다: 질문 id·값·확신도·**판정자 식별자**(세션·모델 — 외부 서비스가 아니다, 2026-09-30)·입력 지문(보낸 바이트의 sha256)·시각. 열 `일치`(일치·불일치·해당 없음)는 판정자 둘 이상이 같은 (질문·지문)에 답했을 때만 뜻을 갖는다. 확신도는 **자기 보고**라 개별 답을 보증하지 않고 단독 응답으로는 자동 적용이 없다. 결과 주석의 `본문:`은 판정자가 쓰지 못하므로 `해당 없음`이다. 게이트 `judge-log`(`chunk_lint`) — **로그가 0건이면 검사 대상이 없어 PASS** | [`p8-judge-session-agreement`](../kb/dev/decision/p8-judge-session-agreement/conclusion.md) |
| 기계 환원 | 요약(`핵심:` 항목의 지지 참조)은 게이트 `summary-support`(`chunk_lint`, 오탐 0/0 실측 — 슬롯 사용 0)로 확정된다. 중복·자리는 `consistency.py` ⑩·⑪이 후보만 내고 확정은 판정자(사람 또는 세션 판정자) 몫이다 | [`p8-judge-session-agreement`](../kb/dev/decision/p8-judge-session-agreement/conclusion.md) |
| 위험 분석의 어휘 | 현상은 `defect` 모듈(`kb/ontology/related/defect/`)의 요인 개체다. 하위 유형 14는 인지·상호작용·실행 세 갈래 아래 ODC 유형이고, 피해는 ODC 영향 차원 다섯(`agt:DefectImpact`)이며 "지식 유실·재생산"은 H1 하위다. 현상 개체는 정의·표기(P번호)·관측 수단·출처를 갖는다(게이트 `shacl`, `defect-factor-shapes`). 위험 지표 S·노출·탐지가능성은 순서 척도이고 **곱하지 않는다** — 등급은 정렬용이고 합격 기준은 케이스가 정한다. 탐지가능성 D는 현상 개체의 `agt:observationMeans`가 갈리는 세 꼴에서 도출된다 — 게이트 이름은 D1, 생성 보고서가 수치로 내되 진행을 막지 않는 것은 D2, `미확정`은 D3다. 값의 원본은 `defect-rules/risk-grade-rules.ttl`이고 수를 여기 적지 않는다(2026-10-01 — 관측 수단 다섯이 서서 D3가 둘로 줄었다). `미확정`을 유지하는 현상은 그 까닭을 정의문에 적는다 — 관측 수단 자리에 산문을 덧붙이지 않는 것이 세 빈 값 규칙이다. 규칙성 가정 A1~A3(`id:asm-links-only-interaction`·`asm-finite-factor-types`·`asm-missing-vocabulary-is-signal`)은 프로파일에서 파생되는 항목이 `assumes`로 참조한다(2026-09-29). 현상 → 피해 인과는 `defect-rules` 모듈의 `agt:hasImpact` 트리플(첫 형태 28건 = 질문지의 피해 열)이다 — 어휘(`defect`)와 형식화(`defect-rules`)를 나눈 이유는 어휘가 안정적이고 규칙이 자주 바뀌므로 어휘 사용자가 규칙 변경에 영향받지 않아야 한다는 것이다(노트 2.3절 (b)) | [`p8-odc-defect-subtypes`](../kb/dev/decision/p8-odc-defect-subtypes/conclusion.md) · [`p8-risk-analysis-profile`](../kb/dev/decision/p8-risk-analysis-profile/conclusion.md) |
| 기준 ≠ 자극 | 기준은 `contract`(vv) 별도 청크, `verifies` 속성으로 바인딩. 판정식 없는 기준은 abstract로 강등 | [`p8-pass-criteria`](../kb/dev/decision/p8-pass-criteria/conclusion.md) |
| 케이스 | concrete 케이스는 사람이 쓰지 않는다 — `keep`+`cover`에서 생성. 표본 근거 없는 케이스 거부 | [`p8-case-generation`](../kb/dev/decision/p8-case-generation/conclusion.md) |
| 역할 | 검증기 저자 ≠ V&V engineer (또는 다른 세션). audit은 쓰기 없음 | [`p8-vv-roles`](../kb/dev/decision/p8-vv-roles/conclusion.md) |
| 재현성 | 재현 불가 → 5~6단계 강등. 6단계 관측은 커버리지에 넣지 않음 | [`p8-reproducibility`](../kb/dev/decision/p8-reproducibility/conclusion.md) |
| 학습된 판정자 | 정확도·판별력·캘리브레이션 3지표 + 사람 승인. 결과는 head `verified` 목록에 | [`p8-learned-environment-and-judge`](../kb/dev/decision/p8-learned-environment-and-judge/conclusion.md) |
| 평가의 목적지 | 확인 결과는 `requirement`로 — 요구가 바뀌는 유일한 정규 경로 | [`p8-verification-and-validation`](../kb/dev/decision/p8-verification-and-validation/conclusion.md) |
| 불일치의 귀속 | 산출물 / 지식(요구 과도·제약 부족·가정 누락) / 둘 다는 **결정**이며 V&V `decision`의 지침. 진단은 기호 도구 먼저 | [`p8-mismatch-attribution`](../kb/dev/decision/p8-mismatch-attribution/conclusion.md) |
| 실행 증거 | 검증기 결과는 개발 KB `satisfies` 후보의 증거 기록에 (+)(−)로 — 링크가 아니라 증거 기록 항목이라 방향 규칙 유지 | [`p9-evidence-ledger`](../kb/dev/decision/p9-evidence-ledger/conclusion.md) |

이 저장소의 실측(2026-09-10)에서 `kb/vv/`는 비어 있다. 이 저장소 자신의 검증 목표·시나리오·기준이 없다 (도입 7단계).

<!-- 인용 끝 -->

## 입력 파일

원본 파일 71개다. 디렉토리로 묶었고 빠진 파일은 없다.

- `kb/dev/decision/p0-entity-iri-forms/` — `conventions.md`
- `kb/dev/decision/p0-service-is-a-three-layer-wiki/` — `conventions.md`
- `kb/dev/decision/p10-link-families/` — `conventions.md`
- `kb/dev/decision/p2-trust-tier-from-generated-and-verified/` — `conventions.md`
- `kb/dev/decision/p4-chunk-as-four-named-graphs/` — `conventions.md`
- `kb/dev/decision/p4-chunk-as-ontology-class/` — `conventions.md`
- `kb/dev/decision/p4-chunk-iri-is-the-anchor/` — `conventions.md`
- `kb/dev/decision/p4-chunk-state-machine/` — `conventions.md`
- `kb/dev/decision/p4-composite-as-part-of/` — `conventions.md`
- `kb/dev/decision/p4-composition-rules/` — `conventions.md`
- `kb/dev/decision/p4-label-is-the-interface/` — `conventions.md`
- `kb/dev/decision/p5-plane-by-verification/` — `conventions.md`
- `kb/dev/decision/p6-executable-splits-by-kb/` — `conventions.md`
- `kb/dev/decision/p6-plane-level-occupancy/` — `conventions.md`
- `kb/dev/decision/p6-transition-gates/` — `conventions.md`
- `kb/dev/decision/p7-alternatives-mandatory/` — `conventions.md`
- `kb/dev/decision/p7-contract-first/` — `conventions.md`
- `kb/dev/decision/p7-decision-spans-three-levels/` — `conventions.md`
- `kb/dev/decision/p7-decision-supersession/` — `conventions.md`
- `kb/dev/decision/p7-dev-kb-completion/` — `conventions.md`
- `kb/dev/decision/p7-dev-plane-substance/` — `conventions.md`
- `kb/dev/decision/p7-dev-roles-and-scopes/` — `conventions.md`
- `kb/dev/decision/p7-developer-requires-concrete/` — `conventions.md`
- `kb/dev/decision/p7-schema-derivation/` — `conventions.md`
- `kb/dev/decision/p8-case-generation/` — `conventions.md`
- `kb/dev/decision/p8-judge-session-agreement/` — `conventions.md`
- `kb/dev/decision/p8-learned-environment-and-judge/` — `conventions.md`
- `kb/dev/decision/p8-mismatch-attribution/` — `conventions.md`
- `kb/dev/decision/p8-odc-defect-subtypes/` — `conventions.md`
- `kb/dev/decision/p8-pass-criteria/` — `conventions.md`
- `kb/dev/decision/p8-reproducibility/` — `conventions.md`
- `kb/dev/decision/p8-scenario-authoring/` — `conventions.md`
- `kb/dev/decision/p8-scenario-ladder-rungs/` — `conventions.md`
- `kb/dev/decision/p8-verification-and-validation/` — `conventions.md`
- `kb/dev/decision/p8-vv-independence-scope/` — `conventions.md`
- `kb/dev/decision/p8-vv-roles/` — `conventions.md`
- `kb/dev/decision/p9-candidate-storage/` — `conventions.md`
- `kb/dev/decision/p9-evidence-ledger/` — `conventions.md`
- `kb/dev/decision/pe-kg-hand-and-generated-files/` — `conventions.md`
- `kb/dev/decision/pe-odd-is-openodd/` — `conventions.md`
- `kb/dev/norm/rules/` — `assumption.md` · `canonical-serialization.md` · `chunk-naming.md` · `chunk.md` · `composite-order.md` · `composite-scope.md` · `composite.md` · `controlled-vocabulary.md` · `development-code-calls.md` · `development-measure.md` · `development.md` · `file-format-empty-values.md` · `file-format-two-kbs.md` · `file-format-vocabulary.md` · `file-format.md` · `graph-boundary.md` · `head.md` · `iri-prefixes-identity.md` · `iri-prefixes.md` · `knowledge-graph.md` · `level.md` · `link-objects.md` · `link-vocabulary.md` · `odd.md` · `plane-subclass.md` · `plane.md` · `traceability.md` · `trust-tier-gates.md` · `trust-tier.md` · `vv-measure.md` · `vv.md`

