import math
x,k=map(float,input().split())
c=math.sqrt(abs(x))
a=pow(c,4)+pow(k,3)
y=pow(math.log10(a),3)+pow(math.cos(x),5)
print('{:.2f}'.format(y))
