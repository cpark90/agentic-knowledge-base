# docs/ — 설계 문서와 소통 채널

이 디렉토리는 **그래프 밖**이다 (`DESIGN.md` A5). 검사 게이트의 어휘 폐쇄·shape
검사 대상이 아니며, 여기 있는 것은 지식이 아니라 저장소의 구조를 서술하는
문서와 소통 기록이다.

## 설계 문서가 지식이 아닌 이유

이 저장소의 지식은 청크(`chunks/`)다. 설계 문서는 청크를 **복사하지 않고
인용한다** — 결정을 서술해야 하는 자리에서는 `id:chunk-dNNNN`을 가리킨다.

| | 담는 것 | 확인 방법 |
|---|---|---|
| **설계 문서** (`docs/*.md`) | 저장소의 구조·배선·배치 | 저장소를 보면 확인된다 |
| **결정 청크** (`chunks/decision/`) | 왜 그렇게 정했는가, 무엇을 기각했는가 | 저장소를 봐도 알 수 없다 |

문서가 결정을 서술하기 시작하면 청크와 이중 관리가 되고, 둘이 어긋나는 순간
어느 쪽이 원본인지 알 수 없어진다. 이것이 노트 4.6절 "투영은 질의로서"를 산문
문서에 적용한 형태다.

## 설계 문서

**구현 설계** — 이 저장소가 체계를 어떻게 실현했는가.

| 문서 | 다루는 것 |
|---|---|
| [`DESIGN.md`](DESIGN.md) | **먼저 읽는다.** 확정 결정 A1–A5, 왜 Bazel인가, 층 구조, 세 실패 모드의 이 저장소판 |
| [`artifact-placement.md`](artifact-placement.md) | 모든 산출물이 ODD·기반·plane × level 격자 어디에 놓이는가. 빈 칸의 해석과 새 산출물의 배치 규칙 |
| [`storage-design.md`](storage-design.md) | 청크 저장 — 한 청크 한 파일, 네 그래프의 실현, frontmatter → head 생성 파이프라인, 정규화 직렬화 |
| [`gate-design.md`](gate-design.md) | 검사 게이트 — 무엇을 기계가 강제하고 무엇이 규약으로 남았는가, Bazel 배선, 게이트 추가 절차 |

**체계 운영** — 진행 상태와 미결. 결정이 아니라 **추적해야 하는 것**이라 청크가
아니다.

| 문서 | 다루는 것 |
|---|---|
| [`roadmap.md`](roadmap.md) | 도입 7단계와 현재 위치(2단계 완료), 단계별 측정 산출, 3단계 진입 조건 |
| [`risks-and-tensions.md`](risks-and-tensions.md) | 체계가 실패하는 방식과 대응, 서로 당기는 힘 사이의 균형점(정해진 것과 미정) |
| [`open-questions.md`](open-questions.md) | 체계의 미해결 26건과 구현의 미해결 9건. 둘을 구분하는 것이 요점 |
| [`references.md`](references.md) | 어느 구조를 어느 표준에서 가져왔는가, 개발 참조 프로파일 |
| [`decomposition-audit.md`](decomposition-audit.md) | 설계 노트가 어디로 갔는가 — 절별 대응과 커버리지 감사 |

## 소통 채널

[`feedback/`](feedback/README.md) — 유저 피드백 채널. hci agent가 담당하며
유저와 직접 상세 소통하는 유일한 창구다. 3-lane 구조(유저↔hci / 타 에이전트→hci /
hci→조사)와 승인 게이트(`status: approved`는 유저만)는 그 안의 `README.md`가
원본이다.

## 다른 문서와의 관계

| 문서 | 위치 | 성격 |
|---|---|---|
| `README.md` | 루트 | 저장소 소개 — 구조·명령·현재 담긴 지식·도입 단계 |
| `AGENTS.md` | 루트 | 에이전트 하네스 운영 규칙 — 역할·워크플로·황금률 |
| `STYLEGUIDE.md` | 루트 | 컴포넌트별 저작 스타일 — `[지킴]`/`[권장]` |
| `docs/*.md` | 여기 | **왜 이 구조인가**. 위 셋이 "무엇을 어떻게 하라"면 여기는 "왜 그렇게 배선했나" |

## "노트 N.N절" 인용에 대하여

청크와 문서 곳곳에 `(노트 2.3절)` 같은 인용이 있다. **노트**는
`agent-knowledge-system-notes.md` — 이 체계의 설계 원본이었던 2476줄짜리 문서다.
2026-09-01에 체계 자신의 규칙에 따라 **결정 청크와 이 디렉토리의 문서로 분해되고
제거되었다.**

절 번호는 그대로 둔다 — 그것이 **출처 기록**이기 때문이다. 어느 청크가 노트의
어느 절에서 왔는지가 남아야 분해의 충실도를 나중에 감사할 수 있다. 원본은 git
이력에 있다:

```bash
git log --all --oneline -- agent-knowledge-system-notes.md
git show ed633cc:agent-knowledge-system-notes.md
```

기계가 읽는 출처는 각 청크의 `derived_from: [.../id/doc-system-notes]`이고, 그
개체는 `kg/base-kg.ttl`에 있다 (지속 IRI — 문서가 사라져도 IRI는 유지된다).

## 참조 저장소의 설계 문서

하네스 지식은 이 체계의 사다리로 두 저장소에 나뉘어 있다.

- `../harness-functional/docs/` — 하네스의 ODD + functional(어휘). 연합 구조
  (`federation-design.md`)와 어휘 기여 절차.
- `../harness-concrete/docs/` — 하네스의 logical + concrete. 레시피 설계,
  조립 방법론, ODR BIND/VERIFY 축, 빌드 투영.

이 문서들의 **형식**(확정 결정 → 구조 → 표 → 미해결)을 여기서도 따른다. 두
저장소의 일반 방법론은 이미 청크 d-0013~d-0020으로 승격되어 있으므로, 그쪽
문서를 읽기 전에 해당 청크를 먼저 본다.
