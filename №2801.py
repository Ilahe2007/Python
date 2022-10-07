import math
a,b=map(int,input().split())
a=math.sqrt(a)
if a<b:
  print('-1')
else:
  print((b*2)-1)
