def f(x):
  if x<2:
    return 1;
  else:
    return x*f(x-2)
x=int(input())
f=f(x)
b=0
while f%10==0:
  f=f//10
  b=b+1
print(b)
