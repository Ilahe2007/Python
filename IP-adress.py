n=str(input())
n=n.replace('.',' ')
n=n.split()
a=0
n=list(map(int,n))
for i in n:
  if i>=0 and i<=255:
     a=a+1
  else:
    a=a
if a==4:
  print('1')
else:
  print('0')
