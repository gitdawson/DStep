import numpy as np
# Creating a 2D vector
vector_2d = np.array([3, 4])
# Creating a 3D vector
vector_3d = np.array([1, 2, 3])
print("2D Vector:", vector_2d)
print("3D Vector:", vector_3d)

import matplotlib.pyplot as plt
# Define vectors
vector_2d_1 = np.array([-3, 4])
vector_2d_2 = np.array([1, 2])

# Plot vectors
plt.figure()
plt.quiver(0, 0, vector_2d_1[0], vector_2d_1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 1')
plt.quiver(0, 0, vector_2d_2[0], vector_2d_2[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector 2')
# Set plot limits
plt.xlim(-3, 5)
plt.ylim(-1, 5)
# Add grid, legend, and labels
plt.grid()
plt.legend()
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('2D Vector Visualization')
# Show plot
plt.show()