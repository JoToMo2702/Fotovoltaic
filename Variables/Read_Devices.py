# ADS1115.py is a program uste to read A0 and A1 inputs and 
# a differential between A2 and A3, but also the humidity and
# temperature of the SHT31-D
# Author: Josue Torres M.
# License: Public Domain

import logging
import time
import Adafruit_ADS1x15
import Read_txt
from Adafruit_SHT31 import *
from math import exp, expm1
from datetime import datetime

sensor = SHT31(address = 0x44)

def print_status():
    status = sensor.read_status()
    is_data_crc_error = sensor.is_data_crc_error()
    is_command_error = sensor.is_command_error()
    is_reset_detected = sensor.is_reset_detected()
    is_tracking_temperature_alert = sensor.is_tracking_temperature_alert()
    is_tracking_humidity_alert = sensor.is_tracking_humidity_alert()
    is_heater_active = sensor.is_heater_active()
    is_alert_pending = sensor.is_alert_pending()
    print 'Status           = {:04X}'.format(status)
    print '  Data CRC Error = {}'.format(is_data_crc_error)
    print '  Command Error  = {}'.format(is_command_error)
    print '  Reset Detected = {}'.format(is_reset_detected)
    print '  Tracking Temp  = {}'.format(is_tracking_temperature_alert)
    print '  Tracking RH    = {}'.format(is_tracking_humidity_alert)
    print '  Heater Active  = {}'.format(is_heater_active)
    print '  Alert Pending  = {}'.format(is_alert_pending)

# Pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V -----> 187.5 uV per bit
#  -   1 = +/-4.096V -----> 125 uV per bit
#  -   2 = +/-2.048V -----> 62.5 uV per bit
#  -   4 = +/-1.024V -----> 31.25 uV per bit
#  -   8 = +/-0.512V -----> 15.625 uV per bit
#  -  16 = +/-0.256V -----> 7.8125 uV per bit

def executeprogram():
	for q in range(0,10):
		
		adc = Adafruit_ADS1x15.ADS1115()
		#print 'Reading ADS1115 values'

		w = adc.read_adc(0, gain=2/3) #Pyranometer
		x = adc.read_adc(1, gain=2/3) #Irradiance Cell
		y = adc.read_adc(2, gain=2/3) #Dont know
		z = adc.read_adc(3, gain=2/3) #Cell Temperature

		RT = (z*(0.0001875)*(1000))/(x*(0.0001875)-z*(0.0001875))
		#RT = (z*(0.0001875)/((y*(0.0001875)-z*(0.0001875))/1000))+3
		TP = ((RT/1000)-1)/0.00392

		adc = Adafruit_ADS1x15.ADS1115(address=0x49,busnum=1)
		f = adc.read_adc(3, gain=2/3)

		# Note you can change the differential value to the following:
		#  - 0 = Channel 0 minus channel 1
		#  - 1 = Channel 0 minus channel 3
		#  - 2 = Channel 1 minus channel 3
		#  - 3 = Channel 2 minus channel 3

		#z = adc.read_adc_difference(3, gain=2/3)

		#Reading Humidity and Degrees values

		degrees = sensor.read_temperature()
		humidity = sensor.read_humidity()

		print 'A0 is: ',w,' and A1 is: ',x,'A2 is: ',y,' and A3 is: ',z
		#print 'The difference btween A0 and A1 is: ',z
		#print 'The value of humidity is: {0:0.3f}'.format(humidity)
		#print 'The value of temperature is: {0:0.3f}'.format(degrees)
		#print 'A3 of the second ADC is: ',f
		print TP
		print RT
		name = 'Variables.txt'
		f = open(name,'a')
		f.write('{0:0.3f}'.format(degrees))
		f.write(' ')
		f.write('{0:0.3f}'.format(humidity))
		f.write(' ')
		f.write('{0:0.3f}'.format(TP))
		f.write(' ')
		f.write('{0:0.3f}'.format(TP)) #Pyranometer
		f.write(' ')
		f.write('{0:0.3f}'.format(TP)) #Irradiance Cell
		f.write('\n')
		f.close()
		
		#time.sleep(0.01)
		
	Read_txt.read_file(name)

	

executeprogram()

