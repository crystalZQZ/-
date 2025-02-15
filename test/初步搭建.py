#导入包
import torch
from torch import nn
import torch.nn.functional as F
import torchkeras
#搭建简单的神经网络
class Net(nn.Module):
    def __init__(self):
        super().__init__()#继承nn.Module的功能
        self.layer1=nn.Linear(2,4)#输入维度2，输出维度4
        self.layer2=nn.Linear(4,8)
        self.layer3=nn.Linear(8,1)
    def forward(self,x):
        x=F.relu(self.layer1(x))#对第一层内容进行激活操作
        x=F.relu(self.layer2(x))
        y=self.layer3(x)#输出不需要激活

#对自己的类进行实例化操作
net=Net()
print(net)
from torchkeras import KerasModel
from torchkeras.metrics import Accuracy
#损失函数
loss_fn=nn.BCEWithLogitsLoss()
#优化器
optimzer=torch.optim.Adam(net.parameters(),lr=0.01)
#验证精度
metrics_dict={'acc':Accuracy()}

model=KerasModel()