import numpy as np
import matplotlib.pyplot as plt
x=float(input("enter the value of y0: "))
previous_step_size=0.1
h=(previous_step_size)/5.0
ini_time=float(input("enter the initial value of x0: "))
fin_time=float(input("enter the final value of x: "))
n=int((fin_time-ini_time)/h)
X,X1,X2,T,T1,T2= [],[],[],[],[],[]
def f(t):
    return np.cos(np.pi*t)
#EULER 
t=ini_time    
for i in range (n):
    x=x+h*f(t)
    t=t+h
    X.append(x)
    T.append(t)
#RK2
t1=ini_time
for i in range (n):
    k1=h*f(t1)
    k2=h*f(t1+h)
    x=x+(k1+k2)/2
    t1=t1+h
    X1.append(x)
    T1.append(t1)  
#RK4
t2=ini_time
for i in range (n):
    k1=h*f(t2)
    k2=h*f(t2+h*0.5)
    k3=h*f(t2+h*0.5)
    k4=h*f(t2+h)
    x=x+((k1+2*k2+2*k3+k4)/6.0)
    t2=t2+h
    X2.append(x)
    T2.append(t2)
#plotting    
plt.xlabel('$t$',size=30)
plt.ylabel('$x$',size=30)
plt.title("Numerical Solution",size=20)
plt.plot(T,X,color='r',ls='-',lw=1,label='$Euler$')
plt.plot(T1,X1,marker='.',ms=3,mfc='r',color='b',ls='--',lw=1,label='$RK2$')
plt.plot(T2,X2,marker='*',ms=6,mfc='k',color='c',ls=':',lw=1,label='$RK4$')
plt.legend(loc='upper right',prop ={'size': 20})
plt.grid()
plt.show()  
    