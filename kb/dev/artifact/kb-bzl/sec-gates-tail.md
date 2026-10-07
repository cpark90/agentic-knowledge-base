---
id: https://agentic-knowledge-base.dev/id/chunk/efa22138-0bbd-46c9-a448-bff8a2787a6e
type: artifact
level: executable
title_ko: 절 gates-tail (defs/kb.bzl)
title: section gates-tail in defs/kb.bzl
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-defs-kb}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-05T16:40:36Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/b5154bf0-e67d-4227-8b66-c63012041201
---
**절** — `defs/kb.bzl` 의 절 `gates-tail` 다. 게이트 목록의 이어짐 — 앞 리터럴의 id 순서를 잇는다 (청크 하나의 인용 상한 2,856토큰, 2026-10-05)

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```starlark
# ── 게이트 목록의 이어짐 — 앞 리터럴의 id 순서를 잇는다 (청크 하나의 인용 상한 2,856토큰, 2026-10-05) ──
# 리터럴 하나가 추출 청크 하나라 게이트가 늘면 인용 상한을 넘는다. 그래서 id 순서를 유지한 채 둘로 잇는다 — 앞의 마지막
# id 보다 뒤의 첫 id 가 뒤이고 두 리터럴은 서로소다(`kb_lib.load_gates` 가 둘을 읽어 대조한다). 판정 대상은 합친 `GATES` 다
GATES_TAIL = {
    "gen-build": {"tier": "analysis", "tool": "gen_build", "ko": "BUILD 생성", "desc": "생성 시점의 묶음·세 청크·링크 규칙 위반"},
    "gen-norms": {"tier": "analysis", "tool": "gen_norms", "ko": "규범 문서 생성", "desc": "생성 시점의 절 청크·규약 줄 위반 — 고아 줄·이중 소비·없는 줄·강도 없는 줄·문서 목록 불일치"},
    "gen-skills": {"tier": "analysis", "tool": "gen_skills", "ko": "skill 생성", "desc": "skill 생성 시점의 입력 위반"},
    "gendoc": {"tier": "test", "tool": "gendoc", "ko": "생성 문서 형태", "desc": "생성 마크다운의 머리 블록과 본문 서식 규약 위반"},
    "judge-log": {"tier": "test", "tool": "chunk_lint", "ko": "판정 로그", "desc": "판정 로그의 표 형식과 필수 필드 위반"},
    "labels": {"tier": "verify", "tool": "validate", "ko": "라벨 완전성", "desc": "agt: 용어의 한·영 라벨 또는 skos:definition 누락"},
    "list-rules": {"tier": "test", "tool": "chunk_lint", "ko": "목록 규칙", "desc": "손 번호·항목 수·중첩·길이·빈 항목의 목록 규칙 위반"},
    "naming": {"tier": "test", "tool": "chunk_lint", "ko": "파일 접미사", "desc": "TTL 파일 이름이 접미사 규약 밖"},
    "norms-drift": {"tier": "test", "tool": "gen_norms", "ko": "규범 문서 드리프트", "desc": "생성 규범 문서가 절 청크와 결정의 규약 줄에 어긋남"},
    "odd-ref": {"tier": "verify", "tool": "validate", "ko": "ODD 참조", "desc": "ODD 에 없는 조건을 참조하는 스코프·가정·변수"},
    "odd2kg": {"tier": "analysis", "tool": "odd2kg", "ko": "ODD 생성", "desc": "OpenODD 문서의 형식과 필수 필드 위반"},
    "prose": {"tier": "test", "tool": "chunk_lint", "ko": "산문 문체", "desc": "경어체 종결과 산문의 느낌표"},
    "residency": {"tier": "verify", "tool": "validate", "ko": "수준 허용표 단일 정의처", "desc": "수준 허용표 shape 가 RESIDENCY 리터럴과 갈림"},
    "restored": {"tier": "analysis", "tool": "chunk2kg", "ko": "복원 표시", "desc": "restored 의 IRI 가 같은 청크의 링크 키 대상에 없음"},
    "rung-before-descent": {"tier": "verify", "tool": "validate", "ko": "정제 계층 사슬", "desc": "같은 정제 수준의 V&V 대응물(목표·기준·검증기 바인딩) 없이 다음 정제 수준으로 내려간 정제"},
    "shacl": {"tier": "shape", "tool": "validate", "ko": "shape 적합성", "desc": "SHACL shape 부적합"},
    "skills-drift": {"tier": "test", "tool": "gen_skills", "ko": "skill 드리프트", "desc": "생성 skill 이 docstring 과 SKILLS 에 어긋남"},
    "space": {"tier": "analysis", "tool": "space2kg", "ko": "설계 공간", "desc": "근거 없는 배제, 확정 후보 수, 변수와 후보의 불일치"},
    "specialization": {"tier": "analysis", "tool": "chunk2kg", "ko": "특수화 링크", "desc": "specializationOf 의 자기 참조·plane 불일치·폐기 대상·순환"},
    "stamp": {"tier": "test", "tool": "stamp", "ko": "도장", "desc": "도장 입력이 등록부와 어긋남"},
    "summary-support": {"tier": "test", "tool": "chunk_lint", "ko": "요약 지지 참조", "desc": "요약 블록의 핵심 항목에 지지 참조가 없음"},
    "syntax": {"tier": "verify", "tool": "validate", "ko": "구문", "desc": "TTL 이 파싱되지 않음"},
    "taxonomy": {"tier": "analysis", "tool": "taxonomy", "ko": "택소노미 생성", "desc": "택소노미 생성 입력이 읽히거나 파싱되지 않음"},
    "tim": {"tier": "analysis", "tool": "starlark", "ko": "TIM", "desc": "링크 타입의 정의역·치역·방향·수준 위반"},
    "token-budget": {"tier": "verify", "tool": "validate", "ko": "토큰 상한 단일 정의처", "desc": "plane 별 본문 토큰 상한의 표와 shape 가 갈림, 어휘 파일 지문 불일치"},
    "verify": {"tier": "verify", "tool": "validate", "ko": "안티패턴", "desc": "안티패턴 SPARQL 질의가 위반 행을 냄"},
    "visibility": {"tier": "analysis", "tool": "bazel", "ko": "의존 방향", "desc": "개발 타깃이 V&V 타깃을 의존함"},
    "vocab": {"tier": "verify", "tool": "validate", "ko": "통제 어휘", "desc": "온톨로지와 등록 표준 어휘 밖의 술어·용어"},
    "vv-case": {"tier": "analysis", "tool": "vv_run", "ko": "V&V 케이스 형식", "desc": "케이스의 기계가 읽는 자극·기대 규약 위반"},
    "vv-run-env": {"tier": "test", "tool": "vv_run_env_test", "ko": "실행기 환경 격리", "desc": "케이스의 명령이 실행기의 파이썬·runfiles 문맥을 물려받음"},
    "workset-budget": {"tier": "analysis", "tool": "workset", "ko": "작업 집합 예산", "desc": "앵커가 있는 작업 집합 뷰가 컨텍스트 예산을 넘음"},
    "writer": {"tier": "human", "tool": "validate", "ko": "승인", "desc": "쓰기 권한 밖의 저작과 검토 없는 stable 전이"},
}

GATES.update(GATES_TAIL)
```
<!-- 인용 끝 -->
