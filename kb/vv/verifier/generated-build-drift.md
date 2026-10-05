---
id: https://agentic-knowledge-base.dev/id/chunk/c05e9a61-1f71-4db2-bf13-ef86e3ac0e61
type: artifact
level: executable
title_ko: 요구 하나의 status를 바꾸고 BUILD를 재생성하지 않으면 FAIL [build-drift]로 거부되고 커밋본은 build_drift_test를 통과한다
title: Changing one requirement status without regenerating BUILD is rejected as FAIL [build-drift] and the committed tree passes build_drift_test
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/fdd0b6c0-473b-47d1-b23e-b1e862416964]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T20:18:09+09:00}
layer: process
---
**검증기** — 원본(frontmatter) 쪽 변경 하나와 커밋된 트리 전체를 자극으로 쓴다.

**자극** — 작업 트리에서 `kb/dev/requirement/r-014-42-line-chunk.md`의 `status: stable`을 `status: draft`로 바꾸고 BUILD를 재생성하지 않은 채 검사 모드를 돌린다. 실행 뒤 `git checkout -- kb/dev/requirement/r-014-42-line-chunk.md`로 되돌린다.

```yaml
edit:   {file: kb/dev/requirement/r-014-42-line-chunk.md, key: status, from: stable, to: draft}
build:  kb/dev/requirement/BUILD.bazel   # 손대지 않는다 — 커밋본 그대로
```

**기대** — 출력에 unified diff(`status = "stable"` → `status = "draft"`)와 `FAIL [build-drift] kb/dev/requirement/BUILD.bazel: frontmatter 와 어긋난다 — tools/gen_build.py 를 돌려 커밋하라 (BUILD 는 뷰, frontmatter 가 원본)`가 있고 종료 코드가 1이다. 되돌린 뒤 같은 명령은 `PASS [build-drift]`다. 양성 실행 `//:build_drift_test`는 PASS다.

**실행 명령** — `python3 tools/gen_build.py --check --root .; bazel test //:build_drift_test`

**판정 범위** — `status`는 청크 규칙의 속성으로 그대로 옮겨지는 값이라 변경 한 곳이 BUILD 한 줄에 대응한다. 라벨·IRI를 바꾸면 링크 해석까지 바뀌어 원인이 둘이 되므로 표본으로 쓰지 않는다. 뷰 쪽 변경(BUILD 직접 편집)은 같은 비교의 반대 방향이라 표본을 늘리지 않는다.

**검증 대응물** — 없음. 옮기기 전 케이스가 `verifies` 하던 결정 `pe-anchor-is-bazel-label` 의 결론은 `concrete` 수준이라 `executable` 검증기가 `verifies` 할 수 없다.
