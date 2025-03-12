import numpy as np
import matplotlib.pyplot as plt
# Define the 2D vector

#user input for vector 

#ask user for color of vector 



v = np.array([[3, 4]])
# Create a plot
plt.figure()
# Use quiver to plot the vector
#String Codes: 'r' (red), 'g' (green), 'b' (blue), 'k' (black), 'c' (cyan),
#'m' (magenta), 'y' (yellow), 'w' (white)
plt.quiver(0, 0, v[0,0], v[0,1], angles='xy', scale_units='xy', scale=1, color='b')
# Set the limits of the plot to make the vector visible
plt.xlim(-5, 5)
plt.ylim(-5, 5)
# Add grid and axis labels for clarity
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
# Set the aspect ratio of the plot to be equal
plt.gca().set_aspect('equal', adjustable='box')
# Show the plot
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Get user input for x and y limits
x_min = float(input("Enter minimum x value: "))
x_max = float(input("Enter maximum x value: "))
y_min = float(input("Enter minimum y value: "))
y_max = float(input("Enter maximum y value: "))

# Define the 2D vector
v = np.array([[3, 4]])

# Create a plot
plt.figure()
# Use quiver to plot the vector
plt.quiver(0, 0, v[0,0], v[0,1], angles='xy', scale_units='xy', scale=1, color='b')

# Set the user-defined limits of the plot
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

# Add grid and axis labels for clarity
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)

# Set the aspect ratio of the plot to be equal
plt.gca().set_aspect('equal', adjustable='box')

# Show the plot
plt.show()
