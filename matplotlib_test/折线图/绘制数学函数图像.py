import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1,1,1000);
y=2*x*x*x;

#创建画布
plt.figure(figsize=(20,8),dpi=80)
#绘制图像
plt.plot(x,y)
#网格
plt.grid(True,linestyle="--",alpha=0.5)
#显示图像
plt.show()