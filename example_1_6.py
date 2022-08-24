####################################################################################################################
#                                                                                                                  #
#    Autor: Dr. A. Schelle. Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                  #
####################################################################################################################

import os
import sys
import math
import numpy
import numpy as np

A = [[1,2,5],[4,1,3],[3,2,1]] # Define matrix

lb, W = np.linalg.eig(A) # Calculate the eigenvalues and eigenvactors of the matrix

print('Eigenvektor 1: ', W[0], 'Eigenwert 1: ',lb[0]) # Print the first eigenvalue and eigenvactor of the matrix
print('Eigenvektor 2: ', W[1], 'Eigenwert 2: ',lb[1]) # Print the second eigenvalue and eigenvactor of the matrix
print('Eigenvektor 3: ', W[2], 'Eigenwert 3: ',lb[2]) # Print the third eigenvalue and eigenvactor of the matrix
