# A program to check if a matrix is diagonalizble or not

# Importing the libraries
import numpy as np

# Maths StackExchange: https://math.stackexchange.com/questions/2001505/quick-way-to-check-if-a-matrix-is-diagonalizable/2001527#:~:text=A%20matrix%20is%20diagonalizable%20if,quickly%20identify%20those%20as%20diagonizable.

# Inputting the square matrix
# matrix = np.array(
#     [
#         [4,2],
#         [3,3]
#     ]
#     )
matrix = np.array(
    [
        [3,2,4],
        [2,0,2],
        [4,2,3]
    ]
    )


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
        print("Eigen Value: ", eigenValue)
        print("Eigen Vector: ", eigenVector)
        print(set(eigenValue),'\n')

        # Check if all the eigenvalues are unique
        if len(eigenValue) == len(set(eigenValue)):
            return "Diagonalizable"
        else:
            return "Not Diagonalizable"
        
                

diagonalizable = Diagonalizable(matrix)
print(diagonalizable.check_diagonalizable())


