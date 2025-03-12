import numpy as np 
x_axis = int(input("what is the x vector?"))
y_axis = int(input("What is the y vector?"))


def  to_unit_vector(vector):


    norm = np.sqrt(np.sum(np.array(vector)**2))

    unit_vector = np.array(vector) / norm
    
    return unit_vector

# Example usage
vector = [x_axis, y_axis]
unit_vector = to_unit_vector(vector)
print(f"Unit vector: {unit_vector}")