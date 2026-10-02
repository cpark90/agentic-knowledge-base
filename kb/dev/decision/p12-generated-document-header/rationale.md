---
id: https://agentic-knowledge-base.dev/id/chunk/6a85d937-acfb-44c8-b64b-47927928a7f9
type: decision
level: logical
title_ko: 시각만으로는 같은 이름의 수치가 왜 다른지 판별되지 않는다
title: A timestamp alone does not tell why two figures of the same name differ
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-21T21:10:00+09:00}
layer: methodology
part_of: https://agentic-knowledge-base.dev/id/composite/094466b2-eced-45bf-991f-85eead474058
---
**근거** — `p12-documents-are-generated`는 생성 시각과 질의를 요구했다. 2026-09-19 실측은 그것으로 부족함을 보인다.

- 같은 커밋에서 트리플 수가 세 값이었다. `metrics` 20418 · `link-candidates` 20361 · `cq`와 weave 넷 21223이다. 셋 다 "그래프"라 부르지만 union 구성이 다르고, 입력 목록을 적은 문서가 없어 독자가 그 차이를 판별할 수 없었다.
- `metrics`의 developer 예산 준수율 `632/632`와 `workset-developer`의 "예산 초과"가 같은 이름으로 다른 정의를 썼다. 질의를 적으면 그 차이가 문서 안에서 드러난다.
- 재현 명령을 자기 안에 적은 것은 `audit` 하나였다. `p12-audit-and-onboarding-self-sufficiency`는 새로 들어오는 에이전트가 체계의 출력만으로 동작할 것을 요구한다. 사본만 손에 든 사람이 갱신 방법을 모르면 그 요구가 깨진다.
- 생성기 버전을 적은 것은 0종이었다. `docs/rules.md`의 OKF 행위자 표기 `<생성기>/<버전>`이 청크에는 내려왔고 문서에는 내려오지 않았다.

지문을 쓰는 이유는 둘이다. 샌드박스에 git이 없어 리비전을 얻을 수 없고, 워킹트리에 추적되지 않은 변경이 있으면 리비전은 입력을 대표하지 못한다. 지문은 입력 내용에서 직접 온다.
