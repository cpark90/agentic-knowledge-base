---
id: https://agentic-knowledge-base.dev/id/chunk/cca34039-f0b1-466a-bdb0-ed871d10347c
type: artifact
level: executable
title_ko: 함수 fixed_sentence_coverage (tools/metrics.py)
title: function fixed_sentence_coverage in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
part_of: https://agentic-knowledge-base.dev/id/composite/46ce1955-674a-4ac3-bec9-631ef1d8c5c7
---
**함수** — `fixed_sentence_coverage(a, live, plane, parts, siblings)` 다. 설계 노트의 [확정] 절 중 청크가 인용한 절의 비율을 한 줄로 돌려준다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def fixed_sentence_coverage(a, live, plane, parts, siblings):
    """설계 노트의 [확정] 절 중 청크가 인용한 절의 비율을 한 줄로 돌려준다."""
    # 1단계 의미 보존 대리 — 확정 문장 커버리지: [확정]이 있는 절 중 결정이 인용하는 절의 비율
    cov_line = "- 의미 보존: 확정 문장 커버리지 — `--notes` 없음"
    if a.notes:
        import re as _re
        text = Path(a.notes).read_text(encoding="utf-8")
        sec, cur = {}, None
        for ln in text.splitlines():
            m = _re.match(r"^## (\d+\.\d+) ", ln)
            if m: cur = m.group(1); sec.setdefault(cur, 0)
            elif cur and "[확정]" in ln: sec[cur] += 1
        with_fixed = {k for k, v in sec.items() if v}
        cited = set()
        for b_ in a.bodies:
            cited |= set(_re.findall(r"(?<![\d.])(\d{1,2}\.\d{1,2})절", Path(b_).read_text(encoding="utf-8")))  # "노트 N.N절"과 "(N.N절)" 둘 다
        missing = sorted(with_fixed - cited, key=lambda x: [int(t) for t in x.split(".")])
        cov_line = (f"- 의미 보존: 확정 문장 커버리지(절 단위) **{kb_lib.pct(len(with_fixed & cited), len(with_fixed))}** — "
                    f"[확정] {sum(sec.values())}문장, 결정 {sum(1 for c in live if plane[c]=='decision' and c not in parts) + len(siblings)}개. 인용 없는 절: " + (", ".join(missing) or "없음"))
    return cov_line
```
<!-- 인용 끝 -->
