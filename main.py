# A program to check if a matrix is diagonalizble or not

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt

# Inputting the matrix
matrix = np.array(
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
    )

# Function to check if for each eigenvalue the dimension of the eigenspace is equal to the multiplicity of the eigenvalue.
# 
# Maths StackExchange: https://math.stackexchange.com/questions/2001505/quick-way-to-check-if-a-matrix-is-diagonalizable/2001527#:~:text=A%20matrix%20is%20diagonalizable%20if,quickly%20identify%20those%20as%20diagonizable.

