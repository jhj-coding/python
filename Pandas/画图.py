import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#DataFram.plot


#数据准备
random = np.random.normal(0, 1, (10, 5))
data_frame = pd.DataFrame(random)
stock=["股票{}".format(i) for i in range(10)]
frame = pd.DataFrame(random, index=stock)
data_range = pd.date_range(start="20180101", periods=5, freq="B")
# data_range=["2018-01-05","2018-01-04","2018-01-03","2018-01-02","2018-01-01"]
pd_data_frame = pd.DataFrame(random, index=stock, columns=data_range)

# x y两列 kind 图形种类 与matplotlib一样
pd_data_frame.plot(x="20180101",y="20180102",kind="scatter")
plt.show()