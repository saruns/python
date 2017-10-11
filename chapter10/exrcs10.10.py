import sys
def flist(x):
 b = []
 for f in open(x):
   b = b + [f]
 print b
flist('output.txt')
if __name__ == "__flist__":
 flist('output.txt')
