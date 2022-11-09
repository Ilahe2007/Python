import math
a=int(input())
b=True
if a==1:
  print("No")
elif a==2:
  print('Yes')
else:
  for i in range(2,int('{:.0f}'.format(math.sqrt(a)))):
    if a%i==0:
      print('No')
      b=False
      break
if b==True:
  print('Yes')
