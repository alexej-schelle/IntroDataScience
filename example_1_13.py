import os
from platform import java_ver
import sys
import math
import random
import numpy
import numpy as np
import pylab
import matplotlib.pyplot as plt
import operator
from sklearn import preprocessing

A = [[ 1., -1.,  2.], [ 2.,  0.,  0.], [ 0.,  1., -1.]] # Implement matrix without normalization

print('')

print('Matrix Norm 1')

A_normalized_1 = preprocessing.normalize(A, norm='l1') # Normlize matrix A with Matrixnorm 1
print(A_normalized_1) # Print normalized matrix with Matrixnorm 1

print('')

print('Matrix Norm 2')

A_normalized_2 = preprocessing.normalize(A, norm='l2') # Normlize matrix A with Matrixnorm 1
print(A_normalized_2) # Print normalized matrix with Matrixnorm 2

print('')

print('Matrix Norm max')

A_normalized_max = preprocessing.normalize(A, norm='max') # Normlize matrix A with Matrixnorm 1
print(A_normalized_max) # Print normalized matrix with Matrixnorm max

print('')
