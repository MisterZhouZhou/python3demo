import numpy as np

array = np.array([1,2,4])
mulArray = np.array([[1,2],[3,4]])

# 设置最小维度
array2 = np.array([1,2,3,4,5], ndmin= 3)

# dtype参数，设置数组元素类型, complex复数
array3 = np.array([1,2,3],dtype=complex)

# 使用数组标量类型
dt = np.dtype(np.int32)
dt2 = np.dtype(np.complex)

# 调整数组的维度
array4 = np.array([[1,2,3],[4,5,6]])
array5 = np.array([[1,2,3],[4,5,6]])
array5.shape = (3,2)

array6 = np.arange(24)

array7 = np.arange(24)
array7.ndim
# x,y,z
array8 = array7.reshape(2,4,3)

# print(array)
# print('========\n',mulArray)
# print('========\n',array2)
# print('========\n',array3)
# print('========\n',dt,'====',dt2)
# print('========\n',array4.shape)
# print(array8)

