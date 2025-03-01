import numpy as np
from scipy import misc
import matplotlib.pyplot as plt
ini_val=2.0
fin_val=6.0
h=0.5
a=np.arange(ini_val,fin_val+h,h)
t=list(a)
def v(t):
    return 0.3*t**3+5*t
def dv(t):
    return misc.derivative(v,t,n=1)
dvdt=[dv(m) for m in t]
y = [v(m) for m in t]
#print('y=' ,y)
###########FORWARD DIFFERENCE METHOD#############
z=np.copy(y)
f_derivative_t=[]
for i in range (0,len(y)-1):
    sum=0.0
    k=0
    for j in range (len(z),1,-1):
        z=np.diff(z)
        sum=sum+(((-1)**k)*z[0])/(k+1.0)
        k=k+1
    z = y[i+1:len(y)]    
    f_derivative_t.append(sum/h)
    #print('z=' ,z)
#print('f_derivative_t=' ,f_derivative_t)
t_f=t[0:len(t)-1]
#print(x_f)
#############BACKWARD DIFFERENCE METHOD#############
z_b=np.copy(y)
b_derivative_t=[]
n=len(y)-1
for i in range (0,n):
    sum=0.0
    k=0
    for j in range (0,len(z_b)-1): 
        z_b=np.diff(z_b)
        sum=sum+(z_b[len(z_b)-1])/(k+1.0)
        k=k+1
    z_b = y[0:n-i]
    b_derivative_t.append(sum/h)
#print('b_derivative_t=' ,b_derivative_t)
t_r=t[1:len(t)]
t_r.reverse()
t_b=t_r
################PLOTTING#################
plt.plot(t,y,marker='o',ms=6,mfc='b',ls='-',lw=3,color='r',label='$v(t)$')
plt.plot(t,dvdt,marker='*',ms=6,mfc='g',ls=':',lw=3,color='k',label="$v'(t)misc$")
plt.plot(t_f,f_derivative_t,marker='d',ms=6,mfc='g',ls='-.',lw=3,color='r',label= "$v'(t)FW$" )
plt.plot(t_b,b_derivative_t,marker='x',ms=6,mfc='m',ls='--',lw=3,color='b',label="$v'(t)BW$")         
plt.xlabel('time in sec',size=20)
plt.ylabel('velocity in m/s' ,size=20)
plt.title('derivative of v(t) = 0.3*t**3+5*t ' , size=20)
plt.xlim(0,7)
plt.ylim(0,100)
plt.legend(loc='best')
plt.grid()
plt.show()
#plt.savefig('velocity_acceleration.png')


