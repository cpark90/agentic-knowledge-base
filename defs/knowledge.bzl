"""지식 산출물용 게이트 매크로.

지식 파일(TTL·청크 본문)은 데이터 타깃이고, 검사 게이트(노트 6.7절)는 테스트 타깃이다.
`bazel test //...` 가 곧 게이트 전체 실행이다.
"""

load("//defs:kb.bzl", "USES_TARGETS")  # `uses` 치역 경계의 단일 정의처 — 대상 모듈의 등록부를 추출 드리프트 테스트의 입력으로 준다
load("@bazel_skylib//rules:build_test.bzl", "build_test")
load("@kb_pip//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_test")

_VALIDATE_SRCS = [
    Label("//tools:validate.py"),
    Label("//tools:kb_lib.py"),
    Label("//tools:chunk2kg.py"),  # kb_lib.load_residency 가 PLANES·LEVELS 리터럴 읽기를 여기서 import 한다 (오케스트레이터 판정 2026-09-27)
]

_LINT_SRCS = [
    Label("//tools:chunk_lint.py"),
    Label("//tools:chunk2kg.py"),  # 논평 본문의 파서 comment_form — 게이트와 방출기가 같은 판정을 쓴다 (p7-commentary-form)
    Label("//tools:kb_lib.py"),
]

_DOCCHECK_SRCS = [
    Label("//tools:doccheck.py"),
    Label("//tools:kb_lib.py"),
    Label("//tools:chunk2kg.py"),  # kb_lib.load_residency 가 PLANES·LEVELS 리터럴 읽기를 여기서 import 한다 (오케스트레이터 판정 2026-09-27)
]

_GENDOC_SRCS = [
    Label("//tools:gendoc.py"),
    Label("//tools:kb_lib.py"),
    Label("//tools:chunk2kg.py"),  # kb_lib.load_residency 가 PLANES·LEVELS 리터럴 읽기를 여기서 import 한다 (오케스트레이터 판정 2026-09-27)
]

_RUNNER_ENV_SRCS = [
    Label("//tools:vv_run_env_test.py"),
    Label("//tools:vv_run.py"),  # 판정 대상 — clean_env·run_command
    Label("//tools:chunk2kg.py"),  # vv_run 이 케이스 frontmatter 를 그 파서로 읽는다
    Label("//tools:kb_lib.py"),
]

_GEN_SKILLS_SRCS = [
    Label("//tools:gen_skills.py"),
    Label("//tools:doccheck.py"),
    Label("//tools:kb_lib.py"),
    Label("//tools:chunk2kg.py"),  # kb_lib.load_residency 가 PLANES·LEVELS 리터럴 읽기를 여기서 import 한다 (오케스트레이터 판정 2026-09-27)
]

# 게이트 등록부(`GATES`)의 단일 정의처 — `kb_lib` 이 적재 시점에 리터럴을 읽어 `*_GATE` 상수를 파생하므로
# `kb_lib.py` 를 `srcs` 로 싣는 타깃은 이 파일을 runfiles 에 둬야 한다. 없으면 적재 시점에 죽는다(의도된 음성 동작).
_GATES_DATA = [Label("//defs:kb.bzl")]

def _with_gates(data):
    """게이트 등록부 리터럴을 runfiles 에 둔다 — 이미 있으면 그대로다.

    `data` 는 라벨 문자열과 `Label` 이 섞이므로 정규화한 문자열로 비교한다. 중복 선언은 Bazel 의 로드 에러다.
    """
    have = [str(Label(d)) for d in data]
    return data + [g for g in _GATES_DATA if str(g) not in have]

_RDF_DEPS = [
    requirement("rdflib"),
    requirement("pyshacl"),
    requirement("owlrl"),
]

def _flag_args(flag, targets):
    if not targets:
        return []
    return [flag] + ["$(rootpaths %s)" % t for t in targets]

