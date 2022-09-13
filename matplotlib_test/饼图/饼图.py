import matplotlib.pyplot as plt

plt.figure(figsize=(20,8),dpi=80)


#饼图  数量 图例 颜色 显示%
plt.pie([10,20],labels=["10","20"],colors=['y','b'],autopct="%1.2f%%")
plt.legend()
plt.axis('equal')
plt.show()