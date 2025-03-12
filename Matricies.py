import pandas as pd
import numpy as np
import math as math


#create 2 2x2 matrix of random integers between 1 and 30
mtx = np.random.randint(1,10,size=(2,2))
print(mtx)
#create 2 2x2 matrix of random integers between 1 and 30
mtx2 = np.random.randint(1,10,size=(2,2))
print(mtx2)


#print mtx by mtx2 using @ operator
print(mtx @ mtx2)

print(np.dot(mtx, mtx2))



