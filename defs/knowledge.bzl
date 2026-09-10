"""지식 산출물용 게이트 매크로.

지식 파일(TTL·청크 본문)은 데이터 타깃이고, 검사 게이트(노트 6.7절)는 테스트 타깃이다.
`bazel test //...` 가 곧 게이트 전체 실행이다.
"""

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
        **kwargs):
    """검사 게이트 테스트 — tools/validate.py 를 지정 그래프들에 대해 돌린다.

    Args:
      name: 테스트 이름.
      ontology: T-Box 모듈 라벨들 (*-ontology, *-rules).
      shapes: SHACL shape 라벨들 (*-shapes).
      odd: ODD 라벨들 (*-odd). 주면 agt:refersTo → ODD 참조 게이트가 켜진다.
      data: A-Box 라벨들 (*-kg, *-space). 통제 어휘 검사 대상.
      reason: SHACL 전에 OWL-RL 추론 적용.
      **kwargs: py_test 로 전달.
    """
    graphs = ontology + shapes + odd + data
    args = (
        _flag_args("--ontology", ontology) +
        _flag_args("--shapes", shapes) +
        _flag_args("--odd", odd) +
        _flag_args("--data", data) +
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

def kb_metrics(name, data, out = "metrics.md"):
    """그래프(-kg)에서 코어 지표 metrics.md를 생성한다 (4.13절, 14.1절 통과 조건)."""
    native.genrule(
        name = name,
        srcs = data,
        outs = [out],
        cmd = "$(location //tools:metrics) --out $@ $(SRCS)",
        tools = [Label("//tools:metrics")],
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

def kb_reference_kg(name, srcs, out = None):
    """청크 본문의 명시적 인용에서 참조 그래프(-kg)를 생성한다 (8.2절).

    본문이 원본이고 이 그래프는 생성물이다 — 목록을 손으로 복제하면 어긋난다.
    인용 대상이 실재하지 않으면 생성이 실패하므로 참조 무결성이 여기서 강제된다.

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
        cmd = "$(location //tools:extract_refs) --out $@ $(SRCS)",
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
