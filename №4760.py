n=int(input())
a=input().split()[:n]
a=list(a)
b=list(filter(lambda x: int(x)>0 or int(x)<0,a))
c=list(filter(lambda x: int(x)==0,a))
print(' '.join(b+c))
