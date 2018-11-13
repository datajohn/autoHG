import serial, time
import numpy as np
import pandas as pd

## POWER ON ##
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
inst1.write("SOUR:CURR:LIM 2.7")
time.sleep(0.5)

#DUTser =  raw_input("Enter two digit serial number: ")

# 5900 Mhz
def unescape(text, restore_backslashes=0):
        """
        Return a string with nulls removed or restored to backslashes.
        Backslash-escaped spaces are also removed.
        """
        if restore_backslashes:
                return text.replace('\x00', '\\')
        else:
                for sep in ['E+00', 'E+00\n\x00+6.0737E+00\n\x00', '\n\x00']:
                        text = ''.join(text.split(sep))
                return text

ser = serial.Serial("COM27")
ser.baudrate = 115200
ser.write('tset txfreq 5.9\n')   
ser.write('tset txvcal 0.0\n')
ser.write('rx off \n')
ser.write('flut \n')
time.sleep(0.5) 
	
results = pd.DataFrame()
steps = np.arange(27,38)	

for step in steps:						
	ser.write('tset txgain {} \n'.format(step))
	ser.write('tset \n')				
	temp = {}
	temp['TxGain']= step
	ser.write('tx on \n')
	ser.write('txpa on \n')
	time.sleep(1.5)
	a = inst1.ask("MEAS:CURR?")
	time.sleep(0.5)
	b = inst.ask("MEAS?")
	temp['Iout'] = unescape(a)
	temp['Pout'] = unescape(b)
	ser.write('txpa off \n')
	results = results.append(temp, ignore_index= True) 
	
inst.write('*CLS')
inst1.write('*CLS')
ser.close()
print results
results.to_csv('5900.csv', sep='\t') 

# 6000 Mhz
def unescape(text, restore_backslashes=0):
        """
        Return a string with nulls removed or restored to backslashes.
        Backslash-escaped spaces are also removed.
        """
        if restore_backslashes:
                return text.replace('\x00', '\\')
        else:
                for sep in ['E+00', 'E+00\n\x00+6.0737E+00\n\x00', '\n\x00']:
                        text = ''.join(text.split(sep))
                return text

ser = serial.Serial("COM27")
ser.baudrate = 115200
ser.write('tset txfreq 6.0\n')   
ser.write('tset txvcal 0.0\n')
ser.write('rx off \n')
ser.write('flut \n')
time.sleep(0.5) 
	
results = pd.DataFrame()
steps = np.arange(27,38)	

for step in steps:						
	ser.write('tset txgain {} \n'.format(step))
	ser.write('tset \n')				
	temp = {}
	temp['TxGain']= step
	ser.write('tx on \n')
	ser.write('txpa on \n')
	time.sleep(1.5)
	a = inst1.ask("MEAS:CURR?")
	time.sleep(0.5)
	b = inst.ask("MEAS?")
	temp['Iout'] = unescape(a)
	temp['Pout'] = unescape(b)
	ser.write('txpa off \n')
	results = results.append(temp, ignore_index= True) 
	
inst.write('*CLS')
inst1.write('*CLS')
ser.close()
print results
results.to_csv('6000.csv', sep='\t') 

# 6100 Mhz
def unescape(text, restore_backslashes=0):
        """
        Return a string with nulls removed or restored to backslashes.
        Backslash-escaped spaces are also removed.
        """
        if restore_backslashes:
                return text.replace('\x00', '\\')
        else:
                for sep in ['E+00', 'E+00\n\x00+6.0737E+00\n\x00', '\n\x00']:
                        text = ''.join(text.split(sep))
                return text

ser = serial.Serial("COM27")
ser.baudrate = 115200
ser.write('tset txfreq 6.1\n')    
ser.write('tset txvcal 0.0\n')
ser.write('rx off \n')
ser.write('flut \n')
time.sleep(0.5) 
	
results = pd.DataFrame()
steps = np.arange(27,38)	

