a=int(input())
b=[]
if a>0:
  while a!=0:
    a=int(input())
    b.append(a)
    c=list(map(str,b))
    c=list(filter( lambda x: int(x)<0,c))
  print(len(c))
else:
  while a!=0:
    a=int(input())
    b.append(a)
    c=list(map(str,b))
    c=list(filter( lambda x: int(x)<0,c))
  print(len(c)+1)
