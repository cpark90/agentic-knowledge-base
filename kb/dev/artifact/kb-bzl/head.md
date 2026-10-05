---
id: https://agentic-knowledge-base.dev/id/chunk/a0bfff7b-bee9-4e2a-91c8-0640117414d1
type: artifact
level: executable
title_ko: 모듈 머리 chunkinfo (defs/kb.bzl)
title: module head chunkinfo in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/9a583117-c61c-48f7-b30a-f60bddda9bfe
---
**모듈 머리** — `defs/kb.bzl` 의 모듈 머리 `chunkinfo` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
ChunkInfo = provider(
    doc = "지식 항목(청크 또는 복합체)이 의존자에게 내보내는 것 — 링크의 끝점은 파일이 아니라 plane·level을 아는 타깃이다.",
    fields = {
        "iri": "항목 IRI (복합체면 복합체 IRI)",
        "plane": "requirement | decision | contract | schema | artifact | annotation | memory | norm",
        "level": "functional | abstract | logical | concrete | executable (결정 복합체면 결론의 수준, 그 밖의 복합체면 부분 전부의 수준)",
        "status": "draft | stable | suspect | invalidated | deprecated",
        "srcs": "청크 파일들 (depset)",
        "parts": "복합체의 부분 IRI 목록 (청크면 빈 목록)",
    },
)

OntologyModuleInfo = provider(
    doc = "온톨로지 모듈(디렉토리)이 내보내는 것 — owl:imports 가 deps 다.",
    fields = {"iri": "모듈 IRI", "srcs": "TTL 파일들 (depset)", "imports": "가져오는 모듈의 IRI 목록"},
)

KgInfo = provider(
    doc = "타깃별 head 그래프 조각 — 청크 head·복합체 트리플의 TTL. //kg:chunks_kg 는 이 depset 의 병합이다 (바뀐 타깃만 재생성).",
    fields = {"ttl": "head TTL 조각 (depset)"},
)
```
<!-- 인용 끝 -->
