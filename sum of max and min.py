a=input()
a=list(a)
b=list(sorted(a))
c=list(reversed(b))
d=''.join(b)
e=''.join(c)
d=int(d)
e=int(e)
if (d//100)%10!=0:
  print(d+e)
else:
  if (d//10)%10!=0:
    g=(d//100)%10
    m=(d//10)%10
    n=d%10
    print(int((str(m)+str(g)+str(n)))+e)
