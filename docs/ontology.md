# ontology — 지식의 골격과 분야 프로파일

온톨로지는 이 체계의 **어휘**다. 사다리의 한 단계가 아니라 사다리 전체가 쓰는 어휘이며,
이 어휘 밖에서 쓴 지식은 이 체계에 존재하지 않는다
([`id:chunk-d0046`](../chunks/decision/d-0046-ontology-as-vocabulary.md)).

## 두 층

| 층 | 담는 것 | 누가 만드나 | 위치 |
|---|---|---|---|
| **골격** | 분야와 무관한 것 — plane, level, 조건, 가정, 역할, 청크·구성체, 링크 타입 | 이 저장소 | `kb/ontology/` (`agt:`) |
| **분야 프로파일** | 각 plane의 실체와 판정 도구, 조건 어휘 셋째 수준, 도메인 결함 하위 유형, 앵커 해석기 | 분야마다 | `profile/<분야>` (미구현) |

프로파일은 별도 장치가 아니라 **골격을 확장만 하는 온톨로지 모듈**이다. 골격 클래스의
하위 클래스와 shape만 추가하며, 골격을 수정하는 프로파일은 검사 실패다
([`id:chunk-d0057`](../chunks/decision/d-0057-profile-extension-only-module.md)). 한 프로젝트가
프로파일을 여럿 가질 수 있고, 링크는 프로파일을 넘는다.

