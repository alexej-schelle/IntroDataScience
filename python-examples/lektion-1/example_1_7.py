#########################################################################################################################################
#                                                                                                                                       #
#    Autor: Dr. A. Schelle (support@krealix.de). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                       #
#########################################################################################################################################

# PYTHON ROUTINE für die Berechnung von Ableitungen einer Funktion #

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
 
x = Symbol('x') # Create a "symbol" called x
 
f = x**2 # Define function
 
derivative_f = f.diff(x) # Calculating the derivative
print('The formal derivate is defined as : ', derivative_f) # Show the form of the derivate

f_prime = lambdify(x,f) # Make derivate of f valuable
print('The value of the formal derivative at x = 4 is : ', f_prime(4)) # Calculate the derivative at x = 4
