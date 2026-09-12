---
from: hci
status: approved
targets: [https://agentic-knowledge-base.dev/id/chunk-d0009, https://agentic-knowledge-base.dev/id/chunk-d0010, https://agentic-knowledge-base.dev/id/chunk-d0041, https://agentic-knowledge-base.dev/id/chunk-d0053, https://agentic-knowledge-base.dev/id/chunk-d0081, https://agentic-knowledge-base.dev/id/chunk-d0082, https://agentic-knowledge-base.dev/id/chunk-d0096, https://agentic-knowledge-base.dev/id/chunk-d0102, https://agentic-knowledge-base.dev/id/chunk-d0105, https://agentic-knowledge-base.dev/id/chunk-d0106, https://agentic-knowledge-base.dev/id/chunk-d0110, https://agentic-knowledge-base.dev/id/chunk-d0111, https://agentic-knowledge-base.dev/id/chunk-d0126, https://agentic-knowledge-base.dev/id/chunk-d0148, ontology/related/, kg/, docs/decomposition-audit.md, purpose-statement.md]
sources:
  - "LEDGER: Scaling Agentic Document Editing with Dependency-aware Graph Retrieval — arXiv 2606.28379 (2026-06)"
  - "LARGER: Lexically Anchored Repository Graph Exploration and Retrieval — arXiv 2605.16352 (2026-05)"
---

# LEDGER·LARGER를 참고한 의존성 그래프 — 추적성(traceability)의 상세 설계

유저(2026-09-04): LARGER의 명시적 의존성 그래프를 참고해 온톨로지·KG를 구상 → 정정:
세 엣지(명시적 참조·암묵적 의미 의존·의미적 관련성)는 **LEDGER**(문서 편집)의 것이고,
**LARGER**는 코드 저장소 그래프 탐색·검색. 둘 다 반영한다. 두 논문은 arXiv HTML을 읽고
요약했다(§0). 구조도 v4(purpose-statement.md)는 추적성을 한 줄("각 종류의 인터페이스를
기준축으로 plane 간 항목을 mapping")로만 두고 상세를 이 문서에 맡긴다.

## 0. 두 논문의 요지 (설계에 쓰는 부분만)

**LEDGER** — 문서를 의존성 그래프로 두고 편집마다 필요한 컨텍스트만 검색.
- 노드 = 문서 단위(section·paragraph·figure·equation). 저장: id·요약·임베딩·타입·위치·수정 시각.
- 엣지 4종: **CONTAINS**(계층, DOM에서 규칙 추출) / **REFERENCES**(명시적 참조 — 본문의
  식별자 언급, LLM 추출 + 알려진 식별자로 검증) / **DEPENDS**(암묵적 의미 의존 — "u_j를
  빼면 u_i가 의미적으로 불완전한가"의 **반사실 검사**, LLM) / **RELATED**(대칭, 임베딩
  코사인 > θ=0.7, 이미 REFERENCES·DEPENDS인 쌍 제외).
- 검색 4단계: 대상 식별 → 의존 확장(upstream ∪ downstream) → 우선순위
  **targets ≫ REFERENCES ≫ DEPENDS ≫ CONTAINS ≫ RELATED** → 토큰 예산 안에서 탐욕 패킹
  (문서의 10~15%, 5K~100K 문서에서 편집당 약 1.5K 토큰으로 일정).
- 갱신: 수정 노드에 붙은 엣지만 제거·재계산(증분). 편집 후 검사 3종: 참조 무결성 / 용어
  일관성(수정 노드의 핵심 용어 vs 의존 노드) / 의미 응집(임베딩 재계산, 유사도 하락 탐지).
- 수치: 일관성 56→76%, 토큰 85~92% 절감. "명시적 의존 표현이 비싼 내부 추론을 일부 대체".

**LARGER** — 코드 저장소 그래프를 에이전트의 **기존 검색 루프 안에서** 쓴다.
- 노드 = 디렉토리·파일·클래스·함수. 엣지 = contains·imports·invokes·cross-artifact
  (소스↔테스트·소스↔문서). AST 정적 분석(Python·Go·TS·C), **엣지 신뢰도 ω∈[0,1]**
  (출처 기반), Leiden 커뮤니티 탐지(서브시스템 분할).
- **lexical anchor**: 어휘 검색 히트를 그래프 노드에 정렬(`align`) → **active set** M_t.
  각 앵커의 K-hop 이웃을 ω ≥ θ(0.5)로 거르고 점수 상위 k(10)만 — 결과를 **검색 결과
  안에 섞어** 돌려준다(별도 그래프 툴·DB 없음). 단계당 오버헤드 Δ = m·k·L_max로
  저장소 크기와 무관.
- 갱신: 커밋 단위 — 바뀐 파일만 재파싱, 없어진 파일 노드 제거, 나머지는 캐시.
- 수치: 파일 위치 찾기 Acc@5 +11.8~13.9p, 시간 −40%, 토큰 −32%. 절제 실험에서 **그래프
  확장 제거가 가장 큰 손실(−13.5)**, 신뢰도 점수 −4.7, 커뮤니티 −4.1.

## 1. 두 논문의 요소가 이 체계의 어디에 닿는가

| 논문 요소 | 이 체계 | 있음? |
|---|---|---|
| LEDGER 노드(id·요약·임베딩·타입·위치·시각) | node(chunk): IRI·**라벨**=요약·—·plane/level·`co:index`·`generatedAtTime` | 임베딩만 없음 |
| LEDGER **CONTAINS** / LARGER contains | 구성체 `hasDirectPart` | 있음(38) |
| LEDGER **REFERENCES** | d-0010에 **없음** | 본문에 `d-NNNN` 29회·절 인용 117회 — 추출만 하면 됨 |
| LEDGER **DEPENDS** | `assumes`·`refines`·`constrains`·`derives-from`·`depends-on` — d-0010 12타입 전부 여기 | 어휘 없음, 링크 0 |
| LEDGER **RELATED** | 없음. 가장 가까운 것: `suspect` 전파 대상(d-0106), 구성체 동거 | 없음 |
| LARGER imports·invokes·cross-artifact | `artifact` plane 링크: `satisfies`·`verifies`(소스↔테스트)·`targets`(소스↔문서) | artifact node 0 |
| LARGER **엣지 신뢰도 ω** | d-0110 판정 근거 5등급(구축 기록 > 동시 편집 > 테스트 공동 커버 > 임베딩 > 같은 세션 읽음) | 등급은 있으나 **수치·상태 없음** |
| LARGER **커뮤니티 탐지** | 구성체 — 단 구성체는 선언, 커뮤니티는 계산 | "통합이 필요한 것" **후보 생성기**로 쓸 수 있음 |
| LEDGER 검색 4단계 / LARGER 앵커→확장 | d-0082 라벨 목록 → 펼치기, d-0126 situation, d-0081 툴 표면 | **알고리즘이 없었다** — §4 |
| LEDGER 증분 갱신 / LARGER 커밋 단위 | d-0106 경계에서 일괄 재판정, Bazel 캐시 | 링크가 없어 미실행 |
| LEDGER 편집 후 검사 3종 | 참조 무결성 = 깨진 참조 검사 / 용어 일관성 = vocab 게이트·라벨 부패 / 의미 응집 = 없음 | 1.5/3 |
| LEDGER "10~15%·1.5K 토큰 일정" / LARGER Δ = m·k·L_max | d-0041 컨텍스트 예산 — L_max = **42줄**이므로 Δ = m·k·42가 그대로 예산식 | 실측 없음 |

**핵심 관찰 셋**
1. 이 체계의 링크 타입은 전부 DEPENDS 족이고 **REFERENCES·RELATED가 비어 있다.** 지금
   기계로 만들 수 있는 것은 REFERENCES뿐이며, "가능성이 살아있는 채로"(목적 진술)는
   RELATED 후보와 ω<1 링크가 실현한다.
2. 두 논문 모두 **검색·편집 루프 안에서** 그래프를 쓴다 — 별도 질의 도구가 아니라 읽기
   응답에 이웃을 섞어 준다. 이것이 d-0081 "툴 표면이 배정을 따른다"·d-0082 "읽기 응답은
   라벨 목록"의 구체 알고리즘이고, 활용 도구 `situation/labels`의 설계가 된다.
3. LEDGER의 "명시적 의존 표현이 내부 추론을 대체한다"는 결과는 이 체계의 존재 이유
   (d-0040 세 단절, d-0036 좁은 컨텍스트)를 외부에서 실측한 것이다.

## 2. 온톨로지 — `related/trace` 모듈

### 2.1 네 족을 상위 속성으로, 기존 12타입을 하위로 (d-0053 subPropertyOf)

```
agt:contains            CONTAINS  = agt:hasDirectPart (이미 있음, 구성체) — 링크 족이 아니라 구성 관계
agt:dependsOn           (추상 상위, 직접 사용 금지)
├── agt:references      REFERENCES ⊑ dcterms:references  방향: 참조하는 쪽 → 참조되는 쪽
│   ├── agt:cites         본문 인용(d-NNNN·절 번호·그림·표 번호)
│   └── agt:targets       (기존) annotation → 임의
├── agt:semanticallyDependsOn   DEPENDS  방향: 사용/결론 → 정의/전제
│   ├── agt:assumes · agt:refines · agt:satisfies · agt:constrains · agt:verifies · agt:derivesFrom (기존)
│   ├── agt:usesConcept   node → 온톨로지 개념(정의). "정의와 사용"
│   └── agt:imports · agt:invokes   (artifact 프로파일, LARGER) — 골격이 아니라 profile/development
└── agt:relatedTo       RELATED ⊑ skos:related (대칭)
    ├── agt:coUpdatesWith  함께 갱신 (대칭)
    └── agt:conflictsWith  (기존)
```
`supersedes`·`prov:wasRevisionOf`는 시간축 — 족 밖.

### 2.2 링크는 개체 (d-0111) — 상태·근거·신뢰도

```turtle
id:link-0001 a agt:Link ;
    agt:from id:chunk-d0067 ; agt:to id:chunk-d0008 ;
    agt:kind agt:derivesFrom ;
    agt:state "candidate" ;             # candidate | valid | suspect | invalid   (d-0106에 candidate 추가)
    agt:evidence agt:constructionRecord ;   # d-0110 5종 + LEDGER 반사실 검사(agt:counterfactualTest) + 임베딩
    agt:confidence 0.9 ;               # LARGER ω ∈ [0,1] — evidence 종류에서 파생(§2.3), 손으로 안 씀
    agt:evidenceNote "decomposition-audit: 3.3절 누락 보충" ;
    prov:generatedAtTime "…" .
```
직접 트리플(`chunk-d0067 agt:derivesFrom chunk-d0008`)은 **valid이고 ω ≥ θ인 링크에서만
생성**(질의 편의, 생성물). candidate는 개체로만 — "가능성이 살아있는 채로".

### 2.3 ~~신뢰도 ω = 근거 종류의 함수~~ — **폐기 (2026-09-10, 노트 v5 9.11절 "수치가 없다")**

아래 표는 기록으로 남긴다. 실제 어휘는 `agt:when`(조건) + `agt:Evidence` 장부(종류·참조·극성)이며
선호는 종류 서열에서 파생된다. 표의 서열은 그 서열의 원안이다.


| 근거 | ω (초안) | 비고 |
|---|---|---|
| 구축 기록 (편집 부산물, 본문 식별자 인용) | 1.0 | REFERENCES 추출은 식별자 검증 통과 시 1.0 |
| 동시 편집 이력 (같은 커밋) | 0.8 | LARGER "provenance-aware" |
| 테스트 공동 커버 | 0.8 | `verifies` |
| 반사실 검사 통과 (LEDGER DEPENDS, LLM) | 0.7 | 유저 확정 전까지 candidate |
| 임베딩 유사도 > 0.7 | 0.5 | RELATED **후보만** (d-0009 확정 근거 금지 유지) |
| 같은 세션에서 읽음 | 0.3 | 구축 기록의 약한 형태 |
θ(확장 컷) 기본 0.5 — LARGER 기본값. 값은 지표(확정 정밀도, d-0112)로 조정.

### 2.4 족별 전파 (d-0106 suspect 규칙을 족 단위로)

| 족 | 대칭 | `to` 변경 시 | `from` 변경 시 | plane 규칙 |
|---|---|---|---|---|
| references | 아니오 | from → suspect | — | 제한 없음 |
| semanticallyDependsOn | 아니오 | from → suspect | — | d-0004 단방향 안에서만 |
| relatedTo | 예 | 양쪽 suspect | 양쪽 suspect | 같은 plane 권장 |
구성체와의 경계: 구성체 = **함께 읽힘·순서**(CONTAINS, 유저 결정: part-of 묶음),
relatedTo = **함께 갱신**(RELATED). "무효화가 함께 번져야 함"은 relatedTo 링크로.

## 3. 지식그래프

| 파일 | 담는 것 | 손/생성 |
|---|---|---|
| `kg/references-kg.ttl` | REFERENCES — 본문에서 추출 | **생성** (d-0159 드리프트 가드) |
| `kg/trace-kg.ttl` | DEPENDS·RELATED 링크 개체 (candidate 포함) | 손 + 도구 제안, 확정은 ω·근거 |
| `kg/embeddings/` (선택) | node 임베딩 벡터 | 생성, 그래프 밖 캐시 — RELATED 후보·의미 응집 검사용 |
| `space/*-space.ttl` | 사다리 후보(refines)·제약 (d-0100) | 후보 관리 method |
| `kg/revision-kg.ttl` | 시간축 (내용 해시 버전) | 커밋 경계 도구 |
| (계산) 커뮤니티 | Leiden 결과 → **구성체 후보** 목록 | 생성, 저장 안 함 — 유저가 채택하면 composite-kg에 손으로 |

## 4. 조회 도구 — situation 조립 알고리즘 (LEDGER 4단계 + LARGER 앵커·확장)

활용 도구 `situation/labels`의 명세. **읽기 응답 안에 이웃을 섞어 준다**(별도 툴 없음).

1. **앵커** — 에이전트의 검색(라벨 목록 grep·IRI 지정·지시문 임베딩)이 맞힌 node = active
   set M. LARGER `align`: 텍스트 히트 → `assertionLocation` 역사상 → IRI.
2. **확장** — 각 앵커에서 K-hop(기본 1), ω ≥ θ인 링크만, upstream(내가 의존) ∪
   downstream(나에게 의존). **스코프 필터**: 역할의 read plane 밖은 제외(d-0081) — 이것이
   LEDGER·LARGER에 없는 이 체계 고유의 단계이며 "complex context coupling 방지"의 실체.
3. **우선순위** — targets ≫ references ≫ semanticallyDependsOn ≫ contains ≫ relatedTo,
   같은 족 안에서는 ω 내림차순.
4. **패킹** — 라벨만(1줄) → 본문(≤42줄) 순으로 예산 B까지 탐욕. Δ = m·k·42 (d-0041의
   예산식이 된다). B 초과분은 **라벨만** 남긴다 — 라벨 목록이 인터페이스(d-0082).
5. **출력** = situation: 앵커 본문 + 이웃 라벨/본문 + 각 항목의 (족, ω, state). candidate
   링크는 "가능성"으로 표시되어 함께 나온다.

## 5. 갱신과 검사 — 게이트에 얹는 것

| LEDGER/LARGER | 이 체계 | 어디에 |
|---|---|---|
| 수정 노드의 엣지만 재계산 / 바뀐 파일만 재파싱 | 본문 해시 변경 → 그 IRI의 링크 suspect → 경계에서 재판정(d-0106). Bazel 캐시가 증분 | 내용 해시 + link 도구 |
| 참조 무결성 | REFERENCES의 `to`가 존재하는 IRI인가 — FAIL | validate 확장 (깨진 참조 = FAIL) |
| 용어 일관성 | 수정 node의 `usesConcept` 대상이 여전히 유효한 개념인가(폐기 참조 경고 d-0035) + 라벨 부패 재검토 | vocab 게이트 + WARN 채널 |
| 의미 응집 | 임베딩 재계산, 유사도 하락 → relatedTo 링크 suspect | 새 검사, 임베딩 캐시 필요 — **선택** |

## 6. 지금 있는 153개에 적용하면 (복원 경로, d-0009 예외)

| 족 | 원천 | 예상 수 | ω |
|---|---|---|---|
| references/cites | 본문 `d-NNNN` 29회 | 29 | 1.0 |
| references/cites | `(노트 N.N절)` 117회 → decomposition-audit 절→node 대응표로 매핑 | 수십~100+ | 1.0 (대응표가 기계적) |
| semanticallyDependsOn/usesConcept | 본문의 `agt:` 개념·라벨 등장 → 개념 IRI | 수백 (후보) | 0.7 반사실 검사 후 |
| semanticallyDependsOn/assumes | 152 공백 → 기본 가정 후 좁힘 | 153 | — |
| semanticallyDependsOn/derivesFrom | audit "흡수·분할·병합" | ~10 | 1.0 |
| relatedTo/coUpdatesWith | 구성체 동거 + 임베딩 > 0.7 (REFERENCES·DEPENDS 쌍 제외) | 후보 수백 | 0.5 |
**결과**: REFERENCES만으로 링크 밀도 0 → ~1, 영향 분석(d-0148) 첫 질의 가능. 우선순위 규칙
덕에 RELATED 후보가 많아도 situation을 부풀리지 않는다(예산 패킹에서 뒤로 밀림).

### 6.1 현재 상태 실측
- 그래프의 구조 관계: `agt:hasDirectPart` 구성체 38(node 153 전부 소속) · `agt:assumes` **1**(d-0001) ·
  `prov:wasDerivedFrom` 153 · d-0010 링크 타입 **0** · 구성체 순서(`co:index`)·중첩 0.
- 잠재 링크: node 20개가 본문에서 다른 node를 29회 언급, `(노트 N.N절)` 인용 117회.
- 원인 다섯 층: ① `related/trace` 어휘 없음 ② 링크 kg 파일 없음(링크는 node 밖에 저장, d-0105)
  ③ 하네스가 읽기·쓰기 집합을 기록하지 않음(d-0009 구축 메커니즘 부재) ④ 153개는 문서
  분해로 들어와 복원 경로 대상 ⑤ 전부 concrete라 수직 링크 `refines`는 정의상 0.
- 지금 양 끝이 있는 타입: decision↔decision(`supersedes`·`derivesFrom`·`dependsOn`)과 `assumes`.

## 7. 결정 지점

- **(a)** 네 족(contains·references·semanticallyDependsOn·relatedTo)을 상위 속성으로, d-0010
  12타입을 하위로 — 수용? (d-0010 "TIM은 바꾸기 어렵다" — 지금 정한다)
- **(b)** 링크 상태에 `candidate` 추가, 신뢰도 ω를 근거 종류에서 **파생**(손으로 안 씀)
- **(c)** REFERENCES는 생성물 — 손으로 쓰지 않는다
- **(d)** 표준 정렬: `agt:references ⊑ dcterms:references`, `agt:relatedTo ⊑ skos:related`
- **(e)** 구성체 = 함께 읽힘·순서, relatedTo = 함께 갱신 — 통합 기준 셋째를 링크로 이관
- **(f)** `usesConcept`은 개념 IRI로 바로
- **(g)** 임베딩 사용 허용 — RELATED **후보**·의미 응집 검사·앵커 확장에만. 확정 근거 금지는 유지(d-0009)
- **(h)** 커뮤니티 탐지를 **구성체 후보 생성기**로 — "통합이 필요한 것"의 기계 제안, 채택은 유저
- **(i)** situation 도구(§4)를 첫 활용 도구로 확정, 예산식 Δ = m·k·42
- **(j)** `imports`·`invokes`는 골격이 아니라 `profile/development`에

hci 권고: 전부 수용. (g)만 유의 — 임베딩 모델 선택·저장이 ODD 조건(환경·의존성)에 새로
들어가야 한다(ODD 확장 동반).

**출처**: [LEDGER (arXiv 2606.28379)](https://arxiv.org/abs/2606.28379) ·
[LARGER (arXiv 2605.16352)](https://arxiv.org/abs/2605.16352)

## 답
유저(2026-09-12): `status: approved` 태깅 + orchestrator에 구두 지시 "이후에 dependency-graph도 반영해줘" — hci 권고(전부 수용) 채택.

인수: orchestrator 2026-09-12 — 결정 지점 (a)~(j)를 현재 온톨로지·결정·도구와 대조해 남은 것만 반영했다.
- 이미 반영돼 있던 것 (v3~v5 재도출, 2026-09-04~11): (a) 네 족 상위 속성 — `related/trace/trace-ontology.ttl`(`dependsOn` > `references`·`semanticallyDependsOn`·`relatedTo`, 구성 관계는 `hasDirectPart`) · (b) `agt:CandidateLink`/`agt:ConfirmedLink` + `linkState`, ω는 9.11절에 따라 폐기(`confidence` deprecated) · (c) `kg/references-kg.ttl` 생성(`extract_refs`) · (d) `agt:references ⊑ dcterms:references`, `agt:relatedTo ⊑ skos:related` · (e) 복합체 = 함께 읽힘·순서, `relatedTo` = 함께 갱신(`rules.md` §2·§4) · (f) `agt:usesConcept` 속성 · (g) 임베딩은 후보 추림에만(`p10-link-judgement-evidence`·`p12-knowledge-retrieval-by-label`, 증거 종류 `embeddingSimilarity`) · (i) situation 도구 = `workset` 첫 형태 + `p0-workset-anchor-neighbourhood` · (j) `imports`·`invokes`는 코어에 없음. 대상 옛 결정 14건은 전부 deprecated이고 `p10-*`·`p9-*`·`p12-*`가 대체했다.
- 이번에 반영: (h) 결정 신설 `p4-community-detection-proposes-composites`(세 청크, 출처 개체 `id:doc-dependency-graph-design`, refines r-011) · (i) 예산식 Δ = m·k·42를 `p0-workset-anchor-neighbourhood/rationale`와 `method.md` §8에 · 문서 네 곳(`rules.md` §2·§4, `ontology.md`, `method.md` §6·§8)의 이 항목 참조를 결정·도구 참조로 승격 — 이 항목은 채널에서 제거돼도 문서가 깨지지 않는다.
- 반영하지 않고 남긴 것: (f) 기존 청크에 `usesConcept` 링크 복원(수백 건 후보 — 후보 생성 도구 `link` 몫, 도입 3단계) · (g)의 ODD 조건(임베딩 모델·저장) — 임베딩 도구가 실제로 생길 때 ODD를 먼저 확장 · §5 의미 응집 검사(임베딩 필요, 선택) · §6 `assumes` 공백(가정 1건 — 도입 4단계) · (h)의 도구 자체(`project` 계열, 도입 8단계).

## 외부 조사로 채운 세부 (2026-09-11)

- **LEDGER** 노드는 (id, 요약, 임베딩, 타입 section/paragraph/figure/table/equation, 위치, 수정 시각). RELATED는 코사인 ≥ 0.7이고 **REFERENCES·DEPENDS가 없을 때만**, 유일하게 양방향. DEPENDS는 반사실 검사("빼면 의미상 불완전·모호·미정의인가")로 추출 — 이 체계에서 `agt:counterfactualTest`를 폐기하고 `proposal` 종류로 흡수한 것과 정합(언어모델의 반사실 검사는 제안). 검색은 대상 식별(명시 대상 또는 임베딩 유사) → 상·하류 확장 → 우선순위(대상 > REFERENCES > DEPENDS > CONTAINS > RELATED, "수치보다 순서") → 예산 패킹(문서 크기와 무관하게 O(1), 10~15%). 편집 후 검사: 참조 무결성 · 용어 일관성 · 의미 응집(임베딩 유사도 하락). 76% vs 56%, 편집당 ~1,535 토큰, 85~92% 절감 (arXiv 2606.28379, ACL 2026 Findings).
- **LARGER** 정식 제목은 *Lexically Anchored Repository Graph Exploration and Retrieval* — "의존성 그래프"는 제목이 아니다. 노드 directory·file·class·function, 엣지 contains·imports·invokes·코드–테스트/문서 교차 링크. 에이전트의 어휘 검색 결과가 active set M_t로 그래프에 앵커되고, 앵커마다 K-hop·신뢰 임계 θ 이웃 중 상위 k를 골라 컨텍스트 사영 Π로 합친다. LocBench 파일 Acc@5 +11.8 (arXiv 2605.16352).
- 이 체계에의 대응은 위 표 그대로이며, 두 논문 모두 **엣지 신뢰도를 수치로 쓰는 쪽**(θ, ω)이다 — 이 체계는 9.11절에 따라 수치 없이 조건·증거 기록으로 간다는 점에서 의도적으로 갈린다.
