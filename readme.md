### 1、下载

```
git clone https://github.com/pjreddie/darknet
cd darknet
# 若需使用GPU，则先修改Makefile文件中的第一行为GPU=1,后make
make
```



### 2、准备数据集

1）将图片数据集放在datasets/shoeDatas/JPEGImages文件夹中，将相应的标注xml文件放在datasets/shoeDatas/Annotations文件夹中;

2）修改datasets/voc_lable.py文件，在datasets/shoeDatas/中生成labels文件夹和train.txt文件

​	labels文件夹中每个文件代表相应图片的物体的类别标签、框的坐标位置和宽高（label, x, y, w, h）;

​	train.txt中存放的为每张训练图片的绝对路径



### 3、修改配置文件

1）修改cfg/yolov3-tiny.cfg文件：

​		修改3、4和6、7行，切换测试和训练模式;

​		修改177和135行的classes数为自己的类别数;

​		修改127和171行filters为 3*(5 + classes), classes为上一行的类别数

2）修改data/shoe.names文件：

​		一行为一个类别的名称，需与labels文件夹中文件的label标签序号对应好

3）修改cfg/shoe.data文件：

​		classes为分类类别数;

​		train：为datasets中生成的train.txt的路径;

​		valid：为datasets中生成的valid.txt的路径;

​		names：为data文件夹下的shoe.names文件路径;

​		backup：为训练时模型文件的保存路径

4）可选操作：选择训练多少次后保存一次模型：

​		修改examples/detector.c文件的第138行，修改完后，需要终端运行 gcc detector.c 编译，然后在darknet目录中make。



### 4、训练

1）从官网（https://pjreddie.com/darknet/yolo/）下载权重文件yolov3-tiny.weights

2）通过下载好的权重文件，得到yolov3-tiny的预训练模型：

```
./darknet partial ./cfg/yolov3-tiny.cfg ./yolov3-tiny.weights ./yolov3-tiny.conv.15 15
```

3）训练模型：

```
./darknet detector train cfg/shoe.data cfg/yolov3-tiny.cfg yolov3-tiny.conv.15
```

4）多GPU训练：

```python
./darknet detector train cfg/shoe.data cfg/yolov3-tiny.cfg yolov3-tiny.conv.15 -gpus 0,1,2,3
```



### 5、测试

```
./darknet detector test cfg/shoe.data cfg/yolov3-tiny.cfg yolov3-tiny.weights data/dog.jpg
```