def kb_gate_test(
        name,
        ontology = [],
        shapes = [],
        odd = [],
        data = [],
        chunk_files = [],
        verify_queries = None,
        reason = False,
        standard_vocab = [],
        residency = None,
        waivers = None,
        gates = None,
        gate_sources = [],
        **kwargs):
    """검사 게이트 테스트 — tools/validate.py 를 지정 그래프들에 대해 돌린다.

    Args:
      name: 테스트 이름.
      ontology: T-Box 모듈 라벨들 (*-ontology, *-rules).
      shapes: SHACL shape 라벨들 (*-shapes).
      odd: ODD 라벨들 (*-odd). 주면 agt:refersTo → ODD 참조 게이트가 켜진다.
      data: A-Box 라벨들 (*-kg, *-space). 통제 어휘 검사 대상.
      chunk_files: 청크 본문 라벨들 (`:bodies`). 주면 게이트 `element-drop` 의 frontmatter 키 전수 대조가 켜진다 —
        소비되지 않는 키는 조용히 버려지는 소스 요소다 (현상 P19, 8.21절 G1).
      reason: SHACL 전에 OWL-RL 추론 적용.
      residency: 수준 허용표의 원본 라벨 (//defs:kb.bzl). 주면 게이트 `residency` 와 `token-budget` 이 켜진다 —
        shape 의 plane × level 구간이 그 파일의 `RESIDENCY` 와 같은지, plane 별 본문 토큰 상한이
        `kb_lib.BODY_TOKEN_LIMITS` 와 같은지 본다. 표를 두 곳에 적는 것을 막는다 (M1 단일 정의처).
        `token-budget` 은 어휘 파일의 sha256 도 고정값과 대조한다 — 토큰으로 적은 상한은 계수기가 고정되지
        않으면 상한이 아니다 (결정 p1-chunk-unit-is-tokens, ODD id:cond-tokenizer-lock).
      standard_vocab: 등록 표준 어휘 원문 라벨들 (@prov_o//file · @skos//file, MODULE.bazel http_file 해시 고정).
        주면 그 네임스페이스의 용어가 원문에 정의돼 있는지까지 본다 — 접두사만 맞는 오타를 잡는다.
      gates: 게이트 등록부의 원본 라벨 (//defs:kb.bzl). 주면 게이트 `gate-registry` 가 켜진다 — 코드의 태그
        집합이 `GATES`·`TOOL_TAGS` 리터럴과 같은지, 손으로 둔 `*_GATE` 상수가 없는지, 등록된 id 가 코드에
        닿는지 본다. 그래프 없이도 도는 유일한 검사다 (M1 단일 정의처, 2026-10-02).
      gate_sources: 게이트 `gate-registry` 가 태그를 훑을 소스 라벨들 (`//tools:tools`).
      waivers: docs/waivers.md 라벨. 주면 게이트 id `shacl`(축 `파일`)로 면제된 파일의 shape 위반은 세지
        않고 `WAIVED [shacl]` 줄로만 남긴다 — 위반의 focus node 를 `agt:assertionLocation` 으로 파일에
        사상해 가른다. shape 를 약화하는 대신 면제를 선언하는 자리가 `waivers.md` 하나다
        (agrtls-practices-review C, `kb_chunk_lint_test` 의 `chunk` 면제와 같은 규약).
      **kwargs: py_test 로 전달.
    """
    vocab = Label("@tiktoken_o200k_base//file")  # 게이트 token-budget 의 계수기 지문 (p1-chunk-unit-is-tokens)
    graphs = ontology + shapes + odd + data + standard_vocab + chunk_files + [vocab]
    args = (
        ["--vocab", "$(rootpath %s)" % vocab] +
        _flag_args("--ontology", ontology) +
        _flag_args("--shapes", shapes) +
        _flag_args("--odd", odd) +
        _flag_args("--data", data) +
        _flag_args("--chunk-files", chunk_files) +
        _flag_args("--standard-vocab", standard_vocab) +
        (["--verify-queries", "tools/verify-queries"] if verify_queries else []) +
        (["--residency", "$(rootpath %s)" % residency] if residency else []) +
        (["--waivers", "$(rootpath %s)" % waivers] if waivers else []) +
        (["--gates", "$(rootpath %s)" % gates] if gates else []) +
        _flag_args("--gate-sources", gate_sources) +
        (["--reason"] if reason else [])
    )
    if verify_queries:
        graphs = graphs + [verify_queries]
    if waivers:
        graphs = graphs + [waivers]
    if gates:
        graphs = graphs + gate_sources
    # `residency`·`gates` 가 가리키는 파일은 `_GATES_DATA` 가 이미 넣는다 — 두 번 넣으면 data 중복이 로드 에러다.
    # 둘의 값은 구성상 `//defs:kb.bzl` 하나다(수준 허용표·게이트 등록부의 단일 정의처가 그 파일이므로) — 다르면 여기서 멈춘다
    for label in [l for l in [residency, gates] if l]:
        if str(Label(label)) != str(_GATES_DATA[0]):
            fail("kb_gate_test(%s): residency·gates 는 %s 하나다 — 단일 정의처가 그 파일이다 (받은 값 %s)" %
                 (name, _GATES_DATA[0], label))
    py_test(
        name = name,
        srcs = _VALIDATE_SRCS,
        main = Label("//tools:validate.py"),
        args = args,
        data = _with_gates(graphs),
        deps = _RDF_DEPS,
        size = kwargs.pop("size", "small"),
        **kwargs
    )

