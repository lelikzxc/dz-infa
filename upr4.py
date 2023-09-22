import math
size, symb=input().split()
size=int(size)
def tr(a, b):
    for i in range(1, int(math.ceil(a/2)+1)):
        print(b*i)
    for i in range(int(math.ceil(a/2))+1):
        print(b*(int(a/2)-i))
tr(size, symb)