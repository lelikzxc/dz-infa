a = list(map(str, input().split()))

def bm(a, b):
    if a==b:
        return 0
    elif a.startswith(b):
        return bm(a[len(b):],b)
    elif b.startswith(a):
        return bm(a, b[len(a):])
    else:
        return -1 if a<b else 1
def max_nums(s):
    num=s
    num.sort(key=lambda x:x, reverse=True, cmp=bm)
    return "".join(num)

print(max_nums(a))