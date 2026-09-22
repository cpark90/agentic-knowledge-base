---
id: https://agentic-knowledge-base.dev/id/chunk/51822789-fb4e-4062-8bb1-6cc0dda2eee0
type: requirement
level: functional
pattern: ubiquitous
title_ko: 합격 기준이 실제로 거르는지는 변이 표본의 거부로 측정되어야 한다
title: Whether pass criteria actually filter must be measured by the rejection of mutation samples
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/ee402e65-6abe-43ec-86ef-554f2ada9207]
---
**검증 목표** — 검증의 세 방향 중 "기준의 질" 이 변이 주입 표본으로 확인된다는 결정이 분석 시점 고정물로 성립한다는 것이 보여져야 한다. 링크 규칙마다 위반 고정물 하나가 있고, 고정물이 실패할 때만 시험이 PASS 다. 판정자의 정확도·판별력·캘리브레이션은 학습된 판정자가 없어 측정 대상이 없다.

- **이해관계자**: 업체 · V&V · **관심사**: 기준과 판정자의 질

**무엇을 관측하면 성립하는가**

- `defs/tests/BUILD.bazel` 의 고정물 다섯(`bad_plane_dir`·`bad_residency`·`bad_supersedes`·`bad_verifies`·`bad_decision_levels`)이 각각 규칙 하나를 어기고, 대응 `failure_test` 가 기대 문구로 실패할 때만 PASS 다.
- 변이 검출률은 `거부된 고정물 / 고정물` 로 읽힌다. 고정물이 통과해 버리면 시험이 FAIL 이다.
- V&V 합격 기준마다 음성 표본(서술 또는 고정물)이 있다.
- 학습된 판정자는 ODD 명시 제외(학습 모델 임베딩)라 세 지표의 측정 대상이 없다.

판정의 원본은 `defs/tests/BUILD.bazel` 의 `failure_test` 다섯과 `defs/kb.bzl` 의 `_check_links`·`_check_residency` 다.
