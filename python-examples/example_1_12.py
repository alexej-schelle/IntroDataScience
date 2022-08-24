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

n_total = 0
n_hits = 0
a = 1.0

x =[]
y = []

while 1 < 2 :

    m = random.uniform(-a,a)
    n = random.uniform(-a,a)

    n_total = n_total + 1

    if (m**2 + n**2 < a**2) : 
        
        n_hits = n_hits + 1

        x.append(m)
        y.append(n)
 
    if (math.fabs(4.0*float(n_hits)/float(n_total) - math.pi) < 1.0E-10) :
        
        print float(n_total)
        print 4.0*float(n_hits)/float(n_total)

        break

plt.figure(1) # Initiate plot of figure
plt.xlabel('x', fontsize = 10)
plt.ylabel('y', fontsize = 10)
plt.hist2d(x, y, bins = 250) # Plot the figure
plt.savefig('/Users/dr.a.schelle/Desktop/IUBH/DLBDSIDSD/Lektion_1/Python_Examples/fig_11.png') # Save the figure to the correct path. You can find your path with the command 'pwd'.