def kb_taxonomy(name, ontology, out = "taxonomy.yml"):
    """related/condition 온톨로지에서 OpenODD 택소노미(속성 범주)를 생성한다 (부록 E.4)."""
    native.genrule(
        name = name,
        srcs = ontology,
        outs = [out],
        cmd = "$(location //tools:taxonomy) --out $@ $(SRCS)",
        tools = [Label("//tools:taxonomy")],
    )

def kb_odd_kg(name, src, taxonomy, out):
    """OpenODD 문서(YAML)에서 ODD 그래프(-odd.ttl)를 생성한다 (3.2절, 부록 E.4).

    원본은 YAML이고 TTL은 생성물이다. 속성 범주가 택소노미 밖이거나 판정 방법 없는
    조건이 있으면 생성이 실패한다 — ODD 게이트의 앞 절반이 여기다.
    """
    native.genrule(
        name = name,
        srcs = [src, taxonomy],
        outs = [out],
        cmd = "$(location //tools:odd2kg) --taxonomy $(location %s) --out $@ $(location %s)" % (taxonomy, src),
        tools = [Label("//tools:odd2kg")],
    )

def kb_cq_report(name, data, queries, out = "cq.md"):
    """역량 질문 질의를 전부 돌려 뷰 cq.md 를 생성한다 (docs/competency-questions.md).

    게이트가 아니라 보고다. 행 수와 상위 행의 라벨만 낸다 — 라벨이 인터페이스다.
    """
    native.genrule(
        name = name,
        srcs = data + [queries],
        outs = [out],
        cmd = "$(location //tools:query) --report $@ --queries $(execpaths %s) --ttl %s" % (queries, " ".join(["$(execpaths %s)" % d for d in data])),
        tools = [Label("//tools:query")],
    )

def kb_metrics(name, data, notes = None, bodies = [], out = "metrics.md"):
    """그래프(-kg)에서 코어 지표 metrics.md를 생성한다 (4.13절, 14.1절 통과 조건 세 축의 대리).

    notes·bodies를 주면 확정 문장 커버리지(1단계 의미 보존 대리)도 계산한다.
    plane 순서·수준 순서·수준 허용표는 //defs:kb.bzl 에서 읽는다 — 표의 단일 정의처가 거기다 (M1 단일 정의처).
    """
    residency = Label("//defs:kb.bzl")
    extra = ((" --notes $(location %s)" % notes) if notes else "") + ((" --bodies " + " ".join(["$(execpaths %s)" % b for b in bodies])) if bodies else "")
    native.genrule(
        name = name,
        srcs = data + ([notes] if notes else []) + bodies + [residency],
        outs = [out],
        cmd = "$(location //tools:metrics) --out $@ --residency $(location %s) %s%s" % (residency, " ".join(["$(execpaths %s)" % d for d in data]), extra),
        tools = [Label("//tools:metrics")],
    )

def kb_consistency(name, bodies, glossary = None, waivers = None, theta = "0.5", out = "consistency.md"):
    """청크 파일에서 정합성 보고 consistency.md 를 생성한다 (p4-redundancy-as-safety-margin).

    중복(정확·근사 후보)·coUpdatesWith 묶임과 응집 저하·결론 라벨 형식·용어집 옛 표기. 게이트가 아니라 뷰다 —
    병합·묶기·유지 판정은 재검증 시점에 사람/승인된 판정자가 한다.
    보고는 커밋마다 생성돼야 하므로(docs/rules.md) build_test 로 감싸 `bazel test //...` 가 곧 생성이 되게 한다.
    waivers 를 주면(docs/waivers.md, agrtls-practices-review C) 게이트 id `term-drift` 의 면제 파일을 집계에서 빼되 목록에 남긴다.
    consistency.py 는 chunk2kg.parse_chunk 로 bodies 를 읽으므로 PLANES·LEVELS·STATES 값 어휘의 원본 //defs:kb.bzl 을
    액션 입력으로 주고 경로를 명시로 넘긴다(M1 단일 정의처, 2026-09-26 — 오케스트레이터 판정 2026-09-27: 폴백 없이,
    없으면 죽는다). 호출부(kb/BUILD.bazel)를 고치지 않도록 매크로 안에서 고정으로 더한다.
    """
    residency = Label("//defs:kb.bzl")
    extra = ((" --glossary $(location %s)" % glossary) if glossary else "") + ((" --waivers $(location %s)" % waivers) if waivers else "")
    native.genrule(
        name = name,
        srcs = bodies + ([glossary] if glossary else []) + ([waivers] if waivers else []) + [residency],
        outs = [out],
        cmd = "$(location //tools:consistency) --out $@ --theta %s --residency $(location %s)%s %s" % (
            theta, residency, extra, " ".join(["$(execpaths %s)" % b for b in bodies])
        ),
        tools = [Label("//tools:consistency")],
    )
    build_test(
        name = name + "_build_test",
        targets = [":" + name],
        size = "small",
    )

