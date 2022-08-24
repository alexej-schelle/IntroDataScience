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

jg = 12.0*float(sl)*160.0 # Yearly income at 160 hours per month.

if (jg < 15000.0) : ghk = 'Geringverdiener'
if (jg >= 15000.0) : ghk = 'Normalverdiener'

print('Bitte geben Sie den vorgeschlagenen Stundenlohn in Euro an :')

sl_neu = input()

jg_neu = 12.0*float(sl_neu)*160.0 # Yearly income at 160 hours per month.

if (jg < 15000.0 and jg_neu < 15000) : ghk = 'Geringverdiener'
if (jg >= 15000.0 and jg_neu < 15000) : ghk = 'Geringverdiener bis Normalverdiener'
if (jg < 15000.0 and jg_neu > 15000) : ghk = 'Geringverdiener bis Normalverdiener'
if (jg >= 15000.0 and jg_neu > 15000) : ghk = 'Normalverdiener'

print (('Mit einem durchschnittlichen Jahresgehalt von'), float(jg+jg_neu)/2.0, (' Euro sind Sie : '), ghk)
