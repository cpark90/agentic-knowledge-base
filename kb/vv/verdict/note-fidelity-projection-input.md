---
id: https://agentic-knowledge-base.dev/id/chunk/076fb076-831c-4734-91e2-0a91fb1363a7
type: annotation
level: concrete
title_ko: 3단계 투영의 입력은 노트가 앞선 확정 문장 9와 KB가 앞선 확정 문장 8이다
title: The input to the stage-3 projection is 9 confirmed sentences where the note leads and 8 where the KB leads
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/e8156600-d7a9-4e0c-b51c-8986083805c7]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-03T08:17:51Z}
---
thought (non-blocking): 3단계 투영의 입력은 노트가 앞선 것 9, KB가 앞선 것 8, 판정 불가 1이다

대상: https://agentic-knowledge-base.dev/id/chunk/e8156600-d7a9-4e0c-b51c-8986083805c7

본문: 1-② 충실도 전수(관측 `fidelity-20261003T081751Z`)는 노트의 `[확정]` 문장 392 중 374가 KB에 `일치` 로 있고 18이 어긋난다고 판정했다. 어긋남은 KB가 앞선 8, 노트가 앞선 9, 판정 불가 1이며 문장별 목록은 관측에 있다. KB가 앞선 8은 노트가 낡은 것이어서 투영이 노트를 생성물로 만들면 저절로 고쳐진다. 노트가 앞선 9는 KB에 결정이 없는 것이고 #226 과 #389 는 대체·폐기 때 유실됐다.

제안: 투영이 노트를 KB의 생성물로 만들기 전에 노트가 앞선 9를 먼저 결정으로 세운다. 그러지 않으면 투영이 그 아홉을 노트에서 지운다. #64 · #66 은 문헌 서술이므로 결정이 아니라 근거 청크의 자리다. 판정 불가 1(#11 0.4절, 둘째 수준 목록의 확장 가능 대 고정)은 유저 질문지 한 문항이다. 투영 전에 노트를 손으로 고친다면 KB가 앞선 8이 범위다. 함께 고칠 KB 내부 잔존은 "42줄"을 유지하는 결정 넷(`p4-chunk-as-ontology-class` 본문 · `p4-chunk-split-and-merge` · `p12-artifact-review-support` · `p2-skeleton-and-domain-profile`)이다.

해소: 열림 — 3단계 투영의 입력이고 이 주석은 판정이 아니라 감사 결과의 요지다. 전체 표는 scratchpad `fidelity/final.tsv` 에 있다.