def kb_community(name, data, out = "communities.md"):
    """그래프(-kg)의 링크 군집에서 communities.md 를 생성한다 (p4-community-detection-proposes-composites).

    같은 plane·level 안의 군집은 복합체 후보, plane·level 을 넘는 군집은 relatedTo 링크 후보 — 판정란은 비어 있고
    채택(복합체 선언)·묶기·기각은 사람이 한다. 뷰이고 게이트가 아니며 생성물은 bazel-bin 에만 있다.
    """
    native.genrule(
        name = name,
        srcs = data,
        outs = [out],
        cmd = "$(location //tools:community) --out $@ %s" % " ".join(["$(execpaths %s)" % d for d in data]),
        tools = [Label("//tools:community")],
    )

def kb_open_questions(name, data, bodies = [], out = "open.md"):
    """head 그래프의 선택 슬롯 `미확정:` 에서 미결 집계 뷰 open.md 를 생성한다 (p4-three-empty-values).

    미결마다 질문 · 그것을 안은 청크(라벨·IRI) · plane/level · 상세 문서를 낸다. 대상은 `agt:bodySlot "미확정"` 인
    청크이고 질문은 그 청크의 본문에서 읽는다. **집계만 맡는다** — 미결의 상세 다섯 절은 42줄 청크에 들어가지 않아
    docs/open-questions.md 색인과 그 아래 문서로 남고 이 뷰가 그것을 대체하지 않는다. 뷰이고 게이트가 아니며
    생성물은 bazel-bin 에만 있다 (STYLEGUIDE §6).

    Args:
      name: 타깃 이름.
      data: 그래프 라벨들 — head(:chunks_kg) 가 있어야 슬롯 표지를 읽는다.
      bodies: 청크 파일 라벨들 (filegroup 가능). 질문 문장이 여기서 나온다.
      out: 생성할 파일명.
    """
    extra = (" --bodies " + " ".join(["$(execpaths %s)" % b for b in bodies])) if bodies else ""
    native.genrule(
        name = name,
        srcs = data + bodies,
        outs = [out],
        cmd = "$(location //tools:open_questions) --out $@ %s%s" % (" ".join(["$(execpaths %s)" % d for d in data]), extra),
        tools = [Label("//tools:open_questions")],
    )

def kb_link_candidates(name, data, k = 7, min_shared = 3, out = "link-candidates.md"):
    """그래프(-kg)의 체계 안 증거에서 복원 후보 뷰 link-candidates.md 를 생성한다 (로드맵 8단계 복원, p10-link-by-construction).

    frontmatter 링크가 없는 살아 있는 청크 쌍에 대해 본문 인용(agt:cites)·테스트 공동 커버(같은 V&V 청크의 verifies)·개념 공유
    (agt:usesConcept 교집합 ≥ min_shared)를 근거로 후보를 내고, TIM 허용 칸(kb_lib.TIM_CELLS)과 defs/kb.bzl 의 단방향 규칙으로 걸러
    앵커당 k 개 이하로 낸다. 판정란은 비어 있고 확정은 사람이 앵커 청크의 frontmatter(링크 키 + restored:)에 적는다
    (p10-candidate-and-confirmed-link · p10-restored-link-marking). 뷰이고 게이트가 아니며 생성물은 bazel-bin 에만 있다.

    Args:
      name: 타깃 이름.
      data: 그래프 라벨들 — head(:chunks_kg) · 참조(:references_kg) · 손으로 쓴 그래프(:kg, 복합체 형제 판정).
      k: 앵커(주어)당 후보 상한 (로드맵 입력표 k ≤ 7).
      min_shared: 개념 공유 후보의 교집합 하한.
      out: 생성할 파일명.
    """
    native.genrule(
        name = name,
        srcs = data,
        outs = [out],
        cmd = "$(location //tools:link) --out $@ --k %d --min-shared %d %s" % (k, min_shared, " ".join(["$(execpaths %s)" % d for d in data])),
        tools = [Label("//tools:link")],
    )

