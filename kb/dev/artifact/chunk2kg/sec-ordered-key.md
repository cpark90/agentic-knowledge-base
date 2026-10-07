---
id: https://agentic-knowledge-base.dev/id/chunk/c4902423-8b93-4f1a-8c9e-22ff76076b32
type: artifact
level: executable
title_ko: 절 ordered-key (tools/chunk2kg.py)
title: section ordered-key in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/7b4508d3-c314-4c0b-a04f-4f86b63bf62e
composite: {id: https://agentic-knowledge-base.dev/id/composite/7b4508d3-c314-4c0b-a04f-4f86b63bf62e, title_ko: 절 복합체 ordered-key (tools/chunk2kg.py), title: section composite ordered-key in tools/chunk2kg.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/c4902423-8b93-4f1a-8c9e-22ff76076b32, https://agentic-knowledge-base.dev/id/chunk/040b7a8d-10e8-4e6e-96db-b8495e467218], part_of: https://agentic-knowledge-base.dev/id/composite/28e52252-d603-4c96-b7ee-f85197b0d7da}
---
**절** — `tools/chunk2kg.py` 의 절 `ordered-key` 다. 복합체의 순서 (결정 p4-composite-order-is-declared, 유저 승인 2026-09-29 — 예외 없음)

**정의** — `order_errors` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 복합체의 순서 (결정 p4-composite-order-is-declared, 유저 승인 2026-09-29 — 예외 없음) ─────────────────
# frontmatter 의 **복합체 키**와 순서의 선언 — 이 절이 판정하는 것이다.
#   part_of:      소속 복합체 IRI (선택) — 복합체는 멤버 중 하나가 composite: 로 선언
#   composite:    {id: …, title_ko: …, title: …, ordered: [<부분 IRI>…], part_of: <상위 복합체 IRI>} (선택) — 복합체 개체 선언.
#                 `part_of` 는 선택 키이며 **선언된 복합체**가 다른 복합체의 직접 부분임을 적는다 (p4-composite-as-part-of —
#                 복합체는 청크 또는 다른 복합체를 부분으로 갖는다). 청크의 최상위 `part_of` 와 자리가 다르다: 앞은 청크의
#                 소속, 뒤는 복합체의 소속이다. 상위 복합체도 같은 실행의 입력 집합 안에서 선언돼야 하고 사슬은 순환하지
#                 않는다. 코드 추출(p7-code-links-on-file-composite)의 파일 → 장·절 → 함수 세 단이 이 키로 선다. `ordered` 는 선택 키이고
#                 순서가 뜻을 갖는 복합체만 적는다 (결정 p4-composite-order-is-declared). 있으면 `agt:Composite , co:List` 로
#                 타이핑하고 부분마다 `co:item [ a co:ListItem ; co:index "<1..n>"^^xsd:positiveInteger ; co:itemContent <부분> ]`
#                 을 그 순서로 낸다. 없으면 `agt:hasDirectPart` 만 낸다(순서 없음) — 순서를 요구하지 않는 것에 순서를 붙이면
#                 거짓 정보다. 목록이 부분 전부를 빠짐없이 한 번씩 담지 않으면 거부한다. **예외는 없다** — 결정 복합체도 선언으로만
#                 순서를 갖고(유저 승인 2026-09-29) 그 선언은 `--ordered` 인자로 들어온다. 이 도구는 역할 이름으로 순서를 추측하지 않는다.
#                 **묶음의 단위는 파일이 아니라 이 실행의 입력 집합**이다 (2026-09-26 반영). part_of 대상은 같은 실행의 파일 어딘가에서
#                 composite: 로 선언돼야 한다. 그 입력 집합을 만드는 것이 defs/kb.bzl 의 kb_decision(결론·근거·대안 셋)과
#                 kb_composite(부분 2~9 가변)이고, 청크 하나만 받는 kb_chunk 로는 복합체가 서지 않는다
#   --ordered:    묶음의 복합체가 선언한 부분의 순서 (인자, 선택) — 생성 BUILD 의 `kb_decision.ordered`·`kb_composite.ordered` 가 넘긴다.
#                 결정 복합체 205개의 선언이 이 자리다 (유저 승인 2026-09-29: 예외 없음, 손으로 frontmatter 를 고치지 않는다).
#                 frontmatter `composite.ordered` 와 함께 있으면 같아야 한다 — BUILD 는 뷰이고 frontmatter 가 원본이다
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
# 복합체 → 함수 청크의 세 단은 부분 상한 9(4.5절) 안에서 파일 하나를 담는 유일한 형태다.
PART_OF_KEY = "part_of"
```
<!-- 인용 끝 -->