for step in steps:						
	ser.write('tset txgain {} \n'.format(step))
	ser.write('tset \n')				
	temp = {}
	temp['TxGain']= step
	ser.write('tx on \n')
	ser.write('txpa on \n')
	time.sleep(1.5)
	a = inst1.ask("MEAS:CURR?")
	time.sleep(0.5)
	b = inst.ask("MEAS?")
	temp['Iout'] = unescape(a)
	temp['Pout'] = unescape(b)
	ser.write('txpa off \n')
	results = results.append(temp, ignore_index= True) 
	
inst.write('*CLS')
inst1.write('*CLS')
ser.close()
print results
results.to_csv('6100.csv', sep='\t') 

# 6200 Mhz
def unescape(text, restore_backslashes=0):
        """
        Return a string with nulls removed or restored to backslashes.
        Backslash-escaped spaces are also removed.
        """
        if restore_backslashes:
                return text.replace('\x00', '\\')
        else:
                for sep in ['E+00', 'E+00\n\x00+6.0737E+00\n\x00', '\n\x00']:
                        text = ''.join(text.split(sep))
                return text

ser = serial.Serial("COM27")
ser.baudrate = 115200
ser.write('tset txfreq 6.2\n')   
ser.write('tset txvcal 0.0\n')
ser.write('rx off \n')
ser.write('flut \n')
time.sleep(0.5) 
	
results = pd.DataFrame()
steps = np.arange(27,38)	

for step in steps:						
	ser.write('tset txgain {} \n'.format(step))
	ser.write('tset \n')				
	temp = {}
	temp['TxGain']= step
	ser.write('tx on \n')
	ser.write('txpa on \n')
	time.sleep(1.5)
	a = inst1.ask("MEAS:CURR?")
	time.sleep(0.5)
	b = inst.ask("MEAS?")
	temp['Iout'] = unescape(a)
	temp['Pout'] = unescape(b)
	ser.write('txpa off \n')
	results = results.append(temp, ignore_index= True) 
	
inst.write('*CLS')
inst1.write('*CLS')
ser.close()
print results
results.to_csv('6200.csv', sep='\t') 

#p_vs_vcal 5900 Mhz
def unescape(text, restore_backslashes=0):
        """
        Return a string with nulls removed or restored to backslashes.
        Backslash-escaped spaces are also removed.
        """
        if restore_backslashes:
                return text.replace('\x00', '\\')
        else:
                for sep in ['E+00', 'E+00\n\x00+6.0737E+00\n\x00', '\n\x00']:
                        text = ''.join(text.split(sep))
                return text

ser = serial.Serial("COM27")
ser.baudrate = 115200
inst.write('*CLS')
ser.write('tset txfreq 5.9\n') 
	
results = pd.DataFrame()
steps = np.arange(1.2, 2.1, 0.1)	

for step in steps:						
	ser.write('tset txvcal {} \n'.format(step))
	ser.write('tset \n')
	time.sleep(0.5)
	temp = {}
	temp['TxVCal']= step
	time.sleep(0.5)
	#ser.write('emit 1 -d 0 \n')  #run this for "with modualation"
	#time.sleep(0.1)
	ser.write('emit cw 1 -d 0 \n')  #run this for "cw only"
	time.sleep(0.9)
	b = inst.ask("MEAS?")
	time.sleep(0.1)
	temp['Pout'] = unescape(b)
	results = results.append(temp, ignore_index= True) 
	
ser.close()
inst.write('*CLS')
print results
results.to_csv('p_vcal_5900.csv', sep='\t')

#p_vs_vcal 6000 Mhz
def unescape(text, restore_backslashes=0):
        """
        Return a string with nulls removed or restored to backslashes.
        Backslash-escaped spaces are also removed.
        """
        if restore_backslashes:
                return text.replace('\x00', '\\')
        else:
                for sep in ['E+00', 'E+00\n\x00+6.0737E+00\n\x00', '\n\x00']:
                        text = ''.join(text.split(sep))
                return text

