---
from: hci
status: approved
targets: [inquiries/design-detail.md, ../agent-knowledge-system-notes.md, ../agentic-knowledge-base-structure.md, purpose-statement.md, ../purpose.md, ../rules.md, ../method.md, ../tools.md, ../competency-questions.md, ../open-questions.md, ontology/, kg/catalog-kg.ttl]
---

# 검토 — `design-detail.md`: 설계 노트 v3와 구조도 v3로 현 KB를 갱신하기

원문: [`inquiries/design-detail.md`](inquiries/design-detail.md) — *"agent-knowledge-system-notes.md,
agentic-knowledge-base-structure.md을 기반으로 현 지식베이스 업데이트해줘. 그리고 두 문서는
intent.md의 핵심이야."* (유저 지시이므로 유저 lane이 자리다. 원문은 옮기지 않고 인용한다.)

## 질문

두 문서는 **이 KB의 설계 원본이 다시 바뀌었다**는 뜻이다. 2026-09-01에 분해되어 제거되었던
설계 노트가 v3(2,789줄 — 분해 원본 대비 +819/−512줄)로 돌아왔고, 구조도는 purpose-statement의
v4를 "v1"로 놓고 그 위에 v2·v3 변경(부록 두 표)을 쌓았다. 결정할 것은 "반영할까"가 아니라
**"무엇을 어떤 순서로, 그리고 이미 내려진 결정과 어긋나는 곳을 어떻게"** 반영하는가다.

어려운 이유 셋:
1. **범위가 온톨로지·규칙·도구·문서·결정 전부**에 걸린다 — plane 7, level 재정의, KB 둘, 개체
   셋(리비전·작업 집합·실행 기록) 도입, 도구 6종 추가.
2. 결정 153개는 **노트 v1에서 분해된 것**이라 그 상당수가 v3와 어긋난다(예: d-0012
   scene·situation·scenario 3분리는 v3에서 폐기). 동결 참조로 둔 것을 어떻게 처리할지.
3. 이 채널에서 내려진 유저 결정 몇 개가 v3 노트와 **정면으로 다르다**(§충돌).

**"intent.md의 핵심"의 해석** — `intent.md`는 저장소에 없다. v3 설계가 `requirement` plane ×
functional을 사다리의 출발점으로 두었으므로, 두 문서가 곧 **이 저장소 자신의 KB에서 요구
층(의도)**이라는 뜻으로 읽었다. 그러면 결정 153개는 이 의도를 `refines`하는 abstract 이하가
되고, 하강 완주율(CQ19)이 이 저장소에도 적용된다. 이 읽기가 맞는지 확인이 필요하다(Q0).

## 이미 정해진 것 — 두 문서가 확정한 것 중 현 KB와 다른 것

### 구조 (골격)

