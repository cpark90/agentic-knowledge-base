load("@bazel_skylib//rules:common_settings.bzl", "BuildSettingInfo")

"""지식 항목을 Bazel 타깃으로 — provider·규칙·가시성 (bazel-dependency-review B + 연결성, 2026-09-11).

원칙: 의존의 원본은 그래프(frontmatter·owl:imports)이고 BUILD는 생성물(tools/gen_build.py)이다.
Bazel이 맡는 것은 링크의 **구조** — 끝점의 존재(로드 시점), 방향(가시성·분석 시점 fail), 파급(rdeps).
링크의 **의미**(SHACL·통제 어휘·상태 전이)는 그래프 게이트(d-0157 union)가 그대로 맡는다.
"""

ChunkInfo = provider(
    doc = "지식 항목(청크 또는 복합체)이 의존자에게 내보내는 것 — 링크의 끝점은 파일이 아니라 plane·level을 아는 타깃이다.",
    fields = {
        "iri": "항목 IRI (복합체면 복합체 IRI)",
        "plane": "requirement | decision | contract | schema | artifact | annotation | memory | norm",
        "level": "functional | abstract | logical | concrete | executable (결정 복합체면 결론의 수준, 그 밖의 복합체면 부분 전부의 수준)",
        "status": "draft | stable | suspect | invalidated | deprecated",
        "srcs": "청크 파일들 (depset)",
        "parts": "복합체의 부분 IRI 목록 (청크면 빈 목록)",
    },
)

OntologyModuleInfo = provider(
    doc = "온톨로지 모듈(디렉토리)이 내보내는 것 — owl:imports 가 deps 다.",
    fields = {"iri": "모듈 IRI", "srcs": "TTL 파일들 (depset)", "imports": "가져오는 모듈의 IRI 목록"},
)

KgInfo = provider(
    doc = "타깃별 head 그래프 조각 — 청크 head·복합체 트리플의 TTL. //kg:chunks_kg 는 이 depset 의 병합이다 (바뀐 타깃만 재생성).",
    fields = {"ttl": "head TTL 조각 (depset)"},
)

# ── 값 어휘와 수준 허용표 — 분석 시점 판정과 파이썬 파생처가 함께 읽는 단일 정의처 ──────────────────────────
LEVELS = ["functional", "abstract", "logical", "concrete", "executable"]
# 5.2절 단방향 순서. `norm`(규범 문서의 절, p12-norm-documents-from-section-chunks)은 끝에 둔다 — 결정의 투영이라 어느 plane 도
# 그것을 refines 하지 않고, 그것은 위의 어느 plane 이든 refines 할 수 있다
PLANES = ["requirement", "decision", "contract", "schema", "artifact", "annotation", "memory", "norm"]
# 수준 허용표 (6.4절) 의 **단일 정의처**다 (M1 단일 정의처, 2026-09-26). 여기 말고 어디에도 표를 손으로 적지 않는다.
# Starlark 는 파일을 읽지 못하므로 분석 시점 판정에 쓰이는 이 표가 원본이고, 파이썬 쪽은 이 리터럴을 읽어 파생한다
# (`tools/kb_lib.py` 의 `load_residency`). 파생처는 셋이다 — 분석 시점 `_check_residency` ·
# `tools/metrics.py` 의 거주 위반 지표 · 게이트 `residency`(`kb/ontology/shapes/residency-shapes.ttl` 이 이 표와 같은지).
# 값에 주석(`#`)을 쓰지 않는다 — 파서가 주석을 지운 뒤 리터럴로 읽는다.
RESIDENCY = {
    "requirement": ["functional"],
    "decision": ["abstract", "logical", "concrete"],
    "contract": ["abstract", "logical"],
    "schema": ["logical", "concrete"],
    "artifact": ["concrete", "executable"],
    "memory": ["concrete"],
    "annotation": LEVELS,
    "norm": ["logical"],
}
STATES = ["draft", "stable", "suspect", "invalidated", "deprecated"]

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

def norm_doc_labels():
    """`NORM_DOCS` 의 생성 파일 → 소스 파일 라벨 — 디렉토리가 패키지다(`STYLEGUIDE.md` → `//:STYLEGUIDE.md`)."""
    out = []
    for path in NORM_DOCS.values():
        pkg, _, name = path.rpartition("/")
        out.append("//%s:%s" % (pkg, name))
    return out

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

# ══ 게이트 등록부 — 게이트 id·계층·도구 태그의 단일 정의처와 그 자기 정합성 ══════════════════════════════════
# ── 게이트 등록부 (`GATES`) — 게이트 id 의 **단일 정의처** (M1, 2026-10-02, RESIDENCY·EXTRACTED_SOURCES 와 같은 해법) ─
# 결정 p0-service-is-a-three-layer-wiki: 게이트는 프로세스 층의 **항목**이다. 2026-10-01 실측에서 같은 목록이 넷으로
# 갈려 있었다 — `kb_lib` 의 `*_GATE` 상수 · 코드의 태그 · `docs/tools.md` 총람의 `id` 열 · 그 아래 하네스 목록.
# 여기 말고 어디에도 게이트 id 를 손으로 적지 않는다. 파생처는 넷이다 — `tools/kb_lib.py` 의 `load_gates`(리터럴
# 읽기 → 모듈 속성 `<이름>_GATE`) · `tools/gates2kg.py`(생성 그래프 `//kg:gates_kg` 의 `id:gate-<id>` 개체) ·
# `validate` 의 게이트 `gate-registry`(코드의 태그 집합 = 이 리터럴) · `doccheck` 의 총람 `id` 열 대조.
# 값에 주석(`#`)을 쓰지 않는다 — 파서가 주석을 지운 뒤 리터럴로 읽는다.
#
# 항목마다 넷을 적는다. `tier` 는 실행 계층(총람의 다섯), `tool` 은 판정 도구(`tools/<이름>.py` 의 모듈 이름 또는
# 파이썬 밖인 `starlark`·`bazel`), `ko` 는 한글 라벨, `desc` 는 무엇을 거부하는가 한 줄이다. 영문 라벨은 id 자신이다.
# 층은 항목마다 적지 않는다 — 게이트는 전부 프로세스 층이고 그 값이 `GATE_LAYER` 다.
GATE_LAYER = "process"
GATE_TIERS = ["shape", "verify", "analysis", "test", "human"]
GATE_TOOLS_OUTSIDE_PYTHON = ["starlark", "bazel"]

