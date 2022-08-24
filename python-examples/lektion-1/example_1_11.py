####################################################################################################################
#                                                                                                                  #
#    Autor: Dr. A. Schelle. Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                  #
####################################################################################################################

import os
from re import X
import sys
import math
from unittest import result
import numpy
import numpy as np
import numdifftools as nd
import matplotlib.pyplot as plt
from sympy import *
import random  
 
a = [25.0, 50.0, 75.0, 100.0, 125.0] # Define list of mean values
b = [5.0, 7.5, 10.0, 12.5, 15.0] # Define list of sigma values

M = 10000000 # Define number of iterations
L = 5 # Number of random variables with Gauß distributions

f = [] # Collecting list for final function f 

random_var = 0.0 # Sum of random variables

for l in range(M):

    random_var = 0.0 # Set random variables to zero

    print(l) # Show the number of iterations

    for k in range(L):

        random_var = random_var + random.gauss(a[k],b[k]) # Sum of Gauß random variables
    
    f.append(random_var) # Collect random variables
    
plt.figure(1) # Initiate plot of figure
plt.xlabel('$\mu=\mu_1+\mu_2+\mu_3+\mu_4+\mu_5$', fontsize = 10)
plt.ylabel('$f(\mu)$', fontsize = 10)
plt.hist(f, bins = 500) # Plot the figure
plt.savefig('/Users/dr.a.schelle/Desktop/IUBH/DLBDSIDSD/Lektion_1/Python_Examples/fig_2.png') # Save the figure to the correct path. You can find your path with the command 'pwd'.

