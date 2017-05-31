#Calculating values

from __future__ import division
from datetime import datetime

def calc(w,x,y,z,degrees,humidity):
		
		w=w/20
		x=x/20
		y=y/20
		z=z/20
		degrees=degrees/20
		humidity=humidity/20
		
		#Value of RTD
		
		RT = (z*(0.0001875)*(1000))/(y*(0.0001875)-z*(0.0001875))		
		TP = ((RT/1000)-1)/0.00392
		
		#Value of pyranometer
		
		Pyra= (w*(0.0001875))/(0.0002)
		
		#Value of Irradiance Cell
		
		IrraCell = (x*(0.0000078125))/(0.0000829)	
				
		#Writing txt file
		
		#print 'A0 is: ',w,' and A1 is: ',x,' and A2 is: ',y,' and A3 is: ',z
		#print TP
		#print RT
		print Pyra
		print IrraCell
		print degrees
		print humidity
		print "-----------------------------------------------------"
		name = 'Tesis.txt'
		f = open(name,'a')
		f.write('T: ')
		f.write('{0:0.3f}'.format(degrees))
		f.write(' H: ')
		f.write('{0:0.3f}'.format(humidity))
		f.write(' Pyra: ')
		f.write('{0:0.3f}'.format(Pyra)) #Pyranometer
		f.write(' IC: ')
		f.write('{0:0.3f}'.format(IrraCell)) #Irradiance Cell
		f.write(' TP ')
		f.write('{0:0.3f}'.format(TP)) #RTD
		f.write(' Date: ')
		f.write(str(datetime.now()))
		f.write('\n')
		f.close()
