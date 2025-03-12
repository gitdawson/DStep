import numpy as np

arr1 = np.zeros((3,5))

print(np.shape(arr1))
print(np.transpose(arr1))

np.save('LAB1FILE',arr1)
arr2 = np.load('myfile.npy')

np.random.randint(1, 101, size=10)
print(arr1)
print(arr2)

