---
id: https://agentic-knowledge-base.dev/id/chunk/70693b1c-ddee-4cfe-84fb-7d1df3326556
type: artifact
level: executable
title_ko: 절 -owlrl-disjoint (tools/validate.py)
title: section -owlrl-disjoint in tools/validate.py
status: stable
sources: [{resource: https://agentic-knowledge-base.dev/id/src-tools-validate}]
assumes: [https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
generated: {by: process:extract, at: 2026-10-31T18:06:07Z}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/c119e011-edad-4e1c-8320-30f9527b9a13
composite: {id: https://agentic-knowledge-base.dev/id/composite/c119e011-edad-4e1c-8320-30f9527b9a13, title_ko: 절 복합체 -owlrl-disjoint (tools/validate.py), title: section composite -owlrl-disjoint in tools/validate.py, ordered: [https://agentic-knowledge-base.dev/id/chunk/70693b1c-ddee-4cfe-84fb-7d1df3326556, https://agentic-knowledge-base.dev/id/chunk/264d9fd1-b338-48ec-9eb9-9ca20577aecc, https://agentic-knowledge-base.dev/id/chunk/36e48838-e65a-47da-9e77-3a3dcef9637a, https://agentic-knowledge-base.dev/id/chunk/56b78eb7-3db4-45f8-b063-9f663a1b2afe, https://agentic-knowledge-base.dev/id/chunk/cd63cbde-c24e-46c6-892a-a26c39ddaa31, https://agentic-knowledge-base.dev/id/chunk/2e3ab692-4155-443c-bf19-1d0a95085056, https://agentic-knowledge-base.dev/id/chunk/36ed7d92-b42b-43c6-9325-c9846e77d4fb, https://agentic-knowledge-base.dev/id/chunk/07104b21-b283-4e54-a921-6b9a61fb6e45], part_of: https://agentic-knowledge-base.dev/id/composite/4d158385-e139-4042-8477-a87c3deeefe2}
---
**절** — `tools/validate.py` 의 절 `-owlrl-disjoint` 다. 논리 정합성

**정의** — `owl_rl_closure` · `_term` · `_axiom_file` · `_type_roots` · `_node_location` · `check_logical_consistency` · `check_shacl` (소스 순서).

<!-- 인용 시작: 소스 파일에서 그대로 옮긴 코드 — 생성기는 원문을 고쳐 쓰지 않는다 -->
```python
# ── 논리 정합성 ────────────────────
# 온톨로지 검사 3단계의 셋째 단계(p2-ontology-compiler-three-tiers). 추론은 OWL 2 RL 안에서만 한다(p2-owl2-rl-profile) —
# pySHACL 의 inference="both" 는 RDFS 의미론을 더한 폐포이고 그 폐포를 밖에서 볼 수 없어 모순 판정에 같은 폐포를 다시
# 계산해야 한다. 그래서 owlrl 로 OWL 2 RL 폐포를 한 번 만들고 그 폐포 하나를 모순 판정과 shape 적합성이 함께 읽는다.
_OWLRL_DISJOINT = re.compile(r"^Disjoint classes (\S+) and (\S+) have a common individual (\S+)$")
_OWLRL_NOTHING = re.compile(r"^(\S+) is defined of type 'Nothing'$")
_IRI_IN_TEXT = re.compile(r"(?:https?://|urn:)[^\s,()'\"]+")
```
<!-- 인용 끝 -->
