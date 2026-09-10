# STYLEGUIDE.md — 컴포넌트별 작성 스타일

이 문서는 지식 산출물 저작의 **단일 진실 공급원**이다. 저작·수정 세션 시작 시 읽는다.
하네스 운영 규칙은 [`AGENTS.md`](AGENTS.md), 무엇이 유효한 구조인지는
[`docs/rules.md`](docs/rules.md), 어떻게 만드는지는 [`docs/method.md`](docs/method.md)다 —
여기는 **어떻게 쓰는가**만 다룬다.

표기: **[지킴]** 게이트 또는 리뷰가 강제 / **[권장]** 따르되 사유가 있으면 어겨도 됨.
어길 때는 커밋 메시지나 파일 주석에 사유를 한 문장 남긴다 — 말없이 머지하지 않는다.

## §0. 공통

목표는 코드 스타일과 같다: **일관성과 가독성**. 다음 세션의 에이전트가 파일 하나를 열어
빠르게 이해하고, 무엇을 재사용할지 알 수 있어야 한다.

- **[지킴]** **한 청크는 한 파일, 한 파일은 한 주제.** 지식·온톨로지·shape 전부. 라벨 하나로
  요약되지 않으면 두 주제다 — 분할한다.
- **[지킴]** **본문 42줄 이하.** 단위는 컴포넌트별 절이 정의한다.
- **[지킴]** **지식의 종류는 고유 용어로 부른다** — 조건·개념·변수·후보·결정·가정·
  시그니처·함수·주석·관측. "결정 청크"가 아니라 "결정"이다. "청크"는 그 항목이 따르는
  구조 규칙을 말할 때만 쓴다. 온톨로지 클래스 이름·그래프 라벨 인용은 예외다.
- **[지킴]** **중복 대신 재사용.** 새 개념·항목을 만들기 전에 기존 것을 찾는다
  (`grep -r kb/ontology/`, 라벨 목록). 같은 뜻의 항목 둘이 이 체계가 막는 드리프트다.
- **[지킴]** **표준어 우선.** 지어낸 용어·자체 약어를 만들지 않는다. 없을 때만 새로 만들고,
  가져온 곳은 [`docs/references.md`](docs/references.md)에 남긴다.
- **[지킴]** **자기설명적으로.** 좋은 라벨과 정의가 주석보다 낫다. 정의는 "무엇인가"의
  재진술이 아니라 **왜 존재하고 언제 쓰는가**를 적는다.
- **[지킴]** 언어: 산문·정의·주석은 한글, 식별자는 영어 소문자 케밥, 개념은 PascalCase.
  라벨은 한/영 각 1. 들여쓰기는 스페이스 4칸(TTL) — 탭 금지.

### 강인성 세 축과 게이트 대응

| 축 | 위협 | 방어 | 게이트 |
|---|---|---|---|
| anti-drift | 어휘가 조용히 갈라짐 | `agt:` 어휘 통제, 표준어 우선 | `validate.py` vocab·labels·boundary |
| anti-rot | 컨텍스트가 무한히 커짐 | 42줄 상한, 라벨 목록 우선 읽기 | `chunk_lint.py`, SHACL `lineCount` |
| anti-orphan | 쓰이지 않는 지식이 쌓임 | 복합체·링크 연결, 고아율 관측 | (없음 — [`docs/tools.md`](docs/tools.md) §게이트 밖) |

## §1. 온톨로지 (`kb/ontology/**/*-ontology.ttl`)

파일 = 청크, 디렉토리 = 모듈(Bazel 패키지).

- **[지킴]** 새 개념은 **주제가 맞는 기존 모듈 디렉토리의 새 파일**로, 새 주제는 **새 모듈
  디렉토리**(+ `BUILD.bazel` + `//kb/ontology:modules` 등록)로 추가한다.
- **[지킴]** 한 개념은 정확히 한 파일에서 정의된다 — 다른 파일에서 재정의·재선언 금지
  (boundary 게이트). 다른 모듈의 개념은 참조만 한다.
- **[지킴]** 모든 `agt:` 클래스·속성·개체에 `rdfs:label` 한/영 각 1 + `skos:definition`(한글).
- **[지킴]** 정의에는 그 개념이 딛고 선 근거를 적는다. 근거 없는 개념은 온톨로지 과설계의
  시작이다 — 역량 질문에 기여하지 않으면 만들지 않는다.
- **[지킴]** 본문 42줄 이하 — `@prefix`·주석·빈 줄 제외.
- **[지킴]** 파일 구조: 상단 배너 주석 1줄(주제) → `@prefix` 블록(agt → owl → rdfs → skos →
  xsd 순) → 개념 블록들.
- **[지킴]** 개념 블록의 술어 순서: `a` → `rdfs:subClassOf`/`owl:disjointWith` →
  `rdfs:domain` → `rdfs:range` → `rdfs:label`(en, ko 순) → `skos:definition`.
