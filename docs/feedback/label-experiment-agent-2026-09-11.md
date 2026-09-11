---
from: hci
status: open
targets: [docs/feedback/label-representativeness-protocol.md, docs/roadmap.md]
---

# 라벨 대표성 실험 — 에이전트 판정 결과 (2026-09-11, 판정자 = hci 세션)

표본: orchestrator 의 `tools/label_sample.py`, seed 20260911 — 실제 60 + 미끼 10. 절차: 라벨만 보고 70개 예측을 파일에 고정(`predictions.md`) → 본문만(출처·미끼 여부 숨김) 대조 → 3점 판정·확신도 → 정답지와 집계.

## 결과

- **적합 58/60 = 96.7%** · 부분 2 · 부적합 0 (실제 표본, 통과 기준 ≥ 80%: **통과**)
- **미끼 검출 10/10** — 라벨과 다른 본문을 전부 부적합으로 잡음. 실제 표본을 부적합으로 오판한 것 0건 (판별력, 8.14절)
- 확신도 평균: 적합 0.94 · 부분 0.60 · 미끼 0.94
- 저작자별(실제 표본): `claude` 적합 37/39 · `hci` 적합 21/21
- 층별(실제 표본): alt 적합 14/15 · conc 적합 20/20 · rat 적합 14/15 · req 적합 10/10

## 부분·부적합 항목 (실제 표본)

| # | 층 | 파일 | 판정 | 이유 |
|---|---|---|---|---|
| 27 | alt | `kb/dev/decision/p0-deprecate-not-delete/alternatives.md` | 부분 | 라벨은 대상을 말하지 않는다 — 예측은 결정 삭제, 본문은 어휘(개념) 폐기의 삭제·참조 거부 안 |
| 31 | rat | `kb/dev/decision/p9-csp-mapping-of-links/rationale.md` | 부분 | 라벨은 다섯 이득 중 (a)만 — 본문은 (a)~(e) |

## 미끼 (전부 검출)

| # | 라벨 출처 | 본문 출처 | 판정 |
|---|---|---|---|
| 1 | `kb/dev/decision/p11-memory-promotion-rule/conclusion.md` | `kb/dev/decision/p3-odd-derivations-and-gate/conclusion.md` | 부적합 (0.95) |
| 5 | `kb/dev/decision/p5-plane-by-verification/alternatives.md` | `kb/dev/decision/p10-candidate-and-confirmed-link/alternatives.md` | 부적합 (0.95) |
| 9 | `kb/dev/decision/p4-plane-subclass-level-property/alternatives.md` | `kb/dev/decision/p7-dev-kb-completion/alternatives.md` | 부적합 (0.95) |
| 13 | `kb/dev/decision/p8-vv-reports/conclusion.md` | `kb/dev/decision/p3-odd-required-sections/conclusion.md` | 부적합 (0.95) |
| 17 | `kb/dev/decision/p0-two-axes-plane-level/rationale.md` | `kb/dev/decision/p2-judgement-history-in-verified/rationale.md` | 부적합 (0.95) |
| 18 | `kb/dev/decision/p11-dev-profile-role-permissions/rationale.md` | `kb/dev/decision/p8-unknown-risk-cases/rationale.md` | 부적합 (0.9) |
| 30 | `kb/dev/decision/p4-composite-as-part-of/rationale.md` | `kb/dev/decision/p4-chunk-iri-is-the-anchor/rationale.md` | 부적합 (0.95) |
| 33 | `kb/dev/decision/p12-artifact-review-support/alternatives.md` | `kb/dev/decision/p3-odd-first-project-start/alternatives.md` | 부적합 (0.95) |
| 40 | `kb/dev/decision/p7-decision-supersession/rationale.md` | `kb/dev/decision/p10-candidate-and-confirmed-link/rationale.md` | 부적합 (0.95) |
| 41 | `kb/dev/decision/p8-vv-roles/conclusion.md` | `kb/dev/decision/p2-ontology-pitfall-catalogue/conclusion.md` | 부적합 (0.95) |

## 편향과 한계

- 판정자(hci 세션)가 실제 표본 중 `hci/` 저작 청크의 저자다 — 저작자별 수치를 위에 나눴다. 두 저작자 모두에서 적합률이 높아 저자 효과는 보이지 않으나, 같은 세션이 라벨 규약(결론 문장형)을 알고 있다는 점은 남는다.
- 판정자 자체의 3지표(8.14절) 중 판별력(미끼)은 잰 셈이고, 정확도·캘리브레이션은 사람 판정(기록지 30)과 대조해야 한다.
- 부분 2건은 라벨이 본문의 **대상**(어휘 폐기 vs 결정 폐기)이나 **범위**(이득 하나 vs 다섯)를 말하지 않는 경우다 — 재저작 후보.

## 답
(유저가 채움 — 사람 판정 결과와 함께 1단계 통과 여부)
