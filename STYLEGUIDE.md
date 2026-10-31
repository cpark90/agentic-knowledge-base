# STYLEGUIDE.md — 컴포넌트별 작성 스타일 (생성 파일)

- 생성기: `tools/gen_norms.py` · gendoc/1
- 입력: 원본 파일 66개 · 절 12 · 규약 줄 103 · 전체 목록은 [입력 파일](#입력-파일)
- 질의: `kb/dev/norm/STYLEGUIDE/` 의 절 항목을 선언 순서로 펼치고 항목마다 결정의 `규약:` 줄을 싣는다
- 재현: `python3 tools/gen_norms.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 `kb/dev/norm/STYLEGUIDE/` 의 절 항목과 결정의 `conventions.md`이다. 검사: `//:norms_drift_test`. 생성 시각·입력 해시값은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

## 목차

- [§0. 공통](#0-공통)
- [§1. 온톨로지 (`kb/ontology/**/*-ontology.ttl`)](#1-온톨로지-kbontology-ontologyttl)
- [§2. SHACL shape (`kb/ontology/shapes/*-shapes.ttl`)](#2-shacl-shape-kbontologyshapes-shapesttl)
- [§3. ODD (`kb/odd/*-odd.yml` — OpenODD 문서. `*-odd.ttl`·`taxonomy.yml`은 생성물, 손으로 쓰지 않는다)](#3-odd-kbodd-oddyml--openodd-문서--oddttltaxonomyyml은-생성물-손으로-쓰지-않는다)
- [§4. 지식 (`kb/{dev,vv}/**/*.md`)](#4-지식-kbdevvvmd)
- [§5. 지식그래프 A-Box (`kg/*-kg.ttl`)](#5-지식그래프-a-box-kg-kgttl)
- [§6. Bazel (`BUILD.bazel`, `defs/*.bzl`)](#6-bazel-buildbazel-defsbzl)
- [§7. 도구 (`tools/*.py`)](#7-도구-toolspy)
- [§8. 소통 채널 (`harness/channel/` · `harness/user/`)](#8-소통-채널-harnesschannel--harnessuser)
- [§9. 생성 문서 (`bazel-bin/**/*.md` · 생성 트리 파일)](#9-생성-문서-bazel-binmd--생성-트리-파일)
- [셀프체크](#셀프체크)
- [입력 파일](#입력-파일)

<!-- 인용 시작: 단위 지식에서 그대로 옮긴 값 — 원본이 자기 게이트를 통과했다 -->

이 문서는 지식 산출물 저작의 **단일 진실 공급원**이어서, 저작이나 수정 세션을 시작할 때 읽는다.
하네스 운영 규칙은 [`AGENTS.md`](AGENTS.md), 무엇이 유효한 구조인지는
[`docs/rules.md`](docs/rules.md), 어떻게 만드는지는 [`docs/method.md`](docs/method.md)가 다루고,
이 문서는 **어떻게 쓰는가**만 다룬다.

표기는 둘이다. **[지킴]**은 게이트 또는 리뷰가 강제한다. 반면 **[권장]**은 따르되 사유가 있으면
어겨도 되며, 어길 때는 말없이 머지하지 않고 커밋 메시지나 파일 주석에 사유를 한 문장 남긴다.

## §0. 공통

목표는 코드 스타일과 같은 **일관성과 가독성**이다. 다음 세션의 에이전트가 파일 하나를 열어
빠르게 이해하고, 무엇을 재사용할지 알 수 있어야 한다.

- **[지킴]** **한 단위 지식은 한 파일이고, 한 파일은 한 주제다** ([`p4-one-file-one-topic`](kb/dev/decision/p4-one-file-one-topic/conclusion.md)). 지식과 온톨로지, shape 전부가 대상이다. 라벨 하나로 요약되지 않으면 두 주제이므로 분할한다.
- **[지킴]** **본문은 토큰 상한 이하다** ([`p1-chunk-unit-is-tokens`](kb/dev/decision/p1-chunk-unit-is-tokens/conclusion.md)). 상한은 저작 산문이 42의 26배인 1,092, `artifact`와 `memory`의 인용이 42의 68배인 2,856이고, 계수기는 고정된 `o200k_base`다(2026-10-01, 그 전에는 42줄). 단위는 컴포넌트별 절이 정의한다.
- **[지킴]** **지식의 종류는 고유 용어로 부른다** ([`p0-terms-from-glossary`](kb/dev/decision/p0-terms-from-glossary/conclusion.md)). 고유 용어는 조건과 개념, 변수, 후보, 결정, 가정, 시그니처, 함수, 주석, 관측이다. "결정 단위 지식"이 아니라 "결정"이라 부르고, "단위 지식"은 그 항목이 따르는 구조 규칙을 말할 때만 쓴다. 온톨로지 클래스 이름과 그래프 라벨의 인용은 예외다.
- **[지킴]** **중복 대신 재사용한다** ([`p4-redundancy-as-safety-margin`](kb/dev/decision/p4-redundancy-as-safety-margin/conclusion.md)). 새 개념·항목을 만들기 전에 `grep -r kb/ontology/`와 라벨 목록으로 기존 것을 찾는다. 같은 뜻의 항목 둘이 이 체계가 막는 드리프트다.
- **[지킴]** **표준어가 우선이다** ([`p0-no-invented-terms`](kb/dev/decision/p0-no-invented-terms/conclusion.md)). 지어낸 용어나 자체 약어를 만들지 않고, 표준어가 없을 때만 새로 만든다. 가져온 곳은 [`docs/references.md`](docs/references.md)에 남긴다.
- **[지킴]** **자기설명적으로 쓴다** ([`p0-self-explanatory-definitions`](kb/dev/decision/p0-self-explanatory-definitions/conclusion.md)). 좋은 라벨과 정의가 주석보다 낫다. 정의는 "무엇인가"의 재진술이 아니라 **왜 존재하고 언제 쓰는가**를 적는다.
- **[지킴]** 산문과 정의, 주석은 한글로 쓰고 식별자는 영어 소문자 케밥, 개념은 PascalCase로 쓴다 ([`p0-notation-format`](kb/dev/decision/p0-notation-format/conclusion.md)). 라벨은 한/영 각 1이고, TTL의 들여쓰기는 탭 없이 스페이스 4칸이다.
- **[지킴]** 영문 라벨인 `title`에는 한글을 섞지 않고, 용어 치환은 한글 필드인 `title_ko`와 본문만 대상으로 한다 ([`p0-english-label-without-hangul`](kb/dev/decision/p0-english-label-without-hangul/conclusion.md)). `chunk2kg`는 `title`에 든 한글과 `title_ko`에 한글이 없는 경우를 거부한다(유저 결정 2026-09-12).
- **[지킴]** **산문은 학술 산문체의 단정 서술형이다**(유저 결정 2026-09-13) ([`p0-prose-assertive-register`](kb/dev/decision/p0-prose-assertive-register/conclusion.md)). 대상은 문서와 단위 지식의 본문, 채널 메시지, 질문지, 세션 보고, dispatch 브리핑 전부다. 문장은 평서형 종결 "…다"로 끝난다. 경어체와 감탄, 구어, 추측 표현을 쓰지 않는다. 경어체는 "습니다·세요·해요", 구어는 "근데·그냥·좀", 추측 표현은 "것 같다·듯하다·수도 있다" 같은 말이다. 의문문은 질문을 다루는 절에만 둔다. 사실과 판단을 구분하되 판단도 단정한다. 근거가 있으면 "…다"로 적고, 없으면 적지 않는다. 경어와 감탄은 게이트 `prose`가 거부하며, 그 판정은 `chunk_lint`와 `doccheck`가 함께 쓴다. 추측과 구어, 대시 밀도는 `consistency` ⑦이 보고한다.
- **[지킴]** **한 문장에는 판정 하나를 담고, 그 판정의 이유와 조건은 연결어미로 같은 문장에 붙인다** ([`p0-sentence-composition`](kb/dev/decision/p0-sentence-composition/conclusion.md)). 짧은 단정문이 셋 이상 이어지면 합치고, 문단은 주제문으로 시작한다.
- **[지킴]** 문장 사이의 관계는 접속어로 드러낸다 ([`p0-sentence-composition`](kb/dev/decision/p0-sentence-composition/conclusion.md)). 원인은 "그래서"나 "따라서", 대조는 "그러나"나 "반면", 제한은 "다만", 대체는 "대신"으로 잇는다. "및·그리고·또한으로 잇지 않는다"는 원자성이 필요한 EARS 요구 문장에만 적용한다.
- **[지킴]** 산문에는 `=`, `+`, `→`, `×` 같은 기호와 영어 논리어를 쓰지 않고, 문장은 명사형이 아니라 서술어로 끝낸다 ([`p0-sentence-composition`](kb/dev/decision/p0-sentence-composition/conclusion.md)).
- **[지킴]** 셋 이상을 나열할 때는 가운뎃점 대신 "와/과"와 쉼표로 잇는다 ([`p0-sentence-composition`](kb/dev/decision/p0-sentence-composition/conclusion.md)). 출처 괄호는 문장 끝이나 문단 끝에 모으고, 대시는 라벨 구분자와 부제에만 쓴다. 이 넷은 `consistency`가 보고 지표로 센다.
- **[지킴]** 지시어가 가리킬 수 있는 대상이 둘 이상이면 명사를 되풀이하고 주어를 밝힌다 ([`p0-sentence-composition`](kb/dev/decision/p0-sentence-composition/conclusion.md)). 비유는 실제 동작을 적는 문장으로 바꾼다.
- **[지킴]** 한글 표준어가 있으면 한글로 쓰고 영문은 첫 등장에만 함께 적는다 ([`p0-sentence-composition`](kb/dev/decision/p0-sentence-composition/conclusion.md)). 영어 상태값은 한국어 서술어로 풀어 쓰고, 식별자 앞에는 그 종류를 가리키는 명사를 붙인다.
- **[권장]** 굵게 쓰는 강조는 결론과 규칙에만 쓴다 ([`p0-sentence-composition`](kb/dev/decision/p0-sentence-composition/conclusion.md)). 불릿은 완결된 문장이거나 명사구 하나다.
- **[지킴]** **빈 자리는 세 값으로만 적는다**(유저 승인 2026-09-22) ([`p4-three-empty-values`](kb/dev/decision/p4-three-empty-values/conclusion.md)). `없음`은 찾아봤으나 없다는 뜻이고, `해당 없음`은 적용되지 않는다는 뜻이며, `미확정`은 아직 모른다는 뜻이다. `N/A`와 `TBD`, `미정`, 단독 대시를 쓰지 않고 자리를 비워 두지도 않는다. 단일 정의 위치는 `tools/kb_lib.py`의 상수 하나다.
- **[지킴]** 세 값 밖의 빈 값 표기는 `chunk_lint`의 게이트 `empty-value`가 거부하며, 대상은 살아 있는 단위 지식이다(2026-09-22 승격) ([`p4-three-empty-values`](kb/dev/decision/p4-three-empty-values/conclusion.md)).
- **[지킴]** **슬롯에는 그 슬롯의 질문에 답하는 문장만 쓴다** ([`p4-slot-answers-one-question`](kb/dev/decision/p4-slot-answers-one-question/conclusion.md)). 그래서 다른 슬롯의 답과 "다음과 같다"나 "이 절에서는" 같은 메타 문장, "특이사항 없음"이나 "추후 결정" 같은 채움의 첨가 셋을 쓰지 않고, 채움 자리에는 세 빈 값을 쓴다. 예산은 상한이지 목표가 아니다.
- **[지킴]** **슬롯 표지는 자리로 판정한다**(2026-09-29) ([`p4-slot-marker-by-position`](kb/dev/decision/p4-slot-marker-by-position/conclusion.md)). `**결론**`, `**요구**`, `**자극**` 같은 굵은 표지는 그 줄의 **필드 머리**에 있을 때만 슬롯이고, 필드 머리는 줄 시작과 목록 항목 표지 `- ` 바로 다음, 같은 줄에서 앞선 필드를 끝낸 ` · ` 바로 다음이다. 반면 표 셀 뒤와 산문 접속 뒤, 문장 중간의 굵은 span은 강조이지 표지가 아니다. `**대안 없음**`처럼 표지 뒤에 붙은 한정어는 12자 이하이고 마침표가 없으며, 꼴이 괄호(`(미확정)`), 대시(` — 미확정`), 낱말 ` 없음` 셋 중 하나일 때만 같은 표지다(2026-10-24). 그 밖의 꼴(`**자극 열**`)과 길거나 마침표가 있는 것은 표지 낱말로 시작하는 별개의 굵은 span이다. 이 규칙은 일곱 틀 전부에 같고, 판정 함수는 `chunk2kg.body_slot_mark` 하나이고 방출과 게이트 `decision-role`이 함께 쓴다(2026-10-24). 표지 낱말끼리 접두가 겹치면 `kb_lib`가 로드 시점에 죽는다.
- **[지킴]** **목록 규칙**은 다섯이다 ([`p4-slot-answers-one-question`](kb/dev/decision/p4-slot-answers-one-question/conclusion.md)). 순서 목록의 모든 항목을 `1.`로 적는데, `2.` 이상의 손 번호는 항목을 넣고 뺄 때 어긋나고 내용 변경이 아닌데도 `contentHash`를 바꾸기 때문이다. 항목은 9개 이하, 중첩은 2단계 이하, 길이는 항목당 240자 이하이고, 산문을 110~120자에서 손으로 접기 때문에 길이는 소스 줄이 아니라 글자로 잰다. 빈 목록 대신 `없음`을 적는다.
- **[지킴]** 첨가와 목록 규칙 위반은 `chunk_lint`의 게이트 `addition`·`list-rules`가 거부한다(2026-09-22 승격) ([`p4-slot-answers-one-question`](kb/dev/decision/p4-slot-answers-one-question/conclusion.md)).
- **[지킴]** **그림은 캡션 한 줄로 시작하고 캡션에 번호를 쓰지 않는다** ([`p0-figure-caption-and-source`](kb/dev/decision/p0-figure-caption-and-source/conclusion.md)). 번호는 표시용이라 소스에 두지 않는데, 항목을 넣고 뺄 때 번호가 어긋나기 때문이며 목록 규칙과 같은 이유다.
- **[지킴]** 다이어그램은 `mermaid`나 `svg`, `plantuml` 같은 **소스 펜스**로 두고, 이미지 파일은 소스가 없을 때만 쓴다 ([`p0-figure-caption-and-source`](kb/dev/decision/p0-figure-caption-and-source/conclusion.md)). 소스는 고칠 수 있고 diff가 읽히지만 이미지는 둘 다 아니기 때문이다.
- **[권장]** 기호·색의 뜻이 자명하지 않으면 "읽는 법"을 명사구 셋 이하로 붙인다 ([`p0-figure-caption-and-source`](kb/dev/decision/p0-figure-caption-and-source/conclusion.md)).

### 강인성 세 축과 게이트 대응

| 축 | 위협 | 방어 | 게이트 |
|---|---|---|---|
| anti-drift | 어휘가 조용히 갈라짐 | `agt:` 어휘 통제, 표준어 우선 | `validate.py`의 vocab, labels, boundary 검사 |
| anti-rot | 컨텍스트가 무한히 커짐 | 1,092 토큰 상한, 라벨 목록 우선 읽기 | `chunk_lint.py`, SHACL `tokenCount` |
| anti-orphan | 쓰이지 않는 지식이 쌓임 | 복합체·링크 연결, 고아율 관측 | 없음 ([`docs/tools.md`](docs/tools.md) §게이트 밖) |

## §1. 온톨로지 (`kb/ontology/**/*-ontology.ttl`)

온톨로지의 파일 하나는 단위 지식 하나이고 디렉토리 하나는 모듈 하나이며, 그 모듈은 Bazel 패키지다.

- **[지킴]** 새 개념은 **주제가 맞는 기존 모듈 디렉토리의 새 파일**로 추가하고, 새 주제는 **새 모듈 디렉토리**로 추가한다 ([`p2-ontology-file-is-a-chunk`](kb/dev/decision/p2-ontology-file-is-a-chunk/conclusion.md)). 새 모듈은 `project-ontology.ttl`의 `owl:imports`와 `//kb/ontology:modules`에 손으로 등록한다. 반면 모듈의 `BUILD.bazel`과 `modules.bzl`은 `tools/gen_build.py`가 생성한다.
- **[지킴]** 한 개념은 정확히 한 파일에서 정의된다 ([`p2-ontology-file-is-a-chunk`](kb/dev/decision/p2-ontology-file-is-a-chunk/conclusion.md)). 그래서 다른 파일에서 재정의하거나 재선언하지 않고 다른 모듈의 개념은 참조만 한다(boundary 게이트).
- **[지킴]** 모든 `agt:` 클래스와 속성, 개체에 `rdfs:label` 한/영 각 1과 한글 `skos:definition`을 단다 ([`p0-notation-format`](kb/dev/decision/p0-notation-format/conclusion.md), [`p0-genus-differentia-definition`](kb/dev/decision/p0-genus-differentia-definition/conclusion.md)).
- **[지킴]** 정의에는 그 개념이 딛고 선 근거를 적는다 ([`p2-competency-questions`](kb/dev/decision/p2-competency-questions/conclusion.md)). 근거 없는 개념은 온톨로지 과설계의 시작이므로, 역량 질문에 기여하지 않는 개념은 만들지 않는다.
- **[지킴]** 본문은 토큰 상한 1,092 이하다 ([`p1-chunk-unit-is-tokens`](kb/dev/decision/p1-chunk-unit-is-tokens/conclusion.md)). `@prefix`·주석·빈 줄은 제외한다.
- **[지킴]** 파일은 주제를 적은 상단 배너 주석 1줄로 시작하고, 이어서 `@prefix` 블록을 agt, owl, rdfs, skos, xsd 순으로 둔 뒤 개념 블록들을 둔다 ([`p2-ontology-ttl-layout`](kb/dev/decision/p2-ontology-ttl-layout/conclusion.md)).
- **[지킴]** 개념 블록의 술어는 `a`, `rdfs:subClassOf`/`owl:disjointWith`, `rdfs:domain`, `rdfs:range`, `rdfs:label`, `skos:definition`의 순서로 쓰고, `rdfs:label`은 en, ko 순으로 적는다 ([`p2-ontology-ttl-layout`](kb/dev/decision/p2-ontology-ttl-layout/conclusion.md)).
- **[지킴]** 상위 온톨로지와 prov, skos, co 같은 외부 어휘의 정의를 변경하지 않는다 ([`p0-agt-namespace`](kb/dev/decision/p0-agt-namespace/conclusion.md), [`p2-ontology-module-structure`](kb/dev/decision/p2-ontology-module-structure/conclusion.md)).
- **[권장]** 동의어는 새 개념이 아니라 `skos:altLabel`로 등록한다 ([`p0-skos-label-synonyms`](kb/dev/decision/p0-skos-label-synonyms/conclusion.md)).

## §2. SHACL shape (`kb/ontology/shapes/*-shapes.ttl`)

- **[지킴]** 파일 하나가 검사 대상 하나 또는 밀접한 쌍을 담는다 ([`p4-shape-file-per-target-with-message`](kb/dev/decision/p4-shape-file-per-target-with-message/conclusion.md)). 파일명은 `<대상>-shapes.ttl`이다.
- **[지킴]** 모든 property shape에 `sh:message`를 달고, 메시지에 강제하는 규칙을 적는다 ([`p4-shape-file-per-target-with-message`](kb/dev/decision/p4-shape-file-per-target-with-message/conclusion.md)). 그래야 FAIL이 곧 수정 방향 안내가 된다.
- **[지킴]** shape는 **강화만** 하고, 기존 제약을 약화하는 변경은 유저 승인 사항이다 ([`p4-shape-only-strengthens`](kb/dev/decision/p4-shape-only-strengthens/conclusion.md)). maxCount 완화와 `sh:in` 확장이 약화의 예다.
- **[지킴]** 값을 갖는 property shape에는 형을 단다 ([`p4-shape-values-are-typed`](kb/dev/decision/p4-shape-values-are-typed/conclusion.md)). 문자열과 정수에는 `sh:datatype`, 개체에는 `sh:class`, 참조에는 `sh:nodeKind sh:IRI`를 달고, 범위가 있으면 `sh:minInclusive`·`sh:maxInclusive`, 닫힌 집합이면 `sh:in`을 단다. 형이 없는 값은 문자열로 남아 "이상·이하·약"이 산문에 머문다(유저 승인 2026-09-23, M5).
- **[권장]** 닫힌 값 목록인 `sh:in`의 원천은 온톨로지 정의의 서술과 일치시킨다 ([`p4-shape-values-are-typed`](kb/dev/decision/p4-shape-values-are-typed/conclusion.md)).

## §3. ODD (`kb/odd/*-odd.yml` — OpenODD 문서. `*-odd.ttl`·`taxonomy.yml`은 생성물, 손으로 쓰지 않는다)

작성 절차는 [`docs/method.md` §2](docs/method.md#2-odd-작성)에 있다.

- **[지킴]** 조건 개체는 `id:cond-<slug>`이고, 타입은 `agt:StaticElement` / `agt:EnvironmentalCondition` / `agt:DynamicElement`의 3분류 중 하나다 ([`p3-condition-entity-from-odd-document`](kb/dev/decision/p3-condition-entity-from-odd-document/conclusion.md), [`p0-condition-taxonomy-extensible`](kb/dev/decision/p0-condition-taxonomy-extensible/conclusion.md)).
- **[지킴]** 모든 조건에 `agt:conditionValue`와 `agt:checkMethod`, `agt:verificationGrade`를 단다 ([`p0-condition-taxonomy-extensible`](kb/dev/decision/p0-condition-taxonomy-extensible/conclusion.md)). 판정 방법은 **객관적 관측 수단**이어야 하므로 "정상이다"가 아니라 "명령 X가 Y를 반환한다"의 꼴로 적는다.
- **[지킴]** 조건은 ODD 개체의 `agt:hasCondition` 목록에 등록하고, 등록 없는 조건을 만들지 않는다 ([`p3-condition-entity-from-odd-document`](kb/dev/decision/p3-condition-entity-from-odd-document/conclusion.md)).
- **[지킴]** 검토했으나 밖에 두는 것은 **명시 제외**로 기록한다 ([`p3-condition-entity-from-odd-document`](kb/dev/decision/p3-condition-entity-from-odd-document/conclusion.md)). ODD 문서의 `EXCLUSIONS_REVIEWED`에는 `concept`와 YYYY-MM 꼴의 `reviewed`, `reason`을 적고, 그래프의 `agt:excludes` 서식은 `"<대상> — reviewed YYYY-MM, 이유: <근거>"`다.
- **[권장]** 판정 등급 C·D인 조건은 판정 방법을 개선하거나 ODD에서 빼고 가정으로 내린다 ([`p0-condition-taxonomy-extensible`](kb/dev/decision/p0-condition-taxonomy-extensible/conclusion.md), [`p3-measurement-method-grades`](kb/dev/decision/p3-measurement-method-grades/conclusion.md)).

## §4. 지식 (`kb/{dev,vv}/**/*.md`)

한 파일은 frontmatter(head)와 본문(assertion)으로 이루어지고, 형식은
[`docs/rules.md` §1](docs/rules.md#1-chunk--자립적-최소-지식-단위)에 있다. head 그래프는
`//kg:chunks_kg`가 생성하므로 `kg/`에 손으로 쓰지 않는다.

- **[지킴]** 한글 용어는 [`docs/glossary.md`](docs/glossary.md)의 표준 용어만 쓰고, 은유나 조어를 새로 만들지 않는다 ([`p0-terms-from-glossary`](kb/dev/decision/p0-terms-from-glossary/conclusion.md)). 가로대와 사다리, 상승, 하강, 장부, 봉사, 거주표가 그런 조어의 예다. 용어집에 없는 개념은 표준어를 찾아 용어집에 먼저 추가한다(유저 결정 2026-09-10, 원장 19).
- **[지킴]** frontmatter 필수 키는 `id`, `type`, `level`, `title_ko`, `title`, `status`, `generated`다(OKF v0.2 사상, 노트 E.2) ([`pe-three-layer-binding`](kb/dev/decision/pe-three-layer-binding/conclusion.md)). 선택 키는 `verified`와 `sources`, `assumes`, 요구에만 쓰는 `pattern`, 복원 링크의 표시 `restored`, 분할 조각의 `specializationOf`, 위험에서 파생된 항목의 `exposes`다. `pattern`의 값은 EARS 패턴이고, 패턴은 `ubiquitous`, `event-driven`, `state-driven`, `unwanted-behaviour`, `optional`, `complex`다. `restored`는 같은 단위 지식의 링크 대상 IRI 목록이고 그 증거가 `proposal`이 된다([`p10-restored-link-marking`](kb/dev/decision/p10-restored-link-marking/conclusion.md)). `specializationOf`는 같은 지식 종류인 원 단위 지식의 IRI 하나다([`p10-split-keeps-work-identity`](kb/dev/decision/p10-split-keeps-work-identity/conclusion.md)). `exposes`는 그 항목이 노출하려는 결함 요인 개체의 `agt:` IRI 목록이며, 링크 키가 아니라 `agt:exposesFactor`로 나가고 게이트 `shacl`의 exposes-factor 검사가 맡는다. `type`과 `status`, `generated`, `verified`는 **OKF v0.2 필드명**이고, 이 저장소의 단위 지식 트리 `kb/`는 OKF 번들이다. 값 어휘의 원본은 둘로 갈린다(2026-09-27). `PLANES`와 `LEVELS`, `STATES`는 **`defs/kb.bzl`**이 원본이고 `tools/chunk2kg.py`는 그 표를 리터럴로 읽어 파생하는데, Starlark는 파일을 읽지 못하므로 분석 시점 판정을 지키려면 표가 거기 있어야 하기 때문이다. `PLANE_CLASS`·`REQUIRED`는 `chunk2kg.py`가 원본이며, `PLANE_CLASS`의 키 집합이 `PLANES`와 다르면 로드 시점에 죽는다. 폴백은 없어서 `defs/kb.bzl`을 입력으로 받지 못한 액션은 `EXIT_CONFIG`로 끝난다.
- **[지킴]** `generated: {by, at}`의 `by`는 OKF 행위자 표기이며, 도구는 `<생성기>/<버전>`, 사람은 `human:<id>`로 적는다 ([`p2-trust-tier-from-generated-and-verified`](kb/dev/decision/p2-trust-tier-from-generated-and-verified/conclusion.md)). **검증하지 않은 것을 `verified`에 적지 않는다.** 미검증이 정직한 상태이고, 검증 뒤 내용을 고치면 재검증 항목을 덧붙일 때까지 게이트가 거부한다. `verified`는 판정 이력이라 덮어쓰지 않고 누적한다. **다만 `artifact` 지식 종류는 예외다.** 코드 단위 지식의 `verified`는 사람 도장이 아니라 `process:bazel-test`와 리비전으로 된 **테스트 통과 도장**이고, 수정마다 재검증이 자동으로 일어난다(`p7-code-extraction-direction`, 2026-09-30).
- **[지킴]** 예약 파일명 `index.md`·`log.md`를 쓰지 않는다(OKF) ([`pe-three-layer-binding`](kb/dev/decision/pe-three-layer-binding/conclusion.md), [`pe-storage-layout`](kb/dev/decision/pe-storage-layout/conclusion.md)).
- **[지킴]** IRI는 `https://agentic-knowledge-base.dev/id/chunk/<uuid4>`이고 내용을 IRI에 넣지 않는다 ([`p0-iri-design`](kb/dev/decision/p0-iri-design/conclusion.md)). 사람이 읽는 이름은 라벨이 맡는다.
- **[지킴]** 본문은 토큰 상한인 저작 산문 1,092와 인용 2,856 이하이고, frontmatter와 앞뒤 빈 줄은 제외한다 ([`p1-chunk-unit-is-tokens`](kb/dev/decision/p1-chunk-unit-is-tokens/conclusion.md), [`p4-one-file-one-topic`](kb/dev/decision/p4-one-file-one-topic/conclusion.md)). 주제는 하나이며 라벨만 보고 본문을 예측할 수 있어야 한다.
- **[지킴]** 지식 종류마다 본문 형식이 정해져 있다 ([`p7-dev-plane-substance`](kb/dev/decision/p7-dev-plane-substance/conclusion.md)).
  - **[지킴]** `decision`은 역할 태그 `**결론**`, `**근거**`, `**대안**`을 쓰고, 대안에는 기각 사유를 포함한다 ([`p7-alternatives-mandatory`](kb/dev/decision/p7-alternatives-mandatory/conclusion.md)). 세 단위 지식은 전부 필수이며 `kb_decision` 규칙과 `gen_build`가 로드 시점에 이를 강제한다(2026-09-11).
  - **[지킴]** `annotation`은 주석이다 ([`p7-commentary-form`](kb/dev/decision/p7-commentary-form/conclusion.md)). 첫 줄은 `<라벨> (<장식>): <요지>`이고, 라벨 일곱 `praise`, `nitpick`, `suggestion`, `issue`, `question`, `thought`, `chore`와 장식 셋 `blocking`, `non-blocking`, `if-minor`는 닫힌 어휘다. 이어서 `targets`와 일치하는 IRI를 담은 `대상:`, 4문장 이하의 `본문:`, 선택 사항인 `제안:`, 그리고 `열림`, `해소`, `기각` 가운데 하나와 한 줄 이유를 담은 `해소:`를 적는다. `issue (blocking)`이면서 `해소: 열림`인 주석만 게이트를 막는다.
  - **[지킴]** `memory`는 관측된 실행 기록 `agt:Run`이며 자극과 환경, 결과를 담는다 ([`p0-run-is-an-append-only-memory-chunk`](kb/dev/decision/p0-run-is-an-append-only-memory-chunk/conclusion.md)). `memory`는 구체 수준 전용이고, `kb/vv/run/`의 단위 지식 파일 하나가 기록 하나다. 대응 절차는 `agt:Runbook`으로 가른다. 기록은 append-only다(`r-026`). 그래서 **커밋된 기록은 표기가 바뀌어도 소급하지 않고**, 표기 변경은 앞으로의 기록부터 적용한다.
  - **[지킴]** 기록의 표 머리가 바뀌면 게이트는 기록 시각(frontmatter `generated.at`)으로 머리를 가린다 ([`p0-run-is-an-append-only-memory-chunk`](kb/dev/decision/p0-run-is-an-append-only-memory-chunk/conclusion.md)). 전환 시각 이전 기록은 옛 머리만, 이후 기록은 새 머리만 받고, 시각을 읽지 못한 기록에는 새 머리를 요구한다. 전환 시각의 단일 정의 위치는 `tools/kb_lib.py`의 `RECORD_HEADER_SINCE`다. 판정 로그의 `입력 해시값` 열과 실행 기록의 `테스트 케이스` 열이 2026-10-25에 이 규칙으로 바뀌었다(Q-0065#Q161).
  - **[지킴]** `contract`와 `schema`, `artifact`의 본문은 각각 언어 네이티브 선언과 스키마, 코드다 ([`p7-dev-plane-substance`](kb/dev/decision/p7-dev-plane-substance/conclusion.md)).
- **[지킴]** 복합체를 저작할 때는 부분 중 하나의 frontmatter에 `composite: {id, title_ko, title}`를 한 번 선언하고 부분 전부에 `part_of`를 적는다 ([`p4-composite-declared-in-frontmatter`](kb/dev/decision/p4-composite-declared-in-frontmatter/conclusion.md), [`p4-composite-as-part-of`](kb/dev/decision/p4-composite-as-part-of/conclusion.md)). 부분은 **같은 디렉토리, 곧 같은 패키지**에 두고 지식 종류와 정제 수준을 같게 하는데, 묶음은 액션의 입력 집합이고 입력 집합은 패키지를 넘지 못하기 때문이다. 부분은 2~9개이고 선언하는 단위 지식의 파일 이름이 타깃 이름이 된다. 다만 결정은 예외여서 `<파트>-<슬러그>/` 디렉토리에 단위 지식 셋과 선택 `conventions.md`를 두고 `kb_decision`이 세운다(2026-09-29, `p4-convention-slot`).
- **[지킴]** **선택 키 `layer: knowledge | methodology | process`는 그 항목이 서비스의 어느 층에서 역할을 갖는가를 나타낸다** ([`p0-service-is-a-three-layer-wiki`](kb/dev/decision/p0-service-is-a-three-layer-wiki/conclusion.md)). 이 키는 지식 종류와 직교하는 역할 속성이다. **명시가 없으면 `knowledge`다.** `chunk2kg`가 기본값을 방출하므로 표시 누락이 산발로 세어지지 않는다. 방법론과 프로세스는 명시한다. 코드 단위 지식에는 손으로 적지 않는다. 대신 등록부 `tools/<모듈>.chunks.yml`의 `layer`가 원본이고, 추출기가 그 값을 정의와 절, 파일 단위 지식 전부로 옮긴다. 값이 어휘 밖이면 `chunk2kg`가 거부하고, 개수는 shape `layer-shapes.ttl`이 본다(2026-10-01).
- **[지킴]** 순서가 뜻을 갖는 복합체만 선언하는 단위 지식의 `composite:`에 선택 키 `ordered: [<부분 IRI>…]`를 더하고, 이 목록은 부분 전부를 빠짐없이 한 번씩 담는다(2026-09-29) ([`p4-composite-order-is-declared`](kb/dev/decision/p4-composite-order-is-declared/conclusion.md)). 키가 없으면 순서가 없고 **예외는 없다**(유저 승인 2026-09-29). 따라서 결정 기록의 선언은 `kb_decision`의 `ordered` 인자로 `gen_build`가 넣으며, 205개 `conclusion.md`를 손으로 고치지 않는다. 도구는 역할 이름으로 순서를 추측하지 않는다.
- **[지킴]** `kb/vv/scenario/`의 V&V 시나리오를 이루는 세 단위 지식의 파일 이름은 `<슬러그>-stimulus.md`, `<슬러그>-factors.md`, `<슬러그>-excluded.md`이고, 역할 태그는 각각 `**자극**`, `**요인**`, `**배제 자극**`이며, 선언하는 단위 지식은 `-stimulus`다 (2026-09-29) ([`p8-scenario-authoring`](kb/dev/decision/p8-scenario-authoring/conclusion.md)). 시나리오 묶음은 읽기 순서가 정해져 있으므로 `ordered`가 **필수**이고, 없으면 `gen_build`가 거부한다.
- **[지킴]** 아직 모르는 것은 본문의 선택 슬롯 **`미확정:`**에 적는다 ([`p4-three-empty-values`](kb/dev/decision/p4-three-empty-values/conclusion.md)). 미결은 문서가 아니라 항목 안에 있고 집계는 생성물이므로, 답이 오면 고칠 자리가 하나다.
- **[지킴]** **전제가 있으면 가정을 만들고 `assumes`로 가리킨다** ([`p0-premise-as-assumption`](kb/dev/decision/p0-premise-as-assumption/conclusion.md)). 가정은 ODD 조건 위의 명제다. 고유 전제를 아직 적지 않은 단위 지식은 기본 가정 `id:asm-chunk-conventions`를 `assumes`하고, 실제 전제가 드러나면 고유 가정을 앞에 더한다. 따라서 기본 가정만 가진 항목은 전제를 아직 적지 않은 항목이며, 리뷰가 그런 항목을 잡는다.
- **[지킴]** 본문을 고치면 라벨이 여전히 대표하는지 재검토한다 ([`p4-one-file-one-topic`](kb/dev/decision/p4-one-file-one-topic/conclusion.md)).
- **[권장]** 상한 근처로 억지 압축하지 않고 분할 신호를 따른다 ([`p4-compression-repeat-is-split-signal`](kb/dev/decision/p4-compression-repeat-is-split-signal/conclusion.md)).

## §5. 지식그래프 A-Box (`kg/*-kg.ttl`)

- **[지킴]** head는 생성 산출물이므로 손으로 쓰지 않는다 ([`pe-kg-hand-and-generated-files`](kb/dev/decision/pe-kg-hand-and-generated-files/conclusion.md)). 여기 두는 것은 가정과 출처 문서, 복합체, 역할, 적용 범위, 채널, 하네스다.
- **[지킴]** 개체 IRI의 꼴은 개체가 어디서 서는가로 정한다 ([`p0-entity-iri-forms`](kb/dev/decision/p0-entity-iri-forms/conclusion.md)). 단위 지식 파일의 frontmatter에서 서는 단위 지식·복합체는 불투명 uuid4 경로인 `id/chunk/<uuid4>`와 `id/composite/<uuid4>`이고, 그 밖의 개체는 `id:` 네임스페이스의 `<kind>-<slug>` 소문자 케밥이다. 접두사 표는 [`docs/rules.md` §개체 IRI 접두사](docs/rules.md#개체-iri-접두사)에 있다. 표에 없는 접두사가 그래프에 나타나면 그 접두사 자체가 드리프트 신호다.
- **[지킴]** 카탈로그 `catalog-kg.ttl`이 완전하다는 것은 하네스가 `agt:hasRole` 하는 모든 역할이 대응 적용 범위를 갖고, 하네스가 그 적용 범위를 `agt:grants` 한다는 뜻이다 ([`p11-catalog-role-has-granted-scope`](kb/dev/decision/p11-catalog-role-has-granted-scope/conclusion.md)).
- **[지킴]** 출처와 귀속, 버전은 PROV-O만 쓴다 ([`p4-chunk-as-four-named-graphs`](kb/dev/decision/p4-chunk-as-four-named-graphs/conclusion.md), [`p0-agt-namespace`](kb/dev/decision/p0-agt-namespace/conclusion.md)). 술어는 `prov:wasDerivedFrom`, `prov:wasAttributedTo`, `prov:generatedAtTime`, `prov:atLocation`이다.
- **[지킴]** 라벨 목록 읽기가 기본 접근이므로 개체에도 한글과 영어 라벨을 단다 ([`pe-kg-hand-and-generated-files`](kb/dev/decision/pe-kg-hand-and-generated-files/conclusion.md)).
- **[지킴]** 파일 상단 배너에 담는 개체 종류와 "손으로 쓰지 않는 것"을 적는다 ([`pe-kg-hand-and-generated-files`](kb/dev/decision/pe-kg-hand-and-generated-files/conclusion.md)).
- **[권장]** ID는 재사용하지 않으므로 폐기는 `state`/`deprecated`로 남기고 새 IRI를 만든다 ([`p10-split-keeps-work-identity`](kb/dev/decision/p10-split-keeps-work-identity/conclusion.md), [`p0-deprecate-not-delete`](kb/dev/decision/p0-deprecate-not-delete/conclusion.md)). 분할에서는 조각 하나가 uuid를 승계하고 나머지를 `specializationOf`로 이으며, 병합은 `supersedes`로 잇는다. 출처는 `prov:wasDerivedFrom`으로 적는다.

## §6. Bazel (`BUILD.bazel`, `defs/*.bzl`)

- **[지킴]** 지식 파일은 반드시 어떤 `filegroup`에 속하고, 그 filegroup은 어떤 게이트 테스트의 입력이다 ([`pe-knowledge-files-are-gate-inputs`](kb/dev/decision/pe-knowledge-files-are-gate-inputs/conclusion.md)). 어느 게이트도 검사하지 않는 지식 파일이 이 하네스의 고아(orphan)다.
- **[지킴]** 게이트는 `defs/knowledge.bzl`의 매크로로만 선언한다 ([`pe-knowledge-files-are-gate-inputs`](kb/dev/decision/pe-knowledge-files-are-gate-inputs/conclusion.md)). `py_test`를 직접 쓰지 않는다.
- **[지킴]** 모듈 디렉토리가 Bazel 패키지다 ([`pe-knowledge-files-are-gate-inputs`](kb/dev/decision/pe-knowledge-files-are-gate-inputs/conclusion.md)). 패키지의 `filegroup` 이름은 디렉토리 이름과 같게 한다.
- **[지킴]** 생성물은 `bazel-out`에만 존재하므로 소스 트리에 같은 이름의 파일을 두지 않는다 ([`pe-generated-outputs-stay-in-bazel-out`](kb/dev/decision/pe-generated-outputs-stay-in-bazel-out/conclusion.md)). 다만 생성 트리 파일 셋은 예외다. 그 셋은 생성 BUILD와 `.claude/skills/`의 SKILL.md, 규범 문서이고, 각각 `//:build_drift_test`와 `//:skills_drift_test`, `//:norms_drift_test`가 재생성 결과와 비교하며, 세 파일은 손으로 고치지 않는다.
- **[권장]** `glob`은 패키지 안 한 디렉토리 깊이만 대상으로 한다 ([`pe-knowledge-files-are-gate-inputs`](kb/dev/decision/pe-knowledge-files-are-gate-inputs/conclusion.md)).

## §7. 도구 (`tools/*.py`)

- **[지킴]** 게이트 도구는 실패하면 비영 코드로 종료하면서 `FAIL [검사명]` 접두사와 근거 인용을 내므로, 메시지가 곧 수정 안내다 ([`p6-gate-catalogue`](kb/dev/decision/p6-gate-catalogue/conclusion.md)).
- **[지킴]** shape나 게이트 코드를 삭제하거나 완화해 검사를 약화하는 변경은 유저 승인 사항이다 ([`p6-weakening-a-check-needs-user-approval`](kb/dev/decision/p6-weakening-a-check-needs-user-approval/conclusion.md)). 반면 면제는 약화가 아니어서 orchestrator가 판정하고 `docs/waivers.md`에 선언해 공개한다(Q7-b).
- **[지킴]** 규약 상수의 단일 정의 위치는 `tools/kb_lib.py`이고 다른 파일에 복제하지 않는다 ([`p6-gate-tool-code-structure`](kb/dev/decision/p6-gate-tool-code-structure/conclusion.md)). 다만 값이 `kb_lib` 밖에 적히는 자리가 둘 있다. 분석 시점에 쓰이는 표인 `GATES`, `RESIDENCY`, `EXTRACTED_SOURCES`, `USES_TARGETS`는 `defs/kb.bzl`의 리터럴이고 `kb_lib`이 그 리터럴을 읽어 파생한다. 본문 떼기와 토큰 계수기, `PLANES`와 `LEVELS`, `STATES` 리터럴 읽기는 `tools/chunk2kg.py`에 있고 `kb_lib`이 그 이름을 다시 내보낸다.
- **[권장]** 새 검사는 독립 함수 `check_*() -> list[str]`로 추가하고 `main`에서 합류한다 ([`p6-gate-tool-code-structure`](kb/dev/decision/p6-gate-tool-code-structure/conclusion.md)).

## §8. 소통 채널 (`harness/channel/` · `harness/user/`)

채널 파일은 지식이 아니라 소통 기록이어서 **그래프 밖**에 있고 어휘·shape 검사 대상이 아니며,
§6의 filegroup 규칙에서 제외되는 유일한 문서군이다. 프로토콜 원본은
[`harness/README.md`](harness/README.md)이고, 질문지 규약 원본은 그 문서의 유저 채널 절이 가리킨다.
채널 파일의 형식은 `//harness:channel_lint_test`가 강제한다.

- **[지킴]** 에이전트 채널은 단일 작성자라서 `to_orchestrator/`에는 interpreter(하위 역할 hci 포함)만, `to_interpreter/`에는 orchestrator만 쓴다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)). 쓰기는 `harness/scripts/send.sh`로, 상태 전이는 수신자가 `harness/scripts/mark.sh`로 한다.
- **[지킴]** 메시지 하나에는 주제 하나만 담고, `task` 하나가 반영 단위이므로 큰 작업은 쪼개어 보낸다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)).
- **[지킴]** `status` 어휘는 채널마다 달라 섞지 않는다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)). 메시지는 `new→read→in_progress→done | blocked`, 질문지는 `open→answered→closed`다. `answered`는 유저가 쓰며, hci 세션에서 답을 알린 경우에는 hci가 대신 쓴다.
- **[지킴]** `task`는 배경, 목표, 완료조건, 제약, 파급효과, 확인 못 한 것의 필수 절 여섯을 갖춘다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)). `result`·`answer`는 `re`로 원 메시지를 가리키고 `result` 없는 `task`는 `done`이 될 수 없다.
- **[지킴]** **유저에게 결정은 항상 파일 질문지로 요청한다** ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)). 채팅에는 질문지를 만들었다는 안내와 요지만 쓰고, 유저가 채팅으로 먼저 답하면 hci가 그 답을 질문지에 원문으로 옮겨 적는다.
- **[지킴]** 메시지와 질문지는 지식을 **식별자**(결정 slug, `agt:`, `id:`, IRI, 조건 id, `file:line`)로 가리키고, slug와 `agt:`, `id:` 옆에는 그 한글 이름을 함께 적는다(Q-0052 Q103 답) ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)). 게이트 `channel`이 판정한다.
- **[지킴]** 유저 판단을 요청하는 질문은 **다섯 가지**를 갖춘다 ([`p11-user-question-has-five-parts`](kb/dev/decision/p11-user-question-has-five-parts/conclusion.md)). 다섯 가지는 왜 어려운가를 포함한 질문과 이미 정해진 것, 측정치인 현재 상태, 답이 가르는 것, 선택지다. 한 줄 질문은 답을 받지 못한다. 선택지마다 비용을 적고 `**권장:**`으로 권장안을 붙인다(유저 지적 2026-09-02).
- **[지킴]** 유저에게 묻는 것은 확정 권한과 방향, 비용이 큰 선택, 새 파일, 검사의 약화로 좁히고, 구현 선택은 orchestrator가 정해 `result`에 적는다 ([`p11-user-question-has-five-parts`](kb/dev/decision/p11-user-question-has-five-parts/conclusion.md)). 선택지마다 끝에 "권한·방향: 바꾼다" 또는 "권한·방향: 그대로"를 적는다(Q-0060#Q140).
- **[지킴]** 채널·질문지 경로는 소멸하므로 본문 인용원이 되지 못하고 근거는 질문 번호로 적는다 ([`p11-harness-two-channels`](kb/dev/decision/p11-harness-two-channels/conclusion.md)). 면제는 코드가 아니라 `docs/waivers.md`에 선언한다(2026-09-12).

## §9. 생성 문서 (`bazel-bin/**/*.md` · 생성 트리 파일)

생성 문서는 도구가 내는 마크다운이고 사람이 쓰지 않는다. 생성 문서를 쓰는 것은 **생성기**이므로 이 절의
대상은 `tools/*.py`의 출력 문자열이다. 규약의 원본은 결정
[`p12-generated-document-header`](kb/dev/decision/p12-generated-document-header/conclusion.md),
[`p12-generated-document-form`](kb/dev/decision/p12-generated-document-form/conclusion.md),
[`p12-generated-documents-are-gated`](kb/dev/decision/p12-generated-documents-are-gated/conclusion.md) 셋이고,
구현의 단일 정의 위치는 `tools/kb_lib.py`이며, 게이트 `gendoc`이 이 규약을 강제한다. 외부 출처는
[`docs/references.md`](docs/references.md) §생성 문서 작성에 있다.

- **[지킴]** 머리는 h1 한 줄과 여섯 줄이다 ([`p12-generated-document-header`](kb/dev/decision/p12-generated-document-header/conclusion.md)). 여섯 줄의 순서는 `생성기`, `생성 시각`, `입력`, `질의`, `재현`, 성격 경고다. h1은 `# <이름> — <목적> (생성 파일)`로 끝난다.
- **[지킴]** `생성기`는 OKF 행위자 표기 `<생성기>/<버전>`을 쓰고, `생성 시각`은 ISO 8601 UTC 초 해상도다 ([`p12-generated-document-header`](kb/dev/decision/p12-generated-document-header/conclusion.md)). `입력`에는 개수만 적지 않고 파일 **목록**과 해시값 `sha256:<앞 12자>`를 적는다. `재현`은 **자기 자신을** 다시 만드는 명령이다.
- **[지킴]** 드리프트 검사가 바이트 비교를 하는 생성 트리 파일인 `.claude/skills/*/SKILL.md`와 생성 BUILD에는 생성 시각과 해시값을 넣지 않는다 ([`p12-generated-document-header`](kb/dev/decision/p12-generated-document-header/conclusion.md)). 그 자리의 건전성 장치는 결정론이다.
- **[지킴]** 제목 계층은 한 단계씩 내려가고 h1은 문서당 하나다 ([`p12-generated-document-form`](kb/dev/decision/p12-generated-document-form/conclusion.md)). 표는 헤더 행을 갖고, 모든 행의 열 수가 같으며, 앞뒤에 빈 줄이 있다. 펜스에는 언어를 명시한다.
- **[지킴]** 본문이 120줄을 넘으면 목차 절을 두고, 앵커는 `doccheck`의 `slug`로 만든다 ([`p12-generated-document-form`](kb/dev/decision/p12-generated-document-form/conclusion.md)).
- **[지킴]** 링크는 **생성물이 놓이는 위치 기준으로** 실재해야 한다 ([`p12-generated-document-form`](kb/dev/decision/p12-generated-document-form/conclusion.md)). 생성물은 소스 트리와 다른 곳에 놓이므로 소스 기준 상대경로는 성립하지 않는다.
- **[지킴]** 빈 값은 `없음` 하나로 적고, 표 셀을 비우거나 대시로 두지 않는다 ([`p12-generated-document-form`](kb/dev/decision/p12-generated-document-form/conclusion.md)). 절은 비어도 제목을 남긴다.
- **[지킴]** 비율은 `n/d = p.p%` 꼴에 소수 한 자리로 적고, 분모 없는 백분율은 쓰지 않는다 ([`p12-generated-document-form`](kb/dev/decision/p12-generated-document-form/conclusion.md)). 0 분모는 `없음`이다. 자릿수 상수는 `kb_lib`에 하나만 둔다.
- **[지킴]** 산문은 §0의 단정 서술형이다 ([`p12-generated-document-form`](kb/dev/decision/p12-generated-document-form/conclusion.md)).
- **[지킴]** 단위 지식 본문이나 라벨을 그대로 옮겨 싣는 **인용 구역**은 표시로 감싼다 ([`p12-generated-document-form`](kb/dev/decision/p12-generated-document-form/conclusion.md)). 그 안에서는 표와 펜스, 빈 값, 수치, 산문의 다섯을 판정하지 않는다. 생성기는 원문을 고쳐 쓰지 않고, 원본은 이미 자기 게이트를 통과했기 때문이다. 다만 제목 계층과 h1, 목차, 링크는 구역 안에도 적용한다.
- **[지킴]** 제목 줄과 링크 텍스트는 수치 표기 판정 밖이다 ([`p12-generated-document-form`](kb/dev/decision/p12-generated-document-form/conclusion.md)). 이름에 든 백분율은 측정치가 아니다.
- **[지킴]** 머리 `입력` 줄의 꼴은 입력 파일 수로 갈린다 ([`p12-generated-document-input-section`](kb/dev/decision/p12-generated-document-input-section/conclusion.md)). 여섯 이하면 파일 목록과 해시값, 규모를 적는다. 일곱 이상이면 개수와 해시값, 규모, `## 입력 파일` 절로의 링크를 적고, 문서 끝의 `## 입력 파일` 절에 파일 전부를 디렉토리로 묶어 적는다. 목록은 생략하지 않는다(G4). 규모 자리의 트리플 수에는 **union 구성**을 함께 적는다(`트리플 <n> (union: chunks +a · base +b · …)`). 구성원마다 붙는 수는 선언 순서대로 앞 구성원들의 합집합에 더한 증분이고, 증분의 합이 총수와 다르거나 증분 없는 옛 표기를 쓴 줄은 G4가 FAIL로 낸다(유저 답 Q40-a, 2026-10-04). 같은 이름의 수치가 도구마다 갈리는 이유가 문서 안에 있어야 한다(현상 `agt:metricVariesByLoadingOption`, 2026-09-29).
- **[권장]** 목표가 정의된 수치에는 `(목표 <값>)`을 붙인다 ([`p12-generated-document-form`](kb/dev/decision/p12-generated-document-form/conclusion.md)). **[지킴]** 붙였다면 표기는 한 꼴이고, 그 통일성은 게이트 `gendoc`의 G16이 강제한다(2026-09-29 측정: 위반 1·오탐 0). 다만 "목표를 붙여야 하는가"는 게이트 밖 사람 판단이다.
- **[권장]** "현재", "최신", "지금" 같은 시점 의존 표현을 값 대신 쓰지 않으며, 인용 자리는 예외다 ([`p12-time-dependent-wording-is-advisory`](kb/dev/decision/p12-time-dependent-wording-is-advisory/conclusion.md)). 게이트화는 보류하고 `check_gendoc`이 후보만 낸다. 2026-09-29 측정에서 후보 7/7이 오탐이었기 때문이다. 그 오탐은 CQ 정식 문구의 인용과 인용 표시 없이 옮긴 단위 지식 본문, 값과 병기된 부연이었다.

## 셀프체크

```bash
bazel test //...    # 반드시 PASS. FAIL이면 게이트가 아니라 산출물을 고친다
```

<!-- 인용 끝 -->

## 입력 파일

원본 파일 66개다. 디렉토리로 묶었고 빠진 파일은 없다.

- `kb/dev/decision/p0-agt-namespace/` — `conventions.md`
- `kb/dev/decision/p0-condition-taxonomy-extensible/` — `conventions.md`
- `kb/dev/decision/p0-english-label-without-hangul/` — `conventions.md`
- `kb/dev/decision/p0-entity-iri-forms/` — `conventions.md`
- `kb/dev/decision/p0-figure-caption-and-source/` — `conventions.md`
- `kb/dev/decision/p0-iri-design/` — `conventions.md`
- `kb/dev/decision/p0-no-invented-terms/` — `conventions.md`
- `kb/dev/decision/p0-notation-format/` — `conventions.md`
- `kb/dev/decision/p0-premise-as-assumption/` — `conventions.md`
- `kb/dev/decision/p0-prose-assertive-register/` — `conventions.md`
- `kb/dev/decision/p0-run-is-an-append-only-memory-chunk/` — `conventions.md`
- `kb/dev/decision/p0-self-explanatory-definitions/` — `conventions.md`
- `kb/dev/decision/p0-sentence-composition/` — `conventions.md`
- `kb/dev/decision/p0-service-is-a-three-layer-wiki/` — `conventions.md`
- `kb/dev/decision/p0-skos-label-synonyms/` — `conventions.md`
- `kb/dev/decision/p0-terms-from-glossary/` — `conventions.md`
- `kb/dev/decision/p1-chunk-unit-is-tokens/` — `conventions.md`
- `kb/dev/decision/p10-split-keeps-work-identity/` — `conventions.md`
- `kb/dev/decision/p11-catalog-role-has-granted-scope/` — `conventions.md`
- `kb/dev/decision/p11-harness-two-channels/` — `conventions.md`
- `kb/dev/decision/p11-user-question-has-five-parts/` — `conventions.md`
- `kb/dev/decision/p12-generated-document-form/` — `conventions.md`
- `kb/dev/decision/p12-generated-document-header/` — `conventions.md`
- `kb/dev/decision/p12-generated-document-input-section/` — `conventions.md`
- `kb/dev/decision/p12-time-dependent-wording-is-advisory/` — `conventions.md`
- `kb/dev/decision/p2-competency-questions/` — `conventions.md`
- `kb/dev/decision/p2-ontology-file-is-a-chunk/` — `conventions.md`
- `kb/dev/decision/p2-ontology-ttl-layout/` — `conventions.md`
- `kb/dev/decision/p2-trust-tier-from-generated-and-verified/` — `conventions.md`
- `kb/dev/decision/p3-condition-entity-from-odd-document/` — `conventions.md`
- `kb/dev/decision/p4-chunk-as-four-named-graphs/` — `conventions.md`
- `kb/dev/decision/p4-composite-declared-in-frontmatter/` — `conventions.md`
- `kb/dev/decision/p4-composite-order-is-declared/` — `conventions.md`
- `kb/dev/decision/p4-compression-repeat-is-split-signal/` — `conventions.md`
- `kb/dev/decision/p4-one-file-one-topic/` — `conventions.md`
- `kb/dev/decision/p4-redundancy-as-safety-margin/` — `conventions.md`
- `kb/dev/decision/p4-shape-file-per-target-with-message/` — `conventions.md`
- `kb/dev/decision/p4-shape-only-strengthens/` — `conventions.md`
- `kb/dev/decision/p4-shape-values-are-typed/` — `conventions.md`
- `kb/dev/decision/p4-slot-answers-one-question/` — `conventions.md`
- `kb/dev/decision/p4-slot-marker-by-position/` — `conventions.md`
- `kb/dev/decision/p4-three-empty-values/` — `conventions.md`
- `kb/dev/decision/p6-gate-catalogue/` — `conventions.md`
- `kb/dev/decision/p6-gate-tool-code-structure/` — `conventions.md`
- `kb/dev/decision/p6-weakening-a-check-needs-user-approval/` — `conventions.md`
- `kb/dev/decision/p7-alternatives-mandatory/` — `conventions.md`
- `kb/dev/decision/p7-commentary-form/` — `conventions.md`
- `kb/dev/decision/p7-dev-plane-substance/` — `conventions.md`
- `kb/dev/decision/p8-scenario-authoring/` — `conventions.md`
- `kb/dev/decision/pe-generated-outputs-stay-in-bazel-out/` — `conventions.md`
- `kb/dev/decision/pe-kg-hand-and-generated-files/` — `conventions.md`
- `kb/dev/decision/pe-knowledge-files-are-gate-inputs/` — `conventions.md`
- `kb/dev/decision/pe-three-layer-binding/` — `conventions.md`
- `kb/dev/norm/STYLEGUIDE/` — `bazel.md` · `channels.md` · `common.md` · `generated-documents.md` · `head.md` · `knowledge-graph.md` · `knowledge.md` · `odd.md` · `ontology.md` · `robustness-axes.md` · `self-check.md` · `shacl-shapes.md` · `tools.md`