# ── 게이트 목록 — id 순서로 잇는 리터럴 둘(`GATES` · `GATES_TAIL`)의 앞이다. 순서와 서로소는 `kb_lib.load_gates` 가 강제한다 ──
GATES = {
    "addition": {"tier": "test", "tool": "chunk_lint", "ko": "첨가", "desc": "슬롯의 질문에 답하지 않는 메타 문장과 채움 문구"},
    "blocking-comment": {"tier": "test", "tool": "chunk_lint", "ko": "해소되지 않은 차단 주석", "desc": "issue (blocking) 이면서 해소가 열린 살아 있는 주석"},
    "boundary": {"tier": "verify", "tool": "validate", "ko": "정의 경계", "desc": "한 용어가 두 모듈 파일에서 정의됨"},
    "build-drift": {"tier": "test", "tool": "gen_build", "ko": "BUILD 드리프트", "desc": "생성 BUILD 가 frontmatter 링크와 어긋남"},
    "canon": {"tier": "test", "tool": "canonicalize", "ko": "정규 직렬화", "desc": "TTL 직렬화가 정규형과 다름"},
    "case-drift": {"tier": "test", "tool": "case_gen", "ko": "케이스 드리프트", "desc": "저장소의 케이스가 논리 시나리오의 생성 결과와 어긋나거나 생성기 밖에서 쓰임"},
    "case-gen": {"tier": "analysis", "tool": "case_gen", "ko": "케이스 생성", "desc": "생성 시점의 입력 위반 — 표본 근거 없는 케이스, ODD 속성이 아닌 변수, keep 안의 요인 값, 실행기가 읽지 못하는 케이스"},
    "catalog": {"tier": "verify", "tool": "validate", "ko": "카탈로그 정합성", "desc": "스코프 없는 역할, 미부여 스코프, write plane 공유, maxConcurrent 합 초과"},
    "channel": {"tier": "test", "tool": "channel_lint", "ko": "채널 규약", "desc": "하네스 채널(메시지·질문지)의 어휘·단일 작성자·필수 절·짝 없는 완료 위반"},
    "chunk": {"tier": "test", "tool": "chunk_lint", "ko": "청크 형식", "desc": "본문 토큰 상한 초과와 frontmatter 형식 위반"},
    "chunk2kg": {"tier": "analysis", "tool": "chunk2kg", "ko": "head 생성", "desc": "head 그래프 생성 시점의 frontmatter·본문 규칙 위반"},
    "chunk2kg-merge": {"tier": "analysis", "tool": "chunk2kg", "ko": "head 병합", "desc": "타깃별 head 조각의 병합 실패"},
    "code-part-link": {"tier": "verify", "tool": "validate", "ko": "코드 부분 링크", "desc": "추출 트리의 복합체 부분(정의·구역 청크)이 refines·serves·verifies 의 끝점"},
    "cross-kb-link": {"tier": "verify", "tool": "validate", "ko": "KB 가로지름 링크", "desc": "verifies 밖의 저작 링크가 두 KB 를 가로지름 (검증 목표 → 요구 derivesFrom 만 예외)"},
    "dangling": {"tier": "verify", "tool": "validate", "ko": "참조 무결성", "desc": "인용·부분·가정·요구·정의 호출의 대상이 실재하지 않음"},
    "decision-role": {"tier": "test", "tool": "chunk_lint", "ko": "결정 역할 표지", "desc": "결론·근거·대안·규약 청크의 첫 산문 줄에 역할 표지가 없음"},
    "doccheck": {"tier": "test", "tool": "doccheck", "ko": "문서 현행성", "desc": "문서의 죽은 링크·앵커·백틱 경로와 산문 문체 위반"},
    "element-drop": {"tier": "verify", "tool": "validate", "ko": "요소 탈락", "desc": "어휘에 슬롯이 없어 조용히 빠진 소스 요소"},
    "empty-value": {"tier": "test", "tool": "chunk_lint", "ko": "빈 값 표기", "desc": "세 빈 값 밖의 표기와 표의 단독 대시 셀"},
    "extract": {"tier": "analysis", "tool": "extract", "ko": "코드 추출", "desc": "추출 시점의 개명 안내·삭제·부분 상한·등록부 불일치"},
    "extract-drift": {"tier": "test", "tool": "extract", "ko": "추출 드리프트", "desc": "추출 생성물이 소스와 등록부에 어긋남"},
    "extract-refs": {"tier": "analysis", "tool": "extract_refs", "ko": "인용 대상 실재", "desc": "본문 인용의 대상이 실재하지 않음"},
    "frozen": {"tier": "test", "tool": "doccheck", "ko": "동결 문서", "desc": "동결 문서의 sha256 이 kb_lib.FROZEN_DOCS 의 고정값과 다름"},
    "gate-registry": {"tier": "verify", "tool": "validate", "ko": "게이트 등록부", "desc": "코드의 게이트 태그 집합이 GATES 리터럴과 갈림"},
    "gates2kg": {"tier": "analysis", "tool": "gates2kg", "ko": "게이트 그래프 생성", "desc": "게이트 등록부의 키·계층 위반과 판정 도구 개체의 부재"},
}

