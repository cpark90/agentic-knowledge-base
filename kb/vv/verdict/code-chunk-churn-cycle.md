---
id: https://agentic-knowledge-base.dev/id/chunk/d29c0250-4327-4f3a-a337-d80979e3fc9a
type: annotation
level: concrete
title_ko: 표본 tools/kb_lib.py 자극 다섯의 churn 한 주기 — 정체성은 보존되나 revalidate·심볼 참조 두 사각지대가 드러난다
title: One churn cycle over five stimuli on the sample tools/kb_lib.py — identity holds, but revalidate and symbol-reference blind spots surface
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
targets: [https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd]
generated: {by: vnv/claude-sonnet-5, at: 2026-09-30T12:40:00+09:00}
---
thought (non-blocking): 다섯 자극 모두 uuid 정체성은 보존되나 revalidate 보고·파이썬 심볼 참조 두 사각지대가 34 파일 확장 전에 남는다.

대상: https://agentic-knowledge-base.dev/id/chunk/a53c0f16-b020-471b-8106-6ec0043ac0dd

본문: 다섯 자극 모두에서 등록부 uuid 정체성은 보존된다 — 개명·순서교환은 신설·소멸 uuid 0건이고 신설·삭제는 정확히 1건씩이다. 그러나 `revalidate.py`는 개명을 파일 경로 기준으로 비교해 삭제+신규 쌍으로 오판하고, `bazel query` 하류 조회는 복합체 묶음 이후의 라벨 구성·kind 필터(`kb_chunk|kb_decision`가 `kb_composite`를 놓친다)가 깨져 다섯 자극 전부에서 하류 0/0으로 보고된다. 개명·삭제 두 자극에서는 등록부 밖의 파이썬 심볼 참조(외부 도구 36곳·같은 파일 내부 호출 1건)가 함께 깨져 `bazel build //kb:consistency`가 즉시 실패했다. 게이트 실행 시간(`extract_drift_test` 1초 내외·`gate_test` 32초 내외)은 다섯 자극 사이에서 사실상 불변이다.

제안: 34 파일로 넓히기 전에 developer가 `revalidate.py`의 라벨 구성을 `gen_build.iri_to_label`과 맞추고 `ITEM_KINDS`에 `kb_composite`를 더하며, 개명 판정을 파일 경로가 아니라 `id:`(uuid) 대조로 바꾼다. 아래는 자극별 실측(스크래치 사본, base 08376515).

| 자극 | 재판정 대상 | 링크 개체 | 등록부 refines diff | uuid 신설/소멸 | extract_drift/gate_test | 근사 중복 후보 |
|---|---|---|---|---|---|---|
| (a) 본문 한 줄(`num` docstring) | 9 | 0 | 0 | 0/0 | 1.0s / 32.1s | 193(불변) |
| (b) 개명(`pct`→`pct_str`) | 30(삭제+신규 오판) | 3 | 0 | 0/0(키 이름만) | 1.9s / 32.8s | 측정 불가 — 호출부 36곳 미수정 |
| (c) 신설(`_scratch_probe_c`) | 28 | 7 | 0 | 1/0 | 0.8s / 31.8s | 193(불변) |
| (d) 삭제(`heading_anchors`) | 23 | 7 | 0 | 0/1 | 0.8s / 32.7s | 측정 불가 — `md_anchors` 내부 호출 파손 |
| (e) 순서교환(`pct`↔`num`) | 12 | 3 | 0 | 0/0 | 0.9s / 32.9s | 193(불변) |

해소: 열림 — 표의 두 사각지대(revalidate 라벨·개명 판정, 파이썬 심볼 무추적)를 developer가 반영한 뒤 34 파일 확장을 재검토한다.
