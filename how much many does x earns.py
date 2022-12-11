n=int(input())
f=[]
for i in range(n):
  a,b=input().split()
  a=str(a)
  b=int(b)
  f.append(a)
  f.append(b)
m=int(input())
for j in range(m):
  d=str(input())
  if f.count(d)!=0:
    print(f[f.index(d)+1])
  else:
    print('-1')
