---
id: https://agentic-knowledge-base.dev/id/chunk/5d00d456-902e-4ec0-b6c8-3a1d112a6dd8
type: artifact
level: executable
title_ko: 절 token-limit-multiple (tools/kb_lib.py)
title: section token-limit-multiple in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/6b96d312-0c81-452d-8431-76ec85445dda
composite: {id: https://agentic-knowledge-base.dev/id/composite/6b96d312-0c81-452d-8431-76ec85445dda, title_ko: 절 복합체 token-limit-multiple (tools/kb_lib.py), title: section composite token-limit-multiple in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/5d00d456-902e-4ec0-b6c8-3a1d112a6dd8, https://agentic-knowledge-base.dev/id/chunk/adf4efcc-f323-49f3-87da-e81bb49bf4f5], part_of: https://agentic-knowledge-base.dev/id/composite/9b61f2e4-e29d-4fe0-8a4f-f1be5708e79a}
---
**절** — `tools/kb_lib.py` 의 절 `token-limit-multiple` 다. 본문 토큰 수의 상한 — plane 별 프로파일 파라미터 (STYLEGUIDE §4, 결정 p1-chunk-unit-is-tokens)

**정의** — `body_token_limit` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 본문 토큰 수의 상한 — plane 별 프로파일 파라미터 (STYLEGUIDE §4, 결정 p1-chunk-unit-is-tokens) ───────────
# 크기의 단위는 줄이 아니라 **토큰**이다 (유저 결정 2026-10-01). 줄 상한(42·200)은 폐지됐고 숫자는 실측이 정한다 —
# 컨텍스트 예산은 저작 산문의 줄당 토큰 중앙값 × 옛 200줄 = 5,418(42×129)이고, 저작 산문의 청크 상한은 그 예산의
# 1/5 에 가장 가까운 42의 배수 1,092(42×26)다. "한 번에 4~5개를 조망한다"는 42줄의 옛 근거를 같은 계수기로 옮긴
# 값이다 — 숫자가 아니라 도출이 규칙이다.
# `artifact`·`memory` = 2,856(42×68): 코드의 줄당 토큰 × 200줄. 두 plane 의 본문은 저작이 아니라 소스·실행의
# 인용이라 저작 산문의 예산이 인위적 분할을 부른다 — 함수를 쪼개는 것은 지식이 코드를 망가뜨리는 것이다.
# "청크 하나가 컨텍스트 한 창을 넘지 않는다"가 이 상한의 뜻이다.
                       # 선언한다(축 파일) — append-only 기록(판정 로그 등)의 소급 분할은 기록을 다시 쓰는 일이라 면제가 유일한 해소다
TOKEN_LIMIT_MULTIPLE = 42  # 상한은 42의 배수다 (유저 결정 2026-10-01) — 42줄의 옛 도출이 이 배수로 남았다
CONTEXT_TOKEN_BUDGET = TOKEN_LIMIT_MULTIPLE * 129  # 5,418 — 컨텍스트 예산 (옛 200줄의 같은 계수기 환산)
MAX_BODY_TOKENS = TOKEN_LIMIT_MULTIPLE * 26  # 1,092 — 저작 산문의 기본 상한 (예산 ÷ 5)
BODY_TOKEN_LIMITS = {"artifact": TOKEN_LIMIT_MULTIPLE * 68, "memory": TOKEN_LIMIT_MULTIPLE * 68}  # 2,856
```
<!-- 인용 끝 -->
