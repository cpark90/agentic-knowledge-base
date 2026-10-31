---
id: https://agentic-knowledge-base.dev/id/chunk/39112a6e-ccc9-4b3f-b3f8-1d1a8b58783c
type: artifact
level: executable
title_ko: 파일 tools/run_evidence.py
title: file tools/run_evidence.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-run-evidence}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/9deed62a-70ad-4a87-99a2-73c11e1a4453, https://agentic-knowledge-base.dev/id/chunk/c5bb1922-eb82-4b96-a49c-a46e41c239e4, https://agentic-knowledge-base.dev/id/chunk/5967869a-2c73-4666-847a-af969e7e6caf]
composite: {id: https://agentic-knowledge-base.dev/id/composite/27628b6a-73ec-4466-bb12-a1a1ae970dd7, title_ko: 파일 복합체 tools/run_evidence.py, title: file composite tools/run_evidence.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/06ff52f5-9406-4ead-8685-51db4f0cb144, https://agentic-knowledge-base.dev/id/composite/78c6c89d-58c3-43c8-8570-d8bfbac1700f, https://agentic-knowledge-base.dev/id/composite/241f90fa-0b02-4c28-a23e-8e84aecaf4da, https://agentic-knowledge-base.dev/id/composite/ed156a01-76a8-4195-b32e-c9096b040444, https://agentic-knowledge-base.dev/id/composite/a7e4d5c8-a3b3-466a-93eb-1bb3d94b2ed5, https://agentic-knowledge-base.dev/id/composite/e202036d-a930-4e1b-a919-03711832262b]}
---
**파일** — `tools/run_evidence.py` 다. 530줄 · 최상위 정의 10개 · 최상위 절 6개이고 이 단위 지식은 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""실행·동시 편집·공동 커버 → 링크의 증거 기록 (p9-evidence-ledger-with-belief 결론 "실행 증거가 특별하다", p10-link-types `satisfies`,
p10-co-edit-evidence-from-small-commits, p10-link-judgement-evidence).

검증기의 통과는 `verifies` 뿐 아니라 그것이 검증하는 `satisfies` 후보에도 실행(+)을, 실패는 실행(−)을 적는다 — V&V 결과가
개발 KB 후보의 증거로 흘러드는 유일한 경로이고 링크가 아니라 **증거 기록 항목**이라 방향 규칙(8.5절)을 깨지 않는다.
이 도구가 그 경로의 생성기다. 손으로 쓰는 링크가 아니라 생성물이며 출력은 `//kg:references_kg` 에 이어 붙는다.

후보의 양 끝은 개발 KB 의 코드 **파일 단위 지식**(파일 복합체의 선언 단위 지식, p7-code-links-on-file-composite)와 **결정 결론**이다.
`satisfies` 증거의 원천은 둘이다.

  도장  파일 단위 지식의 `verified` 에 `process:bazel-test`(kb_lib.STAMP_ACTOR)가 있으면 — 추출기가 `tested.source_hash` 가 지금
        소스와 같을 때만 내므로 살아 있는 도장이다 — 그 단위 지식이 `refines` 하는 결정 결론마다 실행(+) 한 줄. 참조는 그 파일 단위 지식이다
        (도장의 시각 `agt:verifiedAt` 이 거기 있다). 도장은 통과 뒤에만 찍히므로 도장에서 (−)는 나오지 않는다.
  실행  V&V 실행 기록(`kb/vv/run/`, generated.by `process:vv_run`)의 테스트 케이스 표 한 행마다 — 그 테스트 케이스가 `verifies` 하는 결정 결론 D 와,
        그 테스트 케이스를 돌린 검증기(같은 합격 기준을 `refines` 하는 검증기, kb_lib.case_verifiers)가 `verifies` 하는 개발 KB 파일 단위 지식
        A 의 쌍 (A, D) 에 pass 는 실행(+), fail 은 실행(−) 한 줄. 참조는 실행 기록·테스트 케이스·검증기 셋이다. skip 은 증거가 아니다
        (SKIP 은 PASS 가 아니다). 건너뛴 명령이 있는데 pass 로 적힌 행도 (+)로 읽지 않는다 — 절반만 실행한 통과다.
        **이 사슬은 generated.at 이 `CHAIN_SINCE` 이후인 실행 기록부터 적용한다** (유저 답 Q96-a). 그 앞의 실행 기록 5건은 테스트 케이스가
        검증기를 직접 가리키던 옛 구조의 기록이고 소급하지 않는다 — 실행 기록은 추가 전용이다(p0-run-is-an-append-only-memory-chunk).
        **verify 질의(구조 안티패턴 게이트)의 실패는 증거로 쓰지 않는다** — 그 질의는 위반 행의 어느 링크가 틀렸는지 정하지 못한다.

링크의 증거 둘을 더 붙인다. 둘 다 지지(+)이고 이미 확정된 링크(frontmatter)에만 붙인다 — 후보는 링크 후보 뷰(tools/link.py)가 낸다.

  동시 편집  동시 편집 관측(kb_lib.coedit_pairs — 바뀐 단위 지식 파일이 kb_lib.COEDIT_MAX_FILES 이하인 커밋의 쌍)의 두 항목을 잇는
             확정 링크에 `agt:coEditHistory`. 참조는 그 관측이다. git 은 읽지 않는다 — 관측은 `--coedit-record` 모드가 쓴다.
  공동 커버  kb_lib.co_cover 의 (검증기 W, 파일 단위 지식 A) 가 확정 링크 `verifies` W→A 이면 그 링크에 `agt:testCoverage`. 참조는 테스트 케이스들이다.

판정 증거 하나를 더 붙인다 (task 0262, Q-0061 Q145-a, p8-judge-session-agreement).

  판정  판정 로그(`kb/vv/run/judge-*.md`, generated.by `process:judge`)의 쌍 행(`대상` 이 `<앵커> ↔ <대상> · <종류>`, kb_lib.parse_pair_target)
        마다 `agt:judgement` 증거 하나 — 참조는 그 판정 로그, 극성은 값 yes 가 +, no 가 − 다(kb_lib.JUDGE_NOUL_POLARITY). 후보 링크 개체
        (`linkKind` 는 판정한 종류, `linkState "candidate"`)를 함께 낸다. 그 쌍이 이미 확정(frontmatter)이면 내지 않는다 — 판정은 사람 확인 큐를
        거르는 증거이고 확정은 사람이 판정을 본 뒤의 행위다. 확정 링크에 (−) 판정을 붙이면 verify 질의 `confirmed-with-refutation` 이 사람의
        확정을 거부한다. **판정 증거는 반박만 있어도 `invalid` 로 만들지 않는다** —
        아래 `invalid` 규칙은 실행 증거 전용이다(p9-evidence-ledger-with-belief). 행의 `입력 해시값` 이 지금 두 파일의 sha256(앵커 바이트 ∥ 대상 바이트,
        kb_lib.pair_record_fingerprint)과 다르면 낡은 판정이라 증거를 내지 않는다. 단일 항목 판정 행은 링크의 증거가 아니다.

믿음 정도를 후보 링크 곁에 싣는다 (task 0304, 요구 r-032, 설계 공간 degree-of-belief-space, Q166-a).

  믿음 정도  이 도구가 후보로 낸 링크(satisfies 후보와 판정 후보)마다 열린 계산 규칙 A·B·C 의 값을 agt:DegreeOfBelief 노드
             (값 · 계산 규칙 · 입력 증거 수, belief-ontology)로 낸다. 입력은 그 링크의 실행 증거와 판정 증거이고 낡은 판정은 들지 않는다.
             A 는 서열 가중을 극성대로 더해 [0,1]로 접은 점수, B 는 Beta(1, 1) 에 지지·반박 수를 더한 사후 평균과 분산, C 는 판정 확신도의
             평균(보정 전)이다. 값은 상태를 바꾸지 않는다 — 상태를 정하는 함수는 값을 계산하는 함수를 부르지 않고, 게이트 belief-consistency
             가 그것을 본다(Q90-a). 확정 링크와 invalid 링크에는 값을 싣지 않는다.

상태는 p9-evidence-ledger-with-belief 의 전이 규칙 그대로다. 실행(−)만 있으면 `invalid`(배제, 클래스 없음 — space2kg 와 같은 표현), (+)가
하나라도 있으면 `candidate`(agt:CandidateLink) — (+)와 (−)가 공존해도 자동 해소하지 않고 후보로 남긴다(충돌 = open + 유저 큐).
확정 제안은 내지 않는다 — 확정은 사람이 frontmatter `satisfies:` 에 적는 행위다. 그 쌍이 이미 확정이면 상태·클래스를 쓰지 않고
증거 항목만 그 링크에 붙인다(확정 링크도 증거 기록을 유지한다). 직접 트리플 `agt:satisfies` 는 내지 않는다 — 후보는 주장이 아니다.
링크 IRI 는 chunk2kg 와 같은 규칙(양 끝 뿌리 uuid 의 link_hash)이다.

출력·종료: 읽을 수 없는 입력은 `FAIL [run-evidence] <경로>: …` + EXIT_CONFIG. 실행 기록이 가리키는 테스트 케이스가 없으면 stderr 에
`info [run-evidence]` 로 세고 건너뛴다 — 실행 기록은 append-only 라 지난 테스트 케이스 이름이 남는다.
사용: run_evidence.py --out <생성.ttl> --residency defs/kb.bzl <단위 지식 파일들...>   (.md 만 읽는다)
      bazel run //tools:run_evidence -- --coedit-record   (git 에서 동시 편집 쌍을 뽑아 kb/dev/memory/obs-coedit-<UTC>.md 하나를 쓴다)
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import subprocess
import sys
import uuid
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
```
<!-- 인용 끝 -->
