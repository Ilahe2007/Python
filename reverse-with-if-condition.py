a=list(input())
if a[0]=='-':
  del a[0]
  a=list(map(int,a))
  a=list(reversed(a))
  if a[0]==0:
    if a[1]==0:
      if a[2]==0:
        if a[3]==0:
          print(-a[4])
        else:
          print(-int(str(a[3])+str(a[4])))
      else:
        print(-int(str(a[2])+str(a[3])+str(a[4])))
    else:
      print(-int(str(a[1])+str(a[2])+str(a[3])+str(a[4])))
  else:
    print(-int(str(a[0])+str(a[1])+str(a[2])+str(a[3])+str(a[4])))
else:
  if a[0]==0:
    if a[1]==0:
      if a[2]==0:
        if a[3]==0:
          print(a[4])
        else:
          print(str(a[3])+str(a[4]))
      else:
        print(str(a[2])+str(a[3])+str(a[4]))
    else:
      print(str(a[1])+str(a[2])+str(a[3])+str(a[4]))
  else:
    print(str(a[0])+str(a[1])+str(a[2])+str(a[3])+str(a[4]))
