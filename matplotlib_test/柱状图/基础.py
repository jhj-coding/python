import matplotlib.pyplot as plt

x=["电影{}".format(i)for i in range(0,5)];
y=range(5,10);

#创建画布
plt.figure(figsize=(20,8),dpi=80);
#绘制柱状图
#color 数组 每个柱子的颜色
plt.bar(x,y,color=['b','r','r','b','b']);


# plt.text(x, y, s, fontsize, verticalalignment,horizontalalignment,rotation , **kwargs)
# x,y表示标签添加的位置(必选)，默认是根据坐标轴的数据来度量的，是绝对值，也就是说图中点所在位置的对应的值;
# s表示标签的符号(必选);fontsize:加标签字体大小了，取整数。
# verticalalignment表示垂直对齐方式 ，可选 ‘center’ ，‘top’ ， ‘bottom’，‘baseline’ 等
# horizontalalignment表示水平对齐方式 ，可以填 ‘center’ ， ‘right’ ，‘left’ 等

plt.text("电影0", 5 + 0.01, "%.2f" % 5, ha='center', fontsize=8)

#修改刻度
plt.xticks(x,x)

#标题
plt.title("电影")

#网格
plt.grid(True,linestyle="--",alpha=0.5)

plt.show()