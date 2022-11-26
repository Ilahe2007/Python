a=str(input())
b,c=map(int,input().split())
d=(-c)/b
if c!=0:
  if b>0:
    if a=='>':
      print('('+'{:.0f}'.format(d)+';+i)')
    elif a=='<':
      print('(-i;'+'{:.0f}'.format(d)+')')
    elif a=='>=':
      print('['+'{:.0f}'.format(d)+';+i)')
    else:
      print('(-i;'+'{:.0f}'.format(d)+']')
  else:
    if a=='<':
      print('('+'{:.0f}'.format(d)+';+i)')
    elif a=='>':
      print('(-i;'+'{:.0f}'.format(d)+')')
    elif a=='<=':
      print('['+'{:.0f}'.format(d)+';+i)')
    else:
      print('(-i;'+'{:.0f}'.format(d)+']')
else:
  if b>0:
    if a=='>':
      print('('+'{:.0f}'.format(-d)+';+i)')
    elif a=='<':
      print('(-i;'+'{:.0f}'.format(-d)+')')
    elif a=='>=':
      print('['+'{:.0f}'.format(-d)+';+i)')
    else:
      print('(-i;'+'{:.0f}'.format(-d)+']')
  else:
    if a=='<':
      print('('+'{:.0f}'.format(-d)+';+i)')
    elif a=='>':
      print('(-i;'+'{:.0f}'.format(-d)+')')
    elif a=='<=':
      print('['+'{:.0f}'.format(-d)+';+i)')
    else:
      print('(-i;'+'{:.0f}'.format(-d)+']')
