import os
import shutil

def copy_static(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)

    os.mkdir(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied file: {src_path} -> {dst_path}")

        elif os.path.isdir(src_path):
            print(f"Entering directory: {src_path}")
            copy_static(src_path, dst_path)

        