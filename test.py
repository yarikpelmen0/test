import numpy as np

m1 = np.zeros((2,3))
m2 = np.full(6, 1).reshape(2, 3)

m = np.vstack([m1, m2])
summ = m.sum(axis=0)
print(summ)