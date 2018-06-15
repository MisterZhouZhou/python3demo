# 正弦曲线
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

#设置x,y轴的数值（y=sinx）
# linspace 生成0-10，1000个等间距的数
x = np.linspace(0, 10, 1000)
y = np.sin(x)

#创建绘图对象，figsize参数可以指定绘图对象的宽度和高度，单位为英寸，一英寸=80px
plt.figure(figsize=(8,4))

#在当前绘图对象中画图（x轴,y轴,给所绘制的曲线的名字，画线颜色，画线宽度）
plt.plot(x,y, label="$sin(x)$",color="red",linewidth=2)

# X轴的文字
plt.xlabel("Time(s)")

# Y轴的文字
plt.ylabel("Volt")

# 图表的标题
plt.title("PyPlot First Example")

# Y轴的范围
plt.ylim(-1.2, 1.2)

# 显示图示
plt.legend()

# 显示图
plt.show()

# 保存图
plt.savefig("sinx.jpg")
