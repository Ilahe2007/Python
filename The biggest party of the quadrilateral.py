import math
x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
a1=math.sqrt((x2-x1)**2+(y2-y1)**2)
a2=math.sqrt((x4-x1)**2+(y4-y1)**2)
a4=math.sqrt((x3-x2)**2+(y3-y2)**2)
a6=math.sqrt((x4-x3)**2+(y4-y3)**2)
print('{:.2f}'.format(max(a1,a2,a4,a6)))
