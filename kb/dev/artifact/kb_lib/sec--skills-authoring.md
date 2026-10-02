---
id: https://agentic-knowledge-base.dev/id/chunk/ac500e24-d795-4cb2-9409-433d7e56a013
type: artifact
level: executable
title_ko: 절 -skills-authoring (tools/kb_lib.py)
title: section -skills-authoring in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/624bc78e-4e6c-4b96-b0f7-e9c6f5087b46
composite: {id: https://agentic-knowledge-base.dev/id/composite/624bc78e-4e6c-4b96-b0f7-e9c6f5087b46, title_ko: 절 복합체 -skills-authoring (tools/kb_lib.py), title: section composite -skills-authoring in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/ac500e24-d795-4cb2-9409-433d7e56a013, https://agentic-knowledge-base.dev/id/chunk/104f7d3c-d114-46c9-aab7-b44761117813], part_of: https://agentic-knowledge-base.dev/id/composite/2fee8437-c9b3-4f23-a1d9-a0ec5e3891b0}
---
**절** — `tools/kb_lib.py` 의 절 `-skills-authoring` 다. 생성 skill — 저작·검증 도구의 표 (앞 절의 이어지는 블록)

**정의** — `label_of` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 생성 skill — 저작·검증 도구의 표 (앞 절의 이어지는 블록) ────────────────────
# 표를 둘로 나눈 까닭은 하나였을 때 절 청크가 `artifact` 상한(2,856 토큰)을 넘었기 때문이다
# (결정 p1-chunk-unit-is-tokens 의 분할). 표의 순서가 skill 의 순서이므로 두 블록을 **이어 붙인**
# `SKILLS` 가 여전히 단일 정의처다 — 생성물의 바이트는 나누기 전과 같다.
_SKILLS_AUTHORING = (  # 저작·검증 — 추출·BUILD·링크 복원·V&V 실행·판정·문서 뷰·생성 문서·문서 현행성·토큰
    {"tool": "extract", "section": "method.md#3-청크-저작",
     "when": "소스 파일을 고친 뒤 `artifact` plane 의 함수·절·파일 청크를 다시 추출하고 등록부의 개명·신설·삭제를 맞출 때 쓴다.",
     "commands": ["bazel run //tools:extract -- tools/kb_lib.py", "bazel test //:extract_drift_test",
                  "python3 tools/gen_build.py --root . && bazel test //..."]},
    {"tool": "gen_build", "section": "method.md#6-연결",
     "when": "청크를 추가·삭제하거나 frontmatter 링크(refines·serves·supersedes·verifies)를 고친 뒤 BUILD 를 재생성하고 드리프트를 검사할 때 쓴다.",
     "commands": ["python3 tools/gen_build.py --root .", "python3 tools/gen_build.py --check --root .", "bazel test //:build_drift_test"]},
    {"tool": "link", "section": "method.md#6-연결",
     "when": "frontmatter 링크가 없는 청크 쌍의 복원 후보를 체계 안 증거(본문 인용·테스트 공동 커버·개념 공유)로 뽑아 사람이 restored 표시로 확정할 때 쓴다.",
     "commands": ["bazel build //kg:link_candidates && cat bazel-bin/kg/link-candidates.md",
                  "python3 tools/gen_build.py --root . && bazel test //...   # 앵커 청크에 링크 키와 restored: 를 적은 뒤"]},
    {"tool": "vv_run", "section": "method.md#11-검증--vv-층으로",
     "when": "V&V 케이스의 허용 목록 명령(읽기 전용 검증기 열 — `assume_check` 포함, `--record`·저장소 안 `--out` 은 SKIP)을 "
             "실행해 케이스의 기대(종료 코드·문구)와 대조하고 pass·fail·skip 을 판정해 실행 기록(kb/vv/run/, append-only)을 남길 때 쓴다.",
     "commands": ["bazel run //tools:vv_run -- --record", "bazel run //tools:vv_run -- --case <슬러그>",
                  "python3 tools/gen_build.py --root . && bazel test //..."]},
    {"tool": "judge", "section": "method.md#11-검증--vv-층으로",
     "when": "게이트 밖에서 등록된 판정 질문을 청크에 물어 값과 확신도를 받고 판정 로그·결과 주석을 남길 때 쓴다. "
             "판정자는 외부 서비스가 아니라 세션 판정자다 — 응답은 `--responses`로 오프라인 입력한다.",
     "commands": ["bazel run //tools:judge -- --list",
                  "bazel run //tools:judge -- --question labelRepresentsBody --responses r1.json --record <청크 파일…>",
                  "bazel run //tools:judge -- --question bodyHasOneClaim --responses r1.json --responses r2.json "
                  "--decoys key.json --into /tmp/judge <청크 파일…>"]},
    {"tool": "weave", "section": "method.md#9-뷰",
     "when": "결정 기록·요구 색인·변경 이력·감사 보고서를 저장하지 않고 그래프와 관측에서 생성해 인용할 때 쓴다.",
     "commands": ["bazel build //kg:audit && cat bazel-bin/kg/audit.md", "bazel build //kb/dev:adr //kb/dev:requirements //kb/dev:changelog"]},
    {"tool": "gendoc", "section": f"tools.md#{GATE_CATALOGUE_ANCHOR}",
     "when": "생성기를 고친 뒤 생성 문서의 머리 블록·표·목차·링크·비율 표기가 규약 G1~G18 안인지 게이트와 같은 방식으로 검사할 때 쓴다.",
     "commands": ["bazel test //:gendoc_test",
                  "bazel run //tools:gendoc -- bazel-bin/kg/metrics.md bazel-bin/kb/dev/index.md"]},
    {"tool": "doccheck", "section": f"tools.md#{GATE_CATALOGUE_ANCHOR}",
     "when": "문서를 고친 뒤 죽은 링크·앵커·백틱 경로·산문 문체를 게이트와 같은 방식으로 검사할 때 쓴다.",
     "commands": ["bazel run //tools:doccheck -- *.md docs/*.md docs/open-questions/*.md --target-only docs/agent-knowledge-system-notes.md",
                  "bazel test //:doccheck_test"]},
    {"tool": "tokens", "section": "rules.md#1-chunk--자립적-최소-지식-단위",
     "when": "청크가 상한(저작 산문 1,092 · 인용 2,856)에 얼마나 가까운지 보거나 분할 대상을 고를 때 쓴다 — plane 별 "
             "분포·42의 배수별 초과 수·컨텍스트 예산의 환산·상위 20 청크를 고정된 어휘로 낸다.",
     "commands": ["bazel run //tools:tokens", "bazel run //tools:tokens -- --out /tmp/tokens.md",
                  "bazel run //tools:tokens -- kb/dev/decision/<결정>/conclusion.md"]},
)
SKILLS = _SKILLS_READING + _SKILLS_AUTHORING
```
<!-- 인용 끝 -->
