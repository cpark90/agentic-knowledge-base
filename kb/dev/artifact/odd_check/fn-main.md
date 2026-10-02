---
id: https://agentic-knowledge-base.dev/id/chunk/4854fed0-fd7f-4265-a159-21940432a740
type: artifact
level: executable
title_ko: 함수 main (tools/odd_check.py)
title: function main in tools/odd_check.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-odd-check}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-22T11:38:01Z}
layer: process
verified: [{by: process:bazel-test, at: 2026-09-30T15:34:48Z}]
uses: [https://agentic-knowledge-base.dev/id/chunk/0644b925-2088-4a6a-bc60-18ffa1808aa1, https://agentic-knowledge-base.dev/id/chunk/90f688eb-3f5a-4fec-bfc7-b1a2185f172d, https://agentic-knowledge-base.dev/id/chunk/d4ad9c8b-b1ad-417c-8d8e-bd440024008e]
part_of: https://agentic-knowledge-base.dev/id/composite/f0f7ba13-f15d-489f-80df-4c7ae50b0cdd
---
**함수** — `main()` 다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--odd", default="kb/odd/project-odd.yml")
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    root = Path(os.environ.get("BUILD_WORKSPACE_DIRECTORY", "."))
    rows = judge_all(load_odd(root / a.odd), root)
    text, out_of = render(a.odd, rows)
    print(text)
    if a.out:
        Path(a.out).write_text(text, encoding="utf-8")
    return 1 if out_of else 0
```
<!-- 인용 끝 -->
