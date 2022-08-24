####################################################################################################################
#                                                                                                                  #
#    Autor: Dr. A. Schelle. Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                  #
####################################################################################################################

import os
import sys
import math

M = [[1,4,3], [2,4,4], [3,3,3]] # First Matrix M
N = [[2,4,3], [6,6,7], [2,2,1]] # Second Matrix N

def product(m, n) : # Function for matrix multiplication

    result = [[sum(a*b for a,b in zip(M_row,N_col)) for N_col in zip(*N)] for M_row in M] # Perform matrix multiplication

    return result

map_instance = list(map(product, M, N)) # Multiply two matrices in three different blocks
reduce_instance = map_instance[0] # Reduce to only first of three blocks

print(map_instance) # Show result
