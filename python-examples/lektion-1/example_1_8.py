#########################################################################################################################################
#                                                                                                                                       #
#    Autor: Dr. A. Schelle (support@krealix.de). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                       #
#########################################################################################################################################

# PYTHON ROUTINE für die Erzeugung eines Wellenpakets aus der tanh Funktion #

import os
import sys
import math
from unittest import result
import numpy
import numpy as np
import numdifftools as nd
import matplotlib.pyplot as plt

# Importing sympy
 
from sympy import *
 
x = np.linspace(-2, 2, 100)

plt.figure(1) # Initiate plot of figure
 
for i in range(10): # Iterate the functions over i up to ten or more times
    
    df = nd.Derivative(np.tanh, n=i) # Calculate the i-fold derivative of the tanh function
    y = df(x) # Quantify the derivates at the linesspace from -2 to +2

    plt.xlabel('x', fontsize = 10)
    plt.ylabel('tanh(x)', fontsize = 10)

    h = plt.plot(x, y/np.abs(y).max()) # Plot the derivates of the tanh derivate functions
    plt.savefig('/Users/dr.a.schelle/Desktop/IUBH/DLBDSIDSD/Lektion_1/Python_Examples/fig_1.png') # Save the figure to the correct path - Note: find the correct path with terminal calll 'pwd'