# ── 게이트 목록의 이어짐 — 앞 리터럴의 id 순서를 잇는다 (청크 하나의 인용 상한 2,856토큰, 2026-10-05) ──
# 리터럴 하나가 추출 청크 하나라 게이트가 늘면 인용 상한을 넘는다. 그래서 id 순서를 유지한 채 둘로 잇는다 — 앞의 마지막
# id 보다 뒤의 첫 id 가 뒤이고 두 리터럴은 서로소다(`kb_lib.load_gates` 가 둘을 읽어 대조한다). 판정 대상은 합친 `GATES` 다
GATES_TAIL = {
    "gen-build": {"tier": "analysis", "tool": "gen_build", "ko": "BUILD 생성", "desc": "생성 시점의 묶음·세 청크·링크 규칙 위반"},
    "gen-norms": {"tier": "analysis", "tool": "gen_norms", "ko": "규범 문서 생성", "desc": "생성 시점의 절 청크·규약 줄 위반 — 고아 줄·이중 소비·없는 줄·강도 없는 줄·문서 목록 불일치"},
    "gen-skills": {"tier": "analysis", "tool": "gen_skills", "ko": "skill 생성", "desc": "skill 생성 시점의 입력 위반"},
    "gendoc": {"tier": "test", "tool": "gendoc", "ko": "생성 문서 형태", "desc": "생성 마크다운의 머리 블록과 본문 서식 규약 위반"},
    "judge-log": {"tier": "test", "tool": "chunk_lint", "ko": "판정 로그", "desc": "판정 로그의 표 형식과 필수 필드 위반"},
    "labels": {"tier": "verify", "tool": "validate", "ko": "라벨 완전성", "desc": "agt: 용어의 한·영 라벨 또는 skos:definition 누락"},
    "list-rules": {"tier": "test", "tool": "chunk_lint", "ko": "목록 규칙", "desc": "손 번호·항목 수·중첩·길이·빈 항목의 목록 규칙 위반"},
    "naming": {"tier": "test", "tool": "chunk_lint", "ko": "파일 접미사", "desc": "TTL 파일 이름이 접미사 규약 밖"},
    "norms-drift": {"tier": "test", "tool": "gen_norms", "ko": "규범 문서 드리프트", "desc": "생성 규범 문서가 절 청크와 결정의 규약 줄에 어긋남"},
    "odd-ref": {"tier": "verify", "tool": "validate", "ko": "ODD 참조", "desc": "ODD 에 없는 조건을 참조하는 스코프·가정·변수"},
    "odd2kg": {"tier": "analysis", "tool": "odd2kg", "ko": "ODD 생성", "desc": "OpenODD 문서의 형식과 필수 필드 위반"},
    "prose": {"tier": "test", "tool": "chunk_lint", "ko": "산문 문체", "desc": "경어체 종결과 산문의 느낌표"},
    "residency": {"tier": "verify", "tool": "validate", "ko": "수준 허용표 단일 정의처", "desc": "수준 허용표 shape 가 RESIDENCY 리터럴과 갈림"},
    "restored": {"tier": "analysis", "tool": "chunk2kg", "ko": "복원 표시", "desc": "restored 의 IRI 가 같은 청크의 링크 키 대상에 없음"},
    "rung-before-descent": {"tier": "verify", "tool": "validate", "ko": "사다리 사슬", "desc": "같은 높이의 V&V 대응물(목표·기준·검증기 바인딩) 없이 다음 높이로 내려간 하강"},
    "shacl": {"tier": "shape", "tool": "validate", "ko": "shape 적합성", "desc": "SHACL shape 부적합"},
    "skills-drift": {"tier": "test", "tool": "gen_skills", "ko": "skill 드리프트", "desc": "생성 skill 이 docstring 과 SKILLS 에 어긋남"},
    "space": {"tier": "analysis", "tool": "space2kg", "ko": "설계 공간", "desc": "근거 없는 배제, 확정 후보 수, 변수와 후보의 불일치"},
    "specialization": {"tier": "analysis", "tool": "chunk2kg", "ko": "특수화 링크", "desc": "specializationOf 의 자기 참조·plane 불일치·폐기 대상·순환"},
    "stamp": {"tier": "test", "tool": "stamp", "ko": "도장", "desc": "도장 입력이 등록부와 어긋남"},
    "summary-support": {"tier": "test", "tool": "chunk_lint", "ko": "요약 지지 참조", "desc": "요약 블록의 핵심 항목에 지지 참조가 없음"},
    "syntax": {"tier": "verify", "tool": "validate", "ko": "구문", "desc": "TTL 이 파싱되지 않음"},
    "taxonomy": {"tier": "analysis", "tool": "taxonomy", "ko": "택소노미 생성", "desc": "택소노미 생성 입력이 읽히거나 파싱되지 않음"},
    "tim": {"tier": "analysis", "tool": "starlark", "ko": "TIM", "desc": "링크 타입의 정의역·치역·방향·수준 위반"},
    "token-budget": {"tier": "verify", "tool": "validate", "ko": "토큰 상한 단일 정의처", "desc": "plane 별 본문 토큰 상한의 표와 shape 가 갈림, 어휘 파일 지문 불일치"},
    "verify": {"tier": "verify", "tool": "validate", "ko": "안티패턴", "desc": "안티패턴 SPARQL 질의가 위반 행을 냄"},
    "visibility": {"tier": "analysis", "tool": "bazel", "ko": "의존 방향", "desc": "개발 타깃이 V&V 타깃을 의존함"},
    "vocab": {"tier": "verify", "tool": "validate", "ko": "통제 어휘", "desc": "온톨로지와 등록 표준 어휘 밖의 술어·용어"},
    "vv-case": {"tier": "analysis", "tool": "vv_run", "ko": "V&V 케이스 형식", "desc": "케이스의 기계가 읽는 자극·기대 규약 위반"},
    "vv-run-env": {"tier": "test", "tool": "vv_run_env_test", "ko": "실행기 환경 격리", "desc": "케이스의 명령이 실행기의 파이썬·runfiles 문맥을 물려받음"},
    "workset-budget": {"tier": "analysis", "tool": "workset", "ko": "작업 집합 예산", "desc": "앵커가 있는 작업 집합 뷰가 컨텍스트 예산을 넘음"},
    "writer": {"tier": "human", "tool": "validate", "ko": "승인", "desc": "쓰기 권한 밖의 저작과 검토 없는 stable 전이"},
}

GATES.update(GATES_TAIL)

# ── 도구 태그와 등록부의 자기 정합성 검사 ─────────────────────────────────────────────────────────────
# 게이트가 아닌 **도구 태그** — 입력·설정 문제와 보고에만 쓰여 판정 효과가 없다(뷰·생성기의 CONFIG·WARN 자리).
# 같은 대괄호 표기를 쓰므로 게이트 `gate-registry` 가 태그 전수를 볼 때 이 목록이 둘째 경계다 (USES_TARGETS 와
# 같은 자리). `GATES` 와 서로소여야 한다 — `check_gates` 가 로드 시점에 강제한다.
TOOL_TAGS = [
    "consistency",
    "endorse",  # 쓰는 시점의 입력 거부(미래 시각의 --at) — 게이트는 시계에 의존할 수 없어 판정 효과가 없다
    "judge",
    "link",
    "open",
    "propose",
    "revalidate",
    "run-evidence",  # 실행 증거 생성기의 입력 거부(읽을 수 없는 청크·값 어휘) — 판정 효과가 없다
    "tokens",
    "validate",
    "weave",
]

