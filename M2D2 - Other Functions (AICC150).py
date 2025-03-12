import numpy as np

arr = np.arange(15)
arr
np.save('myfile',arr)
newarr = np.load('myfile.npy')
print(newarr)