N=input()
n=N.count('0')
if int(N)!=0:
  if (int(N[0])==1 and n==len(N)-1 and int(N)%10==0) or (int(N)==1):
    print(n)
  else:
    print('No')
