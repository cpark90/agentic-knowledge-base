---
id: https://agentic-knowledge-base.dev/id/chunk/a26b506d-3439-46e5-a9cf-2e53eb4a0300
type: artifact
level: executable
title_ko: 절 clean-env (tools/vv_run.py)
title: section clean-env in tools/vv_run.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T20:48:33Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/9f79d119-83cf-46a7-89c0-680e8f203296, https://agentic-knowledge-base.dev/id/chunk/b8d74a2d-f94b-4fe7-8b3b-13dca638d338, https://agentic-knowledge-base.dev/id/chunk/36a0b6fa-ac60-47db-a769-b49d067f6854]
part_of: https://agentic-knowledge-base.dev/id/composite/38aa6392-7bfb-42b7-84e5-6278007e131f
composite: {id: https://agentic-knowledge-base.dev/id/composite/38aa6392-7bfb-42b7-84e5-6278007e131f, title_ko: 절 복합체 clean-env (tools/vv_run.py), title: section composite clean-env in tools/vv_run.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/a26b506d-3439-46e5-a9cf-2e53eb4a0300, https://agentic-knowledge-base.dev/id/chunk/4b6ece88-9936-435d-b114-96c75670880e, https://agentic-knowledge-base.dev/id/chunk/72467e81-75de-4b48-92ac-2d429de91d8e, https://agentic-knowledge-base.dev/id/chunk/dda506f2-0686-4187-a9dc-b23cf1e83388, https://agentic-knowledge-base.dev/id/chunk/a52db838-3103-4131-8ba5-17b938049c08, https://agentic-knowledge-base.dev/id/chunk/4f74f6b4-a466-4f0e-95c2-4f22a919fbd0], part_of: https://agentic-knowledge-base.dev/id/composite/5fc8dfb1-4583-4c27-8266-44c34557e4c1}
---
**절** — `tools/vv_run.py` 의 절 `clean-env` 다. 명령 실행과 환경 격리

**정의** — `clean_env` · `run_command` · `tests_note` · `materialize` · `substitute` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 명령 실행과 환경 격리 ────────────────────











NEAR_LINES = 40      # 근접 줄을 찾는 범위 — 출력의 마지막 40줄. 게이트의 FAIL 줄은 끝에 모인다
NEAR_RATIO = 0.4     # 이 아래면 근접 줄이라 부르지 않는다 — 무관한 줄을 "가장 가까운" 이라 적으면 수정 방향이 아니다
```
<!-- 인용 끝 -->
