---
id: https://agentic-knowledge-base.dev/id/chunk/0b8bc291-b49e-4904-a9c1-ee4d563ca25e
type: decision
level: logical
title_ko: 상한 없는 추출과 밀폐 빌드 안의 git 읽기와 동시 편집의 미사용은 택하지 않는다
title: Unbounded extraction, reading git inside the hermetic build, and not using co-edit are not taken
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-24T03:40:23+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T03:40:23+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/59017e3e-2652-43b4-9918-0b6b91e8dce3
---
**대안** — 셋을 택하지 않는다.

| 대안 | 택하지 않는 이유 |
|---|---|
| 커밋 크기에 상한을 두지 않는다 | 쌍이 241만 건이 되고 대부분이 일괄 변경의 부산물이다 |
| 링크 후보 뷰가 빌드 안에서 git을 직접 읽는다 | 밀폐 빌드의 입력이 아니어서 같은 리비전의 결과가 달라질 수 있다 |
| 동시 편집을 증거로 쓰지 않는다(Q96의 선택지 b) | 유저가 택하지 않았다. 동시 편집은 서열이 높은 증거여서 버리면 믿음 정도의 재료가 줄어든다 |
