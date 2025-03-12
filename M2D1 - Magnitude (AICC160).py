import numpy as np

V= np.array([[3,3]])

v_mag = np.linalg.norm(V)

print(v_mag)

######

V_mag = np.sqrt(np.sum(V**2))

print(V_mag)

