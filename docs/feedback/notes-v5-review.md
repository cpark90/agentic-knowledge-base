---
from: hci
status: open
targets: [notes-v4-review.md, ../agent-knowledge-system-notes.md, ../agentic-knowledge-base-structure.md, ontology/related/trace/, ontology/related/assumption/, ontology/related/scope/, ../tools.md, ../rules.md, ../method.md, ../open-questions.md]
---

# 검토 — 노트 v5·구조도 v5 (v4 검토의 부록)

유저(2026-09-10 19:00): 두 문서를 **다시** 대규모 개편했고 이를 기반으로 완전히 개선하려 한다.
**v4 검토(`notes-v4-review.md`)의 발견과 질문 Q1~Q7은 전부 그대로 유효하다** — v4의 답이 아직
없고, v5는 v4 위에 얹힌 델타다. 이 문서는 델타만 다루고, 마지막에 두 검토의 결정을 한 표로 합친다.

## 질문

v5의 순증은 +109줄(노트 3,361 → 3,470)·+7줄(구조도)이고 **절 번호 재배치가 없다** — 8.27과
9.11이 끝에 붙었을 뿐이다. 그래서 v4 검토의 "번호 동기화"가 그대로 적용된다. 델타의 실질은
하나의 새 메커니즘과 세 개의 V&V 절차다:

- **9.11 조건부 링크와 증거 장부** — 링크의 가능성을 **조건**(`when` CEL)과 **증거**(종류 × 극성 ±)
  두 축으로 구조화. 수치 없음. 상태는 저장값이 아니라 `when` 평가 결과. `assumes`·스코프
  conditional·링크 조건이 **한 메커니즘**. verifier 결과가 개발 KB `satisfies` 후보의 장부에 ±로
  흘러가는 것이 두 KB 사이의 유일한 증거 경로. 언어모델은 제안·선호만.
- **8.4 불일치의 귀속** — verifier 실패의 귀속(산출물 / 지식 / 둘 다)은 자동이 아니라 **결정**이며,
  V&V `decision`의 **지도 청크**(귀속·조치 / 진단 / 배제된 귀속)로 남긴다.
- **8.27 선제적 V&V** — 개발이 안 바뀌어도 ODD 경계 근접·커버리지 공백·외부 지식 변화·증거 노화가
  V&V를 촉발. 산출은 전부 `origin:observed` 후보. 적응형 실행기는 `[안]`.
- **12.12 기호 진단 도구** — 불만족 핵·보간·최약 전제조건·명세 추론. **보간의 공통 어휘 = 온톨로지**
  이므로 설명이 어휘로 안 써지면 그 자체가 어휘 결손 신호.
- 미해결 +2 — 29(장부 확정 규칙: 실행(+) 몇 건이면 구축 없이 확정 가능한가), 30(`when` 평가 비용).
- 구조도: 도구 `diagnose`·`guide`·`proactive_vv` 추가, rules 골격에 "후보의 구조", V&V rules에
  귀속·장부, `space_check`에 `when` 평가·장부 규칙.

어려운 이유는 9.11이 **지난주에 만든 trace 모듈의 모델을 바꾼다**는 것이다.

## 이미 정해진 것 — 현 구현과 어긋나는 곳

| # | 현 구현 (2026-09-04·09-10) | v5 | 처리 |
|---|---|---|---|
| T1 | `agt:confidence` — LARGER ω ∈ [0,1], 근거 종류에서 파생 | **"수치가 없다."** 지지 증거의 종류 서열이 기본 선호 | `confidence` **폐기**(`deprecated`, `replacedBy` 없음). 선호는 장부에서 파생 |
| T2 | `agt:linkState` 저장값(candidate/confirmed/suspect/invalid) | 상태 = `when` 평가 결과 + 장부 규칙의 결과. 10.10은 여전히 저장값으로 적음 | 값 어휘는 유지(10.10과 일치), **파생 규칙**을 verify 계층에 둔다. 노트 10.10을 9.11에 맞춰 정밀화 |
| T3 | `agt:evidenceKind` 하나(단일 근거) | **증거 장부** — 항목 목록 (종류, 참조, 극성 ±). 종류 = 10.8 다섯 + 실행 + proposal | 장부 항목을 개체로(`agt:Evidence`: kind·ref·polarity·시각). `evidenceKind`는 항목의 속성으로 이동 |
| T4 | 근거 종류에 `counterfactualTest`(LEDGER 반사실 검사) 포함 | 10.8·9.11에 없음 — 구축·동시 편집·공동 커버·임베딩·세션·실행·proposal | 반사실 검사는 언어모델 제안의 한 방식 → `proposal`로 흡수, 별도 종류 폐기 |
| T5 | `assumes`(가정 모듈)·`conditionalRule`(스코프, 문자열) | 셋 다 `when`의 특수형 | `agt:when`(CEL 문자열) 신설. `assumes ⊑`… 는 속성이 아니라 "가정 참일 때"의 `when` 생성 규칙 — 어휘는 유지하되 정의문에 관계 명시. `conditionalRule` → CEL로 형식 전환 |
| T6 | V&V→개발 경로 = `verifies` 링크뿐 | + verifier 결과가 개발 KB `satisfies` 후보 장부에 ± | 장부 항목의 `ref`가 실행 기록을 가리키면 됨 — 새 링크 타입 불필요 ✓ |
| T7 | 도구 목록에 `diagnose`·`guide`·`proactive_vv` 없음 | 있음 | `tools.md` V&V 층에 추가 (도입 7단계) |
| T8 | 노트 10.10 "근거 = `prov:wasDerivedFrom`" | 9.11 장부(극성 있음) | 노트 내부 불일치 — 10.10 정밀화 필요 (유저 편집 대상) |
| T9 | v4 검토 S9·S13 (E.2 `trust`·`valid`, 예약 파일명) | v5에서 **그대로** | Q4 유지 |
| T10 | v4 검토 S1(절 번호 213회)·S2(대안 77건) | v5에서 **그대로** | v4 계획 1·2단계 유지 |

