---
id: https://agentic-knowledge-base.dev/id/chunk/e2d8a9c4-074b-4ff9-89a7-92e76bd285fb
type: artifact
level: executable
title_ko: 모듈 머리 agt (tools/metrics.py)
title: module head agt in tools/metrics.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-metrics}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-09-30T08:07:48Z}
refines: [https://agentic-knowledge-base.dev/id/chunk/9cabcc42-9eb0-4b09-a429-caff7dfca72f, https://agentic-knowledge-base.dev/id/chunk/1f7d15d7-e85d-42dd-bef3-fb9c9a6d0365]
part_of: https://agentic-knowledge-base.dev/id/composite/3c529991-238b-41b3-abc4-9d4e944f0a32
---
**모듈 머리** — `tools/metrics.py` 의 모듈 머리 `agt` 다. 모듈 머리

**정의** — 없음. 선언과 상수만 있는 구역이다.

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
AGT = kb_lib.AGT  # 네임스페이스의 단일 정의처는 kb_lib (STYLEGUIDE §7)
ID = kb_lib.ID
PROV = kb_lib.PROV
DEFAULT_ASSUMPTION = ID["asm-chunk-conventions"]  # 기본 가정 (dependency-graph-design §6 "기본 가정 후 좁힘", docs/rules.md 가정 절)
LINKS = [AGT[p] for p in ("refines", "serves", "satisfies", "verifies", "cites", "targets", "assumes", "supersedes",
                          "derivesFrom", "constrains", "usesConcept", "allocates", "generates", "coUpdatesWith", "conflictsWith",
                          "overlapsWith", "usesDefinition")]  # usesDefinition 은 references 족의 잎 — 링크 개체는 없고 직접 트리플만 센다
# 후보·구축·복원의 구분은 kb_lib.link_origins 하나다 — 후보 = linkState candidate 인 링크 개체(본문 추출 cites, extract_refs),
# 구축 = 구축 기록 증거뿐인 확정 링크 개체, 복원 = 증거 종류가 구축 기록이 아닌 확정 링크 개체(restored: 표시 → proposal).
# 복원 비율 = 복원 / (확정 구축 + 복원). weave audit 이 같은 함수를 쓴다 (유저 결정 2026-09-12 (b), p10-extracted-references-are-candidates)
# plane 순서·수준 순서·수준 허용표의 단일 정의처는 `defs/kb.bzl` 이다 (M1 단일 정의처, 2026-09-26).
# --residency 로 그 파일을 읽어 채운다 — 리스트를 제자리에서 채우므로 아래 함수들의 참조가 그대로 산다.
PLANES: list[str] = []
LEVELS: list[str] = []
RESIDENCY: dict[str, list[str]] = {}
GRADES = "ABCD"  # 판정 방법 등급 (3.9절) — 연언의 등급은 최저 = 가장 뒤의 글자 (assume_check 와 같은 정의)
```
<!-- 인용 끝 -->
