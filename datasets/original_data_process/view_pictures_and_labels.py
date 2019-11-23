"""
将*.xml文件中的boundingbox画在相应的图片中，并展示图片和label
"""
import cv2
import shutil
import os
import glob
from xml.etree.ElementTree import ElementTree


def split_picture_label_file(files_path, pic_path, label_path):
    """
    将图片和标签分开到不同的文件夹里
    :param files_path: 图片和标签所在的文件夹
    :param pic_path: 存放图片的文件夹
    :param label_path: 存放label的文件夹
    :return:
    """
    assert os.path.exists(files_path), ("%s path does not exist" % files_path)
    if not os.path.exists(pic_path):
        os.mkdir(pic_path)
    if not os.path.exists(label_path):
        os.mkdir(label_path)

    pic_pathname_list = glob.glob(os.path.join(files_path, '*.jpg'))
    label_path_list = glob.glob(os.path.join(files_path, '*.xml'))
    # print(len(pic_pathname_list))
    # print(len(label_path_list))
    # assert len(pic_pathname_list) == len(label_path_list), (
    #     "The number of pictures and the number of label does not match")
    for i in range(len(pic_pathname_list)):
        shutil.move(pic_pathname_list[i], pic_path)
        shutil.move(label_path_list[i], label_path)


def read_xml(xml_path):
    """
    读取xml文件中的保存的boundingbox信息
    :param path: xml文件所在的路径
    :return: list，第一个：每个元素表示[name, xmin, ymin, xmax, ymax]，第二个：图片尺寸
    """
    ret_list = []

    tree = ElementTree()
    tree.parse(xml_path)
    root = tree.getroot()
    size = root.find("size")
    width = int(size.find("width").text)
    height = int(size.find("height").text)
    for obj in root.findall("object"):
        name = obj.find("name").text
        bndbox = obj.find("bndbox")
        xmin = int(bndbox.find("xmin").text)
        ymin = int(bndbox.find("ymin").text)
        xmax = int(bndbox.find("xmax").text)
        ymax = int(bndbox.find("ymax").text)
        ret_list.append([name, xmin, ymin, xmax, ymax])

    return ret_list, [height, width]


def view_pictures(img_dir, label_dir):
    """
    将img_path中的图片和对应的label展示
    如果图片标注不对，可以按d，将该图片另外保存，按q或esc退出展示，按任意键查看下一张图片，按w查看上一张图片
    :param img_dir: 图片所在的文件夹
    :param label_dir: label所在的文件夹
    :return:
    """
    if not os.path.exists(img_dir):
        print("The image paht %s is not exist." % img_dir)
        exit()
    if not os.path.exists(label_dir):
        print("The label path %s is not exist." % label_dir)
        exit()

    img_list = glob.glob(os.path.join(img_dir, "*.jpg"))
    num = len(img_list)
    i = 0
    while True:
        img_path = img_list[i]                                      # 图片路径
        item = os.path.basename(img_path)
        label_path = os.path.join(label_dir, item[:-3] + "xml")     # xml文件路径

        img = cv2.imread(img_path)

        label_list, size = read_xml(label_path)
        ratio = max(size[0], size[1]) / 800.0
        for label in label_list:
            top_left = (label[1], label[2])
            bottom_right = (label[3], label[4])
            cv2.rectangle(img, top_left, bottom_right, [255, 0, 0], int(ratio*2))
            cv2.putText(img, label[0], (top_left[0], top_left[1]-30), cv2.FONT_HERSHEY_SIMPLEX, ratio, (255, 0, 0), int(ratio*2))
            cv2.putText(img, item, (0, int(ratio*25)), cv2.FONT_HERSHEY_SIMPLEX, ratio, (0, 255, 255), int(ratio*2))
            print(item)
            print(label[0])

        # 将图片缩小至合适的大小，即长边缩小至800
        if ratio == 0:
            print("ratio: ", ratio)
            print("size: ", size)
        height = int(size[0] / ratio)
        width = int(size[1] / ratio)
        img = cv2.resize(img, (width, height))
        cv2.imshow("image and label", img)

        key = cv2.waitKey(0)
        if key == ord("d"):
            # 标签不合格，将其剪切到子文件夹中
            labelErrorImgsDir = os.path.join(img_dir, "labelErrorImgs")
            errorLabelFilesDir = os.path.join(label_dir, "errorLabelFiles")
            if not os.path.exists(labelErrorImgsDir):
                os.mkdir(labelErrorImgsDir)
            if not os.path.exists(errorLabelFilesDir):
                os.mkdir(errorLabelFilesDir)
            shutil.copy(img_path, labelErrorImgsDir)
            shutil.copy(label_path, errorLabelFilesDir)
            i += 1
        elif key == ord("q") or key == 27 or num-1 == i:
            # 退出展示
            break
        elif key == ord("w"):
            # 展示上一张图片
            if i != 0:
                i -= 1
            continue
        else:
            # 展示下一张图片
            i += 1
            continue
    cv2.destroyAllWindows()


if __name__ == '__main__':
    img_dir = "C:/Users/EDZ/Desktop/self_images"
    lable_dir = "C:/Users/EDZ/Desktop/self_labels"
    # split_picture_label_file(r"C:\Users\EDZ\Desktop\自拍", img_dir, lable_dir)
    view_pictures(img_dir, lable_dir)
    # read_xml(r"C:\Users\EDZ\Desktop\self_labels\665.xml")
