import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({['A','B','C'], 'val':[10,30,20]})
ax = df.plot.bar(x='lab', y='val', rot=0)
plt.show()