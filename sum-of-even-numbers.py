from functools import reduce
n=input()
n=list(n)
n=list(map(int,n))
b=list(filter(lambda x: x%2==0,n))
if len(b)!=0:
  c=reduce(lambda x,y: x+y,b)
  print(c)
else:
  print('0')
