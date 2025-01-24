import shutil
import os

def copy_src_to_dst(src, dst):
    if not os.path.exists(src) or not os.path.exists(dst):
        return
    shutil.rmtree(dst)
    os.mkdir(dst)
    copy_files_rec(src, dst)

def copy_files_rec(src, dst):
    content = os.listdir(src)
    if len(content) == 0:
        return
    for elem in content:
        to_copy = os.path.join(src, elem)
        if os.path.isfile(to_copy):
            shutil.copy(to_copy, dst)
            print(to_copy)
        else:
            os.mkdir(os.path.join(dst, elem))
            copy_files_rec(to_copy, os.path.join(dst, elem))

def main():
    copy_src_to_dst("./static", "./public")

main()
