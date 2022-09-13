#########################################################################################################################################
#                                                                                                                                       #
#    Autor: Dr. A. Schelle (support@krealix.de). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                       #
#########################################################################################################################################

##############################################################################################################
#                                                                                                            #
#   PYTHON ROUTINE zur Berechnung eines quantenmechanischen Wellenfeldes mit Darstellung als 2D Histogramm   #
#                                                                                                            #
##############################################################################################################

import os
import sys
import math
import random
import numpy
import numpy as np
import pylab
import matplotlib.pyplot as plt
import operator

maxmode = 250 # Typical mode size for analysis : 500 - 2500 modes.
ptn = 1000 # Typical particle number : 10^3 - 10^5
sample = 10000 # Typical sample size : 10^5 - 10^8

omx = 2.0*math.pi*42.0 # Trap frequency in x direction
omy = 2.0*math.pi*42.0 # Trap frequency in y direction 
omz = 2.0*math.pi*120.0 # Trap frequency in z direction

start_temp = 2.5 # in units of nK

rhbkb = 7.63822291E-3 # in units of nK

norm = 0.0
int_norm = 0
drop = 0
prob = 0.0
phase_0 = 0.0
z_start = start_temp
mu_start = 0.0
mu_k = 0.0

print ('Trap depth [nK]: '), maxmode*omz*rhbkb # around few muK
print ('Critical temperature [nK]: '), rhbkb*pow(ptn,1.0/3.0)*pow(omx*omy*omz,1.0/3.0)/pow(1.202,1.0/3.0) # around 1.15 mK

en_x = ['']*maxmode
en_y = ['']*maxmode
en_z = ['']*maxmode

pols_x = ['']*maxmode
pols_y = ['']*maxmode
pols_z = ['']*maxmode

pols = ['']*maxmode

x = ['']*ptn
y = ['']*ptn

mu_x = [] # collect the real part of the integrated wave field
mu_y = [] # collect the imaginary part of the integrated wave field

for l in range(1, sample):
          
    drop = 1
    z = random.uniform(1, ptn) # Random sample of non-condensate particle number
    temp = start_temp

    mu = 0.0
    norm = 0.0
    
    print(('Sample step Nr. '), str(l))
                  
    for k in range(1, maxmode):
        
        en_x[k] = rhbkb*k*omx/temp # Energy in x direction
        en_y[k] = rhbkb*k*omy/temp # Energy in y direction
        en_z[k] = rhbkb*k*omz/temp # Energy in z direction
     
        pols_x[k] = 1.0/(1.0-math.exp(-en_x[k])) # Complex poles in x direction
        pols_y[k] = 1.0/(1.0-math.exp(-en_y[k])) # Complex poles in y direction
        pols_z[k] = 1.0/(1.0-math.exp(-en_z[k])) # Complex poles in z direction
                    
    for k in range(1, maxmode):
    
        pols[k-1] = pols_x[maxmode-k]*pols_y[maxmode-k]*pols_z[maxmode-k]-1.0 # General poles
    
    pols[maxmode-1] = -(ptn-z_start)

    prob = complex(0.0,0.0)
    p = ['']*maxmode
    phase_0 = 0.0
   
    x = numpy.roots(pols) # Complex roots of the number conserving equation

    for k in range(0,len(x)):

        p[k] = random.uniform(0.0,1.0)   # Random amplitudes - set p[k] = delta(k-k_random) for single BEC spectrum
        norm = norm + p[k]*p[k]*(x[k].real**2+x[k].imag**2) # Total norm
        
    norm = math.sqrt(norm)
    
    for k in range(0,len(x)): # Calculate phase of the condensate wave field
        	
        p[k] = p[k]/norm # Random amplitudes
    	
        if (operator.gt(x[k].real**2 + x[k].imag**2,0.0)):
                
            if (operator.gt(x[k].real,0.0)):
            
                phase_0 = math.atan(x[k].imag/x[k].real)
        
            if (operator.iand(operator.lt(x[k].real,0.0),operator.ge(x[k].imag,0.0))):
            
                phase_0 = math.atan(x[k].imag/x[k].real) + math.pi
    
            if (operator.iand(operator.lt(x[k].real,0.0),operator.lt(x[k].imag,0.0))):
	            
                phase_0 = math.atan(x[k].imag/x[k].real) - math.pi
    
            if (operator.iand(operator.eq(x[k].real,0.0),operator.gt(x[k].imag,0.0))):
            
                phase_0 = 0.5*math.pi

            if (operator.iand(operator.eq(x[k].real,0.0),operator.lt(x[k].imag,0.0))):
            
                phase_0 = -0.5*math.pi
        	       
            mu += x[k]*p[k] # Random amplitudes times phases
            mu_k = x[k]*p[k] # Condensate field modes
        
            if operator.ne(phase_0,0.0):
    	
                prob += complex(0.5*p[k]*p[k]*math.log(math.fabs(x[k].real**2 + x[k].imag**2)), p[k]*p[k]*phase_0) # Calculate transition probability
    	
            prob = math.sqrt(prob.real**2 + prob.imag**2) 
    	
    if (operator.gt(min((math.exp(prob))/(math.exp(mu_start)),1.00),random.uniform(0.00,1.00))): # Condition for transition to another state at equilibrium
 
        mu_start = prob
        z_start = z
        drop = 0
	    
    if (operator.ne(drop,1)):	
		
        mu_x.append(1.0*mu.real) # Collect non-condensate field modes in x direction
        mu_y.append(1.0*mu.imag) # Collect non-condensate field modes in y direction

        mu_x.append(-1.0*mu.real) # Collect condensate field modes in x direction
        mu_y.append(1.0*mu.imag) # Collect condensate field modes in y direction

        if (operator.gt(mu.real,0.0)): # First quarter plane
            
            phase_0 = math.atan(mu.imag/mu.real) + math.pi
        			
        if (operator.iand(operator.lt(mu.real,0.0),operator.ge(mu.imag,0.0))): # Second quarter plane
            
    	    phase_0 = math.atan(mu.imag/mu.real) + math.pi + math.pi
    
        if (operator.iand(operator.lt(mu.real,0.0),operator.lt(mu.imag,0.0))): # Third quarter plane
	            
            phase_0 = math.atan(mu.imag/mu.real) - math.pi + math.pi
    
        if (operator.iand(operator.eq(mu.real,0.0),operator.gt(mu.imag,0.0))): # Fourth quarter plane
            
            phase_0 = 0.5*math.pi + math.pi

        if (operator.iand(operator.eq(mu.real,0.0),operator.lt(mu.imag,0.0))): # Fifth quartr plane
            
            phase_0 = -0.5*math.pi + math.pi
    	    	        

plt.figure(1)
plt.hist(mu_x, bins = 250)
plt.tick_params(axis='both', which='major', labelsize = 16)
plt.xlabel('$Re(\Psi_0)$', fontsize = 18)
plt.ylabel('$\pi[Re(\Psi_0)]$', fontsize = 18)
plt.savefig('/path-to-file/fig_re.png')

plt.figure(2)
plt.hist(mu_y, bins = 250)
plt.tick_params(axis='both', which='major', labelsize = 16)
plt.xlabel('$Im(\Psi_0)$', fontsize = 18)
plt.ylabel('$\pi[Im(\Psi_0)]$', fontsize = 18)
plt.savefig('/path-to-file/fig_im.png')
