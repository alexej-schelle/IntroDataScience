
#########################################################################################################################################
#                                                                                                                                       #
#    Autor: Dr. A. Schelle (support@krealix.de). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                       #
#########################################################################################################################################

########################################################################
#                                                                      # 
#   PYTHON ROUTINE zum Vertauschen zweiter Spalten in einem CSV File   #
#                                                                      # 
######################################################################## 

import os
import sys
import math
import numpy
import numpy as np
import matplotlib.pyplot as plt
import csv
import random
import pandas

i = j = k = 0

num_cols = 10 # Define number of columns
num_rows = 10 # Define number of rows

data_field = [0.0]*num_cols # Define the data field
fieldnames = ['Spalte 1', 'Spalte 2', 'Spalte 3', 'Spalte 4', 'Spalte 5', 'Spalte 6', 'Spalte 7', 'Spalte 8', 'Spalte 9', 'Spalte 10'] # Define the column name as a vector with n_column entries 
        
with open('/path-to-file/', 'w') as f: # Address file path and open file

    writer = csv.writer(f) # Write to CSV File
    writer.writerow(fieldnames) # Write the header of the CSV File

    for i in range(0, num_rows):

        for j in range(0, num_cols):

            data_field[j] = float(random.uniform(0.0, 1000.0)) # Write the header of the CSV File

        writer.writerow(data_field) # Write the data of the CSV File
        
df = pandas.read_csv('/path-to-file/') # Read data from XML file for string comparison - set the correct path with pwd
print(df) # Print and verify data from CSV File

for i in range(0, num_cols): # Inititate exchange of data between columns 1 and 4

    buffer = df['Spalte 1'][i] # Buffer data from column 1

    df['Spalte 1'][i] = df['Spalte 4'][i] # Write data from column 4 to column 1
    df['Spalte 4'][i] = buffer # Write data from buffer to column 4

print(df) # Verify the change of columns 1 and 4
