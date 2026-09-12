---
id: https://agentic-knowledge-base.dev/id/chunk/0ffbaaaf-9bd5-405c-90f7-ed40b0addcd5
type: decision
level: logical
title_ko: 입력은 ODD와 다른 축이고 파급 기록이 재검토 범위를 만든다
title: Inputs form an axis distinct from the ODD; the impact column defines the review scope
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: claude/fable-5, at: 2026-09-10T18:00:00+09:00}
verified: [{by: process:label-judge-20260911, at: 2026-09-11T18:50:00+09:00}, {by: human:cpark, at: 2026-09-11T18:50:00+09:00}]
part_of: https://agentic-knowledge-base.dev/id/composite/c0707632-682f-4f16-bae0-d5b47f69d096
---
**근거** (노트 11.1절, Part XI 도입)

- ODD가 프로젝트의 **운영 조건**을 적는 문서라면, 입력은 **체계 자체를 이
  프로젝트에 맞게 구성하는 값**이다. 두 축을 한 곳에 두면 변경 파급 계산이
  뒤섞인다.
- 기록 형식은 3.6절 ODD 유지 관리 표와 같다. 세 칸이 다 있어야 입력이
  바뀌었을 때 무엇을 재검토할지가 표에서 바로 읽힌다.
- 제공 주체는 태그 어휘(설계 에이전트 + 유저)를 빼면 전부 유저다. 체계가
  스스로 정하는 입력은 없다 — 그래서 전부 밖이다.
- 파급의 크기가 입력마다 다르다. 상위 온톨로지 선택은 온톨로지 전체
  재정렬로 사실상 불가역이고, 에이전트 카탈로그는 스코프 전부 재파생(3.4절),
  도메인 프로파일·판정 도구 바인딩은 해당 plane 청크 전부 재검사,
  앵커 해석기 구성은 링크 양 끝 재해석이다.
- 언어 정책은 **한글 및 영어 강제**로 이미 확정되어 있고(12.3절) 파급은
  0.6절 표기 형식뿐이다 — 다른 입력 사슬과 만나지 않는다.
- 청크 상한(42줄 기본, plane별 오버라이드) · 일반화 임계값 N·M·K ·
  커버리지 임계 · 후보 상한 k는 수치 파라미터다. 규칙은 그대로 두고 값만
  바뀌므로 파급이 재검사·재계산으로 끝난다.
