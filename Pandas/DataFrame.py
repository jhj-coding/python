import numpy as np
import  pandas as pd
random = np.random.normal(0, 1, (10, 5))

#DataFrame
#结构 既有行索引又有列索引的二维数组
# index 行 columns列
data_frame = pd.DataFrame(random)
#添加行索引
stock=["股票{}".format(i) for i in range(10)]
frame = pd.DataFrame(random, index=stock)
#添加列索引
#生成日期 从哪开始 几天  频率
data_range = pd.date_range(start="20180101", periods=5, freq="B")
pd_data_frame = pd.DataFrame(random, index=stock, columns=data_range)


##属性
#形状
shape = pd_data_frame.shape
#行索引
index = pd_data_frame.index
#列索引
columns = pd_data_frame.columns
#值
values = pd_data_frame.values
#转置
t = pd_data_frame.T
#前n行 前两行
head = pd_data_frame.head(2)
#后n行 后两行
tail = pd_data_frame.tail(2)
#选择第n行 选择第二行
pd_data_frame.iloc[1, :]


##修改索引
# 不能单独修改某一个索引值
data_range = pd.date_range(start="20180102", periods=5, freq="B")
pd_data_frame.columns=data_range
#重设索引
#drop 参数 默认是false 如果是false则会多一列index 会自动生成默认大的索引
#true代表删除原来的索引
pd_data_frame.reset_index()

##设置索引 用map的方式
df=pd.DataFrame({
    'month':[1,2,3],
    'year':[2,3,5],
    'day':[5,6,7]
})
#将月份设置为索引
set_index = df.set_index("month", drop=True)
#设置多个索引
#将年月都设置为索引
set_index = df.set_index(["month","year"], drop=True)

#获取索引结果 类型为MultiIndex
set_index.index


#MuleiIndex
# names:levels的名称
# levels:每个level的元组值
set_index.index.names
set_index.index.levels


#Series 带索引的一维数字 只有行索引
#两个属性 index(行索引) values（值）
frame_ = pd_data_frame.iloc[1, :]
#创建
series = pd.Series(np.arange(3, 9, 2), index=[1, 2, 3])
#使用字典创建
pd_series = pd.Series({'a': 1, 'b': 2, 'c': 3})
print( pd_series)

