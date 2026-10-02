---
id: https://agentic-knowledge-base.dev/id/chunk/de2f167c-8f4b-4825-b54a-474da6a94ab8
type: artifact
level: executable
title_ko: 함수 main (tools/vv_run_env_test.py)
title: function main in tools/vv_run_env_test.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-vv-run-env-test}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-26T10:39:33Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/4ec05239-7f7f-4a11-93fb-cc78958546b5, https://agentic-knowledge-base.dev/id/chunk/75a41a5b-41f9-406e-a6e7-ef2d50a688ec, https://agentic-knowledge-base.dev/id/chunk/890796e2-4d86-47b3-8963-ccab2ab97d40]
part_of: https://agentic-knowledge-base.dev/id/composite/491eacc1-0150-4673-96c8-52951bec7409
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--probe", default="chunk_lint", metavar="VERIFIER",
                    help="하위 프로세스로 띄울 읽기 전용 검증기 — tools/<이름>.py --help 를 부른다")
    a = ap.parse_args()
    root = Path.cwd()  # bazel test 는 runfiles 루트가, 손으로 돌리면 워크스페이스 루트가 cwd 다
    if a.probe not in vv_run.READ_ONLY_VERIFIERS:
        print(f"FAIL [{GATE}] --probe {a.probe}: 허용 목록(vv_run.READ_ONLY_VERIFIERS) 밖이다 — "
              "격리를 재는 자극은 읽기 전용 검증기여야 한다")
        return kb_lib.EXIT_CONFIG
    if not (root / "tools" / f"{a.probe}.py").is_file():
        print(f"FAIL [{GATE}] tools/{a.probe}.py: 없다 — 워크스페이스 루트(또는 runfiles 루트)에서 돌린다")
        return kb_lib.EXIT_CONFIG
    msgs = check_strip() + check_subprocess(root, a.probe) + check_cwd(root)
    for m in msgs:
        print(m)
    if msgs:
        return kb_lib.EXIT_FAIL
    print(f"OK [{GATE}] 걷어내는 변수 {len(EXPECTED_ENV)} · 검증기 {a.probe} 종료 0 · 작업 디렉토리 {root.resolve()}")
    return kb_lib.EXIT_OK
```
<!-- 인용 끝 -->
