a=int(input())
c=0
for i in range(a):
    b=str(input())
    b=b.replace('',' ')
    b=b.split()
    for i in b:
        if i=='A':
            c+=4
        elif i=='J':
            c+=1
        elif i=='Q':
            c+=2
        elif i=='X':
            c+=0
        else:
            c+=3
print(c)
