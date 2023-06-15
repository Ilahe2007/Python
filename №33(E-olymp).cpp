import math
def f(n):
    a=True
    for i in range(2,int('{:.0f}'.format(math.sqrt(n)))+1):
        if(n%i==0):
            a=False
            break
    return a
a,b=map(int,input().split())
c=0
for i in range(a,b+1):
    d=str(i)
    if(f(i)==True and d.find('13')==-1 and i!=1):
        c=c+1
print(c)
