import numpy as np

arrayyy = np.array(([1,2,3,4,5],[6,7,8,9,10]))

# Use np.copy() or .copy() for deep copying
arrayyy2 = np.transpose(arrayyy).copy()

print(arrayyy2)
print(np.shape(arrayyy2))

