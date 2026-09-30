---
id: https://agentic-knowledge-base.dev/id/chunk/ec5b3c44-34a9-4f02-be75-c71bae837f4d
type: artifact
level: executable
title_ko: 파일 tools/space2kg.py
title: file tools/space2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-space2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/7c9d74e6-1a77-4d52-a126-644a65bfab93, https://agentic-knowledge-base.dev/id/chunk/828f6e56-8841-4778-94b7-fe42d706243f, https://agentic-knowledge-base.dev/id/chunk/5b6ac70d-af5e-48ed-8e23-c7a66921493f]
composite: {id: https://agentic-knowledge-base.dev/id/composite/89a47e26-d93e-47e7-ae74-ba6e801d1d5a, title_ko: 파일 복합체 tools/space2kg.py, title: file composite tools/space2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/06619efb-02eb-4124-9d89-7e2245f5d90c, https://agentic-knowledge-base.dev/id/composite/fc3f9858-3941-435d-b741-071b871ce613, https://agentic-knowledge-base.dev/id/composite/2716ece9-44f6-48ff-b2ab-1ad0ea6fa6c0]}
---
**파일** — `tools/space2kg.py` 다. 297줄 · 최상위 정의 7개 · 최상위 절 3개이고 이 청크는 추출 생성물이다. 링크와 가정의 자리가 이 파일 복합체다.

**모듈 머리** — 모듈 docstring 과 import 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
#!/usr/bin/env python3
"""설계 공간 청크(`-space`) → 설계 공간 그래프(`*-space.ttl`) 생성.

설계 변수 하나가 파일 하나다. 후보 링크는 확정 링크와 **다른 자리**에 저장된다 — 확정은 청크 head(frontmatter
링크 키 → Bazel deps), 후보는 `-space` 청크다. **후보는 결코 deps 가 되지 않는다**: 이 생성기는 `kb_chunk` 타깃을
만들지 않고 A-Box 그래프만 내며, 그 그래프는 `//kg:gate_test` 의 `--data` 로 들어가 통제 어휘·SHACL·안티패턴
질의·`check_space` 의 판정을 받는다 (결정 p9-candidate-storage · p9-design-space-file).

frontmatter 는 청크와 같고(`tools/chunk2kg.py` 의 REQUIRED) `type: agt:Space` · `level: logical` 이다.
본문은 언어 태그 `yaml` 을 단 펜스 블록 하나이고 키는 여섯이다:

  variable     {from: <출발 항목 IRI>, kind: <링크 타입>} (필수) — 미확정은 언제나 두 항목이 연결되는가의
               미확정이므로 변수는 값이 아니라 출발 항목과 링크 타입의 쌍이다 (p9-uncertainty-as-link-uncertainty)
  status       open | resolved (필수) — resolved 면 `state: confirmed` 인 후보가 정확히 하나다
  candidates   후보 목록 (선택 — abstract 단계는 variable 까지만 채운다). 항목의 키는 다섯이다:
               to(대상 IRI, 필수) · state(open|eliminated|confirmed, 필수) · when(CEL 술어, 선택) ·
               evidence(지지 증거 목록 [{kind, ref}], 선택) · eliminated_by(배제 근거 {kind, ref}, eliminated 전용·필수)
  constraints  양립 제약 CEL 술어 목록 (선택) → agt:compatibilityConstraint
  preferences  후보 사이의 부분순서 [{prefer: <IRI>, over: <IRI>}] (선택) → agt:preferredOver. 수치는 붙이지 않는다
  후보의 표면 상태는 링크 상태의 기존 값으로 내린다 (kb_lib.SPACE_STATE_LINK) — open 은 agt:CandidateLink 와
  linkState candidate, eliminated 는 linkState invalid, confirmed 는 agt:ConfirmedLink 와 linkState confirmed 다.
  배제 근거·지지 증거는 증거 기록 한 줄(agt:Evidence)로 나가고 극성은 배제가 `-`, 지지가 `+` 다. 기각된 후보는
  지우지 않는다 — logical 은 근거의 보존소이고, 확정되는 순간 후보가 head 로 옮겨져 한 줄 diff 로 리뷰된다.

출력·종료: 위반은 `FAIL [space] <경로>: <메시지>` + EXIT_FAIL, 읽을 수 없는 입력은 EXIT_CONFIG.
           생성기이므로 입력 0건은 빈 그래프다 (SKIP 아님).
사용: space2kg.py --out <생성.ttl> <-space 청크…>   (bazel build //space:design_space)
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

import yaml
```
<!-- 인용 끝 -->
