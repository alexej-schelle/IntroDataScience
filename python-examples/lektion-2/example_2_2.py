#########################################################################################################################################
#                                                                                                                                       #
#    Autor: Dr. A. Schelle (support@krealix.de). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                                       #
#########################################################################################################################################

####################################################################################
#                                                                                  # 
#   PYTHON ROUTINE zum Auslesen bestimmter Variablen aus einem XML Metadatenfile   #
#                                                                                  # 
#################################################################################### 

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

f = open("/path-to-file/metadata.xml", "r") # Read data from XML file for string comparison - set the correct path with pwd

entity_id = 'entityID' # Define variable entityID
key_size = 'KeySize' # Define variable KeyDescriptor     
key_info = 'KeyInfo' # Define variable KeyInfo      

with f : # Read lines separately in f as defined above

    for line in f : # Iterate over lines of the xml file

        if entity_id in line : # Check for variable entityID
        
            entity_id = line

        if key_size in line : # Check for variable KeyDescriptor
        
            key_size = line

        if key_info in line : # Check for variable EncryptionMethod
        
            key_info = line

print('EntityID :', entity_id) # Print information line containing variable entityID 
print('KeySize :', key_size) # Print information line containing variable KeyDescriptor 
print('KeyInfo :', key_info) # Print information line containing variable EncryptionMethod

