import torch
tensor1=torch.tensor([[1,2],[3,4],[5,6]])
#1  2
#3  4
#5  6
tensor2=torch.tensor([[2,4],[6,8],[0,2]])
tensor3=torch.tensor([[1,3],[5,7],[9,1]])
tensor_1=torch.cat([tensor1,tensor2,tensor3],dim=0)#按行拼接，保持列不变
print(tensor_1)
tensor_2=torch.cat([tensor1,tensor2,tensor3],dim=1)
#print(tensor_2)
tensor_3=torch.split(tensor_1,[6,2,1],dim=0)
print(tensor_3)
#tensor([[1, 2],
#        [3, 4],
#        [5, 6],
#        [2, 4],
#        [6, 8],
#        [0, 2],
#        [1, 3],
#        [5, 7],
#        [9, 1]])
#tensor([[1, 2, 2, 4, 1, 3],
#        [3, 4, 6, 8, 5, 7],
#        [5, 6, 0, 2, 9, 1]])
#可以理解为矩阵的横向拼接和纵向拼接
#堆叠的用法相近没有看懂在0维上堆叠和在1维上堆叠的区别在哪里