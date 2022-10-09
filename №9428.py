from fractions import Fraction
a,b=map(str,input().split())
x=a.replace('/',' ')
x=x.split()
x=list(map(int,x))
y=b.replace('/',' ')
y=y.split()
y=list(map(int,y))
x=Fraction(x[0],x[1])
y=Fraction(y[0],y[1])
if x>y:
  print(b,a)
else:
  print(a,b)
