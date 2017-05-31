#SANYO HIP-230HD1
#Pmp = 230
#Voc = 34.3
#Isc = 6.71
#All of them at 25 celcius degrees at 1000 W/m^2 of irradiance

from __future__ import division
from datetime import datetime
import Plot

def variables(TFC,EI,ET):
	NOCT = 47 
	TC = ET+(1000/800)*(NOCT-20) #Calculating temperatures EI must be rewrite
	Porc = abs(((TFC-TC)/TFC)*100)
	DT = TC - 25
	Pmp = 230+DT*-0.3
	Voc = 34.3+DT*-0.106
	Isc = 6.71+DT*0.00217
	print 'TC is: ',TC,'TFC is: ',TFC
	print 'Error porcentage is: ',Porc
	print 'Power Supplied is: ',Pmp
	print 'Voltage Supplied is: ',Voc
	print 'Current Supplied is: ',Isc
	
	name = 'Real_Values.txt'
	f = open(name,'a')
	f.write('{0:0.3f}'.format(TFC))
	f.write(' ')
	f.write('{0:0.3f}'.format(Porc))
	f.write(' ')
	f.write('{0:0.3f}'.format(Pmp))
	f.write(' ')
	f.write('{0:0.3f}'.format(Voc)) 
	f.write(' ')
	f.write('{0:0.3f}'.format(Isc))
	f.write(' ')
	f.write(str(datetime.now())) 
	f.write('\n')
	f.close()
	
	now = datetime.now()
	today8am = now.replace(hour=16, minute=0, second=0, microsecond=0)
	if (now < today8am):
		print "YES!!!"
	else:
		print "NO!!!"
	Plot.plotting("Real_Values.txt")
