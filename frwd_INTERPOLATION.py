x=[2.00,10.00,18.00,26.00,32.00,40.00]
y=[1.26,2.15,2.62,2.96,3.17,3.42]
z=[]
x_val=8
h=8.0
t=float(x_val-x[0])/float(h)
coeff=t
sum=y[0]
k=1
for i in range (len(y),1,-1):
    for j in range(i-1):
        diff=y[j+1]-y[j]
        z.append(diff)
    sum=sum + coeff*z[0]
    coeff= coeff*(t-k)/(k+1)
    k=k+1
    y=z
    z=[]
print('interpolated value=', sum)

##############ploting############
import matplotlib.pyplot as plt
x=[2.00,10.00,18.00,26.00,32.00,40.00]
y=[1.26,2.15,2.62,2.96,3.17,3.42]
x_interpole=[8.0]
y_interpole=[sum]

plt.plot(x,y, color='r',ls='-',lw=2, marker='s',ms=6,mfc='b')
plt.plot(x_interpole,y_interpole, marker='o',ms=6,mfc='g')
plt.show()
