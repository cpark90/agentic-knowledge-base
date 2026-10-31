---
id: https://agentic-knowledge-base.dev/id/chunk/ae6d4d38-8012-4802-9b53-8c33d4293291
type: artifact
level: executable
title_ko: 파일 tools/channel_lint.py
title: file tools/channel_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-channel-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/60faade0-d3e7-4ad4-8bf6-371be22956c3, https://agentic-knowledge-base.dev/id/chunk/f1d4cbae-2b57-4b96-826f-536b132cd624]
composite: {id: https://agentic-knowledge-base.dev/id/composite/84c1731c-46ae-469d-a2b2-a52d6615da86, title_ko: 파일 복합체 tools/channel_lint.py, title: file composite tools/channel_lint.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/2b6adf1a-07f9-41ca-b86b-44bcb3041a2a, https://agentic-knowledge-base.dev/id/composite/ac58dec5-5572-44b8-a5b4-28d1816c56e6, https://agentic-knowledge-base.dev/id/composite/45faf691-73c6-43a3-b8c9-25f7a11782bc, https://agentic-knowledge-base.dev/id/composite/f4e440cf-7d39-4f1b-9334-79189a47b8a2, https://agentic-knowledge-base.dev/id/composite/30c94888-c0b3-4616-8c73-db2b38068fb2, https://agentic-knowledge-base.dev/id/composite/3740ef5b-1def-406b-ab6d-bbb40f9c7329, https://agentic-knowledge-base.dev/id/composite/d356c13f-12da-449f-8621-56cdffd536e1]}
---
**파일** — `tools/channel_lint.py` 다. 562줄 · 최상위 정의 12개 · 최상위 절 7개이고 이 단위 지식은 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""채널 게이트 — 하네스 채널(harness/channel 메시지 · harness/user 질문지)의 프로토콜을 기계로 강제한다.

규약 원본은 harness/README.md(에이전트 채널·메시지)와 harness/user/README.md(유저 채널·질문지)다. 두 세션(interpreter ·
orchestrator)은 파일 채널로만 소통한다. hci 는 interpreter 의 유저 대상 하위 역할이고 같은 세션이 맡으며, 소통만 한다 — 유저의 답을 수행하지 않고 메시지로 orchestrator 에
넘긴다(유저 교정 2026-09-11). 반영 허가 신호는 `답:` 줄이 채워진 질문지에 유저가 직접 `status: answered` 를 태깅하거나, 유저가 hci 세션에서 "답 적었어"라고 알려 hci 가 대신 태깅하는 것이다(유저 답 2026-10-04).

입력은 하네스 루트(`--harness`)이고 그 아래 디렉토리를 **실행 시점에** 읽는다(유저 답 Q-0061 Q152-a). 메시지는 git 밖
런타임 파일이라 빌드가 분석 단계에 잡은 목록은 실행 때 이미 낡았을 수 있다(mark.sh 의 archive 이동). 경로로 종류를 가른다.
  메시지   channel/to_<역할>/<id>.md · channel/archive/<id>.md — 수신함은 역할 어휘 ROLES 에서 끌어낸다(INBOXES)
  질문지   user/Q-*.md · user/archive/Q-*.md
  legacy/(옛 채널 기록)는 읽지 않는다. 파일 목록을 직접 주면(고정물 시험) 그 목록만 보고, 그 밖 경로는 배선 문제다 → CONFIG
읽는 동안 파일이 사라지거나 목록·파일 서명(inode·mtime·크기)이 바뀌면 이동 경쟁으로 보고 디렉토리를 다시 읽는다. 판정이
PASS 가 아니면 한 번 더 읽어 서명이 같은 상태에서 같은 판정이 나야 그 판정을 낸다 — 진짜 결함은 두 번 읽어도 남는다.
검사 (게이트 id `channel`) — 메시지:
  fields      필수 필드 id from to type status subject created. id 는 네 자리, 파일명은 `<id>.md`, id 는 채널 전역에서 유일
  vocab       from·to ∈ interpreter|orchestrator 이고 서로 다르다. 옛 이름 hci 는 interpreter 로 읽는다(ROLE_ALIASES). type ∈ task|question|answer|result|knowledge|status|ack,
              status ∈ new|read|in_progress|done|blocked
  writer      단일 작성자 — to_<역할>/ 의 메시지는 to: <역할>. hci 와 interpreter 는 같은 작성자다
  direction   task 는 interpreter → orchestrator, result·status 는 orchestrator → interpreter
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
  directive   대화 지시 기록 꼴(질문지 규약의 §대화 지시 기록, Q114-a) — `답:` 줄이 `(유저의 대화 지시` 로 시작하는
              질문을 가진 질문지는 넷을 갖춘다. ① 첫 `## ` 절 앞에 원문을 옮긴 인용 블록(`>`)이 있다 ② 답 줄 머리가
              `답: (유저의 대화 지시 원문, YYYY-MM-DD)` 이고 날짜가 실재한다 ③ 그 뒤 같은 줄이나 바로 다음 줄에 원문 또는
              "위 인용 그대로"가 있다 ④ 그 답부터 다음 질문 절(`## Q<번호>`) 전까지 `hci의 읽기` 로 시작하는 줄이나 절이 있다.
              subject 의 꼬리표와 인용 첫 줄의 문구는 보지 않는다 — 옛 기록의 문구가 조금씩 달라 핵심만 본다
  hci-reflect 닫히지 않은 질문지에 hci 가 반영·수행했다는 서술("hci 반영" · "hci 가 반영" · "hci 가 수행")이 있으면 그
              질문지를 source 로 갖는 task 에 result 가 돌아와 있어야 한다. 괄호 서명 "(hci, 날짜)" 는 잡지 않는다
검사 — 메시지·질문지 공통 (유저 답 Q103 3번, 2026-10-24):
  register    경어·감탄 — 게이트 `prose` 의 판정(kb_lib.check_prose: PROSE_FORBIDDEN_ENDINGS · PROSE_EXCLAMATION, 대상
              분절은 prose_segments)을 그대로 건다. frontmatter·코드 펜스·백틱 인용·따옴표 안은 prose_segments 가, 인용
              블록(`>`)은 여기서 뺀다 — 인용 블록에는 유저 원문이 있다
  names       식별자 옆 한글 이름 — 백틱 토큰이 KB 안의 항목으로 풀리면(결정 slug · `agt:<Term>` · `id:<name>`) 같은 줄에
              그 항목의 한글 이름이 정확히 있어야 한다. 한 줄에 같은 식별자가 여러 번 나오면 이름은 한 번이면 된다. 이름은
              결정 slug 가 결정 기록(복합체)의 `composite.title_ko`, `agt:`·`id:` 가 `rdfs:label`·`skos:prefLabel` 의 @ko 다.
              이름이 바뀐 항목은 옛 이름(결정은 `former_title_ko`, `agt:`·`id:` 는 `skos:hiddenLabel` @ko)도 받는다 — 메시지는
              쓴 뒤 고치지 않는 기록이라 그때의 이름이 맞는 이름이다. 발신 전 검사(--message)는 현재 이름만 받는다.
              풀리지 않는 토큰(경로·명령·게이트 id)은 대상이 아니다. 소급하지 않는다 — `created` 가 NAMES_SINCE 이상인
              항목에만 건다. 질문지의 `created` 는 날짜뿐이라 그날 0시(NAMES_SINCE 의 시간대)로 읽는다
WAIT(FAIL 아님): open 질문지 = 유저 답 대기 · answered 질문지 = hci 처리 대기(빈 `답:` 수를 적는다) · 수신함의 done 이 아닌
  메시지 = 수신자 대기(blocked 는 따로 표시).
면제: `--waivers docs/waivers.md` 의 게이트 id `channel`, 축 파일. 코드 속 면제는 없다 (C).
출력: FAIL [channel] <파일>: <이유> · WAIT [channel] … (대기 보고) · CONFIG [channel] … · SKIP [channel] …
종료 코드(kb_lib): 0 PASS · 1 판정 실패 · 2 설정·입력 문제(--waivers 없음, 파일 없음, 경로 밖) · 3 검사 미실행(입력 0건).
SKIP 은 PASS 가 아니다
사용: channel_lint.py --waivers docs/waivers.md --decisions <kb/dev 파일...> --ontology <온톨로지 ttl...>
      --graphs <id: 그래프 ttl...> --harness <하네스 루트 | 그 루트의 파일> [-- <메시지·질문지 md 파일...>]
발신 전 검사: channel_lint.py --decisions … --ontology … --graphs … --message <보낼 메시지 md>
  send.sh 가 수신함에 놓기 전의 임시 파일 하나에 메시지 단위 검사(fields · vocab · direction · re 필수 · sections ·
  register · names)를 건다. 채널 전체를 보는 검사(re 대상·source 의 실재, pair, place, id 유일, 단일 작성자)는 게이트에
  남는다 — re·source 의 실재는 send.sh 가 먼저 본다. 면제는 경로 단위라 아직 놓이지 않은 메시지에는 없다(--waivers 불요).
  인수는 `@<파일>` 로 줄 단위 파일에서 읽을 수 있다 — //harness:channel_send_check 가 이름 원천을 그렇게 싣는다
  이름 원천 셋은 필수다(없으면 CONFIG). --decisions 에서는 `kb/dev/decision/<slug>/conclusion.md` 만 읽는다.
  --harness 에 파일을 주면 그 실경로의 부모가 루트다 — `bazel test` 는 runfiles 의 심볼릭 링크를 따라 소스 트리에 닿는다.
  --harness 도 파일 목록도 없으면 `bazel run` 의 BUILD_WORKSPACE_DIRECTORY 아래 harness/ 를 본다
"""
import argparse
import datetime
import os
import re
import sys
import time
from pathlib import Path

from rdflib import RDFS, Graph, URIRef
from rdflib.namespace import SKOS

try:
    from tools.chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # frontmatter 의 단일 판독처
    from tools.kb_lib import (AGT, CHANNEL_GATE, EXIT_CONFIG, EXIT_FAIL, EXIT_OK, EXIT_SKIP, FORMER_TITLE_KEY, ID,  # bazel runfiles 경로
                              MD_CODE_SPAN, check_prose, gates_bzl_path, load_graph, load_waivers, md_lines, waived)
except ImportError:
    from chunk2kg import apply_plane_level_state, load_plane_level_state, parse_chunk  # 직접 실행
    from kb_lib import (AGT, CHANNEL_GATE, EXIT_CONFIG, EXIT_FAIL, EXIT_OK, EXIT_SKIP, FORMER_TITLE_KEY, ID,
                        MD_CODE_SPAN, check_prose, gates_bzl_path, load_graph, load_waivers, md_lines, waived)
```
<!-- 인용 끝 -->
