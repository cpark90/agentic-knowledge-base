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
        "plane": "requirement | decision | contract | schema | artifact | annotation | memory",
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

LEVELS = ["functional", "abstract", "logical", "concrete", "executable"]
PLANES = ["requirement", "decision", "contract", "schema", "artifact", "annotation", "memory"]  # 5.2절 단방향 순서
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
}
STATES = ["draft", "stable", "suspect", "invalidated", "deprecated"]

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
    """검증 액션 — bazel build 만으로 42줄·frontmatter·첨가·목록 검사가 돈다 (validation output group).

    면제 선언(docs/waivers.md)을 함께 읽는다. 면제는 코드가 아니라 그 표에 있고(AGENTS.md·STYLEGUIDE §8),
    게이트 id 는 prose·addition·empty-value·list-rules 다. 표를 주지 않으면 청크를 겨눈 면제가 이 액션에만
    적용되지 않아 //kb/...:lint_test 와 판정이 갈린다.
    """
    marker = ctx.actions.declare_file(ctx.label.name + ".lint.ok")
    waivers = ctx.file._waivers
    ctx.actions.run_shell(
        inputs = files + [waivers],
        outputs = [marker],
        tools = [ctx.executable._lint],
        command = "%s --chunks %s --waivers %s && touch %s" % (
            ctx.executable._lint.path,
            " ".join([f.path for f in files]),
            waivers.path,
            marker.path,
        ),
        mnemonic = "KbChunkLint",
        progress_message = "청크 검사 %s" % ctx.label,
    )
    return marker

def _head_action(ctx, files, ordered = []):
    """타깃 하나의 head 그래프 조각 — chunk2kg --fragment. 프런트매터 오류·복합체 불일치는 여기서 실패한다.

    PLANES·LEVELS·STATES 값 어휘의 원본은 //defs:kb.bzl 이다(M1 단일 정의처, 2026-09-26). chunk2kg 가 그 리터럴을
    읽으려면 샌드박스에 파일이 있어야 하므로 _residency 를 명시 입력으로 준다 — _waivers 를 //docs:waivers 로 준
    것과 같은 방식이다. 경로는 하드코딩하지 않고 --residency 인자로 넘긴다.

    `ordered` 는 이 묶음의 복합체가 선언한 부분의 순서다 (p4-composite-order-is-declared, 유저 승인 2026-09-29 — 예외 없음).
    비어 있으면 순서를 넘기지 않고 생성기도 추측하지 않는다. 결정 복합체의 선언이 이 자리로 들어온다 — 손으로 205개
    frontmatter 를 고치지 않고 생성 BUILD 의 명시 인자를 원본으로 둔다.
    """
    out = ctx.actions.declare_file(ctx.label.name + ".head.ttl")
    residency = ctx.file._residency
    args = ["--fragment", "--out", out.path, "--residency", residency.path]
    for iri in ordered:  # 부분마다 한 번 — 목록형 인자는 위치 인자인 청크 파일을 삼킨다
        args = args + ["--ordered", iri]
    ctx.actions.run(
        executable = ctx.executable._chunk2kg,
        arguments = args + [f.path for f in files],
        inputs = files + [residency],
        outputs = [out],
        mnemonic = "KbHead",
        progress_message = "head 그래프 조각 %s" % ctx.label,
    )
    return out

_LINK_ATTRS = {
    "refines": attr.label_list(providers = [ChunkInfo], doc = "정제 — 더 높은 수준의 항목으로 (6.2절)"),
    "serves": attr.label_list(providers = [ChunkInfo], doc = "기여 — 결정이 봉사하는 요구 (6.8절, ⊑ refines)"),
    "supersedes": attr.label_list(providers = [ChunkInfo], doc = "대체 — 같은 plane 의 옛 항목 (7.4절)"),
    "verifies": attr.label_list(providers = [ChunkInfo], doc = "검증 — V&V 청크만 주어 (8.5절)"),
    "_lint": attr.label(default = "//tools:chunk_lint", executable = True, cfg = "exec"),
    "_waivers": attr.label(default = "//docs:waivers", allow_single_file = True, doc = "게이트 면제 선언 (docs/waivers.md)"),
    "_chunk2kg": attr.label(default = "//tools:chunk2kg", executable = True, cfg = "exec"),
    "_residency": attr.label(default = "//defs:kb.bzl", allow_single_file = True, doc = "PLANES·LEVELS·STATES 값 어휘의 원본 (M1 단일 정의처)"),
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

MAX_PARTS = 9  # 직접 부분의 상한 (7±2, 4.5절) — shape kb/ontology/shapes/composite-shapes.ttl 의 sh:maxCount 와 같은 수

def _check_order(label, ordered, part_iris):
    """선언된 순서가 부분 전부를 빠짐없이 한 번씩 담는가 — 분석 시점 fail. 색인 1..n 의 정합성은 shape 가 본다."""
    if sorted(ordered) != sorted(part_iris):
        fail("%s: ordered 가 부분 집합과 다르다 — 순서 목록은 부분 전부를 빠짐없이 한 번씩 담는다 (p4-composite-order-is-declared): %s ≠ %s" %
             (label, ordered, part_iris))

def _composite_outputs(ctx, plane, level, files, part_iris, ordered = []):
    """복합체 규칙 둘(kb_decision·kb_composite)이 공유하는 산출 — head 조각 하나·검사 액션 하나·provider.

    묶음의 단위가 **액션의 입력 집합**이다. 부분 청크 전부와 composite: 선언 청크가 한 액션의 입력이라
    chunk2kg --fragment 가 그 안에서 part_of 대상을 찾아 복합체 개체를 방출한다 (파일 하나 = 묶음 하나가 아니다).

    `ordered` 가 있으면 head 액션이 co:List 와 co:index 를 그 순서로 낸다. 없으면 순서가 없다 — 추측하지 않는다.
    """
    head = _head_action(ctx, files, ordered)
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
    return _composite_outputs(ctx, ctx.attr.plane, ctx.attr.level, ctx.files.srcs, ctx.attr.part_iris, ctx.attr.ordered)

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
        "plane": attr.string(mandatory = True, values = PLANES, doc = "복합체와 부분 전부의 plane (동질성)"),
        "level": attr.string(mandatory = True, values = LEVELS, doc = "복합체와 부분 전부의 level (동질성)"),
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
    _check_order(ctx.label, ctx.attr.ordered, ctx.attr.part_iris)  # 결정도 예외가 없다 — 순서는 선언이고 인자가 필수다
    files = [ctx.file.conclusion, ctx.file.rationale, ctx.file.alternatives]
    return _composite_outputs(ctx, "decision", levels[0], files, ctx.attr.part_iris, ctx.attr.ordered)

kb_decision = rule(
    implementation = _kb_decision_impl,
    doc = """결정 복합체 = 타깃 하나 (결론·근거·대안 셋 고정). 대안이 없으면 로드 시점에 실패한다 — 대안 청크 필수(7.4절)의 구조 형태.

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
        "iri": attr.string(mandatory = True, doc = "복합체 IRI"),
        "part_iris": attr.string_list(mandatory = True, doc = "결론·근거·대안 청크 IRI"),
        "ordered": attr.string_list(mandatory = True, doc = "선언된 읽기 순서 — 결론·근거·대안. gen_build 가 넣는다(유저 승인 2026-09-29: 결정도 예외 없이 선언한다)"),
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
    args.add("--root", ".")
    args.add("--out", out)
    args.add_all(ttl)
    ctx.actions.run(
        executable = ctx.executable._workset,
        arguments = [args],
        inputs = ctx.files.data,
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
    },
)
