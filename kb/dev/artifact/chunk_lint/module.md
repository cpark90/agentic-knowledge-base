---
id: https://agentic-knowledge-base.dev/id/chunk/3b9822e1-5e35-4f9e-8c26-429350db7faa
type: artifact
level: executable
title_ko: 파일 tools/chunk_lint.py
title: file tools/chunk_lint.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk-lint}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/d93492e4-f343-4736-b4a5-d04f48a3a75f, https://agentic-knowledge-base.dev/id/chunk/3e80ad06-93e6-4ba1-af6c-f354dd163b97, https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5]
composite: {id: https://agentic-knowledge-base.dev/id/composite/f1d91f37-d353-405b-bd98-41132f8d5390, title_ko: 파일 복합체 tools/chunk_lint.py, title: file composite tools/chunk_lint.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/0149c880-a2a1-45d1-bad4-6d54b7932fc3, https://agentic-knowledge-base.dev/id/composite/ea7476e7-b990-4825-a271-6356855d2118, https://agentic-knowledge-base.dev/id/composite/7b250e22-fd3e-4d64-9b95-214bd55ce9d3]}
---
**파일** — `tools/chunk_lint.py` 다. 389줄 · 최상위 정의 9개 · 최상위 절 3개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""청크·명명·산문 린트.

  --chunks <files>   청크 본문(assertion) 파일 검사 (노트 4.1절):
                     본문 42줄 이하. YAML frontmatter(head 메타데이터)와
                     끝의 빈 줄은 본문으로 세지 않는다. **상한은 plane 별 프로파일 파라미터**이고 정의처는
                     `kb_lib.BODY_LINE_LIMITS` 하나다 — `artifact` 는 200줄이다(본문이 저작이 아니라 소스의
                     인용이라 42줄이 인위적 분할을 부른다, p7-code-extraction-direction "예산").
                     .md 청크는 산문 문체(STYLEGUIDE §0 단정 서술형, 2026-09-13)도 본다 — 경어·비격식 종결이 문장 끝에
                     오거나 산문에 느낌표가 있으면 위반(kb_lib.check_prose, 게이트 id `prose`). 코드·따옴표·주석 안과
                     `!=`·`![` 는 산문이 아니다. TTL 청크는 산문 검사 대상이 아니다. 추측·구어는 consistency ⑦ 보고다.
                     type: decision 인 .md 는 역할 표지(STYLEGUIDE §4, 게이트 id `decision-role`)도 본다 — 본문 첫 산문 줄이
                     굵은 표지로 시작해야 한다. conclusion.md·rationale.md·alternatives.md 는 각각 **결론**·**근거**·**대안**,
                     V&V 시나리오 패키지(kb/vv/scenario)의 `<슬러그>-stimulus.md`·`-factors.md`·`-excluded.md` 는 각각
                     **자극**·**요인**·**배제 자극**(결정 p8-scenario-authoring), 그 밖의 파일명(단일 파일 옛 결정
                     chunks/decision/d-*.md, 단일 청크 시나리오)은 **결론** 이다. 표지 안의 한정어(**대안 없음**)는
                     같은 표지다(kb_lib.DECISION_ROLE_MARKER). status: deprecated 는 대상이 아니다.
                     살아 있는 .md 청크(status draft·stable·suspect, kb_lib.LIVE_STATES)는 첨가와 목록 규칙도 본다
                     (명세 문서 작성 규격 4.1·4.3·9.4, 유저 승인 2026-09-22 — 결정 p4-slot-answers-one-question·
                     p4-three-empty-values). 게이트 id 셋은 `addition`(메타 문장 "다음과 같다"·채움 문구 "특이사항 없음"),
                     `empty-value`(세 빈 값 `없음`·`해당 없음`·`미확정` 밖의 `N/A`·`TBD`·`미정`·표의 단독 대시 셀),
                     `list-rules`(손 번호 `2.` 이상·항목 9개 초과·중첩 3단계 이상·항목당 240자 초과·빈 항목)이다.
                     검사 함수는 consistency ⑧·⑨ 와 같다(kb_lib.check_addition·check_lists) — 보고와 게이트의 수치가 갈리지 않는다.
                     살아 있는 type: annotation 인 .md 는 주석이다 (STYLEGUIDE §4, 결정 p7-commentary-form). 게이트 id
                     `blocking-comment` 는 그 결정이 정한 **유일한 게이트 효과**를 강제한다 — 첫 줄이 `issue (blocking)` 이면서
                     `해소: 열림` 인 주석이 있으면 FAIL 이다. 그 밖의 라벨·장식·해소 상태는 기록이고 막지 않는다. 첫 줄 꼴과
                     닫힌 어휘·본문 문장 상한은 shape(kb/ontology/shapes/review-comment-body-shapes.ttl)가 본다.
                     `generated.by` 가 `process:judge` 이고 `type: memory` 인 .md 는 **판정 로그**다 (결정
                     p8-judge-calibration-binding). 게이트 id `judge-log` 는 판정만 부르지 않고 로그의 형식만 본다 —
                     판정 표의 헤더가 `kb_lib.JUDGE_LOG_TABLE_HEADER` 와 같고 행마다 질문 id·값·확신도·**판정자 식별자**
                     (세션·모델, 2026-09-30 — 외부 서비스가 아니라 세션 판정자다)·입력 지문(sha256 64자)·시각(ISO 8601 UTC)이
                     비어 있지 않으며 처리가 임계의 세 값 안, `일치` 열이 `일치`·`불일치`·`해당 없음` 셋 안이어야 한다.
                     **판정 로그가 0건이면 거부할 것이 없고 그것은 SKIP 이 아니라 PASS 다** — 로그의 존재를 요구하는
                     것은 이 게이트의 몫이 아니다. 판정 자체는 게이트 밖 도구(`bazel run //tools:judge`)가 한다.
                     살아 있는 .md 청크 본문의 선택 슬롯 `핵심:`(요약 항목)은 **요약 지지 참조** 검사(게이트 id
                     `summary-support`, 2026-09-30, judge-without-service 기계 환원 ①)도 받는다 — 항목마다 `[#id]`·
                     `d-NNNN`·IRI(백틱)·마크다운 링크 중 하나로 본문의 지지 근거를 가리켜야 한다. 슬롯이 없으면 대상이
                     아니다. 오탐 실측(2026-09-30): 저장소가 아직 이 슬롯을 쓰지 않아 0/0 — 사용이 늘면 재실측한다.
  --ttl <files>      TTL 파일명이 산출물 접미사 규약(0.2절)을 따르는지 검사.
  --waivers <file>   docs/waivers.md — 게이트 id `prose`·`addition`·`empty-value`·`list-rules`·`blocking-comment`·`judge-log`·
                     `summary-support`(축 파일)로 면제된 파일의 위반은 세지 않는다. 면제된 것은 `WAIVED [<게이트 id>]` 줄로
                     남긴다 (집계에서 빼되 목록에는 남긴다). 없으면 면제 없음.

출력·종료: `FAIL [chunk|naming] <경로>: <메시지>` ·
`FAIL [prose|decision-role|addition|empty-value|list-rules|blocking-comment|judge-log|summary-support] <경로>:<줄>: <이유>` + EXIT_FAIL.
파일 없음·waiver 표 오류는 EXIT_CONFIG, 대상 0건은 EXIT_SKIP (PASS 아님).
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    from tools import kb_lib  # bazel runfiles 경로
except ImportError:
    import kb_lib  # 직접 실행
try:
    from tools.chunk2kg import comment_form  # 주석 본문의 파서 — 방출(chunk2kg)과 게이트가 같은 판정을 쓴다
except ImportError:
    from chunk2kg import comment_form
```
<!-- 인용 끝 -->
