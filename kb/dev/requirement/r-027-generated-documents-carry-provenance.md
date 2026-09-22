---
id: https://agentic-knowledge-base.dev/id/chunk/4ae7ad6d-fabc-4925-bc6a-4aa518eeab55
type: requirement
level: functional
pattern: ubiquitous
title_ko: 생성 문서는 자기 출처와 재현 수단을 담아야 한다
title: A generated document must carry its provenance and the command that rebuilds it
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-21T21:10:00+09:00}
---
**요구** — 체계가 생성하는 모든 문서는 생성기와 그 버전, 생성 시각, 입력 목록과 그 지문, 질의, 자기를 다시 만드는 명령을 담아야 한다.

- **이해관계자**: 감사 역할·새로 들어오는 에이전트 · **관심사**: 사본이 원본으로 오인되지 않는 것
- **출처**: 유저 지시 2026-09-21 · W3C PROV-O · Sandve et al. (2013) Rule 1·6 · IEC/IEEE 82079-1:2019 7.2

생성 시각만으로는 부족하다. 2026-09-19 실측에서 같은 커밋의 세 생성물이 트리플 수를 20418·20361·21223으로 적었고, 어느 문서도 자기 입력 목록을 적지 않아 독자가 그 차이를 판별할 수 없었다.
