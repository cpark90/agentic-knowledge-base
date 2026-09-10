"""지식 항목을 Bazel 타깃으로 — provider·규칙·가시성 (bazel-dependency-review B + 연결성, 2026-09-11).

원칙: 의존의 원본은 그래프(frontmatter·owl:imports)이고 BUILD는 생성물(tools/gen_build.py)이다.
Bazel이 맡는 것은 링크의 **구조** — 끝점의 존재(로드 시점), 방향(가시성·분석 시점 fail), 파급(rdeps).
링크의 **의미**(SHACL·통제 어휘·상태 전이)는 그래프 게이트(d-0157 union)가 그대로 맡는다.
"""

ChunkInfo = provider(
    doc = "지식 항목(청크 또는 결정 복합체)이 의존자에게 내보내는 것 — 링크의 끝점은 파일이 아니라 plane·level을 아는 타깃이다.",
    fields = {
        "iri": "항목 IRI (복합체면 복합체 IRI)",
        "plane": "requirement | decision | contract | schema | artifact | annotation | memory",
        "level": "functional | abstract | logical | concrete | executable (복합체면 결론의 수준)",
        "status": "draft | stable | suspect | invalidated | deprecated",
        "srcs": "청크 파일들 (depset)",
        "parts": "복합체의 부분 IRI 목록 (청크면 빈 목록)",
    },
)

OntologyModuleInfo = provider(
    doc = "온톨로지 모듈(디렉토리)이 내보내는 것 — owl:imports 가 deps 다.",
    fields = {"iri": "모듈 IRI", "srcs": "TTL 파일들 (depset)", "imports": "가져오는 모듈의 IRI 목록"},
)

LEVELS = ["functional", "abstract", "logical", "concrete", "executable"]
PLANES = ["requirement", "decision", "contract", "schema", "artifact", "annotation", "memory"]  # 5.2절 단방향 순서
RESIDENCY = {  # 수준 허용표 (6.4절, residency-shapes.ttl 과 같은 내용 — 분석 시점 판정)
    "requirement": ["functional"],
    "decision": ["abstract", "logical", "concrete"],
    "contract": ["abstract", "logical"],
    "schema": ["logical", "concrete"],
    "artifact": ["concrete", "executable"],
    "memory": ["concrete"],
    "annotation": LEVELS,
}
STATES = ["draft", "stable", "suspect", "invalidated", "deprecated"]

def _check_residency(label, plane, level):
    if plane not in PLANES:
        fail("%s: 알 수 없는 plane %r" % (label, plane))
    if level not in RESIDENCY[plane]:
        fail("%s: 수준 허용표 위반 — plane %s 는 level %s 에 살 수 없다 (6.4절)" % (label, plane, level))

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
    for dep in ctx.attr.verifies:
        if not ctx.label.package.startswith("kb/vv"):
            fail("%s: verifies 의 주어는 V&V KB 청크뿐이다 (8.5절)" % ctx.label)
        if not dep.label.package.startswith("kb/dev"):
            fail("%s: verifies 의 대상은 개발 KB 청크다: %s" % (ctx.label, dep.label))
        if dep[ChunkInfo].level != level:
            fail("%s: verifies 는 같은 수준끼리 (8.3절 검증 대응물): %s ≠ %s" % (ctx.label, level, dep[ChunkInfo].level))

def _lint_action(ctx, files):
    """검증 액션 — bazel build 만으로 42줄·frontmatter 검사가 돈다 (validation output group)."""
    marker = ctx.actions.declare_file(ctx.label.name + ".lint.ok")
    ctx.actions.run_shell(
        inputs = files,
        outputs = [marker],
        tools = [ctx.executable._lint],
        command = "%s --chunks %s && touch %s" % (ctx.executable._lint.path, " ".join([f.path for f in files]), marker.path),
        mnemonic = "KbChunkLint",
        progress_message = "청크 검사 %s" % ctx.label,
    )
    return marker

_LINK_ATTRS = {
    "refines": attr.label_list(providers = [ChunkInfo], doc = "정제 — 더 높은 수준의 항목으로 (6.2절)"),
    "serves": attr.label_list(providers = [ChunkInfo], doc = "기여 — 결정이 봉사하는 요구 (6.8절, ⊑ refines)"),
    "supersedes": attr.label_list(providers = [ChunkInfo], doc = "대체 — 같은 plane 의 옛 항목 (7.4절)"),
    "verifies": attr.label_list(providers = [ChunkInfo], doc = "검증 — V&V 청크만 주어 (8.5절)"),
    "_lint": attr.label(default = "//tools:chunk_lint", executable = True, cfg = "exec"),
}

def _kb_chunk_impl(ctx):
    _check_residency(ctx.label, ctx.attr.plane, ctx.attr.level)
    if ctx.attr.status not in STATES:
        fail("%s: 알 수 없는 status %r" % (ctx.label, ctx.attr.status))
    _check_links(ctx, ctx.attr.plane, ctx.attr.level)
    src = ctx.file.src
    return [
        DefaultInfo(files = depset([src])),
        ChunkInfo(iri = ctx.attr.iri, plane = ctx.attr.plane, level = ctx.attr.level, status = ctx.attr.status, srcs = depset([src]), parts = []),
        OutputGroupInfo(_validation = depset([_lint_action(ctx, [src])])),
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

def _kb_decision_impl(ctx):
    levels = ctx.attr.part_levels
    if len(levels) != 3 or len(ctx.attr.part_iris) != 3:
        fail("%s: 결정은 결론·근거·대안 세 청크의 복합체다 (7.4절)" % ctx.label)
    for lv in levels:
        _check_residency(ctx.label, "decision", lv)
    if ctx.attr.status not in STATES:
        fail("%s: 알 수 없는 status %r" % (ctx.label, ctx.attr.status))
    _check_links(ctx, "decision", levels[0])
    files = [ctx.file.conclusion, ctx.file.rationale, ctx.file.alternatives]
    return [
        DefaultInfo(files = depset(files)),
        ChunkInfo(iri = ctx.attr.iri, plane = "decision", level = levels[0], status = ctx.attr.status, srcs = depset(files), parts = ctx.attr.part_iris),
        OutputGroupInfo(_validation = depset([_lint_action(ctx, files)])),
    ]

kb_decision = rule(
    implementation = _kb_decision_impl,
    doc = "결정 복합체 = 타깃 하나 (결론·근거·대안). 대안이 없으면 로드 시점에 실패한다 — 대안 청크 필수(7.4절)의 구조 형태.",
    attrs = dict({
        "conclusion": attr.label(allow_single_file = [".md"], mandatory = True),
        "rationale": attr.label(allow_single_file = [".md"], mandatory = True),
        "alternatives": attr.label(allow_single_file = [".md"], mandatory = True),
        "iri": attr.string(mandatory = True, doc = "복합체 IRI"),
        "part_iris": attr.string_list(mandatory = True, doc = "결론·근거·대안 청크 IRI"),
        "part_levels": attr.string_list(mandatory = True, doc = "결론·근거·대안의 수준"),
        "status": attr.string(default = "stable", values = STATES),
    }, **_LINK_ATTRS),
)

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
