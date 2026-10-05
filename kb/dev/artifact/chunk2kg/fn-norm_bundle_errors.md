---
id: https://agentic-knowledge-base.dev/id/chunk/15c626f2-ee68-4a3b-a918-8a5054875a54
type: artifact
level: executable
title_ko: 함수 norm_bundle_errors (tools/chunk2kg.py)
title: function norm_bundle_errors in tools/chunk2kg.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-chunk2kg}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/679fc45f-a074-446c-aa6b-755cb0329d4f
---
**함수** — `norm_bundle_errors(declarer, members)` 다. 한 문서(복합체)의 절 청크 구분 — 머리 청크(선언)는 절 키가 없고 그 밖의 부분은 heading·depth 를 갖는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def norm_bundle_errors(declarer: dict, members: list[tuple[dict, str]]) -> list[str]:
    """한 문서(복합체)의 절 청크 구분 — 머리 청크(선언)는 절 키가 없고 그 밖의 부분은 heading·depth 를 갖는다.

    `declarer` 는 선언 청크의 메타(경로는 `_path`), `members` 는 (메타, 경로) 목록이다. 머리 청크만의 키(numbering·strength)가
    절 청크에 있어도 거부한다 — 문서 하나에 값 하나다. 묶음 복합체(문서 복합체 아래의 중첩)는 머리 청크가 없다 — `declarer` 가
    None 이면 부분 전부(선언한 첫 절 청크 포함)를 절 청크로 본다.
    """
    errors = []
    dpath = (declarer or {}).get("_path", "")
    for k in NORM_SECTION_KEYS if declarer is not None else ():
        if k in declarer:
            errors.append(f"{dpath}: 머리 청크(composite: 선언)는 {k} 를 갖지 않는다 — 본문이 문서 도입문·범례이고 절은 다른 청크다 "
                          f"(p12-norm-documents-from-section-chunks)")
    for meta, path in members:
        if meta is declarer or meta.get("type") != NORM_TYPE:
            continue
        if meta.get(NORM_CONTINUES_KEY) == "true":  # 이어짐 절 청크 — 제목·깊이가 없다(check_norm_bundle_form)
            continue
        for k in (NORM_HEADING_KEY, NORM_DEPTH_KEY):
            if k not in meta:
                errors.append(f"{path}: 절 청크에 {k} 가 없다 — 머리 청크 밖의 절 청크는 heading·depth 를 갖는다"
                              f"(이어짐 절 청크 {NORM_CONTINUES_KEY}: true 만 예외다)")
        for k in NORM_HEAD_KEYS:
            if k in meta:
                errors.append(f"{path}: {k} 는 머리 청크(composite: 선언)만의 키다 — 문서 하나에 값 하나다")
    return errors
```
<!-- 인용 끝 -->
