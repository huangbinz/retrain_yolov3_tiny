import os
import cv2
from shutil import copy


count = 1


def lookpic(dir):
    global count
    files = os.listdir(dir)
    print(files)
    for item in files:
        sub_path = os.path.join(dir, item)
        if os.path.isdir(sub_path):
            lookpic(sub_path)
        elif sub_path.endswith(".jpg") or sub_path.endswith(".png") or sub_path.endswith(".jpeg"):
            # 将图片copy到指定的文件夹里，并重命名
            img_copy_path = os.path.join(img_copy_paths, str(count) + ".jpg")
            print(11111111111111111111111)
            print(sub_path)
            print(img_copy_path)
            count += 1
            copy(sub_path, img_copy_path)


if __name__ == '__main__':
    path = "./图片采集"
    img_copy_paths = "./all"

    if not os.path.exists(img_copy_paths):
        os.mkdir(img_copy_paths)

    lookpic(path)
