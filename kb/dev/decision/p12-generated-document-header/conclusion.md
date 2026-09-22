---
id: https://agentic-knowledge-base.dev/id/chunk/61906023-e4bb-46b1-a6db-4bf4635b631b
type: decision
level: concrete
title_ko: 생성 문서의 머리는 제목 한 줄과 여섯 줄의 고정 순서다
title: The head of a generated document is one title line and six lines in fixed order
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-generated-document-standards}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/4ae7ad6d-fabc-4925-bc6a-4aa518eeab55]
serves: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
restored: [https://agentic-knowledge-base.dev/id/chunk/973f5595-b22c-48d1-ad19-976a0408497b]
generated: {by: orchestrator/claude-opus-5, at: 2026-09-21T21:10:00+09:00}
part_of: https://agentic-knowledge-base.dev/id/composite/094466b2-eced-45bf-991f-85eead474058
composite: {id: https://agentic-knowledge-base.dev/id/composite/094466b2-eced-45bf-991f-85eead474058, title_ko: 생성 문서의 머리 블록, title: The head block of a generated document}
---
**결론** — 모든 생성 마크다운은 h1 한 줄과 그 아래 여섯 줄의 머리 블록으로 시작한다. 순서는 고정이다.

| 줄 | 내용 | 무엇을 막는가 |
|---|---|---|
| h1 | `# <이름> — <목적> (생성 파일)` | 사본을 원본으로 오인하는 것 |
| `- 생성기:` | `tools/<도구>.py` · `<생성자>/<버전>` | 어느 도구의 어느 판이 냈는지 모르는 것 |
| `- 생성 시각:` | ISO 8601 UTC 초 해상도 (`%Y-%m-%dT%H:%M:%SZ`) | 낡은 사본을 최신으로 읽는 것 |
| `- 입력:` | 파일 목록 · 지문 `sha256:<앞 12자>` · 규모 수치 | 같은 이름의 수치가 왜 다른지 모르는 것 |
| `- 질의:` | 무엇을 물어 만들었는가 | 수치의 정의가 문서 밖에 있는 것 |
| `- 재현:` | 자기를 다시 만드는 명령 | 사본만 손에 든 사람이 갱신하지 못하는 것 |
| 성격 경고 | 뷰인가 생성 트리 파일인가, 고칠 곳은 어디인가 | 생성물을 손으로 고치는 것 |

리비전이 아니라 **지문**을 쓴다. Bazel 샌드박스에 git이 없고, 지문은 입력 내용에서 직접 오므로 리비전보다 정확하다.

드리프트 검사가 바이트 비교를 하는 생성 트리 파일(`.claude/skills/*/SKILL.md`·생성 BUILD)에는 생성 시각과 지문을 넣지 않는다. 그 자리의 건전성 장치는 결정론이며 `//:skills_drift_test`·`//:build_drift_test`가 그것을 검사한다.

규약의 단일 정의처는 `tools/kb_lib.py`다. 생성기와 게이트가 같은 함수를 쓴다.
