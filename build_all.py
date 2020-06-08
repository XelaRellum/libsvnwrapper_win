import cmake


def build_library(source_dir, arch):
    print("Build %s:" % source_dir)
    build_dir = "_build_%s_%s" % (source_dir, arch)
    bin_dir = "bin/%s" % arch
    cmake.configure(
        source_dir=source_dir, bin_dir=bin_dir, build_dir=build_dir, arch=arch,
    )

    cmake.build(build_dir, "Release")
    cmake.install(build_dir, "Release")


def build_apr_util(arch):
    print("Build APR-UTIL:")
    build_dir = "_build_apr-util-1.6.1_%s" % arch
    bin_dir = "bin/%s" % arch
    cmake.configure(
        source_dir="apr-util-1.6.1", bin_dir=bin_dir, build_dir=build_dir, arch=arch,
    )

    cmake.build(build_dir, "Release")
    cmake.install(build_dir, "Release")


if __name__ == "__main__":
    build_library("apr-1.7.0", "win32")
    build_library("expat-2.2.9", "win32")
    build_library("apr-util-1.6.1", "win32")
    build_library("zlib-1.2.11", "win32")
