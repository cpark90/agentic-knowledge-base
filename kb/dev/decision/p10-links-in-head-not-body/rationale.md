---
id: https://agentic-knowledge-base.dev/id/chunk/d031916e-2866-496c-b858-e12d5a03ae62
type: decision
level: logical
title_ko: head는 본문이 아니므로 링크를 head에 두어도 본문은 자기 링크를 모른다
title: The head is not the body, so links in the head leave the body unaware of its links
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T17:45:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/2280fd28-d481-4b52-94d4-aab439be78b1
---
**근거** (노트 10.5절 `[확정]`, 4.3절, 9.10절) — 노트 10.5절의 이유 셋이 그대로 적용된다. 산출물을 열지 않고 링크를 만들고 질의한다. 산출물 형식마다 링크 표기를 정하지 않는다. 링크 모델의 저장·시각화·검사를 산출물과 독립적으로 교체한다.

- 한 청크는 한 파일이고 frontmatter가 head다. 링크를 frontmatter에 두면 위 셋이 성립한다 — 생성기는 head만 읽고 본문 형식을 모른다.
- 확정과 후보를 다른 자리에 두는 이유는 후보가 Bazel deps가 되지 않게 하기 위해서다(노트 9.10절, `p9-candidate-storage`).
- 본문의 식별자 인용은 링크가 아니라 후보의 재료다. `extract_refs`는 본문 인용을 `agt:cites`와 후보 링크 개체로 방출하고, 확정은 frontmatter 링크 키에 적는 행위다(`tools/extract_refs.py` docstring).

미확정: 본문 마크다운 링크의 대상이 head 또는 `-space`에 있는지 대조하는 lint를 도구 docstring에서 확인하지 못했다.
