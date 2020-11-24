import os
import shutil
import datetime


def copy_n_times(src_root, dst_root, n):
    for item in os.listdir(src_root):
        s = os.path.join(src_root, item)
        d = os.path.join(dst_root, item)
        if os.path.isdir(s):
            for i in range(n):
                path = item+f'-{i}'
                dst = os.path.join(dst_root, path)
                shutil.copytree(s, dst)
        else:
            shutil.copy2(s, d)


if __name__ == "__main__":
    src_root = 'Z:\Model++Project\Project\dawn\data\dongfanghong'
    dst_root = 'Z:\dfh2'
    # 复制 x 倍， n 就赋值为x
    copy_n_times(src_root, dst_root, n=5)