def check_gates():
    """`GATES`·`TOOL_TAGS` 리터럴의 자기 정합성을 로드 시점에 강제한다 (M1, check_extracted_sources 와 같은 자리).

    `BUILD` 파일은 `if` 문을 쓸 수 없어 판정을 함수로 옮겼다. 항목마다 네 키(`tier`·`tool`·`ko`·`desc`)가 있고
    `tier` 는 `GATE_TIERS` 안이며 두 목록은 서로소다. 갈리면 이 패키지를 보는 어떤 bazel 명령이든 바로 `fail`
    한다 — 등록부가 조용히 비거나 어긋나는 사고를 막는다.
    """
    for gid, spec in GATES.items():
        for key in ["tier", "tool", "ko", "desc"]:
            if key not in spec or not spec[key]:
                fail("GATES(//defs:kb.bzl) 의 %r 에 %s 가 없다 — 항목마다 계층·판정 도구·한글 라벨·설명 한 줄을 적는다" % (gid, key))
        if spec["tier"] not in GATE_TIERS:
            fail("GATES(//defs:kb.bzl) 의 %r 의 계층 %r 이 어휘 밖이다 — %s 중 하나다" % (gid, spec["tier"], GATE_TIERS))
    both = [t for t in TOOL_TAGS if t in GATES]
    if both:
        fail("GATES 와 TOOL_TAGS(//defs:kb.bzl) 가 겹친다 — %s. " % both +
             "한 태그는 게이트이거나 도구 태그이고 둘 다일 수 없다")

# ══ 구조 판정 — 등록부 정합성(로드 시점)과 거주·링크·청크·복합체 규칙(분석 시점) ════════════════════════════
# ── 추출 경계의 정합성 — 등록부 사이드카의 실재와 경계 목록을 로드 시점에 대조한다 ──────────────────────────
def check_extracted_sources(registry_globs):
    """등록부 사이드카 glob 결과와 `EXTRACTED_SOURCES` + `EXTRACTED_QUERY_DIRS` 가 같은 집합인지 로드 시점에 강제한다 (M1, 2026-10-01).

    `registry_globs` 는 호출자(`tools/BUILD.bazel`)가 준 `glob(["*.chunks.yml"])` 의 결과다 — `glob` 은 패키지를
    넘어가지 못하므로(최상위 `BUILD.bazel` 에서 `tools/*.chunks.yml` 을 globbing 할 수 없다) 호출은 `tools`
    패키지 안에서 하고, 그 결과는 접두 없는 `<이름>.chunks.yml` 이다. BUILD 파일은 `if` 문을 쓸 수 없어 이
    판정을 함수로 옮겼다(`_check_residency` 와 같은 자리). 갈리면 이 패키지를 보는 어떤 bazel 명령이든 바로
    `fail` 한다 — 조용히 비는 사고(음성 시험, 유저 지시 2026-10-01)를 막는다. `USES_TARGETS` 가
    `EXTRACTED_SOURCES` 의 부분집합인지도 같은 자리에서 본다 — 치역 경계와 방출 경계의 두 목록이 갈리면
    `uses` 의 대상이 실재하지 않는다.
    """
    found = sorted([f[:-len(".chunks.yml")] for f in registry_globs])
    both = [m for m in EXTRACTED_QUERY_DIRS if m in EXTRACTED_SOURCES]
    if both:
        fail("EXTRACTED_SOURCES 와 EXTRACTED_QUERY_DIRS(//defs:kb.bzl) 가 겹친다 — %s. " % both +
             "등록부 사이드카 하나는 소스 모듈 하나이거나 질의 디렉토리 하나다")
    listed = EXTRACTED_SOURCES + EXTRACTED_QUERY_DIRS
    missing_from_list = [m for m in found if m not in listed]
    missing_from_tree = [m for m in listed if m not in found]
    if missing_from_list or missing_from_tree:
        fail("EXTRACTED_SOURCES·EXTRACTED_QUERY_DIRS(//defs:kb.bzl) 와 tools/*.chunks.yml 의 실재가 갈린다 — " +
             "등록부는 있는데 목록에 없음: %s · 목록에는 있는데 등록부가 없음: %s" % (missing_from_list, missing_from_tree))
    outside = [m for m in USES_TARGETS if m not in EXTRACTED_SOURCES]
    if outside:
        fail("USES_TARGETS(//defs:kb.bzl) 가 EXTRACTED_SOURCES 밖을 치역으로 둔다 — %s. " % outside +
             "추출되지 않은 모듈에는 정의 청크가 없어 `uses` 의 대상이 실재하지 않는다 (dangling)")

def check_extracted_starlark(registry_globs):
    """`defs` 패키지의 등록부 사이드카 glob 결과와 `EXTRACTED_STARLARK` 가 같은 집합인지 로드 시점에 강제한다 (유저 답 Q32-a).

    `check_extracted_sources` 의 Starlark 소스판이다. `glob` 은 패키지를 넘지 못하므로 호출은 `defs/BUILD.bazel` 이 하고
    그 결과는 접두 없는 `<이름>.chunks.yml` 이다. 갈리면 이 패키지를 보는 어떤 bazel 명령이든 바로 `fail` 한다 —
    목록에만 있는 이름은 드리프트 테스트가 없는 등록부를 가리키고, 등록부에만 있는 이름은 검사 밖의 생성물을 남긴다.
    """
    found = sorted([f[:-len(".chunks.yml")] for f in registry_globs])
    missing_from_list = [m for m in found if m not in EXTRACTED_STARLARK]
    missing_from_tree = [m for m in EXTRACTED_STARLARK if m not in found]
    if missing_from_list or missing_from_tree:
        fail("EXTRACTED_STARLARK(//defs:kb.bzl) 와 defs/*.chunks.yml 의 실재가 갈린다 — " +
             "등록부는 있는데 목록에 없음: %s · 목록에는 있는데 등록부가 없음: %s" % (missing_from_list, missing_from_tree))