| 항목 | 현 KB | 노트 v3 · 구조도 v3 | 영향 |
|---|---|---|---|
| plane | 6 | **7 — `requirement` 추가**(판정 = 이해관계자 합의). 순서 `requirement → decision → contract·schema → artifact → annotation → memory` (5.1·5.2) | `plane-ontology.ttl`에 `agt:RequirementChunk`, `chunk2kg` `PLANE_CLASS`, plane 순서 문서 |
| level의 뜻 | 추상화 사다리 (functional = 어휘의 서술적 사용) | **요구→산출물의 정제 높이.** functional = `requirement` 전용, executable = `artifact` 전용 (6.1) | `level-ontology.ttl` 정의문 5개 전부 |
| plane × level | 모든 plane이 5단 (d-0084 격자) | **거주표** — plane마다 정해진 level 구간만. 밖은 shape 위반 (6.4) | 새 shape. 현 153개(decision × concrete)는 거주표 안 ✓ |
| 지식 베이스 | 하나 | **둘 — 개발 KB / V&V KB.** 같은 골격, 저장·스코프·편집 주체 분리, `verifies`만 KB 횡단 (7.1·7.5) | 디렉토리 분리(별도 최상위 패키지), 카탈로그 스코프, `vv/` 온톨로지 모듈 |
| 시나리오 | 검증의 응용 개념, 어휘 없음 | **V&V KB의 `decision` plane 실체**, 5수준 (7.2·7.3) | 새 어휘 없음(실체만) — 프로파일 |
| scene · situation · scenario | d-0012 3분리, docs 전체가 situation 사용 | **폐기.** 리비전(정규화 해시) · **작업 집합 `agt:Workset`**(스코프 × level 창) · 실행 기록 `agt:Run` · `agt:Runbook` (0.5) | 어휘 4개 신설, d-0012 대체, `method.md` §8·`tools.md`·`AGENTS.md`의 "situation" 전부 개명 |
| 태그 | 없음 | **범주 9종**(행위자·조건·목적·결함 요인·출처·ODD 관계·환경·대상·level), 값은 온톨로지 개념 (0.5) | 어휘 신설 |
| ODD 동적 갈래 | 조건 3분류 | + **시간 제약 어휘**(선행·배타·시한) — 시간열 개체 제거의 보완 (0.4·0.5) | `condition` 모듈 확장 |
| 링크 타입 | trace 모듈 12타입 + LEDGER 족 셋 | 노트 표 + **채택 4: `allocates`·`depends-on`·`generates`·`conflicts-with`** (9.2). 후보/확정은 **클래스** `CandidateLink`/`ConfirmedLink` (9.4) | `allocates`·`generates` 없음. 우리 `dependsOn`은 추상 상위, 노트의 `depends-on`은 범용 의존 — 뜻 충돌. 후보/확정을 클래스로 할지 `linkState`로 할지 |
| 결정의 형태 | 한 항목에 결론+근거+대안 (hci 가정) | **결정 = 세 청크의 구성체** (4.7) | [`open-questions/decision-role-tags.md`](../open-questions/decision-role-tags.md)가 답을 얻음 → 선택지 C |
| 코드 항목의 단위 | 미결(D7) | **산문 = 파일, 코드 = 심볼** (4.9) | `chunk-definition-unification` D7 = (b)로 닫힘 |
| 온톨로지·ODD의 청크화 | 미결(D1~D6) | 온톨로지 모듈 = 개념 청크의 구성체, ODD = 속성 청크의 절 구성체 (4.7) | D1·D3 방향 확정. plane·level 배정값은 여전히 미정 |
| 온톨로지 검사 | validate 6검사(SHACL 중심) | **컴파일러 3계층** report / verify(SPARQL 안티패턴) / reason(OWL RL) + **용어 제안 워크플로**(ROBOT template) (2.5) | `validate.py`에 verify 계층(SPARQL) 신설, `term_propose` 도구 |
| 도구 | 검사 5 · 활용 6(미구현) | 검사 7(`odd_check`·`assume_check`·`term_propose` 추가) · 활용 8(`workset`·`propagate`·`revalidate` 추가, `labels`→`workset`) | `tools.md` 표 재작성 |
| 입력(Part X) | 문서 없음 | 구조도가 **`input`을 AKB 최상위 가지로 복원** — 15개 파라미터 (10.1) | `docs/input.md` 신설 |
| 커버리지 | 시나리오 커버리지 | **하강 완주율 · 상향 귀속률 · logical 공간 커버**(경계값 별도) (7.7) | `metrics` 명세, CQ19·20 |
| 경쟁 질문 | 우리 CQ-01~32 | 노트 CQ1~20 (번호·내용 다름) | 대응표 필요 |
| 트러스트 | OKF `generated`/`verified` (2026-09-07) | 2.12: 판정 이력을 head의 `trust`에 누적, 신뢰 등급이 `derives-from`·`sources`로 **전파**, `sources` 빈 청크 = 실패 | `verified` 목록이 곧 판정 이력이므로 대부분 이미 맞다. **신뢰 전파 verify 질의**는 없음 |
| 미해결 | 우리 11 열림 / 13 닫힘 | 25건 — 우리가 "닫았다"고 표시한 6·7·9·16·19·20·21·22·23이 **여전히 열려 있음**, 24·25 신규 | 인덱스 재동기화 |
| 카탈로그 | 역할 5 | 개발 프로파일 **9역할**, `design`이 T-Box·ODD 편집 권한, V&V가 V&V KB 쓰기 (10.2·7.5) | 이 저장소는 부분집합 사용 — 단 V&V KB 쓰기 주체가 필요 |
| 도입 순서 | roadmap이 methodology 순서로 재편 | **methodology(운용 순환)와 도입 순서(체계를 세우는 7단계)는 다른 것** (Part XIII, 구조도) | `roadmap.md`에 도입 7단계 복원, 현 위치 재산정 |

### 변하지 않은 것 (확인)

