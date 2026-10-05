---
id: https://agentic-knowledge-base.dev/id/chunk/7da9bdbd-c81f-432f-a9a2-fe6561f504be
type: artifact
level: executable
title_ko: 함수 pkg_group (tools/gen_build.py)
title: function pkg_group in tools/gen_build.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-gen-build}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/b9a75b3d-1c8f-4a7a-8f7f-dc10a84362fa
---
**함수** — `pkg_group(pkg)` 다. 패키지의 본문 filegroup 이름 — 디렉토리 이름과 같다

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def pkg_group(pkg: str) -> str:
    """패키지의 본문 filegroup 이름 — 디렉토리 이름과 같다 (STYLEGUIDE §6). 그래서 `//kb/dev` 처럼 타깃 이름 없이 가리킨다."""
    return pkg.rsplit("/", 1)[-1]
```
<!-- 인용 끝 -->
