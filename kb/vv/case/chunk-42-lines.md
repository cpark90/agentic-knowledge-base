---
id: https://agentic-knowledge-base.dev/id/chunk/a45a0511-d839-4219-9c67-b417be2d8f51
type: schema
level: concrete
title_ko: 본문 43줄인 임시 청크가 chunk_lint에서 FAIL [chunk]로 거부되고 커밋된 청크는 세 lint 게이트를 통과한다
title: A temporary chunk with a 43-line body is rejected by chunk_lint as FAIL [chunk] and committed chunks pass the three lint gates
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/07d19d32-971d-4e08-89c4-f4d985d4471b]
verifies: [https://agentic-knowledge-base.dev/id/chunk/4eef1ba8-9095-4b69-aa55-69ca65ff7a35]
---
**케이스** — 경계값 둘(42줄·43줄)과 커밋된 청크 전체를 자극으로 쓴다.

**자극** — 임시 파일 `/tmp/vv-42.md`·`/tmp/vv-43.md`다. 둘 다 같은 frontmatter를 갖고 본문 줄 수만 다르다. 본문 각 줄은 평서형 문장 `n번째 줄이다.`이다. 커밋하지 않는다.

```yaml
frontmatter: {id: urn:vv:lines, type: contract, level: logical, title_ko: 줄 수 표본, title: line-count sample, status: draft, generated: {by: vnv/claude-fable-5-1, at: 2026-09-19T14:50:00+09:00}}
body_lines: 42 | 43         # frontmatter 와 앞뒤 빈 줄은 세지 않는다
```

**기대** — 42줄 파일은 `chunk_lint`가 PASS이고 43줄 파일은 `FAIL [chunk] /tmp/vv-43.md: 본문 43줄 > 42줄 — 분할하라 (4.10절 분할 신호)`로 끝나며 종료 코드가 1이다. 같은 43줄 파일을 `chunk2kg --fragment`에 넣으면 head에 `agt:lineCount 43`이 나와 `agt:ChunkShape`에 걸린다. 양성 실행 세 타깃은 PASS다.

**실행 명령** — `python3 tools/chunk_lint.py --chunks /tmp/vv-42.md /tmp/vv-43.md; bazel test //chunks:lint_test //kb/dev:lint_test //kg:gate_test`

**표본 근거** — 임계 기준은 경계 양쪽 값으로 판정한다. 42는 통과해야 하고 43은 실패해야 하므로 두 값이 상한의 위치를 하나로 고정한다. frontmatter 길이를 같게 두어 본문만이 세어짐을 보인다.
