# 참조 표준과 프로파일

체계의 본문은 프로젝트 어휘로만 쓰되, **구조를 어디서 가져왔는지** 기록한다.
지어낸 용어를 쓰지 않는다는 원칙의 뒷면이다 — 표준에서 가져왔으면
그 사실이 남아야 검증도 되고, 표준이 개정될 때 무엇을 다시 볼지도 알 수 있다.
원래 설계 노트의 부록이었다.

## 1. 참조 표준 — 어느 구조를 어디서 가져왔나

### 자율주행 안전 표준 계열 (ODD·시나리오·검증)

| 가져온 구조 | 출처 |
|---|---|
| 경계 조건 3분류(정적/환경/동적), 객관적 판정 방법 요구 | ISO 34503 |
| 명세 형식 mode / include / exclude / conditional | ISO 34503 |
| 설계 조건과 실제 조건의 구분, 실행 시 관측 요구 | ISO 34503, ASAM OpenODD |
| ODD를 독립 문서로 두고 스코프·시나리오·커버리지를 파생 | ISO 34503, ASAM OpenODD, BSI PAS 1883 |
| 명시 제외 절 — 검토 후 제외와 미검토의 구분 | ISO 34503 |
| ODD 이탈 — 실제 조건과 설계 조건의 대조, 이탈 시 대응 | ISO 34503, ISO 21448 |
| 판정 등급, 안전 정지(최소 위험 조건) | ISO 34503, SAE J3016 |
| scene · situation · scenario 3분 (관측자 관점 기준) | ISO 34501, Ulbrich et al. |
| 시나리오 구성 요소 — 행위자 · 행동 · 트리거 | ASAM OpenSCENARIO |
| 계층 없는 태그 기반 범주화, 태그 범주 | ISO 34504 |
| abstract 단계 — functional과 logical 사이의 형식화 | ISO 34501, ASAM OpenSCENARIO |
| 결함의 구성 — 3갈래 요인의 조합으로 위험 시나리오 | ISO 34502 |
| 알려진 것과 알려지지 않은 것 — 미지 요인 vs 미지 조합 | ISO 21448 |
| 검증 환경 계층(MIL→SIL→HIL→실차)의 충실도·통제·재현성 | X-in-the-loop 검증, ISO 26262 V-모델 |
| 시나리오의 환경 할당, 합격 기준 분리, 재현성 조건 | ISO 34502 |

### 온톨로지 공학

| 가져온 구조 | 출처 |
|---|---|
| 상위 온톨로지 — BFO 기반 구축 | kul-ai/ontology-autonomous-driving |
| 모듈 구조 — entity/related 분리, 어휘/형식화 분리 | lu-w/auto |
| 온톨로지 품질 검사 — 자동 검사와 정규화 직렬화 | kul-ai/ontology-autonomous-driving |
| 시간 정체성 — 개체의 시간 관통 정체성 | lu-w/auto |
| 역량 질문 — 온톨로지 요구사항 정의 | METHONTOLOGY, NeOn |
| 관계 어휘 — 표준 관계 재사용 | Relations Ontology |
| 추론 프로파일 — OWL 2 RL/EL/DL | W3C OWL 2 |
| 결함 카탈로그 — 온톨로지 pitfall 검사 | OOPS! |
| 정보 내용 개체 — `agt:Chunk`의 상위 클래스 (정렬 예정) | IAO |
| `part-of` — 표준 부분-전체 관계와 공리 | 상위 온톨로지 mereology |
| 정의 형식 — 속 + 종차 / 폐기 — `owl:deprecated`, `replaced_by` | OBO Foundry 관행 |
| 라벨·동의어 — prefLabel / altLabel / hiddenLabel | W3C SKOS |
| 순서 있는 부분 — `co:List`, `co:index` | Collections Ontology |
| 출처·버전 어휘 — `wasDerivedFrom` 등 | W3C PROV-O |
| 원칙의 shape화 | W3C SHACL |

