import matplotlib.pyplot as plt

x=range(0,500,50);
y=range(0,500,50);

#创建画布
plt.figure(figsize=(20,8),dpi=80)
#绘制图像
plt.scatter(x,y)
#显示图像
plt.show()