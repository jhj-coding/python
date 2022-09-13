import matplotlib.pyplot as plt

plt.figure(figsize=(20,8),dpi=80)

#参数 x 组数（最大值-最小值）/组距离  density频率
plt.hist([2,2,1,5,3],bins=2,density=True)

#修改x
plt.xticks(range(1,7,2))

plt.grid(linestyle="--",alpha=0.5)
plt.show()