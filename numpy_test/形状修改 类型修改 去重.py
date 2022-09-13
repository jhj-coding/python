import numpy as np
import matplotlib.pyplot as plt

#size 几行几列
normal = np.random.normal(0, 1.0, size=(8, 10))

# 获取第三天的数据
normal[0,0:3]

array = np.array([[[1, 2, 3], [3, 4, 5]], [[12, 13,14], [22, 23, 25]]])
#找到5
array[0,1,2]
#找到[4,5]
array[0, 1, [1, 2]]

#查看形状 几行几列
normal.shape

#形状修改 只是将数据重新划分 没有行列互换 返回新的ndarray 原始数据没有改
normal.reshape([10,8])
#形状修改 没有返回值 对原始的ndarray进行修改 没有行列互换
normal.resize([10,8])
#形状修改 没有返回值 对原始的ndarray进行修改 行列互换 转置
normal.T


#将数组内的所有数据按照类型转换
normal.astype("int32")
#序列化
normal.tobytes()

#数组去重
np_array = np.array([[1, 2, 3,4], [3, 4, 5, 6]])
np.unique(np_array)

#转换为1维数组 set只能处理一维形式
np_array.flatten()



