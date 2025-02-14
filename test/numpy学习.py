import numpy as np
import torch
#arr=np.array([1,2,3,4,5])
arr2D=np.array([[1,2,3],[4,5,6]])
print(arr2D)
arr3D=np.array([[[1,2,3],[4,5,6]],[[1,3,5],[2,4,6]]])
print(arr3D,'\n',arr3D.ndim)
arr=np.array([[1,2,3],[4,5,6]])

print(arr[1])

print(arr.dtype)

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
new_arr=arr.reshape(4,3)
print(new_arr,new_arr.shape)

arr=np.array([1,2,3,4,5])
arr2=arr.copy()   #创建副本
arr[0]=9  #此处修改原数组
print(arr,arr2)

arr=np.array([1,2,3,4,5])
arr2=arr.view()   #创建视图
arr[0]=9  #此处修改原数组
print(arr,arr2)  
arr2[0]=99
print(arr,arr2)   
#输出:[9,2,3,4,5]  [9,2,3,4,5]

#创建三维数组
arr_3=np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=3)
print(arr_3)
arr_4=arr_3.reshape(-1)
print(arr_4)

#改变形状的对象
print('原数组:',arr_3.reshape(9).base)
print('视图',arr_3.reshape(9))

