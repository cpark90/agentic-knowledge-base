---
id: https://agentic-knowledge-base.dev/id/chunk/ae6d4d38-8012-4802-9b53-8c33d4293291
type: artifact
level: executable
title_ko: 파일 tools/channel_lint.py
title: file tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/60faade0-d3e7-4ad4-8bf6-371be22956c3, https://agentic-knowledge-base.dev/id/chunk/f1d4cbae-2b57-4b96-826f-536b132cd624]
composite: {id: https://agentic-knowledge-base.dev/id/composite/84c1731c-46ae-469d-a2b2-a52d6615da86, title_ko: 파일 복합체 tools/channel_lint.py, title: file composite tools/channel_lint.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/2b6adf1a-07f9-41ca-b86b-44bcb3041a2a, https://agentic-knowledge-base.dev/id/composite/ac58dec5-5572-44b8-a5b4-28d1816c56e6]}
---
**파일** — `tools/channel_lint.py` 다. 206줄 · 최상위 정의 4개 · 최상위 절 2개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""채널 게이트 — 유저 피드백 채널(docs/feedback)의 역할 규약을 기계로 강제한다.

규약(docs/feedback/README.md, .claude/agents/hci.md): hci 는 소통만 한다. 유저의 구두 답은 담당 역할(orchestrator 등)에게
유효한 지시이지만, **hci 는 어떤 답이든 채널 밖에 반영하지 않는다** — 답을 `## 답` 에 옮기고 `handoff/` 항목으로 담당 역할에
넘긴다(유저 교정 2026-09-11, agrtls-practices-review-2026-09-12 F).

검사 (게이트 id `channel`):
  lane        경로로 판별 — 유저 lane(docs/feedback/*.md) · agents/ · inquiries/ · handoff/. `*.wip.md` 는 작성 중 — 건너뛴다(집계만)
  status      lane 별 허용 값 — 유저 open|approved|rejected (approved·rejected 는 유저만 태깅; lint 는 값만 본다)
              · agents open|relayed|answered|closed · inquiries open|answered|closed · handoff open|closed. 어휘 밖 → FAIL.
              status 가 없는 파일(유저의 자유 서술)은 검사하지 않고 INFO 로 센다
  handoff     `source` 가 실재하는 유저 lane 파일, `verdict` ∈ apply|apply-with-changes|needs-decision,
              필수 절 `## 파급효과` `## 반영 계획` `## 확인 못 한 것` `## 판정` → 아니면 FAIL
  ref         agents 항목의 `ref`(선택)는 실재해야 한다 — `handoff/<파일>` 또는 유저 lane 파일 → 아니면 FAIL
  pair        verdict apply·apply-with-changes 이고 open 인 handoff 항목을 `ref` 하는 agents 항목이 있으면 "되돌아옴",
              없으면 "되돌아오지 않은 handoff N건" 으로 보고(FAIL 아님 — pending)
  hci-reflect **유저 lane 만**: hci 가 반영·수행했다는 서술("hci 반영" · "hci 가 반영" · "hci 가 수행")이 있는 항목은 해소 기록이
              있어야 한다 — `인수: <역할> …` 줄(2026-09-12 이전 관례) **또는** 그 항목(또는 그것을 source 로 갖는 handoff 항목)을
              `ref` 하는 agents 항목, 또는 closed(되돌림). 둘 다 없으면 FAIL. 절 제목의 서명 "(hci, 날짜)" 는 소통의 표기이지 반영
              표지가 아니다. agents·inquiries·handoff lane 은 hci 가 아닌 역할이 쓰거나 hci 가 계획을 쓰는 곳이라 같은 문구가
              hci 에 대한 서술이다 — 돌리지 않는다 (오탐 실측 2026-09-12)
  pending     `## 답` 에 유저 답이 옮겨졌으나 반영 기록(인수·ref)이 없는 항목 → 담당 역할 대기로 보고
  placeholder 답 절에 placeholder(`(유저가 채움` · `(hci가 유저의 답을 채움`)가 남은 항목은 처리 대상 아님 — 집계만
면제: `--waivers docs/waivers.md` 의 게이트 id `channel`, 축 파일(규약 문서·원장). 코드 속 면제는 없다 (C).
출력: FAIL [channel] <파일>: <이유> · WAIT [channel] … (대기 보고) · CONFIG [channel] … · SKIP [channel] …
종료 코드(kb_lib): 0 PASS · 1 판정 실패 · 2 설정·입력 문제(--waivers 없음, 파일 없음) · 3 검사 미실행(항목 0건). SKIP 은 PASS 가 아니다
사용: channel_lint.py --waivers docs/waivers.md <채널 md 파일...>
"""
import argparse
import re
import sys
from pathlib import Path

try:
    from tools.kb_lib import CHANNEL_GATE, EXIT_CONFIG, EXIT_FAIL, EXIT_OK, EXIT_SKIP, load_waivers, waived  # bazel runfiles 경로
except ImportError:
    from kb_lib import CHANNEL_GATE, EXIT_CONFIG, EXIT_FAIL, EXIT_OK, EXIT_SKIP, load_waivers, waived  # 직접 실행
```
<!-- 인용 끝 -->