42줄·한 주제·라벨 인터페이스 · 구성체 = part-of, 같은 plane·level만, 7±2 · 지식 종류는
고유 용어("X 청크" 금지 — 구조도가 그대로 씀) · 행위자는 개체가 아니라 **태그** · 청크는
프로젝트를 넘지 않는다(11.7) · 어휘 폐쇄·표준어 우선 · 링크는 산출물 밖, 한 방향 · 구축이
기본, 복원은 예외 · 임베딩은 후보 추림만 · 상승은 자동화하지 않음.

## 현재 상태 — 실측

- 결정 153개 전부 `decision × concrete`, `status: stable`, 인용 링크 27, 가정 1, 사람 검토 0.
- 온톨로지 91개 용어(파일 22). `requirement`·`Workset`·`Run`·`Runbook`·태그·시간 제약·
  `allocates`·`generates`·`vv/` **없음**.
- `situation`이라는 말이 `docs/`·`AGENTS.md`·`.claude/`에 걸쳐 쓰이고 있다(v3에서 폐기된 용어).
- 결정 중 v3가 폐기·개정한 것(확인된 것만): d-0012(3분리), d-0084(전 plane 5단 격자),
  d-0005·d-0027·d-0046의 level 정의(functional = 어휘의 서술적 사용), d-0003·d-0125(plane 6·
  역할 권한), d-0010(링크 타입 표). **v1→v3 diff가 819줄 추가·512줄 삭제**라 이 목록은 부분이다.
- `docs/agent-knowledge-system-notes.md`가 저장소에 있으나 `docs/README.md` 색인에 없고, 노트
  2.12·2.5가 참조하는 "Part XIII"의 OKF 절은 노트 안에 없다(Part XIII = 도입 순서) — 노트
  자체의 끊긴 참조.

## 답이 가르는 것

### 이 채널의 유저 결정과 노트 v3가 어긋나는 곳 — 어느 쪽이 이기는가

| # | 유저 결정(채널) | 노트 v3 | hci 제안 |
|---|---|---|---|
| C1 | `status: stable` (OKF 변환, 2026-09-07 결정 13-2) | 4.11 `valid` 유지 | **채널 결정 유지** — 노트 4.11을 OKF 어휘로 고친다. 노트가 2.12에서 OKF `status`를 이미 인용한다 |
| C2 | 통합이 필요한 것만 구성체 (결정 1·9) | 4.7 "결정 = 세 청크의 구성체", "모든 지식은 구성체" | **노트 우선** — 결정 하나는 결론·근거·대안 세 항목의 구성체. 단 "통합이 필요한 것만"은 유지 가능: 결정은 통합이 *필요한* 경우다. 153개 분할 작업이 따른다 |
| C3 | plane 6, 격자 "모든 plane이 5단" (구조도 v4) | plane 7, 거주표 | **노트 우선** — v4는 v1으로 대체됨 |
| C4 | 스키마 편집 권한 "기존대로 developer" (결정 13-1) | 10.2 `design` 역할이 T-Box·ODD 편집 | **채널 결정 유지** — 이 저장소는 9역할의 부분집합을 쓰므로 developer가 겸한다. 카탈로그에 그 사실을 적는다 |
| C5 | 미해결 6·7·9·16·19·20·21·22·23 닫힘 (v4 근거) | 여전히 열림 | **노트 우선** — 닫은 근거(v4)가 대체되었으므로 다시 연다 |
| C6 | 트러스트 = OKF `generated`/`verified` | `trust` 필드에 판정 이력 누적 | **둘이 같다** — `verified`가 목록이므로 이력이다. 노트의 `trust`를 `verified`로 정정 |
| C7 | LEDGER 세 족(references·semanticallyDependsOn·relatedTo), `cites`·`usesConcept`·`coUpdatesWith` | 없음 — `depends-on`은 범용 의존 | **병합** — 노트 9.2가 `depends-on`을 "하위 타입의 상위"로 채택했으니 우리 `agt:dependsOn`이 그 자리다. 족 셋은 그 아래. `allocates`·`generates` 추가 |

### 반영 범위의 선택

- **A. 전면 재도출** — 노트 v3를 다시 분해해 결정 집합을 새로 만들고 옛 153개를 `supersedes`로
  잇는다. 비용 최대(하루·5 에이전트가 v1 때의 실측), 그러나 노트와 결정이 일치한다.
- **B. 델타 반영** — diff에 걸린 절만 새 결정으로 만들고(`supersedes`), 온톨로지·규칙·도구·
  문서를 v3로 고친다. 옛 결정 중 대체된 것은 `deprecated`. **권고.**