def kb_weave(name, kind, data, bodies = [], out = None):
    """그래프(와 청크 본문)에서 문서 뷰를 생성한다 (4.6절 weave, method §9, p12-documents-are-generated).

    kind 는 adr(결정 복합체의 ADR — bodies 필요) · requirements(요구 색인) · changelog(supersedes 이력) · audit(감사 보고서 —
    그래프와 관측 청크만으로, bodies 에 //kb/vv:bodies·//kb/dev:bodies; 로드맵 8단계 audit-self-sufficiency) 중 하나다.
    생성물마다 머리에 생성 시각(UTC)과 질의를 적는다. 뷰이고 게이트가 아니며 생성물은 bazel-bin 에만 있다 —
    소스 트리에 같은 이름의 파일을 두지 않는다 (STYLEGUIDE §6).

    Args:
      name: 타깃 이름.
      kind: adr | requirements | changelog | audit.
      data: 그래프 라벨들 (-kg · -odd · 온톨로지 모듈) — query·metrics 와 같은 union.
      bodies: 청크 파일 라벨들 (filegroup 가능). adr 의 결론·근거·대안 본문, audit 의 관측(실행 기록·가정 판정) 본문.
      out: 생성할 파일명 (기본 <kind>.md).
    """
    if kind not in ["adr", "requirements", "changelog", "audit"]:
        fail("%s: kind 는 adr | requirements | changelog | audit 중 하나다 — 실제 %r" % (name, kind))
    out = out or kind + ".md"
    # bodies 가 있을 때만 weave.py 가 chunk2kg.parse_chunk 를 부른다 — 그때만 PLANES·LEVELS·STATES 원본(//defs:kb.bzl)이
    # 액션 입력으로 있어야 한다(M1 단일 정의처 — 오케스트레이터 판정 2026-09-27: 폴백 없이, 없으면 죽는다).
    residency = [Label("//defs:kb.bzl")] if bodies else []
    extra = ((" --bodies " + " ".join(["$(execpaths %s)" % b for b in bodies])
              + " --residency $(location %s)" % residency[0]) if bodies else "")
    native.genrule(
        name = name,
        srcs = data + bodies + residency,
        outs = [out],
        cmd = "$(location //tools:weave) --kind %s --out $@ %s%s" % (kind, " ".join(["$(execpaths %s)" % d for d in data]), extra),
        tools = [Label("//tools:weave")],
    )

def kb_skills_drift_test(name, skills, docs, tools = Label("//tools"), **kwargs):
    """생성 skill 드리프트 가드 — tools/gen_skills.py --check 로 트리의 .claude/skills/*/SKILL.md 를 재생성과 비교한다.

    원본은 도구 docstring 과 kb_lib.SKILLS, skill 은 커밋되는 뷰다 (BUILD 와 같은 이유 — 도구가 없어도 skill 이 읽혀야 한다).
    docstring·SKILLS 를 고치고 생성을 안 돌린 경우와 손으로 쓴 skill(이중 원본)을 FAIL [skills-drift] 로 잡는다.

    Args:
      name: 테스트 이름.
      skills: 트리의 skill 파일 라벨 (filegroup — .claude/skills/**/SKILL.md).
      docs: 원본 절 앵커의 실재를 판정할 문서 라벨들 (//docs:docs).
      tools: 도구 소스·BUILD 의 filegroup (docstring 과 py_binary 목록의 원본).
      **kwargs: py_test 로 전달.
    """
    py_test(
        name = name,
        srcs = _GEN_SKILLS_SRCS,
        main = Label("//tools:gen_skills.py"),
        args = ["--check", "--root", "."],
        data = _with_gates([skills, tools] + docs),
        deps = [requirement("rdflib")],  # kb_lib(SKILLS 표의 단일 정의처)가 요구
        size = kwargs.pop("size", "small"),
        **kwargs
    )

