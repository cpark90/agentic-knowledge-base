---
from: user            # 유저 구술을 hci가 옮겨 적음 — 원문은 §1·§2·§3 그대로
status: open
targets: [../purpose.md, ../methodology.md, ../ontology.md, ../rules.md, ../method.md, ../tools.md, ../roadmap.md]
---

# 목적 진술과 구조도 — 유저 원문과 결정 원장

**이 문서가 문서 체계의 기준이다.** §3 구조도 v4가 최종 규범이며, `docs/`의 문서들이 그
가지를 하나씩 맡는다. §1~§3은 유저가 쓴 원문이고 손대지 않는다.

*hci가 쓴 중간 산출(v1 대응표·v2 구조표·v3 검토·v3.1 정리본)은 v4로 대체되어 2026-09-04에
제거했다 — 그 내용은 `docs/`의 각 문서로 옮겨졌고, 원문은 git 이력에 있다.*

## 1. 원문 (2026-09-03)

- 내가 하고자하는게 무엇인가?
    - 각 산출물을 개선하는 것
    - agent가 지식을 활용하기 위한 보조 도구
        - 지식간 대부분의 연결에 대한 가능성이 살아있는채로 진행
        - complex context coupling에 대한 방지
        - 현장에 특화된 지식의 반영
    - agent 성능의 개선
        - 서로 다른 역할의 에이전트
        - 서로 다른 역할의 에이전트가 한 주제에 대한 처리를 주고 받는것
- Agentic knowledge base
    - methodology
    - result
        - ontology
        - tools
        - method
            - rules
            - 각 주제에 따른 다른 plane으로 정보를 관리.
            - 다른 plane들에 있는 내용이 traceability를 통해 인터페이스를 기준으로 mapping되어 있음.
            - knowledge graph
                - ODD
                - abstract, logical, concrete
            - chunk
                - 42 lines

### 확인 질문에 대한 답
(2026-09-04 유저 구술, hci 기록) 행위자는 없어도 됨 → §5의 행위자 층 제거, §5.1 2번 철회.

Q1. 맞다
Q2. 판정방식으로 나뉘는 것이 맞음
Q3. 기준축(axis)라는 의미
Q4. 의도가 아님

p.s. 제시한 구조표는 아직 미완이고 계속해서 내용을 추가하고 정리중임. 이 작업을 도와달라는 의미임. 이 프로젝트를 통해 만드는 대상에 대한 궁극적인 목적부터 정리해가고 싶음. 대략적으로는 특정분야에서 사업을 수행하는 업체가 특정 분야에 대한 온톨로지를 구축하고, 프로젝트를 수행할 때 ODD를 정하고 프로젝트 수행을 위한 지식을 기반으로한 시스템과 시스템에 대한 지식을 각 주제에 맞게 plane을 나누고 level에 따라서 정리하는 것임.

## 2. 구조도 v3 (유저, 2026-09-03)
- 궁극 목적
    - 특정 분야에서 사업을 수행하는 업체가, 그 분야의 지식을 에이전트가 활용할 수 있는 형태로 축적하고, 프로젝트마다 그 지식 위에서 시스템을 만들고 운용.
    - 대상 지식
        - 시스템을 만들기 위한 지식
            - 의도
            - 결정
            - 계약
            - 스키마
        - 시스템에 대한 지식
            - 구현
            - 관측
            - 논평
            - 기억
            - 교훈
- Agentic knowledge base
    - methodology
    - result
        - ontology: 지식의 골격 및 뼈대
        - tools: ontology 및 method, rules를 수행 및 관리하기 위한 도구
            - 검사: validate · chunk_lint · chunk2kg · canonicalize
            - 활용: situation/labels · link · query · impact · project · metrics,
        - rules: 지식의 모델링을 위한 규칙
            - chunk
                - 42 lines, 온톨로지 정의대로 (chunk-definition-unification)
                - 포맷이 아니라 구조 규율 — 온톨로지·ODD·space·kg에도 적용. 지식 종류(조건·개념·후보·결정·가정·관측…)
            - 구성체
                - 지식을 모델링하기 위해 chunk가 구조적으로 연결된 집합
                - chunk간 연결에는 가능성을 포함
            - plane
                - 판정 방식으로 나뉜 주제
            - traceability
                - 각 주제의 인터페이스를 기준축으로 plane 간 항목을 mapping
            - knowledge graph
                - ODD: 프로젝트당 하나, 스코프·가정·시나리오의 분모
                - level: functional · abstract · logical · concrete · executable
        - method: 지식을 모델링하기 위한 구체적인 방법

