# 생성 파일 — 손으로 고치지 않는다. 원본은 project-ontology.ttl 의 owl:imports (tools/gen_build.py). 검사: //:build_drift_test
"""project-ontology.ttl 이 가져오는 모듈 — owl:imports 에서 생성."""

PROJECT_IMPORTS = [
    "//kb/ontology/entity/knowledge-item",
    "//kb/ontology/related/assumption",
    "//kb/ontology/related/channel",
    "//kb/ontology/related/condition",
    "//kb/ontology/related/harness",
    "//kb/ontology/related/scope",
    "//kb/ontology/related/state",
    "//kb/ontology/related/tag",
    "//kb/ontology/related/trace",
    "//kb/ontology/related/trust",
]
