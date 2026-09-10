"""음성 시험 규칙 — 분석에 실패해야 하는 타깃을 영구 테스트로 남긴다 (skylib analysistest)."""

load("@bazel_skylib//lib:unittest.bzl", "analysistest", "asserts")

def _expect_failure_impl(ctx):
    env = analysistest.begin(ctx)
    asserts.expect_failure(env, ctx.attr.expected)
    return analysistest.end(env)

failure_test = analysistest.make(_expect_failure_impl, expect_failure = True, attrs = {"expected": attr.string(doc = "실패 메시지에 있어야 할 문구")})
