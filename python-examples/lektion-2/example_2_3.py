#########################################################################################################################################
#                                                                                                                                       #
#    Autor: Dr. A. Schelle (support@krealix.de). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                       #
#########################################################################################################################################

##############################################################################################
#                                                                                            #
#   PYTHON ROUTINE zur Berechnung der Genauigkeit der Untermenge an gegeben Messwerten       #                                                         #
#                                                                                            # 
############################################################################################## 

from html.entities import entitydefs
import os
import sys
import math
import numpy
import numpy as np
import matplotlib.pyplot as plt
import csv
import random
import pandas

def accuracy(cfs, ncols): # Function which quantifies accuracy

    arcy = ardg = 0.0

    for i in range(ncols):

        ardg = ardg + cfs[i][i]

        for j in range(ncols):

            arcy = arcy + cfs[i][j]

    return float(ardg/arcy)

i = j = k = 0

num_cols = 10 # Define number of columns

cfm = [[0.0 for k in range(num_cols)] for l in range(num_cols)] # Define the data field
data = [0.0]*num_cols

index = ['Spalte 1', 'Spalte 2', 'Spalte 3', 'Spalte 4', 'Spalte 5', 'Spalte 6', 'Spalte 7', 'Spalte 8', 'Spalte 9', 'Spalte 10'] # Define the column name as a vector with n_column entries 
        
# Build preliminary float matrix

with open('/path-to-file/', 'w') as f: # Address file path and open file

    writer = csv.writer(f) # Write to CSV File
    writer.writerow(index) # Write the header of the CSV File

    for i in range(0, num_cols): # Label for data colums

        for j in range(0, num_cols): # Label for data lines

            if (i == j) : data[j] = float(random.uniform(0, 10000.0)) # Write the header of the CSV File
            if (i != j) : data[j] = float(random.uniform(0, 10.0)) # Write the header of the CSV File
       
        writer.writerow(data) # Write the data of the CSV File
 
df = pandas.read_csv('/path-to-file/') # Read data from XML file for string comparison - set the correct path with pwd

# Read and build confusion matrix

for i in range(0, num_cols):

    for j in range(0, num_cols): # Inititate exchange of data between columns 1 and 4

        cfm[i][j] = int(df[index[i]][j]) # Confusion matrix is build from the float matrix in import_file.csv

acu_1 = accuracy(cfm,num_cols) # Accuracy of confuguration 1
pf = pandas.DataFrame.filter(df, items=['Spalte 1', 'Spalte 4', 'Spalte 8']) # Confusion matrix for reduced system with only three columns

num_cols = 3 # Set the number of column to three correspondingly
new_index = ['Spalte 1', 'Spalte 4', 'Spalte 8'] # Define new index attribute values

for i in range(0, num_cols): # Iteratie over the number of columns

    for j in range(0, num_cols): # Inititate exchange of data between columns 1 and 4

        cfm[i][j] = int(pf[new_index[i]][j]) # Confusion matrix is build from the float matrix in import_file.csv

acu_2 = accuracy(cfm,num_cols) # Accuracy of configuration 2

print('Accuracy improvement : ', (acu_2-acu_1)*100.0, '%') # Calculate and print the accuracy improvement
