#导包
import matplotlib.pyplot as plt
#创建画布
#有两个参数 figsize图像大小 图的长宽 dpi清晰度
# plt.figure()
plt.figure(figsize=(20,8),dpi=80)
#画图  （横坐标数据+纵坐标数据）
plt.plot([1,0,9],[4,5,6])

#将图保存到某个文件下 要先保存再展示
plt.savefig("G://1.png");

#展示 当执行完显示图像之后保存图片将只能保存空图片
plt.show()