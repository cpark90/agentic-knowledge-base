---
id: https://agentic-knowledge-base.dev/id/chunk/e976e617-0bab-4b65-a4e7-8ae7faf43f54
type: artifact
level: executable
title_ko: 절 gate-input-roots (tools/gen_build.py)
title: section gate-input-roots in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-07T09:06:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/6f567db9-617b-4afe-bc62-3ae6f78e6dce
composite: {id: https://agentic-knowledge-base.dev/id/composite/6f567db9-617b-4afe-bc62-3ae6f78e6dce, title_ko: 절 복합체 gate-input-roots (tools/gen_build.py), title: section composite gate-input-roots in tools/gen_build.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/e976e617-0bab-4b65-a4e7-8ae7faf43f54, https://agentic-knowledge-base.dev/id/chunk/13aadb6d-6816-4906-8368-5b13dc8dd3f2, https://agentic-knowledge-base.dev/id/chunk/9ea0c3bb-9662-498e-a0ad-c8a481ad765f, https://agentic-knowledge-base.dev/id/chunk/c2012ece-9826-4be9-bfdc-24eaf1fda875, https://agentic-knowledge-base.dev/id/chunk/535d310e-db77-40f1-a678-68d3de7d9727], part_of: https://agentic-knowledge-base.dev/id/composite/9bb41e68-1b5c-4d4c-aee0-32a2899bedf9}
---
**절** — `tools/gen_build.py` 의 절 `gate-input-roots` 다. 게이트 입력 — 어느 타깃에도 들지 않은 지식 파일 (pe-knowledge-files-are-gate-inputs, 유저 답 Q80-a)

**정의** — `_glob_pattern` · `_build_of` · `check_gate_inputs` · `source_root` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 게이트 입력 — 어느 타깃에도 들지 않은 지식 파일 (pe-knowledge-files-are-gate-inputs, 유저 답 Q80-a) ────────────────────
# 지식 파일은 소유 패키지(가장 가까운 BUILD 의 디렉토리)의 BUILD 가 이름이나 glob 으로 담아야 filegroup·kb_chunk 의
# 입력이 된다. 담지 않으면 그 파일을 보는 게이트가 없다 — gen_build 가 모르는 디렉토리를 kb/ 아래에 만들면 그렇게 된다.
GATE_INPUT_ROOTS = ("kb",)  # 지식 파일의 뿌리 — 채널(harness/)은 그래프 밖이라 대상이 아니다 (STYLEGUIDE §8)
_GLOB_CALL = re.compile(r"glob\(\s*\[([^\]]*)\]\s*(?:,\s*exclude\s*=\s*\[([^\]]*)\])?", re.S)
_QUOTED = re.compile(r'"([^"]+)"')
```
<!-- 인용 끝 -->
