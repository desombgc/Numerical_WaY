import numpy as np
a=np.array([[1,2,4],[7,8,1],[2,1,6]], dtype=float)
b=np.array([2,8,7],dtype=float)
n=len(a)     #number of rows
B=b.reshape(n,1)
C=np.hstack((a,B))   #augmented matrix
for i in range (n):
    if a[i,i]==0:
        print("Solution cannot be obtained")
        exit()
r=len(C)          #number of rows
for k in range (r-1):
    for j in range(k+1,r):
        f=C[j,k]/C[k,k]
        C[j]=C[j]-f*C[k] 
#print(C)        #triangular matrix[lower triangular elements are zero]
s=np.ones(r)       #guess solution
det=1.0
for i in range (r-1,-1,-1):
    temp=0.0
    for j in range(i+1,r):
        temp=temp+s[j]*C[i,j]
    C[i,r]=C[i,r]-temp
    s[i]=C[i,r]/C[i,i]
    det=float(det*C[i,i])     
    print("The unknown variables are:C{}={}".format(i+1,s[i]))
print("the determinant of matrix 'a'is : ",det)