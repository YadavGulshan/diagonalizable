# pylint: disable=missing-module-docstring
# 
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/diagonalizable > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/diagonalizable/blob/master/LICENCE >
#
# All rights reserved.

import numpy as np

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


