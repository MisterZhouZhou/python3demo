import numpy as np

x = np.empty([3,2], dtype=int)

x1 = np.zeros(5)

x2 = np.zeros((5,), dtype=np.int)

x3 = np.zeros((2,2), dtype =  [('x',  'i4'),  ('y',  'i4')])

x4 = np.ones(5)

# 将列表转换为array
x5 = np.asarray(x4)

x6 = np.asarray(x4, dtype=int)

print(x6)