import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.normal(0, 1, (10, 5)))

df[0][1]="?"
#判断是否是NAN
pd.isnull(df)
pd.notnull(df)

#判断后的.any .all 只要一个 所有
#删除缺失值
df.dropna()
#将NaN插补
# df.fillna(填补的值)

#替换
replace = df.replace("?", np.NAN)



#数据离散化
#当标识类别时需要平衡类别 操作叫做数据离散化
# 比如 男 女
# 男 女
# 1 0
# 0 1

#如何实现数据的离散化
#分组
#自动分组
# pd.qcut(data,分几组)
#自定义分组
# pd.qcut(data,[]设置好的分组)
#将分组好的数据转换成one-hot编码
# pd.get_dummies(pd.qcut(),prefix= 前缀)


#查看每组的区间段的样本
# pd.qcut().value_counts()


#合并
# pd.concat([data1,data2],axis=)

#按索引拼接
# how inner outer left right 左右合并
#on 按什么进行合并
# pd.merge(左表，右表，how="inner"，on=[按照哪个合并字段])