## 3. 구조도 v4 (유저, 2026-09-04) — 최종 기준
- 궁극 목적
    - 특정 분야에서 사업을 수행하는 업체가, 그 분야의 지식을 에이전트가 활용할 수 있는 형태로 축적하고, 프로젝트마다 그 지식 위에서 시스템을 만들고 운용.
    - 대상 지식
        - 시스템을 만들기 위한 지식 (사다리 하강의 산출)
            - 의도: ODD, functional - 온톨로지 개념의 서술적 사용
            - 결정: decision plane. 결론·근거·대안
            - 계약: `contract` plane. 인터페이스
            - 스키마: `schema` plane
            - 경쟁 질문: 온톨로지가 답해야 하는 질문 목록 = 요구사항이자 완료 판정
        - 시스템에 대한 지식 (사다리 상승의 입력)
            - 구현: artifact plane, executable 수준
            - 관측: 실행 기록. concrete 전용, append-only
            - 논평: annotation plane. 판정, 리뷰, 설명
            - 기억: memory plane. 단기, 첫 실행 시 한 번에 읽음
            - 교훈: 기억·관측에서 승격된 것. 결정 또는 규칙이 됨.
            - 순환: 만들기 위한 지식 → 시스템 → 시스템에 대한 지식 → 교훈 → 만들기 위한 지식
- Agentic knowledge base
    - methodology: 지식을 축적·운용하는 전체 순서와 그 이유
        - 프로파일 구축 → 프로젝트 ODD 작성 → 하강(저작) → 조회 → 연결 → 갱신 → 투영 → 상승 → (교훈이 다시 프로파일·ODD·결정으로)
        - 각 단계의 완료 판정과 다음 단계의 전제 (예: ODD 없이는 스코프·가정을 만들 수 없다)
    - result
        - ontology: 지식의 골격 및 뼈대
            - 골격: 분야 무관. plane·level·조건·가정·역할
            - 분야 프로파일: 골격을 확장만 하는 모듈 `profile/<분야>`. 각 plane의 실체·판정 도구·조건 어휘·결함 유형
        - tools: ontology 및 method, rules를 수행 및 관리하기 위한 도구
            - 검사 (rules의 기계 형태): validate · chunk_lint · chunk2kg · canonicalize
            - 활용 (method의 기계 형태): situation/labels · link · query · impact · project · metrics
        - rules: 지식의 모델링을 위한 규칙
            - chunk
                - 42 lines
                - 자립적 최소 지식 단위.
                - 포맷이 아니라 구조 규율: 온톨로지·ODD·space·kg에도 적용. 지식 종류(조건·개념·후보·결정·가정·관측…)는 고유 용어
                - 한 chunk = 한 plane · 한 level · 한 주제 · 한 파일. 상태 기계 draft/valid/suspect/invalidated/deprecated
            - 구성체
                - chunk의 part-of 묶음. 같은 plane·level, 순서(필요할 때만)
                - chunk와 함께 지식을 실질적으로 모델링함
            - plane
                - 판정 방식으로 나뉜 종류.
                - ex) decision, contract/schema, artifact, annotation, memory, design specification, 주석 / 리뷰 코멘트, 설계 결정 / 아키텍처 문서, 데이터 프로토콜 / 스키마, 인터페이스 / 타입 시그니처, 소스코드, 에이전트 작업 메모리 등
            - traceability
                - 각 종류의 인터페이스를 기준축으로 plane 간 항목을 mapping.
            - knowledge graph
                - ODD: 프로젝트당 하나, 스코프·가정·시나리오의 분모
                - level: functional · abstract · logical · concrete · executable
                - 담는 개체: node head(생성) · 구성체 · 가정 · 조건 · 역할·스코프(입력)
                - 가정: 모든 node(chunk)는 ODD 조건 위의 가정 위에 선다. ODD에 없는 조건은 참조 불가
                - 어휘 폐쇄: 데이터의 술어는 온톨로지 안에서만. 표준어 우선, 지어낸 용어 금지
        - method: 지식을 모델링하기 위한 구체적인 방법
            - 프로파일 구축: 골격 클래스의 하위 클래스·shape 추가 절차.
            - ODD 작성: 식별 → 분류 → 정량화 → 제외 검토 → 검증
            - node(chunk) 저작: plane·level 배정 → 파일 → 가정 → (필요하면) 구성체 → 게이트. 분할·병합 신호
            - 하강 전이: functional → abstract → logical → concrete → executable
            - 후보 관리: 변수·후보·제약(-space)
            - 연결
            - 갱신: 가정 판정 → 무효화 전파 8단계 → 재판정 경계
            - 조회: 스코프 → 라벨 목록 → 펼치기 → situation
            - 투영: tangle·weave·문서·매트릭스는 저장하지 않고 질의
            - 상승: 관측 → 도메인 → 변수 → 개념. 트리거는 초기에 사람 지정. 교훈 승격
            - 검증: 시나리오·합격 기준·환경
            - 영향 분석: 변경 전에 의존 집합·승인 필요 수 산출

