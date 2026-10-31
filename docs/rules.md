# rules.md — 무엇이 유효한 지식 구조인가 (생성 파일)

- 생성기: `tools/gen_norms.py` · gendoc/1
- 입력: 원본 파일 71개 · 절 30 · 규약 줄 80 · 전체 목록은 [입력 파일](#입력-파일)
- 질의: `kb/dev/norm/rules/` 의 절 항목을 선언 순서로 펼치고 항목마다 결정의 `규약:` 줄을 싣는다
- 재현: `python3 tools/gen_norms.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 `kb/dev/norm/rules/` 의 절 항목과 결정의 `conventions.md`이다. 검사: `//:norms_drift_test`. 생성 시각·입력 해시값은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

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

<!-- 인용 시작: 단위 지식에서 그대로 옮긴 값 — 원본이 자기 게이트를 통과했다 -->

이 문서의 원본은 노트 v5의 Part II, IV, V, VII, VIII, IX, X와 그 재도출 결정이다. 노트는
[`agent-knowledge-system-notes.md`](agent-knowledge-system-notes.md)이고 결정은 `kb/dev/decision/`에 있다.
구조도 v5에 따라 셋으로 적는다. 두 KB에 공통인 **코어**는 §1~§6, **development**는 §7, **V&V**는 §8이다.
**규칙은 이 문서가 적고, 규칙을 수행하는 절차는 [`method.md`](method.md)가, 규칙을 기계로 강제하는 검사 도구는
[`tools.md`](tools.md)가 적는다.** 기계가 판정할 수 없는 규칙은 [`../STYLEGUIDE.md`](../STYLEGUIDE.md)의 `[지킴]`으로 남는다.

## §1. chunk — 자립적 최소 지식 단위

**단위 지식은 형식이 아니라 구조 규칙이다.** 그래서 이 규칙은 마크다운 본문뿐 아니라
온톨로지와 ODD, 설계 공간, 지식그래프 파일에도 같이 적용된다 (유저 결정 2026-09-04).

| 규칙 | 내용 | 근거 |
|---|---|---|
| 크기 | 본문은 **토큰 상한** 이하다. 저작 산문은 42의 26배인 **1,092**이고, 이 값은 예산 5,418의 1/5이라 한 번에 4~5개를 조망한다. `artifact`와 `memory`의 인용은 42의 68배로 한 창인 **2,856**이다. 계수기는 ODD `cond-tokenizer-lock`으로 고정된 `o200k_base`이고, 단일 정의 위치는 `tools/kb_lib.py`의 `BODY_TOKEN_LIMITS`, 그래프 쪽은 `token-budget-shapes.ttl`이다. 그 전에는 42줄·200줄이었고, 줄은 내용에 따라 토큰이 1.9배 갈린다(2026-10-01). | [`p4-chunk-as-ontology-class`](../kb/dev/decision/p4-chunk-as-ontology-class/conclusion.md) · [`p1-chunk-unit-is-tokens`](../kb/dev/decision/p1-chunk-unit-is-tokens/conclusion.md) |
| 층 | 선택 키 `layer: knowledge \| methodology \| process`는 항목이 서비스의 어느 층에서 역할을 갖는가를 나타낸다([p0-service-is-a-three-layer-wiki](../kb/dev/decision/p0-service-is-a-three-layer-wiki/conclusion.md), 2026-10-01). 층은 지식 종류와 직교하므로 type 제한이 없고, 명시가 없으면 `chunk2kg`가 `agt:inLayer agt:knowledgeLayer`를 방출한다. 표시 누락이 산발로 세어지지 않아야 하고 층별 집계(CQ-38)의 분모가 항목 전수여야 하기 때문이다. 코드 단위 지식은 등록부의 `layer`가 원본이다. 값 어휘와 개수는 `layer-shapes`가 본다 | [`p0-service-is-a-three-layer-wiki`](../kb/dev/decision/p0-service-is-a-three-layer-wiki/conclusion.md) |
| 단위 | 단위 지식 하나는 지식 종류 하나와 정제 수준 하나, 주제 하나, **파일 하나**다 | [`p4-chunk-as-ontology-class`](../kb/dev/decision/p4-chunk-as-ontology-class/conclusion.md) · [`p4-plane-subclass-level-property`](../kb/dev/decision/p4-plane-subclass-level-property/conclusion.md) |
| 라벨 | 라벨은 한글과 영어로 하나씩 둔다. 라벨만 보고 본문을 예측할 수 있어야 하며, 이 조건은 검사할 수 없으므로 규약으로 둔다 | [`p4-label-is-the-interface`](../kb/dev/decision/p4-label-is-the-interface/conclusion.md) |
| 상태 | `draft`, `stable`, `suspect`, `invalidated`, `deprecated` 차례로 전이한다. 이 가운데 `draft`와 `stable`, `deprecated`는 OKF `status` 어휘이고 `suspect`·`invalidated`는 무효화를 위한 확장이다. `stable`이 이 결정이 대체한 옛 결정의 `valid`다 | [`p4-chunk-state-machine`](../kb/dev/decision/p4-chunk-state-machine/conclusion.md) |
| 앵커 | 단위 지식 IRI가 앵커다. 산문 계열은 파일 경로로, 코드 계열은 심볼로 해석한다 | [`p4-chunk-iri-is-the-anchor`](../kb/dev/decision/p4-chunk-iri-is-the-anchor/conclusion.md) · [`p10-link-storage-and-anchors`](../kb/dev/decision/p10-link-storage-and-anchors/conclusion.md) |
| 신뢰 등급 | `generated.by`가 필수이고 현재 내용 이후(`at ≥ generated.at`)의 `verified` 항목이 없으면 미검증이다. 그 항목에 `human:` 접두어가 있으면 사람 검토 등급이며, 상세는 §1의 신뢰 등급 절에 있다 | [`p2-trust-tier-from-generated-and-verified`](../kb/dev/decision/p2-trust-tier-from-generated-and-verified/conclusion.md) |
| 네 그래프 | 타입과 지식 종류, 정제 수준, 라벨을 담는 head, 본문을 담고 토큰 상한이 유일하게 적용되는 assertion, provenance, pubinfo | [`p4-chunk-as-four-named-graphs`](../kb/dev/decision/p4-chunk-as-four-named-graphs/conclusion.md) |

**지식의 종류는 "X 단위 지식"이라 부르지 않는다.** 조건, 개념, 변수, 후보, 결정, 가정, 시그니처,
함수, 주석, 관측처럼 고유 용어로 부르고, "단위 지식"이라는 말은 그것들이 따르는 구조 규칙을 가리킬 때만
쓴다 (유저 결정 2026-09-04). 다만 온톨로지 클래스 이름(`agt:DecisionChunk` 등)과 그래프 라벨은 구조 타입의
식별자이므로 인용할 때 그대로 쓴다.

**본문 중복은 안전율로 용인한다** (유저 결정 2026-09-11,
[`p4-redundancy-as-safety-margin`](../kb/dev/decision/p4-redundancy-as-safety-margin/conclusion.md)).
자립성이 맥락의 반복을 요구하므로 같은 서술이 여러 단위 지식에 있는 것은 결함이 아니다. 다만 용인에는
경계가 있어서 **개념, 용어, 라벨과 요구의 중복은 용인하지 않는다.** 이 중복은 어휘 드리프트와
인터페이스 충돌을 낳고 추적 커버리지를 왜곡하기 때문이다. 알고 둔 중복은 `coUpdatesWith`로 묶어 한쪽의
변경이 다른 쪽을 `suspect`로 만들게 한다. 반면 링크 없는 중복은 드리프트다. 정리는 재검증 시점에
일괄로 한다. `consistency` 보고는 커밋마다 내며 중복, 라벨 형식과 용어를 다루고, 병합할지 묶을지 유지할지의
판정은 도입 단계가 끝날 때마다 한다.

### 신뢰 등급 — 누가 만들고 누가 검증했는가

행위자 표기는 OKF의 행위자 규약을 그대로 써서, 도구는 `<생성기>/<버전>`, 사람은 `human:<id>`, 프로세스는
`process:<id>`로 적는다. 신뢰 등급은 저장하지 않고 질의로 얻는다. `verified`가 없으면 등급은 **미검증**이고,
`human:` 없는 검증만 있으면 **기계 확인**, `human:`이 있는 검증이 있으면 **사람 검토**다.

게이트 둘이 이 등급 위에서 검사한다.

원본: [`p2-trust-tier-from-generated-and-verified`](../kb/dev/decision/p2-trust-tier-from-generated-and-verified/conclusion.md).

| 검사 | 강제하는 것 |
|---|---|
| `generatedBy` 필수 | 누가 만들었는지 없는 항목을 만들 수 없다 |
| 가장 늦은 `verifiedAt` ≥ `generatedAtTime` | **검증 뒤에 내용이 바뀌고 재검증 항목이 없으면 FAIL이다.** 사람이 검증한 항목을 에이전트가 고치고 재검증하지 않는 경우를 잡는다 |

요점은 둘째다. "decision은 유저 승인이 `valid` 전이의 조건"이라는 규칙이 지금까지 그래프에
기록되지 않았고, 채널의 `status: approved`는 그래프 밖에 있었다 (`p5-plane-by-verification`). `verified`가 그 둘을 잇고, 그래서
쓰기 대상 지식 종류의 경계가 규약에서 기계 검사로 내려온다.

*2026-09-10에 측정한 현재 상태에서 생성자는 `claude/fable-5`·`claude/opus-5`뿐이고 **사람 검토는 0건**이다.*

### 파일 형식과 head 생성

head 메타데이터는 파일 안의 frontmatter에 있고, `bazel-bin/kg/chunks-kg.ttl`은 거기서 **생성**되므로 손으로
쓰지 않는다. `tokenCount`·`assertionLocation`이 파일에서 계산되므로 어긋날 수 없다.

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

IRI는 uuid로 영속하고, 내용 버전은 `chunk2kg`가 본문의 sha256 앞 12자를
`agt:contentHash`로 계산해 붙인다. 그래서 같은 IRI에서 내용이 바뀌었는지를 해시 비교로
안다 (노트 9.9절, 유저 결정 Q1).

**이 형식은 [OKF v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
번들이다.** 번들은 마크다운과 YAML 프론트매터로 되어 있고, `type`만 필수이며, 소비자는 알 수 없는 키를 견딘다.
`id`, `title_ko`, `level`, `assumes` 등은 확장 키로 남으므로 외부 도구도 이 저장소를 읽을 수 있다
(필드 사상은 [`pe-three-layer-binding`](../kb/dev/decision/pe-three-layer-binding/conclusion.md)).
예약 파일명 `index.md`·`log.md`는 **생성물로만** 두고, 생성 명령은 `bazel build //kb/dev:index`다 (유저 결정 Q4).

**본문의 빈 자리는 세 값으로만 적는다** (유저 승인 2026-09-22, [`p4-three-empty-values`](../kb/dev/decision/p4-three-empty-values/conclusion.md)).
`없음`은 찾아봤고 없다는 뜻, `해당 없음`은 적용되지 않는다는 뜻, `미확정`은 아직 모른다는 뜻이며, 이 셋만 행동이 갈린다.
그래서 `N/A`, `TBD`, `미정`과 단독 대시를 쓰지 않는다. 아직 모르는 것은 선택 슬롯 `미확정:`에 적고, 미결 집계는
문서가 아니라 그 슬롯에서 생성된다. 슬롯에는 그 슬롯의 질문에 답하는 문장만 쓰므로, 다른 슬롯의 답이나 메타
문장, 채움은 첨가다 ([`p4-slot-answers-one-question`](../kb/dev/decision/p4-slot-answers-one-question/conclusion.md)).
순서 목록의 모든 항목은 `1.`로 적고, 항목 9개와 중첩 2단계와 항목당 2줄을 넘지 않는다. 검사는 `consistency` ⑧·⑨
보고에서 시작하고, 수치가 0이 된 뒤 `chunk_lint`로 올린다. 슬롯 표지는 **자리**로 판정한다. 그 줄의 필드 머리, 곧 줄
시작이나 `- ` 다음, ` · ` 다음에 있는 굵은 span만 슬롯이고, 표 셀이나 문장 중간의 굵은 span은 강조다. 한정어는 12자
이하이고 마침표가 없을 때만 같은 표지로 본다. 시나리오 표지를 더하자 옛 단위 지식 32파일에서 60건의 강조가 슬롯으로
방출됐고, 이 규칙으로 그 수가 0이 됐다 (2026-09-29). 표지 낱말의 접두 겹침은 `kb_lib.validate_body_slot_markers`가
로드 시점에 거부한다.

**게이트 id의 단일 정의 위치는 `defs/kb.bzl`의 `GATES`와 `TOOL_TAGS`다.** `GATES`는 id마다 실행 계층, 판정 도구,
한글 라벨과 설명 한 줄을 적고, `TOOL_TAGS`는 게이트가 아닌 입력 문제와 보고 태그를 적는다. 이 단일화는 통일 기획
2단계의 첫 조각이고, 그 전에는 같은 목록이 넷으로 갈려 있었다 (2026-10-02). `kb_lib`이 리터럴 읽기로 `*_GATE`·`*_TAG`를
파생하므로 상수를 손으로 두지 않는다. 게이트는 프로세스 층의 **항목**이고, 그 개체는 `//kg:gates_kg`의 `id:gate-<id>`다.
이 개체는 `agt:Gate`이고 `agt:gateTier`와 판정 도구의 파일 복합체를 가리키는 `agt:enforcedBy`를 가지며, `kg/`에 손으로
쓰지 않는다. 목록이 갈리면 게이트 `gate-registry`가 거부한다. 이 게이트는 코드의 태그가 등록부에 포함되는지, 손 상수가
없는지, 폴백 값이 일치하는지, 등록 id가 코드에 닿는지를 본다.

**값 어휘와 지식 종류별 허용 수준 표의 단일 정의 위치는 `defs/kb.bzl`이다** (2026-09-26·27). `PLANES`, `LEVELS`,
`STATES`, `RESIDENCY`를 거기에만 적고, 파이썬 쪽 도구인 `chunk2kg`와 `kb_lib`는 그 리터럴을 읽어 파생한다. 단위 지식을 파싱하는
모든 액션은 `//defs:kb.bzl`을 입력으로 받는다. 그 액션은 `kb_chunk`와 `kb_decision`의 head 액션, `kb_consistency`,
`kb_weave`, `kb_index`, `//space:design_space`, `//:build_drift_test`이고, `bazel run` 도구는 `BUILD_WORKSPACE_DIRECTORY`로
경로를 푼다. 폴백값은 두지 않는다. 값이 같아도 정의 위치가 둘이면 어느 날 하나만 고쳐지기 때문이다.
shape 파일 `residency-shapes.ttl`은 소스로 남지만, 게이트 `residency`가 원본과의 동일성을 강제한다.

`tools/chunk2kg.py`가 따로 정의하는 것은 지식 종류 이름에서 온톨로지 클래스로 가는 사상인 `PLANE_CLASS`와 필수 키 `REQUIRED`뿐이고, 그 사상의 키 집합이 `defs/kb.bzl`의 `PLANES`와 같은지는 로드할 때 단정한다. 생성 경로에서는 단위 지식
타깃인 `kb_chunk`와 `kb_decision`마다 head 조각을 내고, 그 조각을 패키지의 `:kg` 묶음으로 모은 뒤 `kb_kg_merge` 규칙의 `//kg:chunks_kg`가
합쳐 `bazel-out/.../kg/chunks-kg.ttl`을 만들며, 이 파일이 `//kg:gate_test`의 입력이 된다. 생성물은 `bazel-out`에만
존재하며 소스 트리에 같은 이름의 파일을 두지 않는다.

**지식은 두 KB로 갈려 산다.** 개발 KB `kb/dev/`는 요구와 결정, 계약, 스키마, 구현을 담고, V&V KB
`kb/vv/`는 검증 목표와 시나리오, 판정 기준을 담는다. 두 KB를 잇는 링크는 `verifies` 하나뿐이고 그 주어는
항상 V&V 쪽이며, `kb/vv/`의 편집 주체는 vnv 역할뿐이다 (노트 Part VII, 유저 결정 저장 분리).
v1에서 온 옛 결정 트리는 결정 기록으로 옮긴 뒤 지웠고, 그 파일은 git 역사에 남는다(유저 답 Q113-b).

**네 그래프는 현재 논리적 구분이다.** 저장 형식이 Turtle이므로 물리적으로는 기본 그래프
하나이고, TriG 전환은 `annotation`이 생겨 "어느 그래프에 대한 주석인가"를 말해야 할 때
재검토한다.

## §2. 복합체 — 통합이 필요한 것만

복합체는 **단위 지식의 part-of 묶음**이고, 클래스는 `agt:Composite`다. 복합체에는 본문이 없고 라벨과 순서 있는 부분
목록만 있다. `agt:Composite`는 `agt:Chunk`와 서로소이고, 둘 다 `agt:KnowledgeItem`의 하위 클래스다.

| 규칙 | 내용 | 근거 |
|---|---|---|
| 동질성 | 부분의 지식 종류 클래스가 전체와 같다. 정제 수준도 같아야 하지만 결정 기록은 예외여서 결론은 구체 수준이고 근거와 대안은 논리 수준이다(`p7-decision-spans-three-levels`). 지식 종류나 정제 수준을 넘는 관계는 전부 링크이고, verify 질의 `composite-heterogeneous`가 이를 검사한다 (2026-09-13). | [`p4-composition-rules`](../kb/dev/decision/p4-composition-rules/conclusion.md) |
| 크기 | 직접 부분은 최대 9개다(7±2). 9개를 넘는 묶음은 **중첩**으로 담는다. 선언하는 단위 지식의 `composite.part_of`가 그 복합체를 상위 복합체의 직접 부분으로 만들고, 중첩된 복합체 전부는 한 액션, 곧 한 Bazel 타깃이 뿌리부터 잎까지 받는다(`p4-composite-as-part-of`). 코드 추출이 이 자리를 처음 쓰며, 파일 아래 장·절 복합체를 두고 그 아래 정의 단위 지식을 두는 구조의 원본은 소스의 절 주석인 `# ══ 장`과 `# ── 절`이다. 절 주석이 없어 9를 넘는 파일은 `FAIL [extract]`로 절 주석을 요구하고, 순서에 뜻이 없는 묶음이 되므로 9개씩 자르지 않는다 | [`p4-composition-rules`](../kb/dev/decision/p4-composition-rules/conclusion.md) · [`p7-code-links-on-file-composite`](../kb/dev/decision/p7-code-links-on-file-composite/conclusion.md) |
| 순서 | 순서가 뜻을 갖는 복합체만 `co:List`와 `co:index`로 적는다. 순서의 원본은 **선언**이어서, 선언하는 단위 지식의 `composite:`에 선택 키 `ordered: [<부분 IRI>…]`가 부분 전부를 빠짐없이 한 번씩 담고 있을 때만 생성기가 순서를 낸다. 결정 기록도 예외가 아니어서 생성기가 결론, 근거, 대안의 순서를 `ordered` 인자로 선언한다(유저 답 2026-09-29). 시나리오 복합체는 `ordered`가 필수다. 순서를 요구하지 않는 것에 순서를 붙이면 거짓 정보가 된다 | [`p4-composite-as-part-of`](../kb/dev/decision/p4-composite-as-part-of/conclusion.md) · [`p4-composite-order-is-declared`](../kb/dev/decision/p4-composite-order-is-declared/conclusion.md) |
| 비순환 | `part-of`의 반대칭 공리로 추론된다 | [`p4-composition-rules`](../kb/dev/decision/p4-composition-rules/conclusion.md) |
| 상태 | 부분에서 추론되며, 부분 하나가 `invalidated`면 복합체는 `suspect`다 | [`p4-composition-rules`](../kb/dev/decision/p4-composition-rules/conclusion.md) |

**모든 단위 지식이 복합체에 속할 필요는 없다** (유저 결정 2026-09-02). 통합이 필요한 것만
묶고 나머지는 개별로 두며, 통합의 기준은 둘이다. 첫째는 **함께 읽혀야 이해되는가**로 병합 신호에 해당하고,
둘째는 **순서가 뜻을 갖는가**다 ([p4-chunk-split-and-merge](../kb/dev/decision/p4-chunk-split-and-merge/conclusion.md) · [p4-composite-as-part-of](../kb/dev/decision/p4-composite-as-part-of/conclusion.md)).
셋째 기준인 "무효화가 함께 번져야 하는가"는 복합체가 아니라 `relatedTo` 링크로 표현한다 (§4 링크 타입 표).
복합체 **후보**는 커뮤니티 탐지가 제안하고 채택은 사람이 한다 ([`p4-community-detection-proposes-composites`](../kb/dev/decision/p4-community-detection-proposes-composites/conclusion.md)).

**결정은 단위 지식 셋으로 된 복합체다** (노트 4.7절·7.4절, 유저 결정 C2). 결론은 구체 수준인 `concrete`이고 근거와
대안은 논리 수준인 `logical`이다. 대안은 **필수**이며 "대안 없었음"도 기록한다. 세 단위 지식은
`kb/dev/decision/<파트>-<슬러그>/` 디렉토리 하나에 두고, 복합체 개체는 결론 항목의 frontmatter 선언에서
`chunk2kg`가 생성한다. 이 복합체는 정제 수준이 섞이므로 동질성 규칙과 긴장 관계에 있었다. 그 긴장은
[`p4-composition-rules`](../kb/dev/decision/p4-composition-rules/conventions.md)의 규약이 결정 기록을 동질성의 수준 예외로 정하면서 해소됐다 (2026-09-13).

**결정 밖의 복합체는 `kb_composite`로 선다** (유저 답 2026-09-26, 도구를 고친다). 묶음의 단위는 파일이 아니라
**액션의 입력 집합**이다. 그래서 같은 패키지에서 `composite.id`를 공유하는 단위 지식 2~9개가 타깃 하나가 되고, 부분
단위 지식의 개별 `kb_chunk` 타깃은 사라진다. 타깃 이름은 `composite:`를 선언한 단위 지식의 파일 이름이다. 부분과
선언은 같은 패키지에 있어야 하고, 부분들의 지식 종류와 수준은 서로 같아야 한다. 판정은 세 시점에서 한다. 생성
시점에는 `tools/gen_build.py`의 `_check_bundle`이, 분석 시점에는 `kb_composite`가, 그래프 단계에서는 verify 질의
`composite-heterogeneous`가 판정한다. `kb_composite`는 `plane`과 `level`을 한 쌍만 받으므로 이질 복합체를 표현할 수 없다.
수준이 섞이는 것은 결정 기록에만 예외로 허용한다. 손으로 쓴 `kg/composite-kg.ttl`의 복합체는 이 경로로 옮기되,
부분이 하나인 것은 복합체가 아니므로 남기지 않는다. 복합체 IRI는 지속 IRI 원칙에 따라 기존 `id:comp-*`를 유지한다.

**순서는 선언에서만 나오고**, 결정도 예외가 아니다 ([`p4-composite-order-is-declared`](../kb/dev/decision/p4-composite-order-is-declared/conclusion.md),
유저 승인 2026-09-29, 도구 반영도 같은 날). 선언하는 단위 지식의 `composite:`에 `ordered: [<부분 IRI>…]`가 있으면 `kb_composite`와 `gen_build`가
`part_iris`를 그 순서로 내고, `chunk2kg`가 `<복합체> a agt:Composite, co:List ; co:item [ a co:ListItem ; co:index
"<1..n>"^^xsd:positiveInteger ; co:itemContent <부분> ] …`을 방출한다. `ordered`가 없으면 `hasDirectPart`만 낸다. `hasDirectPart`는
순서와 무관하게 남으므로 순서 트리플은 그 위에 더해질 뿐이다. 목록이 부분 집합과 어긋나면 생성 시점에는 `gen-build`가,
실행 시점에는 `chunk2kg`가 거부한다. 색인이 1..n으로 연속하는지, 중복이 없는지, 부분 집합과 일치하는지는 shape
`composite-order-shapes`가 판정하며, 이 shape는 이 저장소에서 `sh:sparql`을 처음 쓴 사례다. 판정 단위가 복합체 노드
하나이므로 이 판정은 verify 실행 계층이 아니라 shape 실행 계층에 속한다. `ordered`는 frontmatter의 메타데이터이므로
더하거나 고쳐도 `generated.at`과 `verified`를 건드리지 않는다.

## §3. plane — 판정 방식으로 나뉜 종류

지식 종류의 분류 기준은 저장 위치나 파일 형식이 아니라 **"맞다"고 판정되는 메커니즘**이다
([`p5-plane-by-verification`](../kb/dev/decision/p5-plane-by-verification/conclusion.md)).

지식 종류는 **일곱**이고, v3에서 `requirement`가 추가됐다.

원본: [`p5-plane-by-verification`](../kb/dev/decision/p5-plane-by-verification/conclusion.md) · [`p7-dev-plane-substance`](../kb/dev/decision/p7-dev-plane-substance/conclusion.md).

| plane | 판정 방식 | 변경률 | 개발 프로파일의 실체 |
|---|---|---|---|
| `requirement` | EARS 형식과 유저 승인에 의한 이해관계자 확인 | 매우 낮음 | 요구사항 문장 |
| `decision` | 논박할 수 있으나 기계로 판정할 수 없어 유저가 승인하는 논증의 타당성 | 낮음 | 설계 결정·아키텍처 문서 |
| `schema` | 스키마·호환성 검사 | 낮음 | 데이터 프로토콜·스키마 |
| `contract` | 결정론적 형식 검사 | 중간 | 인터페이스·타입 시그니처 |
| `artifact` | 실행·측정 | 빠름 | 소스코드 |
| `annotation` | 해소·승인에 의한 사회적 합의 | 매우 높음 | 주석·리뷰 코멘트 |
| `memory` | 없음, 휘발성 | 매우 빠름 | 에이전트 작업 메모리 |

`plane`으로 적는 지식 종류는 `agt:Chunk`의 **하위 클래스**이고, `level`로 적는 정제 수준은 **속성**인 `agt:hasLevel`이다. 이렇게
나눈 까닭은 지식 종류마다 다른 shape을 붙이기 위해서이고, 같은 항목이 수준을 바꾸는 일이 없기 때문이다. 수준의
전이는 새 단위 지식을 만들어 `refines`로 잇는 방식으로 한다 ([`p4-plane-subclass-level-property`](../kb/dev/decision/p4-plane-subclass-level-property/conclusion.md)).

**지식 종류를 추가하는 유일한 근거는 판정 방식이 기존 어디와도 다를 때다.** 판정 방식이 같으면 하위 클래스로
둔다. 영향은 단방향이고 순서의 기준은 변화 속도이며, 그 순서는
`requirement → decision → contract/schema → artifact → annotation → memory`다. 무효화도 이 순서로만 전파되므로
파급이 유계가 된다 (노트 5.2절).

## §4. traceability — 인터페이스를 기준축으로 한 mapping

각 종류의 **인터페이스를 기준축**으로 지식 종류 사이의 항목을 잇는다. 링크의 양 끝은 파일이 아니라
단위 지식이나 복합체의 IRI이고, 링크는 산출물 밖의 `-kg`에 한 방향만 저장하며 역방향은 질의로 얻는다
([p10-link-types](../kb/dev/decision/p10-link-types/conclusion.md) · [p10-link-storage-and-anchors](../kb/dev/decision/p10-link-storage-and-anchors/conclusion.md)).

링크 타입은 세 족과 구성 관계로 정렬된다 (`kb/ontology/related/trace/`).

원본: [`p10-link-families`](../kb/dev/decision/p10-link-families/conclusion.md).

| 족 | 뜻 | 잎 | 전파 |
|---|---|---|---|
| `agt:references` | 본문이 식별자로 가리킨다 | `cites` · `targets` · `usesDefinition`(정의에서 같은 모듈의 정의로 가는 링크이며 추출기가 AST의 최상위 이름 참조에서 낸다, 2026-09-30) | 대상이 바뀌면 출발점이 `suspect`가 된다 |
| `agt:semanticallyDependsOn` | 빼면 의미상 불완전하다 | `refines` · `satisfies` · `constrains` · `verifies` · `derivesFrom` · `usesConcept` · `assumes` · `generates` · `allocates` | 위와 같다. 다만 지식 종류의 단방향 안에서만 전파한다 |
| `agt:relatedTo` | 참조·의미 의존 어느 족에도 들지 않는 관련성 | `coUpdatesWith` · `conflictsWith` · `overlapsWith`(가장 약한 잎이며 이름 없는 관련성의 자리다, 2026-09-26) | 대칭이므로 양쪽이 `suspect`가 된다 |
| (구성 관계) | 함께 읽힘·순서 | `hasDirectPart` | 부분이 무효면 전체가 `suspect`가 된다 |

**링크 어휘의 확장 규칙** — 새 관계는 위 세 족 가운데 하나의 **잎으로만** 더하고 족을 새로 만들지 않는다(유저 승인 2026-09-23,
링크 견고성 E). 잎은 `rdfs:subPropertyOf`로 족에 속하고, 게이트가 부모 트리플을 함께 생성하므로 족 단위 질의는
새 잎을 자동으로 본다. 잎의 이름은 `docs/references.md` §추적성의 추적성 관계 분류에서 가져오고 지어내지 않으며,
`overlapsWith`가 그렇게 가져온 이름이다. 후보 생성기는 추적 매트릭스에 칸이 없는 쌍을 만나면 `relatedTo`가 아니라 `overlapsWith`로
낸다. 인용은 겹침의 표지이고 칸 없는 참조는 참조 링크로 확정되지 않기 때문이다. 다만 칸이 생기면 그 칸의 잎으로 올린다.

frontmatter 링크 키는 두 무리로 나뉜다. 첫째 무리는 Bazel `deps`가 되는 네 키 `refines`와 `serves`, `supersedes`, `verifies`다.
둘째 무리는 그래프 트리플과 링크 개체만 되는 나머지 키 `satisfies`와 `constrains`, `derivesFrom`, `allocates`, `generates`,
`overlapsWith`다. 대칭 속성은 `deps`가 되면 순환이 생기므로 둘째 무리에만 든다.

`allocates`는 요구를 구성요소에 할당하는 링크이고 `generates`는 산출 의존이며, 둘은 v3 9장에서 추가됐다 (유저 결정
C7). `serves ⊑ refines`는 결정에서 요구나 관심사로 가는 링크이고, v4 6.8절과 7.3절이 명시한 기여 관계다. `supersedes`는
시간축의 링크이므로 세 족 밖에 있다. **링크는 개체다** (`agt:Link`). 링크는 양 끝, 타입, **조건**과 **증거 기록**을
갖는다. 조건은 `when`이며 ODD 속성과 가정 위의 CEL이다. 증거 기록은 `agt:Evidence`이며 종류와 참조, 지지나 반박을 뜻하는 극성을 가진
항목의 목록이다. 확정 전 후보는 `agt:CandidateLink`이고, 판정된 것은 `agt:ConfirmedLink`다. 상태는 `candidate`, `confirmed`, `suspect`, `invalid` 넷이고,
저장값이 아니라 **조건 평가와 증거 기록 규칙의 결과**다. **수치 신뢰도는 없다.** 대신 선호는 지지 증거의 종류 서열에서
파생되며, 서열은 높은 쪽부터 구축, 실행, 동시 편집, 공동 커버, 임베딩, 세션, 제안이다. `assumes`와 적용 범위 conditional은
`when`의 특수형이다. 증거 기록 규칙 둘은 verify 질의로 검사한다. 하나는 구축과 실행의 지지 증거가 없는 확정을 잡고, 다른
하나는 반박 증거가 있는 확정을 잡는다 (`tools/verify-queries/`; 노트 9.11절, 2026-09-10).

조회 알고리즘은 앵커에서 이웃을 확장하고 우선순위를 매긴 뒤 예산 안에 패킹하는 순서이며, [`p0-workset-anchor-neighbourhood`](../kb/dev/decision/p0-workset-anchor-neighbourhood/conclusion.md)에 있다.
복원 경로는 [`p10-link-by-construction`](../kb/dev/decision/p10-link-by-construction/conclusion.md)·[`p9-candidate-generation-limits`](../kb/dev/decision/p9-candidate-generation-limits/conclusion.md)에 있다.
LEDGER·LARGER 대응표 원안은 2026-09-04의 출처 문서 `id:doc-dependency-graph-design`에 있고, 이 원안은 2026-09-12에
반영을 마쳤으며 그 위치는 `kg/base-kg.ttl`의 `prov:atLocation`이 적는다.
**어휘는 갖춰졌고 링크 개체는 전부 구축 기록 증거를 갖는다.** 그 수는 `bazel build //kg:metrics`의 3단계 절이 내며,
2026-09-11의 472는 2026-10-01에 1,277이었다.

## §5. knowledge graph — 무엇을 담는가

원본: [`pe-kg-hand-and-generated-files`](../kb/dev/decision/pe-kg-hand-and-generated-files/conclusion.md) · [`pe-odd-is-openodd`](../kb/dev/decision/pe-odd-is-openodd/conclusion.md) · [`p9-candidate-storage`](../kb/dev/decision/p9-candidate-storage/conclusion.md).

| 담는 것 | 위치 | 손/생성 |
|---|---|---|
| 지식 head | `bazel-bin/kg/chunks-kg.ttl` | **생성** |
| 복합체 | `kg/composite-kg.ttl` | 손 |
| 가정·출처 문서 | `kg/base-kg.ttl` | 손 |
| 역할과 적용 범위, 채널, 하네스 (입력) | `kg/catalog-kg.ttl` | 손 |
| 조건과 ODD | 손으로 쓰는 `kb/odd/project-odd.yml`에서 `project-odd.ttl`과 `taxonomy.yml`을 생성한다. YAML은 OpenODD 매핑인 `TAXONOMY`, `MODULES`, `INCLUDE_AND` 등을 쓰고, 확장 키는 `ATTRIBUTES`, `LITERALS`, `CHECKS`, `EXCLUSIONS_REVIEWED`다 | YAML 손, TTL 생성 |
| 후보 링크 | `type: agt:Space`이고 변수 하나에 파일 하나인 `kb/dev/**/*.space.md` | 미구현 |

### ODD

ODD는 프로젝트당 하나이며, 적용 범위, 가정, 시나리오, 커버리지의 **분모**다. 조건은 정적 요소, 환경
조건, 동적 요소의 3분류이고, 각 조건은 값이나 범위, 객관적 판정 방법, 등급 A~D를 갖는다. 다만 판정
불가(D)는 ODD에 넣지 않는다 ([p3-odd-derivations-and-gate](../kb/dev/decision/p3-odd-derivations-and-gate/conclusion.md) · [p3-odd-required-sections](../kb/dev/decision/p3-odd-required-sections/conclusion.md) · [p3-measurement-method-grades](../kb/dev/decision/p3-measurement-method-grades/conclusion.md)).

### 가정

모든 단위 지식은 ODD 조건 위에 세운 가정에 기댄다. **ODD에 없는 조건을 참조하는 파생물은 게이트가
거부한다.** 따라서 대응은 ODD를 확장하거나 파생물을 기각하는 것뿐이다. 가정이 깨지면 그 가정에 의존하는
항목이 자동으로 무효화 표시되므로 전수조사가 필요 없다 ([p6-assumption-invalidation](../kb/dev/decision/p6-assumption-invalidation/conclusion.md) · [p0-odd-scope-assumption](../kb/dev/decision/p0-odd-scope-assumption/conclusion.md) · [p6-assumption-verification-methods](../kb/dev/decision/p6-assumption-verification-methods/conclusion.md)).

규칙은 **기본 가정 후 좁힘**이다 (2026-09-12). 항목 고유의 전제를 아직 적지 않은 단위 지식은 기본 가정
`id:asm-chunk-conventions`를 `assumes`한다. 이 기본 가정은 저장소 구조와 언어 정책의 조건으로 된 자리표시이므로,
항목의 실제 전제가 드러나면 그 고유 가정을 **앞에 더한다**. 예를 들어 Bazel 하네스에 기대는 결정의 고유 전제는
`asm-bazel-toolchain`이다. 다만 항목이 단위 지식 규약에도 기대는 동안에는 기본 가정이 남는다. 좁힘의 진행은
고유 가정을 가진 단위 지식 수로 재고, 그 수는 `metrics`의 가정 절이 낸다 (2026-09-14 정정).

### level — 정제 수준과 지식 종류별 허용 수준 표

v3가 `level` 키를 **정제 수준**으로 재정의했다 (노트 6.4절). 다섯 수준은 요구만 있는 `functional`,
형식 문장만 있고 도메인이 없는 `abstract`, 후보와 제약을 담는 `logical`, 확정된 개체를 담는 `concrete`, 동작만 남은
`executable`이고, 이 다섯 단계는 유지하며 건너뛰지 않는다.

**모든 지식 종류가 모든 정제 수준에 놓일 수 있는 것은 아니다.** 그래서 지식 종류별 허용 수준 표를 SHACL로 강제한다
(`kb/ontology/shapes/residency-shapes.ttl`).

원본: [`p6-plane-level-occupancy`](../kb/dev/decision/p6-plane-level-occupancy/conclusion.md).

| plane | 허용 level |
|---|---|
| `requirement` | `functional` |
| `decision` | `abstract`, `logical`, `concrete` |
| `contract` | `abstract`, `logical` |
| `schema` | `logical`, `concrete` |
| `artifact` | `concrete`, `executable` |
| `memory` | `concrete` |
| `annotation` | 제약이 없어 모든 정제 수준의 항목에 주석을 단다 |

### 통제 어휘

데이터의 술어는 `agt:` 온톨로지나 등록된 표준 어휘 안에 있어야 하고, 등록된 표준 어휘는 rdf, rdfs,
owl, xsd, skos, sh, prov, dcterms, co, obo다. prov와 skos의 용어는 W3C 원문에 실재해야 하며, 게이트가 `MODULE.bazel`의
`http_file`로 해시를 고정한 원문 `@prov_o`·`@skos`와 대조한다 (2026-09-12). `agt:` 접두어인데 온톨로지에 없으면
오타이거나 무단 어휘 생성이고, 등록되지 않은 네임스페이스면 어휘 우회다. 그래서 둘을 다른 메시지로 구분해
보고한다 ([p0-agt-namespace](../kb/dev/decision/p0-agt-namespace/conclusion.md)). 목록의 단일 정의 위치는 `tools/kb_lib.py`다.

### 개체 IRI 접두사

원본: [`p0-entity-iri-forms`](../kb/dev/decision/p0-entity-iri-forms/conclusion.md) · [`p0-iri-design`](../kb/dev/decision/p0-iri-design/conclusion.md).

| 종류 | 형식 | 사는 곳 |
|---|---|---|
| 지식, v3 이후 | `id/chunk/<uuid4>`, 불투명 영속 IRI | 생성물 `chunks-kg.ttl` |
| 지식, 묘비(지운 v1 결정) | `id:chunk-d<번호>`이고 새로 만들지 않는다 | 생성 `chunks-kg.ttl`의 묘비로 남고 `supersedes`의 끝점이다 |
| 복합체, v3 이후 | `id/composite/<uuid4>` | 생성물 또는 `composite-kg.ttl` |
| 가정 · 출처 문서 | `asm-` · `doc-` | `base-kg.ttl` |
| 손으로 쓴 복합체 | `comp-` | `composite-kg.ttl` |
| ODD · 조건 | `odd-` · `cond-` | `project-odd.ttl` |
| 하네스, 역할, 적용 범위, 채널 | `h-` · `role-` · `scope-` · `chan-` | `catalog-kg.ttl` |
| 시나리오 | `scn-` | 아직 없음 |
| 게이트 | `gate-` | 생성되는 `bazel-bin/kg/gates-kg.ttl`이다. 원본은 `defs/kb.bzl`의 `GATES`이고 손으로 쓰지 않는다(2026-10-02) |
| 투영인 뷰 · skill | `view-` · `skill-` | 생성되는 `bazel-bin/kg/projections-kg.ttl`이다. 원본은 `defs/kb.bzl`의 `VIEWS`와 `tools/kb_lib.py`의 `SKILLS`이고, `prov:wasDerivedFrom`이 원본 코드 단위 지식을 가리킨다. 층은 없다(Q9-a, 2026-10-03) |
| 실행 기록 | `id/chunk/<uuid4>`. `memory` 지식 종류의 단위 지식이고, 파일은 `kb/vv/run/run-<시각>.md`, 프로세스는 `process:vv_run`이다 | 생성물 `chunks-kg.ttl` |

IRI는 불투명하게 유지한다. 라벨이나 경로가 바뀌어도 IRI가 유지되어야 시간 정체성이
성립하므로, v3부터 IRI는 uuid다 (유저 결정 Q1). 사람이 읽는 이름은 IRI가 아니라
`rdfs:label`이고, 내용 버전은 `agt:contentHash`다.

### 정규화 직렬화

기계가 만든 TTL은 커밋 전에 정규형으로 바꾼다. 직렬화 순서가 불안정하면 git diff가 의미 없는 변경으로 오염되고, 그 오염이
무효화 판정의 입력을 더럽히기 때문이다 ([p2-ontology-compiler-three-tiers](../kb/dev/decision/p2-ontology-compiler-three-tiers/conclusion.md)).
정규형은 `@prefix`를 정렬하고 트리플을 주어와 술어, 목적어 순으로 정렬한 꼴이다. 반면 `kg/*-kg.ttl`과 온톨로지, shape처럼 손으로
쓰는 TTL은 STYLEGUIDE §1·§5의 서식이 원본이므로 정규형 검사 대상이 아니다. 그 서식은 배너와 주석, 술어 순서를 정한다(2026-09-13 판정).

```bash
bazel run //tools:canonicalize -- --write <files>
```

## §6. 그래프 안과 밖

검사 대상인 지식과 검사 대상이 아닌 문서를 가르는데, 소통 기록과 지식을 섞으면 통제 어휘 검사가 무의미해지기
때문이다. 지식은 `kb/{ontology,odd,dev,vv}/`와 `kg/`에 있고, 문서는 `docs/`와 `.claude/`에 있다.
문서는 결정을 복사하지 않고 **IRI로 인용**한다. 복사하면 이중 관리가 되고, 원본과 사본이 어긋나는
순간 어느 쪽이 원본인지 알 수 없어지기 때문이다 ([p4-projection-as-query](../kb/dev/decision/p4-projection-as-query/conclusion.md)).

## §7. development 규칙 — 개발 KB (노트 7.2~7.7)

개발 KB는 요구 명세에서 실산출물을 생산하기 위한 지식이다
([`p7-dev-kb-purpose`](../kb/dev/decision/p7-dev-kb-purpose/conclusion.md)). 코어 규칙 위에 다음 규칙이 더해진다.

**코드는 단위 지식으로 올라오고 방향은 추출이다** (유저 승인 2026-09-30, [`p7-code-extraction-direction`](../kb/dev/decision/p7-code-extraction-direction/conclusion.md)).
소스 파일 하나가 패키지 `kb/dev/artifact/<모듈>/` 하나이고, 그 패키지의 단위 지식은 전부 `bazel run //tools:extract -- <소스>`의
생성물이다. 그래서 손으로 고치면 `//:extract_drift_test`가 거부한다. 정체성의 원본은 소스 옆 사이드카 등록부 `<소스>.chunks.yml`의
`한정 이름 → uuid`이고, 신설만 자동이며 개명과 삭제는 등록부를 편집해서 한다 ([`p10-function-identity-registry`](../kb/dev/decision/p10-function-identity-registry/conclusion.md)).
링크는 파일 복합체가 갖는다 ([`p7-code-links-on-file-composite`](../kb/dev/decision/p7-code-links-on-file-composite/conclusion.md)). 추출기가 등록부의
`refines`를 파일 항목과 절 항목으로 옮기고, 정의는 `part_of`만 갖는다. `serves`는 정의역이 `agt:DecisionChunk`이므로
`artifact` 단위 지식은 요구를 직접 `serves`하지 않는다. 대신 결정을 `refines`하고 그 결정이 요구에 닿는다. `artifact`의
`verified`는 테스트를 통과했다는 표시다 (`STYLEGUIDE.md` §4).

**정의 사이의 호출은 `usesDefinition`으로 올라온다** (유저 답 2026-09-30). 정의의 선택 키 `uses`는 같은 모듈의
최상위 정의를 가리키고, 추출기가 AST의 이름 참조에서 그 값을 낸다. `uses`는 `references` 족의 잎이므로 Bazel `deps`도
링크 개체도 아니며, 링크는 그대로 파일 복합체가 갖는다. 방출의 경계는 `defs/kb.bzl`의 `EXTRACTED_SOURCES`이고, 이 경계는
37 파일 전부를 덮으며 측정한 트리플은 476이다. `EXTRACTED_SOURCES`는 `RESIDENCY`와 같은 해법으로 둔 단일 정의 위치다
(2026-10-01). `BUILD.bazel`은 그 리터럴을 load하고 `kb_lib.load_extracted_sources`가 `ast.literal_eval`로 읽어 `uses`
방출 경계를 파생하므로, 상수를 둘로 두지 않는다. 또한 `tools/BUILD.bazel`의 `check_extracted_sources`가 등록부 사이드카의
집합과 그 목록이 같은지를 로드 시점에 강제하므로, 둘이 갈리면 bazel 명령이 바로 실패한다.

**치역 경계는 선언이다** (유저 답 1, 2026-10-01). `uses`의 치역은 같은 모듈의 최상위 정의와, `defs/kb.bzl`의
`USES_TARGETS`가 선언한 모듈의 최상위 정의다. 표본 쌍은 `kb_lib` 하나이고, 치역을 넓히려면 그 리터럴에 이름을 더한다.
모듈 밖 해소는 최상위 import와 정의 안의 늦은 import가 묶은 이름을 보고, 별칭을 포함한 `kb_lib.<이름>`과
`from kb_lib import <이름>`의 `Load` 참조를 대상 모듈 등록부의 uuid로 푼다. 측정한 `agt:usesDefinition`은 667이다.
모듈 안이 484, 모듈 간이 183이고 치역은 전부 `kb_lib`이며, 표본 30과 독립 대조에서 오탐과 누락은 모두 0이었다. 채널이 든
사례인 `pct`는 이제 **호출부 12**로 잡힌다.

**남은 사각지대는 셋이다.** 첫째는 치역 경계 밖의 모듈이고, 전부로 넓히면 52가 늘며 그 대부분이 `chunk2kg`의 43이다.
둘째는 함수를 인자로 넘기는 간접 호출 17 표현식이고, 넘기는 쪽은 잡히지만 받는 쪽은 잡히지 않는다. 셋째는 정의가 아닌
이름인 상수와 모듈 변수를 쓰는 관계이고, 그 이름에는 정의가 없어 어느 경계에서도 올라오지 않는다.

단위 지식 100과 복합체 25로 된 표본 `tools/kb_lib.py`의 churn을 측정해 uuid 정체성이 성립함을 확인했고, 이를 근거로 같은 날
대상을 `tools/*.py` 전부로 넓혔다. 그 결과는 **37 파일 전부**, 단위 지식 624, 복합체 184이고, 파일마다 드리프트 테스트
`//:extract_drift_<모듈>`이 있고 그 묶음은 `//:extract_drift_test`다. 절 주석은 최소 하나이므로 파일 복합체의 부분은 둘 이상이다.
클래스는 정의 하나로 올라오고 측정한 최대 길이는 85줄이다. 200줄을 넘던 `consistency`와 `metrics`의 `main` 둘은 상한을
올리지 않고 나눴으며, 나눈 뒤에도 산출물은 바이트 단위로 같다.

| 규칙 | 내용 | 결정 |
|---|---|---|
| `requirement` | 기능 수준 전용이다. EARS 다섯 패턴을 쓰고 이해관계자와 관심사가 필수다 | [`p7-dev-plane-substance`](../kb/dev/decision/p7-dev-plane-substance/conclusion.md) |
| 결정 기록 | 결정 기록은 항상 결론과 근거, 대안의 세 단위 지식으로 이루어진다. **대안이 없는 결정은 shape 위반이고**, 대안이 없었다는 사실도 기록한다 | [`p7-alternatives-mandatory`](../kb/dev/decision/p7-alternatives-mandatory/conclusion.md) |
| 결정의 정제 수준 | 변수를 다루는 추상 수준과 후보, 제약, 배제를 다루는 논리 수준, 값을 다루는 구체 수준은 별개 단위 지식이고 `refines`로 연결한다. 구체 수준 항목이 생겨야 결정이 확정된다. 추상 수준 항목은 `-space`가 있을 때만 둔다 | [`p7-decision-spans-three-levels`](../kb/dev/decision/p7-decision-spans-three-levels/conclusion.md) |
| 기여 | 추상 수준 결정은 `refines`의 하위 속성인 `serves`로 어느 요구의 어느 관심사에 기여하는지 밝혀야 하고, 밝히지 않으면 거부된다 | [`p6-transition-gates`](../kb/dev/decision/p6-transition-gates/conclusion.md) |
| 계약 우선 | 추상 수준의 `contract`가 구현보다 먼저 확정되고, 계약이 없는 구현은 정제가 끊긴 것이다. 논리 수준의 계약인 사후조건이 V&V 기준의 재료다 | [`p7-contract-first`](../kb/dev/decision/p7-contract-first/conclusion.md) |
| 스키마 | `decision`에서 `derives-from`으로 파생되어 `contract`를 `constrains`로 제약하고, 비호환 변경은 새 IRI를 만들어 `supersedes`로 잇는다 | [`p7-schema-derivation`](../kb/dev/decision/p7-schema-derivation/conclusion.md) |
| `artifact` | 구현만 담고, 검증기는 V&V KB에 둔다 | [`p6-executable-splits-by-kb`](../kb/dev/decision/p6-executable-splits-by-kb/conclusion.md) |
| 구현 착수 | developer는 구체 수준 결정과 확정 스키마 없이 구현할 수 없다(적용 범위 conditional). developer 작업 집합에는 `-space`가 없다 | [`p7-developer-requires-concrete`](../kb/dev/decision/p7-developer-requires-concrete/conclusion.md) |
| 대체 | 결정은 `supersedes`로 대체하고, 옛 결정은 `deprecated`가 되며 그 결정의 `satisfies` 링크는 모두 `suspect`가 된다 | [`p7-decision-supersession`](../kb/dev/decision/p7-decision-supersession/conclusion.md) |
| 완료 | 연쇄 완주와 계약 선행, 대안 존재, 가정의 `stable` 상태, **V&V `verifies`의 유효**를 모두 갖춰야 완료이므로, 개발 KB만으로는 완료를 선언할 수 없다 | [`p7-dev-kb-completion`](../kb/dev/decision/p7-dev-kb-completion/conclusion.md) |
| 역할 | design은 요구, 결정, 계약, 스키마, ODD / developer는 `artifact`와 개발 KB의 `contract` / orchestrator는 dispatch 결정 / V&V는 `annotation`만 | [`p7-dev-roles-and-scopes`](../kb/dev/decision/p7-dev-roles-and-scopes/conclusion.md) |

2026-09-10에 측정한 이 저장소의 항목 수는 `requirement` 33, `decision` 182이고 `contract`, `schema`, `artifact`는 0이다. 대안은 결정 182 가운데 182에 있다.

## §8. V&V 규칙 — V&V KB (노트 8.2~8.5, 8.11~8.15, 8.4, 9.11)

V&V KB는 코어의 두 번째 인스턴스이므로, 새 지식 종류를 만들지 않고 실체만 다르다
([`p8-vv-plane-instances`](../kb/dev/decision/p8-vv-plane-instances/conclusion.md)).

| 규칙 | 내용 | 결정 |
|---|---|---|
| 독립성 | 개발 역할은 V&V KB에 쓸 수 없고, 기준은 요구를 고쳐서만 고친다. 저장은 `kb/vv/`로 분리하고, 의존은 V&V에서 개발로 향하는 한 방향이다 | [`p8-vv-independence-scope`](../kb/dev/decision/p8-vv-independence-scope/conclusion.md) |
| 검증 대응물 필수 | 기능에서 추상으로 갈 때 검증 목표가, 논리에서 구체로 갈 때 합격 기준이, 구체에서 실행으로 갈 때 검증기가 있어야 한다. 없으면 개발 게이트가 실패하고, 7단계 전에는 경고만 낸다 | [`p8-scenario-ladder-rungs`](../kb/dev/decision/p8-scenario-ladder-rungs/conclusion.md) |
| `verifies` | KB를 가로지르는 유일한 링크이고, 방향은 V&V에서 개발로 향하며 같은 정제 수준끼리 잇는다 | [`p6-executable-splits-by-kb`](../kb/dev/decision/p6-executable-splits-by-kb/conclusion.md) |
| 시나리오 | 시나리오는 자극과 요인, 배제 자극으로 이루어진 `decision`(vv) 복합체다. 변수는 ODD 속성만 쓰고, ODD 밖은 `odd:outside`로 커버리지에서 뺀다. 세 단위 지식의 파일 이름은 `<슬러그>-stimulus.md`, `<슬러그>-factors.md`, `<슬러그>-excluded.md`이고, 역할 표지 **자극**, **요인**, **배제 자극**이 결정의 결론, 근거, 대안 슬롯에 사상되며, 선언하는 단위 지식은 `-stimulus`이고 `ordered`는 필수다(게이트 `decision-role`·`shacl`, 2026-09-29). 접미 판정은 `kb/vv/scenario/`에서만 거는데, 옛 결정 가운데 stem이 `-factors`로 끝나는 것이 있기 때문이다. 단일 단위 지식 시나리오는 이행 기간 동안 **결론** 표지로 통과한다 | [`p8-scenario-authoring`](../kb/dev/decision/p8-scenario-authoring/conclusion.md) |
| 판정 로그 | 판정 로그는 실행 기록이어서 `kb/vv/run/judge-<시각>.md`에 append-only로 쌓이고, 생성자는 `process:judge`이며 역할이 아니므로 writer 검사 밖이다. 판정 표의 열이 곧 필수 필드로, 질문 id와 값, 확신도, **판정자 식별자**, 입력 해시값, 시각이다. 판정자 식별자는 외부 서비스가 아니라 세션·모델이다(2026-09-30). 입력 해시값은 보낸 바이트의 sha256이다. 열 `일치`의 값은 일치, 불일치, 해당 없음이고, 이 열은 판정자 둘 이상이 같은 질문과 해시값의 쌍에 답했을 때만 뜻을 갖는다. 확신도는 **자기 보고**라 개별 답을 보증하지 않으므로 단독 응답으로는 자동 적용이 없다. 결과 주석의 `본문:`은 판정자가 쓰지 못하므로 `해당 없음`이다. 게이트는 `chunk_lint`의 `judge-log`이고, **로그가 0건이면 검사 대상이 없어 PASS다** | [`p8-judge-session-agreement`](../kb/dev/decision/p8-judge-session-agreement/conclusion.md) |
| 기계 환원 | `핵심:` 항목의 지지 참조인 요약은 `chunk_lint`의 게이트 `summary-support`로 확정되며, 이 게이트의 측정 오탐은 0/0이고 슬롯 사용은 0이다. 중복과 자리는 `consistency.py` ⑩·⑪이 후보만 내고, 확정은 판정자, 곧 사람 또는 세션 판정자가 한다 | [`p8-judge-session-agreement`](../kb/dev/decision/p8-judge-session-agreement/conclusion.md) |
| 쌍 판정 | 링크 후보의 판정은 쌍 모드(`judge --pairs`)다. 행은 쌍 하나이고 `대상` 열은 `<앵커 IRI> ↔ <대상 IRI> · <링크 종류>`다. 질문은 링크 종류가 겹침이면 `overlapsHolds`, 그 밖이면 `proposedLinkHolds`이고 둘 다 예/아니오형이다. 결과 주석은 쌍마다 하나로, 판정자 둘의 값과 확신도, 일치를 함께 담고 `targets:`에 두 IRI를 적는다. 미끼는 판정 로그와 증거에 넣지 않고 검출률만 로그에 남긴다. 쌍의 입력 해시값은 두 파일 바이트를 이은 것의 sha256이고, 지금 두 파일과 다르면 낡은 판정이라 증거를 내지 않으므로 그 쌍은 다시 판정한다. 판정 증거는 반박만 있어도 후보를 무효로 만들지 않고, 이미 확정된 쌍에는 붙지 않는다. 판정자 하나만 답한 쌍은 판정 없음으로 센다(Q-0061#Q145) | [`p8-judge-session-agreement`](../kb/dev/decision/p8-judge-session-agreement/conclusion.md) |
| 위험 분석의 어휘 | 현상은 `kb/ontology/related/defect/`에 있는 `defect` 모듈의 요인 개체다. 하위 유형 14는 인지와 상호작용, 실행의 세 갈래 아래 ODC 유형이고, 피해는 ODC 영향 차원 다섯인 `agt:DefectImpact`이며, "지식 유실·재생산"은 H1 하위다. 현상 개체는 정의와 P번호 표기, 관측 수단, 출처를 갖는다(게이트 `shacl`, `defect-factor-shapes`). 위험 지표 S와 노출, 탐지가능성은 순서 척도이므로 **곱하지 않으며**, 등급은 정렬용이고 합격 기준은 테스트 케이스가 정한다. 탐지가능성 D는 현상 개체의 `agt:observationMeans`가 갈리는 세 꼴에서 도출되어, 게이트 이름이면 D1, 생성 보고서가 수치로 내되 진행을 막지 않으면 D2, `미확정`이면 D3다. 값의 원본은 `defect-rules/risk-grade-rules.ttl`이므로 수를 여기 적지 않는다. 관측 수단 다섯이 서서 D3가 둘로 줄었다(2026-10-01). `미확정`을 유지하는 현상은 그 까닭을 정의문에 적는데, 관측 수단 자리에 산문을 덧붙이지 않는 것이 세 빈 값 규칙이기 때문이다. 규칙성 가정 A1~A3은 `id:asm-links-only-interaction`, `asm-finite-factor-types`, `asm-missing-vocabulary-is-signal`이고, 프로파일에서 파생되는 항목이 이 가정을 `assumes`로 참조한다(2026-09-29). 현상에서 피해로 가는 인과는 `defect-rules` 모듈의 `agt:hasImpact` 트리플이고, 첫 형태 28건이 질문지의 피해 열이다. 어휘인 `defect`와 형식화인 `defect-rules`를 나눈 이유는 어휘가 안정적이고 규칙이 자주 바뀌므로 어휘 사용자가 규칙 변경에 영향받지 않아야 한다는 데 있다(노트 2.3절 (b)). | [`p8-odc-defect-subtypes`](../kb/dev/decision/p8-odc-defect-subtypes/conclusion.md) · [`p8-risk-analysis-profile`](../kb/dev/decision/p8-risk-analysis-profile/conclusion.md) |
| 기준과 자극의 구분 | 기준은 별도 `contract`(vv) 단위 지식이고 `verifies` 속성으로 바인딩한다. 판정 술어가 없는 기준은 추상 수준으로 강등한다 | [`p8-pass-criteria`](../kb/dev/decision/p8-pass-criteria/conclusion.md) |
| 테스트 케이스 | 구체 수준 테스트 케이스는 사람이 쓰지 않고 `keep`과 `cover`에서 생성한다. 표본 근거가 없는 테스트 케이스는 거부한다 | [`p8-case-generation`](../kb/dev/decision/p8-case-generation/conclusion.md) |
| 테스트 케이스의 상태 | 생성기는 시나리오의 상태를 테스트 케이스에 물려준다. 시나리오가 stable이면 테스트 케이스도 stable이고, 그 재검증 표시는 `process:case_gen`이 시나리오의 재검증 시각으로 단다. 그래서 생성물의 바이트 비교가 그대로 성립한다 (유저 답 Q131-a, 2026-10-24) | [`p8-case-generation`](../kb/dev/decision/p8-case-generation/conclusion.md) |
| 역할 | 검증기 저자는 V&V engineer와 다른 사람이거나 다른 세션이어야 하고, audit은 쓰지 않는다 | [`p8-vv-roles`](../kb/dev/decision/p8-vv-roles/conclusion.md) |
| 재현성 | 재현할 수 없으면 5~6단계로 강등하고, 6단계 관측은 커버리지에 넣지 않는다 | [`p8-reproducibility`](../kb/dev/decision/p8-reproducibility/conclusion.md) |
| 학습된 판정자 | 정확도와 판별력, 캘리브레이션의 세 지표를 통과하고 사람이 승인해야 하며, 결과는 head의 `verified` 목록에 적는다 | [`p8-learned-environment-and-judge`](../kb/dev/decision/p8-learned-environment-and-judge/conclusion.md) |
| 평가의 목적지 | 확인 결과는 `requirement`로 가고, 이 경로가 요구가 바뀌는 유일한 정규 경로다 | [`p8-verification-and-validation`](../kb/dev/decision/p8-verification-and-validation/conclusion.md) |
| 불일치의 귀속 | 실패를 산출물이나 지식, 또는 둘 다에 귀속하는 일은 **결정**이고 V&V `decision` 지식 종류의 지침으로 남는다. 지식 쪽 귀속에는 요구 과도와 제약 부족, 가정 누락이 있고, 진단은 기호 도구로 먼저 한다 | [`p8-mismatch-attribution`](../kb/dev/decision/p8-mismatch-attribution/conclusion.md) |
| 실행 증거 | 검증기 결과는 개발 KB의 `satisfies` 후보가 가진 증거 기록에 지지 증거나 반박 증거로 적힌다. 링크가 아니라 증거 기록 항목이므로 방향 규칙은 유지된다 | [`p9-evidence-ledger-with-belief`](../kb/dev/decision/p9-evidence-ledger-with-belief/conclusion.md) |
| 믿음 정도 | 믿음 정도는 증거 기록에서 계산해 후보와 링크 곁에 병기하고 선호의 동률을 깨지만, 상태 전이 규칙은 믿음 정도를 읽지 않는다 (Q90-a, Q109-b) | [`p9-evidence-ledger-with-belief`](../kb/dev/decision/p9-evidence-ledger-with-belief/conclusion.md) |
| 유저 결정과 판정 | 유저 결정은 서열 밖의 확정 권한이고 참조는 `Q-NNNN#Qn`이나 `legacy/<파일 이름>.md`다. 판정은 확신도와 함께 적히되 확정 근거가 아니고, 서열에서 공동 커버 다음, 임베딩 앞에 선다 (Q111-a, Q118-a) | [`p9-evidence-ledger-with-belief`](../kb/dev/decision/p9-evidence-ledger-with-belief/conclusion.md) |

이 저장소를 2026-09-10에 측정한 결과 `kb/vv/`는 비어 있고, 이 저장소 자신의 검증 목표, 시나리오, 기준이 없다 (도입 7단계).

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
- `kb/dev/decision/p9-evidence-ledger-with-belief/` — `conventions.md`
- `kb/dev/decision/pe-kg-hand-and-generated-files/` — `conventions.md`
- `kb/dev/decision/pe-odd-is-openodd/` — `conventions.md`
- `kb/dev/norm/rules/` — `assumption.md` · `canonical-serialization.md` · `chunk-naming.md` · `chunk.md` · `composite-order.md` · `composite-scope.md` · `composite.md` · `controlled-vocabulary.md` · `development-code-calls.md` · `development-measure.md` · `development.md` · `file-format-empty-values.md` · `file-format-two-kbs.md` · `file-format-vocabulary.md` · `file-format.md` · `graph-boundary.md` · `head.md` · `iri-prefixes-identity.md` · `iri-prefixes.md` · `knowledge-graph.md` · `level.md` · `link-objects.md` · `link-vocabulary.md` · `odd.md` · `plane-subclass.md` · `plane.md` · `traceability.md` · `trust-tier-gates.md` · `trust-tier.md` · `vv-measure.md` · `vv.md`

