a=str(input())
b=[]
d=[]
e=[]
#How many elements are repeated in the string
for i in a:
  if a.count(i)>=2:
    if b.count(i)==0:
      b.append(i)
      c=a.count(i)
      d.append(c)
try:
  f=list(filter(lambda x: a.count(x)==max(d),a))
  for j in f:
    if e.count(j)==0:
      e.append(j)
  print((max(d)))
  print(' '.join(e))
except:
  print('1')
  print(' '.join(a))