def kb_extract_drift_test(name, source, chunks, registry, tools = Label("//tools"), **kwargs):
    """추출 드리프트 가드 — tools/extract.py --check 로 트리의 생성 청크·등록부를 재추출과 비교한다.

    코드가 원본이고 청크는 생성물이다 (p7-code-extraction-direction). 소스를 고치고 추출을 안 돌린 경우와 생성 청크를
    손으로 고친 경우를 FAIL [extract-drift] 로 잡는다. //:build_drift_test·//:skills_drift_test 와 같은 형이다.
    `uses`(agt:usesDefinition) 의 두 경계 — 방출 경계 EXTRACTED_SOURCES 와 치역 경계 USES_TARGETS — 의 단일 정의처
    //defs:kb.bzl 을 --residency 로 준다 (M1, load_residency 와 같은 해법, 2026-10-01) — 샌드박스에 그 파일이
    있어야 extract.py 가 읽는다. 치역 경계 안의 모듈은 그 등록부 사이드카도 입력이다: 모듈 간 `uses` 의 대상
    uuid 가 거기 있고, 없으면 extract.py 가 EXIT_CONFIG 로 죽는다(조용히 비지 않는다).

    Args:
      name: 테스트 이름.
      source: 추출할 소스 파일의 저장소 상대 경로 (문자열).
      chunks: 생성 청크 묶음의 라벨 (filegroup — kb/dev/artifact/<모듈>:bodies).
      registry: 등록부 사이드카의 라벨 (<소스>.chunks.yml).
      tools: 도구 소스의 filegroup — 소스 파일 자신이 여기 있어야 추출이 읽는다.
      **kwargs: py_test 로 전달.
    """
    residency = Label("//defs:kb.bzl")  # EXTRACTED_SOURCES 리터럴의 단일 정의처
    py_test(
        name = name,
        srcs = [
            Label("//tools:extract.py"),
            Label("//tools:kb_lib.py"),
            Label("//tools:chunk2kg.py"),
        ],
        main = Label("//tools:extract.py"),
        args = [source, "--check", "--root", ".", "--residency", "$(rootpath %s)" % residency],
        # 치역 경계 안의 모듈의 등록부 — 모듈 간 `uses` 의 대상 uuid. 자기 등록부는 이미 `registry` 다(중복 금지)
        data = _with_gates([chunks, registry, tools, residency]) +
               ["//tools:%s.chunks.yml" % m for m in USES_TARGETS if "tools/%s.py" % m != source],
        deps = [requirement("rdflib")],  # kb_lib(추출 규약의 단일 정의처)가 요구
        size = kwargs.pop("size", "small"),
        **kwargs
    )

def kb_index(name, srcs, out = "index.md"):
    """청크 head에서 라벨 목록 index.md를 생성한다 (5.6절, 부록 E.2).

    OKF 예약 파일 index.md는 생성물이다 — 손으로 쓰면 본문과 어긋난다.

    Args:
      name: 타깃 이름.
      srcs: 청크 파일 라벨들 (filegroup 가능).
      out: 생성할 파일명 (기본 index.md).
    """
    residency = Label("//defs:kb.bzl")  # labels.py 가 chunk2kg.parse_chunk 를 부른다 — 값 어휘 원본을 액션 입력으로 준다
    native.genrule(
        name = name,
        srcs = srcs + [residency],
        outs = [out],
        cmd = "$(location //tools:labels) --out $@ --residency $(location %s) %s" % (
            residency, " ".join(["$(execpaths %s)" % s for s in srcs])
        ),
        tools = [Label("//tools:labels")],
    )

def kb_reference_kg(name, srcs, out = None, ontology = []):
    """청크 본문의 명시적 인용·개념 사용에서 참조 그래프(-kg)를 생성한다 (8.2절).

    본문이 원본이고 이 그래프는 생성물이다 — 목록을 손으로 복제하면 어긋난다.
    인용 대상이 실재하지 않으면 생성이 실패하므로 참조 무결성이 여기서 강제된다.

    Args:
      name: 타깃 이름.
      srcs: 청크 파일 라벨들 (filegroup 가능).
      out: 생성할 TTL 파일명 (기본 <name>.ttl, 접미사 규약상 -kg 권장).
      ontology: 온톨로지 모듈 라벨들. 주면 본문의 `agt:<Term>` 표기 중 온톨로지가 정의한 용어를
        agt:usesConcept 로도 방출한다 (dependency-graph-design §6 복원 경로, 결정 지점 (f)).
    """
    out = out or name + ".ttl"
    # 빈 filegroup(예: 아직 비어 있는 //kb/vv:bodies)은 $(execpaths) 에서 분석 에러이므로 청크는 $(SRCS) 로 넘긴다.
    # $(SRCS) 에는 온톨로지 파일도 섞이므로 extract_refs 는 위치 인자 중 .md 만 청크로 읽는다.
    onto = (" --ontology " + " ".join(["$(execpaths %s)" % o for o in ontology]) + " --") if ontology else ""
    native.genrule(
        name = name,
        srcs = srcs + ontology,
        outs = [out],
        cmd = "$(location //tools:extract_refs) --out $@%s $(SRCS)" % onto,
        tools = [Label("//tools:extract_refs")],
    )

