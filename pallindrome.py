x=input('Enter your input')
'''l=len(x)
for j in range(0,l):
 if x[j]==x[l-j-1]:
  print('YES')
 else:
  print('NO')'''
if x==x[::-1]:
 print('YES')
else : print('NO')
