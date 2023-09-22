def mnk(x, y):
    if len(x)!=len(y):
        return None
    x_mean=sum(x)/len(x)
    y_mean=sum(y)/len(y)
    numerator=0
    denominator=0
    for i in range(len(x)):
        numerator+=(x[i]-x_mean)*(y[i]-y_mean)
        denominator+=(x[i]-x_mean)**2
        a=numerator/denominator
        b=y_mean-a*x_mean
        return a, b
x=list(map(float, input().split()))
y=list(map(float, input().split()))
a, b=mnk(x, y)
print(a,b)