def kb_chunk_lint_test(name, chunks = [], ttl = [], waivers = None, **kwargs):
    """청크 토큰 상한(4.1절, 게이트 id `chunk`)·TTL 접미사 규약(0.2절)·.md 청크의 산문 문체(게이트 id `prose`) 린트.

    크기의 단위는 줄이 아니라 토큰이고 상한은 저작 산문 1,092 · `artifact`·`memory` 2,856 이다
    (결정 p1-chunk-unit-is-tokens, 유저 결정 2026-10-01 — 줄 상한 42·200 은 폐지됐다). 계수기는 고정된
    어휘 하나(`o200k_base`)이므로 어휘 파일이 이 테스트의 `data` 이고 경로를 `--vocab` 으로 명시해 넘긴다.

    살아 있는 .md 청크는 첨가와 목록 규칙도 본다 — 게이트 id `addition`·`empty-value`·`list-rules`(STYLEGUIDE §0,
    결정 p4-slot-answers-one-question·p4-three-empty-values, 2026-09-22 승격). 검사 함수는 consistency ⑧·⑨ 와 같다.

    waivers 를 주면(docs/waivers.md, agrtls-practices-review C) 그 게이트 id 들(축 파일)로 면제된 파일의 위반은 세지
    않고 `WAIVED` 줄로만 남긴다. TTL 입력은 산문·첨가·목록 검사 대상이 아니다 — chunk_lint 가 .md 에만 돌린다.
    """
    vocab = Label("@tiktoken_o200k_base//file")  # 크기 판정의 계수기 — 어휘가 없으면 판정을 내릴 수 없다
    args = _flag_args("--chunks", chunks) + _flag_args("--ttl", ttl) + ["--vocab", "$(rootpath %s)" % vocab]
    if waivers:
        args += ["--waivers", "$(rootpath %s)" % waivers]
    py_test(
        name = name,
        srcs = _LINT_SRCS,
        main = Label("//tools:chunk_lint.py"),
        args = args,
        data = _with_gates(chunks + ttl + [vocab] + ([waivers] if waivers else [])),
        deps = [
            requirement("rdflib"),  # kb_lib(접미사 규약의 단일 정의처)가 요구
            requirement("tiktoken"),  # 토큰 계수기 (p1-chunk-unit-is-tokens)
        ],
        size = kwargs.pop("size", "small"),
        **kwargs
    )

def kb_doccheck_test(name, srcs, target_only = [], data = [], empty_dirs = [], waivers = None, gates = None, **kwargs):
    """문서 현행성 게이트 — 죽은 링크·앵커·백틱 경로 + 산문 문체 (tools/doccheck.py, agrtls-practices-review N; STYLEGUIDE §0).

    실재 판정은 runfiles 로 한다 — 문서가 가리키는 파일은 `data` 로 선언돼야 실재한다. 선언되지 않은
    파일을 가리키면 FAIL 이고, 그것이 곧 "문서가 가리키는 것은 하네스에 배선돼 있어야 한다"는 뜻이다.
    glob 은 패키지 경계를 넘지 않으므로 다른 패키지의 문서는 그 패키지의 filegroup 으로 넘긴다.

    Args:
      name: 테스트 이름.
      srcs: 검사할 문서 라벨들 (안에서 나가는 링크·경로를 본다). 비어 있으면 SKIP(비영 종료).
      target_only: 링크 대상으로만 쓰는 문서 라벨들 — srcs 에도 있으면 검사하지 않는다 (유저 문서
        docs/agent-knowledge-system-notes.md). 빈 filegroup 은 줄 수 없다 ($(rootpaths) 가 비면 분석 에러).
      data: 문서가 가리키는 파일들의 라벨 (filegroup 가능, 비어 있어도 된다) — 실재의 근거.
      empty_dirs: 파일이 없어 runfiles 에 나타나지 않는 디렉토리(빈 패키지 — kb/vv, space 처럼 자리만 있는 것).
        문서가 그 디렉토리를 가리키는 것은 옳으므로 여기서 실재를 선언한다.
      waivers: docs/waivers.md 라벨. 주면 게이트 id `prose`(축 파일)로 면제된 문서의 산문 위반(경어·감탄)은 세지 않는다.
      gates: 게이트 등록부의 원본 라벨 (//defs:kb.bzl). 주면 `docs/tools.md` 게이트 총람이 `GATES` 리터럴의
        투영인지 본다 — 표의 `id` 열에 등록부 밖의 id 가 있으면 FAIL 이고, 총람에 없는 등록 id 는 보고다
        (3단계에서 표 자체를 생성 뷰로 바꾼다).
      **kwargs: py_test 로 전달.
    """
    args = ["$(rootpaths %s)" % s for s in srcs]
    for t in target_only:
        args += ["--target-only", "$(rootpaths %s)" % t]
    for d in empty_dirs:
        args += ["--empty-dir", d]
    if waivers:
        args += ["--waivers", "$(rootpath %s)" % waivers]
    if gates:
        args += ["--gates", "$(rootpath %s)" % gates]
    py_test(
        name = name,
        srcs = _DOCCHECK_SRCS,
        main = Label("//tools:doccheck.py"),
        args = args,
        data = _with_gates(srcs + target_only + data + ([waivers] if waivers else [])),
        deps = [requirement("rdflib")],  # kb_lib(종료 코드 규약의 단일 정의처)가 요구
        size = kwargs.pop("size", "small"),
        **kwargs
    )

