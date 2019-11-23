"""
将自拍图片上下翻转，成为他拍图片
"""
import os
import cv2
import glob
import shutil
from xml.etree.ElementTree import ElementTree


def flip_pictures_tb(pic_dir, save_path):
    """
    将指定文件夹下的图片上下翻转一下
    :param pic_dir: 需要翻转的图片所在的文件夹
    :param save_path: 将翻转后的图片保存到的文件夹
    :return:
    """
    if not os.path.exists(pic_dir):
        print("The directory of %s is not exist." % pic_dir)
        exit()
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    img_list = os.listdir(pic_dir)
    for item in img_list:
        if not item.endswith(".jpg"):
            print("%s not a picture" % item)
            continue
        img_path = os.path.join(pic_dir, item)
        img_save = os.path.join(save_path, item)
        img = cv2.imread(img_path)
        img = cv2.flip(img, 0)
        cv2.imwrite(img_save, img)


def flip_pictures_lr(pic_dir, save_path):
    """
    将制定文件夹下的图片左右翻转一下
    :param pic_dir: 需要翻转的图片所在的文件夹
    :param save_path: 将翻转后的图片保存到的文件夹
    :return:
    """
    if not os.path.exists(pic_dir):
        print("The directory of %s is not exist." % pic_dir)
        exit()
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    img_list = os.listdir(pic_dir)
    for item in img_list:
        if not item.endswith(".jpg"):
            print("%s not a picture" % item)
            continue
        img_path = os.path.join(pic_dir, item)
        # img_save = os.path.join(save_path, item[:-4] + "_1" + item[-4:])
        img_save = os.path.join(save_path, item)
        img = cv2.imread(img_path)
        img = cv2.flip(img, 1)
        cv2.imwrite(img_save, img)


def flip_labels_tb(label_dir, save_dir):
    """
    将上下翻转后的图片的label信息对应的翻转
    :param label_dir: 原label文件所在的文件夹
    :param save_dir: 翻转后的label文件的保存文件夹
    :return:
    """
    assert os.path.exists(label_dir), (
        "The %s directory does not exist.")
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    label_path_list = glob.glob(os.path.join(label_dir, "*.xml"))
    # 先将xml文件复制一份，后修改相应数据
    for path in label_path_list:
        save_path = os.path.join(save_dir, os.path.basename(path))
        shutil.copy(path, save_path)

        etree = ElementTree()
        etree.parse(save_path)
        root = etree.getroot()

        size = root.find("size")
        # width = int(size.find("width").text)
        height = int(size.find("height").text)

        for obj in root.findall("object"):
            # 标签名处理
            name = obj.find("name")
            if name.text == "right_shoe_self_r":
                name.text = "left_shoe_other_r"
            elif name.text == "right_shoe_self_l":
                name.text = "left_shoe_other_l"
            elif name.text == "right_shoe_self_o":
                name.text = "left_shoe_other_o"
            elif name.text == "left_shoe_self_r":
                name.text = "right_shoe_other_r"
            elif name.text == "left_shoe_self_l":
                name.text = "right_shoe_other_l"
            elif name.text == "left_shoe_self_o":
                name.text = "right_shoe_other_o"
            elif name.text == "right_shoe_other_r":
                name.text = "left_shoe_self_r"
            elif name.text == "right_shoe_other_l":
                name.text = "left_shoe_self_l"
            elif name.text == "right_shoe_other_o":
                name.text = "left_shoe_self_o"
            elif name.text == "left_shoe_other_r":
                name.text = "right_shoe_self_r"
            elif name.text == "left_shoe_other_l":
                name.text = "right_shoe_self_l"
            elif name.text == "left_shoe_other_o":
                name.text = "right_shoe_self_o"
            else:
                print("Error label %s in file %s " % (name.text, path))
                continue

            # bbox坐标处理
            bndbox = obj.find("bndbox")
            # xmin = bndbox.find("xmin")
            ymin = bndbox.find("ymin")
            # xmax = bndbox.find("xmax")
            ymax = bndbox.find("ymax")

            yymin = str(height - int(ymax.text))
            yymax = str(height - int(ymin.text))
            ymin.text = yymin
            ymax.text = yymax
        etree.write(save_path, encoding="utf-8", xml_declaration=True)


def flip_labels_lr(label_dir, save_dir):
    """
    将左右翻转后的图片的label信息对应的翻转
    :param label_dir: 原label文件所在的文件夹
    :param save_dir: 翻转后的label文件的保存文件夹
    :return:
    """
    assert os.path.exists(label_dir), (
        "The %s directory does not exist.")
    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
    label_path_list = glob.glob(os.path.join(label_dir, "*.xml"))
    # 先将xml文件复制一份，后修改相应数据
    for path in label_path_list:
        save_path = os.path.join(save_dir, os.path.basename(path))
        shutil.copy(path, save_path)

        etree = ElementTree()
        etree.parse(save_path)
        root = etree.getroot()

        size = root.find("size")
        width = int(size.find("width").text)
        # height = int(size.find("height").text)

        for obj in root.findall("object"):
            # 标签名处理
            name = obj.find("name")
            if name.text == "right_shoe_self_r":
                name.text = "left_shoe_self_l"
            elif name.text == "right_shoe_self_l":
                name.text = "left_shoe_self_r"
            elif name.text == "right_shoe_self_o":
                name.text = "left_shoe_self_o"
            elif name.text == "left_shoe_self_r":
                name.text = "right_shoe_self_l"
            elif name.text == "left_shoe_self_l":
                name.text = "right_shoe_self_r"
            elif name.text == "left_shoe_self_o":
                name.text = "right_shoe_self_o"
            elif name.text == "right_shoe_other_r":
                name.text = "left_shoe_other_l"
            elif name.text == "right_shoe_other_l":
                name.text = "left_shoe_other_r"
            elif name.text == "right_shoe_other_o":
                name.text = "left_shoe_other_o"
            elif name.text == "left_shoe_other_r":
                name.text = "right_shoe_other_l"
            elif name.text == "left_shoe_other_l":
                name.text = "right_shoe_other_r"
            elif name.text == "left_shoe_other_o":
                name.text = "right_shoe_other_o"
            else:
                print("Error label %s in file %s " % (name.text, path))
                continue

            # bbox坐标处理
            bndbox = obj.find("bndbox")
            xmin = bndbox.find("xmin")
            # ymin = bndbox.find("ymin")
            xmax = bndbox.find("xmax")
            # ymax = bndbox.find("ymax")

            xxmin = str(width - int(xmax.text))
            xxmax = str(width - int(xmin.text))
            xmin.text = xxmin
            xmax.text = xxmax
        etree.write(save_path, encoding="utf-8", xml_declaration=True)


if __name__ == '__main__':
    flip_pictures_lr(r"C:\Users\EDZ\Desktop\img", r"C:\Users\EDZ\Desktop\img_3")
    # flip_pictures_tb(r"C:\Users\EDZ\Desktop\img", r"C:\Users\EDZ\Desktop\img_2")

    # flip_labels_tb(r"C:\Users\EDZ\Desktop\label", r"C:\Users\EDZ\Desktop\label_2")
    # flip_labels_lr(r"C:\Users\EDZ\Desktop\label", r"C:\Users\EDZ\Desktop\label_3")
