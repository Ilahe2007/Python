n=int(input())
a1,b1=input().split()[:n]
a2,b2=input().split()[:n]
a3,b3=input().split()[:n]
if float(b1)<50:
  print(float(a1))
elif float(b1)<50 and float(b2)<50:
  print(int(a1)+int(a2))
elif float(b1)<50 and float(b2)<50 and float(b3)<50:
  print(int(a1)+int(a2)+int(a3))
elif float(b2)<50 and float(b3)<50:
  print(int(a2)+int(a3))
elif float(b1)<50 and float(b3)<50:
  print(int(a1)+int(a3))
