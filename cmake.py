import subprocess

generators = {
    "win32": "Visual Studio 14 2015",
    "x64": "Visual Studio 14 2015 Win64",
}

configs = ["Release", "Debug"]


def cmake(*args):
    subprocess.run(["cmake.exe"] + list(args), check=True)


def configure(source_dir, build_dir, bin_dir, arch):
    print("Configure:")
    cmake(
        "-G%s" % generators[arch],
        "-B%s" % build_dir,
        "-DCMAKE_INSTALL_PREFIX=%s" % bin_dir,
        "--target",
        "-Wno-dev",
        source_dir,
    )


def build(build_dir, config):
    assert config in configs
    print("Build '%s':" % config)
    cmake("--build", build_dir, "--config", config)


def install(build_dir, config):
    assert config in configs
    print("Install '%s':" % config)
    cmake("--build", build_dir, "--config", config, "--target", "install")
