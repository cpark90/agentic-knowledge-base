---
id: https://agentic-knowledge-base.dev/id/chunk/14782c7c-bf50-47a8-ab11-62715aeeb63e
type: decision
level: concrete
title_ko: 프로젝트를 넘는 것은 어휘·제약·ODD 코어와 도구이고 지식은 넘지 않는다
former_title_ko: ["프로젝트를 넘는 것은 어휘·제약·ODD 코어이고 청크는 넘지 않는다", "프로젝트를 넘는 것은 어휘·제약·ODD 코어이고 지식 항목은 넘지 않는다", "프로젝트를 넘는 것은 어휘·제약·ODD 코어이고 지식은 넘지 않는다"]
title: Vocabulary, constraints, the ODD skeleton, and the tools cross projects; chunks do not
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}, {resource: git:aeb0a58:chunks/decision/d-0149-cross-project-reuse.md, id: https://agentic-knowledge-base.dev/id/chunk-d0149, title_ko: "청크는 프로젝트를 넘지 않는다", title: "Chunks do not cross projects"}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-11-01T05:42:48+09:00}
verified: [{by: orchestrator/claude-opus-5-5, at: 2026-10-24T18:07:48+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-24T22:57:27+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-10-25T13:48:52+09:00}, {by: orchestrator/claude-opus-5-5, at: 2026-11-01T05:42:48+09:00}]
refines: [https://agentic-knowledge-base.dev/id/chunk/d8e8aa97-d95c-4962-a88a-94e047702e4d, https://agentic-knowledge-base.dev/id/chunk/20148952-30c4-4f76-8cbf-4d9b32c68b25]
supersedes: [https://agentic-knowledge-base.dev/id/chunk-d0149]
part_of: https://agentic-knowledge-base.dev/id/composite/8dbf8cd0-81dd-478f-b73e-3aeea905768f
composite: {id: https://agentic-knowledge-base.dev/id/composite/8dbf8cd0-81dd-478f-b73e-3aeea905768f, title_ko: 프로젝트 간 재사용의 단위, title: The unit of cross-project reuse}
---
**결론** — 3.7절 "이전 ODD 복사"의 확장. 프로젝트를 넘는 것은 **어휘·제약·
ODD 코어와 도구**이고, **지식은 재사용하지 않는다.**

| 재사용 대상 | 방식 | 조건 |
|---|---|---|
| 온톨로지 | 공유. 프로젝트별 확장 모듈만 추가 | 코어 수정 금지 |
| ODD | 복사 후 축소·확장 | 3.6절 변경 유형 |
| 일반화로 올라간 제약 | 온톨로지 공리로 자동 상속 | 없음 |
| `defect` 어휘 | 공유 | 없음 |
| 도구와 게이트(`defs/`·`tools/`) | Bazel 모듈 의존(`git_override`로 커밋 고정) | 코어 수정 금지, 이름공간은 빌드 설정 |
| 지식 | 재사용하지 않음 | 프로젝트 ODD 안에서만 유효 |

**모듈 의존의 규약** (Q-0075#Q172-a, 2026-11-01) — 다른 프로젝트는 이 저장소를 `MODULE.bazel`의 의존으로 쓰고 도구와 게이트를 복사하지 않는다. 그래서 도구는 두 뿌리를 가른다. 온톨로지 코어, 판정 프로파일과 shape, CQ 질의, `defs/kb.bzl`은 이 모듈의 뿌리(runfiles, 함수 `core_root`)에서 읽는다. 호출 저장소의 지식과 생성 그래프, 온톨로지 확장은 작업 트리에서 읽는다. 온톨로지는 두 뿌리의 합이다. 매크로가 명령에 넣는 도구 라벨은 이 모듈 기준으로 푼다. 단위 지식 IRI 이름공간은 빌드 설정 `//defs:id_base`가 정하고, 비면 기본값 `https://agentic-knowledge-base.dev/id/`이다. 기본값 리터럴은 `tools/chunk2kg.py`의 `ID_BASE_DEFAULT` 한 곳에 있고, 값은 환경 변수 `KB_ID_BASE`로 도구에 간다. 설정은 루트 모듈의 지식 타깃과 도구 실행에만 닿으므로, 의존 저장소에서 빌드한 이 저장소의 지식은 원래 이름공간을 지킨다. `agt:` 어휘 이름공간은 매개화하지 않는다. 코어 어휘는 공유하기 때문이다. verify 질의 게이트는 질의 파일을 라벨로 받고, 질의가 0개로 풀리면 설정 오류(종료 코드 2)로 끝난다. 질의 없는 통과는 판정이 아니기 때문이다.
