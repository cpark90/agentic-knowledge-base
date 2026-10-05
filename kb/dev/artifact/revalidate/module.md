---
id: https://agentic-knowledge-base.dev/id/chunk/6bb7181c-bb07-4fff-a7da-c5f6c82427f1
type: artifact
level: executable
title_ko: 파일 tools/revalidate.py
title: file tools/revalidate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-revalidate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/651e2c44-9a19-4a3e-b04a-ed1226aeef23, https://agentic-knowledge-base.dev/id/chunk/57fc48aa-6091-4ee7-9763-13ddab8ac8b1, https://agentic-knowledge-base.dev/id/chunk/ab6eb286-d87b-43a5-88f0-e32ffdd54acc]
composite: {id: https://agentic-knowledge-base.dev/id/composite/974f7eff-3756-4a18-af98-04c75441cd70, title_ko: 파일 복합체 tools/revalidate.py, title: file composite tools/revalidate.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/8013f604-8091-4bcf-aa5e-9a4a96aa15f1, https://agentic-knowledge-base.dev/id/composite/c09b8f1b-53e8-470d-b164-aa1dfa534c68, https://agentic-knowledge-base.dev/id/composite/f6f22e05-67fd-4351-a17e-d9abe0817b50, https://agentic-knowledge-base.dev/id/composite/a0ecc169-b26e-47aa-b280-454b96a75c1f]}
---
**파일** — `tools/revalidate.py` 다. 449줄 · 최상위 정의 16개 · 최상위 절 4개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""재검증 후보 — 본문 해시가 바뀐 청크의 링크와 하류 의존자를 재판정 대상으로 보고한다 (dependency-graph-design §5, method §7).

본문(frontmatter 제외)의 contentHash 가 base 리비전과 다르면 그 IRI 에 붙은 링크는 suspect 후보이고 재검증 시점에서
재판정한다 — 링크 부패 규칙(p10 link decay)의 첫 형태. 해시는 tools/chunk2kg.py 의 parse_chunk 를 그대로 써서
head 그래프의 agt:contentHash 와 같다. 재판정 대상은 다섯 갈래를 합친다:
  (a) frontmatter 링크의 상대 — refines·serves·supersedes·verifies·assumes·part_of (+ satisfies·constrains·derivesFrom·allocates·
      coUpdatesWith·overlapsWith), 양방향
  (b) Bazel 하류 의존자 — bazel query rdeps(<universe>, <타깃>) 의 kb_chunk·kb_decision (직접 / 전이)
  (c) **호출부** — 본문 해시가 바뀐 정의 청크를 `uses`(agt:usesDefinition)로 가리키는 출발점. 그 수가 **코드 호출부
      파손의 상한**이다: 같은 모듈의 최상위 이름 참조와 치역 경계(defs/kb.bzl 의 USES_TARGETS — 2026-10-01 표본 쌍은
      `kb_lib` 하나다) 안의 모듈 간 참조를 세므로, 경계 밖의 모듈을 치역으로 하는 호출은 여기 들어오지 않고 실제
      파손은 이 수보다 크다 (유저 답 2026-09-30·2026-10-01, 채널 uses-definition·uses-definition-range).
      링크 개체가 아니라 직접 트리플이므로 (d) 의 표에는 오르지 않는다
  (d) **링크 개체** — 본문 해시가 바뀐 청크를 양 끝 중 하나로 갖는 agt:Link 의 IRI. 그 링크가 suspect 로 유도되는 자리다.
      IRI 는 chunk2kg 와 같은 함수(link_hash × work_id)로 계산하므로 head 그래프의 링크 개체와 같은 것이다 — 그래서 이 보고의
      한 줄이 그래프의 한 개체를 가리킨다. 상태는 저장하지 않는다 (노트 9.11절): suspect 는 여기서 물질화된다.
**정체성은 uuid(frontmatter `id`)이고 경로는 주소다** (p10-split-keeps-work-identity · p10-function-identity-registry).
그래서 base 와 워킹트리를 uuid 로 맞춘다 — 경로로 비교하면 개명·이동이 "삭제 + 신규" 로 보여 재판정 대상이 부풀고 링크가
깨진 것처럼 읽힌다. 경로가 바뀐 것은 **라벨 변경**으로 보고한다. 하류 조회의 타깃 라벨은 `gen_build` 의 `iri_to_label`
에서 온다 — 복합체 묶음 뒤에는 부분마다의 개별 타깃이 없으므로 경로에서 라벨을 지어내면 rdeps 가 늘 0 이다.

git 과 bazel query 를 부르므로 odd_check 처럼 테스트 타깃이 아니다. 판정은 사람/승인된 판정자의 몫이다.
**스냅숏 비교** (유저 답 Q38-c): `--base-dir <d1> --head-dir <d2>` 는 git 리비전 대신 디렉토리 둘(아래의 `*.md` 전부)을, `--base-files`·
`--head-files` 는 파일 목록 둘을 uuid 로 맞춰 같은 재판정 대상을 낸다. git 도 `bazel query` 도 부르지 않으므로 (c)의 하류 의존자는
비고 읽기 전용이다 — V&V 케이스 실행기(`vv_run`)의 허용 목록이 받는 꼴이 이것이다. 파일 목록은 주소가 아니라서 경로 변경을 보고하지 않는다.

사용: bazel run //tools:revalidate -- [--base HEAD] [--universe '//...'] [--out report.md]
      python3 tools/revalidate.py --base-dir <d1> --head-dir <d2> [--out report.md]
      python3 tools/revalidate.py --base-files <f…> --head-files <f…> [--out report.md]
종료: 0 = 변경 없음(재판정 대상 없음), 1 = 재판정 대상 있음, 2 = 입력 문제(스냅숏 한쪽만 · 없는 경로 · 값 어휘)
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile
from collections import defaultdict
from pathlib import Path
```
<!-- 인용 끝 -->
