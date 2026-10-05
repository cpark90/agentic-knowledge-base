---
id: https://agentic-knowledge-base.dev/id/chunk/e8380930-b5fb-496b-bd8a-5c1baa7c9ea3
type: artifact
level: executable
title_ko: 절 extracted-sources (defs/kb.bzl)
title: section extracted-sources in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9a583117-c61c-48f7-b30a-f60bddda9bfe
---
**절** — `defs/kb.bzl` 의 절 `extracted-sources` 다. 추출 경계와 생성 표 — 코드 청크의 방출·치역 경계, 생성 뷰와 규범 문서의 목록

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
# ── 추출 경계와 생성 표 — 코드 청크의 방출·치역 경계, 생성 뷰와 규범 문서의 목록 ────────────────────────
# 추출 대상 소스 모듈 — tools/<이름>.py 에 등록부 사이드카(<이름>.chunks.yml)가 있는 소스 전부(코드를 청크로,
# p7-code-extraction-direction). **단일 정의처**(M1, 2026-10-01 — RESIDENCY 와 같은 해법): 여기 말고 어디에도
# 이 목록을 손으로 적지 않는다. `BUILD.bazel` 은 이 리터럴을 load 해 추출 드리프트 테스트를 세우고,
# `tools/kb_lib.py` 의 `load_extracted_sources`(ast.literal_eval)가 `uses`(agt:usesDefinition) 방출 경계
# USES_SOURCES 를 이 값에서 파생한다 — 상수 둘을 두지 않는다. 이름에 `.py` 접미사를 붙이지 않는다(각 소비자가
# 필요한 모양으로 붙인다). 더하거나 빼려면 등록부 사이드카의 존재와 이 목록을 같은 커밋에서 맞춘다 — 갈리면
# `BUILD.bazel` 의 소스 존재 확인(`glob` 대조, 로드 시점)이 바로 죽는다.
EXTRACTED_SOURCES = [
    "assume_check",
    "canonicalize",
    "case_gen",
    "channel_lint",
    "choices",
    "chunk2kg",
    "chunk_lint",
    "community",
    "consistency",
    "doccheck",
    "endorse",
    "extract",
    "extract_refs",
    "gates2kg",
    "gen_build",
    "gen_norms",
    "gen_skills",
    "gendoc",
    "handoff",
    "impact",
    "judge",
    "kb_lib",
    "label_sample",
    "labels",
    "link",
    "metrics",
    "odd2kg",
    "odd_check",
    "open_questions",
    "query",
    "revalidate",
    "run_evidence",
    "space2kg",
    "stamp",
    "taxonomy",
    "term_propose",
    "tokens",
    "validate",
    "vv_run",
    "vv_run_env_test",
    "weave",
    "workset",
]

# 추출 대상 질의 디렉토리 — tools/<이름>/*.rq 의 SPARQL 질의 파일 하나가 `artifact` 청크 하나다(2단계 편입, 2026-10-03:
# //kg:cq 뷰의 내용 원본인 역량 질문 질의와 //kg:gate_test 의 검증 질의가 코드 청크 밖에 있었다). 방향은
# EXTRACTED_SOURCES 와 같다(p7-code-extraction-direction) — 질의 파일이 원본이고 청크는 `tools/extract.py` 의 생성물이며,
# 정체성은 디렉토리 옆의 등록부 사이드카(`tools/<이름>.chunks.yml`, 파일 이름 → uuid)가 준다(p10-function-identity-registry).
# **단일 정의처**다(M1): `BUILD.bazel` 이 이 리터럴로 추출 드리프트 테스트(게이트 id `extract-drift`)를 세우고,
# `tools/extract.py` 가 `kb_lib.load_extracted_sources(…, EXTRACTED_QUERY_DIRS)` 로 읽어 디렉토리 소스를 허용한다.
# 등록부 사이드카의 존재와 이 목록·EXTRACTED_SOURCES 의 합이 같은 집합인지는 `check_extracted_sources` 가 본다.
EXTRACTED_QUERY_DIRS = [
    "cq-queries",
    "verify-queries",
]

# 추출 대상 Starlark 소스 — defs/<이름>.bzl 의 최상위 정의 하나가 `artifact` 청크 하나다(유저 답 Q32-a, 2026-10-04: 요구
# r-010·r-022·r-023 을 강제하는 코드가 이 파일의 `_check_links` 등에 있는데 코드 청크 밖이었다). 방향과 청크 모양은
# EXTRACTED_SOURCES 와 같다(p7-code-extraction-direction — 소스가 원본, 최상위 정의 = 정의 청크, 절 주석 = 절 복합체).
# 등록부 사이드카는 소스 옆의 `defs/<이름>.chunks.yml` 이고 생성 패키지는 `kb/dev/artifact/<이름>-bzl` 이다.
# **규칙을 강제하는 코드가 든 파일만** 넣는다 — 입력 집합과 인자의 배선만 하는 파일(`defs/knowledge.bzl`)은 항목이
# 아니다(유저 답 Q10-a). 한 파일 안의 배선 정의는 등록부의 `wiring` 목록이 추출에서 뺀다. **단일 정의처**다(M1):
# `BUILD.bazel` 이 이 리터럴로 추출 드리프트 테스트(게이트 id `extract-drift`)를 세우고, `tools/extract.py` 가
# `kb_lib.load_extracted_sources(…, EXTRACTED_STARLARK)` 로 읽어 `.bzl` 소스를 허용한다. 등록부 사이드카의 존재와 이
# 목록이 같은 집합인지는 `check_extracted_starlark`(`defs/BUILD.bazel`)가 로드 시점에 본다.
EXTRACTED_STARLARK = [
    "kb",
]

