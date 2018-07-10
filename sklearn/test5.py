# 朴素贝叶斯分类器

import numpy as  np
from sklearn.naive_bayes import BernoulliNB

X = np.random.randint(2,size=(6,100))
y = np.array([1,2,3,4,4,5])

clf = BernoulliNB()
clf.fit(X,y)
BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)

print(X[2:3])
print(clf.predict(X[2:3]))