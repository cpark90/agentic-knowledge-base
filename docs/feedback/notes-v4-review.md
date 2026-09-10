---
from: hci
status: open
targets: [../agent-knowledge-system-notes.md, ../agentic-knowledge-base-structure.md, ../decomposition-audit.md, design-detail-review.md, ../../INTENT.md, kb/dev/decision/, ontology/, ../tools.md, ../rules.md, ../method.md, ../roadmap.md, ../open-questions.md]
---

# 검토 — 노트 v4·구조도 v4 대규모 개편과 현 프로젝트의 완전 개선

유저(2026-09-10 17:34): *"agent-knowledge-system-notes.md와 structure.md 문서를 대규모 개편했어.
이를 기반으로 현 프로젝트를 완전히 개선하려고 해. 검토해줘."*

## 질문

한 시간 전(16:30)에 **노트 v3 기준 전면 재도출**이 끝났다 — 요구 26·결정 145·옛 126 deprecated·
7 plane·두 KB·uuid IRI(감사 §3). 그 직후 노트가 v4(2,789 → **3,361줄**, 순증 +572)로, 구조도가
v4(198줄)로 바뀌었다. 결정할 것은 "다시 재도출할까"가 아니라 **v3 재도출 산출물 중 무엇이 그대로
서고 무엇이 v4 때문에 틀렸는가, 그리고 v4가 새로 확정한 구현 바인딩(부록 E)을 어느 순서로
받는가**다.

어려운 이유:
1. v4의 순증 대부분이 **개발 KB(Part VII 신설)·V&V 워크플로(8.19~8.26)·구현 바인딩(부록 E)**이라
   결정만 늘어나는 게 아니라 **저장 구조·파일 형식·Bazel 아키텍처**가 바뀐다.
2. Part 신설로 **v3 Part VII 이후가 전부 한 칸 밀렸다.** 재도출된 결정 145건의 `(노트 N.N절)`
   인용과 감사표가 v3 번호다.
3. v4가 v3 재도출 직후에 **새 shape 규칙**(대안 청크 필수)을 확정해, 방금 만든 결정의 절반이
   위반이 되었다.

## 이미 정해진 것 — v3 → v4에서 바뀐 것 (순증 +572줄의 소재)

| 위치 | v3 | v4 | 성격 |
|---|---|---|---|
| **Part VII 개발 KB** (7.1~7.9, 128줄) | 없음 | 목적 · plane별 실체와 거주 수준(**결정은 수준마다 별개 청크**) · 저작 흐름 8단계(역할·게이트·V&V 대응물) · 결정의 구성체(**대안 청크 필수**, "대안 없었음"도 기록) · 계약 우선 · 스키마 파생 · 개발 역할·스코프(developer는 concrete 결정 없이 구현 불가, `-space`는 developer 작업 집합에 없음) · 산출과 지표 6 · 완료 판정 5조건(V&V `verifies` valid 필요) | **신설** — 재도출에 없음 |
| Part VIII V&V (8.19~8.26, 126줄) | 7.1~7.18 | + 워크플로 10단계 · 역할 5(engineer ≠ verifier author) · **위험 분석 G1~G6 = V&V 프로파일 구축 절차** · 시나리오 저작(부류에서, concrete는 생성만) · 케이스 생성 5규칙(`sampling:` 태그) · 보고 5종 · 에이전트 V&V · 지표 7 | 신설 8절 |
| 6.7 검사 게이트 | 10줄 | **게이트 총람 19종 × 실행 계층 5**(shape·verify·analysis·test·human) + "게이트 실패는 `draft`에 멈춘다" | 도구 설계의 새 원본 |
| 9.10 후보의 저장 형식 | 없음 | `-space` = `type: agt:Space` OKF 청크, 변수 하나 = 파일 하나, YAML(candidates·constraints **CEL**·preferences), **후보는 deps 아님**, 확정 시 head로 이동 | 신설 |
| 12.3 평가 | 10줄 | 인지능력 측정 절차 4단계 · **지표는 셋으로 제한**("낮으면 무엇을 고치는가") | 확장 |
| Part XIV 도입 순서 | 7단계 | **8단계**(7 V&V KB, 8 복원·감사) + **14.1 단계별 작업·도구·통과 조건·실패 시** | 확장 |
| 부록 B 사례 | 포인터 | device harvest **요구 하나의 완전한 하강·V&V·실행·되먹임·매트릭스** | 체계의 첫 실행 예제 |
| **부록 E 구현 바인딩** | 없음 | OKF v0.2 / Turtle+**LinkML** / Bazel 세 층 · OKF 필드 사상 · 수준별 본문 표기(YAML·**CEL**·JSON Schema·**OpenSCENARIO**) · ODD = **OpenODD YAML** · Bazel **plane별 규칙**(provider·deps=링크·분석 시점 검사) · 저장 구조 `kb/{ontology,odd,dev,vv}` | **신설 — 가장 큰 변화** |
| 산출물 정의 | 기반 2 + 메커니즘 5 + KB 1 | 기반 2 + 메커니즘 5 + **KB 2** 표, 문서의 지도 | 정리 |
| 미해결 | 25 | **28** — 26 시나리오 부류 재사용 범위 · 27 CEL 필터의 한계·솔버 전환 · 28 OKF `trust` 값 사상 | +3 |
| 5.3 | "현재 6개" (v1 잔재) | "현재 7개" — **고쳐짐** | — |
| 0.4 스코프 예시 | v1 plane `source`·`interface`·`protocol` | **그대로** — v1 잔재 남음 | 유저 판정 대상 |
| 구조도 | 211줄, 부록에 v1·v2 대비 변경 | 198줄. `input`이 Part XI로, **result가 골격/development/V&V 세 층**으로, 도구 목록 골격 15 + development 8 + V&V 14, rules·method도 세 층 | 재편 |

