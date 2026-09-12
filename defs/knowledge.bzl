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

def kb_chunk_kg(name, srcs, out = None):
    """청크 파일들의 frontmatter에서 head 그래프(-kg)를 생성한다 (4.3절).

    한 청크는 한 파일이다 — head 메타데이터는 청크 파일 안에 있고, kg의
    head 그래프는 이 규칙이 생성한다. lineCount·assertionLocation은 파일에서
    계산되므로 손으로 쓴 메타데이터와 어긋날 수 없다.

    Args:
      name: 타깃 이름.
      srcs: 청크 파일 라벨들 (filegroup 가능).
      out: 생성할 TTL 파일명 (기본 <name>.ttl, 접미사 규약상 -kg 권장).
    """
    out = out or name + ".ttl"
    native.genrule(
        name = name,
        srcs = srcs,
        outs = [out],
        cmd = "$(location //tools:chunk2kg) --out $@ $(SRCS)",
        tools = [Label("//tools:chunk2kg")],
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

def kb_consistency(name, bodies, glossary = None, theta = "0.5", out = "consistency.md"):
    """청크 파일에서 정합성 보고 consistency.md 를 생성한다 (p4-redundancy-as-safety-margin).

    중복(정확·근사 후보)·coUpdatesWith 묶임과 응집 저하·결론 라벨 형식·용어집 옛 표기. 게이트가 아니라 뷰다 —
    병합·묶기·유지 판정은 재검증 시점에 사람/승인된 판정자가 한다.
    보고는 커밋마다 생성돼야 하므로(docs/rules.md) build_test 로 감싸 `bazel test //...` 가 곧 생성이 되게 한다.
    """
    extra = (" --glossary $(location %s)" % glossary) if glossary else ""
    native.genrule(
        name = name,
        srcs = bodies + ([glossary] if glossary else []),
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

def kb_workset(name, role, data, levels = "", anchor = "", budget = 200, out = None):
    """역할의 작업 집합 뷰 workset-<role>.md — 라벨 목록 + 앵커 이웃, 예산 패킹 (0.5절, 5.6절). 저장하지 않는 질의 결과다."""
    out = out or "workset-%s.md" % role
    native.genrule(
        name = name,
        srcs = data + ["//kb/dev:bodies"],
        outs = [out],
        cmd = "$(location //tools:workset) --role %s --levels '%s' --anchor '%s' --budget %d --root . --out $@ %s" % (role, levels, anchor, budget, " ".join(["$(execpaths %s)" % d for d in data])),
        tools = [Label("//tools:workset")],
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

def kb_chunk_lint_test(name, chunks = [], ttl = [], **kwargs):
    """청크 42줄 제한(4.1절)과 TTL 접미사 규약(0.2절) 린트."""
    args = _flag_args("--chunks", chunks) + _flag_args("--ttl", ttl)
    py_test(
        name = name,
        srcs = _LINT_SRCS,
        main = Label("//tools:chunk_lint.py"),
        args = args,
        data = chunks + ttl,
        deps = [requirement("rdflib")],  # kb_lib(접미사 규약의 단일 정의처)가 요구
        size = kwargs.pop("size", "small"),
        **kwargs
    )
