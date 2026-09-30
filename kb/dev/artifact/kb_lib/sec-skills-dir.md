---
id: https://agentic-knowledge-base.dev/id/chunk/24795977-8003-4c34-8e0c-6aed3c366fda
type: artifact
level: executable
title_ko: 절 skills-dir (tools/kb_lib.py)
title: section skills-dir in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/cfe0afad-9ee7-4e4c-9283-5fddef1781ff
composite: {id: https://agentic-knowledge-base.dev/id/composite/cfe0afad-9ee7-4e4c-9283-5fddef1781ff, title_ko: 절 복합체 skills-dir (tools/kb_lib.py), title: section composite skills-dir in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/24795977-8003-4c34-8e0c-6aed3c366fda, https://agentic-knowledge-base.dev/id/chunk/104f7d3c-d114-46c9-aab7-b44761117813], part_of: https://agentic-knowledge-base.dev/id/composite/2fee8437-c9b3-4f23-a1d9-a0ec5e3891b0}
---
**절** — `tools/kb_lib.py` 의 절 `skills-dir` 다. 생성 skill (gen_skills — agrtls K "skill 은 손으로 쓰지 않고 지식·절차에서 생성한다", 로드맵 6단계)

**정의** — `label_of` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 생성 skill (gen_skills — agrtls K "skill 은 손으로 쓰지 않고 지식·절차에서 생성한다", 로드맵 6단계) ──────────────────
# 어떤 도구를 skill 로 내는가와 그 절차의 원본 절은 이 표가 단일 정의처다. 본문(무엇·언제·사용법)은 도구 모듈의 docstring 이
# 원본이고, 생성기(tools/gen_skills.py)가 둘을 합쳐 .claude/skills/<도구-kebab>/SKILL.md 를 트리에 쓴다. 생성물은 BUILD 와
# 같은 이유로 커밋 대상이며(도구 없이도 skill 이 읽혀야 한다) //:skills_drift_test 가 재생성과 비교한다.
#   tool      tools/<tool>.py 이며 tools/BUILD.bazel 에 같은 이름의 py_binary 가 있어야 한다
#   section   원본 절 — docs/ 아래 문서 `<파일>#<GitHub 앵커>`. 생성기가 앵커 실재를 검사한다
#   when      언제 쓰는가 한 문장(단정 서술형) — skill frontmatter 의 description
#   commands  대표 명령 1~3
SKILLS_DIR = ".claude/skills"
SKILLS_DRIFT_GATE = "skills-drift"  # 게이트 id — FAIL [skills-drift]
GEN_SKILLS_GATE = "gen-skills"      # 생성 시점 거부 — FAIL [gen-skills]
SKILLS = (
    {"tool": "workset", "section": "method.md#8-조회",
     "when": "dispatch 전에 역할·수준 창·앵커로 거른 작업 집합(라벨 목록과 이웃 본문)을 컨텍스트 예산 안에서 뽑을 때 쓴다.",
     "commands": ["bazel build //kg:workset --//kb:role=developer --//kb:anchor='<라벨|IRI>' --//kb:levels=concrete",
                  "cat bazel-bin/kg/workset-developer.md"]},
    {"tool": "query", "section": "method.md#8-조회",
     "when": "역량 질문(CQ)의 답을 그래프에서 라벨 목록으로 얻거나 한 항목이 무엇을 가리키는지 SPARQL 로 확인할 때 쓴다.",
     "commands": ["bazel run //tools:query", "bazel run //tools:query -- CQ-07 --labels",
                  "bazel run //tools:query -- CQ-19 --labels --bind '?x=<IRI|id:슬러그|라벨>'"]},
    {"tool": "impact", "section": "method.md#12-영향-분석",
     "when": "청크·결정을 고치기 전에 영향 항목 수·plane 분포·suspect 가 될 링크 수·승인이 필요한 결정 수를 계산할 때 쓴다.",
     "commands": ["bazel run //tools:impact -- //kb/dev/requirement:<타깃>", "bazel run //tools:impact -- //kb/dev/decision:<결정> --universe //kb/..."]},
    {"tool": "assume_check", "section": "method.md#7-갱신",
     "when": "가정을 ODD 조건으로 판정해 깨진 가정의 직접 영향 집합과 suspect 후보를 내거나 --break 로 인위 파괴 실험을 할 때 쓴다.",
     "commands": ["bazel run //tools:assume_check", "bazel run //tools:assume_check -- --break cond-build-system",
                  "bazel run //tools:assume_check -- --record && python3 tools/gen_build.py --root ."]},
    {"tool": "revalidate", "section": "method.md#7-갱신",
     "when": "청크 본문을 고친 뒤 base 리비전 대비 재판정 대상(링크 상대·복합체 형제·하류 의존자)을 표로 낼 때 쓴다.",
     "commands": ["bazel run //tools:revalidate -- --base HEAD", "bazel run //tools:revalidate -- --base <rev> --out /tmp/revalidate.md"]},
    {"tool": "odd_check", "section": "method.md#2-odd-작성",
     "when": "세션 시작이나 환경 변경 뒤에 실제 조건이 ODD 안인지 CHECKS 명령으로 판정해 이탈을 보고할 때 쓴다.",
     "commands": ["bazel run //tools:odd_check", "bazel run //tools:odd_check -- --out /tmp/odd-check.md"]},
    {"tool": "endorse", "section": "method.md#13-저작-흐름과-완료",
     "when": "쓰기 권한 역할이 검토를 마친 청크에 verified 를 붙여 writer 검사를 해소할 때 쓴다.",
     "commands": ["bazel run //tools:endorse -- --by orchestrator/<모델> --at <ISO 8601> <청크 파일…>"]},
    {"tool": "term_propose", "section": "method.md#10-일반화",
     "when": "관측에서 뽑은 개념 후보를 검사를 거쳐 온톨로지 승인 큐(kb/ontology/proposals/)에 제안할 때 쓴다.",
     "commands": ["bazel run //tools:term_propose -- --id <slug> --kind class --parent agt:<상위> --label-ko '<한글>' --label-en '<english>' --definition '<속+종차>' --cq CQ-NN"]},
    {"tool": "consistency", "section": "method.md#9-뷰",
     "when": "커밋 전에 중복·라벨 형식·용어 옛 표기·단정성(추측·구어·대시 밀도)·첨가(메타 문장·채움·빈 값 이상 표기)·목록 규칙 후보를 보고로 확인할 때 쓴다.",
     "commands": ["bazel build //kb:consistency && cat bazel-bin/kb/consistency.md"]},
    {"tool": "open_questions", "section": "method.md#9-뷰",
     "when": "무엇이 아직 미결인지 — 청크의 선택 슬롯 `미확정:` 에 든 질문과 그것을 안은 청크를 문서에 적지 않고 집계에서 인용할 때 쓴다.",
     "commands": ["bazel build //kg:open && cat bazel-bin/kg/open.md"]},
    {"tool": "choices", "section": "method.md#5-후보-관리",
     "when": "무엇을 아직 고르지 않았는가 — 열린 설계 변수와 그 후보를 체크박스(`[ ]` 열림 · `[-]` 배제 + 근거 · `[x]` 확정)로 확인할 때 쓴다.",
     "commands": ["bazel build //space:choices && cat bazel-bin/space/choices.md"]},
    {"tool": "metrics", "section": "method.md#완료-판정",
     "when": "고아율·CQ19·CQ20 커버리지·도입 단계 통과 조건 같은 수치를 문서에 적지 않고 생성물에서 인용할 때 쓴다.",
     "commands": ["bazel build //kg:metrics && cat bazel-bin/kg/metrics.md"]},
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
    {"tool": "gendoc", "section": "tools.md#게이트-총람--이-문서가-원본이다",
     "when": "생성기를 고친 뒤 생성 문서의 머리 블록·표·목차·링크·비율 표기가 규약 G1~G18 안인지 게이트와 같은 방식으로 검사할 때 쓴다.",
     "commands": ["bazel test //:gendoc_test",
                  "bazel run //tools:gendoc -- bazel-bin/kg/metrics.md bazel-bin/kb/dev/index.md"]},
    {"tool": "doccheck", "section": "tools.md#게이트-총람--이-문서가-원본이다",
     "when": "문서를 고친 뒤 죽은 링크·앵커·백틱 경로·산문 문체를 게이트와 같은 방식으로 검사할 때 쓴다.",
     "commands": ["bazel run //tools:doccheck -- *.md docs/*.md docs/open-questions/*.md --target-only docs/agent-knowledge-system-notes.md",
                  "bazel test //:doccheck_test"]},
)
```
<!-- 인용 끝 -->
