---
id: https://agentic-knowledge-base.dev/id/chunk/f128d09c-7a12-42c1-adb4-65e6b8b83f69
type: artifact
level: executable
title_ko: 절 md-fence (tools/kb_lib.py)
title: section md-fence in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/ff72735f-0f6b-4d18-b673-004825efe869, https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd, https://agentic-knowledge-base.dev/id/chunk/120eba0b-c9d8-433e-9f52-d35502589c23]
part_of: https://agentic-knowledge-base.dev/id/composite/5c506aa2-9c1f-48ba-b959-5260d60d13ac
composite: {id: https://agentic-knowledge-base.dev/id/composite/5c506aa2-9c1f-48ba-b959-5260d60d13ac, title_ko: 절 복합체 md-fence (tools/kb_lib.py), title: section composite md-fence in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/f128d09c-7a12-42c1-adb4-65e6b8b83f69, https://agentic-knowledge-base.dev/id/chunk/078b2808-e9ad-4d17-b2a5-9ab6a30d04f0, https://agentic-knowledge-base.dev/id/chunk/07b69002-1dea-4097-9ab5-18b1bc332898, https://agentic-knowledge-base.dev/id/chunk/a9138ecc-8714-414e-a8f3-69d0c646e65d, https://agentic-knowledge-base.dev/id/chunk/0a822cf9-05aa-4c0f-90e3-b293ed84a187, https://agentic-knowledge-base.dev/id/chunk/ecb06437-81f9-480c-90ba-0b78a8fde56b, https://agentic-knowledge-base.dev/id/chunk/a0841084-48a1-45f6-842a-57f5b8cbf0c9], part_of: https://agentic-knowledge-base.dev/id/composite/2fee8437-c9b3-4f23-a1d9-a0ec5e3891b0}
---
**절** — `tools/kb_lib.py` 의 절 `md-fence` 다. 마크다운 구조 헬퍼 — 펜스·제목 앵커·링크 (doccheck 과 생성 문서 게이트의 공용)

**정의** — `frontmatter_end` · `md_lines` · `slug` · `heading_anchors` · `md_anchors` · `find_links` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 마크다운 구조 헬퍼 — 펜스·제목 앵커·링크 (doccheck 과 생성 문서 게이트의 공용) ────────────────
# 앵커 규칙은 GitHub 과 같다. doccheck·weave·gen_skills·gendoc 이 모두 여기를 쓴다 (STYLEGUIDE §7).
MD_FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
MD_HEADING = re.compile(r"^ {0,3}(#{1,6})[ \t]+(.*?)(?:[ \t]+#+)?[ \t]*$")
MD_CODE_SPAN = re.compile(r"(`+)(.+?)\1")
MD_LINK_TEXT = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
MD_HTML_TAG = re.compile(r"<[^>]+>")
MD_SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:")
```
<!-- 인용 끝 -->
