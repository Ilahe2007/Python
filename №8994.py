a=str(input())
b=str(input())
a=list(a)
b=list(b)
c=[]
for i in b:
  if i in a:
    c.append('Ok')
  else:
    c.append('No')
if len(set(c))==1:
  print(c[0])
else:
  print("No")
