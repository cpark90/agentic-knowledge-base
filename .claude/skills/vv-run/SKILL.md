---
name: vv-run
description: V&V 케이스의 허용 목록 명령(읽기 전용 검증기 열 — `assume_check` 포함, `--record`·저장소 안 `--out` 은 SKIP)을 실행해 케이스의 기대(종료 코드·문구)와 대조하고 pass·fail·skip 을 판정해 실행 기록(kb/vv/run/, append-only)을 남길 때 쓴다.
---

# vv_run — V&V executor (생성 파일)

- 생성기: `tools/gen_skills.py` · gendoc/1
- 입력: 원본 파일 3개: `docs/method.md` · `tools/kb_lib.py` · `tools/vv_run.py`
- 질의: 이 도구는 무엇이고(모듈 docstring 첫 문단) 언제 쓰고(`kb_lib.SKILLS`) 어떻게 부르는가(docstring 의 `사용:` 줄)
- 재현: `python3 tools/gen_skills.py --root .`
- 생성 파일 — 손으로 고치지 않는다. 원본은 도구 docstring 과 `kb_lib.SKILLS`이다. 검사: `//:skills_drift_test`. 생성 시각·입력 지문은 없다 — 재생성 바이트 비교가 그 자리의 건전성 장치다

V&V executor — 케이스의 실행 명령 중 허용 목록의 양성 명령을 실행하고 결과를 실행 기록으로 남긴다 (노트 8.20절 executor, r-026 관측은 append-only 실행 기록, p0-run-as-observation `agt:Run`, p8-vv-plane-instances memory = 실행 기록, p8-reproducibility).

## 언제 쓰는가

V&V 케이스의 허용 목록 명령(읽기 전용 검증기 열 — `assume_check` 포함, `--record`·저장소 안 `--out` 은 SKIP)을 실행해 케이스의 기대(종료 코드·문구)와 대조하고 pass·fail·skip 을 판정해 실행 기록(kb/vv/run/, append-only)을 남길 때 쓴다.

## 명령

```bash
bazel run //tools:vv_run -- --record
bazel run //tools:vv_run -- --case <슬러그>
python3 tools/gen_build.py --root . && bazel test //...
```

## 원본

- 절차: [`docs/method.md` 11. 검증 — V&V 층으로](../../../docs/method.md#11-검증--vv-층으로)
- 도구: `tools/vv_run.py` (`bazel run //tools:vv_run`) — 사용법은 docstring 이 원본이다

```text
bazel run //tools:vv_run -- [--record] [--case <슬러그>…] [--out report.md] [--waivers docs/waivers.md]
python3 tools/vv_run.py [--record] [--case <슬러그>…] --vocab <어휘 파일>
```

## 실패 시

`FAIL [<id>]` 의 해소는 [`docs/tools.md` 게이트 총람](../../../docs/tools.md#게이트-총람--원본은-gates-리터럴이고-이-표는-그-투영이다)의 `해소` 열이다. 종료 코드는 `kb_lib` 상수다 (0 OK · 1 FAIL · 2 CONFIG · 3 SKIP). SKIP 은 PASS 가 아니다.
