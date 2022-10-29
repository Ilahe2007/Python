n=int(input())
for i in range(n):
  c=0
  d=0
  a=str(input())
  for i in a:
    if i=='<':
      c=c-1
    elif i==">":
      c=c+1
    elif i=="^":
      d=d+1
    else:
      d=d-1
  print(c,d)
