n=int(input())
b=[]
for i in range(n):
  a=int(input())
  b.append(a)
  c=list(map(str,b[::-1]))
print(' '.join(c))
