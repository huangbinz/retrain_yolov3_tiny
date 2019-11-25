import xml.etree.ElementTree as ET
import os


# classes = ["right_shoe", "left_shoe"]
classes = ["right_shoe_self_l", "right_shoe_self_r", "right_shoe_self_o", "right_shoe_other_l", "right_shoe_other_r", "right_shoe_other_o", \
			"left_shoe_self_l", "letf_shoe_self_r", "left_shoe_self_o", "left_shoe_other_l", "left_shoe_other_r", "left_shoe_other_o"]



def convert(size, box):
    dw = 1.0/(size[0])
    dh = 1.0/(size[1])
    x = (box[0] + box[1])/2.0 - 1
    y = (box[2] + box[3])/2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


def convert_annotation(file_name):
    wd = os.getcwd()
    # if not os.path.exists("shoeDatas/lables"):
    #     os.makedirs("shoeDatas/labels")
    train_file = open("shoeDatas_2/train.txt", "a")       # 如果是训练集，则改为test.txt
    train_file.write("%s/shoeDatas_2/JPEGImages/%s.jpg\n" % (wd, file_name))
    train_file.close()

    in_file = open('shoeDatas_2/Annotations/%s.xml' % file_name)
    out_file = open('shoeDatas_2/labels/%s.txt' % file_name, 'w')
    tree = ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


path = "./shoeDatas/Annotations/"
file_names = os.listdir(path)
for file_name in file_names:
    convert_annotation(file_name.split(".")[0])
    # print(file_name.split(".")[0])