바뀌지 않은 것: 42줄·고유 용어·행위자는 태그·구성체 part-of·구축 우선·임베딩 후보만·상승 비자동·
"청크는 프로젝트를 넘지 않는다". 그리고 **Part 0~VI의 본문은 거의 그대로**다(재도출 145건 중
Part 0~6 유래 100여 건은 내용상 유효).

## 현재 상태 — v3 재도출 산출물 중 v4 때문에 틀린 것 (실측)

| # | 실측 | v4 규칙 | 상태 |
|---|---|---|---|
| S1 | 결정 145건의 절 인용 중 **Part 7~12 인용 213회**가 v3 번호 (`p7-*` 슬러그 21건 = v3 Part VII V&V, v4에서는 VIII) | Part VII 신설로 VII→VIII … XVI→XVII | **전부 한 칸 어긋남.** 감사 §3 표도 v3 기준 |
| S2 | 대안 청크 없는 결정 **77 / 145** (alternatives.md 68개뿐) | 7.4 "대안 청크 없는 결정 = shape 위반. '대안 없었음'도 기록" | **절반이 위반** |
| S3 | 결정 구성체 = 결론(concrete) + 근거(logical) + 대안(logical) | 7.2 "결정은 수준마다 별개 청크 — abstract 변수 선언 / logical 후보·제약·배제 / concrete 값" + 7.4 "결론·근거·대안 세 청크" | **v4 안에서 두 분할이 겹친다** (Q1). 감사가 이미 동질성 긴장으로 등록 |
| S4 | 결정 → 요구 링크가 `refines` | 6.8 "봉사를 `refines`로 명시", 7.3·7.4·B.2는 **`serves`** | 노트 내부 불일치 (Q2). `serves`는 trace 모듈에 없음 |
| S5 | `INTENT.md`·`docs/README`가 "노트 v3, 2,789줄" | v4 3,361줄 | 낡음 |
| S6 | `docs/roadmap.md` 도입 **7단계** | 14 "8단계" + 14.1 통과 조건 | 갱신 필요 |
| S7 | `docs/open-questions.md` 25건 | 28건 | +3 |
| S8 | `docs/tools.md` 검사 7·활용 8 (골격만) | 구조도: 골격 15 + development 8 + V&V 14 | 세 층 재편 |
| S9 | 프론트매터 `iri`·`label_ko`/`label_en`·`derived_from`·`status: stable`·`verified` | E.2: `id`·`title`+`title_ko`·**`sources`**·`status` = draft/**valid**/…·**`trust`**·`index.md`·`log.md` 생성 | **부록 E가 09-07 OKF 변환(결정 13-2)과 09-10 C1·C6과 다르다** (Q4) |
| S10 | `ontology/`·`odd/project-odd.ttl`(Turtle) 루트, `kb/vv/` 빈 BUILD | E.7 `kb/ontology/`·`kb/odd/`(**OpenODD YAML**)·`kb/dev/*.space.md`·`kb/vv/{goal,scenario,criteria,case,verifier}/` + `domain.osc`, 디렉터리마다 `index.md` | 구조 이동 + 형식 전환 |
| S11 | 게이트 = genrule + `py_test`(validate 7검사 + SHACL 7 shape) | E.6 plane별 Bazel 규칙, provider, **링크 = deps**, TIM·거주표·동질성은 분석 시점 실패, visibility = 읽기 스코프, `bazel query rdeps` = 영향 분석 | 아키텍처 전환 |
| S12 | 도입 1단계 "완료"로 표기 | 14.1 통과 조건: **"같은 작업의 토큰이 줄어듦이 측정됨, 고아율 < 10%"** | 측정된 적 없음 — **v4 기준으로 1단계 미통과** |
| S13 | STYLEGUIDE "예약 파일명 `index.md`·`log.md`를 쓰지 않는다"(09-07) | E.2 둘 다 **생성한다** | 규칙 반전 |

## 답이 가르는 것

