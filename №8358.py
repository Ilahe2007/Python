b=1
d=[]
e=[]
f=0
while b!=" ":
  try:
    b=str(input())
    c=b.split()
    c=str(' '.join(c))
    d.append(c)
  except:
    break
d=str(' '.join(d))
d=d.split()
d=list(map(int,d))
a=max(d)
b=min(d)
print('{:.0f}'.format((sum(d)-a*d.count(a)-b*d.count(b))/(len(d)-d.count(a)-d.count(b))))
