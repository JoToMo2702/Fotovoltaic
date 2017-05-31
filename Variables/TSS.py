#Read Temperature, Humidity and Irradiation
# ADS1115.py is a program use to read A0 for irradiation and
# for the humidity and temperature of the SHT31-D and 
# Author: Josue Torres M.
# License: Public Domain


import logging
import time
import Calc
import Adafruit_ADS1x15
from Adafruit_SHT31 import *

adc = Adafruit_ADS1x15.ADS1115()
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

Pyra = range(0,20)
Irr = range(0,20)
Vin = range(0,20)
V2 = range(0,20)
D = range(0,20)
H = range(0,20)

def executeprogram():
	for q in range(0,20):
		
		#Read ADC Values
		
		w = adc.read_adc(0, gain=2/3) #Pyranometer
		x = adc.read_adc(1, gain=16) #Irradiance Cell
		y = adc.read_adc(2, gain=2/3) #ViN
		z = adc.read_adc(3, gain=2/3) #V2
		
		Pyra[q]=w
		Irr[q]=x
		Vin[q]=y
		V2[q]=z
		
		#Read SHT31-D
		
		degrees = sensor.read_temperature()
		humidity = sensor.read_humidity()
		
		D[q]=degrees
		H[q]=humidity
		
		if (q==19):
			P = 0
			I = 0
			V = 0
			VV = 0
			Deg = 0
			Hum = 0
			for m in range(0,19):
				P=P+Pyra[m]
				I=I+Irr[m]
				V=V+Vin[m]
				VV=VV+V2[m]
				Deg=Deg+D[m]
				Hum=Hum+H[m]
				#print Hum
			
			Calc.calc(P,I,V,VV,Deg,Hum)
		
		
while True:
	executeprogram()		
	time.sleep(60)