### 지식 구조화

| 가져온 구조 | 출처 |
|---|---|
| 자립적 최소 단위(청크) — 7±2, 라벨 필수, 한 주제 | 인지과학(Miller), 구조적 글쓰기(Horn) |
| plane = 하위 클래스 — 정보 유형의 특수화 | 모듈형 문서(DITA specialization) |
| 참조 재사용 | 모듈형 문서(DITA conref) |
| 이름 붙은 그래프 4분 구조, 내용 해시 IRI(trusty URI) | 나노출판(nanopublication) |
| tangle / weave — 별도 도구가 아닌 그래프 질의 | 문학적 프로그래밍(Knuth) |

### 추적성

| 가져온 구조 | 출처 |
|---|---|
| 추적성 정보 모델 — 대상 유형 × 링크 타입 × 제약 | 요구공학 TIM 문헌 |
| 링크 타입 의미론, 단방향 저장 | 요구공학 링크 의미론, SysML |
| 링크 타입 분류 — 의존/정련/진화/충족/근거 | Ramesh & Jarke 참조 모델, SysML |
| 구축과 복원 — 복원의 사후성, 중간 단계의 완충 효과 | 추적성 복원 연구 |
| 읽기·쓰기 인수인계 — 탐색·편집 컨텍스트 분리 | SWE-Edit |
| 후보 추림과 판정 분리 — 임베딩 검색 → 분류 → 확인 | 추적성 복원 연구 (LiSSA 계열) |
| 산출물 밖 링크 모델, 앵커 해석기 | Eclipse Capra |
| 링크 붕괴, 변경 통지 트리거, 규칙 기반 갱신 | Eclipse Capra, 추적성 유지 연구 |
| 추적 매트릭스 — plane × plane 격자 | Eclipse Capra |
| 재판정 규칙 — 변경 유형별 링크 갱신 | 추적성 유지 연구 |

### 기타

| 가져온 구조 | 출처 |
|---|---|
| 호 일관성 — 증분 제약 전파 | CSP 표준 알고리즘 |
| plane 후보 — 소프트웨어 산출물 유형과 판정 방식 | SWEBOK 산출물, 아키텍처 뷰포인트 |
| 요인 하위 유형 8·한정자 3(missing·incorrect·extraneous)·트리거·영향 | 직교 결함 분류 ODC v5.2 (Chillarege, IBM) |
| 도입 순서 — 단계별 측정 가능 산출 | (고유) |

## 1.1 외부 조사로 확인한 세부 (2026-09-11)

부록 E의 바인딩과 용어집이 기대는 명세를 원문에서 확인했다. 확인/정정/미확인을 구분한다.

