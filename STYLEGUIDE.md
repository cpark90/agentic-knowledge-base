# STYLEGUIDE.md — 컴포넌트별 작성 스타일

이 문서는 이 저장소의 지식 산출물 저작의 **단일 진실 공급원**이다. 저작·수정 세션
시작 시 읽는다. 하네스 운영 규칙은 `AGENTS.md`, 체계의 근거는
`agent-knowledge-system-notes.md`(이하 "노트")다.

표기: **[지킴]** 게이트 또는 리뷰가 강제 / **[권장]** 따르되 사유가 있으면 어겨도 됨.
어길 때는 커밋 메시지나 파일 주석에 사유를 한 문장 남긴다 — 말없이 머지하지 않는다.

## §0. 공통 철학

목표는 코드 스타일과 같다: **일관성과 가독성**. 다음 세션의 에이전트가 파일 하나를
열어 빠르게 이해하고, 무엇을 재사용할지 알 수 있어야 한다.

- **[지킴]** **한 청크는 한 파일, 한 파일은 한 주제.** 지식·온톨로지·shape 전부.
  라벨 하나로 요약되지 않으면 두 주제다 — 분할한다 (노트 4.10절).
- **[지킴]** **본문 42줄 이하** (4.1절). 단위는 컴포넌트별 절이 정의한다.
- **[지킴]** **중복 대신 재사용.** 새 개념·청크를 만들기 전에 기존 것을 찾는다
  (`grep -r ontology/`, 라벨 목록). 같은 뜻의 항목 둘이 이 체계가 막는 drift다.
- **[지킴]** **표준어 우선** (0.0절). 지어낸 용어·자체 약어를 만들지 않는다.
  확립된 표준어가 있으면 그것을 쓰고, 없을 때만 새로 만든다.
- **[지킴]** **자기설명적으로.** 좋은 라벨과 정의가 주석보다 낫다. 정의는 "무엇인가"의
  재진술이 아니라 **왜 존재하고 언제 쓰는가**를 적는다.
- **[지킴]** 언어 (0.6절): 산문·정의·주석은 한글, 식별자는 영어 소문자 케밥, 개념은
  PascalCase. 라벨은 한/영 각 1. 들여쓰기는 스페이스 4칸(TTL) — 탭 금지.

### 강인성 세 축과 게이트 대응

| 축 | 위협 | 방어 | 게이트 |
|---|---|---|---|
| anti-drift | 어휘가 조용히 갈라짐 | `agt:` 어휘 통제, 표준어 우선 | `validate.py` vocab·labels·boundary |
| anti-rot | 컨텍스트가 무한히 커짐 | 42줄 청크, 라벨 목록 우선 읽기 | `chunk_lint.py`, SHACL lineCount |
| anti-orphan | 뜬 지식이 쌓임 | 구성체·링크 연결 (Part XII 3단계에서 게이트화 예정) | (예정) |

## §1. 온톨로지 청크 (`ontology/**/*-ontology.ttl`)

파일 = 청크, 디렉토리 = 모듈(Bazel 패키지), 노트 2.3절 구조.

- **[지킴]** 새 개념은 **주제가 맞는 기존 모듈 디렉토리의 새 파일**로, 새 주제는
  **새 모듈 디렉토리**(+ `BUILD.bazel` + `//ontology:modules` 등록)로 추가한다.
  기존 파일에 덧붙이는 것은 그 파일의 주제일 때만.
- **[지킴]** 한 개념은 정확히 한 파일에서 정의된다 — 다른 파일에서 재정의·재선언
  금지 (boundary 게이트). 다른 모듈의 개념은 참조만 한다.
- **[지킴]** 모든 `agt:` 클래스·속성·개체에 `rdfs:label` 한/영 각 1 +
  `skos:definition`(한글, 노트 절 번호 인용) — labels 게이트가 강제.
- **[지킴]** 정의(skos:definition)에는 그 개념이 딛고 선 **노트 절 번호**를 적는다.
  근거 없는 개념은 온톨로지 과설계의 시작이다 (2.7절 경쟁 질문).
- **[지킴]** 본문 42줄 이하 — `@prefix`·주석·빈 줄 제외 (`//ontology:chunk_lint_test`).
- **[지킴]** 파일 구조: 상단 배너 주석 1줄(주제 + 노트 절 번호) → `@prefix` 블록
  (agt → owl → rdfs → skos → xsd 순) → 개념 블록들.
