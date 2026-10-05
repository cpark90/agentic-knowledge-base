---
id: https://agentic-knowledge-base.dev/id/chunk/7a685532-9783-48e8-9af5-649c4bcf4934
type: artifact
level: executable
title_ko: 절 norm-type (tools/chunk2kg.py)
title: section norm-type in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/679fc45f-a074-446c-aa6b-755cb0329d4f
composite: {id: https://agentic-knowledge-base.dev/id/composite/679fc45f-a074-446c-aa6b-755cb0329d4f, title_ko: 절 복합체 norm-type (tools/chunk2kg.py), title: section composite norm-type in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/7a685532-9783-48e8-9af5-649c4bcf4934, https://agentic-knowledge-base.dev/id/chunk/9397f206-c8b3-40ab-8fb8-d286bf02749f, https://agentic-knowledge-base.dev/id/chunk/4eb70032-9c6d-47dc-a0b0-34e02f426e80, https://agentic-knowledge-base.dev/id/chunk/8c16b743-c8b1-4799-9c5b-5b003686ac07, https://agentic-knowledge-base.dev/id/chunk/0771e060-41a6-434b-bb56-61bcf3e3b7ec, https://agentic-knowledge-base.dev/id/chunk/cc796185-bb2d-4940-a069-48a9334eecc8, https://agentic-knowledge-base.dev/id/chunk/15c626f2-ee68-4a3b-a918-8a5054875a54], part_of: https://agentic-knowledge-base.dev/id/composite/28e52252-d603-4c96-b7ee-f85197b0d7da}
---
**절** — `tools/chunk2kg.py` 의 절 `norm-type` 다. 규범 문서의 절 (결정 p12-norm-documents-from-section-chunks, 유저 답 Q19-b·Q21-a·Q22-b)

**정의** — `parse_norm_ref` · `parse_norm_items` · `norm_item_slugs` · `check_norm_keys` · `check_norm_bundle_form` · `norm_bundle_errors` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 규범 문서의 절 (결정 p12-norm-documents-from-section-chunks, 유저 답 Q19-b·Q21-a·Q22-b) ─────────────────
# frontmatter 의 **절 키** — `type: norm` 에서만 쓴다. 문서 하나가 `kb/dev/norm/<문서 stem>/` 의 복합체 하나이고 순서는
# 선언 청크(머리 청크)의 `composite.ordered` 다. 머리 청크의 본문은 문서 도입문·범례이고 절 키를 갖지 않는다.
#   heading:   절 제목 (머리 청크 밖에서 필수). 번호를 두지 않는다 — 번호는 생성기(tools/gen_norms.py)가 순서로 붙인다
#   depth:     2 또는 3 (머리 청크 밖에서 필수) — 생성 문서의 `##`·`###`
#   items:     순서 목록 (선택). 항목은 셋 중 하나다 — `slug#k` · `slug#k + slug2`(둘째 결정은 링크만) ·
#              `{규약: slug#k, 하위: [slug#k, …]}`. `slug` 는 결정 디렉토리 이름, `k` 는 그 결정의 `conventions.md` 안
#              `규약:` 줄의 1부터의 순번이다. 결정 복합체로의 `agt:projectsConvention` 이 여기서 나온다
#   numbered:  true | false (선택, 절 청크만, 기본 true) — false 면 생성기가 이 depth 2 절에 번호를 붙이지 않고 번호를 소비하지도
#              않는다(문서 끝의 `셀프체크` 같은 부록 절). depth 3 절에서는 뜻이 없어 거부한다
#   numbering: 첫 depth 2 절의 번호 꼴 (선택, 머리 청크만) — `§0.` · `1.` · `0.` 처럼 접두·첫 수·마침표. 없으면 번호가 없다
#   strength:  required | optional (선택, 머리 청크만, 기본 required) — required 면 이 문서가 싣는 `규약:` 줄은 전부
#              `[지킴]`·`[권장]` 강도를 가져야 한다(생성기가 거부한다). 표 절의 줄은 예외 없이 강도를 갖지 않는다
# 절 청크 하나는 항목 묶음 하나(목록 하나 또는 표 하나)를 갖고 본문은 그 묶음 **앞**의 산문이다. 묶음의 꼴은 다음 키가 정한다.
#   form:        bullets | ordered | table (선택, 절 청크만, 기본 bullets, items 가 있을 때만) — ordered 는 항목마다 `1.` 을 낸다
#   columns:     [열 머리, …] (form: table 일 때만, 그때 필수) — 비지 않은 서로 다른 문자열
#   link_column: 열 머리 (선택, columns 가 있을 때만) — columns 의 마지막 원소여야 한다. 그 열의 칸은 생성기가 항목의
#                `slug#k + slug2` 에서 결정 링크로 낸다. 없으면 생성기가 표 바로 앞에 `원본: …` 한 줄을 낸다
#   continues:   true | false (선택, 절 청크만, 기본 false) — true 면 heading·depth·numbered 가 없는 **이어짐 절 청크**다.
#                본문은 앞 묶음 뒤의 산문이고 자기 묶음을 가질 수 있다. 깊이는 앞 절을 잇고 번호를 소비하지 않는다.
#                문서의 첫 절에는 둘 수 없다(순서를 아는 생성기가 판정한다). 그래프에는 agt:sectionContinues true 로 낸다
# 표 절의 `규약:` 줄은 `a | b | c` 꼴이다(바깥 파이프 없음, 링크 열 제외). 칸 수·강도는 생성기가 판정한다.
# 줄의 실재·고아·이중 소비는 문서 전체와 결정 전체를 아는 생성기가 판정한다 — 이 도구는 형식만 본다.
NORM_TYPE = "norm"
NORM_HEADING_KEY, NORM_DEPTH_KEY, NORM_ITEMS_KEY = "heading", "depth", "items"
NORM_NUMBERING_KEY, NORM_STRENGTH_KEY, NORM_NUMBERED_KEY = "numbering", "strength", "numbered"
NORM_FORM_KEY, NORM_COLUMNS_KEY, NORM_LINK_COLUMN_KEY, NORM_CONTINUES_KEY = "form", "columns", "link_column", "continues"
NORM_SECTION_KEYS = (NORM_HEADING_KEY, NORM_DEPTH_KEY, NORM_ITEMS_KEY, NORM_NUMBERED_KEY,  # 절 청크의 키 — 머리 청크는 갖지 않는다
                     NORM_FORM_KEY, NORM_COLUMNS_KEY, NORM_LINK_COLUMN_KEY, NORM_CONTINUES_KEY)
NORM_HEAD_KEYS = (NORM_NUMBERING_KEY, NORM_STRENGTH_KEY)                  # 머리 청크(복합체 선언)만의 키
NORM_DEPTHS = ("2", "3")
NORM_STRENGTHS = ("required", "optional")
NORM_NUMBERED_VALUES = ("true", "false")  # frontmatter 값은 문자열로 읽힌다(parse_value) — 기본 true
NORM_FORMS = ("bullets", "ordered", "table")  # 항목 묶음의 꼴 — 기본 bullets
NORM_FORM_DEFAULT, NORM_FORM_TABLE = "bullets", "table"
NORM_CONTINUES_VALUES = ("true", "false")  # 기본 false
NORM_ITEM_MAIN, NORM_ITEM_SUB = "규약", "하위"  # 하위 항목을 가진 항목의 맵 키
NORM_REF = re.compile(r"^([a-z0-9][a-z0-9-]*)#([1-9][0-9]*)$")  # `slug#k`
NORM_SLUG = re.compile(r"^[a-z0-9][a-z0-9-]*$")
NORM_NUMBERING = re.compile(r"^(\D*?)([0-9]+)\.$")  # 접두(§ 등) + 첫 번호 + 마침표
NORM_HEADING_NUMBERED = re.compile(r"^(§|[0-9]+\.)")  # 손 번호 — 번호는 생성기가 붙인다
# 결정 복합체 → 절 청크의 규약 줄 투영 술어 (norm-section-ontology.ttl). 대상 IRI 는 `--convention-target slug=IRI` 로 받는다
PROJECTS_CONVENTION_PREDICATE = "agt:projectsConvention"














# LEVELS·STATES(값 어휘)는 위에서 defs/kb.bzl 에서 파생된다(load_plane_level_state) — 여기서 다시 선언하지 않는다.
HANGUL = re.compile(r"[ㄱ-ㆎ가-힣]")  # 한글 음절·자모 — 라벨 언어 검사 (0.6절 표기 형식)
REQUIRED = ("id", "type", "level", "title_ko", "title", "status", "generated")

PREAMBLE = """\
# 생성 파일 — 손으로 고치지 않는다. 원본은 각 청크 파일의 frontmatter다.
# 생성: tools/chunk2kg.py (bazel build //kg:chunks_kg)
@prefix agt: <https://agentic-knowledge-base.dev/agt/> .
@prefix co: <http://purl.org/co/> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
"""
```
<!-- 인용 끝 -->
