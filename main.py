# pylint: disable=missing-module-docstring
#
# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/diagonalizable > project,
# and is released under the "MIT License".
# Please see < https://github.com/YadavGulshan/diagonalizable/blob/master/LICENCE >
#
# All rights reserved.

import numpy as np
import os

matrix = np.array(
    [
        [4,2,2],
        [2,4,2],
        [2,2,4],
    ]
)


class Diagonalizable:
    def __init__(self, matrix):
        self.matrix = matrix
        self.size = len(matrix)

    def check_diagonalizable_square(self):
        # Checking if the matrix is square
        print("Making required checks!!")
        print("please wait...")
        if all(i==self.matrix.shape[0] for i in self.matrix.shape):
            os.system('clear')
            return True
        else:
            return False

    def getEigenStuff(self):
        # First check if the matrix is square
        if self.check_diagonalizable_square():
            # Getting the eigenvalues and eigenvectors
            eigenValue, eigenVector = np.linalg.eig(self.matrix)
            return eigenValue, eigenVector
        else:
            print("The matrix is not square")
            exit()

    def check_diagonalizable(self):
        # Checking if the matrix is diagonalizable
        eigenValue, eigenVector = self.getEigenStuff()
        print("Eigen Value: ", eigenValue)
        print("Eigen Vector: \n",eigenVector)
        print(set(eigenValue), '\n')

        # Check if all the eigenvalues are unique and real
        if len(eigenValue) == len(set(eigenValue)) and np.all(np.isreal(eigenValue)):
            return "Diagonalizable"
        else:
            return "Not Diagonalizable"


diagonalizable = Diagonalizable(matrix)
print(diagonalizable.check_diagonalizable())
