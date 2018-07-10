import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

# 构造一个hilbert矩阵10*10
X = 1. / (np.arange(1,11)+np.arange(0,10)[:,np.newaxis])
# 10个1
y = np.ones(10)
# 学习效率
n_alphas = 200
#等比数列，200个，作为岭回归的系数
alphas = np.logspace(-10,-2,n_alphas)
clf = linear_model.Ridge(fit_intercept=False)
coefs = []
for a in alphas:
	clf.set_params(alpha=a)
	clf.fit(X,y)
	coefs.append(clf.coef_) #得到200个不同系数所训练出常数参数值

ax = plt.gca()
ax.set_color_cycle(['b', 'r', 'g', 'c', 'k', 'y', 'm'])
ax.plot(alphas,coefs)
ax.set_xscale('log') #转为极坐标系
ax.set_xlim(ax.get_xlim()[::-1]) #反转x轴
plt.xlabel('alpha')
plt.ylabel('weight')
plt.title('Ridge coefficients as a function of the regularization')
plt.axis('tight')
plt.show()