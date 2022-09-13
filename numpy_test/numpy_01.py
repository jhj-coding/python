import numpy as np

import matplotlib.pyplot as plt
#生成数组方法

#生成0 几行几列 3行5列 dtype指定类型
# [[0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]
#   [0. 0. 0. 0. 0.]]
zero=np.zeros((3,5))
print(zero)

#生成1 几行几列 3行5列 dtype指定类型
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]
one=np.ones((3,5))
print(one)

#从现有数组中生成
# [[1 1]
#  [0 0]]
#深拷贝
print(np.array([[1, 1], [0, 0]]))
#深拷贝
print(np.asarray([[1, 1], [0, 0]]))
#浅拷贝
print(np.copy([[1, 1], [0, 0]]))

#生成固定范围的数据

#生成 0-10 闭区间 5个元素 等距离
# [ 0.   2.5  5.   7.5 10. ]
print(np.linspace(0,10,5));
#生成 0-10 左闭右开 5是步长 每隔5生成一个数
# [0 5]
print(np.arange(0,10,5));


#随机生成均匀分布
#均匀分布 标识每一组的可能性是相等的
#0.0,1.0之间生成1000000个
#[0.91724985 0.25917706 0.24047901 0.74772049 0.16574878]
uniform = np.random.uniform(0.0, 1.0, 1000000)
print(uniform);
plt.figure(figsize=(20,8),dpi=80)
plt.hist(uniform,1000)
plt.show()