####################################################################################################################
#                                                                                                                  #
#    Autor: Dr. A. Schelle. Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #
#                                                                                                                  #
####################################################################################################################

import os
import sys
import math

jg = 0.0 # Yearly income
sl = 0.0 # Hourly income

ghk = ''; # Income class

print('Bitte geben Sie den vorgeschlagenen Stundenlohn in Euro an :')

sl = input()

jg = 12.0*float(sl)*160.0 # Yearly income at average of 160 hours per month.

print (jg)

if (jg < 15000.0) : ghk = 'Geringverdiener'
if (jg >= 15000.0 and jg < 50000.0) : ghk = 'Normalverdiener'
if (jg > 50000.0) : ghk = 'Vielverdiener'

print ('Mit einem Jahresgehalt von'), jg, (' Euro sind Sie : '), ghk