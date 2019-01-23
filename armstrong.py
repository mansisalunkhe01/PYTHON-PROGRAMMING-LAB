x=input('enter a number')
l=len(x)
s=0
for j in range (0,l):
 s+=int(x[j])**l
if int(x)==s:
 print('Armstrong')
else:
 print('Not Armstrong')
