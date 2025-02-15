import torch.nn as nn


class simplecnn(nn.Module):
    #定义CNN作为特征提取
    def __init__(self,num_class):#num_class是我们的分类数
        super().init_()
        #定义特征提取
        self.features=nn.Sequential(
            nn.Conv2d(3,16,kernel_size=3,stride=1,padding=1),#输入通道数，输出通道数，卷积核，步长,填充层数为1——让输出图像的尺寸不变
            #32张，彩色图3，像素数224*224
            nn.ReLU(),#卷积之后接上激活函数，增加非线性特征
            nn.MaxPool2d(kernel_size=2,stride=2),#大小减半——从步长可以看出，池化层   16*112*112
            nn.Conv2d(16,32,kernel_size=3,stride=3,padding=1),#保持图像大小不变 32*112*112
            nn.MaxPool2d(kernel_size=2,stride=2)#图像大小：32*56*56
        )
    #定义全连接层，作分类
        self.classifier=nn.Sequential(
            nn.Linear(32*56*56,128),#把三维数据转化为一维数据
            nn.ReLU(),
            nn.Linear(128,num_class)##num_class为分类数
        )
    #定义前向传播
    def forward(self,x):
        #前向传播部分
        x=self.features(x)   #特征提取
        x.view(x.size(0),-1)

