import numpy as np
x=np.linspace(0,1,1001)
y=1/(1+x**2)
h=x[1]-x[0]
#print(y[0])
I= 0.5*h*(y[0]+y[len(y)-1]+2*sum(y[1:len(y)-1]))
print('Value of the Integral= ' , I )
