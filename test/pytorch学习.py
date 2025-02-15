import torch
import numpy
#尺寸打印
matrix=torch.tensor([[1,2,3,4],[5,6,7,8],[1,3,5,7]])
print(matrix.shape)
print(matrix.reshape(-1),matrix.reshape(2,6))

#数据类型转化
array=matrix.numpy()
print(type(array))
matrix_2=torch.from_numpy(array)
print(type(matrix_2))
num_list=torch.tensor([1,2,3,4])
num=num_list.tolist()
print(type(num))
number=torch.tensor(1)
number=number.item()
print(type(number))

tensor1=torch.arange(1,10,step=2)
print(tensor1)
tensor2=torch.linspace(1,10,steps=5)
print(tensor2)
tensor3=torch.ones((3,3))
print(tensor3)

#生成随机数
torch.manual_seed(0)
a=torch.rand(5)
print(a)