# ── 링크와 거주의 구조 판정 — 분석 시점 fail. 의미 판정은 그래프 게이트가 한다 ──────────────────────────────
def _check_residency(label, plane, level):
    if plane not in PLANES:
        fail("%s: 알 수 없는 plane %r" % (label, plane))
    if level not in RESIDENCY[plane]:
        fail("%s: 수준 허용표 위반 — plane %s 는 level %s 에 살 수 없다 (6.4절)" % (label, plane, level))

def _is_vv(label):
    """V&V KB 의 타깃인가 — 패키지 접두 kb/vv (pe-storage-layout). 그 밖(kb/dev·chunks)은 개발 KB 다."""
    return label.package == "kb/vv" or label.package.startswith("kb/vv/")


def _check_links(ctx, plane, level):
    """링크 방향의 구조 판정 — 분석 시점 fail. 의미 판정은 그래프 게이트가 한다."""
    for dep in ctx.attr.refines + ctx.attr.serves:
        t = dep[ChunkInfo]
        if LEVELS.index(t.level) >= LEVELS.index(level):
            fail("%s: refines/serves 대상 %s 은 더 높은 수준이어야 한다 (정제 계층 6.2절): %s → %s" % (ctx.label, dep.label, level, t.level))
        if PLANES.index(t.plane) > PLANES.index(plane):
            fail("%s: plane 단방향 위반 (5.2절) — %s 가 하위 plane %s 를 refines 한다" % (ctx.label, plane, t.plane))
    for dep in ctx.attr.serves:
        if dep[ChunkInfo].plane != "requirement":
            fail("%s: serves 의 대상은 requirement 뿐이다 (6.8절): %s" % (ctx.label, dep.label))
    for dep in ctx.attr.supersedes:
        if dep[ChunkInfo].plane != plane:
            fail("%s: supersedes 는 같은 plane 안에서만 (7.4절): %s → %s" % (ctx.label, plane, dep[ChunkInfo].plane))
    for dep in ctx.attr.refines + ctx.attr.serves + ctx.attr.supersedes:
        if _is_vv(ctx.label) != _is_vv(dep.label):
            fail("%s: refines/serves/supersedes 는 KB 안에서만이다 — KB 를 가로지르는 링크는 verifies 뿐이다 (V&V → 개발, 7.5절): %s" % (ctx.label, dep.label))
    for dep in ctx.attr.verifies:
        if not _is_vv(ctx.label):
            fail("%s: verifies 의 주어는 V&V KB 청크뿐이다 (8.5절)" % ctx.label)
        if _is_vv(dep.label):
            fail("%s: verifies 의 대상은 개발 KB 청크다: %s" % (ctx.label, dep.label))
        if dep[ChunkInfo].level != level:
            fail("%s: verifies 는 같은 수준끼리 (8.3절 검증 대응물): %s ≠ %s" % (ctx.label, level, dep[ChunkInfo].level))

def _lint_action(ctx, files):
    """검증 액션 — bazel build 만으로 토큰 상한·frontmatter·첨가·목록 검사가 돈다 (validation output group).

    면제 선언(docs/waivers.md)을 함께 읽는다. 면제는 코드가 아니라 그 표에 있고(AGENTS.md·STYLEGUIDE §8),
    게이트 id 는 prose·addition·empty-value·list-rules 다. 표를 주지 않으면 청크를 겨눈 면제가 이 액션에만
    적용되지 않아 //kb/...:lint_test 와 판정이 갈린다.
    어휘 파일(`_vocab`)도 명시 입력이다 — 크기의 단위가 토큰이므로 계수기가 이 액션의 입력이고, 그것이
    샌드박스에 없으면 판정을 내릴 수 없다 (결정 p1-chunk-unit-is-tokens, ODD id:cond-tokenizer-lock).
    """
    marker = ctx.actions.declare_file(ctx.label.name + ".lint.ok")
    waivers = ctx.file._waivers
    vocab = ctx.file._vocab
    ctx.actions.run_shell(
        inputs = files + [waivers, vocab],
        outputs = [marker],
        tools = [ctx.executable._lint],
        command = "%s --chunks %s --waivers %s --vocab %s && touch %s" % (
            ctx.executable._lint.path,
            " ".join([f.path for f in files]),
            waivers.path,
            vocab.path,
            marker.path,
        ),
        mnemonic = "KbChunkLint",
        progress_message = "청크 검사 %s" % ctx.label,
    )
    return marker

def _head_action(ctx, files, ordered = [], conventions = {}):
    """타깃 하나의 head 그래프 조각 — chunk2kg --fragment. 프런트매터 오류·복합체 불일치는 여기서 실패한다.

    PLANES·LEVELS·STATES 값 어휘의 원본은 //defs:kb.bzl 이다(M1 단일 정의처, 2026-09-26). chunk2kg 가 그 리터럴을
    읽으려면 샌드박스에 파일이 있어야 하므로 _residency 를 명시 입력으로 준다 — _waivers 를 //docs:waivers 로 준
    것과 같은 방식이다. 경로는 하드코딩하지 않고 --residency 인자로 넘긴다.

    `ordered` 는 이 묶음의 복합체가 선언한 부분의 순서다 (p4-composite-order-is-declared, 유저 승인 2026-09-29 — 예외 없음).
    비어 있으면 순서를 넘기지 않고 생성기도 추측하지 않는다. 결정 복합체의 선언이 이 자리로 들어온다 — 손으로 205개
    frontmatter 를 고치지 않고 생성 BUILD 의 명시 인자를 원본으로 둔다.

    `conventions` 는 결정 slug → 결정 복합체 IRI 다 — 규범 문서의 절 청크(`norm`)가 `items` 로 가리키는 결정을 head 조각의
    `agt:projectsConvention` 으로 풀 때 쓴다(p12-norm-documents-from-section-chunks). gen_build 가 결정 디렉토리에서 풀어 넣는다.
    """
    out = ctx.actions.declare_file(ctx.label.name + ".head.ttl")
    residency = ctx.file._residency
    vocab = ctx.file._vocab  # agt:tokenCount 를 이 어휘로 센다 — 계수기가 액션의 입력이다 (p1-chunk-unit-is-tokens)
    args = ["--fragment", "--out", out.path, "--residency", residency.path, "--vocab", vocab.path]
    for iri in ordered:  # 부분마다 한 번 — 목록형 인자는 위치 인자인 청크 파일을 삼킨다
        args = args + ["--ordered", iri]
    for slug in sorted(conventions.keys()):
        args = args + ["--convention-target", "%s=%s" % (slug, conventions[slug])]
    ctx.actions.run(
        executable = ctx.executable._chunk2kg,
        arguments = args + [f.path for f in files],
        inputs = files + [residency, vocab],
        outputs = [out],
        mnemonic = "KbHead",
        progress_message = "head 그래프 조각 %s" % ctx.label,
    )
    return out

