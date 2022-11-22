import math
n=int(input())
i=1
f=1
while i<=n:
  f=f*i
  i=i+1
j=1
g=1
while j<=n-3:
  g=g*j
  j=j+1
print('{:.0f}'.format(f/g))
