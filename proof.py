import numpy as np
import matplotlib.pyplot as plt

def h( x ):
    result = np.sin(x)+10
    return result

steps=1000
le=150*3.14159
xarray = np.linspace( 0,le,steps )
harray = h( xarray )
qrray=[]
i=1
qrray.append(harray[0])
while i<steps:
    try:
        perc=(harray[i]-harray[i-1])/harray[i-1]
        lev=3*perc
        res=(1+lev)*qrray[i-1]
        qrray.append(res)
    except ZeroDivisionError:
        qrray.append(qrray[i-1])
    i+=1

frray=[]
i=1
frray.append(harray[0])
while i<steps:
    try:
        perc=(harray[i]-harray[i-1])/harray[i-1]
        lev=2*perc
        res=(1+lev)*frray[i-1]
        frray.append(res)
    except ZeroDivisionError:
        frray.append(qrray[i-1])
    i+=1





flat= np.linspace(10,10,steps)
#plotting
plt.plot( xarray,harray,'b-', label='Underlying' )
plt.plot(xarray,frray,'g-')
plt.plot(xarray,qrray,'r-', label='3x Leverage')
plt.plot(xarray,flat,'k-')
#plt.legend(loc='upper right')
plt.xlabel( 'Time' )
plt.ylabel( 'Value' )
plt.title( 'Simulated Beta Slippage' )
plt.xlim( 0,le )
plt.show() 
