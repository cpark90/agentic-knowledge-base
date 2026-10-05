---
id: https://agentic-knowledge-base.dev/id/chunk/fc5b71dc-3637-48e3-a344-aeac11fcbb88
type: norm
level: logical
title_ko: AGENTS.md 절 — 셀프체크
title: AGENTS.md section — Self-check
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-04T04:37:29+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/1267fef2-8d09-45ef-94f3-ee31ceaafac9
heading: 셀프체크
depth: 2
---
작업 완료 전 반드시 실행한다.

```bash
bazel test //...        # 게이트 전체. 반드시 PASS
bazel run //tools:canonicalize -- --write <기계 생성 TTL>   # 커밋 전 정규화
python3 tools/gen_build.py --root .        # frontmatter 링크를 고쳤으면 BUILD 재생성 (//:build_drift_test)
python3 tools/gen_skills.py --root .       # 도구 docstring·kb_lib.SKILLS 를 고쳤으면 skill 재생성 (//:skills_drift_test)
bazel run //tools:extract -- <소스>       # 소스를 고쳤으면 코드 청크 재추출 (//:extract_drift_test)
```
