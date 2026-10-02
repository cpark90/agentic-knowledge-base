---
id: https://agentic-knowledge-base.dev/id/chunk/792451e0-c2da-44f5-83a6-9551e94c1b05
type: decision
level: logical
title_ko: 리비전 기재·시각 생략·도구별 머리 유지 안은 기각된다
title: Recording a revision, omitting the timestamp, and per-tool heads are rejected
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-21T21:10:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/094466b2-eced-45bf-991f-85eead474058
---
**대안** — 넷을 기각한다.

| 대안 | 기각 이유 |
|---|---|
| 지문 대신 git 리비전을 적는다 (`p8-vv-reports`의 문구) | Bazel 샌드박스에 git이 없다. 워킹트리에 추적되지 않은 변경이 있으면 리비전이 입력을 대표하지 못한다 — `audit`가 "워킹트리 추적 파일 변경 있음"을 덧붙여야 했던 것이 그 증거다 |
| 생성 시각을 빼고 `SOURCE_DATE_EPOCH`로 고정해 비트 동일성을 얻는다 | 뷰의 값은 시각이 아니라 최신성이다. 낡은 사본을 최신으로 읽는 것이 여기서 막을 위험이고, `p12-documents-are-generated`의 대안 절이 이미 시각 생략을 배제했다. 재현 판정은 지문이 맡는다 |
| 머리 형식을 도구마다 자유롭게 두고 권장만 문서에 적는다 | 2026-09-19 실측에서 머리 문구 세 갈래·메타 블록 세 갈래·시각 형식 세 갈래가 공존했다. 권장은 이미 있었고 지켜지지 않았다 |
| 머리를 YAML frontmatter로 둔다 | 생성물은 청크가 아니다. frontmatter를 붙이면 `chunk2kg`의 입력으로 오인될 여지가 생기고, 사람이 첫 화면에서 읽는 것이 목적이므로 본문에 둔다 |
