def GCD(x,y):
  r=x%y
  if r==0:
    return y
  else:
    return GCD(y,r)
n,m=input().split()
n=int(n)
m=int(m)
a=GCD(m,n)
print((n*m)//a)