**좋은 소식**: `agt:CandidateLink`·`agt:ConfirmedLink`(v3 재도출이 추가)와 `agt:Link`의 양 끝·타입
속성은 9.11과 맞는다. 바꾸는 것은 **수치 하나를 빼고 장부 하나를 넣는 것**이다.

## 현재 상태 — 개편의 속도와 재도출의 비용

오늘 하루 노트가 세 번 바뀌었다(v3 16:30 기준 재도출 완료 → v4 17:32 → v5 19:00). 노트는
**git에 추적되지 않아** v3·v4 원문이 없고, 이번 검토는 이전 검토문의 절 목록으로 대조했다.
이제부터는 hci가 검토 시점마다 스냅샷을 뜬다(`scratchpad/notes-v5-1900.md`). 그러나 근본 해결은
노트 자신의 규칙이다 — **0.5절 "리비전 = 커밋"**. 노트를 커밋하면 (i) v_n → v_{n+1} diff가 공짜고
(ii) 재도출이 "어느 리비전 기준인가"를 해시로 말할 수 있으며 (iii) 결정의 `derived_from`이 문서
IRI가 아니라 **리비전**을 가리킬 수 있다. 커밋은 inspection·유저 권한이라 hci가 하지 않는다 → Q11.

## 답이 가르는 것 — 결정 통합표 (v4 Q1~Q7 + v5 Q8~Q11)

| # | 결정 | hci 권고 |
|---|---|---|
| Q1 | 결정 청크 분할 — 역할 3청크 유지 + abstract 변수 청크는 `-space` 있을 때만 (a) vs 수준 3청크 (b) | **(a)** |
| Q2 | `serves` vs `refines`(→요구) | `agt:serves ⊑ agt:refines`, 치역 `RequirementChunk` |
| Q4 | 부록 E.2 `valid`·`trust`·예약 파일명 vs 09-07·09-10 결정 | **(i)** 결정 유지 — 노트 E.2·4.11·10.10을 `stable`·`verified`로 고치고 `index.md`·`log.md`는 생성물로만 |
| Q5 | 0.4 스코프 예시의 v1 plane 이름 | v4 plane으로 고침 |
| Q6 | 부록 E 채택 순서 | (a) OKF 필드 정렬 지금 → (b) `kb/{ontology,odd}` + OpenODD → (c) Bazel plane 규칙은 도입 3단계 → (d) CEL·LinkML·OSC는 5·7단계 |
| Q7 | 도입 1단계 통과 조건(토큰 감소·고아율 < 10%) 먼저 측정 | 예 |
| **Q8** | trace 모듈 개정 시점 — `confidence` 폐기·`agt:Evidence` 장부·`agt:when` 신설을 **지금**(어휘만, 데이터 0) vs 도입 3단계(링크 구축)와 함께 | **지금 어휘만** — 데이터가 0이라 가장 싸고, CQ-13~20의 질의가 장부 형태로 미리 고정된다 |
| **Q9** | `assumes`·스코프 `conditionalRule`을 `when`으로 통일하는 어휘 변경 시점 | 어휘 정의문 정밀화는 지금, `conditionalRule` CEL 전환은 5단계(CEL 도입)와 함께 |
| **Q10** | `counterfactualTest` 근거 종류 | 폐기 → `proposal`로 흡수 (9.11 "언어모델의 자리") |
| **Q11** | 노트·구조도를 **git에 추적**하고 개편마다 커밋 — 재도출·검토의 기준을 리비전 해시로 | 예 (inspection 또는 유저가 커밋) |

## 선택지 — 순서 (v4 계획에 v5를 끼움)

