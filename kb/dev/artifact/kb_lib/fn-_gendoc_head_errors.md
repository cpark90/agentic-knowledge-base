---
id: https://agentic-knowledge-base.dev/id/chunk/2c1b164b-eed1-4874-8bee-b8c56033e286
type: artifact
level: executable
title_ko: 함수 _gendoc_head_errors (tools/kb_lib.py)
title: function _gendoc_head_errors in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T15:04:08Z}
layer: process
uses: [https://agentic-knowledge-base.dev/id/chunk/a9138ecc-8714-414e-a8f3-69d0c646e65d]
part_of: https://agentic-knowledge-base.dev/id/composite/a3a476aa-1402-4998-a124-e37b5596aa09
---
**함수** — `_gendoc_head_errors(body, first, rows)` 다. G1·G2~G7 — 머리 블록의 위반.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def _gendoc_head_errors(body: list[str], first: int, rows: list) -> list[tuple[int, str]]:
    """G1·G2~G7 — 머리 블록의 위반. 첫 줄이 h1 이고 그 뒤 머리 키의 순서·값이 고정이다."""
    errors: list[tuple[int, str]] = []
    # h1 한 줄이 첫 줄이고 그 뒤 머리 키의 순서가 고정이다 — `first` 는 본문 첫 줄의 파일 줄 번호다
    if not body or not re.fullmatch(r"# \S.*" + re.escape(GENDOC_H1_SUFFIX), body[0]):
        errors.append((first, f"G1 첫 줄이 `# <이름> — <목적> {GENDOC_H1_SUFFIX}` 가 아니다 — kb_lib.gendoc_header 로 낸다"))
    else:
        if len(body) < 2 or body[1].strip():
            errors.append((first + 1, "G1 h1 다음 줄은 빈 줄이다 — kb_lib.gendoc_header 로 낸다"))
        head = []
        for i, line in enumerate(body[2:], start=2):
            if not line.startswith("- "):
                break
            head.append((first + i, line))
        keys = [k for k in GENDOC_HEAD_KEYS]
        got = [(ln, line[2:].split(":", 1)[0]) for ln, line in head]
        want = [k for k in keys if k != "생성 시각" or any(g == "생성 시각" for _, g in got)]
        for i, k in enumerate(want):
            if i >= len(got) or got[i][1] != k:
                errors.append((head[i][0] if i < len(head) else first + 2,
                               f"G2~G6 머리 블록 {i + 1}번째 항목은 `- {k}:` 다 — 순서는 {' · '.join(want)} 이고 그 뒤가 성격 경고 한 줄이다"))
                break
        else:
            v = {k: head[i][1][2:].split(": ", 1)[-1] for i, k in enumerate(want)}
            if GENDOC_VERSION.split("/")[0] + "/" not in v["생성기"]:
                errors.append((head[0][0], f"G2 생성기 줄에 규약 버전 표기 `{GENDOC_VERSION}` 가 없다 — kb_lib.GENDOC_VERSION 이 단일 정의처다"))
            if "생성 시각" in v and not GENDOC_TIME_RE.fullmatch(v["생성 시각"].strip()):
                errors.append((head[want.index("생성 시각")][0],
                               f"G3 생성 시각이 `{GENDOC_TIME_FORMAT}` 가 아니다 (실제 {v['생성 시각'].strip()!r}) — kb_lib.now_utc 를 쓴다"))
            i_in = head[want.index("입력")][0]
            if "생성 시각" in v and "지문 `sha256:" not in v["입력"]:
                errors.append((i_in, "G4 입력 줄에 지문(`sha256:<앞 12자>`)이 없다 — kb_lib.input_fingerprint 를 쓴다"))
            if "개:" not in v["입력"] and f"#{slug(GENDOC_INPUTS_HEADING)}" not in v["입력"] and NONE_MARK not in v["입력"]:
                errors.append((i_in, f"G4 입력 줄에 파일 목록이 없다 — 개수만 적지 않는다. 많으면 `{GENDOC_INPUTS_HEADING}` 절로 접는다"))
            if f"#{slug(GENDOC_INPUTS_HEADING)}" in v["입력"] and not any(
                    (m := MD_HEADING.match(line)) and m.group(2).strip() == GENDOC_INPUTS_HEADING for _, line in rows):
                errors.append((i_in, f"G4 입력 줄이 `{GENDOC_INPUTS_HEADING}` 절을 가리키는데 그 절이 없다 — kb_lib.gendoc_inputs_section 을 붙인다"))
            if "`" not in v["재현"]:
                errors.append((head[want.index("재현")][0], "G6 재현 줄의 명령은 백틱 안에 적는다 — 자기 자신을 다시 만드는 명령이다"))
            notice = head[len(want)][1] if len(head) > len(want) else ""
            if GENDOC_VIEW_MARK not in notice and GENDOC_TREE_MARK not in notice:
                errors.append((head[len(want) - 1][0] + 1,
                               "G7 머리 블록 끝에 성격 경고 한 줄이 없다 — kb_lib.gendoc_view_notice · gendoc_tree_notice"))
    return errors
```
<!-- 인용 끝 -->
