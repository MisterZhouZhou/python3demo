'''
  利用matplotlib绘制简单的坐标图
'''
import matplotlib.pyplot as plt

# 绘制折线图
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]
# 给plot同时提供输入值和输出值
plt.plot(input_values, squares, linewidth=5)

# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小，将刻度标记的字号设置为14
plt.tick_params(axis='both', labelsize=14)

plt.show()