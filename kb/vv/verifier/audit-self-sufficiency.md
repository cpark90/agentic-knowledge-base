---
id: https://agentic-knowledge-base.dev/id/chunk/020fd3c6-2184-4705-abea-c7df3338682c
type: artifact
level: executable
title_ko: //kg:audit이 srcs 일곱(그래프 다섯·본문 둘)만으로 bazel-bin/kg/audit.md를 만들고 머리에 체계 밖 정보 0을 적는다
title: //kg:audit produces bazel-bin/kg/audit.md from its seven srcs alone, five graphs and two body groups, and states zero out-of-system information in its head
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/a3798247-024d-49f1-996e-159100ae3f9e]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T20:18:09+09:00}
layer: process
---
**검증기** — 감사 보고서 타깃 하나와 그 선언 입력을 자극으로 쓴다.

**자극** — `//kg:audit`이다. `kb_weave(kind = "audit")`이 `genrule`로 전개되고 `srcs`는 아래 일곱 라벨이다. 실행 기록은 `kb/vv/run/`의 파일 전부, 가정 판정은 `kb/dev/memory/`의 관측이다.

```yaml
data:   [//kg:chunks_kg, //kg:kg, //kg:references_kg, //kb/odd:odd, //kb/ontology:modules]
bodies: [//kb/vv:vv, //kb/dev:dev]
tool:   //tools:weave      # git · 네트워크 호출 없음 — 리비전은 실행 기록 본문에서 읽는다
```

**기대** — 빌드가 성공하고 `bazel-bin/kg/audit.md`의 머리에 `입력의 종류: 그래프 union(…) · 관측 본문 — 실행 기록 N건 · 가정 판정 M건. 체계 밖 정보 0 (요구 audit-self-sufficiency)`이, 끝에 `## 자족성 선언`과 재생성 명령 `bazel build //kg:audit`이 있다. `bazel query 'labels(srcs, //kg:audit)'`의 출력이 위 일곱 라벨과 같다.

**실행 명령** — `bazel build //kg:audit && bazel query 'labels(srcs, //kg:audit)'`

**판정 범위** — 감사 보고서는 체계 밖 정보의 유혹이 가장 큰 뷰(리비전·환경·수치)라 자족성의 경계값이다. 입력 목록을 `bazel query`로 그대로 인용하면 선언과 실제가 한 명령으로 대조된다. 온보딩 쪽(라벨 목록)은 입력이 그래프뿐이라 같은 분기의 더 쉬운 값이고 표본을 늘리지 않는다.

**검증 대응물** — 없음. 옮기기 전 케이스가 `verifies` 하던 결정 `p12-audit-and-onboarding-self-sufficiency` 의 결론은 `concrete` 수준이라 `executable` 검증기가 `verifies` 할 수 없다.
