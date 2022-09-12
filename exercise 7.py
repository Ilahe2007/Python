n=int(input())
b=[]
for i in range(n+1,n+100):
  i=str(i)
  if len(i)==len(set(i)):
    b.append(i)
print(b[0])
