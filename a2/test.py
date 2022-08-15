import numpy as np

m = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
m1=m[0]
t=np.array([[1,2,3]])
print(m)
print(m1)
print(m.shape)
print(m1.shape)
print(t.shape)
print(m1+t)
print(m1.T)
print(m1.T.shape)

a=[1,2,3,4,5]
print(a[1::])
print(a[1:-1])
