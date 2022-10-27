n=int(input())
for i in range(n):
  a=int(input())
  c=0
  d=0
  for i in range(a):
    m,n=map(str,input().split())
    if m==n:
      c=c+0
      d=d+0
    elif (m=='R' and  n=='S') or (m=='S' and  n=='P') or (m=='P' and  n=='R'):
      c=c+1
      d=d+0
    else:
      d=d+1
      c=c+0
  if c>d:
    print("Player 1")
  elif c<d:
    print("Player 2")
  else:
    print('TIE')
