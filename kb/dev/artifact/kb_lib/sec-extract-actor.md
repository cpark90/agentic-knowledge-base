---
id: https://agentic-knowledge-base.dev/id/chunk/0ae6e19c-609b-4bb9-a904-7f7e9f7e97c9
type: artifact
level: executable
title_ko: 절 extract-actor (tools/kb_lib.py)
title: section extract-actor in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/a228d4f1-cdb8-4a79-bd48-f9b961eaa607
composite: {id: https://agentic-knowledge-base.dev/id/composite/a228d4f1-cdb8-4a79-bd48-f9b961eaa607, title_ko: 절 복합체 extract-actor (tools/kb_lib.py), title: section composite extract-actor in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/0ae6e19c-609b-4bb9-a904-7f7e9f7e97c9, https://agentic-knowledge-base.dev/id/chunk/3e0a2fd1-776d-4762-b6e5-538b8cd4987d], part_of: https://agentic-knowledge-base.dev/id/composite/9b61f2e4-e29d-4fe0-8a4f-f1be5708e79a}
---
**절** — `tools/kb_lib.py` 의 절 `extract-actor` 다. 코드의 추출 (extract — p7-code-extraction-direction · p7-code-links-on-file-composite, 유저 승인 2026-09-30)

**정의** — `code_part` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 코드의 추출 (extract — p7-code-extraction-direction · p7-code-links-on-file-composite, 유저 승인 2026-09-30) ──────
# 코드가 원본이고 함수 청크는 생성물이다. 규약의 단일 정의처가 여기이고 추출기(tools/extract.py)와 게이트가 같은 것을 읽는다.
#   등록부   소스 파일 옆의 사이드카 `<소스>.chunks.yml` — 한정 이름 → uuid 의 원본. 손으로 쓰는 것은 정체성(uuid)과
#            파일 단위 링크(refines·serves)뿐이고, 신설 uuid·소스 시각·소스 해시는 추출기가 더한다. 사이드카를 소스 옆에
#            두는 까닭은 둘이다 — 생성 트리(kb/dev/artifact/)는 바이트 동일 비교 대상이라 손 파일을 둘 수 없고,
#            소스와 같은 디렉토리에 있어야 이동·개명이 한 diff 에 들어온다
#   한정 이름 `file`(파일 복합체) · `module`(파일 청크) · `section:<키>` · `composite:<키>` · `fn:<함수명>`
#   절 키    그 절에서 처음 나오는 최상위 이름 — 소스에서 계산되고 등록부가 그 이름에 uuid 를 붙인다
#   생성물   kb/dev/artifact/<모듈>/ 의 청크 전부. 손으로 고치면 게이트 `extract-drift` 가 거부한다
EXTRACT_ACTOR = "process:extract"     # generated.by — 역할이 아니라 프로세스다. writer 검사 대상 밖이다 (validate check_writer)
# `artifact` 의 `verified` 는 사람 검토가 아니라 **테스트 통과**다 (p7-code-extraction-direction "도장"). 도장의 자리는
# 등록부의 `tested: {rev, at, source_hash}` 이고 추출기가 `source_hash` 가 지금 소스와 같을 때만 `verified` 를 낸다 —
# 소스가 도장 뒤에 바뀌면 `verified` 가 빠져 수정 뒤 미검증이 되고 재판정이 자동이다. 사람 도장은 결정·요구에 남는다.
STAMP_ACTOR = "process:bazel-test"    # verified.by — 판정 주체가 사람에서 게이트로 바뀐 자리다
STAMP_KEY = "tested"                  # 등록부의 도장 필드
EXTRACT_ROOT = KB_DEV + "/artifact"   # 생성 청크가 사는 곳 — 파일 하나 = 패키지 하나
EXTRACT_REGISTRY_SUFFIX = ".chunks.yml"  # 등록부 사이드카 — tools/kb_lib.py → tools/kb_lib.chunks.yml
# 절 주석의 깊이 — 상자 그리기 문자가 깊이를 정한다. `═` 가 장, `─` 가 절이다. 소스의 절 주석이 복합체 구조의 원본이고
# 추출기는 순서를 뜻으로 읽는다(코드의 순서는 뜻을 가진다). 부분 상한 9(4.5절)를 넘으면 잘라 맞추지 않고 절 주석을 요구한다
EXTRACT_MARKERS = {"═": 1, "─": 2}
EXTRACT_MARKER_RE = re.compile(r"^#\s*([═─])\1+\s*(.*?)\s*[═─]*\s*$")
# 인용 구역 — 생성 청크가 소스에서 그대로 옮긴 자리. 생성기는 원문을 고쳐 쓰지 않는다(p7-code-extraction-direction).
# 산문·첨가·목록 게이트는 코드 펜스 안을 이미 판정하지 않으므로(prose_segments·md_lines) 이 표지는 그 사실의 선언이다.
SOURCE_QUOTE_OPEN = "<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->"
SOURCE_QUOTE_CLOSE = "<!-- 인용 끝 -->"
# 코드 부분 청크 — 추출 트리 안에서 복합체의 부분인 청크(정의 청크와 절·장·모듈 머리의 구역 청크)다. 링크의 자리는 파일
# 복합체의 선언 청크인 파일 청크 하나이므로(p7-code-links-on-file-composite, 유저 결정 Q47-b) 부분은 아래 종류의 링크
# 끝점이 아니다. 복원 후보 생성기(link `R_CODE_PART`)와 게이트 `code-part-link`(validate check_code_part_link)가 이 판정 하나를 쓴다
CODE_PART_LINK_KINDS = ("refines", "serves", "verifies")
```
<!-- 인용 끝 -->
