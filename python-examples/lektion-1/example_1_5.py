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
import pandas
import pandas as pd
from IPython.display import display

dt = {'Student':["Student 1", "Student 2", "Student 3"], 'Fachrichtung' : ["Fachrichtung Student 1", "Fachrichtung Student 2", "Fachrichtung Student 3"], 
'Geburtsdatum':["Geburtsdatum Student 1", "Geburtsdatum Student 2", "Geburtsdatum Student 3"]} # Definition of input array

dt_pandas = pd.DataFrame(dt) # Create Pandas Data Framework (Pandas Table)

display(dt_pandas) # Show Pandas Table
