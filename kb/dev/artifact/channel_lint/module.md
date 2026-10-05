---
id: https://agentic-knowledge-base.dev/id/chunk/ae6d4d38-8012-4802-9b53-8c33d4293291
type: artifact
level: executable
title_ko: 파일 tools/channel_lint.py
title: file tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/60faade0-d3e7-4ad4-8bf6-371be22956c3, https://agentic-knowledge-base.dev/id/chunk/f1d4cbae-2b57-4b96-826f-536b132cd624]
composite: {id: https://agentic-knowledge-base.dev/id/composite/84c1731c-46ae-469d-a2b2-a52d6615da86, title_ko: 파일 복합체 tools/channel_lint.py, title: file composite tools/channel_lint.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/2b6adf1a-07f9-41ca-b86b-44bcb3041a2a, https://agentic-knowledge-base.dev/id/composite/ac58dec5-5572-44b8-a5b4-28d1816c56e6, https://agentic-knowledge-base.dev/id/composite/45faf691-73c6-43a3-b8c9-25f7a11782bc, https://agentic-knowledge-base.dev/id/composite/f4e440cf-7d39-4f1b-9334-79189a47b8a2, https://agentic-knowledge-base.dev/id/composite/3740ef5b-1def-406b-ab6d-bbb40f9c7329, https://agentic-knowledge-base.dev/id/composite/d356c13f-12da-449f-8621-56cdffd536e1]}
---
**파일** — `tools/channel_lint.py` 다. 295줄 · 최상위 정의 7개 · 최상위 절 6개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""채널 게이트 — 하네스 채널(harness/channel 메시지 · harness/user 질문지)의 프로토콜을 기계로 강제한다.

규약 원본은 harness/README.md(에이전트 채널·메시지)와 harness/user/README.md(유저 채널·질문지)다. 두 세션(hci ·
orchestrator)은 파일 채널로만 소통하고, hci 는 소통만 한다 — 유저의 답을 수행하지 않고 메시지로 orchestrator 에
넘긴다(유저 교정 2026-09-11). 반영 허가 신호는 `답:` 줄이 채워진 질문지에 유저가 직접 `status: answered` 를 태깅하거나, 유저가 hci 세션에서 "답 적었어"라고 알려 hci 가 대신 태깅하는 것이다(유저 답 2026-10-04).

입력은 파일 목록이고 경로로 종류를 가른다.
  메시지   channel/{to_orchestrator,to_hci,archive}/<id>.md — 이 디렉토리의 .md 는 전부 메시지로 본다
  질문지   user/<id>.md · user/archive/<id>.md — 이 디렉토리의 .md 는 전부 질문지로 본다
  그 밖(legacy/ 아래 포함)의 입력은 배선 문제다 → CONFIG
검사 (게이트 id `channel`) — 메시지:
  fields      필수 필드 id from to type status subject created. id 는 네 자리, 파일명은 `<id>.md`, id 는 채널 전역에서 유일
  vocab       from·to ∈ hci|orchestrator 이고 서로 다르다. type ∈ task|question|answer|result|knowledge|status|ack,
              status ∈ new|read|in_progress|done|blocked
  writer      단일 작성자 — to_orchestrator/ 의 메시지는 to: orchestrator, to_hci/ 는 to: hci
  direction   task 는 hci → orchestrator, result·status 는 orchestrator → hci
  re          answer·result 는 re 필수. re 는 실재하는 메시지여야 하고 answer 의 대상은 question, result 의 대상은 task
  source      source 는 실재하는 질문지여야 한다
  sections    task 본문의 필수 절 여섯 — ## 배경 · ## 목표 · ## 완료조건 · ## 제약 · ## 파급효과 · ## 확인 못 한 것
  place       done 은 archive/ 에, done 이 아닌 것은 수신함에 있다
  pair        짝 없는 완료 — done 인 task 에 그것을 re 로 가리키는 result 가, done 인 question 에 answer 가 없으면 FAIL
검사 — 질문지:
  fields      필수 필드 id status subject created. id 는 파일명 stem(`Q-<네 자리>`)과 같다
  vocab       status ∈ open|answered|closed (answered 는 유저가 태깅하거나 유저 알림에 따라 hci 가 대신 태깅한다 — lint 는 값만 보고 행위자는 판별하지 않는다)
  place       closed 는 user/archive/ 에, closed 가 아닌 것은 user/ 에 있다
  answers     `답:` 줄이 하나 이상 있다. closed 인데 빈 `답:` 줄(콜론 뒤가 공백뿐)이 있으면 FAIL
  re          re(선택)는 실재하는 메시지여야 한다 — 닫히지 않은 질문지만 본다(메시지는 git 밖이라 archive 의 질문지가
              가리키던 메시지는 reset 뒤나 새 clone 에서 없다)
  hci-reflect 닫히지 않은 질문지에 hci 가 반영·수행했다는 서술("hci 반영" · "hci 가 반영" · "hci 가 수행")이 있으면 그
              질문지를 source 로 갖는 task 에 result 가 돌아와 있어야 한다. 괄호 서명 "(hci, 날짜)" 는 잡지 않는다
WAIT(FAIL 아님): open 질문지 = 유저 답 대기 · answered 질문지 = hci 처리 대기(빈 `답:` 수를 적는다) · 수신함의 done 이 아닌
  메시지 = 수신자 대기(blocked 는 따로 표시).
면제: `--waivers docs/waivers.md` 의 게이트 id `channel`, 축 파일. 코드 속 면제는 없다 (C).
출력: FAIL [channel] <파일>: <이유> · WAIT [channel] … (대기 보고) · CONFIG [channel] … · SKIP [channel] …
종료 코드(kb_lib): 0 PASS · 1 판정 실패 · 2 설정·입력 문제(--waivers 없음, 파일 없음, 경로 밖) · 3 검사 미실행(입력 0건).
SKIP 은 PASS 가 아니다
사용: channel_lint.py --waivers docs/waivers.md <메시지·질문지 md 파일...>
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
