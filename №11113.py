N,M=map(int,input().split())
if N==0 or M==0:
  print('0')
elif (N==1 and M>=2) or (N>=2 and M==1):
  print('1')
elif N*2<M:
  if N<M:
    print(abs(N))
  else:
    print(abs(M))
elif M*2<N:
  if N>M:
    print(abs(M))
  else:
    print(abs(N))
else:
  print('{:.0f}'.format((N+M)//3))
