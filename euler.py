import matplotlib.pyplot as plt
def f(y,t):
    return -k*y
k=0.1
t,y,h=0.0,5.0,0.01  #initial values
Y,T = [],[]
ini_t=0.0  
fin_t=20.0
n=int((fin_t-ini_t)/h)
print('n=',n)
for i in range (n+1):
    y=y+h*f(y,t)
    t=t+h
    Y.append(y)
    T.append(t)
plt.title("Radioactive Decay of an element", size='30')
plt.xlabel("time in min", size='30')
plt.ylabel("y(t)",size='30')  
plt.plot(T,Y,ls= '-', lw=1,color='r',label='$euler$')
plt.legend(loc='best',prop={'size':20})
plt.grid()
plt.show()