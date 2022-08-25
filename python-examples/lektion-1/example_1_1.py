
#########################################################################################################################################
#                                                                                                                                       #
#    Autor: Dr. A. Schelle (support@krealix.de). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                       #
#########################################################################################################################################

# PYTHON ROUTINE zur Berechnung von Funktionswerten einer Cosinusfunktion #

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
plt.savefig('/path_to_figure/') # Save the figure to the correct path. You can find your path with the command 'pwd'.
