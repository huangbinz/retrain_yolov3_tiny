"""处理 yuantu_train 的数据"""
import os
from shutil import copy


img_dir = "./datasets/yuantu_train/p"
xml_dir = "./datasets/yuantu_train/a"
img_save_dir = "./datasets/shoeDatas/JPEGImages"
xml_save_dir = "./datasets/shoeDatas/Annotations"
count = 1

print("Start processing...")

paths = os.listdir(img_dir)
for path in paths:
    # 初始路劲
    img_path = os.path.join(img_dir, path)
    xml_path = os.path.join(xml_dir, path[:-3] + "xml")
    # 需复制到的路径
    img_save_path = os.path.join(img_save_dir, str(count) + ".jpg")
    xml_save_path = os.path.join(xml_save_dir, str(count) + ".xml")

    # 复制文件
    copy(img_path, img_save_path)
    copy(xml_path, xml_save_path)

    count += 1

print("end of processing.")