- **[지킴]** 개념 블록의 술어 순서: `a` → `rdfs:subClassOf`/`owl:disjointWith` →
  `rdfs:domain` → `rdfs:range` → `rdfs:label` (en, ko 순) → `skos:definition`.
- **[지킴]** 상위 온톨로지(`upper`)는 수정 금지. 외부 어휘(prov·skos·co 등)의 정의를
  변경하지 않는다 (0.3절).
- **[권장]** 동의어는 새 개념이 아니라 `skos:altLabel`로 등록한다 (0.8절).

## §2. SHACL shape (`ontology/shapes/*-shapes.ttl`)

- **[지킴]** 파일 하나 = 검사 대상 하나(또는 밀접한 쌍). 파일명 `<대상>-shapes.ttl`.
- **[지킴]** 모든 property shape에 `sh:message`를 달고, 메시지에 **강제하는 노트 절
  번호**를 적는다 — FAIL이 곧 수정 방향 안내가 되게.
- **[지킴]** shape는 **강화만** 한다. 기존 제약을 약화(maxCount 완화, sh:in 확장 등)
  하는 변경은 사용자 승인 사항이다 (`AGENTS.md` 워크플로 ⑤).
- **[권장]** 닫힌 값 목록(`sh:in`)의 원천은 온톨로지 정의의 서술과 일치시킨다 —
  값을 추가하면 해당 개념의 `skos:definition`도 갱신한다.

## §3. ODD (`odd/*-odd.ttl`)

- **[지킴]** 조건 개체는 `id:cond-<slug>`, 타입은 3분류(`agt:StaticElement` /
  `agt:EnvironmentalCondition` / `agt:DynamicElement`) 중 하나 (0.4절).
- **[지킴]** 모든 조건에 `agt:conditionValue`(값 또는 범위) + `agt:checkMethod` +
  `agt:verificationGrade`. 판정 방법은 **객관적 관측 수단**이어야 한다 — "정상이다"가
  아니라 "명령 X가 Y를 반환한다" (0.4절).
- **[지킴]** 조건은 ODD 개체의 `agt:hasCondition` 목록에 등록한다. 등록 없는 조건
  개체를 만들지 않는다.
- **[지킴]** 명시 제외(`agt:excludes`)의 서식: `"<대상> — reviewed YYYY-MM, 이유: <근거>"`.
  검토한 제외와 미검토를 구분하는 것이 이 절의 존재 이유다 (3.2절).
- **[권장]** 판정 등급 C·D인 조건은 판정 방법을 개선하거나 ODD에서 빼고 가정으로
  내린다 (0.4절). B 이하로 내려가는 변경은 사유를 남긴다.

## §4. 지식 청크 (`chunks/<plane>/*.md`)

한 청크는 한 파일: frontmatter(head) + 본문(assertion). head 그래프는
`//kg:chunks_kg`가 생성한다 — kg에 손으로 쓰지 않는다.

- **[지킴]** frontmatter 필수 키: `iri`, `plane`, `level`, `label_ko`, `label_en`,
  `state`. 선택: `assumes`, `derived_from`, `generated_at`. 값 어휘는
  `tools/chunk2kg.py` 상단 주석이 원본.
- **[지킴]** IRI는 `https://agentic-knowledge-base.dev/id/chunk-<slug>`. 내용을 IRI에
  넣지 않는다 — 사람이 읽는 이름은 라벨이다 (0.7절).
- **[지킴]** 본문 42줄 이하(frontmatter·앞뒤 빈 줄 제외). 한 주제. 라벨만 보고
  본문을 예측할 수 있어야 한다 (4.4절 라벨링).
- **[지킴]** plane별 본문 형식 (4.12절):
  - `decision` — 역할 태그 셋 중 하나 이상: `**결론**` / `**근거**` / `**대안**`
    (대안에는 기각 사유를 적는다).
  - `annotation` — 첫 줄에 대상 청크 IRI.
  - `memory` — 구조화 관측: 시각, 행동, situation 요약.
  - `contract`/`schema`/`artifact` — 언어 네이티브 선언·스키마·코드.
