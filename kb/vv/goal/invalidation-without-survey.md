---
id: https://agentic-knowledge-base.dev/id/chunk/91dbec7f-3480-49ec-a83b-0273b572afde
type: requirement
level: functional
pattern: unwanted-behaviour
title_ko: 깨진 조건의 무효 범위는 전수조사 없이 가정 링크에서 계산되어야 한다
title: The invalidation range of a broken condition must be computed from assumption links without an exhaustive survey
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-21T22:30:00+09:00}
derivesFrom: [https://agentic-knowledge-base.dev/id/chunk/e0d0bf5c-8c1c-4638-9f64-89f94185d366]
---
**검증 목표** — 가정이 깨지면 그 가정을 전제하는 항목이 자동으로 무효화 표시된다는 결정이 그래프 질의 하나로 성립한다는 것이 보여져야 한다. 조건 판정 → 가정 상태 → `assumes` 역질의의 사슬이 무효 범위이고, 청크 본문을 읽지 않는다.

- **이해관계자**: 프로젝트 · **관심사**: 경계와 갱신

**무엇을 관측하면 성립하는가**

- 모든 가정이 ODD 조건을 `agt:refersTo` 하고 그 조건이 ODD 안에 있어(`odd-ref`) 가정의 판정식이 조건 판정의 연언으로 파생된다.
- 가정 하나의 의존 집합이 질의 하나로 나온다(CQ-22 `같은 가정에 의존하는 항목 집합`). 그 집합이 무효 범위의 직접 영향 집합이다.
- 인위 파괴 실험(`assume_check --break <cond-id>`)의 직접 영향 집합이 청크 파일 frontmatter 를 독립 스캔한 실제 의존 집합과 일치한다(정밀도·재현율 1).
- 무효화는 상태 표시이고 삭제가 아니다. 판정 결과는 관측으로 남는다(`kb/dev/memory/`).

판정의 원본은 `tools/assume_check.py` 의 전파 절과 `tools/cq-queries/CQ-22.rq`, `tools/validate.py` 의 `check_odd_refs` 다.
