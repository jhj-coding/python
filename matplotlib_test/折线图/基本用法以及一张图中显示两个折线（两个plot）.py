import matplotlib.pyplot as plt
import random
x=range(60)
#均匀分布 产生x个对应的y数据
y=[random.uniform(15,18) for i in x]

#画布
plt.figure(figsize=(20,8),dpi=100)

#x y坐标 图像 颜色 线条风格 标签
plt.plot(x,y,color='r',linestyle='-.',label="上海")
# 其中标签需要和显示图例一起使用才能展示 参数可以传图例的位置
plt.legend()
#修改xy刻度

#x 每隔5
# 准备x的刻度说明
x_label=["11点{}分".format(i) for i in x]
#两个参数 刻度 刻度说明
plt.xticks(x[::5],x_label[::5])

#0~40 每隔5
plt.yticks(range(0,40,5))

#添加网格 参数1 是否添加网格 参数2linestyle 线条风格 参数3 alpha透明度
plt.grid(True,linestyle='--',alpha=0.5)

#添加标题
#x标题
#y标题
plt.xlabel("时间变化")
plt.ylabel("温度变化")
plt.title("某城市温度时间变化")


## 两个城市 就两个图层 两个plot
y=[random.uniform(1,3) for i in x]
plt.plot(x,y,label="北京")
plt.legend()

#展示
plt.show()
