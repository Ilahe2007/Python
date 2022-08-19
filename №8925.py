from functools import reduce
a=input()
b=list(a)
n=list(filter(lambda x:int(x)%2!=0,b))
if len(n)!=0:
  print(''.join(n))
else:
  print('0')