ser = serial.Serial("COM27")
ser.baudrate = 115200
inst.write('*CLS')
ser.write('tset txfreq 6.0\n') 
	
results = pd.DataFrame()
steps = np.arange(1.2, 2.1, 0.1)	

for step in steps:						
	ser.write('tset txvcal {} \n'.format(step))
	ser.write('tset \n')
	time.sleep(0.5)
	temp = {}
	temp['TxVCal']= step
	time.sleep(0.5)
	#ser.write('emit 1 -d 0 \n')  #run this for "with modualation"
	#time.sleep(0.1)
	ser.write('emit cw 1 -d 0 \n')  #run this for "cw only"
	time.sleep(0.9)
	b = inst.ask("MEAS?")
	time.sleep(0.1)
	temp['Pout'] = unescape(b)
	results = results.append(temp, ignore_index= True) 
	
ser.close()
inst.write('*CLS')
print results
results.to_csv('p_vcal_6000.csv', sep='\t')

#p_vs_vcal 6100 Mhz
def unescape(text, restore_backslashes=0):
        """
        Return a string with nulls removed or restored to backslashes.
        Backslash-escaped spaces are also removed.
        """
        if restore_backslashes:
                return text.replace('\x00', '\\')
        else:
                for sep in ['E+00', 'E+00\n\x00+6.0737E+00\n\x00', '\n\x00']:
                        text = ''.join(text.split(sep))
                return text

ser = serial.Serial("COM27")
ser.baudrate = 115200
inst.write('*CLS')
ser.write('tset txfreq 6.1\n') 
	
results = pd.DataFrame()
steps = np.arange(1.2, 2.1, 0.1)	

for step in steps:						
	ser.write('tset txvcal {} \n'.format(step))
	ser.write('tset \n')
	time.sleep(0.5)
	temp = {}
	temp['TxVCal']= step
	time.sleep(0.5)
	#ser.write('emit 1 -d 0 \n')  #run this for "with modualation"
	#time.sleep(0.1)
	ser.write('emit cw 1 -d 0 \n')  #run this for "cw only"
	time.sleep(0.9)
	b = inst.ask("MEAS?")
	time.sleep(0.1)
	temp['Pout'] = unescape(b)
	results = results.append(temp, ignore_index= True) 
	
ser.close()
inst.write('*CLS')
print results
results.to_csv('p_vcal_6100.csv', sep='\t')

#p_vs_vcal 6200 Mhz
def unescape(text, restore_backslashes=0):
        """
        Return a string with nulls removed or restored to backslashes.
        Backslash-escaped spaces are also removed.
        """
        if restore_backslashes:
                return text.replace('\x00', '\\')
        else:
                for sep in ['E+00', 'E+00\n\x00+6.0737E+00\n\x00', '\n\x00']:
                        text = ''.join(text.split(sep))
                return text

ser = serial.Serial("COM27")
ser.baudrate = 115200
inst.write('*CLS')
ser.write('tset txfreq 6.2\n') 
	
results = pd.DataFrame()
steps = np.arange(1.2, 2.1, 0.1)	

for step in steps:						
	ser.write('tset txvcal {} \n'.format(step))
	ser.write('tset \n')
	time.sleep(0.5)
	temp = {}
	temp['TxVCal']= step
	time.sleep(0.5)
	#ser.write('emit 1 -d 0 \n')  #run this for "with modualation"
	#time.sleep(0.1)
	ser.write('emit cw 1 -d 0 \n')  #run this for "cw only"
	time.sleep(0.9)
	b = inst.ask("MEAS?")
	time.sleep(0.1)
	temp['Pout'] = unescape(b)
	results = results.append(temp, ignore_index= True) 
	
ser.close()
inst.write('*CLS')
print results
results.to_csv('p_vcal_6200.csv', sep='\t')

## POWER OFF ##
inst1.write("SOUR:VOLT 0.0")
inst1.write("OUTP OFF")
inst.write('*CLS')
inst1.write('*RST')