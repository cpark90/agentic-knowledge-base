"""지식 산출물용 게이트 매크로.

지식 파일(TTL·청크 본문)은 데이터 타깃이고, 검사 게이트(노트 6.7절)는 테스트 타깃이다.
`bazel test //...` 가 곧 게이트 전체 실행이다.
"""

load("@bazel_skylib//rules:build_test.bzl", "build_test")
load("@kb_pip//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_test")

_VALIDATE_SRCS = [
    Label("//tools:validate.py"),
    Label("//tools:kb_lib.py"),
]

_LINT_SRCS = [
    Label("//tools:chunk_lint.py"),
    Label("//tools:chunk2kg.py"),  # 논평 본문의 파서 comment_form — 게이트와 방출기가 같은 판정을 쓴다 (p7-commentary-form)
    Label("//tools:kb_lib.py"),
]

_DOCCHECK_SRCS = [
    Label("//tools:doccheck.py"),
    Label("//tools:kb_lib.py"),
]

_GENDOC_SRCS = [
    Label("//tools:gendoc.py"),
    Label("//tools:kb_lib.py"),
]

_GEN_SKILLS_SRCS = [
    Label("//tools:gen_skills.py"),
    Label("//tools:doccheck.py"),
    Label("//tools:kb_lib.py"),
]

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
        verify_queries = None,
        reason = False,
        standard_vocab = [],
        **kwargs):
    """검사 게이트 테스트 — tools/validate.py 를 지정 그래프들에 대해 돌린다.

    Args:
      name: 테스트 이름.
      ontology: T-Box 모듈 라벨들 (*-ontology, *-rules).
      shapes: SHACL shape 라벨들 (*-shapes).
      odd: ODD 라벨들 (*-odd). 주면 agt:refersTo → ODD 참조 게이트가 켜진다.
      data: A-Box 라벨들 (*-kg, *-space). 통제 어휘 검사 대상.
      reason: SHACL 전에 OWL-RL 추론 적용.
      standard_vocab: 등록 표준 어휘 원문 라벨들 (@prov_o//file · @skos//file, MODULE.bazel http_file 해시 고정).
        주면 그 네임스페이스의 용어가 원문에 정의돼 있는지까지 본다 — 접두사만 맞는 오타를 잡는다.
      **kwargs: py_test 로 전달.
    """
    graphs = ontology + shapes + odd + data + standard_vocab
    args = (
        _flag_args("--ontology", ontology) +
        _flag_args("--shapes", shapes) +
        _flag_args("--odd", odd) +
        _flag_args("--data", data) +
        _flag_args("--standard-vocab", standard_vocab) +
        (["--verify-queries", "tools/verify-queries"] if verify_queries else []) +
        (["--reason"] if reason else [])
    )
    if verify_queries:
        graphs = graphs + [verify_queries]
    py_test(
        name = name,
        srcs = _VALIDATE_SRCS,
        main = Label("//tools:validate.py"),
        args = args,
        data = graphs,
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
    """
    extra = ((" --notes $(location %s)" % notes) if notes else "") + ((" --bodies " + " ".join(["$(execpaths %s)" % b for b in bodies])) if bodies else "")
    native.genrule(
        name = name,
        srcs = data + ([notes] if notes else []) + bodies,
        outs = [out],
        cmd = "$(location //tools:metrics) --out $@ %s%s" % (" ".join(["$(execpaths %s)" % d for d in data]), extra),
        tools = [Label("//tools:metrics")],
    )

def kb_consistency(name, bodies, glossary = None, waivers = None, theta = "0.5", out = "consistency.md"):
    """청크 파일에서 정합성 보고 consistency.md 를 생성한다 (p4-redundancy-as-safety-margin).

    중복(정확·근사 후보)·coUpdatesWith 묶임과 응집 저하·결론 라벨 형식·용어집 옛 표기. 게이트가 아니라 뷰다 —
    병합·묶기·유지 판정은 재검증 시점에 사람/승인된 판정자가 한다.
    보고는 커밋마다 생성돼야 하므로(docs/rules.md) build_test 로 감싸 `bazel test //...` 가 곧 생성이 되게 한다.
    waivers 를 주면(docs/waivers.md, agrtls-practices-review C) 게이트 id `term-drift` 의 면제 파일을 집계에서 빼되 목록에 남긴다.
    """
    extra = ((" --glossary $(location %s)" % glossary) if glossary else "") + ((" --waivers $(location %s)" % waivers) if waivers else "")
    native.genrule(
        name = name,
        srcs = bodies + ([glossary] if glossary else []) + ([waivers] if waivers else []),
        outs = [out],
        cmd = "$(location //tools:consistency) --out $@ --theta %s%s %s" % (theta, extra, " ".join(["$(execpaths %s)" % b for b in bodies])),
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
    extra = (" --bodies " + " ".join(["$(execpaths %s)" % b for b in bodies])) if bodies else ""
    native.genrule(
        name = name,
        srcs = data + bodies,
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
        data = [skills, tools] + docs,
        deps = [requirement("rdflib")],  # kb_lib(SKILLS 표의 단일 정의처)가 요구
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
    native.genrule(
        name = name,
        srcs = srcs,
        outs = [out],
        cmd = "$(location //tools:labels) --out $@ $(SRCS)",
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
    """청크 42줄 제한(4.1절)·TTL 접미사 규약(0.2절)·.md 청크의 산문 문체(STYLEGUIDE §0, 게이트 id `prose`) 린트.

    살아 있는 .md 청크는 첨가와 목록 규칙도 본다 — 게이트 id `addition`·`empty-value`·`list-rules`(STYLEGUIDE §0,
    결정 p4-slot-answers-one-question·p4-three-empty-values, 2026-09-22 승격). 검사 함수는 consistency ⑧·⑨ 와 같다.

    waivers 를 주면(docs/waivers.md, agrtls-practices-review C) 그 게이트 id 들(축 파일)로 면제된 파일의 위반은 세지
    않고 `WAIVED` 줄로만 남긴다. TTL 입력은 산문·첨가·목록 검사 대상이 아니다 — chunk_lint 가 .md 에만 돌린다.
    """
    args = _flag_args("--chunks", chunks) + _flag_args("--ttl", ttl)
    if waivers:
        args += ["--waivers", "$(rootpath %s)" % waivers]
    py_test(
        name = name,
        srcs = _LINT_SRCS,
        main = Label("//tools:chunk_lint.py"),
        args = args,
        data = chunks + ttl + ([waivers] if waivers else []),
        deps = [requirement("rdflib")],  # kb_lib(접미사 규약의 단일 정의처)가 요구
        size = kwargs.pop("size", "small"),
        **kwargs
    )

def kb_doccheck_test(name, srcs, target_only = [], data = [], empty_dirs = [], waivers = None, **kwargs):
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
      **kwargs: py_test 로 전달.
    """
    args = ["$(rootpaths %s)" % s for s in srcs]
    for t in target_only:
        args += ["--target-only", "$(rootpaths %s)" % t]
    for d in empty_dirs:
        args += ["--empty-dir", d]
    if waivers:
        args += ["--waivers", "$(rootpath %s)" % waivers]
    py_test(
        name = name,
        srcs = _DOCCHECK_SRCS,
        main = Label("//tools:doccheck.py"),
        args = args,
        data = srcs + target_only + data + ([waivers] if waivers else []),
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
        data = docs + data,
        deps = [requirement("rdflib")],  # kb_lib(규약의 단일 정의처)가 요구
        size = kwargs.pop("size", "small"),
        **kwargs
    )
