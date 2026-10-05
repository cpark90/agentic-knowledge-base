---
id: https://agentic-knowledge-base.dev/id/chunk/a3798247-024d-49f1-996e-159100ae3f9e
type: contract
level: logical
title_ko: 감사 보고서는 srcs에 선언된 그래프·본문만 읽는 샌드박스 액션으로 생성되고 체계 밖 정보 0을 선언한다
title: The audit report is produced by a sandboxed action reading only the graphs and bodies declared in srcs and declares zero out-of-system information
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-fable-5-1, at: 2026-10-03T18:27:49+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/db7470cb-ff9c-45b3-8817-27bf77a30aaf]
---
**합격 기준** — 기준 종류는 **불변식**이다. `srcs(//kg:audit) = 그래프 union ∪ 관측 본문`이고 생성기의 읽기 집합은 `srcs`에 포함된다. 보고서의 모든 수치는 그 입력에서만 나온다.

**판정식**

- 양성(생성): `bazel build //kg:audit`이 성공하고 `bazel-bin/kg/audit.md`의 머리 절에 `입력: 그래프 파일 N개 · 트리플 M`과 `체계 밖 정보 0`이, 끝에 `## 자족성 선언`이 있다.
- 양성(입력): `bazel query 'labels(srcs, //kg:audit)'`의 출력이 그래프 라벨 다섯(`//kg:chunks_kg`·`//kg:kg`·`//kg:references_kg`·`//kb/odd:odd`·`//kb/ontology:modules`)과 본문 라벨 둘(`//kb/vv:vv`·`//kb/dev:dev`)이고 그 밖의 라벨이 없다.
- 음성: 생성기가 `srcs` 밖의 파일(`docs/*.md` 등)을 열면 샌드박스에 그 파일이 없어 액션이 실패한다. 서술 표본이다.
- 재현: 입력이 같은 두 번의 생성이 생성 시각 줄을 제외하고 같다.

**등급** — B다. 판정은 기계가 하되 그래프 적재와 생성의 실행 비용이 있다.

기준의 대상은 `//kg:audit`과 그 생성기이고 판정의 원본은 `defs/knowledge.bzl`의 `kb_weave`(`srcs = data + bodies`)와 Bazel 샌드박스다. 온보딩 네 단계의 자족성은 라벨 목록 뷰(`//kg:workset`)의 몫이고 이 기준 밖이다.
