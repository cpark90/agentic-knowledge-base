---
id: https://agentic-knowledge-base.dev/id/chunk/782db9bf-fe98-4c49-89d5-5143bc44c0c6
type: artifact
level: executable
title_ko: 모듈 머리 exit-fail (tools/doccheck.py)
title: module head exit-fail in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/b5da82da-f5cc-4c80-9fbf-d65784ffee7d
---
**모듈 머리** — `tools/doccheck.py` 의 모듈 머리 `exit-fail` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
EXIT_FAIL = kb_lib.EXIT_FAIL      # 판정 실패
EXIT_CONFIG = kb_lib.EXIT_CONFIG  # 파일 없음·인자 오류·읽을 수 없는 입력
EXIT_SKIP = kb_lib.EXIT_SKIP      # 검사 대상 0건 — PASS 가 아니다

TAG = kb_lib.DOCCHECK_GATE
FROZEN = kb_lib.FROZEN_GATE  # 동결 문서 게이트 id — 원본 해시의 단일 정의처는 kb_lib.FROZEN_DOCS
PROSE = kb_lib.PROSE_GATE  # 산문 게이트 id — waivers.md 가 같은 이름으로 면제를 선언한다
PATH_PREFIXES = ("kb/", "kg/", "tools/", "docs/", "defs/", "chunks/", "space/", "harness/", ".claude/")
SKIP_MARKS = ("*", "<", "{", "…", "$", "//", "bazel-bin/", "bazel-out", ".wip")
# 마크다운 구조 헬퍼는 kb_lib 이 원본이다 — doccheck·weave·gen_skills·gendoc 이 같은 앵커 규칙을 쓴다
SCHEME, FENCE, HEADING, CODE_SPAN = kb_lib.MD_SCHEME, kb_lib.MD_FENCE, kb_lib.MD_HEADING, kb_lib.MD_CODE_SPAN
MD_LINK, HTML_TAG = kb_lib.MD_LINK_TEXT, kb_lib.MD_HTML_TAG
prose_lines, slug, anchors, find_links = kb_lib.md_lines, kb_lib.slug, kb_lib.md_anchors, kb_lib.find_links
FILE_LINE = re.compile(r":\d+(?:-\d+)?$")
```
<!-- 인용 끝 -->
