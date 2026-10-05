---
id: https://agentic-knowledge-base.dev/id/chunk/aa90f4e4-9bbe-4436-82f0-4a68059d129d
type: decision
level: logical
title_ko: 손 번호는 항목을 넣고 뺄 때 어긋나고 소스는 고칠 수 있으며 diff가 읽힌다
title: Hand numbers drift when items move, and a source can be edited and its diff read
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-03T15:00:00+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-04T12:19:10+09:00}]
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/97352110-2d95-4c45-ad01-1d9302b08656
---
**근거** — 셋은 명세 문서 작성 규격(유저 제안)의 그림 틀 6.8절을 옮긴 것이다. 그 틀의 슬롯은 캡션(문장 하나, 번호 없음)·그림(소스 펜스 또는 이미지 경로)·읽는 법(명사구 목록 셋 이하)이다.

캡션 번호를 금하는 근거는 규격의 원칙 "표시용 번호는 소스에 없다"다. 번호는 항목을 넣고 뺄 때 어긋난다. 목록의 손 번호를 금하는 이유와 같다(`p4-slot-answers-one-question`). 소스 펜스를 우선하는 근거는 소스는 고칠 수 있고 diff가 읽히지만 이미지는 둘 다 아니라는 것이다.

유저는 2026-09-22에 규격 반영의 즉시 묶음에 그림 틀을 넣어 승인했다. 같은 날 실측에서 그림 틀이 반영되지 않은 것이 드러났고, 유저는 반영하는 쪽을 골랐다. 그때 그림을 담은 파일은 저장소 전체에서 1개였다.

미확정: 그림 규칙을 게이트로 올릴지는 정하지 않았다. 캡션과 펜스 언어는 기계가 볼 수 있으나 2026-09-22에는 표본이 1파일이라 오탐률을 재지 못했다.