- **Q1 결정 청크의 분할** — (a) 역할 3청크 유지(결론 concrete·근거 logical·대안 logical), abstract
  변수 선언은 `-space`가 있는 결정에만 넷째 청크로 (b) 수준 3청크(abstract·logical·concrete)로
  바꾸고 역할은 태그로. hci 권고 **(a)** — 재도출 산출물을 살리고 7.2·7.4를 둘 다 만족한다. 노트
  7.2의 "수준마다 별개 청크"를 "변수가 있으면"으로 정밀화하는 편집이 따른다.
- **Q2 `serves`** — 6.8의 `refines`와 7.3의 `serves`를 통일. hci 권고: `agt:serves ⊑ agt:refines`,
  치역 `RequirementChunk`, 관심사를 속성으로. 재도출된 `refines: [요구]`는 그대로 유효.
- **Q4 부록 E vs 09-07·09-10 결정** — E.2가 `valid`·`trust`를 쓰고 `index.md`·`log.md`를 생성한다.
  (i) 결정 유지 — 노트 E.2·4.11을 `stable`·`verified`로 고치고 예약 파일명은 **생성물로만** 허용
  (ii) 노트대로 — `stable`→`valid` 되돌리고 `trust` 필드 신설. hci 권고 **(i)** — OKF v0.2 실제
  필드명이고, `verified` 목록이 곧 판정 이력이라 `trust`가 필요 없다(미해결 28이 그 사상 문제를
  묻는데, 답은 "`verified`로 흡수"다). `title`/`title_ko`·`sources`·`id`는 E.2대로 **정렬**한다.
- **Q5 0.4 v1 잔재** — 스코프 예시의 `source`·`interface`·`protocol`을 v4 plane으로 고칠지.
- **Q6 부록 E 채택 순서** — 전부 받되 순서가 문제다. hci 권고:
  (a) **OKF 필드 정렬**(Q4) — 384 파일 기계 변환, 지금
  (b) **저장 구조 이동** `kb/{ontology,odd}` + ODD → OpenODD YAML + 택소노미 생성기 — ODD가 하나뿐이라 싸다
  (c) **Bazel plane 규칙** — 도입 3단계(링크 = deps)와 함께. 지금의 `py_test` 게이트는 그때까지 유효한 디딤돌
  (d) **CEL·LinkML·OSC** — 도입 5단계(`-space`·판정식)와 7단계(시나리오)에서
- **Q7 도입 1단계 통과** — 14.1 기준으로 "토큰 감소 측정"과 "고아율 < 10%"를 먼저 잴 것인가(권고:
  예 — 1단계 이득이 없으면 뒤를 진행할 근거가 없다는 것이 노트 자신의 규칙).

## 선택지 — 순서 (권고)

| 순서 | 무엇 | 크기 | 게이트 |
|---|---|---|---|
| 0 | Q1·Q2·Q4~Q7 결정 | — | — |
| 1 | **번호·수치 동기화** — 결정 145·감사·문서의 절 인용을 v4로(Part ≥ 7은 +1), `INTENT.md`·README 줄 수, 미해결 26~28 추가, roadmap 8단계 + 14.1 | 기계적 | 링크 검사 |
| 2 | **대안 청크 77건 보충** ("대안 없었음" 포함) + Q1 구조 반영 + `serves` 어휘 | 77 파일 | `bazel test` |
| 3 | **v4 델타 재도출** — Part VII 9절 · 8.19~8.26 · 6.7 총람 · 9.10 · 12.3 · 14.1 · 부록 B·E의 `[확정]` → 결정 약 40~60건, 요구 층 공백 7건(감사 §3) 보충 | 중간 | `bazel test` + 고아율 |
| 4 | **부록 E(a)** OKF 필드 정렬 + 예약 파일명 생성 | 384 파일 기계 변환 | 게이트 |
| 5 | **부록 E(b)** `kb/ontology`·`kb/odd` 이동, OpenODD YAML, `kb/vv/` 하위 구조 | 중간 | 게이트 |
| 6 | **문서 세 층 재편** — tools·rules·method를 골격/development/V&V로, 6.7 게이트 총람을 `tools.md`의 원본으로 | 문서 | 링크 검사 |
| 7 | **1단계 통과 조건 측정** — 토큰 감소·고아율 | 측정 | 14.1 |
| 8 | 부록 E(c)(d)는 도입 3·5·7단계에서 | — | — |

각 단계 끝에 `bazel test //...` PASS와 실측. **3단계까지가 "v4 정합"이고 4단계부터가 "완전 개선"**이다.

## 답
**유저(2026-09-10): "권고대로 진행"** — Q1(a) · Q2 `serves ⊑ refines` · Q4(i) 결정 유지·노트 정정 ·
Q5 v4 plane으로 · Q6 (a)→(b)→(c)→(d) · Q7 예 · Q8 지금 어휘만 · Q9 정의문은 지금, CEL은 5단계 ·
Q10 `counterfactualTest` 폐기 · Q11 노트 커밋(inspection/유저).

진행 기록은 아래에 추가된다.
