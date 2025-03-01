import numpy as np
from scipy.special import legendre
m=2
n=2
pm=legendre(m)
pn=legendre(n)
f=pm*pn
#calculation of integration and no required no of intervals####
a=-1.0
b=1.0
no_decimal_tol=6
n_ini=10 
int_old=0.0
int_new=0.0
temp_error=1.0
n=n_ini
n_step=10
while True:
      int_old = int_new
      h=float(b-a)/float(n)
      x_e = np.arange(a+2*h,b,2*h)
      x_o = np.arange(a+h,b,2*h)
      integration_value = (h/3.0)*(f(a) + f(b) + 4.0*sum(f(x_o)) + 2.0*sum(f(x_e)))
      int_new=integration_value
      temp_error = abs(float(int_new-int_old))
      if int(temp_error*(10**no_decimal_tol)) == 0:
          break
      n=n+n_step
print('integration_value =',integration_value)
print('no of intervals =',n)      

     