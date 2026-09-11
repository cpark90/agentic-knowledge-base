---
from: hci
status: approved
targets: [docs/feedback/label-representativeness-protocol.md]
---

# 라벨 대표성 실험 — 판정 기록지 (선택지 1: 사람 판정, 층화 표본 30, seed 20260911)

**절차.** 아래 라벨만 보고 각 항목이 무엇을 말하는지 **한 문장으로 예측**해 "예측" 열에 적는다. 30개를 다 적은 뒤에만
`label-representativeness-key.md`를 열어 본문 요지와 대조하고 "판정" 열에 **적합 / 부분 / 부적합**을 적는다.
통과 기준: 적합 ≥ 24/30 (80%). 부적합 라벨은 재저작 대상. 결과는 관측으로 기록한다 (4.13절, 14.1 정정본 1단계).

표본: 요구 5 · 결론 10 · 근거 8 · 대안 7 — 살아 있는 청크에서 무작위(seed 고정). 순서는 섞였다.

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

- 적합: /30 · 부분: /30 · 부적합: /30 → 통과(≥ 24) / 미통과
- 부적합 라벨 목록:

## 답
(유저가 채움 — 판정 결과 또는 절차 이의)
