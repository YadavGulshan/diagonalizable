# A program to check if a matrix is diagonalizble or not

# Importing the libraries
from traceback import print_tb
import numpy as np

# Maths StackExchange: https://math.stackexchange.com/questions/2001505/quick-way-to-check-if-a-matrix-is-diagonalizable/2001527#:~:text=A%20matrix%20is%20diagonalizable%20if,quickly%20identify%20those%20as%20diagonizable.

# Inputting the square matrix
matrix = np.array([[1,2],[3,1]])


class Diagonalizable:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)

    def check_diagonalizable_square(self):
        # Checking if the matrix is square
        if self.matrix.shape[0] == self.matrix.shape[1]:
            return True
        else:
            return False

    def getEigenStuff(self):
        # First check if the matrix is square
        if self.check_diagonalizable_square():
            # Getting the eigenvalues and eigenvectors
            eigenValue , eigenVector = np.linalg.eig(self.matrix)
            return eigenValue, eigenVector
        else:
            print("The matrix is not square")
            exit()
    
    def check_diagonalizable(self):
        # Checking if the matrix is diagonalizable
        eigenValue, eigenVector = self.getEigenStuff()

        print("Eigenvalues: ", eigenValue)
        print("Eigenvectors: ", eigenVector)

diagonalizable = Diagonalizable(matrix)
print(diagonalizable.check_diagonalizable())


