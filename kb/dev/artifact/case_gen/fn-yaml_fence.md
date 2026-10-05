---
id: https://agentic-knowledge-base.dev/id/chunk/e222b91b-3e94-4d2c-a3f9-cf2851ce0d9f
type: artifact
level: executable
title_ko: 함수 yaml_fence (tools/case_gen.py)
title: function yaml_fence in tools/case_gen.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-case-gen}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-04T04:52:48Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/098b0459-1cbf-4bc0-8bad-a7a5f9cee7fc, https://agentic-knowledge-base.dev/id/chunk/b23dee78-99ba-49f8-bcde-88ea157cbe7a, https://agentic-knowledge-base.dev/id/chunk/c321eb50-ec20-462b-b4cd-c1d3a46065a8]
part_of: https://agentic-knowledge-base.dev/id/composite/7cb71e27-ad8a-449d-b46a-454149642b32
---
**함수** — `yaml_fence(key, value)` 다. `files` 또는 `expect` 펜스 — 손으로 내고 실행기의 꼴로 되읽어 같은지 본다(생성기의 자기 검사).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def yaml_fence(key: str, value) -> list[str]:
    """`files` 또는 `expect` 펜스 — 손으로 내고 실행기의 꼴로 되읽어 같은지 본다(생성기의 자기 검사).

    literal 블록이 실행기의 읽기에서 내용을 바꾸면(펜스 끝의 줄바꿈이 잘린다) 그 파일만 큰따옴표 한 줄로 다시 낸다.
    """
    if key == "files":
        quoted: set[str] = set()
        for _ in range(2):
            lines = ["```yaml", f"{key}:"]
            for name, content in value.items():
                sc = yaml_scalar(content, "  ", name not in quoted)
                lines += [f"  {name}: {sc[0]}"] + sc[1:]
            lines.append("```")
            back = read_back(lines)
            got = back.get(key, {}) if isinstance(back, dict) and isinstance(back.get(key), dict) else {}
            quoted |= {n for n, c in value.items() if got.get(n) != c}
        want = value
    else:
        lines = ["```yaml", f"{key}:"]
        for e in value:
            lines.append(f"  - exit: {int(e.get('exit', 0))}")
            phrases = vv_run.phrases(e.get("contains"))
            if phrases:
                lines.append("    contains:")
                lines += [f"      - {json.dumps(p, ensure_ascii=False)}" for p in phrases]
        lines.append("```")
        want = [{"exit": int(e.get("exit", 0)), **({"contains": vv_run.phrases(e["contains"])} if e.get("contains") else {})} for e in value]
    if read_back(lines) != {key: want}:
        raise CaseGenError(f"`{key}` 펜스가 실행기의 꼴로 되읽어 같지 않다 — 생성기의 직렬화 결함이다")
    return lines
```
<!-- 인용 끝 -->
