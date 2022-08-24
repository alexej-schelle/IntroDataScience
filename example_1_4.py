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
import matplotlib.pyplot as plt

x = np.linspace(-10,10,100) # Define linear Linespace (linear grid)
f = np.cos(x) # Define cosinus function on grid

plt.figure(1) # Initiate plot of figure
plt.xlabel('x', fontsize = 10)
plt.ylabel('cos(x)', fontsize = 10)
plt.plot(x,f) # Plot the figure
plt.savefig('/Users/dr.a.schelle/Desktop/IUBH/DLBDSIDSD/Lektion_1/Python_Examples/fig_2.png') # Save the figure to the correct path. You can find your path with the command 'pwd'.