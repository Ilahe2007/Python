a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a==b and b==c:
    print("(equilateral")
elif a==b and a!=c:
    print("isosceles")
elif a==c and a!=b:
    print("isosceles")
elif b==c and b!=a:
    print("isosceles")
else:
    print("scalene")
