a=1
b=1
while a!=' ' and b!=' ':
  try:
    a,b=map(int,input().split())
    print(a*b)
  except:
    break