# ── 청크 규칙 (`kb_chunk`) — 청크 하나 = 타깃 하나. 링크 속성의 provider 요구가 끝점을 지식 항목으로 묶는다 ───
_LINK_ATTRS = {
    "refines": attr.label_list(providers = [ChunkInfo], doc = "정제 — 더 높은 수준의 항목으로 (6.2절)"),
    "serves": attr.label_list(providers = [ChunkInfo], doc = "기여 — 결정이 봉사하는 요구 (6.8절, ⊑ refines)"),
    "supersedes": attr.label_list(providers = [ChunkInfo], doc = "대체 — 같은 plane 의 옛 항목 (7.4절)"),
    "verifies": attr.label_list(providers = [ChunkInfo], doc = "검증 — V&V 청크만 주어 (8.5절)"),
    "_lint": attr.label(default = "//tools:chunk_lint", executable = True, cfg = "exec"),
    "_waivers": attr.label(default = "//docs:waivers", allow_single_file = True, doc = "게이트 면제 선언 (docs/waivers.md)"),
    "_chunk2kg": attr.label(default = "//tools:chunk2kg", executable = True, cfg = "exec"),
    "_residency": attr.label(default = "//defs:kb.bzl", allow_single_file = True, doc = "PLANES·LEVELS·STATES 값 어휘의 원본 (M1 단일 정의처)"),
    "_vocab": attr.label(default = "@tiktoken_o200k_base//file", allow_single_file = True, doc = "토큰 계수기의 어휘 파일 — 크기 판정과 agt:tokenCount 의 계수기 (p1-chunk-unit-is-tokens)"),
}

def _kb_chunk_impl(ctx):
    _check_residency(ctx.label, ctx.attr.plane, ctx.attr.level)
    if ctx.attr.status not in STATES:
        fail("%s: 알 수 없는 status %r" % (ctx.label, ctx.attr.status))
    _check_links(ctx, ctx.attr.plane, ctx.attr.level)
    src = ctx.file.src
    head = _head_action(ctx, [src])
    return [
        DefaultInfo(files = depset([src])),
        ChunkInfo(iri = ctx.attr.iri, plane = ctx.attr.plane, level = ctx.attr.level, status = ctx.attr.status, srcs = depset([src]), parts = []),
        KgInfo(ttl = depset([head])),
        OutputGroupInfo(_validation = depset([_lint_action(ctx, [src])]), kg = depset([head])),
    ]

kb_chunk = rule(
    implementation = _kb_chunk_impl,
    doc = "청크 하나 = 타깃 하나. frontmatter 에서 생성된다 (tools/gen_build.py) — 손으로 쓰지 않는다.",
    attrs = dict({
        "src": attr.label(allow_single_file = [".md"], mandatory = True),
        "iri": attr.string(mandatory = True),
        "plane": attr.string(mandatory = True, values = PLANES),
        "level": attr.string(mandatory = True, values = LEVELS),
        "status": attr.string(default = "stable", values = STATES),
    }, **_LINK_ATTRS),
)

# ── 복합체 규칙 (`kb_composite`·`kb_decision`) — 부분의 수·순서·결정의 세 청크를 분석 시점에 강제한다 ─────────
MAX_PARTS = 9  # 직접 부분의 상한 (7±2, 4.5절) — shape kb/ontology/shapes/composite-shapes.ttl 의 sh:maxCount 와 같은 수

def _check_order(label, ordered, part_iris):
    """선언된 순서가 부분 전부를 빠짐없이 한 번씩 담는가 — 분석 시점 fail. 색인 1..n 의 정합성은 shape 가 본다."""
    if sorted(ordered) != sorted(part_iris):
        fail("%s: ordered 가 부분 집합과 다르다 — 순서 목록은 부분 전부를 빠짐없이 한 번씩 담는다 (p4-composite-order-is-declared): %s ≠ %s" %
             (label, ordered, part_iris))

def _composite_outputs(ctx, plane, level, files, part_iris, ordered = [], conventions = {}):
    """복합체 규칙 둘(kb_decision·kb_composite)이 공유하는 산출 — head 조각 하나·검사 액션 하나·provider.

    묶음의 단위가 **액션의 입력 집합**이다. 부분 청크 전부와 composite: 선언 청크가 한 액션의 입력이라
    chunk2kg --fragment 가 그 안에서 part_of 대상을 찾아 복합체 개체를 방출한다 (파일 하나 = 묶음 하나가 아니다).

    `ordered` 가 있으면 head 액션이 co:List 와 co:index 를 그 순서로 낸다. 없으면 순서가 없다 — 추측하지 않는다.
    """
    head = _head_action(ctx, files, ordered, conventions)
    return [
        DefaultInfo(files = depset(files)),
        ChunkInfo(iri = ctx.attr.iri, plane = plane, level = level, status = ctx.attr.status, srcs = depset(files), parts = part_iris),
        KgInfo(ttl = depset([head])),
        OutputGroupInfo(_validation = depset([_lint_action(ctx, files)]), kg = depset([head])),
    ]

