string=input()
f={}
for element in string:
    if element in f:
        f[element]+=1
    else:
        f[element]=1
u=[]
for element in f:
    if f[element]==1:
        u.append(element)
print(u)