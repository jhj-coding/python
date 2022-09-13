import matplotlib.pyplot as plt
import random
x=range(60)
#均匀分布 产生x个对应的y数据
y=[random.uniform(15,18) for i in x]

#画布
#参数
#几行
#几列
#宽高
#清晰度
figure,axes = plt.subplots(nrows=1,ncols=2,figsize=(20, 8),dpi=80)

#x y坐标 图像 颜色 线条风格 标签
axes[0].plot(x,y,color='r',linestyle='-.',label="上海")
# 其中标签需要和显示图例一起使用才能展示 参数可以传图例的位置
axes[0].legend()
#修改xy刻度
## 两个城市 就两个图层 两个plot
y=[random.uniform(1,3) for i in x]
axes[1].plot(x,y,label="北京")
axes[1].legend()
#x 每隔5
# 准备x的刻度说明
x_label=["11点{}分".format(i) for i in x]
#两个参数 刻度 刻度说明
axes[0].set_xticks(x[::5],x_label[::5])

#0~40 每隔5
axes[0].set_yticks(range(0,40,5))

#两个参数 刻度 刻度说明
axes[1].set_xticks(x[::5],x_label[::5])

#0~40 每隔5
axes[1].set_yticks(range(0,40,5))

#添加网格 参数1 是否添加网格 参数2linestyle 线条风格 参数3 alpha透明度
axes[0].grid(True,linestyle='--',alpha=0.5)
axes[1].grid(True,linestyle='--',alpha=0.5)

#添加标题
#x标题
#y标题
axes[0].set_xlabel("时间变化")
axes[0].set_ylabel("温度变化")
axes[0].set_title("某城市温度时间变化")
axes[1].set_xlabel("时间变化")
axes[1].set_ylabel("温度变化")
axes[1].set_title("某城市温度时间变化")



#展示
plt.show()
