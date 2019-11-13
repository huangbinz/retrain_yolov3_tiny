"""处理 已标注61组数据文件 的数据"""
import os
from shutil import copy


base_path = "./datasets/已标注61组数据文件/已标注61组数据文件/"
img_save_path = "./datasets/shoeDatas/JPEGImages"
xml_save_path = "./datasets/shoeDatas/Annotations"
count = 1

print("Start processing...")

first_dirs = os.listdir(base_path)
for path1 in first_dirs:
    second_path = os.path.join(base_path, path1)
    # print(second_path)
    second_dirs = os.listdir(second_path)
    # print(second_dirs)
    for path2 in second_dirs:
        third_path = os.path.join(second_path, path2)
        # print(third_path)
        third_dirs = os.listdir(third_path)
        # print(third_dirs)
        for path3 in third_dirs:
            if path3.endswith(".jpg") or path3.endswith(".JPG"):
                img_path = os.path.join(third_path, path3)      # 待复制的图片路径
                xml_path = os.path.join(third_path, path3[:-4]+".xml")      # 待复制的xml文件路径
                copy(img_path, os.path.join(img_save_path, str(count)+".jpg"))
                copy(xml_path, os.path.join(xml_save_path, str(count)+".xml"))
                count += 1

print("end of processing.")
