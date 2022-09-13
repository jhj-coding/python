import matplotlib.pyplot as plt

x=range(0,5);
y=range(5,10);

#创建画布
plt.figure(figsize=(20,8),dpi=80);
#绘制柱状图
#color 数组 每个柱子的颜色
#width 柱子宽度
#两个柱子作比较 x要变化以下
plt.bar(x,y,color=['b','r','r','b','b'],width=0.1);

plt.bar([0.1,1.1,2.1,3.1,4.1],[1,2,3,4,5],color=['b','r','r','b','y'],width=0.1);



#网格
plt.grid(True,linestyle="--",alpha=0.5)

plt.show()