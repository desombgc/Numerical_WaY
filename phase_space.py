import numpy as np
import matplotlib.pyplot as plt
t=float(input("enter the value of time: "))
x=float(input("enter the value of x: "))
z=float(input("enter the value of z: "))
h=float(input("enter the value of h: "))  
ini_time=t
fin_time=float(input("enter the final value of time: "))
n=int((fin_time-ini_time)/h)
def f(t,x,z):
    return z
def g(t,x,z):
    return -((np.pi)**2)*x
#EULER
X,T,Z=[],[],[]
for i in range (n):
    x=x+h*f(t,x,z)
    z=z+h*g(t,x,z)
    t=t+h
    X.append(x)
    Z.append(z) 
    T.append(t)
#RK4
X1,T1,Z1= [],[],[]
for i in range (n):
    a1=h*f(t,x,z) 
    b1=h*g(t,x,z)
    a2=h*f(t+h*0.5,x+a1*0.5,z+b1*0.5)
    b2=h*g(t+h*0.5,x+a1*0.5,z+b1*0.5)
    a3=h*f(t+h*0.5,x+a2*0.5,z+b2*0.5)
    b3=h*g(t+h*0.5,x+a2*0.5,z+b2*0.5)    
    a4=h*f(t+h,x+a3,z+b3)
    b4=h*g(t+h,x+a3,z+b3)
    x=x+((a1+2*a2+2*a3+a4)/6.0)
    z=z+((b1+2*b2+2*b3+b4)/6.0)
    t=t+h
    X1.append(x)
    Z1.append(z)
    T1.append(t)
#ANALYTIC
t=np.linspace(0,10,200)
d=(np.cos(np.pi*t))             #the analytical form of generalised coordinate
g=-(np.pi)*np.sin(np.pi*t)  #the analytical form of generalised momentum 
plt.xlabel("$x$",size=20)
plt.ylabel("$P(x)$",size=20)
plt.title('Phase Space Plot',size=20)
plt.plot(X,Z,color='b',ls='--',lw=0.5,marker='v',ms=2,label="$Euler$")
plt.plot(X1,Z1,color='g',ls='--',lw=1,marker='+',ms=2,label="$RK4$")
plt.plot(d,g,color='r',ls='-',lw=1,marker='*',ms=6,label="$Analytic$")
plt.legend(loc='best',prop={'size':20}) 
plt.show()       