---
id: https://agentic-knowledge-base.dev/id/chunk/9807be26-ff48-4cca-89c1-129f52e69df4
type: requirement
level: functional
pattern: ubiquitous
title_ko: 생성 문서의 서식은 하나의 규약을 따라야 한다
title: Generated documents must follow one form convention
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-21T21:10:00+09:00}
---
**요구** — 체계가 생성하는 모든 문서는 도구마다 다른 서식이 아니라 하나의 규약을 따라야 하고, 그 규약은 생성 전에 고정되어 있어야 한다.

- **이해관계자**: 문서를 읽는 사람과 에이전트 · **관심사**: 한 번 익힌 읽기 방식의 재사용
- **출처**: 유저 지시 2026-09-21 · markdownlint · ISO/IEC/IEEE 26514:2022 · Microsoft Writing Style Guide

서식이 생성기마다 독립으로 내려지면 문서마다 읽는 법을 다시 익혀야 한다. 2026-09-19 실측에서 빈 값의 표기가 네 갈래, 시각 형식이 세 갈래, 머리 문구가 세 갈래였다.