# 생성 뷰 — 그래프·청크에서 생성하는 마크다운 Bazel 타깃의 **단일 정의처**(M1, 2단계 편입 2026-10-03). 전에는 같은 목록이
# 손 목록 넷(`//:gendoc_test` 의 `docs` · 그 주석 · `docs/tools.md` 의 두 자리)으로 갈려 개수가 서로 어긋났다.
# 소비자는 `BUILD.bazel` 의 `//:gendoc_test`(생성 문서 형태 게이트의 입력)이고, 문서는 개수를 적지 않고 이 목록을 가리킨다.
# 생성 skill(.claude/skills)은 트리 파일이라 여기 넣지 않는다 — 원본은 `kb_lib.SKILLS` 다. 뷰를 더하거나 빼려면 여기만 고친다.
# 값은 그 뷰를 내는 생성 도구(`tools/<도구>.py`)다 — 뷰는 층의 항목이 아니라 그 도구의 `module` 코드 청크의 **투영**이고
# (`agt:View`, `prov:wasDerivedFrom`, 결정 p0-service-is-a-three-layer-wiki · 유저 답 Q9-a) `//kg:projections_kg` 가 이 표로
# 개체를 낸다. 소비자는 키 목록(`list(VIEWS)`)을 쓴다.
VIEWS = {
    "//kb:consistency": "consistency",
    "//kb/dev:adr": "weave",
    "//kb/dev:changelog": "weave",
    "//kb/dev:index": "labels",
    "//kb/dev:requirements": "weave",
    "//kg:audit": "weave",
    "//kg:communities": "community",
    "//kg:cq": "query",
    "//kg:link_candidates": "link",
    "//kg:metrics": "metrics",
    "//kg:open": "open_questions",
    "//kg:workset": "workset",
    "//space:choices": "choices",
}

# 규범 문서 — 절 청크(`norm` plane)와 결정의 규약 줄에서 생성하는 소스 트리 파일의 **단일 정의처** (M1, 결정
# p12-norm-documents-from-section-chunks, 유저 답 Q19-b). 키는 문서 stem 이고 절 청크 디렉토리 `kb/dev/norm/<stem>/` 의 이름이며,
# 값은 생성 파일의 저장소 상대 경로다. 소비자는 넷이다 — `BUILD.bazel` 의 `//:norms_drift_test`(재생성 바이트 비교)와
# `//:gendoc_test`(생성 문서 형태, `norm_doc_labels`)·`//:build_drift_test`(문서별 생성 BUILD) · `tools/gen_norms.py`(리터럴
# 읽기 — 디렉토리 집합과 키 집합이 갈리면 FAIL [gen-norms]). `VIEWS` 와 다른 까닭은 생성물이 bazel-bin 이 아니라 소스 트리에
# 있다는 것이다(`.claude/skills` 와 같은 생성 트리 파일). 하위 디렉토리의 문서(`docs/rules.md`)는 그 패키지가
# `exports_files` 로 내놓아야 라벨이 선다. 값에 주석(`#`)을 쓰지 않는다 — 파서가 주석을 지운 뒤 리터럴로 읽는다.
NORM_DOCS = {"AGENTS": "AGENTS.md", "STYLEGUIDE": "STYLEGUIDE.md", "method": "docs/method.md", "rules": "docs/rules.md"}


# `uses`(agt:usesDefinition) 의 **치역 경계** — 모듈 밖에서 가리킬 수 있는 대상 모듈 (유저 답 1, 2026-10-01,
# 채널 uses-definition-range). 모듈 안 호출은 사각지대의 63%만 덮으므로(실측 739 중 모듈 간 274) 치역을
# 표본 쌍 하나에서 먼저 넓힌다 — `kb_lib` 을 치역으로 두는 모듈 간 호출이 그 대부분이다. 넓히는 일은 여기
# 이름을 더하는 것이고, 그 밖의 모듈을 치역으로 하는 호출은 방출하지 않는다. **단일 정의처**다(M1,
# EXTRACTED_SOURCES 와 같은 해법): `tools/kb_lib.py` 의 `load_extracted_sources` 가 이 리터럴을 읽어
# 추출기의 치역 경계로 쓰고, `//defs:knowledge.bzl` 이 같은 리터럴로 드리프트 테스트의 입력(대상 모듈의
# 등록부 사이드카)을 세운다. EXTRACTED_SOURCES 의 부분집합이어야 한다 — 아래 검사가 로드 시점에 강제한다.
USES_TARGETS = [
    "kb_lib",
]
```
<!-- 인용 끝 -->
