n=int(input())
a=input().split()[:n]
n=n/2
b=[]
for i in a:
  if a.count(i)>n:
    b.append(i)
if len(b)==0:
  print('-1')
else:
  b=list(set(b))
  print(' '.join(b))
