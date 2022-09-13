#########################################################################################################################################
#                                                                                                                                       #
#    Autor: Dr. A. Schelle (support@krealix.de). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                       #
#########################################################################################################################################

##########################################################################################################
#                                                                                                        #
#   PYTHON ROUTINE zur Berechnung der Konvergenz bei der Berechnung der Kreiszahl pi mit Zufallszahlen   #
#                                                                                                        #
##########################################################################################################

import os
import sys
import math
import random
import numpy
import numpy as np
import pylab
import matplotlib.pyplot as plt
import operator

n_total = 0 # Define Variables
n_hits = 0
n_iteration = 100000

a = 1.0
x = [] 

for i in range (n_iteration) : # Iteration over the number of realisations for the ratio 4.0*float(n_hits)/float(n_total)

    m = random.uniform(-a,a) # Set ranges for parsing with random numbers
    n = random.uniform(-a,a)

    n_total = n_total + 1

    if (m**2 + n**2 < a**2) : # Count number of occurence of values inside the area with surface pi/4.0      

        n_hits = n_hits + 1
 
    x.append(4.0*float(n_hits)/float(n_total)) # Calculate the ration of the two surface pi and unit surface


plt.figure(1) # Initiate plot of figure and plot the figure
plt.xlabel('Quotientenwert von n_hits und n_total', fontsize = 10)
plt.ylabel('Häufigkeit des Quotientenwerts', fontsize = 10)
plt.xlim([3.0, 3.4])
plt.hist(x, bins = 250) # Plot the figure
plt.savefig('/path-to-file/') # Save the figure to the correct path. You can find your path with the command 'pwd'.
