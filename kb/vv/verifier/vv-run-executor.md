---
id: https://agentic-knowledge-base.dev/id/chunk/4ef1451d-5f8a-4360-8765-f2c24683e0cf
type: artifact
level: executable
title_ko: 케이스의 허용 목록 명령을 실행해 기대와 대조하고 pass·fail·skip 을 내는 검증기는 tools/vv_run.py 다
title: The verifier that runs each case's allow-listed commands, compares them with the expectation and yields pass, fail or skip is tools/vv_run.py
status: draft
sources: [{resource: https://agentic-knowledge-base.dev/id/doc-system-notes}]
assumes: [https://agentic-knowledge-base.dev/id/asm-bazel-toolchain, https://agentic-knowledge-base.dev/id/asm-chunk-conventions]
refines: [https://agentic-knowledge-base.dev/id/chunk/6bb376e1-0a34-4ab6-ba78-df2c0b030043, https://agentic-knowledge-base.dev/id/chunk/60b9e928-9226-4449-b92f-014597e9ff98, https://agentic-knowledge-base.dev/id/chunk/a3798247-024d-49f1-996e-159100ae3f9e, https://agentic-knowledge-base.dev/id/chunk/1b595055-a384-4309-8946-800c67dd91d6, https://agentic-knowledge-base.dev/id/chunk/5c6686a2-7697-55cc-85a9-631af3888d4c, https://agentic-knowledge-base.dev/id/chunk/fdd0b6c0-473b-47d1-b23e-b1e862416964, https://agentic-knowledge-base.dev/id/chunk/2f69c738-6a24-4c0b-9a14-29a44b25d6ee, https://agentic-knowledge-base.dev/id/chunk/a5dbd9da-c201-45bc-8019-9dbca4b89333, https://agentic-knowledge-base.dev/id/chunk/21c8bb87-da8e-5df6-8bca-0c230e6d1d86, https://agentic-knowledge-base.dev/id/chunk/d14eff56-2983-5271-a6fa-6328bd0a91a9, https://agentic-knowledge-base.dev/id/chunk/4b8db9e7-d121-515a-9dcd-6b6ca1394698, https://agentic-knowledge-base.dev/id/chunk/46ac80de-c7f6-5a67-a1f9-14e5b550dbff]
restored: [https://agentic-knowledge-base.dev/id/chunk/6bb376e1-0a34-4ab6-ba78-df2c0b030043, https://agentic-knowledge-base.dev/id/chunk/60b9e928-9226-4449-b92f-014597e9ff98]
generated: {by: vnv/claude-opus-5-5, at: 2026-10-04T23:18:48+09:00}
layer: process
part_of: https://agentic-knowledge-base.dev/id/composite/ff058e5b-5ef1-474e-b392-3948fb4f04c7
---
**검증기** — 케이스(`kb/vv/case/`)의 `**실행 명령**` 줄을 읽어 명령을 `;`·`&&` 로 나누고 케이스마다 판정을 내는 검증기는 `tools/vv_run.py` 다. 진입점은 `bazel run //tools:vv_run` 이고 보고는 저장하지 않는 생성 문서다.

**적용하는 기준** — 실행한 명령이 하나라도 기대와 어긋나면 `fail`, 명령 전부를 실행해 전부 기대와 맞으면 `pass`, 건너뛴 명령이 있거나 실행한 명령이 없으면 `skip` 이다. 기대는 종료 코드와 `contains` 의 문구 둘이고 둘 다 맞아야 맞은 것이다. 판정 어휘 셋의 정의처는 `tools/kb_lib.py` 의 `RUN_VERDICTS` 다.

**실행 범위** — 양성 허용 목록은 `bazel test`·`bazel build`·`bazel query`·`python3 tools/gen_build.py --check` 넷이고 전부 읽기 전용이다. 케이스가 `**자극**`·`**기대**` 옆에 `yaml` 펜스(`files`·`expect`)를 두면 읽기 전용 검증기를 직접 부르는 음성 명령까지 실행한다 — 자극의 임시 파일 경로는 검증기가 정하고 케이스는 `{{이름}}` 으로 가리킨다. 규약을 어긴 케이스 형식은 `FAIL [vv-case]` 로 실행 전에 멈춘다.

**재현 기록** — 명령마다 종료 코드와 소요를 적고 리비전·워킹트리 변경 여부·bazel 버전·python 버전·플랫폼을 초기 상태로 남긴다. 명령이 도는 환경은 실행기 자신의 `PYTHONSAFEPATH`·`PYTHONPATH`·`PYTHONHOME`·`RUNFILES_DIR`·`RUNFILES_MANIFEST_FILE` 를 걷어낸 것이다 (`p8-verifier-env-isolation`). 난수 seed 는 없다.

**산출** — `--record` 는 실행 기록을 `kb/vv/run/run-<UTC>.md` 에 관측으로 쓰고 이미 있는 파일을 덮지 않는다. 그 기록의 `generated.by` 는 역할이 아니라 `process:vv_run` 이라 writer 검사 밖이다.

**검증 대응물** — 없음. `verifies` 의 대상은 같은 수준의 개발 항목이어야 하는데 개발 KB 에 `executable` 수준의 항목이 하나도 없다.
