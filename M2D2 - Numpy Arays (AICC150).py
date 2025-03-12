import numpy as np

Mylist = np.zeros((2,5)) #Python List
Nparray = np.array(Mylist)
Nparray
Nparray.dtype
print(Nparray)
print(Nparray.dtype)

arr = np.array([1,2,3,4,5])
arr.dtype
myfloat = arr.astype(np.float64)
myfloat.dtype
print(myfloat.dtype)

ar1 = np.array([1,2,3,4,5])
ar2 = np.array([6,7,8,9,0])
ar3 = ar1+ar2
print(ar2 **2)
print(ar2)
print(ar3)
