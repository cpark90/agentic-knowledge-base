---
id: https://agentic-knowledge-base.dev/id/chunk/fb258975-cc11-4bbc-bfd3-0f37cd32887e
type: decision
level: concrete
title_ko: 규범 문서 규약 — 단위 지식은 온톨로지 클래스이자 토큰 상한의 최소 단위다
title: Normative-document conventions — A chunk is an ontology class and the token-bounded minimal unit
former_title_ko: ["규범 문서 규약 — 지식 항목은 온톨로지 클래스이자 토큰 상한의 최소 단위다"]
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:47:12+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/dd76498b-2cca-4b79-a1fe-ce5a4d33c0ca
---
**규약** — `p4-chunk-as-ontology-class`의 결론을 규범 문서에 싣는 문장이다.

규약: 크기 | 본문은 **토큰 상한** 이하다. 저작 산문은 42의 26배인 **1,092**이고, 이 값은 예산 5,418의 1/5이라 한 번에 4~5개를 조망한다. `artifact`와 `memory`의 인용은 42의 68배로 한 창인 **2,856**이다. 계수기는 ODD `cond-tokenizer-lock`으로 고정된 `o200k_base`이고, 단일 정의 위치는 `tools/kb_lib.py`의 `BODY_TOKEN_LIMITS`, 그래프 쪽은 `token-budget-shapes.ttl`이다. 그 전에는 42줄·200줄이었고, 줄은 내용에 따라 토큰이 1.9배 갈린다(2026-10-01).
규약: 단위 | 단위 지식 하나는 지식 종류 하나와 정제 수준 하나, 주제 하나, **파일 하나**다
