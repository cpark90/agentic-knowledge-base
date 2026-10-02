---
id: https://agentic-knowledge-base.dev/id/chunk/64a3fcde-a6b0-422e-a4e7-290fdaca0959
type: artifact
level: executable
title_ko: 절 report-docs (tools/doccheck.py)
title: section report-docs in tools/doccheck.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-doccheck}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
layer: process
refines: [https://agentic-knowledge-base.dev/id/chunk/54aefb11-98b0-4629-9f11-c112ed9948f5, https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f]
part_of: https://agentic-knowledge-base.dev/id/composite/379df7df-38d0-4a60-b9ed-27e40b758ea3
composite: {id: https://agentic-knowledge-base.dev/id/composite/379df7df-38d0-4a60-b9ed-27e40b758ea3, title_ko: 절 복합체 report-docs (tools/doccheck.py), title: section composite report-docs in tools/doccheck.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/64a3fcde-a6b0-422e-a4e7-290fdaca0959, https://agentic-knowledge-base.dev/id/chunk/dbdeebe3-848d-4908-81dc-0c291b07bbe2, https://agentic-knowledge-base.dev/id/chunk/9ad037aa-26ed-4502-92a5-7bc7dd0855a3, https://agentic-knowledge-base.dev/id/chunk/204439f0-e005-4a79-befc-167bfd308ec9, https://agentic-knowledge-base.dev/id/chunk/6d777811-ef05-4ecd-a3c1-78c66baba749, https://agentic-knowledge-base.dev/id/chunk/6550bab7-f62f-40fd-893e-4d46be446f2f, https://agentic-knowledge-base.dev/id/chunk/cbb17652-19dd-4e9e-833d-0e61dfbd4110, https://agentic-knowledge-base.dev/id/chunk/2674f907-6204-42f7-a25e-6789137904d6, https://agentic-knowledge-base.dev/id/chunk/16c7fdef-8fd8-4248-95ec-85ff4668d9bd], part_of: https://agentic-knowledge-base.dev/id/composite/b5da82da-f5cc-4c80-9fbf-d65784ffee7d}
---
**절** — `tools/doccheck.py` 의 절 `report-docs` 다. 보고 모드 — 문서의 수치 대 생성물의 수치 (V&V 기준 document-table-matches-generated, 현상 agt:documentLag)

**정의** — `num_key` · `name_values` · `snapshot_lines` · `generated_values` · `report_numbers` · `report_doc_path` · `to_rel` · `main` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 보고 모드 — 문서의 수치 대 생성물의 수치 (V&V 기준 document-table-matches-generated, 현상 agt:documentLag) ──────────

REPORT_DOCS = ("docs/roadmap.md", "docs/rules.md", "docs/method.md", "docs/tools.md")
VIEW_PATHS = {"metrics": "bazel-bin/kg/metrics.md", "audit": "bazel-bin/kg/audit.md",
              "candidates": "bazel-bin/kg/link-candidates.md"}
VIEW_BUILD = "bazel build //kg:metrics //kg:audit //kg:link_candidates"
# (이름, 문서에서 이름을 찾는 정규식, ((생성물, 값 한 그룹을 뽑는 정규식), …)) — 이름 열넷의 원본은 V&V 기준 청크의 대조 대상 목록이다.
# 같은 이름의 생성물 값이 둘 이상인 것(매트릭스 채움·후보 링크)은 어느 하나와 같으면 일치로 본다 — 그 애매성 자체가 현상 P21 이다
NUMBER_NAMES = (
    ("살아 있는 청크", r"살아 있는 청크", (("metrics", r"살아 있는 것 ([\d,]*\d)"),)),
    ("고아율", r"고아율", (("metrics", r"## 고아율[\s\S]{0,400}?살아 있는 청크: \*\*[\d,]*\d/[\d,]*\d = ([\d.]+%)"),)),
    ("연결 성분", r"연결 성분", (("metrics", r"연결 성분 \*\*(\d+)\*\*"),)),
    ("매트릭스 채움", r"매트릭스", (("metrics", r"`refines` 매트릭스 채움 (\d+/\d+)"), ("metrics", r"TIM 허용 칸 채움 \*\*(\d+/\d+)"))),
    ("CQ19", r"CQ19", (("metrics", r"executable까지 닿은 요구: \*\*[\d,]*\d/[\d,]*\d = ([\d.]+%)"),)),
    ("CQ20", r"CQ20", (("metrics", r"비요구 청크\(관측·주석 제외\): \*\*[\d,]*\d/[\d,]*\d = ([\d.]+%)"),)),
    ("링크 개체", r"링크 개체", (("metrics", r"링크 개체 \*\*([\d,]*\d)\*\*"), ("audit", r"`agt:Link` \*\*([\d,]*\d)\*\*"))),
    ("확정 링크의 구축·복원 내역", r"확정 링크|구축(?=[ *`]*\d)|복원(?=[ *`]*\d)",
     (("metrics", r"\(확정 ([\d,]*\d) · 후보"), ("metrics", r"구축\(구축 기록 증거뿐\) ([\d,]*\d)"), ("metrics", r"vs 복원 ([\d,]*\d)"))),
    ("복원 비율", r"복원 비율", (("metrics", r"복원 비율 \*\*[\d,]*\d/[\d,]*\d = ([\d.]+%)"),)),
    ("후보 링크", r"후보 링크|링크 후보|후보 수", (("metrics", r"후보 링크 개체\([^)]*\) \*\*(\d+)\*\*"), ("candidates", r"\| 후보 수 \| (\d+) \|"))),
    ("cites", r"cites", (("metrics", r"`agt:cites` (\d+)"),)),
    ("usesConcept", r"usesConcept", (("metrics", r"`agt:usesConcept` ([\d,]*\d)"),)),
    ("확정 문장 커버리지", r"확정 문장 커버리지", (("metrics", r"확정 문장 커버리지\(절 단위\) \*\*([\d,]*\d/[\d,]*\d)"),)),
    ("테스트 수", r"테스트(?=[ *`]*\d)", ()),
)
WINDOW = 24                      # 이름 뒤로 수치를 찾는 창의 글자 수 — 표 셀 하나가 들어가는 폭이다
CELL_END = re.compile(r"[|·]")   # 창의 경계 — 표 셀과 목록 항목의 구분자
NUM_TOKEN = re.compile(r"(\d[\d,]*(?:\.\d+)?)(?:\s*/\s*(\d[\d,]*(?:\.\d+)?))?\s*%?")
# 이름과 값이 붙어 있을 때만 쌍으로 본다 — 사이에 낱말이 들어가면 그 수치는 이 이름의 값이 아니다. 화살표는 예외다("31.6 → 64.5%")
ADJACENT = re.compile(r"[\s*`]{0,3}$|[\s\d.,%/*`]{0,16}[→~][\s*`]{0,3}$")
NOISE = re.compile(r"\d{4}-\d{2}(?:-\d{2})?|\d+(?:\.\d+)?절|§\d+|[A-Za-z]+-?\d+(?:~[A-Za-z]?\d+)?")  # 날짜·절 번호·식별자
CITED = re.compile(r"`bazel [^`]*`|\d{4}-\d{2}-\d{2}")  # 생성 명령이나 시각의 병기 (기준의 둘째 절)
SNAPSHOT = re.compile(r"스냅샷")


















if __name__ == "__main__":
    sys.exit(main())
```
<!-- 인용 끝 -->
