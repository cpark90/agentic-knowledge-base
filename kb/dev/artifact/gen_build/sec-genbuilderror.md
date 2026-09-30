---
id: https://agentic-knowledge-base.dev/id/chunk/d19e28ff-8c1f-4b0b-844f-86988512852f
type: artifact
level: executable
title_ko: 절 genbuilderror (tools/gen_build.py)
title: section genbuilderror in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/047c5c56-2b6c-4f8b-993e-32f3a35fd1d6, https://agentic-knowledge-base.dev/id/chunk/28655d6b-d000-4f43-8d68-9e0ce042c39c, https://agentic-knowledge-base.dev/id/chunk/4962e5fe-9d28-4f18-b054-95670b51808e]
part_of: https://agentic-knowledge-base.dev/id/composite/5d2c4208-d2d8-45df-b4a3-1931a6c56dfd
composite: {id: https://agentic-knowledge-base.dev/id/composite/5d2c4208-d2d8-45df-b4a3-1931a6c56dfd, title_ko: 절 복합체 genbuilderror (tools/gen_build.py), title: section composite genbuilderror in tools/gen_build.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/d19e28ff-8c1f-4b0b-844f-86988512852f, https://agentic-knowledge-base.dev/id/chunk/04bfcfb9-d96b-42ec-9555-a58bd09f1551, https://agentic-knowledge-base.dev/id/chunk/be13ce99-9dc5-4abe-8367-5558f1aa4b02, https://agentic-knowledge-base.dev/id/chunk/a8f6816d-512e-4fb2-8bce-765ddee8bf42, https://agentic-knowledge-base.dev/id/chunk/0f0f082a-c9cd-454c-ab65-ca4f3bebc461, https://agentic-knowledge-base.dev/id/chunk/ad68f79e-bbb2-4a80-b6c8-518fdd88a3a2], part_of: https://agentic-knowledge-base.dev/id/composite/9bb41e68-1b5c-4d4c-aee0-32a2899bedf9}
---
**절** — `tools/gen_build.py` 의 절 `genbuilderror` 다. 청크 읽기와 항목 수집

**정의** — `GenBuildError` · `parse_item` · `q` · `label_list` · `scan` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 청크 읽기와 항목 수집 ────────────────────



HEADER ="# 생성 파일 — 손으로 고치지 않는다. 원본은 각 청크의 frontmatter (tools/gen_build.py). 검사: //:build_drift_test\n"
LINKS = ("refines", "serves", "supersedes", "verifies")
ONTO_BASE = "https://agentic-knowledge-base.dev/ontology/"
MEMORY_PKG = "kb/dev/memory"  # 관측 패키지 — 비어 있어도 BUILD 는 생성한다 (//kb/dev:bodies·//kg:chunks_kg 의 끝점)
# 추출된 코드 청크 (p7-code-extraction-direction) — 소스 파일 하나 = 패키지 하나다. 패키지 이름은 소스의 stem 이고
# 그 안의 청크 전부는 tools/extract.py 의 생성물이다(손으로 고치면 //:extract_drift_test 가 거부한다). 묶음은 중첩
# 복합체이므로 뿌리(파일 복합체)를 선언한 `module.md` 가 타깃 이름이 된다. 경로 접두는 kb_lib.EXTRACT_ROOT 와 같다 —
# 이 도구는 rdflib 없이 돌므로 VV_ROOT 와 같은 사유로 자체 상수를 갖는다
ARTIFACT_ROOT = "kb/dev/artifact"
# V&V KB — 코어의 두 번째 인스턴스 (p8-vv-plane-instances): 디렉토리 = plane 실체 (pe-storage-layout 의 vv/ 번들). 패키지마다 kb_chunk 타깃,
# 비어 있어도 BUILD 는 생성한다. 편집은 vnv 만(kg/catalog-kg.ttl agt:writesIn "kb/vv"), verifies 링크만 KB 를 가로지른다 (defs/kb.bzl).
# 경로 접두는 kb_lib.KB_VV 와 같다 — 이 도구는 rdflib 없이 돌므로 자체 상수로 둔다
VV_ROOT = "kb/vv"
VV_PKGS = {"goal": "requirement", "scenario": "decision", "criteria": "contract", "case": "schema", "verifier": "artifact",
           "verdict": "annotation", "run": "memory"}
SCENARIO_PKG = f"{VV_ROOT}/scenario"  # 시나리오 실체의 패키지 — 역할 접미 규약이 걸리는 자리다
# 시나리오 세 청크의 파일 접미 — 정의처는 kb_lib.SCENARIO_ROLE_MARKERS 의 키이고 이 도구는 rdflib 없이 돌아 kb_lib 를
# 의존할 수 없으므로 VV_ROOT 와 같은 사유로 자체 상수를 갖는다. 표지 낱말(자극·요인·배제 자극)은 게이트 `decision-role` 의 몫이다
SCENARIO_ROLE_SUFFIXES = ("stimulus", "factors", "excluded")
# 결정 복합체의 읽기 순서 — 결론 없이 근거를 읽지 않고 대안은 결론을 전제한다. 이것을 생성기가 `ordered` 인자로 **선언**하고
# chunk2kg 는 추측하지 않는다 (유저 승인 2026-09-29, p4-composite-order-is-declared). ADR 뷰(weave)의 조립 순서와 같다
DECISION_READING_ORDER = ("conclusion", "rationale", "alternatives")
# 키는 plane 이름이 아니라 실체 이름이다 — verdict = 판정 주석 (p8-vv-plane-instances 의 annotation 실체). `verdict` 는
# kb_lib.RUN_VERDICTS(pass·fail·skip)가 이미 쓰는 낱말이라 지어낸 용어가 아니다 (STYLEGUIDE §0 표준어 우선).
# run = 실행 기록 (agt:Run, append-only) — vv_run --record 가 만든다 (kb_lib.VV_RUN_DIR)










MAX_PARTS = 9  # 직접 부분의 상한 (7±2, 4.5절) — defs/kb.bzl 의 MAX_PARTS·composite-shapes.ttl 과 같은 수
```
<!-- 인용 끝 -->
