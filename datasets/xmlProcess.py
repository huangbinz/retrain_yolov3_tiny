"""
将图片统一缩放到长边为500,短边等比缩放
"""

import cv2
from xml.etree.ElementTree import ElementTree


xml_path = "10.xml"
img_path = "10.jpg"

tree = ElementTree()
tree.parse(xml_path)
root = tree.getroot()

# 获取原始大小
size = root.find("size")
ori_width = int(size.find("width").text)
ori_height = int(size.find("height").text)

max_data = max(ori_width, ori_height)
ratio = 500.0/max_data    # 将最大边缩放到500

# 图像resize后的尺寸
img_width = int(ori_width*ratio)
img_height = int(ori_height*ratio)
print(ratio, img_width, img_height)

# 更改xml文件中的尺寸值
size.find("width").text = str(img_width)
size.find("height").text = str(img_height)

for obj in root.findall("object"):
    bndbox = obj.find("bndbox")
    xmin = bndbox.find("xmin")
    ymin = bndbox.find("ymin")
    xmax = bndbox.find("xmax")
    ymax = bndbox.find("ymax")

    xxmin = str(int(int(xmin.text)*ratio))
    yymin = str(int(int(ymin.text)*ratio))
    xxmax = str(int(int(xmax.text)*ratio))
    yymax = str(int(int(ymax.text)*ratio))

    xmin.text = xxmin
    ymin.text = yymin
    xmax.text = xxmax
    ymax.text = yymax

tree.write(xml_path, encoding="utf-8", xml_declaration=True)

# resize图像大小
img = cv2.imread(img_path)
img = cv2.resize(img, (img_height, img_width))
cv2.imwrite(img_path, img)
