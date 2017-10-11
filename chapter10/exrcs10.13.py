import sys
def interlock(x,y):
 z = []
 n = 0
 m = 0
 for i in x:
  z.append(i)
  for j in y[m:]:
   if n == 0:
    z.append(j)
    n = n + 1
  n = n - 1
  m = m + 1
 print ''.join(z)
a = raw_input("enter the 1st string: ")
a = list(a)
b = raw_input("enter the 2nd string: ")
b = list(b)
interlock(a,b)
