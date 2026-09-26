---
id: https://agentic-knowledge-base.dev/id/chunk/a45a0511-d839-4219-9c67-b417be2d8f51
type: schema
level: concrete
title_ko: 본문 43줄인 임시 청크가 chunk_lint에서 FAIL [chunk]로 거부되고 커밋된 청크는 세 lint 게이트를 통과한다
title: A temporary chunk with a 43-line body is rejected by chunk_lint as FAIL [chunk] and committed chunks pass the three lint gates
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: vnv/claude-opus-5, at: 2026-09-23T02:50:00+09:00}
refines: [https://agentic-knowledge-base.dev/id/chunk/07d19d32-971d-4e08-89c4-f4d985d4471b]
verifies: [https://agentic-knowledge-base.dev/id/chunk/4eef1ba8-9095-4b69-aa55-69ca65ff7a35]
---
**케이스** — 경계값 둘(42줄·43줄)과 커밋된 청크 전체를 자극으로 쓴다.

**자극** — 임시 파일 둘이다. 이름은 `vv-42.md`·`vv-43.md`이고 경로는 검증기가 정한다. 둘 다 같은 frontmatter를 갖고 본문 줄 수만 다르다. 본문 각 줄은 평서형 문장 `n번째 줄이다.`이다. 커밋하지 않는다. 자극이 42줄을 넘으므로 큰따옴표 한 줄 스칼라에 `\n`으로 적는다.

```yaml
files:
  vv-42.md: "---\n{id: urn:vv:lines, type: contract, level: logical, title_ko: 줄 수 표본, title: line-count sample, status: draft, generated: {by: vnv/claude-opus-5, at: 2026-09-23T02:50:00+09:00}}\n---\n1번째 줄이다.\n2번째 줄이다.\n3번째 줄이다.\n4번째 줄이다.\n5번째 줄이다.\n6번째 줄이다.\n7번째 줄이다.\n8번째 줄이다.\n9번째 줄이다.\n10번째 줄이다.\n11번째 줄이다.\n12번째 줄이다.\n13번째 줄이다.\n14번째 줄이다.\n15번째 줄이다.\n16번째 줄이다.\n17번째 줄이다.\n18번째 줄이다.\n19번째 줄이다.\n20번째 줄이다.\n21번째 줄이다.\n22번째 줄이다.\n23번째 줄이다.\n24번째 줄이다.\n25번째 줄이다.\n26번째 줄이다.\n27번째 줄이다.\n28번째 줄이다.\n29번째 줄이다.\n30번째 줄이다.\n31번째 줄이다.\n32번째 줄이다.\n33번째 줄이다.\n34번째 줄이다.\n35번째 줄이다.\n36번째 줄이다.\n37번째 줄이다.\n38번째 줄이다.\n39번째 줄이다.\n40번째 줄이다.\n41번째 줄이다.\n42번째 줄이다.\n"
  vv-43.md: "---\n{id: urn:vv:lines, type: contract, level: logical, title_ko: 줄 수 표본, title: line-count sample, status: draft, generated: {by: vnv/claude-opus-5, at: 2026-09-23T02:50:00+09:00}}\n---\n1번째 줄이다.\n2번째 줄이다.\n3번째 줄이다.\n4번째 줄이다.\n5번째 줄이다.\n6번째 줄이다.\n7번째 줄이다.\n8번째 줄이다.\n9번째 줄이다.\n10번째 줄이다.\n11번째 줄이다.\n12번째 줄이다.\n13번째 줄이다.\n14번째 줄이다.\n15번째 줄이다.\n16번째 줄이다.\n17번째 줄이다.\n18번째 줄이다.\n19번째 줄이다.\n20번째 줄이다.\n21번째 줄이다.\n22번째 줄이다.\n23번째 줄이다.\n24번째 줄이다.\n25번째 줄이다.\n26번째 줄이다.\n27번째 줄이다.\n28번째 줄이다.\n29번째 줄이다.\n30번째 줄이다.\n31번째 줄이다.\n32번째 줄이다.\n33번째 줄이다.\n34번째 줄이다.\n35번째 줄이다.\n36번째 줄이다.\n37번째 줄이다.\n38번째 줄이다.\n39번째 줄이다.\n40번째 줄이다.\n41번째 줄이다.\n42번째 줄이다.\n43번째 줄이다.\n"
```

**기대** — 42줄 파일은 `chunk_lint`가 PASS이고 43줄 파일은 `FAIL [chunk]`와 본문 줄 수 사유로 거부되며 종료 코드가 1이다. 같은 43줄 파일을 `chunk2kg --fragment`에 넣으면 head에 `agt:lineCount 43`이 나와 `agt:ChunkShape`에 걸린다. 양성 실행 세 타깃은 PASS다.

```yaml
expect:
  - exit: 1
    contains:
      - "FAIL [chunk]"
      - "본문 43줄 > 42줄 — 분할하라 (4.10절 분할 신호)"
  - exit: 0
```

**실행 명령** — `python3 tools/chunk_lint.py --chunks {{vv-42.md}} {{vv-43.md}}; bazel test //chunks:lint_test //kb/dev:lint_test //kg:gate_test`

**표본 근거** — 이 자극이 어기는 규칙은 본문 42줄 상한 하나다. 임계 기준은 경계 양쪽 값으로 판정하고, 42는 통과해야 하고 43은 실패해야 하므로 두 값이 상한의 위치를 하나로 고정한다. 최소성은 실험으로 확인했다 — 줄 수만 42로 줄인 같은 파일이 같은 명령에서 종료 0 이고 43줄 파일의 거부도 `FAIL [chunk]` 하나뿐이다(2026-09-23, `p8-minimal-negative-stimulus`). 통제인 42줄 파일이 같은 명령 안에 있고 frontmatter 길이를 같게 두어 본문만이 세어짐을 보인다.
