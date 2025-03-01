import numpy as np
x=np.linspace(0,1,1001)
y=1/(1+x**2)
h=x[1]-x[0]
I=h/3*(y[0]+y[len(y)-1]+4*sum(y[1:len(y)-1:2])+2*sum(y[2:len(y)-2:2]))
print('Value of the Integral= ' , I )
