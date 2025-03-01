import numpy as np
import matplotlib.pyplot as plt
x=[1000,1200,1400,1600,1800,2000,2200]
y=[1.31,1.63,1.97,2.33,2.69,3.05,3.47]
x_val=1100
h=200.0
z=np.copy(y)
#print(z)
t=float(x_val-x[0])/float(h)
coeff=t        
sum=z[0]
k=1

for i in range (len(z),1,-1):
        z=np.diff(z)
        #print(z)
        sum = sum + t*z[0]
        coeff=coeff*(t-k)/(k+1)
        k=k+1

print('Interpolated value at the point x=1100 is =' ,sum)        
x_interpole=1100
y_interpole=sum
plt.xlim(800,2400)
plt.ylim(1,4.00)
plt.plot(x,y, color='r',ls='-',lw=2,marker='^',ms=6,mfc='b',label='$Given Data Points$')
plt.plot(x_interpole,y_interpole,marker='D',ms=6,mfc='g',label='$Interpolated Point$')
plt.xlabel('Temperature in K ',size=20)
plt.ylabel('Rt/Rd',size=20)
plt.title('Plot of data points and interpolated point',size=20)
plt.legend(loc='best',prop={'size':15})
plt.show()
#plt.savefig('Stefan_Law_graph.png')
