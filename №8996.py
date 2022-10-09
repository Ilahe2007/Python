a=str(input())
b=[]
for i in a:
  if b.count(i)==0:
    b.append(i)
print(''.join(b))
