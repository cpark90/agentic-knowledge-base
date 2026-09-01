---
iri: https://agentic-knowledge-base.dev/id/chunk-d0026
plane: decision
level: concrete
label_ko: 지식 표현의 좌표는 plane과 level 두 축
label_en: Knowledge is located by two axes, plane and level
state: valid
derived_from: [https://agentic-knowledge-base.dev/id/doc-system-notes]
generated_at: 2026-09-01T00:00:00+09:00
---
**결론** — 모든 지식 **표현**의 위치는 두 축으로 정해진다.
**plane**(지식의 종류, 한글 "평면"): `annotation`, `decision`, `schema`,
`contract`, `artifact`, `memory`. **level**(추상도, 한글 "추상화 수준"):
functional, abstract, logical, concrete, executable.
**온톨로지 자체는 축 위에 있지 않다.**

**근거** (노트 0.1절)
- 온톨로지는 두 축의 값이 되는 이름들을 정의하는 기반이므로, 자기가
  정의하는 좌표계 안에 놓일 수 없다. 축 위에 놓으면 어휘의 갱신이 어휘로
  기술된 항목의 갱신과 같은 규칙을 받게 된다.
- 두 축이 직교하므로 "무슨 종류의 지식인가"와 "얼마나 추상적인가"를 따로
  판정하고 따로 갱신할 수 있다. 축이 하나면 판정 방식(5.1절)과 전이
  규칙(6.2절)이 한 분류에 섞인다.
- 한 청크는 하나의 plane, 하나의 level만 갖는다(4.1절) — 좌표가 하나여야
  격자 위 배치가 성립한다.
