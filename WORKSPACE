load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(
    name = "aspect_rules_format",
    sha256 = "c8d04f68082c0eeac2777e15f65048ece2f17d632023bdcc511602f8c5faf177",
    strip_prefix = "bazel-super-formatter-2.0.0",
    url = "https://github.com/aspect-build/bazel-super-formatter/archive/refs/tags/v2.0.0.tar.gz",
)

load("@aspect_rules_format//format:repositories.bzl", "rules_format_dependencies")

rules_format_dependencies()

# Register Node.js toolchain for bazel-super-formatter
load("@rules_nodejs//nodejs:repositories.bzl", "DEFAULT_NODE_VERSION", "nodejs_register_toolchains")

nodejs_register_toolchains(
    name = "node",
    node_version = DEFAULT_NODE_VERSION,
)

load("@aspect_rules_format//format:dependencies.bzl", "parse_dependencies")

parse_dependencies()

# This should be done last in the WORKSPACE file to avoid getting the versions
# of things from bazel-super-formatter instead of the intended versions.
load("@aspect_rules_format//format:toolchains.bzl", "format_register_toolchains")

format_register_toolchains()
