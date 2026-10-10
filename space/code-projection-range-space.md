---
id: https://agentic-knowledge-base.dev/id/chunk/10c290e0-79d7-45fe-9105-252f4e5306ec
type: agt:Space
level: logical
title_ko: 코드를 청크로 투영하는 범위를 무엇이 정하는가
title: What sets the range of code projected into chunks
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: orchestrator/claude-opus-5-5, at: 2026-10-09T18:04:39+09:00}
---
유저는 미결을 "개선 및 확장이 이루어지는 frontier 포인트"로 보았다(Q54-a).

질문 — 코드 → 청크 투영의 범위가 원리가 아니라 목록(`EXTRACTED_SOURCES`·`EXTRACTED_QUERY_DIRS`·`EXTRACTED_STARLARK`, `defs/kb.bzl`)이다. `defs/kb.bzl`은 추출되고 `defs/knowledge.bzl`·`harness/scripts/*`·`tools/relock.sh`는 추출되지 않는다. `p0-service-is-a-three-layer-wiki`의 대안은 "빌드 배선을 청크로 추출하는 안"을 기각했는데 `defs/kb.bzl`은 추출된다. 하네스 코드는 층도 지위도 없다. 같은 원인의 사례로 새 `.bzl` 파일이 빌드 배선인지 추출 대상인지 정해지지 않았다. 구조 검수(2026-10-06)가 이 자리를 지적했고 유저가 설계 공간으로 세웠다(Q75-a). 요구 `r-029`(하네스 자기 개선)에서 투영 범위를 정하는 결정으로 가는 `refines`가 변수다. `r-029`의 미확정(하네스의 어느 부분이 지식에서 생성되는가의 경계)은 2단계 편입(도구 → 절차 청크)을 그 답의 첫 형태로 든다.

이미 정해진 것 — 소스가 원본이고 청크는 추출의 생성물이다(`p7-code-extraction-direction`). 빌드 배선(손 BUILD·Starlark)은 항목이 아니다(Q10-a). `EXTRACTED_STARLARK`의 주석은 규칙을 강제하는 코드가 든 `.bzl` 파일만 넣고 배선만 하는 `defs/knowledge.bzl`은 항목이 아니라고 적는다(Q32-a).

현재 상태(2026-10-09 실측) — `defs/kb.bzl`의 목록은 `EXTRACTED_SOURCES` 42개 · `EXTRACTED_QUERY_DIRS` 2개 · `EXTRACTED_STARLARK` 1개(`kb`)다. 목록 밖의 코드는 `defs/knowledge.bzl`, `harness/scripts/`의 셸 스크립트 9개, `harness/scripts_test.py`, `tools/relock.sh`다. 측정은 세 리터럴의 항목과 `ls defs/ harness/scripts/ tools/*.sh`의 대조다.

답이 가르는 것 — 새 코드 파일이 추출 대상인지를 목록을 고치기 전에 판단할 수 있는지가 갈린다.

선택지 — A는 범위를 등록 목록 셋이 정하는 현행 유지안이다(`p7-extraction-range-by-list`). B는 범위를 원리로 정하고 목록을 그 실현으로 두는 안이다(`p7-extraction-range-by-principle`). 구조 검수는 이 자리에 선택지를 들지 않았다. 그래서 현행 유지와 질문이 가르는 반대쪽 둘만 세운다. 관련 결정 `p0-service-is-a-three-layer-wiki`의 대안은 기각한 안 여섯의 표라 한 후보로 들지 않는다. 두 후보 모두 열려 있다.

```yaml
variable:
  from: https://agentic-knowledge-base.dev/id/chunk/cb7ac129-5b94-47cd-84a8-b87e7e238efe
  kind: refines
status: open
candidates:
  - to: https://agentic-knowledge-base.dev/id/chunk/70d56a11-ab22-475f-8ca6-7af9c727eb1d
    state: open
  - to: https://agentic-knowledge-base.dev/id/chunk/108a10f4-abcb-4cea-8d00-e71d462969a1
    state: open
```
