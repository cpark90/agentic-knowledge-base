---
id: https://agentic-knowledge-base.dev/id/chunk/c34e4a59-5cb0-4d80-8835-757a656aa25d
type: artifact
level: executable
title_ko: 절 max-parts (defs/kb.bzl)
title: section max-parts in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/f39dff5d-eec4-44a9-a9eb-ac03d49b15bb
composite: {id: https://agentic-knowledge-base.dev/id/composite/f39dff5d-eec4-44a9-a9eb-ac03d49b15bb, title_ko: 절 복합체 max-parts (defs/kb.bzl), title: section composite max-parts in defs/kb.bzl, ordered: [https://agentic-knowledge-base.dev/id/chunk/c34e4a59-5cb0-4d80-8835-757a656aa25d, https://agentic-knowledge-base.dev/id/chunk/1bd8f244-2394-47da-84b8-ccc6b62491f3, https://agentic-knowledge-base.dev/id/chunk/9ea0fc86-c0a7-40b9-9890-52de62a048a9, https://agentic-knowledge-base.dev/id/chunk/2293c3e9-50cc-4f0a-a8f4-3fa05b5eb583], part_of: https://agentic-knowledge-base.dev/id/composite/84e893d0-8cc4-4710-b3b9-3885ce121377}
---
**절** — `defs/kb.bzl` 의 절 `max-parts` 다. 복합체 규칙 (`kb_composite`·`kb_decision`) — 부분의 수·순서·결정의 세 청크를 분석 시점에 강제한다

**정의** — `_check_order` · `_kb_composite_impl` · `_kb_decision_impl` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
# ── 복합체 규칙 (`kb_composite`·`kb_decision`) — 부분의 수·순서·결정의 세 청크를 분석 시점에 강제한다 ─────────
MAX_PARTS = 9  # 직접 부분의 상한 (7±2, 4.5절) — shape kb/ontology/shapes/composite-shapes.ttl 의 sh:maxCount 와 같은 수




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
```
<!-- 인용 끝 -->