- **[지킴]** 전제가 있으면 가정 개체(`kg/base-kg.ttl`)를 만들고 `assumes`로 가리킨다.
  가정 없는 청크는 ODD 전체를 전제한다는 뜻이 아니라 전제를 아직 안 적은 것이다 —
  리뷰에서 잡는다.
- **[지킴]** 본문을 고치면 라벨이 여전히 대표하는지 재검토한다 (라벨 부패,
  Part XIII).
- **[권장]** 42줄 근처로 억지 압축하지 않는다 — 분할 신호(4.10절)를 따른다.

## §5. 지식그래프 A-Box (`kg/*-kg.ttl`)

- **[지킴]** 청크 head를 손으로 쓰지 않는다 (생성 산출물). 여기 두는 것은 청크가
  아닌 개체다: 가정, 출처 문서, 역할, 스코프, 하네스.
- **[지킴]** 개체 IRI는 `id:` 네임스페이스, `<kind>-<slug>` 소문자 케밥:

  | 종류 | 접두사 | 예 |
  |---|---|---|
  | 청크 | `chunk-` | `id:chunk-d0001` |
  | 가정 | `asm-` | `id:asm-bazel-toolchain` |
  | 조건 | `cond-` | `id:cond-build-system` |
  | 출처 문서 | `doc-` | `id:doc-system-notes` |
  | 역할 | `role-` | `id:role-developer` |
  | 스코프 | `scope-` | `id:scope-developer` |
  | 하네스 | `h-` | `id:h-akb` |
  | 구성체 | `comp-` | `id:comp-…` |
  | 시나리오 | `scn-` | `id:scn-…` |
  | 실행 기록 | `run-` | `id:run-…` |

- **[지킴]** 출처·귀속·버전은 PROV-O만 쓴다 (4.3절): `prov:wasDerivedFrom`,
  `prov:wasAttributedTo`, `prov:generatedAtTime`, `prov:atLocation`.
- **[지킴]** 개체에도 라벨 한/영을 단다 — 라벨 목록 읽기가 기본 접근이다 (4.4절).
- **[지킴]** 파일 상단 배너에 이 파일이 담는 개체 종류와 "손으로 쓰지 않는 것"을
  적는다.
- **[권장]** ID는 재사용하지 않는다. 폐기는 `state`/`deprecated`로 남기고 새 IRI를
  만든다 — 분할·병합은 `prov:wasDerivedFrom`으로 잇는다 (4.10절).

## §6. Bazel (`BUILD.bazel`, `defs/*.bzl`)

- **[지킴]** 지식 파일은 반드시 어떤 `filegroup`에 속하고, 그 filegroup은 어떤 게이트
  테스트의 입력이다. 어느 게이트도 검사하지 않는 지식 파일이 이 하네스의 orphan이다.
- **[지킴]** 게이트는 `defs/knowledge.bzl`의 매크로(`kb_gate_test`, `kb_chunk_kg`,
  `kb_chunk_lint_test`)로만 선언한다 — `py_test`를 직접 쓰지 않는다.
- **[지킴]** 모듈 디렉토리 = Bazel 패키지. 패키지의 `filegroup` 이름은 디렉토리
  이름과 같게 한다 (`//ontology/related/condition` 처럼 짧게 참조되도록).
- **[지킴]** 생성 산출물의 원본 규칙: 생성물은 `bazel-out`에만 존재한다. 소스
  트리에 같은 이름의 파일을 두지 않는다.
- **[권장]** `glob`은 패키지 안 한 계층만. 깊은 glob이 필요해지면 패키지를 나눈다.

## §7. 판정 도구 (`tools/*.py`)

- **[지킴]** 게이트 도구는 실패 시 비영 종료 + `FAIL [검사명]` 접두사 + **노트 절
  번호 인용** — 메시지가 곧 수정 안내다.
- **[지킴]** 검사를 약화하는 변경(검사 삭제, 예외 추가)은 사용자 승인 사항이다.
- **[지킴]** 접미사·네임스페이스 등 규약 상수의 단일 정의처는 `tools/kb_lib.py`다 —
  다른 파일에 복제하지 않는다.
- **[권장]** 새 검사는 독립 함수 `check_*() -> list[str]`로 추가하고 `main`에서
  합류한다 — 검사 간 결합을 만들지 않는다.

## 셀프체크

```bash
bazel test //...    # 반드시 PASS. FAIL이면 게이트가 아니라 산출물을 고친다
```