- **C. 문서·온톨로지만** — 결정 153개는 "v1 기준"으로 동결 표기만 하고 손대지 않는다.
  가장 싸지만 결정과 노트가 영구히 어긋난다 — CQ8("누가 무엇을 근거로")의 답이 낡는다.

## 선택지 — 순서 (B 기준)

| 순서 | 무엇 | 왜 먼저 | 게이트 |
|---|---|---|---|
| 0 | **Q0·C1~C7 결정** + `intent.md` 위치 | 뒤 전부가 종속 | — |
| 1 | **골격 어휘** — `RequirementChunk`, level 정의 5개 개정, 거주표 shape, `Workset`·`Run`·`Runbook`, 태그 범주, 시간 제약, `allocates`·`generates`, 후보/확정 표현 | 어휘 없이는 어떤 항목도 못 만든다 | `bazel test //...` |
| 2 | **규칙·문서** — purpose·methodology·rules·method·tools·roadmap(도입 7단계 복원)·competency-questions(대응표)·open-questions(재동기화) + `docs/input.md` 신설 + `situation`→작업 집합 개명 | 골격이 바뀌면 규칙 문서가 거짓이 된다 | 링크 검사 |
| 3 | **두 KB 분리** — 디렉토리·카탈로그 스코프·`vv/` 모듈 | 저장 분리는 어휘·규칙 뒤 | 카탈로그 정합성 |
| 4 | **결정 델타** — diff 절 → 새 결정, `supersedes`, 옛 것 `deprecated`. 결정 3분할(C2) 여기서 | 어휘·규칙이 정해진 뒤 | 게이트 + 고아율 |
| 5 | **검사 3계층** — `validate`에 SPARQL verify 계층(거주표·`sources` 빈 청크·신뢰 전파·기준 없는 `verifies`), `term_propose` | 규칙이 확정된 뒤 게이트화 | 음성 시험 |
| 6 | **이 저장소를 요구 층으로** — 두 문서를 `requirement` × functional 항목으로 등록, 결정이 `refines`. `intent.md` 생성 여부 | Q0에 종속 | 하강 완주율 |

각 단계 끝에 `bazel test //...` PASS와 실측 보고. 1단계만으로 이득이 없으면 멈춘다(노트 Part XIII).

### 유저가 정할 것

- **Q0** "두 문서 = 이 저장소 KB의 요구 층(functional)"이라는 해석이 맞는가? `intent.md`는
  새로 만드는 파일인가(두 문서를 가리키는 요구 문서), 아니면 두 문서 자체를 그렇게 부르는가?
- **C1~C7** 위 표의 hci 제안대로인가.
- **A/B/C** 반영 범위. hci 권고 **B**.
- 두 KB의 저장 분리 형태 — 같은 저장소의 별도 최상위 패키지(`kb/dev/`·`kb/vv/`) vs 별도 저장소.
  노트 7.5는 둘 다 허용. hci 권고: **같은 저장소, 별도 패키지** — 게이트 하나로 두 KB를 검사한다.

## 답
Q0: claude에서 추천하는 intent.md로 새로 작성
c1~c7: 제안대로
반영범위: A
저장 분리: 같은 저장소, 별도 패키지

---

## 재검토 (2026-09-10, 유저 답 수신 후)

**유저 답**: Q0 = Claude 권고안으로 `intent.md` 새로 작성 · C1~C7 = 제안대로 · 반영 범위 = **A(전면
재도출)** · 저장 분리 = 같은 저장소, 별도 패키지.

### 제 검토문의 오류 정정

1. **"우리가 닫은 미해결 9건이 노트에서 여전히 열림"은 과소 계산이다 — 13건이다.** 노트 XVI는
   옛 1~23을 하나도 지우지 않았다. 우리가 v4 근거로 닫은 것 중 노트에 남은 것: 4(구성체 가정)·
   6·7·9·11·12·16·18·19·20·21·22·23. 노트가 버린 것은 옛 24(프로파일 공유)·옛 25(42줄 손상)·역할
   긴장뿐이고, 새 24(decision concrete 중복)·25(변이 표본 크기)가 들어왔다. C5(노트 우선)에 따라
   **13건을 다시 연다.** `docs/open-questions.md`의 "닫힌 질문" 표는 3건만 남는다.
