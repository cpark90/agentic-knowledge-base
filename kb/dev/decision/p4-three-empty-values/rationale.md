---
id: https://agentic-knowledge-base.dev/id/chunk/d5ab2281-0688-4762-a070-ee3f234f0fb4
type: decision
level: logical
title_ko: 하나의 빈칸은 모른다와 없다를 구분하지 못한다
title: A single blank cannot tell "unknown" from "none"
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-spec-writing-standard}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-22T19:00:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/1718358a-d741-45d7-bed6-df7818724e78
---
**근거** — 빈칸 하나는 세 사실을 같은 모양으로 만든다. 읽는 쪽은 그것이 조사 끝의 결론인지, 애초에 묻지 않은 것인지, 답을 기다리는 중인지 알 수 없다. 셋 중 `미확정`만이 행동을 요구하는데 구분이 없으면 그 요구가 사라진다.

이것은 `r-011`이 자료구조 수준에서 막으려는 것과 같다. 후보가 여럿인 상태를 정상으로 두는 구조만이 근거 없는 할당을 막는다. `미확정`은 그 상태의 문서 층 표기다.

실측이 필요를 보인다. 2026-09-22에 청크 46개가 "미확정"을 산문으로 쓰고 있었고, 그것을 세는 수단은 없었다. 미결은 `docs/open-questions/`의 11 파일에 손으로 관리됐다. 손 관리는 항목이 고쳐질 때 함께 고쳐지지 않는다 — 저장된 뷰가 원본과 어긋나는 것과 같은 문제다(`d-0075`).

세 값으로 정한 근거는 다음 행동이 갈리는 지점이 셋이라는 것이다. `없음`과 `해당 없음`은 둘 다 행동이 없지만 감사에서 다르게 읽힌다. 검토한 적 없는 자리와 검토하고 비운 자리를 구분하는 것이 `agt:excludes`의 "reviewed YYYY-MM" 서식이 하는 일과 같다.
