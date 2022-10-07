n=str(input())
for i in n:
  try:
    i=int(i)
    if i!=9:
      print(i+1,end='')
    else:
      print('0',end='')
  except:
    print(i,end='')
print()
