import numpy as np
import  pandas as pd

#数据准备
random = np.random.normal(0, 1, (10, 5))
data_frame = pd.DataFrame(random)
stock=["股票{}".format(i) for i in range(10)]
frame = pd.DataFrame(random, index=stock)
data_range = pd.date_range(start="20180101", periods=5, freq="B")
# data_range=["2018-01-05","2018-01-04","2018-01-03","2018-01-02","2018-01-01"]
pd_data_frame = pd.DataFrame(random, index=stock, columns=data_range)




#删除一些列
drop = pd_data_frame.drop(["2018-01-01"], axis=1)
#删除一些行
drop = pd_data_frame.drop(["股票0","股票1"], axis=0)


##索引操作 （获取某个元素）
#直接索引 先列索引后行索引
pd_data_frame["2018-01-01"]["股票0"]
#按名字索引 先行索引后列索引
pd_data_frame.loc["股票0"]["2018-01-01"]
#按数字索引 先行后列
pd_data_frame.iloc[0,1]
#选择第n行 选择第二行
pd_data_frame.iloc[1, :]
#选择第n列 选择第二列
pd_data_frame.iloc[:, 1]
#选择第二行 1~3元素
pd_data_frame.iloc[1, 1:3]




## 赋值
# 某一列直接赋值 列名
pd_data_frame["2018-01-01"]=1
# 利用索引找到然后进行赋值
# pd_data_frame["2018-01-01"]["股票0"]=2



##排序
#对内容进行排序
#参数by 列名 参数ascending True升序 False降序
#如果是多个 就用[] 先看2018-01-02 再看2018-01-03
values = pd_data_frame.sort_values(by=["2018-01-02","2018-01-03"], ascending=False)

#对索引进行排序
#参数ascending True升序 False降序 axis 1行 0列
#如果是多个 就用[] 先看2018-01-02 再看2018-01-03
values = pd_data_frame.sort_index(axis=0,ascending=False)



##运算
#算术运算 + - * / 或者 add(+) sub()-
values.iloc[0,:].add(1)
#逻辑运算和nump一样 每个元素都和其比较 True False

#灵活运用筛选出此列大于0的信息
values[values["2018-01-02"]>0]
#与
values[(values["2018-01-02"]>0) & (values["2018-01-03"]<0.5)]

t = values.T
#逻辑运算函数
# 筛选
t.query("股票0 > 0 & 股票1 <0.5")
#判断是否为某个值 股票0这一列是否是1 或者0
isin = t['股票0'].isin([1, 0])
t[isin]

#统计运算
# 计算最大值 最小值 方差 与numpy相同
# 计数 count  5.000000  5.000000  5.000000  ...  5.000000  5.000000  5.000000
# 平均值 mean  -0.107413  0.215273  0.790414  ...  0.207015  0.291973 -0.712056
# 标准差 std    1.097290  0.997688  0.966712  ...  1.104062  0.426518  1.429809
# 最小 min   -1.456493 -0.900594 -0.107953  ... -0.911197 -0.108231 -2.680100
# 分位数
# 25%   -0.768860 -0.848893  0.151340  ... -0.499933  0.041162 -1.491704
# 50%   -0.335736  0.827254  0.560719  ... -0.267888  0.234543 -0.532588
# 75%    1.000000  0.998599  1.000000  ...  1.000000  0.292391  0.144111
# 最大 max    1.024027  1.000000  2.347966  ...  1.714091  1.000000  1.000000
t.describe()

#累加
t["股票0"].cumsum()

#自定义运算
#apply 参数1 函数 参数 2 axis
#示例 每一列最大值减去最小值
apply = t.apply(lambda x: x.max() - x.min())
print(apply)