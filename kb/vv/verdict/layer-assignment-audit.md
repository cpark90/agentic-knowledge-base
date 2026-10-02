---
id: https://agentic-knowledge-base.dev/id/chunk/1c32f4e0-cea2-405c-b42c-3674669b6805
type: annotation
level: concrete
title_ko: 층 배정은 청크 쪽에서 끝났고 산발의 본체는 규약 161 자리 중 113이 원본 결정을 갖지 못하는 것이다
title: Layer assignment is complete on the chunk side, and the bulk of the scatter is the 113 of 161 convention slots that have no source decision
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: https://agentic-knowledge-base.dev/id/doc-structure}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/e8156600-d7a9-4e0c-b51c-8986083805c7]
generated: {by: vnv/claude-opus-5, at: 2026-10-01T10:00:00+09:00}
---
thought (non-blocking): 1-① 전수 배정의 결과는 청크 전수가 층을 받는 반면 청크가 아닌 대상에서는 배정 불가 다섯과 투영 사상 불가 113이 남는다는 것이다

대상: https://agentic-knowledge-base.dev/id/chunk/e8156600-d7a9-4e0c-b51c-8986083805c7

본문: `kb/vv/verifier/` 3에 `layer: process` 를 적어 CQ-38이 프로세스 651을 내고 지식 층의 `agt:ArtifactChunk` 행이 사라졌다
(지식 층은 나머지 전수이고 방법론은 0이다). 청크가 아닌 대상 중 뷰 13과 skill 21은 전부 도구 코드 청크의 투영이고 손 문서 20 중 열다섯이 투영이며 테스트 타깃 71
중 55는 추출 드리프트 37과 음성 고정물 18로 생성물이다. 배정 불가는 다섯이다 — 게이트 id, 면제 선언 문서, 참조 표준 목록,
분해 감사 문서, 유저 피드백 채널이다. 규약은 배정 불가가 아니라 투영 사상 불가다 —
`STYLEGUIDE.md` 88 항목과 `docs/rules.md` 73 행을 합한 161 자리 중 48만 결정을 원본으로 가리키고 113은 원본이
없거나 유저 결정만 가리킨다.

제안: 표시 자리 판정은 developer 조사표의 (a)안에 **동의한다** — 게이트·뷰·skill은 어느 청크의 투영으로도 환원되지 않는 것이
있고(게이트 id 52 중 테스트 타깃으로 서지 않는 것이 섞인다) 투영이 아닌 것은 항목이어야 하므로 `agt:inLayer`를 받을 개체가
필요하다. 손 목록과 그래프의 동일성 검사가 공통 비용이라는 진단에도 동의하며 그 검사의 첫 대상은 게이트 id다: 같은 이름의
목록이 지금 넷으로 갈려 있다 — `kb_lib` 의 `*_GATE` 상수 25 · 도구의 `FAIL [<id>]` 태그 실측 39 · `docs/tools.md` 총람과
하네스 목록의 합 40 · 네 목록의 합집합 52. 브리핑의 "게이트 id 25"는 그중 상수 쪽 하나이고, 단일 정의처가 없다는 것이
(a)안을 요구하는 직접 근거다.

**이견 하나.** 조사표는 비용을 "손 목록과 그래프의 동일성 검사"로 잡았으나 규약 113의 투영 사상 불가는 그 검사로 잡히지
않는다. 규약은 그래프에 개체를 세울 대상이 아니라 **방법론 층 결정의 투영**이어야 하고, 투영의 원본이 없으면 세울 개체도
없다. 2단계 편입에 "규약 → 결정" 신설이 들어가지 않으면 (a)안을 다 구현해도 산발의 다수가 그대로 남는다.

**2단계 예상 청크 수**는 119다 — 절차 청크 37(도구) + 규칙 청크 52(게이트 id 합집합) + 판정 절차 16(묶이지 않는 테스트 타깃)
+ 질의 청크 13(뷰) + 매크로 하나. skill 21은 생성물이라 0이고, 방법론 전환 108(결정 디렉토리 65 + `d-NNNN` 43, 청크 238)은
키 추가라 0이다. 규약 113의 원본 결정은
이 수에 들지 않는다 — 결정 저작은 orchestrator 몫이다.

해소: 열림 — 2단계 편입과 3단계 투영의 입력이고 이 주석은 판정이 아니라 감사 결과의 요지다. 전체 표는 hand-back에 있다.
