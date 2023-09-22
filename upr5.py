import numpy as np
n, m = input().split()
n=int(n)
m=int(m)
a=np.zeros((n,m))
for i in range(n):
    for j in range(m):
        a[i,j]=