#Plot data
#Fix different length of numbers!!!

import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def plotting(name_file):
	fo = open(name_file, "rw+")
	print "Name of the file: ", fo.name

	num_lines = sum(1 for line in open('Real_Values.txt'))
		
	T = range(num_lines)
	Porc = range(num_lines)
	P = range(num_lines)
	Time = range(num_lines)
	Voc = range(num_lines)
	Isc = range(num_lines)
	x = range(num_lines)
	now = datetime.now()
	i = 0
	b = 0
	p = 0
	s = ''
	
		
	for line in fo:
			x[i] = line
			i = i +1			
	fo.close() 
	for n in range(num_lines):
		for c in range(len(x[n])):
			 s = s+x[n][c]
			 p = p+1
			 if ((x[n][c] == ' ')and b == 0):
				 #T[n] = float(s)
				 s = ''
				 b = b+1
			 elif ((x[n][c] == ' ')and b == 1):
				 #Porc[n] = float(s)
				 s = ''
				 b = b+1
			 elif ((x[n][c] == ' ')and b == 2):
				 P[n] = float(s)
				 s = ''
				 b = b+1
			 elif ((x[n][c] == ' ')and b == 3):
				 Voc[n] = float(s)
				 s = ''
				 b = b+1
			 elif ((x[n][c] == ' ')and b == 4):
				 Isc[n] = float(s)
				 s = ''
				 b = b+1
			 elif ((x[n][c] == ' ')and b == 5):
				 #Time[n] = float(s)
				 s = ''
				 b = b+1
			 elif (p > (len(x[n])-2)  and b == 6):
				 Time[n] = float(s[0]+s[1]+s[3]+s[4])
				 s = ''
				 b = b+1
			 if c == (len(x[n])-1):
				 b = 0
				 p = 0
				 s = ''
		#P[n] = float(x[n][15:20])
		#Time[n] = float((x[n][47:49])+(x[n][50:52]))
		#Voc[n] = float(x[n][23:29])
		#Isc[n] = float(x[n][30:35])
	#print P
	#print Time
	#print Voc
	#print Isc
	
	plt.subplot(311)
	plt.plot(Time,P,'ro')
	plt.ylabel('Power [W]')
	plt.axis([0, 2000, 0, 300])
	
	plt.subplot(312)
	plt.plot(Time,Voc,'bo')
	plt.ylabel('Voltage [V]')
	plt.axis([0, 2000, 0, 40])
	
	plt.subplot(313)
	plt.plot(Time,Isc,'go')
	plt.ylabel('Current [A]')
	plt.xlabel('Time (Military Hour)')
	plt.axis([0, 2000, 0, 10])
	
	plt.savefig('Cell_Behavior_'+str(now.year)+'_'+str(now.month)+'_'+str(now.day)+'.png')
	plt.show()
	
plotting("Real_Values.txt")


