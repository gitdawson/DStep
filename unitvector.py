# Import required libraries
import numpy as np
import pandas as pd

'''Remember that the array may be row or column based, so you will need to handle both cases.'''
def norm(myarray):
    # Initialize sum variable to store squared values
    sum = 0
    # Get array dimensions
    myshape = myarray.shape
    
    # Handle Row Vector case
    if(len(myshape)==1):
        for i in range(0,myshape[0]):
            sum = sum + myarray[i]**2
    # Handle Column Vector case        
    else:
        for i in range(0,myshape[0]):
            for j in range(0,myshape[1]):
                sum = sum + myarray[i][j]**2
    
    # Return Euclidean norm (square root of sum of squares)
    return np.sqrt(sum)

# Create test array
tarray = np.array([1,2,3])
vnorm = norm(tarray)
if(vnorm == 0):
    print("A Zero vector? Seriously?")
else:
    uvector = tarray/vnorm
    print("Unit vector is: ", uvector)