---
id: https://agentic-knowledge-base.dev/id/chunk/b56b2584-a192-489e-bfed-2b18ca3e03d8
type: decision
level: logical
title_ko: 링크 값을 객체로 바꾸거나 증거를 별도 파일에 두는 안은 기각된다
title: Object-valued link entries and a separate evidence file are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-fable-5-1, at: 2026-09-19T16:10:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/66d847e5-4837-43ea-8498-da00a8fb92f3
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 링크 값을 객체로(`refines: [{target, evidence}]`) | 링크 키 아홉의 파서·`gen_build` deps·shape가 전부 바뀐다. 표현력은 크나 첫 형태의 비용이 크다 |
| 증거를 별도 파일(`kg/evidence-kg.ttl`)에 손으로 | 청크와 증거가 분리돼 청크를 옮기면 어긋난다. `kg/`는 생성물이다 |
| 새 증거 종류 `restoration` 신설 | 어휘 밖 술어 금지. `proposal`이 뜻을 이미 담는다 |
| 표시 없이 도구가 `git log`로 사후 여부 판정 | 샌드박스에 git이 없고, 커밋 시점과 링크 시점이 다르다(구축 링크도 나중에 커밋된다) |
