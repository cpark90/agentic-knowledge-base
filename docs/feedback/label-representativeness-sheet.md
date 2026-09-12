---
from: hci
status: approved
targets: [docs/feedback/label-representativeness-protocol.md]
---

# 라벨 대표성 실험 — 판정 기록지 (사람 판정, 표본 30, seed 20260911)

## 무엇을 재는 실험인가

이 체계는 **읽기 응답의 기본이 라벨 목록**이다 — 에이전트에게 본문을 다 주지 않고 라벨만 보여준 뒤,
필요한 것만 펼치게 한다 (5.6절). 그래서 **라벨만 보고 본문을 짐작할 수 있어야** 이 구조가 성립한다.
짐작이 빗나가면 에이전트는 엉뚱한 청크를 펼치고, 컨텍스트 예산은 예산대로 쓰면서 필요한 것은 놓친다.

"라벨이 본문을 대표하는가"는 **기계가 판정할 수 없다** — 그래서 도입 1단계의 마지막 통과 조건이
사람의 판정으로 남아 있다 (4.13절 라벨 대표성, 14.1 정정본 "의미 보존" 축). 이 기록지가 그 판정이다.

같은 실험을 에이전트 판정자로도 했다 — 적합 58/60, 미끼 10/10 검출
([`label-experiment-agent-2026-09-11.md`](label-experiment-agent-2026-09-11.md)). 그 판정자는 이 저장소의 청크를
저작한 세션이라 **믿을 수 있는지 자체가 미검증**이다. 사람의 판정이 그 대조군이다 — 두 결과가 비슷하면
앞으로 이 실험을 에이전트에게 맡길 수 있고, 크게 다르면 맡길 수 없다.

## 어떻게 채우는가 (30분)

1. 아래 표의 **라벨만** 본다. 파일 이름도 본문도 보지 않는다.
2. 각 행의 "예측" 칸에 **이 청크가 무슨 말을 할지 한 문장**으로 적는다. 모르겠으면 "모름"이라 적는다 — 그것도 데이터다.
3. 30개를 다 적은 **뒤에** [`label-representativeness-key.md`](label-representativeness-key.md)를 연다. 번호마다 본문 요지가 있다.
4. 예측과 본문을 대조해 "판정" 칸에 셋 중 하나를 적는다.

| 판정 | 뜻 | 예 |
|---|---|---|
| **적합** | 예측이 본문의 요지와 같다. 세부가 달라도 "무엇에 대한 것인지"가 맞으면 적합 | 라벨 "대안 청크 선택적 기록의 기각" → 예측 "대안을 있을 때만 두는 안을 기각" → 본문이 그 내용 |
| **부분** | 대상은 맞는데 **범위나 초점이 어긋난다** | 라벨이 이득 하나만 말하는데 본문은 다섯을 말함 |
| **부적합** | 다른 것을 예측했다. 라벨이 본문을 대표하지 못한다 | 라벨은 "기억 승격"인데 본문은 "ODD가 기반인 이유" |

5. 맨 아래 "집계"에 수를 적는다. **적합 24/30(80%) 이상이면 통과**다.
6. 부적합·부분으로 나온 라벨은 재저작 대상이다 — 담당 역할이 라벨을 고치고 다시 판정한다.

## 읽는 법

- **종류** 열: `요구`는 요구 문장, `결정 결론/근거/대안`은 결정 하나를 이루는 세 청크의 각 부분이다.
- 라벨은 한글·영어 1:1이다. 어느 쪽으로 예측해도 된다.
- 표본 30은 살아 있는 청크에서 무작위로 뽑았다(요구 5 · 결론 10 · 근거 8 · 대안 7, seed 고정이라 재현된다). 순서는 섞여 있다.

