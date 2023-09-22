a, b = input().split()
a=int(a)
b=int(b)
def nod(x,y):
    s=x
    w=y
    while x!=0 and y!=0:
        if x>y:
            x=x-y
        else:
            y=y-x
    d=x+y
    ai=100
    bj=100
    for i in range(-100, 100):
        for j in range(-100, 100):
            if i*s+j*w==d:
                if (abs(ai)>abs(i)) and (abs(bj)>abs(j)):
                    ai=i
                    bj=j
    print(ai, bj, d)

nod(a,b)