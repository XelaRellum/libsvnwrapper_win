import cmake
from glob import glob
import re


def build_library(source_dir, arch):
    print("Build %s:" % source_dir)
    build_dir = "_build_%s_%s" % (source_dir, arch)
    bin_dir = "bin/%s" % arch
    cmake.configure(
        source_dir=source_dir, bin_dir=bin_dir, build_dir=build_dir, arch=arch,
    )

    cmake.build(build_dir, "Release")
    cmake.install(build_dir, "Release")


def detect_library(prefix):
    dirs = glob(prefix + "-*")
    r = re.compile(r"-[0-9.]+$")
    for dir in dirs:
        if r.search(dir):
            return dir

    assert False, "Library with prefix '%s' not found!" % prefix


if __name__ == "__main__":
    for platform in ["win32"]:
        for library_prefix in ["apr", "expat", "apr-util", "zlib"]:
            library = detect_library(library_prefix)

            build_library(library, platform)
