n,k=map(int,input().split())
for i in range(k):
  n=list(sorted(str(n),reverse=True))
  a=list(reversed(n))
  n=int(''.join(n))
  a=int(''.join(a))
  n=n-a
print(n)