| 대상 | 확인된 세부 | 이 저장소 |
|---|---|---|
| **OKF v0.2** ([SPEC](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)) | 필수 `type`뿐. 권장 `title`·`description`·`resource`·`tags`. **`sources`는 객체 목록** — `resource`(필수)·`id`·`title`·`author`·`usage_count`·`last_modified`. `generated {by, at}`, `verified` = `{by, at}` 목록. `status` = draft/stable/deprecated(기본 stable), `stale_after`. 행위자 `<producer>/<version>`·`human:<id>`·`process:<id>`. 예약 `index.md`(frontmatter 없음)·`log.md`(ISO 날짜 제목). 미지 키는 거부 불가·보존. `type: Attested Computation`에 `runtime`·`parameters`·`computation`·`executor`·`attester` | **정정**: `sources`를 `[{resource: IRI}]`로 이행. `stale_after` ↔ 8.27 증거 노화 후보. 판정식 "계산 필드"는 Attested Computation |
| **ASAM OpenODD 1.0** ([6.4 모듈](https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/06_model_concept/06_04_openodd_modules.html), [10.2 택소노미 YAML](https://publications.pages.asam.net/standards/ASAM_OpenODD/ASAM_OpenODD/latest/specification/10_yaml/10_02_openodd_export_taxonomy_yaml.html)) | 모듈 = `id`·`title`(LangString)·`description`·`comment`·`is_root`·`is_active`·`labels`·`tags`, INCLUDE·EXCLUDE 각 최대 하나, 연산자 AND/OR. **MODULE = INCLUDE ∧ ¬EXCLUDE**. 식 5종 `LowerBound`·`UpperBound`·`Equal`·`Range [a .. b]`·`CategoricalList`. `unknown` 리터럴 = 값 부재일 때 참. 택소노미 YAML: 최상위 `TAXONOMY:`, 속성은 `이름: float velocity`·`boolean`·범주 목록, 단위 체계 | **2026-09-11 정합**: `project-odd.yml`을 YAML 매핑 참조 모양으로 재작성(Release Presentation 2025-04-03 slide 6·8 — `TAXONOMY:`·`MODULES:`·`INCLUDE_AND:`, 식 리터럴/`"[a .. b] unit"`). 확장 키는 대문자 `ATTRIBUTES`·`LITERALS`·`CHECKS`·`EXCLUSIONS_REVIEWED`·`EXCLUDE_WHEN_UNKNOWN`. `taxonomy.yml`은 `TAXONOMY:` 아래 범주 3 레코드(속성은 ODD 문서가 확장) |
| **ASAM OpenSCENARIO DSL 2.x** ([coverage](https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/language-reference/coverage_main.html), [scenarios](https://publications.pages.asam.net/standards/ASAM_OpenSCENARIO/ASAM_OpenSCENARIO_DSL/latest/conceptual-overview/writing_a_scenario.html)) | `keep(it in [a..b])` 제약, `do serial/parallel` 시간 구성, actor = 시나리오를 담는 구조체. **`cover(expr, event:, target:)`** = 커버리지 수집점, 스칼라 식, 목표 횟수 | 부록 E.5·9.10·8.23의 `keep`/`cover` 용법과 일치 |
| **CEL** ([langdef](https://github.com/google/cel-spec/blob/master/doc/langdef.md), [cel-go](https://pkg.go.dev/github.com/google/cel-go/cel)) | 메모리 안전·부작용 없음·종료 보장·강타입·결정론. 값 또는 오류. **미지값(unknown)** 은 cel-go의 부분 평가(`PartialVars`·`OptTrackState`·잔여 AST)로 다룬다 | `when`의 세 값(참·거짓·판정 불가)은 값·오류·미지 → 잔여 식으로 사상 |
| **ISO/IEC/IEEE 29148** | 검증 방법 4종 inspection·analysis·demonstration·test. 전방/후방 추적성 | 판정 유형 5종(그래프 질의·파일 검사·실행 검사·외부 조회·사람 확인)의 대응: 질의·파일 ≈ analysis/inspection, 실행 ≈ test/demonstration, 사람 ≈ inspection |
| **EARS** (Mavin, RE'09) | 다섯 패턴 ubiquitous · event-driven(When) · state-driven(While) · unwanted behaviour(If…then) · optional(Where) + complex | 7.2 `requirement` 실체 |
| **ISO 34503:2023** | 최상위 3범주 **scenery elements** · environmental conditions · dynamic elements | 이 체계의 "정적 요소(static element)"는 scenery의 소프트웨어 적응. "ODD exit"·국문 명칭은 **미확인** |
| **ODC v5.2** (Chillarege, IBM) | 결함 유형 8: function · interface · checking · assignment · timing/serialization · build/package/merge · documentation · algorithm. **한정자 3: missing · incorrect · extraneous**. 열 때 activity·trigger·impact, 닫을 때 target·type·qualifier·age·source | **정정**: 노트 8.17·결정에 `extraneous` 추가 |
| **LinkML** | YAML 스키마 → JSON Schema·SHACL·ShEx·OWL·GraphQL·SQL DDL·Python 생성 | 부록 E.1 온톨로지 층의 LinkML |
| **ISO/IEC 15026-2** | 보증 사례 = 최상위 주장 · 논증 · 증거 · 명시 가정. 추론 = 하위 주장(전제)에서 결론 | 증거 기록(9.11)의 "증거" 용어 |
| **ISO 25964 · ISO/IEC/IEEE 42010** | 통제 어휘 = 개념마다 일관된 라벨 하나를 정한 목록. 뷰 = 뷰포인트 규약에 따라 관심사를 담는 산출물 | 용어집 "통제 어휘"·"뷰" |
| **rules_python** ([sdist](https://github.com/bazel-contrib/rules_python/issues/2410)) | sdist 빌드 지원(저장소 규칙·빌드 액션). PyYAML ≥ 6.0.1은 sdist 빌드 가능 | **2026-09-11 적용**: `pyyaml==6.0.2`를 잠금에 추가(호스트 휠 + sdist 두 해시), `kb_yaml.py` 삭제 |
| **LEDGER** ([2606.28379](https://arxiv.org/abs/2606.28379), ACL 2026 Findings) | 노드 (id, 요약, 임베딩, 타입 section/paragraph/figure/table/equation, 위치, 시각). 엣지 CONTAINS(DOM) · REFERENCES(최소 명시 참조) · DEPENDS(반사실 검사 — 빼면 의미상 불완전) · RELATED(코사인 ≥ 0.7, REFERENCES·DEPENDS 없을 때만, 양방향). 검색: 대상 식별 → 상·하류 확장 → 우선순위(대상 > REFERENCES > DEPENDS > CONTAINS > RELATED) → 예산 패킹. 편집 후 검사 3: 참조 무결성·용어 일관성·의미 응집. 76% vs 56% 일관성, 편집당 ~1,535 토큰, 85~92% 토큰 절감 | `dependency-graph-design.md` 대응표. DEPENDS의 반사실 검사는 이 체계에서 `proposal` 종류 |
| **LARGER** ([2605.16352](https://arxiv.org/abs/2605.16352)) | 정식 제목 *Lexically Anchored Repository Graph Exploration and Retrieval*. 노드 4종 directory·file·class·function, 엣지 contains·imports·invokes·코드–테스트/문서 교차 링크. 에이전트의 어휘 검색 결과가 그래프 진입점(active set), 앵커마다 K-hop·신뢰 임계 θ·상위 k 확장, 컨텍스트 사영 Π. LocBench Acc@5 +11.8 | 앵커 = 청크 IRI, K-hop 확장 = 작업 집합 조립(§4) |

**미확인으로 남긴 것**: 역량 질문의 국문 정역, ISTQB 국문 용어집의 "합격 판정 기준" 표기, ISO 34503 국문 명칭. (OpenODD 모듈 YAML 키는 ASAM 릴리스 발표 slide 8에서 확인 — 명세 10.3 페이지 자체는 404.)

## 2. 참조 프로파일

코어를 소프트웨어 개발 작업에 특수화한 결정들은 [`ontology.md`](ontology.md)의 "참조
프로파일" 표로 옮겼다 — 그것은 출처 기록이 아니라 어휘의 일부이기 때문이다.

## 3. 관련 산출물과 사례

- **하네스 지식** — 두 참조 저장소:
  `../harness-functional`(ODD + functional: 어휘 TBox·shapes·도구),
  `../harness-concrete`(logical + concrete: union root·부품 라이브러리·조립 명세).
  내용의 원천일 뿐 빌드 의존이 아니다. 두 저장소의 일반 방법론은 결정 d-0013~d-0020과
  d-0156~d-0185로 승격되어 있고 출처는 `derived_from`으로 남아 있다.
- **사례 프로젝트** — device harvest 웹서비스(`~/git/agrtls/webservice`). 이 체계의
  검증 케이스로 쓰기로 한 대상이며, 아직 적용되지 않았다.
