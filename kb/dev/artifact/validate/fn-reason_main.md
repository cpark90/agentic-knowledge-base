---
id: https://agentic-knowledge-base.dev/id/chunk/20010c39-d032-41e2-8566-e7d12dc09fd6
type: artifact
level: executable
title_ko: 함수 reason_main (tools/validate.py)
title: function reason_main in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/07104b21-b283-4e54-a921-6b9a61fb6e45, https://agentic-knowledge-base.dev/id/chunk/264d9fd1-b338-48ec-9eb9-9ca20577aecc, https://agentic-knowledge-base.dev/id/chunk/36ed7d92-b42b-43c6-9325-c9846e77d4fb]
part_of: https://agentic-knowledge-base.dev/id/composite/d0b4b228-df49-490d-b346-c659c4c6e8da
---
**함수** — `reason_main(asserted, files, shapes, shape_paths, waivers, n_files)` 다. 추론 모드(`--reason`)의 판정 — OWL 2 RL 폐포를 한 번 만들고 모순과 폐포 위 shape 적합성을 본다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def reason_main(asserted: Graph, files: dict[str, Graph], shapes: Graph, shape_paths: list[str],
                waivers: list[dict], n_files: int) -> int:
    """추론 모드(`--reason`)의 판정 — OWL 2 RL 폐포를 한 번 만들고 모순과 폐포 위 shape 적합성을 본다.

    게이트마다 `PASS [<id>]` 또는 `FAIL [<id>]` 줄을 내고 끝에 도구 태그의 집계 줄을 낸다. 모순이 있어도 shape 적합성을
    돌린다 — 한 번의 실행이 고칠 것을 전부 보인다.
    """
    closed, messages = owl_rl_closure(asserted)
    errors = check_logical_consistency(asserted, closed, messages, files)
    if not errors:
        print(f"PASS [{LOGICAL_CONSISTENCY}] — OWL 2 RL 폐포 트리플 {len(closed)}개(단언 {len(asserted)}개), "
              f"추론기 오류 노드 0건, owl:Nothing 소속 0건")
    if shape_paths:
        shacl_errors = check_shacl(closed, shapes, True, shape_paths, waivers)
        if not shacl_errors:
            print(f"PASS [{SHACL}] — OWL 2 RL 폐포 위 shape 적합 (shape 파일 {len(shape_paths)}개)")
        errors += shacl_errors
    if errors:
        for e in errors:
            print(f"FAIL {e}")
        print(f"\nFAIL [{VALIDATE_TAG}] — {len(errors)}건 (추론 모드)")
        return EXIT_FAIL
    print(f"PASS [{VALIDATE_TAG}] — 파일 {n_files}개, 추론 모드")
    return 0
```
<!-- 인용 끝 -->
