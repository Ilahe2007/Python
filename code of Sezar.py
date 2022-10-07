a=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
n=str(input())
b=int(input())
d=[]
n=n.replace('',' ')
n=n.split()
for i in n:
  c=a.index(i)
  d.append(a[c-b])
d=list(map(str,d))
print(''.join(d))
