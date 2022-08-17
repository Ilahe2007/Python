a,b,c,d=input().split()
a=int(a)
b=int(b)
c=int(c)
d=int(d)
if a>b and a>c and a>d:
  if b>c and b>d:
    if c>d:
      print(b-c)
    else:
      print(b-d)
  elif c>b and c>d:
    if b>d:
      print(c-b)
    else:
      print(c-d)
  else:
    if b>c:
      print(d-b)
    else:
      print(d-c)
elif b>c and b>a and b>d:
  if c>a and c>d:
    if a>d:
      print(c-a)
    else:
      print(c-d)
  elif a>d and a>c:
    if d>c:
      print(a-d)
    else:
      print(a-c)
  else:
    if a>c:
      print(d-a)
    else:
      print(d-c)
elif c>d and c>b and c>a:
  if d>b and d>a:
    if b>a:
      print(d-b)
    else:
      print(d-a)
  elif b>d and b>a:
    if d>a:
      print(b-d)
    else:
      print(b-a)
  else:
    if a>d and a>b:
      if d>b:
        print(a-d)
      else:
        print(a-b)
else:
  if c>b and c>a:
    if b>a:
      print(c-b)
    else:
      print(c-a)
  elif b>a and b>c:
    if a>c:
      print(b-a)
    else:
      print(b-c)
  else:
    if c>b:
      print(a-c)
    else:
      print(a-b)
