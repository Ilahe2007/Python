n=1
while n!=' ':
  try:
    n=int(input())
    n=str(bin(n))
    n=list(n)
    del n[1]
    del n[0]
    print(''.join(n))
  except:
    break
