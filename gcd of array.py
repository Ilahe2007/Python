from functools import reduce
import math
def gcd(a,b):
  return math.gcd(a,b)
a=int(input())
n=[int(i) for i in input().split()]
r=reduce(gcd,n)
print(r)