**현재 `profile/` 디렉토리는 없다.** 프로파일 구축 절차도 아직 없다 —
[`method.md §1`](method.md#1-프로파일-구축)이 그 자리이고, 첫 프로파일 작성이 다음 산출이다
([`roadmap.md`](roadmap.md)).

## 골격의 구성

```
kb/ontology/
  project-ontology.ttl          # 최상위. import만 하는 얇은 파일
  entity/                       # plane으로 분류 가능한 개념
    knowledge-item/             #   KnowledgeItem · Chunk · Composite · plane 7종 · level · 속성
  related/                      # 횡단 개념 — 어느 plane에도 속하지 않는다
    condition/  scope/  assumption/  channel/  harness/  trace/  trust/  state/  tag/
  shapes/                       # SHACL — 원칙의 검사 가능한 형태 (plane×level 상주표 포함)
  proposals/                    # 용어 제안 승인 큐 — //kb/ontology:modules 밖 (2.5절)
```

모듈 = 디렉토리 = Bazel 패키지이고, 한 파일이 한 주제다. 분할 축은 둘 — **plane으로
분류되는 개념(`entity/`)과 횡단 개념(`related/`)**, 그리고 **어휘(`-ontology`)와
형식화(`-rules`·`-shapes`)** ([`id:chunk-d0048`](../chunks/decision/d-0048-ontology-module-structure.md)).

`related/trace`(링크 타입·링크 개체·판정 근거, 파일 8개)가 2026-09-04에 추가되었다 — 설계는
[`feedback/dependency-graph-design.md`](feedback/dependency-graph-design.md).

`related/trust`(생성·검증 주체)가 2026-09-07에 추가되었다 — OKF v0.2의 트러스트 티어.

노트 v3 반영(2026-09-10)으로 추가된 것: `related/state`(Workset·Run·Runbook),
`related/tag`(태그 범주 9종), `related/condition/temporal-ontology.ttl`(precedes·
mutuallyExclusiveWith·withinDeadline), `entity/knowledge-item`의 `RequirementChunk`,
`shapes/residency-shapes.ttl`(plane×level 상주표), trace의 `allocates`·`generates`·
`CandidateLink`·`ConfirmedLink`, `agt:contentHash`.

설계가 요구하나 아직 없는 모듈: `upper`(상위 온톨로지 정렬), `related/policy`,
`profile/`, `defect`·`defect-rules`.

## 확장 규칙

1. **기존 어휘를 먼저 찾는다** (`grep -r "찾는개념" kb/ontology/`). 같은 뜻의 개념을 둘
   만드는 것이 이 체계가 막는 드리프트다 ([`id:chunk-d0160`](../chunks/decision/d-0160-search-before-authoring.md)).
2. 주제가 맞는 **기존 모듈 디렉토리에 새 파일 하나**, 새 주제면 **새 모듈 디렉토리**
   + `BUILD.bazel` + `//kb/ontology:modules` 등록.
3. 한 개념은 정확히 한 파일에서 정의된다 — 다른 파일에서 재정의하면 boundary 게이트가
   거부한다.
4. 모든 `agt:` 용어에 한/영 `rdfs:label`과 `skos:definition`. 정의는 속 + 종차로 쓰고
   ([`id:chunk-d0034`](../chunks/decision/d-0034-genus-differentia-definition.md)), 그래프가
   보여주지 못하는 것만 서술한다 ([`id:chunk-d0161`](../chunks/decision/d-0161-definition-says-why-and-when.md)).
5. **지어낸 용어를 쓰지 않는다.** 확립된 표준어가 있으면 그것을 쓰고, 고유 관계가
   필요하면 표준 관계의 하위 속성으로 매단다 (d-0024 · d-0053). 어디서 가져왔는지는
   [`references.md`](references.md)에 기록한다.
6. 폐기는 삭제가 아니다 — `owl:deprecated` + `agt:replacedBy` (d-0035).
7. **에이전트는 제안만 한다** — 상승이 온톨로지에 닿을 때는 `bazel run //tools:term_propose`로
   제안을 승인 큐(`kb/ontology/proposals/`)에 올리고, 유저 승인 뒤에만 모듈 파일로 옮긴다
   (노트 2.5절). 큐는 `//kb/ontology:modules` 밖이라 승인 전에는 그래프에 들어가지 않는다.

## 경쟁 질문 — 온톨로지의 요구사항이자 완료 판정

온톨로지가 답해야 하는 질문 목록이 그 온톨로지의 요구사항이다
([`id:chunk-d0052`](../chunks/decision/d-0052-competency-questions.md)). 질문에 기여하지 않는
개념은 과설계이고, 질문이 질의로 답해지면 그 부분은 완성이다.

목록과 현재 답할 수 있는 것의 실측은 [`competency-questions.md`](competency-questions.md) —
노트 v3의 CQ1~20과 이 저장소 등록분 CQ-01~32의 대응표도 거기에 있다. 답할 수 없는
질문이 어휘 확장의 우선순위다.

## 참조 프로파일 — 소프트웨어 개발

골격을 개발 작업에 특수화한 결정들이며, 다른 프로파일의 템플릿이다. 이 저장소는 이
프로파일의 부분집합만 쓴다 — 현재 `requirement`·`decision` plane이 채워져 있고, 역할은
노트 10.2절 9역할 중 5개다(design은 developer가 겸함 — 유저 결정 C4).

| 골격 항목 | 개발 프로파일의 결정 |
|---|---|
| `requirement` | EARS 문장. 이해관계자 관심사에서 도출 |
| `decision` | 설계 결정. 결론(concrete)·근거·대안(logical) 세 청크의 구성체 |
| `schema` | 프로토콜 메시지·필드. 스키마 언어 |
| `contract` | 인터페이스 시그니처. 언어 네이티브 선언 |
| `artifact` | **함수.** 42줄 초과 함수는 분할 |
| `annotation` | 코드 주석·리뷰 코멘트. 코드 밖에 저장 |
| 앵커 해석 | 심볼 ID → 파일 내 범위 |
| 판정 도구 | 컴파일러, 타입 체커, 스키마 검사기, 테스트, 린터 |
| 투영 | tangle(코드 파일), weave(문서) |
| 결함 하위 유형 | ODC 8유형 |
| 조건 셋째 수준 | 언어·런타임, 빌드 체계, 저장소 구조, 의존성 버전 |
| 검증 환경 | 단위 → 계약 → mock 통합 → 실제 인프라 → 스테이징 → 운영 |
