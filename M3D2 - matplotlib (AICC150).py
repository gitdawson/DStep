import numpy as np
from scipy.spatial.distance import cosine
import matplotlib.pyplot as plt
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

mynums = np.arange(4)
mypearson = []
mycosine = []
myxaxis = []

for i in range(-50, 51):
    mybignums = mynums + i
    coef = np.corrcoef(mynums, mybignums)
    mypearson.append(coef[0,1])
    coef = cosine_similarity(mynums, mybignums)
    mycosine.append(coef)
plt.plot(mypearson, 'g*', mycosine, 'r*')
plt.xlabel("Offset")
plt.ylabel("Function Values")
plt.title("Plot of Correlation ")
plt.show()