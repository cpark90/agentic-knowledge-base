---
id: https://agentic-knowledge-base.dev/id/chunk/b2fcf90c-4978-456a-b281-c304ba47b7f7
type: artifact
level: executable
title_ko: 모듈 머리 agt (tools/belief_calibration.py)
title: module head agt in tools/belief_calibration.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-belief-calibration}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-11-27T05:32:11Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/53c1af98-94eb-4b8d-81cf-9914292abca6
composite: {id: https://agentic-knowledge-base.dev/id/composite/53c1af98-94eb-4b8d-81cf-9914292abca6, title_ko: 모듈 머리 복합체 agt (tools/belief_calibration.py), title: section composite agt in tools/belief_calibration.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/b2fcf90c-4978-456a-b281-c304ba47b7f7, https://agentic-knowledge-base.dev/id/chunk/e3dfa007-25f8-4aa0-9b65-c4124af23269], part_of: https://agentic-knowledge-base.dev/id/composite/589ba97d-9372-4794-b33c-9b040ecccc97}
---
**모듈 머리** — `tools/belief_calibration.py` 의 모듈 머리 `agt` 다. 모듈 머리

**정의** — `fail` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from tools import kb_lib
    from tools.chunk2kg import ID_BASE, SpecializationError, link_hash, work_id
    from tools.run_evidence import BELIEF_RULES, belief_of
except ImportError:
    import kb_lib
    from chunk2kg import ID_BASE, SpecializationError, link_hash, work_id
    from run_evidence import BELIEF_RULES, belief_of

AGT = kb_lib.AGT
LABEL_PREFIX = "label-"                  # 사람 라벨 관측 기록의 파일명 접두 — 판정 로그(judge-)·실행 기록(run-)과 한 디렉토리에서 갈린다
LABEL_COLUMNS = ("문항", "링크 IRI", "라벨", "지위")  # 라벨 표에서 읽는 열 — 그 밖의 열은 읽기 위한 열이다
INDEPENDENT = "독립"                      # 지위 열의 독립 사람 라벨 표시 (Q178-b) — '확인'·'확인(약함)'은 hci 권장 뒤 사람 확인이다
RULE_ORDER = (("kind-rank", "A"), ("beta-binomial", "B"), ("judge-mean", "C"))   # 설계 공간 후보의 순서
RULE_DECISION = {"kind-rank": "p9-belief-by-evidence-kind-rank", "beta-binomial": "p9-belief-by-beta-binomial",
                 "judge-mean": "p9-belief-by-calibrated-judge"}
SAMPLE_MIN = 20                          # 합격 기준의 표본 하한 |S| ≥ 20
BINS_UNDER = 50                          # |S| < 50 이면 구간 셋 (합격 기준 술어 2)
BINS = ((Fraction(0), Fraction(1, 3), "[0, 1/3)"), (Fraction(1, 3), Fraction(2, 3), "[1/3, 2/3)"), (Fraction(2, 3), Fraction(1), "[2/3, 1]"))
Q_LO, Q_HI = Fraction(1, 40), Fraction(39, 40)   # 95% 구간의 양쪽 분위수 2.5% · 97.5%
CALIBRATION_MIN = 20                     # C 의 보정을 적용하는 사람 라벨 표본 하한 (결정 p9-belief-by-calibrated-judge, Q186-b)
PLATT_EPS = 1e-6                         # 로짓 입력을 [ε, 1 − ε]로 자르는 폭 — 근거는 모듈 docstring 의 '보정한 C'
PLATT_MAX_ITER = 100                     # 뉴턴법 반복 상한 — 분리되지 않은 표본은 10번 안팎에 수렴한다
PLATT_TOL = 1e-10                        # 수렴 판정 — 한 걸음의 매개변수 변화량 최댓값
PLATT_HALVINGS = 30                      # 로그 우도가 줄 때 걸음을 반으로 줄이는 최대 횟수
PLATT_NAME = "C `judge-mean` (Platt 보정, LOO)"   # 판정 요약 표의 보정한 C 행 이름
_GENERATED_BY = re.compile(r"^generated:\s*\{[^}]*?\bby:\s*([^,}\s]+)", re.MULTILINE)
```
<!-- 인용 끝 -->
