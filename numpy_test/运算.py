import numpy as np
normal = np.random.normal(0, 1.0, size=(8, 10))
#逻辑判断
#所有大于0.5 为True 小于为false
normal > 0.5
#所有大于0.5的都等于1.1
normal[normal>0.5]

#通用判断函数

#参数传进去布尔值 只要有一个False就返回False 否则True
np.all(normal>0.5)

#参数传进去布尔值 只要有一个True就返回True 否则False
np.any(normal>0.5)

# 三元运算符
#参数 布尔值，True的值，False的值
where = np.where(normal > 0.5, 1, 0)

#或 与
#与
#满足返回True 不满足返回False
logical_and = np.logical_and(normal > 0.5, normal < 1.2)
#或
#满足返回True 不满足返回False
logical_or = np.logical_or(normal > 0.5, normal < 0.3)


#最大值
#不传参数 代表所有的元素的最大值
#传 axis=1 标识每一行的最大值 0标识每一列的最大值
normal.max()
#最小值
#不传参数 代表所有的元素的最大值
#传 axis=1 标识每一行的最大值 0标识每一列的最大值
normal.min()

#最小值
#不传参数 代表所有的元素的最大值
#传 axis=1 标识每一行的最大值 0标识每一列的最大值
normal.min()
#平均值
normal.mean()
#中位数
np.median(normal)
#标准差
normal.var()
#方差
normal.std()
#如果想找到其位置在方法前加上arg即可
normal[:4,:4].argmax(axis=1)


#数组间的运算
array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#每个数都加减乘除 某个数字
array+1


array1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#数组的运算 数组与数组的运算需要满足广播机制
#维度相等 shape（其中一个对应的位置为1） （2，5）（2，5）
array+array1
array*array1

#矩阵运算
#矩阵乘法 M*N N*l=>m*l 第一行每个元素与第一列每个元素相乘相加为第一个元素
#如果是二维数组进行运算
np_array = np.array([
    [80, 86],
    [90, 100]])
np_array1 = np.array([
    [0.7],
    [0.3]])
#叉乘
matmul = np.matmul(np_array, np_array1)
#点乘
dot = np.dot(np_array, np_array1)
#@符号
array_ = np_array @ np_array1
#如果是矩阵
mat = np.mat([[80, 86], [90, 100]])
mat1 =np.mat([[0.7],[0.3]])
mat_ = mat * mat1


##合并
# 横着拼接
hstack = np.hstack((np_array, np_array1))
#竖着拼接
vstack = np.vstack((np_array, np_array))
#可以横着可以竖着
concatenate = np.concatenate((np_array, np_array1), axis=1)


## 分割

#从0~9 每隔2
x=np.arange(0,9,2)
#按照索引进行分割 第2 3位置分割
np.split(x, [1,2])
