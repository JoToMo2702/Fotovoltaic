import os
import Proba

def read_file(txt):
	fo = open(txt, "rw+")
	print "Name of the file: ", fo.name

	x = range(10)   #Lines
	ET = range(10)  #Enviroment Temperature
	H = range(10)   #Humidity
	TFC = range(10) #Temperatuce Fotovoltaic Cell
	EI = range(10)  #Enviroment Irradiance
	IFC = range(10) #Irradiance Fotovoltaic Cell
	CFC = range(10) #Current Fotovoltaic Cell
	VFC = range(10) #Voltage Fotovoltaic Cell

	i = 0
	w = 0
	e = 0
	r = 0
	t = 0

	for line in fo:
			x[i] = line
			#print x[i]
			i = i +1
	fo.close()       

	for n in range(0,10):
		ET[n] = float(x[n][0:6])
		H[n] = float(x[n][7:13])
		TFC[n] = float(x[n][14:20])
		EI[n] = float(x[n][21:27])
		IFC[n] = float(x[n][28:34])

	for q in range(0,10):
		i = i+ET[q]
		w = w+H[q]
		e = e+TFC[q]
		r = r+EI[q]
		t = t+IFC[q]

	os.remove('Variables.txt')
	
	i = i/10
	w = w/10
	e = e/10
	r = r/10
	t = t/10
		
	print i
	print w
	print e
	print r
	print t
	
	Proba.variables(e,r,i)
# Close opend file