2. **"현 153개는 거주표 안 ✓"는 형식적으로만 참이다.** 각 항목이 결론·근거·대안을 한 몸에 담고
   있어서, C2(결정 = 세 청크)로 쪼개면 결론은 concrete, 근거·대안은 **logical**에 거주한다.
   즉 재도출 후 `decision` plane은 두 level에 걸치게 되고 그것이 정상이다.

### 답의 귀결 — A + C2가 뜻하는 규모

| | v1 분해(2026-09-01) | v3 재도출 예상 |
|---|---|---|
| 노트 | 2,476줄 | 2,789줄 |
| 결정 | 153 | 약 170~190 (`[확정]` 수 기준 추정 — 재도출 시 실측) |
| 청크 파일 | 153 (결정 = 파일 하나) | **약 500~570** (결정 = 결론·근거·대안 세 청크) + 구성체 170~190 |
| 링크 | 0 | `refines`(결정 → 요구), `supersedes`(새 → 옛 153), `cites` |
| 소요 | 하루, 에이전트 5개 병렬 | 병렬 없이는 여러 세션 |

두 가지가 따라온다.
- **IRI 체계** — 노트 0.7이 `[확정]`한 "uuid + 내용 해시"를 지금 도입하는 것이 가장 싸다.
  전부 새로 만드는 순간이라 옛 순번 IRI(`chunk-d0001`)와 공존시킬 이유가 없다. 옛 153개는
  `deprecated`로 남고 새 것이 `supersedes`로 가리킨다. → **Q1**
- **병렬 에이전트** — 지금 세션은 단독 실행이다. v1 분해가 5개 병렬로 하루였으니 단독이면
  여러 턴에 걸친다. 원하시면 분해 단계만 병렬로 돌린다. → **Q2**

### Q0 — `intent.md` 권고안

v3에서 사다리의 출발점은 `requirement` × functional이다. **이 저장소 자신의 KB에도 그 층이
있어야 하강 완주율(CQ19)이 성립한다.** 지금은 없다 — 결정 153개가 무엇을 `refines`하는지
말할 수 없는 이유다. `intent.md`가 그 층의 진입 문서다.

| | 권고 |
|---|---|
| 위치 | 저장소 루트 `intent.md` — README·AGENTS·STYLEGUIDE와 같은 층. 세션 시작 필독에 넣는다 |
| 성격 | **요구 층의 진입 문서(색인)**. 그래프 밖. 요구 항목 자체는 `kb/dev/requirement/`의 청크(functional, EARS) |
| 내용 | ① 궁극 목적 한 단락(구조도 v3 첫 줄 그대로) ② **이해관계자와 관심사** — 업체(분야 지식 축적), 프로젝트(ODD 안에서 시스템 생산·운용), 에이전트(좁은 컨텍스트에서 판단), 검증자(독립 판정) ③ 요구 목록 — 관심사별 구성체, 각 요구는 EARS 한 문장 + 출처 절 ④ 두 핵심 문서의 자리 — 노트 v3 = 요구의 **근거와 결정의 원천**, 구조도 v3 = **운용 지도** |
| 요구의 출처 | 노트 **Part I(왜 이 체계인가)·산출물 정의·한 줄 요약**, 구조도 **궁극 목적·대상 지식·순환**. `[확정]` 절은 요구가 아니라 결정의 원천이다 — 그래서 Parts II~XII는 재도출에서 `decision`으로 간다 |
| 예 | "에이전트가 200줄 컨텍스트 안에서 판단할 때, 체계는 그 판단에 필요한 지식을 라벨 목록으로 먼저 보여주어야 한다" (1.1·1.4) / "산출물이 바뀌면 체계는 전수조사 없이 무효가 된 상위 지식의 범위를 계산할 수 있어야 한다" (1.3) / "만든 주체와 판정 주체는 같은 KB를 쓸 수 없어야 한다" (7.1) |
| 링크 | 재도출된 결정이 요구를 `refines`. 요구는 두 문서를 `derives-from` |
| 크기 | 요구 20~30개 예상. 요구 하나 = 청크 하나(42줄) |

**따라서 순서가 바뀐다** — 요구가 결정보다 먼저 있어야 `refines`를 구축으로 만들 수 있다
(복원이 아니라). 재도출 전에 `intent.md`와 요구 청크를 먼저 만든다.

### 실행 순서 (A 확정판)

