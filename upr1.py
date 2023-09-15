A=list(map(int, input().split()))
s=0
n=A[0]
s1=0
for i in range(n):
    s+=A[i]
s-=A[0]
for i in range(n+1):
    s1+=i
print(s1-s)
