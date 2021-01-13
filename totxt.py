import os
import random
 
trainval_percent = 1 #train verification set to the proportion of the entire data set, modify it as needed
train_percent = 0.7 #The proportion of the training set to the training validation set, modify it as needed
xmlfilepath = '/home/fyang/workspace/PyTorch_YOLOv4/VOCdevkit/VOC2007/Annotations'
txtsavepath = '/home/fyang/workspace/PyTorch_YOLOv4/VOCdevkit/VOC2007/ImageSets/Main'
total_xml = os.listdir(xmlfilepath)
 
num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)
 
ftrainval = open(txtsavepath+'/trainval.txt', 'w')
ftest = open(txtsavepath+'/test.txt', 'w')
ftrain = open(txtsavepath+'/train.txt', 'w')
fval = open(txtsavepath+'/val.txt', 'w')
 
for i  in list:
    name=total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)
 
ftrainval.close()
ftrain.close()
fval.close()
ftest .close()