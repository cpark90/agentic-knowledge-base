---
id: https://agentic-knowledge-base.dev/id/chunk/580a3b59-587a-4b6a-9e51-73b42edc5251
type: artifact
level: executable
title_ko: 절 gendoc-version (tools/kb_lib.py)
title: section gendoc-version in tools/kb_lib.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-kb-lib}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-02T00:08:55Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ad8f9fc0-eedf-44e1-a93f-65f667e359ce
composite: {id: https://agentic-knowledge-base.dev/id/composite/ad8f9fc0-eedf-44e1-a93f-65f667e359ce, title_ko: 절 복합체 gendoc-version (tools/kb_lib.py), title: section composite gendoc-version in tools/kb_lib.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/580a3b59-587a-4b6a-9e51-73b42edc5251, https://agentic-knowledge-base.dev/id/chunk/a720999d-da2c-4b54-9c40-b64df9c9a74a, https://agentic-knowledge-base.dev/id/chunk/0c73f827-eef2-4929-a126-f9b2c056d037, https://agentic-knowledge-base.dev/id/chunk/f243c562-ded5-4297-9b93-44e75ff0822e, https://agentic-knowledge-base.dev/id/chunk/bb657e8b-5946-421e-bfcb-8829e044c9e2, https://agentic-knowledge-base.dev/id/chunk/dcdad310-25df-4a9e-8939-6ef8be6f1e20], part_of: https://agentic-knowledge-base.dev/id/composite/9b61f2e4-e29d-4fe0-8a4f-f1be5708e79a}
---
**절** — `tools/kb_lib.py` 의 절 `gendoc-version` 다. 생성 문서 규약 G1~G18 — 에이전트가 만드는 마크다운의 형태 (유저 지시 2026-09-21)

**정의** — `utc_stamp` · `now_utc` · `pct` · `num` · `gendoc_input_name` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 생성 문서 규약 G1~G18 — 에이전트가 만드는 마크다운의 형태 (유저 지시 2026-09-21) ─────────────
# 출력 형태를 생성 전에 고정하고, 파싱·형식 복구를 없애며, 확신 상태(입력 지문·생성 시각·질의)를 값으로 남긴다.
# 여기가 규약의 단일 정의처다 — 상수·머리 블록 방출·검사가 한 곳에 있고 생성기와 게이트가 같은 것을 import 한다 (STYLEGUIDE §7).
# G16(표기 통일성)·G17 오탐률 실측(2026-09-29, 생성 뷰 전부 + SKILL.md 19)으로 G16 은 표기 통일성 부분만 게이트로
# 올렸다(19건 중 1건, 오탐 0) — "목표를 붙여야 하는가"는 여전히 사람 판단이다. G17 은 후보 7건 전부가 오탐이라
# (CQ 정식 문구·주석 인용·이미 값이 있는 문장의 부연) 게이트로 올리지 않고 check_gendoc 의 둘째 반환값(보고 전용)으로만 낸다.
GENDOC_VERSION = "gendoc/1"               # OKF 행위자 표기의 버전 (docs/rules.md 생성자 표기). 도구별이 아니라 규약 하나의 버전이다
GENDOC_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"  # G3 — ISO 8601 UTC 초 해상도. 오프셋 표기(+00:00)·분 해상도를 쓰지 않는다
GENDOC_TIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
NONE_MARK = EMPTY_REVIEWED                # G14 — 생성 문서의 빈 값 표기. 빈 셀·em dash·"N/A" 를 쓰지 않는다. 정의처는 EMPTY_VALUE 셋의 첫 값 하나다
RATIO_DIGITS = 1                          # G15 — 백분율 소수 자릿수
VALUE_DIGITS = 3                          # G15 — 백분율이 아닌 수치(모듈러리티 Q·Jaccard·링크 밀도·소요 초)의 자릿수
GENDOC_TOC_MIN = 120                      # G12 — 본문이 이 줄 수를 넘으면 목차 절을 둔다 (ISO/IEC/IEEE 26514:2022 9.10.5)
GENDOC_TOC_HEADING = "목차"
GENDOC_INPUT_INLINE_MAX = 6               # G4 — 입력 목록을 머리 블록에 그대로 쓰는 상한. 넘으면 입력 파일 절로 접는다
GENDOC_INPUTS_HEADING = "입력 파일"
GENDOC_HEAD_KEYS = ("생성기", "생성 시각", "입력", "질의", "재현")  # 순서 고정 (G2~G6). 그 뒤가 성격 경고 한 줄 (G7)
GENDOC_H1_SUFFIX = "(생성 파일)"
GENDOC_VIEW_MARK = "이 파일은 뷰다."              # G7 — Bazel 뷰
GENDOC_TREE_MARK = "생성 파일 — 손으로 고치지 않는다."  # G7 — 생성 트리 파일 (SKILL·BUILD)
GENDOC_DETERMINISTIC_NOTE = "생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다"
# 인용 구역 — 생성물이 청크 본문을 그대로 옮긴 자리. 원본 청크가 자기 게이트(chunk_lint prose·본문 토큰 상한)를 이미 통과했고
# 생성기는 원문을 고쳐 쓰지 않으므로(p12-generated-document-form), 서식 규칙 G10·G11·G14·G15·G16·G18 은 이 구역을
# 판정하지 않는다. 문서 전체에 걸리는 구조 규칙 G8·G9·G12·G13 은 구역 안에도 그대로 적용한다 — 인용이 문서를 깨뜨리면 안 된다.
GENDOC_QUOTE_OPEN = "<!-- 인용 시작: 청크에서 그대로 옮긴 값 — 원본이 자기 게이트를 통과했다 -->"
GENDOC_QUOTE_CLOSE = "<!-- 인용 끝 -->"
GENDOC_QUOTE_LINE = "<!-- 인용 -->"  # 한 줄짜리 인용 — 라벨처럼 그래프에서 그대로 가져온 값을 담은 줄의 끝에 붙인다
GENDOC_QUOTE_EXEMPT = ("G10", "G11", "G14", "G15", "G16", "G18")
_GENDOC_BAZEL_OUT = re.compile(r"^(?:\.\./)*(?:bazel-out/[^/]+/(?:bin|genfiles)/|external/)")
_GENDOC_PCT = re.compile(r"(?<![\d/.])(\d+(?:\.\d+)?)%")
_GENDOC_PCT_OK = re.compile(r"\d+/\d+ = \*{0,2}$")
_GENDOC_EMPTY_CELL = re.compile(r"^(?:|-|—|–|N/A|n/a|없음\s*\(\s*\))$")
# G16 — 목표 표기(STYLEGUIDE §9 권장, 결정 p12-generated-document-form "목표 표기" 행): 목표가 정의된 수치에는
# `(목표 <값>)`을 붙이고 표기를 한 꼴로 맞춘다. "붙여야 하는가"(그 수치에 목표가 정의돼 있는가)는 문서 밖 지식이라
# 사람 판단으로 남긴다 — 여기서 기계 판정하는 것은 이미 쓰인 표기의 통일성뿐이다. 콜론 변형 `(목표: …)`은 그 밖의
# 전부(`(목표 …)`, 공백 하나 뒤 값)와 갈라진 표기다(2026-09-29 오탐률 실측 — 생성 뷰 전부에서 19건 중 1건, 오탐 0).
GENDOC_TARGET_BAD_RE = re.compile(r"\(목표:")
# G17(보고 전용, 게이트 아님) — 시점 의존 표현(STYLEGUIDE §9 권장): "현재·최신·지금"을 값 대신 쓰지 않는다.
# "값 대신 쓰였는가"는 기계로 못 가른다 — 2026-09-29 오탐률 실측에서 인용·제목·표 헤더를 뺀 후보 7건 전부가
# CQ 정식 문구·주석 청크 본문의 인용·이미 값이 적힌 문장의 부연이라 오탐이었다(kg/cq.md·kg/metrics.md·kg/open.md).
# 그래서 게이트로 올리지 않고 후보만 낸다 — 판정은 사람 몫이다.
GENDOC_TIME_WORD_RE = re.compile(r"현재|최신|지금")
```
<!-- 인용 끝 -->