| 순서 | 무엇 | 산출 |
|---|---|---|
| 1 | **골격 어휘** — `RequirementChunk`·level 5 정의 개정·거주표 shape·`Workset`/`Run`/`Runbook`·태그 범주·시간 제약·`allocates`/`generates`·`CandidateLink`/`ConfirmedLink`(C7 병합)·IRI 체계(Q1) | `ontology/` 갱신, 게이트 PASS |
| 2 | **저장 구조** — `kb/dev/<plane>/`·`kb/vv/<plane>/` 패키지, `chunk2kg`·`extract_refs`가 두 KB를 읽음, 카탈로그 스코프(V&V 쓰기 주체) | BUILD 배선 |
| 3 | **`intent.md` + 요구 청크** — Part I·산출물 정의·구조도 궁극 목적에서 EARS 요구 20~30개 | `kb/dev/requirement/`, 요구 → 두 문서 `derives-from` |
| 4 | **결정 재도출** — 노트 v3 Parts 0~XII의 `[확정]`을 결정으로. 결정 = 결론(concrete)·근거·대안(logical) 세 청크 + 구성체. 각 결정이 요구를 `refines`, 옛 153을 `supersedes`. 절→항목 대응표(감사) 갱신 | `kb/dev/decision/`, 옛 `chunks/decision/`은 `deprecated` |
| 5 | **규칙·문서** — purpose·methodology·rules·method·tools·roadmap(도입 7단계 복원)·competency-questions(노트 CQ1~20 대응)·open-questions(13건 재개)·`docs/input.md` 신설·`situation`→작업 집합 | 링크 검사 |
| 6 | **검사 3계층** — SPARQL verify(거주표·`sources` 빈 청크·신뢰 전파·기준 없는 `verifies`), `term_propose` | 음성 시험 |

단계마다 `bazel test //...` PASS·실측을 보고하고, 1단계 뒤 이득이 없으면 멈춘다.

### 유저가 정할 것 (둘)

- **Q1** IRI를 노트 0.7의 "uuid + 내용 해시"로 지금 전환하는가? (권고: 예 — 전면 재도출과 같은 순간)
- **Q2** 4단계(재도출)를 병렬 에이전트로 돌리는가? (권고: 예 — v1 실측이 5개·하루)

### 사용자 피드백
Q1: 예
Q2: 예

## 반영 결과 (2026-09-10, orchestrator)

실행 순서 6단계 전부 완료. 최종 `bazel test //...` **7/7 PASS**.

| 단계 | 산출 (실측) |
|---|---|
| 1 골격 어휘 | `RequirementChunk` · level 재정의 · 상주표 shape · `state/`(Workset·Run·Runbook) · `tag/`(범주 9) · 시간 제약 3 · `allocates`/`generates` · `CandidateLink`/`ConfirmedLink` · `contentHash` — 모듈 파일 26 |
| 2 저장 구조 | `kb/dev/`·`kb/vv/` 패키지, chunk2kg가 uuid IRI·contentHash·refines/supersedes/구성체 생성 지원, 카탈로그에 V&V 편집 주체·C4 명시 |
| 3 요구 층 | `intent.md` + 요구 26건 (EARS, `kb/dev/requirement/`) |
| 4 결정 재도출 | **결정 145건 / 파일 358** (`kb/dev/decision/`, 6 에이전트 병렬 + 서두·Part I 직접분 5). 노트 유래 옛 결정 **126건 전부 deprecated** — 대체 없는 폐기 0. 잔류 27건은 harness 유래·d-0001 |
| 5 규칙·문서 | purpose · methodology · rules · method · ontology · tools · roadmap(도입 7단계) · competency-questions(CQ 대응표) · open-questions(25건 재동기화) · `input.md` 신설 · README/AGENTS/docs-README · 감사 §3 · situation→작업 집합 |
| 6 검사 3계층 | validate에 verify 계층(`tools/verify-queries/` 4질의) + `term_propose` 승인 큐 — 음성 시험 통과 |

재도출이 낳은 부산물 — **요구 층 공백 7건**(컨텍스트 예산, 명명 결정론, 입력 버전 관리,
문서 생성 원칙, 검증 수단의 신뢰도, 감사 자족성, 재현성), **노트 v3 내부 v1 잔재**(0.4
스코프 예시 plane, 절 번호 참조 몇 곳, 5.3 "현재 6개"), **동질성 긴장**(결정 구성체의
level 혼합) — 상세는 `docs/decomposition-audit.md` §3과 `docs/open-questions.md`.