def _kb_composite_impl(ctx):
    n = len(ctx.attr.part_iris)
    if n < 2:
        fail("%s: 복합체는 부분 둘 이상의 묶음이다 — 부분 하나면 청크다 (4.5절): 부분 %d" % (ctx.label, n))
    if n > MAX_PARTS:
        fail("%s: 직접 부분은 최대 %d개(7±2)다 (4.5절): 부분 %d" % (ctx.label, MAX_PARTS, n))
    if len(ctx.files.srcs) < n:
        fail("%s: 부분이 묶음 밖에 있다 — 부분 청크는 이 액션의 입력 집합 안에 있어야 한다 (4.5절): 파일 %d · 부분 %d" %
             (ctx.label, len(ctx.files.srcs), n))
    _check_residency(ctx.label, ctx.attr.plane, ctx.attr.level)
    if ctx.attr.status not in STATES:
        fail("%s: 알 수 없는 status %r" % (ctx.label, ctx.attr.status))
    _check_links(ctx, ctx.attr.plane, ctx.attr.level)
    if ctx.attr.ordered:
        _check_order(ctx.label, ctx.attr.ordered, ctx.attr.part_iris)
    if ctx.attr.conventions and ctx.attr.plane != "norm":
        fail("%s: conventions 는 규범 문서의 절(plane norm)의 복합체에만 준다 — 실제 plane %s (p12-norm-documents-from-section-chunks)" %
             (ctx.label, ctx.attr.plane))
    return _composite_outputs(ctx, ctx.attr.plane, ctx.attr.level, ctx.files.srcs, ctx.attr.part_iris, ctx.attr.ordered,
                              ctx.attr.conventions)

kb_composite = rule(
    implementation = _kb_composite_impl,
    doc = """복합체 = 타깃 하나 (부분 2~9개의 가변 묶음). 결정 밖 plane 의 복합체가 이 규칙으로 선다 (p4-all-knowledge-is-composite).

    kb_decision 과 다른 것은 둘이다. 첫째, 부분의 수가 가변이라 역할 이름 붙은 인자(conclusion·rationale·alternatives)가 아니라
    srcs 목록을 받는다. 둘째, **동질성**이 구조로 강제된다 — plane·level 을 복합체 하나가 한 쌍만 갖고 gen_build 가 부분들의
    frontmatter 가 그 쌍에 일치할 때만 이 규칙을 생성한다. 결정 복합체의 수준 혼합(결론 concrete·근거/대안 logical)은
    kb_decision 의 예외로 남는다 (p7-decision-spans-three-levels).

    순서는 선언에서만 온다 (p4-composite-order-is-declared, 유저 승인 2026-09-29 — 예외 없음) — 선언 청크의
    `composite.ordered` 가 있으면 gen_build 가 그것을 `ordered` 인자와 `part_iris` 순서로 옮기고 head 액션이 `co:List` +
    `co:index` 를 낸다. 없으면 순서가 없고 part_iris 는 srcs 순서일 뿐 뜻을 갖지 않는다.""",
    attrs = dict({
        "srcs": attr.label_list(allow_files = [".md"], mandatory = True, doc = "부분 청크 파일들 + composite: 선언 청크 — 이 액션의 입력 집합이 묶음이다"),
        "iri": attr.string(mandatory = True, doc = "복합체 IRI"),
        "part_iris": attr.string_list(mandatory = True, doc = "부분 청크 IRI — 선언 청크에 `composite.ordered` 가 있으면 그 순서, 없으면 srcs 순서(뜻 없음)"),
        "ordered": attr.string_list(doc = "선언된 부분의 순서 (선택) — 선언 청크의 `composite.ordered` 를 gen_build 가 옮긴 뷰다. 비어 있으면 순서가 없다"),
        "conventions": attr.string_dict(doc = "결정 slug → 결정 복합체 IRI (선택, plane norm 만) — 절 청크의 items 가 줄을 싣는 결정이다. gen_build 가 결정 디렉토리에서 푼다"),
        "plane": attr.string(mandatory = True, values = PLANES, doc = "복합체와 부분 전부의 plane (동질성)"),
        "level": attr.string(mandatory = True, values = LEVELS, doc = "복합체와 부분 전부의 level (동질성)"),
        "status": attr.string(default = "stable", values = STATES),
    }, **_LINK_ATTRS),
)

def _kb_decision_impl(ctx):
    levels = ctx.attr.part_levels
    n = 4 if ctx.file.conventions else 3  # 세 청크는 필수이고 규약 청크는 선택 넷째다 (p4-convention-slot, 유저 답 Q22-b)
    if len(levels) != n or len(ctx.attr.part_iris) != n:
        fail("%s: 결정은 결론·근거·대안 세 청크(+ 선택 규약 청크)의 복합체다 (7.4절, p4-convention-slot) — 부분 파일 %d · 수준 %d · IRI %d" %
             (ctx.label, n, len(levels), len(ctx.attr.part_iris)))
    for lv in levels:
        _check_residency(ctx.label, "decision", lv)
    if ctx.attr.status not in STATES:
        fail("%s: 알 수 없는 status %r" % (ctx.label, ctx.attr.status))
    _check_links(ctx, "decision", levels[0])
    _check_order(ctx.label, ctx.attr.ordered, ctx.attr.part_iris)  # 결정도 예외가 없다 — 순서는 선언이고 인자가 필수다
    files = [ctx.file.conclusion, ctx.file.rationale, ctx.file.alternatives] + ([ctx.file.conventions] if ctx.file.conventions else [])
    return _composite_outputs(ctx, "decision", levels[0], files, ctx.attr.part_iris, ctx.attr.ordered)

kb_decision = rule(
    implementation = _kb_decision_impl,
    doc = """결정 복합체 = 타깃 하나 (결론·근거·대안 셋 필수 + 선택 넷째 규약 청크). 대안이 없으면 로드 시점에 실패한다 — 대안 청크 필수(7.4절)의 구조 형태.
    규약 청크 `conventions.md` 는 결정이 규범 문서에 싣는 `규약:` 줄을 담고 순서는 셋 뒤다 (p4-convention-slot, 유저 답 Q22-b).

    결정 밖의 복합체는 kb_composite 다. 두 규칙은 _composite_outputs 로 같은 head 액션·검사 액션·provider 를 쓰고,
    부분의 수(셋 고정 대 2~9 가변)와 동질성 예외(결정만 수준 혼합)에서만 갈린다.

    순서는 갈리지 않는다 — 결정도 예외가 아니고 선언으로만 순서를 갖는다 (유저 승인 2026-09-29, p4-composite-order-is-declared).
    다만 선언의 자리가 다르다: `kb_composite` 는 선언 청크의 frontmatter 를 gen_build 가 옮기고, 결정은 역할이 순서를 정하므로
    gen_build 가 결론·근거·대안 순서를 `ordered` 인자로 **넣는다**(필수). 205개 conclusion.md 를 손으로 고치는 것이 첨가이기
    때문이고, 그래도 순서의 원본은 추측이 아니라 생성 BUILD 의 명시 인자다.""",
    attrs = dict({
        "conclusion": attr.label(allow_single_file = [".md"], mandatory = True),
        "rationale": attr.label(allow_single_file = [".md"], mandatory = True),
        "alternatives": attr.label(allow_single_file = [".md"], mandatory = True),
        "conventions": attr.label(allow_single_file = [".md"], doc = "규약 청크 conventions.md (선택 넷째 부분, p4-convention-slot) — 규범 문서에 실릴 `규약:` 줄"),
        "iri": attr.string(mandatory = True, doc = "복합체 IRI"),
        "part_iris": attr.string_list(mandatory = True, doc = "결론·근거·대안(·규약) 청크 IRI"),
        "ordered": attr.string_list(mandatory = True, doc = "선언된 읽기 순서 — 결론·근거·대안(·규약). gen_build 가 넣는다(유저 승인 2026-09-29: 결정도 예외 없이 선언한다)"),
        "part_levels": attr.string_list(mandatory = True, doc = "결론·근거·대안(·규약)의 수준"),
        "status": attr.string(default = "stable", values = STATES),
    }, **_LINK_ATTRS),
)

