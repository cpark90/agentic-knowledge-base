# FX.md — 고정물 규범 문서 (생성 파일)

- 생성기: `tools/gen_norms.py` · gendoc/1
- 입력: 원본 파일 11개 · 절 9 · 규약 줄 11 · 전체 목록은 [입력 파일](#입력-파일)
- 질의: `kb/dev/norm/fx/` 의 절 청크를 선언 순서로 펼치고 항목마다 결정의 `규약:` 줄을 싣는다
- 재현: `python3 tools/gen_norms.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 `kb/dev/norm/fx/` 의 절 청크와 결정의 `conventions.md`이다. 검사: `//:norms_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

<!-- 인용 시작: 청크에서 그대로 옮긴 값 — 원본이 자기 게이트를 통과했다 -->

고정물 문서의 도입문이다. 범례의 원본은 [고정물 결정](kb/dev/decision/fx-a/conclusion.md)이다.

## §0. 공통

이 절은 공통 규칙을 싣는다. 링크 텍스트의 코드 스팬은 링크의 일부다 — [`fx-b`](kb/dev/decision/fx-b/conclusion.md)가 그 예다.
백틱 안에 적은 링크 꼴 `[예시](../../decision/fx-b/conclusion.md)`는 링크가 아니므로 그대로 옮긴다.
줄을 넘는 코드 스팬 `한정 이름 →
uuid` 뒤의 링크 [`fx-b`](kb/dev/decision/fx-b/conclusion.md)도 출력 위치 기준으로 다시 계산된다.

- **[지킴]** **첫 문장은 굵은 강조 안에서 끝난다** ([`fx-a`](kb/dev/decision/fx-a/conclusion.md)). 둘째 문장은 [다른 결정](kb/dev/decision/fx-b/conclusion.md)을 가리킨다.
- **[권장]** 링크는 첫 문장 끝에 둔다(괄호 안의 4.5절 마침표는 문장 끝이 아니다) ([`fx-a`](kb/dev/decision/fx-a/conclusion.md)). 둘째 문장이다.
  - **[지킴]** 하위 항목에는 마침표가 없어도 링크가 끝에 붙는다 ([`fx-a`](kb/dev/decision/fx-a/conclusion.md))

### 세부

- **[지킴]** 다른 결정을 링크로 함께 가리킨다 ([`fx-a`](kb/dev/decision/fx-a/conclusion.md), [`fx-b`](kb/dev/decision/fx-b/conclusion.md)).

## 부록

이 절은 번호를 받지 않는다. 번호를 소비하지도 않으므로 다음 묶음 절이 `§1.` 을 받는다.

## §1. 묶음

이 절은 묶음 복합체를 선언한다. 묶음은 제목을 내지 않는다.

### 묶음 세부

이 절은 묶음 안의 둘째 부분이다.

## §2. 표

이 절은 링크 열을 가진 표를 싣는다. 링크 열의 칸은 생성기가 항목에서 낸다.

| 이름 | 내용 | 결정 |
|---|---|---|
| 행 하나 | 칸 안의 `a \| b` 는 한 칸이다 | [`fx-a`](kb/dev/decision/fx-a/conclusion.md) |
| 행 둘 | [다른 결정](kb/dev/decision/fx-b/conclusion.md)을 칸 안에서 가리킨다 | [`fx-a`](kb/dev/decision/fx-a/conclusion.md) · [`fx-b`](kb/dev/decision/fx-b/conclusion.md) |

이 산문은 앞 표 뒤에 온다. 다음 표는 링크 열이 없어 생성기가 표 앞에 원본 줄을 낸다.

원본: [`fx-a`](kb/dev/decision/fx-a/conclusion.md) · [`fx-b`](kb/dev/decision/fx-b/conclusion.md).

| 항목 | 뜻 |
|---|---|
| 표의 첫 행 | 링크 열이 없다 |
| 표의 둘째 행 | 주 결정은 원본 줄에 한 번만 나온다 |

### 순서

이 절은 순서 목록을 싣는다. 항목마다 `1.` 이다.

1. **[지킴]** 순서 목록의 첫 항목이다 ([`fx-a`](kb/dev/decision/fx-a/conclusion.md)).
1. **[권장]** 순서 목록의 둘째 항목이다 ([`fx-a`](kb/dev/decision/fx-a/conclusion.md)).

이 산문은 앞 순서 목록 뒤에 온다. 이어짐은 번호를 소비하지 않는다.

- **[지킴]** 이어짐 절의 항목이다 ([`fx-a`](kb/dev/decision/fx-a/conclusion.md)).

<!-- 인용 끝 -->

## 입력 파일

원본 파일 11개다. 디렉토리로 묶었고 빠진 파일은 없다.

- `kb/dev/decision/fx-a/` — `conventions.md`
- `kb/dev/norm/fx/` — `eight.md` · `five.md` · `four.md` · `head.md` · `nine.md` · `one.md` · `seven.md` · `six.md` · `three.md` · `two.md`