- **[지킴]** 상위 온톨로지와 외부 어휘(prov·skos·co 등)의 정의를 변경하지 않는다.
- **[권장]** 동의어는 새 개념이 아니라 `skos:altLabel`로 등록한다.

## §2. SHACL shape (`kb/ontology/shapes/*-shapes.ttl`)

- **[지킴]** 파일 하나 = 검사 대상 하나(또는 밀접한 쌍). 파일명 `<대상>-shapes.ttl`.
- **[지킴]** 모든 property shape에 `sh:message`를 달고, 메시지에 강제하는 규칙을 적는다 —
  FAIL이 곧 수정 방향 안내가 되게.
- **[지킴]** shape는 **강화만** 한다. 기존 제약을 약화(maxCount 완화, `sh:in` 확장 등)하는
  변경은 유저 승인 사항이다.
- **[권장]** 닫힌 값 목록(`sh:in`)의 원천은 온톨로지 정의의 서술과 일치시킨다.

## §3. ODD (`kb/odd/*-odd.yml` — OpenODD 문서. `*-odd.ttl`·`taxonomy.yml`은 생성물, 손으로 쓰지 않는다)

작성 절차는 [`docs/method.md` §2](docs/method.md#2-odd-작성).

- **[지킴]** 조건 개체는 `id:cond-<slug>`, 타입은 3분류(`agt:StaticElement` /
  `agt:EnvironmentalCondition` / `agt:DynamicElement`) 중 하나.
- **[지킴]** 모든 조건에 `agt:conditionValue` + `agt:checkMethod` + `agt:verificationGrade`.
  판정 방법은 **객관적 관측 수단**이어야 한다 — "정상이다"가 아니라 "명령 X가 Y를 반환한다".
- **[지킴]** 조건은 ODD 개체의 `agt:hasCondition` 목록에 등록한다. 등록 없는 조건을 만들지
  않는다.
- **[지킴]** 명시 제외(`agt:excludes`)의 서식: `"<대상> — reviewed YYYY-MM, 이유: <근거>"`.
- **[권장]** 판정 등급 C·D인 조건은 판정 방법을 개선하거나 ODD에서 빼고 가정으로 내린다.

## §4. 지식 (`chunks/<plane>/*.md`)

한 파일 = frontmatter(head) + 본문(assertion). head 그래프는 `//kg:chunks_kg`가 생성한다 —
`kg/`에 손으로 쓰지 않는다. 형식은 [`docs/rules.md` §1](docs/rules.md#1-chunk--자립적-최소-지식-단위).

- **[지킴]** 한글 용어는 [`docs/glossary.md`](docs/glossary.md)의 표준 용어만 쓴다 — 은유·조어(가로대·사다리·상승·하강·장부·투영·봉사·거주표…)를
  새로 만들지 않는다. 용어집에 없는 개념은 표준어를 찾아 용어집에 먼저 추가한다 (유저 결정 2026-09-10, 원장 19).
- **[지킴]** frontmatter 필수 키(OKF v0.2 사상, 노트 E.2): `id`, `type`, `level`, `title_ko`, `title`, `status`,
  `generated`. 선택: `verified`, `sources`, `assumes`. `type`·`status`·`generated`·
  `verified`는 **OKF v0.2 필드명**이다 — 이 저장소의 `chunks/`는 OKF 번들이다. 값 어휘의
  원본은 `tools/chunk2kg.py`의 상수(`PLANE_CLASS`·`LEVELS`·`STATES`·`REQUIRED`)다.
- **[지킴]** `generated: {by, at}`의 `by`는 OKF 행위자 표기 — 도구는 `<생성기>/<버전>`,
  사람은 `human:<id>`. **검증하지 않은 것을 `verified`에 적지 않는다** — 미검증이 정직한
  상태이고, 검증 뒤 내용을 고치면 게이트가 거부한다.
- **[지킴]** 예약 파일명 `index.md`·`log.md`를 쓰지 않는다 (OKF).
- **[지킴]** IRI는 `https://agentic-knowledge-base.dev/id/chunk-<slug>`. 내용을 IRI에 넣지
  않는다 — 사람이 읽는 이름은 라벨이다.
- **[지킴]** 본문 42줄 이하(frontmatter·앞뒤 빈 줄 제외). 한 주제. 라벨만 보고 본문을
  예측할 수 있어야 한다.
- **[지킴]** plane별 본문 형식:
  - `decision` — 역할 태그 `**결론**` / `**근거**` / `**대안**`(기각 사유 포함).
    *현재 실측: 결론 153 · 근거 150 · 대안 19. 셋 중 무엇이 필수인지는 미정 —
    [`docs/open-questions.md`](docs/open-questions.md).*
  - `annotation` — 첫 줄에 대상 IRI.
  - `memory` — 구조화 관측: 시각, 행동, situation 요약.
  - `contract`/`schema`/`artifact` — 언어 네이티브 선언·스키마·코드.
- **[지킴]** 전제가 있으면 가정을 만들고 `assumes`로 가리킨다. 가정 없는 항목은 전제를 아직
  안 적은 것이다 — 리뷰에서 잡는다.
- **[지킴]** 본문을 고치면 라벨이 여전히 대표하는지 재검토한다.
- **[권장]** 42줄 근처로 억지 압축하지 않는다 — 분할 신호를 따른다.

## §5. 지식그래프 A-Box (`kg/*-kg.ttl`)

- **[지킴]** head를 손으로 쓰지 않는다(생성 산출물). 여기 두는 것은 가정·출처 문서·복합체·
  역할·스코프·채널·하네스다.
- **[지킴]** 개체 IRI는 `id:` 네임스페이스, `<kind>-<slug>` 소문자 케밥. 접두사 표는
  [`docs/rules.md` §개체 IRI 접두사](docs/rules.md#개체-iri-접두사) — 표에 없는 접두사가
  그래프에 나타나면 그 자체가 드리프트 신호다.
- **[지킴]** 카탈로그(`catalog-kg.ttl`)의 완전성: 하네스가 `agt:hasRole` 하는 모든 역할은
  대응 스코프를 갖고 하네스가 그것을 `agt:grants` 한다.
- **[지킴]** 출처·귀속·버전은 PROV-O만 쓴다: `prov:wasDerivedFrom`, `prov:wasAttributedTo`,
  `prov:generatedAtTime`, `prov:atLocation`.
- **[지킴]** 개체에도 라벨 한/영을 단다 — 라벨 목록 읽기가 기본 접근이다.
- **[지킴]** 파일 상단 배너에 담는 개체 종류와 "손으로 쓰지 않는 것"을 적는다.
- **[권장]** ID는 재사용하지 않는다. 폐기는 `state`/`deprecated`로 남기고 새 IRI를 만든다 —
  분할·병합은 `prov:wasDerivedFrom`으로 잇는다.

## §6. Bazel (`BUILD.bazel`, `defs/*.bzl`)

- **[지킴]** 지식 파일은 반드시 어떤 `filegroup`에 속하고, 그 filegroup은 어떤 게이트
  테스트의 입력이다. 어느 게이트도 검사하지 않는 지식 파일이 이 하네스의 orphan이다.
- **[지킴]** 게이트는 `defs/knowledge.bzl`의 매크로로만 선언한다 — `py_test`를 직접 쓰지
  않는다.
- **[지킴]** 모듈 디렉토리 = Bazel 패키지. 패키지의 `filegroup` 이름은 디렉토리 이름과 같게.
- **[지킴]** 생성물은 `bazel-out`에만 존재한다. 소스 트리에 같은 이름의 파일을 두지 않는다.
- **[권장]** `glob`은 패키지 안 한 계층만.

## §7. 도구 (`tools/*.py`)

- **[지킴]** 게이트 도구는 실패 시 비영 종료 + `FAIL [검사명]` 접두사 + 근거 인용 — 메시지가
  곧 수정 안내다.
- **[지킴]** 검사를 약화하는 변경(삭제·예외 추가)은 유저 승인 사항이다.
- **[지킴]** 규약 상수의 단일 정의처는 `tools/kb_lib.py`다 — 다른 파일에 복제하지 않는다.
- **[권장]** 새 검사는 독립 함수 `check_*() -> list[str]`로 추가하고 `main`에서 합류한다.

## §8. 소통 채널 (`docs/feedback/**`)

채널 파일은 지식이 아니라 소통 기록이다 — **그래프 밖**이며 게이트 검사 대상이 아니다
(§6의 filegroup 규칙에서 제외되는 유일한 문서군). 규약 원본은
[`docs/feedback/README.md`](docs/feedback/README.md).

- **[지킴]** 쓰기 경계: hci는 채널 전체와 자기 역할 메모리, 다른 에이전트는 자기 항목만.
- **[지킴]** 한 파일에 한 주제 — 항목이 반영·승인의 단위다.
- **[지킴]** `status` 어휘는 lane마다 다르다 — 섞지 않는다: 유저 lane `open→approved`
  (approved는 유저만), 에이전트 lane `open→relayed→answered→closed`, 조사 lane
  `open→answered→closed`.
- **[지킴]** 에이전트가 쓰는 항목은 `.wip.md`로 작성하고 완료 시 rename한다.
- **[지킴]** 항목에서 지식을 가리킬 때는 이름이 아니라 **IRI·조건 id·`file:line`**으로.
- **[지킴]** 유저 판단을 요청하는 항목은 **다섯 절**로 쓴다 — 질문(왜 어려운가 포함) /
  이미 정해진 것 / 현재 상태(실측) / 답이 가르는 것 / 선택지. 한 줄 질문은 답을 받지 못한다.

## 셀프체크

```bash
bazel test //...    # 반드시 PASS. FAIL이면 게이트가 아니라 산출물을 고친다
```
