---
id: https://agentic-knowledge-base.dev/id/chunk/5d6ffe38-1280-4b10-a5aa-c79e35a4f0bd
type: artifact
level: executable
title_ko: 절 gates (defs/kb.bzl)
title: section gates in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/b5154bf0-e67d-4227-8b66-c63012041201
---
**절** — `defs/kb.bzl` 의 절 `gates` 다. 게이트 목록 — id 순서로 잇는 리터럴 둘(`GATES` · `GATES_TAIL`)의 앞이다. 순서와 서로소는 `kb_lib.load_gates` 가 강제한다

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
# ── 게이트 목록 — id 순서로 잇는 리터럴 둘(`GATES` · `GATES_TAIL`)의 앞이다. 순서와 서로소는 `kb_lib.load_gates` 가 강제한다 ──
GATES = {
    "addition": {"tier": "test", "tool": "chunk_lint", "ko": "첨가", "desc": "슬롯의 질문에 답하지 않는 메타 문장과 채움 문구"},
    "blocking-comment": {"tier": "test", "tool": "chunk_lint", "ko": "해소되지 않은 차단 주석", "desc": "issue (blocking) 이면서 해소가 열린 살아 있는 주석"},
    "boundary": {"tier": "verify", "tool": "validate", "ko": "정의 경계", "desc": "한 용어가 두 모듈 파일에서 정의됨"},
    "build-drift": {"tier": "test", "tool": "gen_build", "ko": "BUILD 드리프트", "desc": "생성 BUILD 가 frontmatter 링크와 어긋남"},
    "canon": {"tier": "test", "tool": "canonicalize", "ko": "정규 직렬화", "desc": "TTL 직렬화가 정규형과 다름"},
    "case-drift": {"tier": "test", "tool": "case_gen", "ko": "케이스 드리프트", "desc": "저장소의 케이스가 논리 시나리오의 생성 결과와 어긋나거나 생성기 밖에서 쓰임"},
    "case-gen": {"tier": "analysis", "tool": "case_gen", "ko": "케이스 생성", "desc": "생성 시점의 입력 위반 — 표본 근거 없는 케이스, ODD 속성이 아닌 변수, keep 안의 요인 값, 실행기가 읽지 못하는 케이스"},
    "catalog": {"tier": "verify", "tool": "validate", "ko": "카탈로그 정합성", "desc": "스코프 없는 역할, 미부여 스코프, write plane 공유, maxConcurrent 합 초과"},
    "channel": {"tier": "test", "tool": "channel_lint", "ko": "채널 규약", "desc": "하네스 채널(메시지·질문지)의 어휘·단일 작성자·필수 절·짝 없는 완료 위반"},
    "chunk": {"tier": "test", "tool": "chunk_lint", "ko": "청크 형식", "desc": "본문 토큰 상한 초과와 frontmatter 형식 위반"},
    "chunk2kg": {"tier": "analysis", "tool": "chunk2kg", "ko": "head 생성", "desc": "head 그래프 생성 시점의 frontmatter·본문 규칙 위반"},
    "chunk2kg-merge": {"tier": "analysis", "tool": "chunk2kg", "ko": "head 병합", "desc": "타깃별 head 조각의 병합 실패"},
    "code-part-link": {"tier": "verify", "tool": "validate", "ko": "코드 부분 링크", "desc": "추출 트리의 복합체 부분(정의·구역 청크)이 refines·serves·verifies 의 끝점"},
    "cross-kb-link": {"tier": "verify", "tool": "validate", "ko": "KB 가로지름 링크", "desc": "verifies 밖의 저작 링크가 두 KB 를 가로지름 (검증 목표 → 요구 derivesFrom 만 예외)"},
    "dangling": {"tier": "verify", "tool": "validate", "ko": "참조 무결성", "desc": "인용·부분·가정·요구·정의 호출의 대상이 실재하지 않음"},
    "decision-role": {"tier": "test", "tool": "chunk_lint", "ko": "결정 역할 표지", "desc": "결론·근거·대안·규약 청크의 첫 산문 줄에 역할 표지가 없음"},
    "doccheck": {"tier": "test", "tool": "doccheck", "ko": "문서 현행성", "desc": "문서의 죽은 링크·앵커·백틱 경로와 산문 문체 위반"},
    "element-drop": {"tier": "verify", "tool": "validate", "ko": "요소 탈락", "desc": "어휘에 슬롯이 없어 조용히 빠진 소스 요소"},
    "empty-value": {"tier": "test", "tool": "chunk_lint", "ko": "빈 값 표기", "desc": "세 빈 값 밖의 표기와 표의 단독 대시 셀"},
    "extract": {"tier": "analysis", "tool": "extract", "ko": "코드 추출", "desc": "추출 시점의 개명 안내·삭제·부분 상한·등록부 불일치"},
    "extract-drift": {"tier": "test", "tool": "extract", "ko": "추출 드리프트", "desc": "추출 생성물이 소스와 등록부에 어긋남"},
    "extract-refs": {"tier": "analysis", "tool": "extract_refs", "ko": "인용 대상 실재", "desc": "본문 인용의 대상이 실재하지 않음"},
    "frozen": {"tier": "test", "tool": "doccheck", "ko": "동결 문서", "desc": "동결 문서의 sha256 이 kb_lib.FROZEN_DOCS 의 고정값과 다름"},
    "gate-registry": {"tier": "verify", "tool": "validate", "ko": "게이트 등록부", "desc": "코드의 게이트 태그 집합이 GATES 리터럴과 갈림"},
    "gates2kg": {"tier": "analysis", "tool": "gates2kg", "ko": "게이트 그래프 생성", "desc": "게이트 등록부의 키·실행 계층 위반과 판정 도구 개체의 부재"},
}
```
<!-- 인용 끝 -->
