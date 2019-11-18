"""
将自拍图片上下翻转，成为他拍图片
"""
import os
import cv2


def flip_pictures_tb(pic_dir, save_path):
    """
    将制定文件夹下的图片上下翻转一下
    :param pic_dir:
    :param save_path:
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


def flip_pictures_lr(pic_dir):
    """
    将制定文件夹下的图片左右翻转一下
    :param pic_dir:
    :return:
    """
    if not os.path.exists(pic_dir):
        print("The directory of %s is not exist." % pic_dir)
        exit()
    img_list = os.listdir(pic_dir)
    for item in img_list:
        if not item.endswith(".jpg"):
            print("%s not a picture" % item)
            continue
        img_path = os.path.join(pic_dir, item)
        img_save = os.path.join(pic_dir, item[:-4] + "_1" + item[-4:])
        img = cv2.imread(img_path)
        img = cv2.flip(img, 1)
        cv2.imwrite(img_save, img)


if __name__ == '__main__':
    pic_dir = "./pic"
    save_path = "./saves"

    flip_pictures_lr(pic_dir)
    flip_pictures_tb(pic_dir, save_path)
