# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:21:49 2017

@author: hgLaptop
"""

#POWER AND INITIALIZE EQ.

# POWER OFF
inst1.write("SOUR:VOLT 0.0")
inst1.write("OUTP OFF")
inst.write('*CLS')
inst1.write('*RST')

# POWER ON
# HP E4418A = inst
# KEITHLEY = inst1
import serial, time
from wanglib import prologix
plx = prologix.prologix_USB('COM25')
inst = plx.instrument(13)
#inst.write("OC0") #contols the cal pwr ref
inst1 = plx.instrument(16)
inst1.write("SOUR:VOLT 3.701")
inst1.write("OUTP ON")
inst1.write("SOUR:CURR:LIM 2.5")



