---
from: hci
status: open
targets: [inquiries/suggestion-bazel-okf-ontology.md, ../rules.md, ../tools.md, ../method.md, ../competency-questions.md, ../../AGENTS.md, https://agentic-knowledge-base.dev/id/chunk-d0003, https://agentic-knowledge-base.dev/id/chunk-d0024, https://agentic-knowledge-base.dev/id/chunk-d0049, https://agentic-knowledge-base.dev/id/chunk-d0054, https://agentic-knowledge-base.dev/id/chunk-d0077, https://agentic-knowledge-base.dev/id/chunk-d0082, https://agentic-knowledge-base.dev/id/chunk-d0088, https://agentic-knowledge-base.dev/id/chunk-d0125]
sources:
  - "Open Knowledge Format (OKF) v0.2 SPEC — GoogleCloudPlatform/knowledge-catalog (2026-06)"
---

# 제안 검토 — OKF · 온톨로지 · Bazel 세 층 구조

원문: [`inquiries/suggestion-bazel-okf-ontology.md`](inquiries/suggestion-bazel-okf-ontology.md)
(유저 제안이므로 유저 lane이 자리다 — 조사 lane은 hci가 타 에이전트에게 묻는 곳이다.
원문은 유저가 쓴 것이라 옮기지 않고 여기서 인용한다.)

## 질문

제안의 세 층(OKF 원본 / PROV-O + SHACL 온톨로지 / Bazel)은 **이 저장소가 이미 하고 있는
것과 거의 같다.** 그래서 결정할 것은 "이 구조를 채택할까"가 아니라 **"제안이 우리에게 없는
다섯 가지를 받을까, 어디까지 받을까"**다. 어려운 이유는 그중 둘이 기존 결정과 부딪히기
때문이다 — 프론트매터 어휘(OKF `status` vs 우리 `state`)와 클래스 모델(제안의 5클래스 vs
plane 6 × level 5).

**OKF는 실재하는 표준이다** — Google Cloud가 2026-06에 낸 v0.1, 현재 v0.2. 마크다운 +
YAML 프론트매터, `type`만 필수, 나머지는 선택이며 **소비자는 알 수 없는 키를 견뎌야 한다**
(conformance 요건). 지어낸 용어를 쓰지 않는다는 원칙(d-0024)이 여기 걸린다.

## 이미 정해진 것 — 제안의 대부분은 구현되어 있다

| 제안 | 이 저장소 | 상태 |
|---|---|---|
| 마크다운 + YAML 프론트매터 원본, git 버전 관리 | `chunks/<plane>/*.md` | **있음** |
| 프론트매터를 트리플로, 바뀐 것만 변환 | `tools/chunk2kg.py` + `//kg:chunks_kg` genrule + 입력 해시 캐시 | **있음** |
| Bazel test로 SHACL 검증, 실패 시 빌드 실패 | `//kg:gate_test`·`//ontology:gate_test`, shape 5개 | **있음** |
| TBox/ABox 분리 | `ontology/` vs `kg/` (d-0049) | **있음** |
| PROV-O 그대로 쓰기 | `wasDerivedFrom`·`generatedAtTime`·`atLocation` (STYLEGUIDE §5) | **있음** |
| "실제로 쿼리하는 관계만 살아남게 하라" | 경쟁 질문 30개 — 기여하지 않는 개념은 과설계 (d-0052) | **있음, 원칙으로** |
| "OWL 추론 쓰지 마라" | 추론은 OWL 2 RL로 제한 (d-0054). 실제로 추론기를 쓰지 않는다 | **사실상 일치** |
| "에이전트에게 스키마를 맡기지 마라" | ⚠ **어긋난다** — AGENTS 역할 표는 developer가 "온톨로지 개념 저작"을 한다 | **충돌** |
| 관계에 이름 붙이기(supersedes·dependsOn·contradicts) | `related/trace` 네 족 12타입 (2026-09-04) | **있음, 더 상세** |
| 증분·캐시·CI 강제 | Bazel 그대로 | **있음** |

## 현재 상태 — 제안이 가리키는 공백은 우리 미구현 목록과 겹친다

제안의 검증 5종을 우리 게이트와 대조하면:

| 제안의 검증 | 우리 상태 |
|---|---|
| 인용한 코드 타깃이 존재하는가 | **미구현** — 깨진 참조 검사([`tools.md` 게이트 밖](../tools.md#게이트-밖--규약으로-남은-것)) |
| 전제가 retracted인데 이 결정이 active인가 | **미구현** — 무효화 전파 (d-0088). 가정이 152/153에서 비어 있어 입력도 없다 |
| superseded 결정이 여전히 active 코드를 constrains 하는가 | **미구현** — 재판정 규칙 (d-0107). 어휘는 있고 링크 데이터가 0 |
| Decision에 Evidence를 인용하는 Rationale이 있는가 | **미해결** — 역할 태그 필수 여부가 미정([`open-questions/decision-role-tags.md`](../open-questions/decision-role-tags.md)). 실측 결론 153·근거 150 |
| `verified: human` 파일을 에이전트 커밋이 건드렸는가 | **어휘 자체가 없다** — 새것 |

**다섯 중 넷이 이미 "만들기만 하면 되는 것"으로 등록되어 있다.** 제안은 새 방향이 아니라
같은 목록을 다른 순서로 가리킨다 — 그래서 이 제안의 값은 **우선순위 근거**와 **다섯째
항목(트러스트 티어)**에 있다.

### OKF 프론트매터와 우리 프론트매터 대조

| OKF v0.2 | 우리 | 판정 |
|---|---|---|
| `type` (유일한 필수) | `plane` + `level` | 이름만 다름. `type` 추가로 준수 가능 |
| `title` · `description` | `label_ko` · `label_en` | 우리가 한/영 1:1로 더 강함 |
| `status: draft \| stable \| deprecated` | `state: draft \| valid \| suspect \| invalidated \| deprecated` | **동음 충돌** — 같은 이름, 다른 값 집합 |
| `generated: {by, at}` | `generated_at`만 | **`by`가 없다** — 누가 만들었는지 기록되지 않는다 |
| `verified: [{by, at}]`, `human:` 접두어가 트러스트 티어를 올린다 | **없음** | 새것 |
| `sources: [{resource, id, title, author, …}]` | `derived_from: [IRI]` | 우리가 더 좁음(IRI만) |
| 링크 = 평범한 마크다운 링크, 관계는 산문에 | 타입 있는 링크 12종 + 링크 개체 | **우리가 더 강함** — OKF가 못 하는 것을 제안도 인정 |
| 예약 파일명 `index.md` · `log.md` | 없음 | 회피만 하면 됨 |

**중요**: OKF는 "소비자가 알 수 없는 키를 견뎌야 한다"고 요구한다. 즉 `iri`·`plane`·
`level`·`assumes`를 그대로 두고 **`type` 하나만 더하면 우리 청크는 OKF 번들이 된다.**
호환 비용이 거의 없다.

## 답이 가르는 것

- **트러스트 티어를 받으면** — "유저 승인이 `valid` 전이의 조건"(d-0003)이 처음으로
  *기록*된다. 지금은 153개가 전부 `valid`인데 누가 승인했는지 그래프에 없다. 채널의
  `status: approved`가 유일한 승인 신호인데 그것은 그래프 밖이다. `verified: {by: human:…}`이
  그 둘을 잇는다. 나아가 "에이전트가 사람 검증 항목을 덮어썼는가"가 게이트가 된다 —
  AGENTS의 write plane 경계가 규약에서 기계 검사로 내려온다.
- **OKF를 준수하면** — 표준어 우선 원칙을 지키고, 외부 도구가 이 저장소를 읽을 수 있다.
  대신 `state`/`status` 동음을 정리해야 하고, 우리 필드가 "producer-defined key"로 남는다.
- **5클래스 고정을 받으면** — plane × level 격자(구조도 v4)를 버리는 것이 된다. 취지("아무도
  채우지 않는 칸을 만들지 마라")는 경쟁 질문이 이미 담당한다.
- **Bazel 라벨 앵커를 받으면** — 코드 계열 앵커가 경로에서 라벨로 바뀐다. 리팩터링에
  견디므로 [시간 정체성](../open-questions/temporal-identity.md)의 절반이 풀린다. 단 관리
  대상이 Bazel 프로젝트일 때만 성립하므로 **골격이 아니라 분야 프로파일**의 결정이다.

## 선택지

**A. 다섯 가지를 순서대로 받는다 (hci 권고)**
1. **트러스트 티어** — 프론트매터에 `generated: {by, at}` · `verified: [{by, at}]`를 OKF
   필드명 그대로 추가하고, `chunk2kg`가 PROV(`wasAttributedTo`)로 방출. 게이트 하나:
   *사람이 검증한 항목을 에이전트가 고쳤는데 재검증이 없으면 FAIL*. 이것이 다섯 중 유일하게
   새것이고, 우리 승인 경계의 구멍을 정확히 막는다.
2. **OKF 준수** — `type` 필드 추가, `state`→OKF와 겹치지 않게 유지(§선택지 D 참조),
   예약 파일명 회피. 문서에 "OKF v0.2 번들"임을 명시.
3. **`cites` 추출 + 깨진 참조 게이트** — 제안의 첫 검증 항목. 본문 인용 146회가 이미 있고
   어휘(`agt:cites`)도 있다. 가장 싸다.
4. **규칙 물질화** — `superseded → suspect`, `가정 위반 → invalidated` 전파를 SPARQL
   UPDATE로. 산출물은 `bazel-out`에만. d-0088의 구현 수단이 된다.
5. **조회 파이프라인** — Oxigraph를 빌드 산출물로 두고 질의를 MCP로 노출. **단 CONSTRUCT
   결과를 통째로 로드하지 않는다** — 스코프 필터와 예산 패킹을 그 위에 얹는다
   ([`dependency-graph-design.md`](dependency-graph-design.md) §4). 세션 시작 지시가 이미
   347줄이라 부분그래프를 그대로 넣으면 예산이 터진다.

**B. 트러스트 티어만 받고 나머지는 기존 순서대로** — 로드맵의 "다음 산출"을 바꾸지 않고,
제안 중 진짜 새것 하나만 흡수한다. 가장 보수적.

**C. 세 층 구조를 제안대로 다시 세운다** — 5클래스로 스키마를 고정하고 plane × level을
접는다. 구조도 v4와 결정 153개의 상당 부분을 개정해야 한다. **권고하지 않는다** — 제안이
경계하는 "과잉 설계"의 방어는 이미 경쟁 질문이 하고 있고, 5클래스는 개발 프로파일 하나의
어휘라 도메인 중립 골격을 대체할 수 없다.

**부속 결정 넷**
- **D. `state` vs OKF `status`** — (i) 우리 `state`를 유지하고 `status`는 쓰지 않는다(동음
  회피, 권고) (ii) OKF `status`로 갈아타고 `valid`·`suspect`·`invalidated`를 잃는다
  (iii) 둘 다 두고 사상 규칙을 적는다(이중 관리 위험).
- **E. TBox 편집 권한** — 제안은 "스키마는 사람만". AGENTS 표는 developer가 온톨로지 개념을
  저작한다. 좁힐 것인가? 좁히면 역할 표와 `kg/catalog-kg.ttl`을 같은 커밋에서 고쳐야 한다.
- **F. Gazelle** — 지금은 `glob`으로 충분하고 BUILD를 손으로 쓰지 않는다. **보류** 권고 —
  [개체 수준 분할](chunk-definition-unification.md)이 승인되어 파일이 수백 개가 되면 재검토.
- **G. Bazel 라벨 앵커** — 골격이 아니라 `profile/development`의 앵커 해석기로. 이 저장소는
  Bazel 프로젝트이므로 첫 프로파일의 좋은 시험 재료다.

## 답

**유저(2026-09-07): "A로 진행. 충돌 1은 기존에 하던 대로, 2는 OKF로 변환, 3은 기존 구조도대로."**

| 결정 | 반영 |
|---|---|
| **A** 다섯 단계 진행 | 아래 진행 상태 |
| 충돌 1 — 스키마 편집 권한 | **기존 유지** — developer가 온톨로지 개념을 저작한다. 부속 결정 E는 "좁히지 않는다"로 닫힘 |
| 충돌 2 — `state` vs `status` | **OKF로 변환** — 필드명 `status`, 값 `draft`/`stable`/`deprecated`(OKF) + `suspect`/`invalidated`(확장). `valid` → `stable` |
| 충돌 3 — 5클래스 모델 | **기각** — plane × level 격자 유지 (선택지 C 미채택) |

### 진행 상태 (2026-09-07)

| 단계 | 상태 | 산출 |
|---|---|---|
| ① 트러스트 티어 | **완료** | `ontology/related/trust/`(어휘 3) · `ontology/shapes/trust-shapes.ttl`(게이트 2) · 153개 항목에 `generated` 기록 |
| ② OKF 준수 | **완료** | `plane`→`type`, `state: valid`→`status: stable`, `generated_at`→`generated: {by, at}`. `chunks/`가 OKF v0.2 최소 준수 번들 |
| ③ 인용 추출 + 참조 무결성 | **완료** | `tools/extract_refs.py` · `//kg:references_kg` · `validate.py`의 `dangling` 검사. 인용 링크 27개 |
| ④ 규칙 물질화 | 미착수 | `superseded → suspect`, 가정 위반 전파를 SPARQL UPDATE로 |
| ⑤ 조회 파이프라인 | 미착수 | 임베디드 질의 + 도구 노출. **부분그래프를 통째로 로드하지 않는다** |

부속 결정: **D** = OKF로 변환(위) · **E** = 좁히지 않음(충돌 1) · **F** Gazelle = 보류 ·
**G** Bazel 라벨 앵커 = `profile/development`의 결정으로 미룸([`../roadmap.md`](../roadmap.md) 6번).

게이트는 음성 시험으로 확인했다 — 검증 뒤 수정, `generated` 누락, 없는 항목 인용 셋 다 거부한다.