# ── 묶음·병합·뷰 규칙 — 입력 집합과 인자의 배선이다(등록부 `wiring`, 유저 답 Q10-a) ──────────────────────────
def _kb_ontology_module_impl(ctx):
    return [
        DefaultInfo(files = depset(ctx.files.srcs)),
        OntologyModuleInfo(iri = ctx.attr.iri, srcs = depset(ctx.files.srcs), imports = [d[OntologyModuleInfo].iri for d in ctx.attr.imports]),
    ]

kb_ontology_module = rule(
    implementation = _kb_ontology_module_impl,
    doc = "온톨로지 모듈(디렉토리) = 타깃 하나. imports 는 owl:imports 에서 생성된다.",
    attrs = {
        "srcs": attr.label_list(allow_files = [".ttl"], mandatory = True),
        "iri": attr.string(mandatory = True),
        "imports": attr.label_list(providers = [OntologyModuleInfo]),
    },
)

def _kb_bundle_impl(ctx):
    ttl = depset(transitive = [d[KgInfo].ttl for d in ctx.attr.items if KgInfo in d])
    return [DefaultInfo(files = ttl), KgInfo(ttl = ttl)]

kb_bundle = rule(
    implementation = _kb_bundle_impl,
    doc = "패키지의 지식 항목 묶음 — KgInfo 를 전이적으로 모은다. gen_build 가 패키지마다 :kg 로 생성한다.",
    attrs = {"items": attr.label_list(mandatory = True)},
)

def _kb_kg_merge_impl(ctx):
    frags = depset(transitive = [d[KgInfo].ttl for d in ctx.attr.deps])
    out = ctx.actions.declare_file(ctx.attr.out)
    args = ctx.actions.args()
    args.add("--merge")
    args.add("--out", out)
    args.add_all(frags)
    ctx.actions.run(
        executable = ctx.executable._chunk2kg,
        arguments = [args],
        inputs = frags,
        outputs = [out],
        mnemonic = "KbKgMerge",
        progress_message = "head 그래프 병합 %s" % ctx.label,
    )
    return [DefaultInfo(files = depset([out]))]

kb_kg_merge = rule(
    implementation = _kb_kg_merge_impl,
    doc = "타깃별 head 조각을 하나의 -kg 로 병합한다 (chunk2kg --merge). 바뀐 타깃의 조각만 다시 만들어지고 병합만 다시 돈다.",
    attrs = {
        "deps": attr.label_list(providers = [KgInfo], mandatory = True),
        "out": attr.string(mandatory = True),
        "_chunk2kg": attr.label(default = "//tools:chunk2kg", executable = True, cfg = "exec"),
    },
)

def _kb_workset_view_impl(ctx):
    """작업 집합 뷰 — 스코프(역할) × 수준 창 × 앵커 이웃, 빌드 설정으로 고른다 (0.5절 정정본)."""
    role = ctx.attr._role[BuildSettingInfo].value
    anchor = ctx.attr._anchor[BuildSettingInfo].value
    levels = ctx.attr._levels[BuildSettingInfo].value
    hops = ctx.attr._hops[BuildSettingInfo].value
    budget = ctx.attr._budget[BuildSettingInfo].value
    out = ctx.actions.declare_file("workset-%s.md" % role)
    ttl = [f for f in ctx.files.data if f.extension == "ttl"]
    args = ctx.actions.args()
    args.add("--role", role)
    args.add("--levels", levels)
    args.add("--anchor", anchor)
    args.add("--hops", str(hops))
    args.add("--budget", str(budget))
    args.add("--vocab", ctx.file._vocab)  # 예산의 단위가 토큰이다 (p1-chunk-unit-is-tokens)
    args.add("--root", ".")
    args.add("--out", out)
    args.add_all(ttl)
    ctx.actions.run(
        executable = ctx.executable._workset,
        arguments = [args],
        inputs = ctx.files.data + [ctx.file._vocab],
        outputs = [out],
        mnemonic = "KbWorkset",
        progress_message = "작업 집합 %s (role=%s anchor=%s)" % (ctx.label, role, anchor or "-"),
    )
    return [DefaultInfo(files = depset([out]))]

kb_workset_view = rule(
    implementation = _kb_workset_view_impl,
    doc = "작업 집합 뷰. 선택자는 빌드 설정 //kb:role·anchor·levels·hops·budget — BUILD 를 고치지 않고 명령줄로 고른다. 저장하지 않는 질의 결과다.",
    attrs = {
        "data": attr.label_list(allow_files = True, mandatory = True, doc = "그래프 TTL(-kg)과 청크 본문"),
        "_role": attr.label(default = "//kb:role"),
        "_anchor": attr.label(default = "//kb:anchor"),
        "_levels": attr.label(default = "//kb:levels"),
        "_hops": attr.label(default = "//kb:hops"),
        "_budget": attr.label(default = "//kb:budget"),
        "_workset": attr.label(default = "//tools:workset", executable = True, cfg = "exec"),
        "_vocab": attr.label(default = "@tiktoken_o200k_base//file", allow_single_file = True),
    },
)
