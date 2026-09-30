---
id: https://agentic-knowledge-base.dev/id/chunk/c4902423-8b93-4f1a-8c9e-22ff76076b32
type: artifact
level: executable
title_ko: 절 ordered-key (tools/chunk2kg.py)
title: section ordered-key in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/ab66f02d-6126-4507-b73a-c29429769f11, https://agentic-knowledge-base.dev/id/chunk/01f6a247-ed75-405f-b286-3d59b8acc9d2, https://agentic-knowledge-base.dev/id/chunk/28655d6b-d000-4f43-8d68-9e0ce042c39c]
part_of: https://agentic-knowledge-base.dev/id/composite/7b4508d3-c314-4c0b-a04f-4f86b63bf62e
composite: {id: https://agentic-knowledge-base.dev/id/composite/7b4508d3-c314-4c0b-a04f-4f86b63bf62e, title_ko: 절 복합체 ordered-key (tools/chunk2kg.py), title: section composite ordered-key in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/c4902423-8b93-4f1a-8c9e-22ff76076b32, https://agentic-knowledge-base.dev/id/chunk/040b7a8d-10e8-4e6e-96db-b8495e467218], part_of: https://agentic-knowledge-base.dev/id/composite/f7d6eec7-bef4-4e94-ac55-36e7dda654ce}
---
**절** — `tools/chunk2kg.py` 의 절 `ordered-key` 다. 복합체의 순서 (결정 p4-composite-order-is-declared, 유저 승인 2026-09-29 — 예외 없음)

**정의** — `order_errors` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 복합체의 순서 (결정 p4-composite-order-is-declared, 유저 승인 2026-09-29 — 예외 없음) ─────────────────
# 순서는 **선언**이다. 선언이 있을 때만 co:List 와 co:index 를 방출하고, 없으면 hasDirectPart 만 낸다(순서 없음) —
# 순서를 요구하지 않는 것에 순서를 붙이면 거짓 정보다(d-0073). 목록은 부분 전부를 빠짐없이 한 번씩 담아야 하고
# 어긋나면 이 게이트가 거부한다. **도구는 역할 이름·파일 stem 으로 순서를 추측하지 않는다** — 추측 갈래는 유저 판정
# (2026-09-29, 선택지 2)으로 삭제됐다. 결정 복합체 205개도 예외가 아니고 선언을 gen_build 가 생성 BUILD 의 명시 인자
# (`kb_decision.ordered`)로 넣어 `--ordered` 로 이 도구에 들어온다 — 손으로 205개 frontmatter 를 고치는 것이 첨가이기 때문이다.
# 선언의 자리는 둘이고 둘 다 명시다: 저작한 복합체는 frontmatter `composite.ordered`, 생성된 결정 복합체는 `--ordered` 인자다.
# 둘이 함께 있으면 같아야 한다 — 생성 BUILD 는 뷰이고 frontmatter 가 원본이므로 불일치는 드리프트다.
# hasDirectPart 는 순서와 무관하게 IRI 순으로 낸다 — community·weave·audit 이 그 술어를 읽고 순서 트리플은 추가일 뿐이다.
ORDERED_KEY = "ordered"
# 복합체가 다른 복합체의 부분이 되는 자리 (p4-composite-as-part-of "복합체는 청크 또는 다른 복합체를 부분으로 갖는다").
# 청크의 최상위 `part_of` 는 그 청크가 어느 복합체의 부분인가이고, `composite.part_of` 는 **선언된 복합체**가 어느
# 복합체의 부분인가다. 코드의 추출(p7-code-links-on-file-composite)이 이 자리를 처음 쓴다 — 파일 복합체 → 장·절
# 복합체 → 함수 청크의 세 층은 부분 상한 9(4.5절) 안에서 파일 하나를 담는 유일한 형태다.
PART_OF_KEY = "part_of"


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