| 순서 | 무엇 | v4 계획 대비 |
|---|---|---|
| 0 | Q1~Q11 결정 · **노트 커밋(Q11)** — 이후 모든 단계가 그 리비전을 가리킨다 | Q8~Q11 추가 |
| 1 | 번호·수치 동기화, 미해결 26~**30**, roadmap 8단계 + 14.1 | 미해결 +2 |
| 2 | 대안 청크 77건 + Q1 + `serves` | 동일 |
| 3 | v4·**v5** 델타 재도출 — Part VII·8.19~**8.27**·6.7·9.10·**9.11**·**8.4 귀속**·12.3·**12.12 기호 진단**·14.1·부록 B·E → 결정 약 50~70건 | +9.11·8.4·8.27·12.12 |
| 3′ | **trace 모듈 개정**(Q8·Q10) — `confidence` 폐기, `agt:Evidence`(kind·ref·polarity), `agt:when`, 장부 규칙 4종을 verify 질의로 | **신설** |
| 4~8 | E(a) OKF 정렬 → E(b) 저장 구조·OpenODD → 문서 세 층 → 1단계 측정 → E(c)(d) | 동일. `tools.md`에 `diagnose`·`guide`·`proactive_vv` |

## 답
**유저(2026-09-10): "권고대로 진행"** — Q1(a) · Q2 `serves ⊑ refines` · Q4(i) 결정 유지·노트 정정 ·
Q5 v4 plane으로 · Q6 (a)→(b)→(c)→(d) · Q7 예 · Q8 지금 어휘만 · Q9 정의문은 지금, CEL은 5단계 ·
Q10 `counterfactualTest` 폐기 · Q11 노트 커밋(inspection/유저).

진행 기록은 아래에 추가된다.

### 진행 (2026-09-10)

| 단계 | 상태 | 산출 |
|---|---|---|
| 0 답 기록 | 완료 | 결정 원장 16-1 |
| 1 번호·수치 동기화 | **완료** | 절 인용 69건·Part 참조 19건 v3→v5, 디렉토리 63개 `p8`~`p13`, intent·README·감사 갱신, 미해결 26~30, roadmap 8단계 + 14.1 통과 조건(1단계 **미통과** 표기) |
| 3′ trace 개정 (Q8·Q10·Q2·Q9) | **완료** | `confidence`·`counterfactualTest` deprecated, `agt:when`, `ledger-ontology.ttl`(`Evidence`·`hasEvidence`·`evidenceKind`·`evidenceRef`·`polarity`), `runResult`·`proposal` 종류, `agt:serves ⊑ refines`, `assumes`·`conditionalRule` 정의문. verify 질의 2개(장부 규칙) |
| Q4(i)·Q5 노트 정정 | **완료** | 4.11 `valid`→`stable`, E.2 `status`·`verified` 행, 2.12·8.20·부록 C `trust`→`verified`, 미해결 28 해소 표기, 10.10을 9.11과 정합, 0.4·3.4 스코프 예시 plane 이름 v4로. 구조도 2곳 |
| 2 대안 청크 77건 | **완료** | 145/145. 노트가 대비한 안은 그 내용으로, 열거하지 않은 것은 "대안 없음 — 후보가 하나였다는 사실" (7.4절) |
| 3 v4·v5 델타 재도출 | **완료** | 결정 **37건**(`[확정]` 79문장 → Part VII 12 · VIII 9 · IX 6 · 6.7 1 · 12 2 · 14.1 1 · 부록 E 6) + 요구 **7건**(감사 §3 공백: 컨텍스트 예산·명명 결정론·입력 버전·문서 생성·검증 수단 신뢰도·감사 자족성·재현성). 결정 182 · 요구 33. 게이트 7/7 |
| 4 E(a) OKF 필드 정렬 | **완료** | frontmatter 키 `iri`→`id`, `label_ko`→`title_ko`, `label_en`→`title`, `derived_from`→`sources` (청크 732개, 구성체 182), `chunk2kg`·`extract_refs`·STYLEGUIDE·rules 갱신. `index.md`는 생성물 — `tools/labels.py` + `kb_index` 매크로 (`bazel build //kb/dev:index`) |
| 5 E(b) `kb/{ontology,odd}` + OpenODD | **완료** | `git mv` + 라벨·경로 재작성 22파일. ODD 원본 `kb/odd/project-odd.yml`(OpenODD, 확장 키 `checks`·`exclusions_reviewed`), `taxonomy.yml`·`project-odd.ttl` 생성(`tools/taxonomy.py`·`odd2kg.py`, 부정 검사 2종 확인). YAML 부분집합 로더는 부채로 기록 |
| 6 문서 세 층 | **완료** | `tools.md` 전면 재편 — 게이트 총람(19+2)이 원본, 계층·실측 열. `rules.md` §7 development·§8 V&V, `method.md` §13·§14, `ontology.md` development·V&V 층. 결정 링크는 파일 경로(링크 검사 대상) |
| 7~8 | 미착수 | — |
| Q11 노트 커밋 | **유저/inspection** | `git add docs/agent-knowledge-system-notes.md docs/agentic-knowledge-base-structure.md && git commit` |
