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
| 요인 하위 유형·한정자·트리거·영향 | 직교 결함 분류 ODC (Chillarege) |
| 도입 순서 — 단계별 측정 가능 산출 | (고유) |

## 2. 참조 프로파일

코어을 소프트웨어 개발 작업에 특수화한 결정들은 [`ontology.md`](ontology.md)의 "참조
프로파일" 표로 옮겼다 — 그것은 출처 기록이 아니라 어휘의 일부이기 때문이다.

## 3. 관련 산출물과 사례

- **하네스 지식** — 두 참조 저장소:
  `../harness-functional`(ODD + functional: 어휘 TBox·shapes·도구),
  `../harness-concrete`(logical + concrete: union root·부품 라이브러리·조립 명세).
  내용의 원천일 뿐 빌드 의존이 아니다. 두 저장소의 일반 방법론은 결정 d-0013~d-0020과
  d-0156~d-0185로 승격되어 있고 출처는 `derived_from`으로 남아 있다.
- **사례 프로젝트** — device harvest 웹서비스(`~/git/agrtls/webservice`). 이 체계의
  검증 케이스로 쓰기로 한 대상이며, 아직 적용되지 않았다.
