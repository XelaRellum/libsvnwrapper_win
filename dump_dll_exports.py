from glob import glob
import os
import subprocess


def detect_dir(dirs, suffix):
    found = list(filter(lambda dir: dir.endswith(suffix), dirs))
    assert len(found) == 1
    return found[0]


bin_dirs = glob("bin/*.*")
# print(bin_dirs)
for arch in ("win32", "x64"):
    # print(arch)
    src_dir = detect_dir(bin_dirs, suffix=arch)
    src_files = glob(os.path.join(src_dir, "lib*.dll"))
    # print(src_files)
    print("Extract exports from %s:" % src_dir)

    target_dir = os.path.join("exports", arch)
    if not os.path.isdir(target_dir):
        os.makedirs(target_dir)

    for src_file in src_files:
        filename = os.path.basename(src_file)
        print("  Extract exports from '%s'..." % filename, end="")
        filename_without_ext = os.path.splitext(filename)[0]
        dst_file = os.path.join(target_dir, filename_without_ext + ".txt")

        subprocess.run(
            ["dumpbin.exe", "/NOLOGO", "/EXPORTS", "/OUT:%s" % dst_file, src_file],
            check=True,
        )

        print("OK")