## 4. 유저 결정 원장 (이 채널의 결정 기록 — 2026-09-02~04)

문서·구현이 이 결정들을 따른다. 반영 위치를 함께 적는다.

| # | 결정 | 반영 |
|---|---|---|
| 1 | ontology·odd·space·kg·functional 항목도 청크·구성체 형태. **통합이 필요한 것만 통합**하고 나머지는 개별 운영 | [`../rules.md` §1·§2](../rules.md) |
| 2 | **chunk는 온톨로지가 말하는 의미**로 사용한다 | [`../rules.md` §1](../rules.md#1-chunk--자립적-최소-지식-단위) · `chunk-definition-unification.md` |
| 3 | 본래 목적 = 온톨로지 + 활용 방법론 + 도구. 원래 목적으로 정리한다 | [`../purpose.md`](../purpose.md) · [`../roadmap.md`](../roadmap.md) |
| 4 | 궁극 목적(§1 p.s.) — 분야 업체가 분야 온톨로지를 구축, 프로젝트마다 ODD, 지식을 plane·level로 정리 | [`../purpose.md`](../purpose.md) |
| 5 | methodology = 전체 절차 / method = 구체적 방법 / rules = 구조 규칙. plane은 판정 방식. 인터페이스 = 기준축. level 5단 유지 | [`../methodology.md`](../methodology.md) · [`../method.md`](../method.md) · [`../rules.md`](../rules.md) |
| 6 | **행위자 층은 두지 않는다** — 분야는 프로파일 층, 프로젝트는 ODD 단위 | [`../purpose.md`](../purpose.md) |
| 7 | chunk는 포맷이 아니라 구조 규율(온톨로지에도 적용). **지식의 종류는 고유 용어**로 부른다 | [`../rules.md` §1](../rules.md#1-chunk--자립적-최소-지식-단위) · `AGENTS.md` 황금률 5 · `STYLEGUIDE.md` §0 |
| 8 | LEDGER·LARGER를 참고한 추적성 설계 | `dependency-graph-design.md` (승인 대기) |
| 9 | 구성체 = part-of 묶음 / 골격·프로파일 두 층 / 교훈은 순환 고리 / plane은 "종류" / 프로파일 구축 절차는 다음 산출 | [`../rules.md`](../rules.md) · [`../ontology.md`](../ontology.md) · [`../purpose.md`](../purpose.md) · [`../method.md` §1](../method.md#1-프로파일-구축) |
| 10 | **구조도 v4가 최종 기준** (§구조도 v4) | 문서 체계 전체 |
| 11 | 유저 판단 요청 항목은 **다섯 절**로 쓴다 | `AGENTS.md` 소통 규칙 · `STYLEGUIDE.md` §8 · [`../open-questions.md`](../open-questions.md) |
| 12 | 구조도 v4에 따라 모든 문서를 제거·수정한다 (2026-09-04) | 이 재편 |
| 13 | OKF·온톨로지·Bazel 세 층 제안을 **A(다섯 단계)로 진행**한다 (2026-09-07) | `suggestion-okf-three-layer.md` |
| 13-1 | 스키마 편집 권한은 **기존대로** — developer가 온톨로지 개념을 저작한다 | `AGENTS.md` 역할 표 (변경 없음) |
| 13-2 | `state` vs OKF `status` 충돌은 **OKF로 변환** — 필드·값 어휘를 OKF에 맞추고 무효화 확장 둘을 더한다 | [`../rules.md` §1](../rules.md#1-chunk--자립적-최소-지식-단위) |
| 13-3 | 제안의 5클래스 모델은 **기각** — plane × level 격자를 유지한다 | 구조도 v4 그대로 |
| 14 | 설계 노트 v3(`docs/agent-knowledge-system-notes.md`)와 구조도 v3(`docs/agentic-knowledge-base-structure.md`)로 KB를 갱신한다. 두 문서가 "INTENT.md의 핵심" (2026-09-10) | `design-detail-review.md` |
| 14-1 | 반영 범위 **A(전면 재도출)**, C1~C7 hci 제안대로, 저장 분리는 같은 저장소 별도 패키지, `INTENT.md`는 권고안으로 신규 작성 (2026-09-10) | **완료** (감사 §3): 요구 26·결정 145·옛 126 deprecated |
| 15 | 노트 v4(3,361줄)·구조도 v4로 대규모 개편 — 이를 기반으로 프로젝트를 완전히 개선한다 (2026-09-10 17:32) | `notes-v4-review.md` — Q1·Q2·Q4~Q7 대기 |
| 16 | 노트 v5(3,470줄)·구조도 v5로 재개편 — 조건부 링크·증거 장부(9.11), 불일치 귀속(8.4), 선제적 V&V(8.27), 기호 진단(12.12) (2026-09-10 19:00) | `notes-v5-review.md` |
| 16-1 | v4·v5 검토의 Q1~Q11 **전부 권고대로** (2026-09-10) | `notes-v5-review.md` 진행 표 — 0·1·2·3·3′ 완료, 4~8 진행 중 |
| 17 | 1단계 통과 조건의 재정의 — "토큰 감소"가 아니라 **의미를 보존하면서 예산(제한) 이내** (2026-09-10) | `stage1-pass-measurement.md` 재정의 절 |
| 18 | 단계별 통과 조건은 양이 아니라 **의미 보존 · 가상화 단계에 따른 구체화 · 유기적 연결** 세 축으로 (2026-09-10) | `stage-pass-conditions.md` — **채택**, 노트 14.1 정정 |
| 19 | 전체 문서·에이전트 용어를 표준 용어로 정규화 (2026-09-10) | `terminology-normalization.md` — **표대로 적용**, `docs/glossary.md` |
| 20 | 진행 검토 + 외부 조사로 세부 보충 (2026-09-11) — OKF `sources` 객체화·ODC 한정자 3·PyYAML 정책 정정, 참조 표준 상세 | `external-review-2026-09-11.md` — §3 둘 다 진행(OpenODD 정합·PyYAML 잠금) |
| 21 | 작업 집합 정의에 **앵커 이웃** — 스코프 × 수준 창 × 앵커 이웃 (2026-09-11) | 노트 0.5·11.3·14.1 정정, `agt:anchor`, `p0-workset-anchor-neighbourhood`, metrics 앵커 비율 |
| 22 | 의존성·연결성을 Bazel로 — B안 + 링크 deps + 가시성 + rules (2026-09-11 반영 1~6단계 완료) | `bazel-dependency-review.md` 진행 기록 |
| 23 | 3단계 착수 — frontmatter 링크 = `agt:Link` + 구축 기록 증거, `handoff`(읽기 집합 → sources), metrics 3단계 대리; 라벨 대표성 실험 프로토콜 제안 (2026-09-11) | `label-representativeness-protocol.md` — 답 대기 |
| 24 | 채널 refresh — 인수·반영이 끝난 항목 제거 (2026-09-11): `handoff-to-orchestrator-2026-09-11` · `stage3-link-construction` · `consistency-review-2026-09-11` · `hci-generated-chunks-2026-09-11.txt`. 기록은 git 이력(546dfb8·a522f2e)과 지식 산출물 | 채널 규약 refresh |

**아직 유저 답을 기다리는 것**: `dependency-graph-design.md`의 (a)~(j),
`chunk-definition-unification.md`(반영 완료로 제거 — git 이력)의 D1~D9(온톨로지·ODD 항목의 plane·level 배정).

> 결정 로그가 인용하는 채널 항목 중 반영 완료로 제거된 것(`chunk-definition-unification.md`·`suggestion-okf-three-layer.md`·`notes-v4-review.md`·`terminology-normalization.md`)은 git 이력에서 본다.