def kb_gendoc_test(name, docs, data = [], empty_dirs = [], **kwargs):
    """생성 문서 게이트 — 에이전트가 만드는 마크다운의 규약 G1~G18 (tools/gendoc.py, 유저 지시 2026-09-21).

    `kb_doccheck_test` 와 달리 검사 대상이 **생성물**이다. 생성 뷰 타깃을 그대로 `docs` 에 주면
    테스트가 그것을 빌드해 runfiles 에 놓고, 같은 runfiles 로 링크 대상의 실재를 판정한다 —
    생성물이 가리키는 파일도 `data` 에 선언돼야 실재한다.

    Args:
      name: 테스트 이름.
      docs: 검사할 생성 문서 타깃들 (genrule·rule 의 출력, 또는 생성 트리 파일의 filegroup).
      data: 생성물이 가리키는 파일들의 라벨 — 실재의 근거.
      empty_dirs: 파일이 없어 runfiles 에 나타나지 않지만 실재하는 디렉토리(빈 패키지).
      **kwargs: py_test 로 전달.
    """
    args = ["$(rootpaths %s)" % d for d in docs]
    for d in empty_dirs:
        args += ["--empty-dir", d]
    py_test(
        name = name,
        srcs = _GENDOC_SRCS,
        main = Label("//tools:gendoc.py"),
        args = args,
        data = _with_gates(docs + data),
        deps = [requirement("rdflib")],  # kb_lib(규약의 단일 정의처)가 요구
        size = kwargs.pop("size", "small"),
        **kwargs
    )

def kb_runner_env_test(name, probe = "chunk_lint", **kwargs):
    """실행기 환경 격리 게이트 — 케이스의 명령이 실행기의 파이썬·runfiles 문맥을 물려받지 않는지 판정한다
    (tools/vv_run_env_test.py, 결정 p8-verifier-env-isolation, 논평 runner-env-leaks-into-case).

    다른 게이트와 달리 검사 대상이 **도구 자신의 동작**이다. 실행기 전체는 케이스가 `bazel test` 를 부르므로
    테스트 타깃이 될 수 없지만(중첩 실행), `clean_env()` 와 `run_command()` 는 bazel 을 부르지 않는다.
    대상을 격리의 동작으로 좁히면 중첩 없이 `bazel test //...` 안에 든다.

    자극은 실제 하위 프로세스다 — `probe` 검증기의 소스를 data 로 놓아 runfiles 에서 `python3 tools/<probe>.py`
    로 부른다. 그 형태가 케이스가 쓰는 형태와 같아야 격리가 케이스에 대해 판정된다.

    Args:
      name: 테스트 이름.
      probe: 하위 프로세스로 띄울 읽기 전용 검증기 이름 (vv_run.READ_ONLY_VERIFIERS 안).
      **kwargs: py_test 로 전달.
    """
    py_test(
        name = name,
        srcs = _RUNNER_ENV_SRCS,
        main = Label("//tools:vv_run_env_test.py"),
        args = ["--probe", probe],
        data = _with_gates([Label("//tools:%s.py" % probe)]),
        # 검증기는 케이스가 부르는 그대로 워크스페이스 셸의 `python3` 로 돈다 — 그 해석기의 사용자 site-packages 는
        # HOME 아래에 있고, 실행기가 도는 `bazel run` 은 클라이언트의 HOME 을 그대로 물려준다. 테스트도 같은 조건에
        # 두어야 자극이 케이스의 자극과 같다. 격리가 깨지면 그 전에 `import kb_lib` 에서 죽는다
        env_inherit = ["HOME"],
        deps = [
            requirement("rdflib"),  # kb_lib(종료 코드 규약의 단일 정의처)가 요구
            requirement("pyyaml"),  # vv_run 이 케이스 본문의 `yaml` 펜스를 읽는다 — import 에 필요하다
        ],
        size = kwargs.pop("size", "small"),
        **kwargs
    )
