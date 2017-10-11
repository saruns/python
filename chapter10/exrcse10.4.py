import sys
def middle(x):
 print "middle list is",x[1:-1]
n = input("enter the no elements  ")
if n == 1:
 print "enter your string"
 s = raw_input()
 b = list(s)
 print "your middle string is",b[1:-1]
else: 
 print "enter the elements"
 a = [0 for i in range(n)]
 for i in range(n):
  a[i] = raw_input()
 print "your list is",a
 middle(a)
if __name__ == "__middle__":
 middle(a)
