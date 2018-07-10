import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.linear_model import LinearRegression

# sklearn 提供了一些很有用的数据集生成器
# 生成数据集，并将其绘制出来

diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data[:,np.newaxis,2]
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train) #这里就是在训练模型了

print('Coefficients: \n', regr.coef_) #这就是w0，常数项
print("Residual sum of squares: %.2f" % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2)) #这个是预测与真实的差
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test)) #这里就是得分，1为拟合最好，0最差

plt.scatter(diabetes_X_test, diabetes_y_test, color = 'black')
plt.plot(diabetes_X_test,regr.predict(diabetes_X_test), color='blue',linewidth=3)
plt.xticks(())
plt.yticks(())

plt.show()