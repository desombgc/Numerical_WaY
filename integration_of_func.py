import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
def f(t):
    return 5*np.cos(t)

a=0.0
b=2*(np.pi)
no_decimal_tol=6
b_interval=0.05
no_of_loop=int(float(b-a)/float(b_interval))+1
trap_integral=[]
sim_integral=[]
quad_integral=[]
t_val=[]
b1=a
a1=a-b_interval
for i in range (no_of_loop):
    #print(b1)    
    t_val.append(b1)
    #print(t_val)
    ##integration by trapezoidal rule#####
    trap_n_ini=10
    int_old=0.0
    int_new=0.0
    temp_error=1.0
    n=trap_n_ini
    n_step=10

    while True:
        int_old=int_new
        h=float(b1-a1)/float(n)
        #print(h)
        t_all=np.arange(a1,b1+h,h)
        #print(t_all)
        trap_value=h*(sum(f(t_all))-(f(a1)+f(b1))/2.0)
        #print(trap_value)
        int_new=trap_value
        temp_error=abs(float(int_new-int_old))
        if int(temp_error*(10**no_decimal_tol))==0:
            break
        n=n+n_step
    #print(n)
    trap_integral.append(trap_value)

    ##integration by simpson 1/3 rule######
    sim_n_ini=10
    int_old=0.0
    int_new=0.0
    temp_error=1.0
    n=sim_n_ini
    n_step=10

    while True:
        int_old=int_new
        h=float(b1-a1)/float(n)
        t_e=np.arange(a1+2*h,b1,2*h)
        t_o=np.arange(a1+h,b1,2*h)
        sim_int_value=(h/3.0)*(f(a1)+f(b1)+4.0*sum(f(t_o))+2.0*sum(f(t_e)))
        int_new=sim_int_value
        temp_error=abs(float(int_new-int_old))
        if int(temp_error*(10**no_decimal_tol))==0:
            break
        n=n+n_step
    sim_integral.append(sim_int_value)
    ##integration by quad#########
    temp=quad(f,a1,b1)
    quad_int_value=temp[0]
    quad_integral.append(quad_int_value)
    b1=b1+b_interval
y_val=[f(z) for z in t_val]
plt.title('Integration of f(t)=5*np.cos(t)',size=30)
plt.xlabel('time in sec',size=30)
plt.ylabel('current in amp',size=30)
plt.xlim(0,7)
plt.ylim(-8,8)
plt.text(3,4,'$\int f(t)dt = {\Psi}(t)+c =\Phi(t)$',size=30)
plt.plot(t_val,y_val,marker ='o',ms=3,mfc='b', ls='-',lw=3,color='r',label='$f(t)$')
plt.plot(t_val,trap_integral,marker='v',ms=3, mfc='r',ls='-.',lw=1,color='b',label='${\Phi}_{Trapz}(t)$')
plt.plot(t_val,sim_integral,marker='+',ms=3, mfc='k',ls=':',lw=1,color='g',label='${\Phi}_{Sim}(t)$')
plt.plot(t_val,quad_integral,marker='*',ms=3, mfc='g',ls='--',lw=1,color='k',label='${\Phi}_{quad}(t)$')
plt.legend(loc='best',prop={'size':20})
plt.grid()
plt.show()
#plt.savefig('charge.png')


        
