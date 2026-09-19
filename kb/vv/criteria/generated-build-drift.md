---
id: https://agentic-knowledge-base.dev/id/chunk/fdd0b6c0-473b-47d1-b23e-b1e862416964
type: contract
level: logical
title_ko: frontmatter와 어긋난 BUILD는 검사 모드가 거부하고 커밋된 생성 BUILD는 전부 원본과 일치한다
title: A BUILD that disagrees with the frontmatter is rejected in check mode and every committed generated BUILD matches its source
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:45:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/e853e578-c267-4a55-8497-739fa3ed863d]
---
**합격 기준** — 기준 종류는 **명세 대조**다. 생성 대상 BUILD마다 `render(frontmatter) == 커밋본`이 바이트 단위로 성립한다. 명세는 각 청크의 frontmatter이고 BUILD는 그 뷰다.

**판정식**

- 음성(원본 변경): 청크의 frontmatter 한 값을 바꾸고 BUILD를 다시 생성하지 않은 채 `python3 tools/gen_build.py --check --root .`를 돌리면 `FAIL [build-drift] <BUILD>: frontmatter 와 어긋난다`로 끝나고 종료 코드가 1이다.
- 음성(뷰 변경): BUILD를 손으로 고쳐도 같은 메시지로 끝난다.
- 결정론: 같은 frontmatter에서 생성기를 두 번 돌린 출력이 같다. `--check`의 PASS가 이를 함의한다.
- 양성: `bazel test //:build_drift_test`가 PASS이고 출력에 `PASS [build-drift] — 생성 BUILD N개가 원본과 일치`가 있다.

**등급** — B다. 판정은 기계가 하되 생성기 재실행의 비용이 있다.

기준의 대상은 `gen_build`가 생성하는 BUILD 전부(`kb/dev/requirement`·`kb/dev/decision`·`kb/dev/memory`·`chunks/decision`·온톨로지 모듈)이고 판정의 원본은 `tools/gen_build.py`의 `main`이다.
