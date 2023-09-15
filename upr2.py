a=list(map(str, input().split()))
s=int(a[0])
b=a[1]
d=[]
group_lenght=len(b)//s
result=[]
for i in range(0, len(b), group_lenght):
    result.append(b[i:i+group_lenght])
result=["".join(reversed(group)) for group in result]
r=''.join(result)
print(r)