| # | 종류 | 라벨 (ko) | 라벨 (en) | 예측 | 판정 |
|---|---|---|---|---|---|
| 1 | 결정 대안 | V&V 전용 plane 신설의 기각 | Rejecting new V&V-specific planes |  |  |
| 2 | 결정 대안 | ODD에서 새 속성을 바로 만드는 안 | Introducing new properties directly in the ODD |  |  |
| 3 | 결정 결론 | 가정에는 판정 유형과 판정 식을 함께 적는다 | Every assumption records its verification kind and expression |  |  |
| 4 | 결정 결론 | plane은 판정 방식으로 정의되고 코어는 일곱이다 | Planes are defined by verification mechanism; the skeleton has seven |  |  |
| 5 | 결정 결론 | V&V 프로파일은 도메인당 한 번의 위험 분석 G1~G6으로 만든다 | The V&V profile is built once per domain by risk analysis G1–G6 |  |  |
| 6 | 결정 근거 | 네 질의가 링크 모델의 역량 질문이다 | The four queries are the link model's competency questions |  |  |
| 7 | 결정 결론 | 추적성 지표 다섯과 그 경고 신호 | Five traceability metrics and what they warn about |  |  |
| 8 | 요구 | 분야 지식을 어휘로 축적한다 | Accumulate domain knowledge as vocabulary |  |  |
| 9 | 결정 근거 | 셋을 섞으면 무효화 범위가 흐려진다 | Conflating the three blurs the scope of invalidation |  |  |
| 10 | 결정 근거 | 구성도 하나의 결정이며 반복 기각은 공리의 재료다 | Composition is itself a decision, and repeated elimination is material for axioms |  |  |
| 11 | 결정 근거 | 이행성·반대칭성 공리가 이미 있고 part-of는 순서를 모른다 | Transitivity and antisymmetry already exist; part-of does not know order |  |  |
| 12 | 결정 결론 | entity/related와 어휘/형식화로 나눈 모듈을 최상위가 import한다 | Modules split by entity/related and vocabulary/rules, imported by a thin top |  |  |
| 13 | 결정 근거 | 수준마다 판정이 다르므로 청크가 다르다 | Different judgements per level require different chunks |  |  |
| 14 | 결정 대안 | v1의 scene·situation·scenario 3분리 폐기 | The v1 scene, situation, scenario split is retired |  |  |
| 15 | 요구 | 기준 없는 verifies는 거부한다 | Reject verifies without pass criteria |  |  |
| 16 | 결정 대안 | 양방향 전파의 기각 | Rejecting bidirectional propagation |  |  |
| 17 | 결정 결론 | ODD는 일곱 절과 속성별 판정 방법으로 쓴다 | The ODD has seven sections and a check per property |  |  |
| 18 | 결정 근거 | 아무것도 거르지 않는 기준도 통과하므로 기준의 질을 따로 잰다 | A criterion that filters nothing also passes, so its quality is measured separately |  |  |
| 19 | 요구 | 감사는 체계의 출력만으로 성립한다 | Audit stands on the system output alone |  |  |
| 20 | 결정 결론 | 결정의 대체는 supersedes이고 옛 결정은 deprecated로 남는다 | A decision is replaced via supersedes; the old one remains deprecated |  |  |
| 21 | 요구 | 하네스는 읽기·쓰기 집합을 기록한다 | The harness records read and write sets |  |  |
| 22 | 결정 결론 | 개념 정의와 개체는 파일이 다르고 편집 주체도 다르다 | Concept definitions and individuals live in different files with different editors |  |  |
| 23 | 결정 근거 | 요인이 할당을 증명하고 통제되지 않은 관측은 시험이 아니다 | The factor justifies the assignment; uncontrolled observation is not a test |  |  |
| 24 | 요구 | 조건이 깨지면 전수조사 없이 무효화한다 | Invalidate without exhaustive survey |  |  |
| 25 | 결정 결론 | 세 단절의 공통 원인은 공통 어휘의 부재 — 어휘에서 시작한다 | Three breaks share one cause; start from vocabulary |  |  |
| 26 | 결정 결론 | 개발 프로파일에서 일곱 plane의 실체·거주 수준·단위·판정 도구 | Substance, residency, unit and verification tool of the seven planes in the development profile |  |  |
| 27 | 결정 대안 | 판정 도구 없는 plane 허용의 기각 | Rejecting planes without verification tools |  |  |
| 28 | 결정 대안 | 확인 생략과 자동 귀속의 기각 | Rejecting verification-only and automatic attribution |  |  |
| 29 | 결정 근거 | plane은 판정 방식이므로 프로파일은 실체와 도구만 채운다 | Since a plane is a mode of judgement, a profile only fills in substance and tools |  |  |
| 30 | 결정 대안 | ODC만으로 두는 안의 기각 | Rejecting ODC-only subtypes |  |  |

## 집계

| | 수 |
|---|---|
| 적합 | /30 |
| 부분 | /30 |
| 부적합 | /30 |
| **판정** | 적합 ≥ 24 → 통과 / 미만 → 미통과 |

- 부분·부적합으로 나온 번호:
- 메모(절차가 이상했던 점, 라벨을 고치고 싶은 것):

## 답
(유저가 채움 — 위 집계를 채우면 그것이 답이다. 절차 자체에 이의가 있으면 여기에 적는다)
