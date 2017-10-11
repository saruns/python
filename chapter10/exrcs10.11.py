import sys
def indexlst(x,y):
 b = []
 if y not in x:
  print "none"
 else: 
  for f in x:
   if f == y:
    b.append(str(x.index(f)))
    print b
a = []
a = raw_input("enter the string : ")
c = raw_input("enter the element to be searched  ")
print indexlst(a,c)
if __name__ == "__indexlst":
 indexlst(a,c)
