a=int(input())
a=input().split()[:a]
a=list(map(int,a))
a=list(sorted(a))
a=list(map(str,a))
print(' '.join(a))
