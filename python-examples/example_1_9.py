####################################################################################################################
#                                                                                                                  #
#    Autor: Dr. A. Schelle. Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                  #
####################################################################################################################

import os
import sys
import math
from unittest import result
import numpy
import numpy as np
import numdifftools as nd
import matplotlib.pyplot as plt

#Importing sympy
 
from sympy import *
 
x = np.linspace(-2, 2, 100)

maximum = []
minimum = []

df = nd.Derivative(np.tanh, n=6) # Calculate the i-fold derivative of the tanh function
y = df(x) # Quantify the derivates at the linesspace from -2 to +2
    
plt.xlabel('x', fontsize = 10)
plt.ylabel('tanh(x)', fontsize = 10)

h = plt.plot(x, y/np.abs(y).max()) # Plot the derivates of the tanh derivate functions
plt.savefig('/Users/dr.a.schelle/Desktop/IUBH/DLBDSIDSD/Lektion_1/Python_Examples/fig_1.png') # Save the figure to the correct path - Note: find the correct path with terminal call 'pwd'

for k in range(len(y)-1):

    if (y[k]/np.abs(y).max() < 0.0 and y[k+1]/np.abs(y).max() > 0.0) : # Zero's of the positive derivates define the maxima of the integrated function.
            
        maximum.append(x[k]) # Append all maxima

    if (y[k]/np.abs(y).max() > 0.0 and y[k+1]/np.abs(y).max() < 0.0) : # Zero's of the negative derivates define the maxima of the integrated function.
            
        minimum.append(x[k]) # Append all minima

        # Plot the derivates of the tanh derivate functions

print (maximum, minimum) # Print all maxima and minima

