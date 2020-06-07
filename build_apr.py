import cmake


def build_apr(arch):
    build_dir = "_build_apr_%s" % arch
    bin_dir = "bin/apr_%s" % arch
    cmake.configure(
        source_dir="apr-1.7.0", bin_dir=bin_dir, build_dir=build_dir, arch=arch,
    )

    cmake.build(build_dir, "Release")
    cmake.install(build_dir, "Release")


if __name__ == "__main__":
    build_apr("win32")
