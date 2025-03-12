import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# Create figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Vector components
x, y, z = 0, 0, 0 # Starting point of vector
u, v, w = 2, 47, 58 # Vector components
# Plot the vector
ax.quiver(x, y, z, u, v, w, color='r')
# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Vector Plot')
# Show the plot
plt.show()