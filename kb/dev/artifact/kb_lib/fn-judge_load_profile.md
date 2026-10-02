---
id: https://agentic-knowledge-base.dev/id/chunk/2cabfcc4-8242-47a2-9710-9ed682ab9f2b
type: artifact
level: executable
title_ko: 함수 judge_load_profile (tools/kb_lib.py)
title: function judge_load_profile in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-28T22:13:05Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/558e3a5c-2634-4500-bc61-15dad26a9821
---
**함수** — `judge_load_profile(root, profile, shapes)` 다. 판정 질문·척도·임계 프로파일 온톨로지 모듈과 shape 를 한 그래프로 읽는다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
def judge_load_profile(root: Path, profile: str = JUDGE_PROFILE_DIR, shapes: str = JUDGE_QUESTION_SHAPES) -> Graph:
    """판정 질문·척도·임계 프로파일 온톨로지 모듈과 shape 를 한 그래프로 읽는다.

    단일 정의처(2026-09-30 vnv 결함 보고 ⑥) — `tools/judge.py`(질문을 청크에 묻는다)와 `tools/label_sample.py`
    (`--judge-sheet`의 척도 문장을 프로파일에서 그대로 옮긴다)가 이 함수와 `judge_questions`를 같이 쓴다. 둘이
    각자 질의를 복제하면 척도 문장이 갈릴 위험이 생긴다 — 갈리면 판정자가 sheet에서 본 척도와 judge.py 가 파싱하는
    척도가 달라진다."""
    g = Graph()
    files = sorted((root / profile).glob("*.ttl")) + ([root / shapes] if (root / shapes).is_file() else [])
    if not files:
        raise ValueError(f"{profile}: 프로파일 TTL 이 없다 — 질문·척도·임계의 원본이 거기다")
    for f in files:
        g.parse(f, format="turtle")
    return g
```
<!-- 인용 끝 -->
