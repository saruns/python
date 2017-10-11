import sys
def string(x,y):
 count = 0
 for f in x:
  if f == y:
   count = count + 1
 return count
print "Enter your string"
a = raw_input()
print "Enter your letter to be saerched"
b = raw_input()
print string(a,b)
if __name__ == "__string__":
 string(a,b)
